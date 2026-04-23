import os
import requests
import json

from agent import pwd

USER_ID = "user12345"
SESSION_ID = "session45678"

def test_chat_gen_fate():
    url = "http://127.0.0.1:8000/chat/gen_fate"
    
    # 这里的 user_id 和 session_id 必须与你之前聊天时使用的一致
    payload = {
        "user_id": USER_ID,
        "session_id": SESSION_ID,
        "user_fate": json.load(open(os.path.join(pwd, 'test.json')))['data']
    }

    print(f"\n{'='*50}")
    print(f"正在初始化命盘: {url}")
    print(f"用户ID: {payload['user_id']}, 会话ID: {payload['session_id']}")
    print(f"{'='*50}\n")

    try:
        response = requests.post(url, json=payload)
        
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"错误详情: {response.text}")
            return

        data = response.json()
        if data['success']:
            print('已完成初始化')
            return
        else:
            print('初始化失败')
            return

    except Exception as e:
        print(f"发生错误: {e}")
    


def test_get_history():
    url = "http://127.0.0.1:8000/chat/history"
    
    # 这里的 user_id 和 session_id 必须与你之前聊天时使用的一致
    payload = {
        "user_id": USER_ID,
        "session_id": SESSION_ID
    }

    print(f"\n{'='*50}")
    print(f"正在查询历史记录: {url}")
    print(f"用户ID: {payload['user_id']}, 会话ID: {payload['session_id']}")
    print(f"{'='*50}\n")
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"错误详情: {response.text}")
            return

        data = response.json()
        history = data

        if not history:
            print("未找到该会话的历史记录。")
            return

        print(f"找到 {len(history)} 条消息记录：\n")
        
        for i, msg in enumerate(history, 1):
            msg_type = msg.get("type")
            content = msg.get("content")
            tool_calls = msg.get("tool_calls")

            # 简单的角色转换显示
            role = "🤖 AI" if "AI" in msg_type else "👤 USER"
            if "Tool" in msg_type: role = "🔧 TOOL"
            
            print(f"[{i}] {role} ({msg_type})")
            
            if content:
                print(f"    内容: {content}")
            
            if tool_calls:
                print(f"    工具调用: {json.dumps(tool_calls, ensure_ascii=False, indent=2)}")
            
            print("-" * 30)

    except Exception as e:
        print(f"发生错误: {e}")
    

def test_chat_stream():
    url = "http://127.0.0.1:8000/chat/stream"
    
    # 测试数据
    payload = {
        "user_id": USER_ID,
        "session_id": SESSION_ID,
        "message": "我今年健康方面的运势怎么样？"
    }

    print(f"正在发送请求到: {url}...")
    
    try:
        # 使用 stream=True 处理流式响应
        with requests.post(url, json=payload, stream=True) as response:
            if response.status_code != 200:
                print(f"请求失败: {response.status_code}")
                return

            print("--- 收到流式响应 ---")
            for line in response.iter_lines():
                if line:
                    # 去掉 SSE 的 "data: " 前缀
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith("data: "):
                        data_str = decoded_line[6:]
                        data = json.loads(data_str)
                        
                        # 格式化打印输出
                        node = data.get("node")
                        path = data.get("path")
                        content = data.get("content")
                        tool_calls = data.get("tool_calls")
                        
                        print(f"\n>> 节点: {node} (路径: {path})")
                        if content:
                            print(f"内容: {content}")
                        if tool_calls:
                            print(f"工具调用: {json.dumps(tool_calls, ensure_ascii=False)}")
                            
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    test_chat_gen_fate()
    test_chat_stream()
    # test_get_history()
