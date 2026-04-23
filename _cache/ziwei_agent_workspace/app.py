import json
import os
import traceback
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from langchain.messages import HumanMessage
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

# 从 agent.py 导入逻辑
from agent import get_agent_builder, pre_path, pwd
from ziwei_person import Person

# 统一日志模块
from utils.logger import get_global_logger, get_app_logger, log_to_session

# 全局日志目录
LOG_DIR = os.path.join(pwd, "logs")
os.makedirs(LOG_DIR, exist_ok=True)


class GenFateRequest(BaseModel):
    user_id: str
    session_id: str
    user_fate: dict

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    message: str

class HistoryRequest(BaseModel):
    user_id: str
    session_id: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 【启动阶段】
    db_path = os.path.join(pwd, "database", "chat.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    agent_builder = get_agent_builder()

    async with AsyncSqliteSaver.from_conn_string(db_path) as memory:
        app.state.agent = agent_builder.compile(checkpointer=memory)
        app_logger = get_app_logger(LOG_DIR)
        app_logger.info(f"Agent 已使用异步 SQLite 编译完成，数据库：{db_path}")
        yield
        app_logger.info("正在关闭异步数据库连接...")

app = FastAPI(title="Ziwei", lifespan=lifespan)

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求追踪中间件
@app.middleware("http")
async def log_requests(request: Request, call_next):
    path = request.url.path
    method = request.method
    global_logger = get_global_logger(LOG_DIR)
    global_logger.info(f"请求开始: {method} {path}")
    try:
        response = await call_next(request)
        global_logger.info(f"请求完成: {method} {path} - {response.status_code}")
        return response
    except Exception as e:
        global_logger.error(f"请求异常: {method} {path} - {e}", exc_info=True)
        raise

# FastAPI 全局异常处理器
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    global_logger = get_global_logger(LOG_DIR)
    global_logger.error(f"API 全局异常: {request.url.path} - {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": str(exc), "type": type(exc).__name__}
    )

@app.post("/chat/gen_fate")
async def chat_gen_fate(request: GenFateRequest):
    # 会话id
    user_session_id = f"{request.user_id}*_*{request.session_id}"
    # 命盘文件
    fate_dir = os.path.join(pwd, "fates")
    os.makedirs(fate_dir, exist_ok=True)
    fate_file = os.path.join(fate_dir, f"{user_session_id}.json")

    app_logger = get_app_logger(LOG_DIR)
    try:
        with open(fate_file, 'w', encoding='utf8') as f:
            json.dump(request.user_fate, f, indent=2, ensure_ascii=False, separators=(',', ': '))
        app_logger.info(f"命盘文件已保存: {fate_file}")
        return {'success': True}
    except Exception as e:
        app_logger.error(f"保存命盘文件失败: {e}", exc_info=True)
        return {'success': False}


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    agent = app.state.agent
    user_session_id = f"{request.user_id}*_*{request.session_id}"
    app_logger = get_app_logger(LOG_DIR)

    config = {
        "configurable": {
            "thread_id": user_session_id,
        }
    }

    async def event_generator():
        log_to_session(LOG_DIR, user_session_id, "info",
            f"\n{'='*50}\n[USER INPUT] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Session: {user_session_id}\nContent: {request.message}\n{'='*50}")

        # 读取命盘文件并创建 Person 对象
        fate_file = os.path.join(pwd, "fates", f"{user_session_id}.json")

        input_data = {
            "messages": [HumanMessage(content=request.message)],
            "fate_file": fate_file,
            "llm_calls": 0,
            "sender": ""
        }

        async for step_path, step_content in agent.astream(
            input_data,
            config=config,
            stream_mode="updates",
            subgraphs=True
        ):
            for node_name, data in step_content.items():
                if "messages" in data:
                    for m in data["messages"]:
                        payload = {
                            "path": " -> ".join(step_path),
                            "node": node_name,
                            "type": m.__class__.__name__,
                            "content": m.content,
                            "tool_calls": getattr(m, 'tool_calls', None)
                        }

                        # 记录日志
                        log_header = f"[{node_name}] ({' -> '.join(step_path)})"
                        log_to_session(LOG_DIR, user_session_id, "debug",
                            f"\n{log_header}\nType: {m.__class__.__name__}")
                        if m.content:
                            log_to_session(LOG_DIR, user_session_id, "debug",
                                f"Content: {m.content}")
                        if payload["tool_calls"]:
                            log_to_session(LOG_DIR, user_session_id, "debug",
                                f"Tool Calls: {json.dumps(payload['tool_calls'], ensure_ascii=False, indent=2)}")

                        yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.post("/chat/history")
async def get_chat_history(request: HistoryRequest):
    agent = app.state.agent
    # 保持与 chat_stream 逻辑一致的 thread_id 构造方式
    user_session_id = f"{request.user_id}*_*{request.session_id}"

    config = {"configurable": {"thread_id": user_session_id}}

    # 获取该线程的最新的状态
    state = await agent.aget_state(config)

    history = []
    if state.values and "messages" in state.values:
        for m in state.values["messages"]:
            history.append({
                "type": m.__class__.__name__,
                "content": m.content,
                # 如果是 AI 消息，可能包含 tool_calls
                "tool_calls": getattr(m, 'tool_calls', None) if hasattr(m, 'tool_calls') else None,
            })

    return history

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
