# 小程序前后端交互与业务流程

更新时间：2026-04-23

本文用于快速理解 `testAi` 小程序、Node 后端和 Python Agent 的完整调用链。后端结构可参考 `C:\Users\Administrator\Desktop\testAi_backend\CLAUDE.md`。

## 总体架构

```text
微信小程序前端
  pages/chart/index.js
  pages/qa/index.js
    |
    | HTTPS
    v
Nginx / bianyuan.art
    |
    | proxy_pass
    v
Node Express 后端 :3000
  /api/aiData
  /api/agent/stream
    |
    | HTTP localhost
    v
Python FastAPI Agent :8000
  /chat/gen_fate
  /chat/stream
```

## 前端页面流程

### 1. 注册与档案录入

页面：

```text
pages/register/index
```

用户录入并保存到微信本地 storage：

```text
currentUser.phone
currentUser.gender
profiles[].name
profiles[].birthDate
profiles[].timeIndex
profiles[].timeLabel
profiles[].gender
```

注册和添加档案阶段不调用后端。

### 2. 验证命盘

页面：

```text
pages/calibration/index
```

当前题目保留在前端：

```text
utils/calibrationService.js -> getQuestions()
```

答完后固定通过：

```json
{ "status": "success", "accuracy": 95 }
```

后续若改成后端题库或校准接口，只替换 `calibrationService`，页面流程不需要重写。

### 3. 首页

页面：

```text
pages/home/index
```

行为：

- 读取本地档案、会员模拟状态、问答次数。
- 快捷提问会先跳转 `pages/qa/index?question=...`。
- 首页本身不调用后端。

### 4. 命盘详情

页面：

```text
pages/chart/index.js -> loadChart()
```

调用时机：

- 点击“查看完整命盘”进入页面。
- 若当前档案没有有效命盘缓存，调用后端。
- 若 `birthDate/timeIndex/gender` 没变，直接读本地缓存。

请求：

```text
POST https://bianyuan.art/api/aiData
```

请求体：

```json
{
  "birthDate": "1990-01-01",
  "timeIndex": 6,
  "gender": "男"
}
```

前端使用：

```text
data.bySolar
data.majorPeriods
data.yearlyPeriods
```

### 5. 命理问答

页面：

```text
pages/qa/index.js
```

进入页面时：

- 先检查档案是否已校准。
- 若当前档案没有有效命盘缓存，先调用 `/api/aiData` 准备命盘。
- 准备完成后生成新的 `sessionId`，显示开场消息。

发送问题时：

```text
pages/qa/index.js -> sendQuestion()
utils/agentStreamService.js -> startAgentStream()
```

请求：

```text
POST https://bianyuan.art/api/agent/stream
Accept: text/event-stream
```

请求体：

```json
{
  "birthDate": "1990-01-01",
  "timeIndex": 6,
  "gender": "男",
  "occupation": "",
  "userId": "user_xxx",
  "sessionId": "sess_xxx",
  "question": "我今年事业怎么样？"
}
```

前端处理 SSE：

```text
meta   -> 接收请求元信息
delta  -> 追加助手气泡文本
done   -> 结束流式回答，增加本机问答次数
error  -> 展示错误横幅
```

当前不调用 `/api/agent/history`。问答页文案为：

```text
本机不保存对话记录 · 服务端仅用于本次分析处理
```

### 6. 账户、会员、协议、客服

页面：

```text
pages/account/index
pages/pricing/index
pages/policy/index
```

当前均不调用后端。

- 会员充值为本地模拟，写入 `subscription/paymentHistory`。
- 客服反馈为本地提示，不提交服务端。
- 分享使用小程序 `open-type="share"` 和右上角菜单能力。

## 后端接口

### `/api/aiData`

Node 文件：

```text
routes/api.js
```

职责：

- 校验 `birthDate/timeIndex/gender`
- 调用 `iztro`
- 返回 `bySolar / majorPeriods / yearlyPeriods`

### `/api/agent/stream`

Node 文件：

```text
routes/agent.js
services/pokemonAgentService.js
services/agentSessionStore.js
```

核心链路：

```text
1. 校验前端参数
2. 用 iztro 重新生成 aiData
3. 写入 SQLite session 表
4. initFate(userId, sessionId, aiData)
   -> POST http://127.0.0.1:8000/chat/gen_fate
5. streamChatMessage(userId, sessionId, question)
   -> POST http://127.0.0.1:8000/chat/stream
6. 将 Python SSE 归一化为前端 SSE
```

前端期望：

```text
data: {"type":"meta",...}
data: {"type":"delta","content":"..."}
data: {"type":"done"}
```

若出现 `connect ECONNREFUSED ::1:8000`，优先检查 PM2 配置是否把上游地址误改回 `localhost:8000`。
