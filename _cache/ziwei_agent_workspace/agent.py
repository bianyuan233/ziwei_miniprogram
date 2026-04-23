import json
import os
import logging
import asyncio
from datetime import datetime
from typing_extensions import TypedDict, Annotated
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain.messages import SystemMessage, HumanMessage, ToolMessage, AnyMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.runnables import RunnableConfig
from rule_const import JIANKANG_LOC_RULE, JIANKANG_PRE_RULE
from rule_engine import RuleEngine
from ziwei_person import Person

# 统一日志模块
from utils.logger import get_agent_logger

# 1. 第三方库日志配置（保留）
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

pwd = os.path.dirname(__file__)

# 初始化 agent 日志器
LOG_DIR = os.path.join(pwd, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
agent_logger = get_agent_logger(LOG_DIR)

# 2. 环境变量与全局配置
minimax_api_key = 'sk-cp-eUTDFfHYTrgPYhyFMpzFe60bklqgaE2qQ7En2KAcZX8S0bR0XXaxBr2TvnxzKE63vmnkmpylJW2f4zSFa2-uYCF5UWf39LQxSNKZRDnmuB8CrHhE5smstQs'
pre_path = os.path.join(pwd, 'sandbox_space')
os.environ["ANTHROPIC_BASE_URL"] = "https://api.minimaxi.com/anthropic"
os.environ["ANTHROPIC_API_KEY"] = minimax_api_key

# 3. 状态定义
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    llm_calls: int
    sender: str
    fate_file: str

class ExecutorState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    task_instructions: dict

# 4. 工具定义
async def get_ziwei_person(fate_file):
    person = None
    if os.path.exists(fate_file):
        with open(fate_file, 'r', encoding='utf8') as f:
            ziwei_json = json.load(f)
        person = Person(ziwei_json)
    return person

@tool
def age_year_converter(
    birth_year: int,
    target_age: int = -1,
    target_year: int = -1
):
    """年龄和年份换算工具

    Args:
        birth_year (int): 出生年份
        target_age (int): 要查询的年龄（虚岁，出生时为1岁），与target_year二选一
        target_year (int): 要查询的年份，与target_age二选一，两者都有时以target_year为准

    Returns:
        dict: 包含换算结果，{"year": int, "age": int}
    """
    if target_year != -1:
        age = target_year - birth_year + 1
        return {"year": target_year, "age": age}
    elif target_age != -1:
        year = birth_year + target_age - 1
        return {"year": year, "age": target_age}
    else:
        return {"year": -1, "age": -1}

@tool
async def health_fate(
    start_year: int = 0,
    end_year: int = 0,
    month: int = 0,
    config: RunnableConfig = None
):
    """获取命主在健康方面的运势

    Args:
        start_year (int): 起始年份（包含），0表示从用户出生年份开始
        end_year (int): 结束年份（包含），0表示到用户100岁那年
        month (int): 要查看健康运势的对应月份，1代表一月，2代表二月，以此类推，0表示全年
        config (RunnableConfig): 运行时配置，包含 ziwei_json 数据

    Returns:
        str: 命主在对应时期的健康运势，按年分组，这个是工具调用的结果不应该给用户看到，需要你在这个结果的基础上润色，以用户更能接受的方式说明运势结果
    """
    fate_file = config.get("configurable", {}).get("fate_file") if config else None
    if not fate_file:
        agent_logger.warning("health_fate 未找到 fate_file")
        return '无法获取命盘数据'
    ziwei_person = await get_ziwei_person(fate_file)
    birth_year = 0

    try:
        birth_year = int(ziwei_person.info.get('出生日期（阳历）').split('-')[0])
    except Exception as e:
        agent_logger.error(f"解析出生日期失败: {e}", exc_info=True)
        return '无法获取出生日期'
    if start_year == 0:
        start_year = birth_year
    if end_year == 0:
        end_year = birth_year + 99

    agent_logger.debug(f"健康运势分析: {start_year}-{end_year}, month={month}")

    results = {}
    for year in range(start_year, end_year + 1):
        age = year - birth_year + 1
        rule_engine = RuleEngine(ziwei_person, year=year, age=age, month=month)

        pre_rule_lst = []
        loc_rule_lst = []
        for rule in JIANKANG_PRE_RULE:
            if rule_engine.exctract_rule(rule['rule']):
                pre_rule_lst.append({
                    'index': rule['index'],
                    '判断依据': rule['reason'],
                    '应验事项和可能性分数': rule['result'],
                    '建议': rule['solution']
                })
        if len(pre_rule_lst) > 0:
            for rule in JIANKANG_LOC_RULE:
                if rule_engine.exctract_rule(rule['rule']):
                    loc_rule_lst.append({
                        'index': rule['index'],
                        '判断依据': rule['reason'],
                        '前提条件': rule['premise'],
                        '应验事项和定位准确性分数': rule['result'],
                        '建议': rule['solution']
                    })

        if len(pre_rule_lst) > 0 and len(loc_rule_lst) > 0:
            results[str(year)] = {"status": "注意", "details": {"大运分析": pre_rule_lst, "流年定位": loc_rule_lst}}
        else:
            results[str(year)] = {"status": "平稳", "details": []}

    return str(results)

# 5. 模型与逻辑节点
model = ChatAnthropic(model="MiniMax-M2.7")
tools = [health_fate, age_year_converter]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

async def fate_agent(state: MessagesState):
    # 从 state 中获取命盘信息，构建 system prompt
    agent_logger.info(f"进入 fate_agent 节点，messages 数量: {len(state.get('messages', []))}")
    now = datetime.now().strftime('%Y-%m-%d')
    system_content = f'当前日期：{now}\n'
    if state.get("fate_file"):
        person = await get_ziwei_person(state.get("fate_file"))
        system_content += f"我的基本信息：{person.describe_info()}"
        agent_logger.info(f"已加载命盘文件: {state.get('fate_file')}")
    else:
        agent_logger.warning("未找到 fate_file")
    response = await model_with_tools.ainvoke(
        [SystemMessage(content=system_content)] + state["messages"]
    )
    agent_logger.info(f"LLM 响应: {response.content[:200] if response.content else 'None'}...")
    return {"messages": [response], "llm_calls": state.get('llm_calls', 0) + 1, "sender": "fate_agent"}

async def tool_node(state: dict):
    agent_logger.info("进入 tool_node 节点")
    result = []
    tool_calls = state["messages"][-1].tool_calls
    agent_logger.debug(f"工具调用数量: {len(tool_calls)}")
    for tool_call in tool_calls:
        tool_obj = tools_by_name[tool_call["name"]]
        agent_logger.debug(f"执行工具: {tool_call['name']}, 参数: {tool_call.get('args')}")
        observation = await tool_obj.ainvoke(
            tool_call["args"],
            config={"configurable": {"fate_file": state.get("fate_file")}}
        )
        agent_logger.debug(f"工具 {tool_call['name']} 返回结果长度: {len(observation) if observation else 0}")
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

# 6. 图构建逻辑
def should_continue_fate_agent(state: MessagesState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tool_node"
    return END


def get_agent_builder():

    # --- 构建主工作流 ---
    agent_builder = StateGraph(MessagesState)
    agent_builder.add_node("fate_agent", fate_agent)
    agent_builder.add_node("tool_node", tool_node)
    agent_builder.add_edge(START, "fate_agent")
    agent_builder.add_conditional_edges("fate_agent", should_continue_fate_agent)
    agent_builder.add_edge("tool_node", "fate_agent")

    return agent_builder
