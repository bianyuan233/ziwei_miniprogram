from openai import OpenAI

def send_msg(url,
             model_name,
             system_prompt,
             user_prompt,
             api_key,
             json_format=False,
             timeout=120):
    """发送LLM请求，支持Interleaved Thinking友好格式(reasoning_split)"""

    # 构造 base_url（从 url 中提取基础路径）
    # url 格式如: https://api.minimaxi.com/v1/chat/completions
    # base_url 应为: https://api.minimaxi.com/v1
    base_url = url.rsplit('/v1', 1)[0] + '/v1' if '/v1' in url else url

    client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    extra_body = {"reasoning_split": True}

    try:
        kwargs = {
            "model": model_name,
            "messages": messages,
            "extra_body": extra_body
        }
        if json_format:
            kwargs["response_format"] = {"type": "json_object"}
        response = client.chat.completions.create(**kwargs)

        msg = response.choices[0].message

        # 提取正文内容
        content = msg.content or ""

        # json_format=True 时，去除 markdown 代码块包裹
        if json_format:
            content = _strip_json_code_block(content)

        # 提取思考内容 - 优先使用 reasoning_details（结构化列表）
        reasoning_details = msg.reasoning_details
        if reasoning_details and isinstance(reasoning_details, list):
            # reasoning_details 是列表，取第一个元素的 text 字段
            reasoning = reasoning_details[0].get('text', '') if reasoning_details else ''
        else:
            # 备用 reasoning_content（字符串形式）
            reasoning = getattr(msg, 'reasoning_content', '') or ''

        return {
            'success': True,
            'content': content,
            'reasoning': reasoning
        }

    except Exception as e:
        return {'success': False, 'content': f"请求异常: {e}"}