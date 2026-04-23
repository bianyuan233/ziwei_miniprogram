from ziwei_const import *
from rule_const import *
import re
from ziwei_person import Person


class RuleEngine:

    def __init__(self, ziwei_person: Person, year=None, age=None, month=None):
        self.ziwei_person = ziwei_person
        self.year = year
        self.age = age
        self.month = month

    def exctract_func(self, vocab, ziwei_str):
        patterns = []
        for key, lst in vocab:
            patterns.append(f"(?P<{key}>{'|'.join(lst)})")
        full_pattern = ".*?".join(patterns)
        match = re.search(full_pattern, ziwei_str)
        if match:
            kwargs = match.groupdict()
            return kwargs
        else:
            return {}

    def func_tianganhua(self, ziwei_str):
        """
        执行天干化的判断函数
        """
        vocab = [('palace_mode_0', DIMENSION_LST), ('palace_0', PALACE_LST),
                 ('hua', HUA_LST), ('palace_mode_1', DIMENSION_LST),
                 ('palace_1', PALACE_LST)]
        kwargs = self.exctract_func(vocab, ziwei_str)
        if kwargs:
            return self.ziwei_person.palace_hua_palace(**kwargs,
                                                  year=self.year,
                                                  age=self.age)
        else:
            raise ValueError(f"匹配失败，字符串格式不符合预期: {ziwei_str}")
            return False

    def func_shengnianhua(self, ziwei_str):
        """
        执行有生年的判断函数
        """
        vocab = [('palace_mode', DIMENSION_LST), ('palace', PALACE_LST),
                 ('hua', HUA_LST)]
        kwargs = self.exctract_func(vocab, ziwei_str)
        if kwargs:
            return self.ziwei_person.palace_hua(**kwargs,
                                           year=self.year,
                                           age=self.age)
        else:
            raise ValueError(f"匹配失败，字符串格式不符合预期: {ziwei_str}")
            # return False

    def func_havestar(self, ziwei_str):
        """
        执行有星判断函数
        """
        vocab = [('palace_mode', DIMENSION_LST), ('palace', PALACE_LST),
                 ('borrow', [PARA_JIEGONG, PARA_BENGONG]), ('star', STAR_LST)]
        kwargs = self.exctract_func(vocab, ziwei_str)
        if kwargs['borrow'] == PARA_JIEGONG:
            kwargs['borrow'] = True
        elif kwargs['borrow'] == PARA_BENGONG:
            kwargs['borrow'] = False
        if kwargs:
            return self.ziwei_person.palace_have_star(**kwargs,
                                                 year=self.year,
                                                 age=self.age)
        else:
            raise ValueError(f"匹配失败，字符串格式不符合预期: {ziwei_str}")

    def evaluate_condition(self, condition_str):
        """
        根据 condition_str 执行对应的判断函数，返回 True 或 False。
        """
        condition_str = condition_str.strip()

        # 示例逻辑：根据关键字匹配
        if FUNC_TIANGANHUA in condition_str:
            return self.func_tianganhua(condition_str)
        elif FUNC_SHENGNIANHUA in condition_str:
            return self.func_shengnianhua(condition_str)
        elif FUNC_HAVESTAR in condition_str:
            return self.func_havestar(condition_str)

        return False

    def exctract_rule(self, rule_text):

        def replacer(match):
            # match.group(1) 是括号内的内容
            content = match.group(1)
            # 调用我们的逻辑判断函数
            result = self.evaluate_condition(content)
            # 将布尔值转为字符串，供 eval 使用
            return str(result)

        processed_str = re.sub(r'\((.*?)\)', replacer, rule_text)
        # print(f"解析后的表达式: {processed_str}")
        if processed_str:
            final_result = eval(processed_str)
            return final_result
        else:
            return False


# if __name__ == '__main__':
#     import json

#     url = "https://api.siliconflow.cn/v1/chat/completions"
#     api_key = "sk-xakjmutgpevfbtnayqjoxgzvvhalddjlwbzvsaknbgvkwipn"
#     model_name = "Pro/MiniMaxAI/MiniMax-M2.5"

#     # print(json.dumps(JIANKANG_PRE_RULE, ensure_ascii=False, indent=2, separators=(',', ':')))

#     ziwei_person = None
#     with open('./testResult0310.json', 'r', encoding='utf8') as f:
#         data = json.load(f)
#         ziwei_person = Person(data['data'])
#     for year in range(1990, 2030):
#         age = year - 1990 + 1
#         for month in range(1, 2):
#             rule_engine = RuleEngine(ziwei_person, year=year, month=month)
#             pre_rule_lst = []
#             loc_rule_lst = []
#             for rule in JIANKANG_PRE_RULE:
#                 if rule_engine.exctract_rule(rule['rule']):
#                     pre_rule_lst.append({
#                         'index': rule['index'],
#                         '判断依据': rule['reason'],
#                         '应验事项和可能性分数': rule['result'],
#                         '建议': rule['solution']
#                     })
#             if len(pre_rule_lst) > 0:
#                 for rule in JIANKANG_LOC_RULE:
#                     if rule_engine.exctract_rule(rule['rule']):
#                         loc_rule_lst.append({
#                             'index': rule['index'],
#                             '判断依据': rule['reason'],
#                             '前提条件': rule['premise'],
#                             '应验事项和定位准确性分数': rule['result'],
#                             '建议': rule['solution']
#                         })

#             if len(pre_rule_lst) > 0 and len(loc_rule_lst) > 0:
#                 print('*' * 20)
#                 user_prompt = need_prompt.format(year=year, age=age, pre_rule_lst=pre_rule_lst, loc_rule_lst=loc_rule_lst)
#                 result = send_msg(url=url,
#                                   model_name=model_name,
#                                   system_prompt='',
#                                   user_prompt=user_prompt,
#                                   api_key=api_key,
#                                   json_format=True)
#                 if not result['success']:
#                     continue

#                 llm_response = json.loads(result['content'])
#                 if llm_response['result'] != '需要':
#                     continue
#                 print(f"{year}年需要关注")

#                 exit()
