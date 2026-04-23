# AI 流式问答 Demo — 前端说明

本文档描述 `pages/api-result` 的状态机设计、消息结构、SSE 协议解析和手工测试步骤。

---

## 两段式流程

```
onLoad()
  │
  ├─ 读 storage.getProfile() → birthDate / birthHour / gender / profession
  ├─ format.getBackendTimeIndex(birthHour) → timeIndex
  └─ _loadChart()
       │
       └─ POST /api/aiData { birthDate, timeIndex, gender }
            │
            ├─ 成功 → pageState = ready，生成 sessionId（本页固定复用）
            └─ 失败 → pageState = error

用户输入 question → onSend()
  └─ POST /api/agent/stream { birthDate, timeIndex, gender, occupation,
                              userId, sessionId, question }
       │  (enableChunked: true)
       ├─ onChunkReceived → decodeBuffer → _processSSEText → _handleSSEEvent
       ├─ type=meta    → 忽略（仅记录 requestId）
       ├─ type=delta   → 追加到最后一条 assistant 消息的 content
       ├─ type=done    → streaming=false，pageState=ready，解禁输入
       └─ type=error   → _handleStreamError → pageState=error
```

---

## 页面状态机

```
         onLoad
           │
           ▼
    ┌─ loadingChart ─┐
    │  /api/aiData   │
    └────────────────┘
          │                    │
       success               fail
          │                    │
          ▼                    ▼
       ready ◄──── done     error
          │
       onSend
          │
          ▼
       streaming
```

| `pageState` | 含义 | UI 表现 |
|---|---|---|
| `loadingChart` | /api/aiData 请求中 | spinner + skeleton |
| `ready` | 命盘就绪，可提问 | 摘要卡 + 输入栏可用 |
| `streaming` | SSE 流接收中 | 输入禁用，assistant 气泡滚动 |
| `error` | 请求失败 | 无命盘→错误卡+重试；有命盘→可关闭横幅 |

---

## 消息结构

```js
messages: [
  { id: '1714xxx_u', role: 'user',      content: '我的事业运如何？', streaming: false },
  { id: '1714xxx_a', role: 'assistant', content: '根据命盘…',        streaming: false },
  // 多轮追加，不清空
]
```

- `streaming: true` 时该气泡显示 typing indicator（content 为空）或流式文本+游标（content 非空）。
- `streaming: false` 后气泡内容固定，不再变化。

---

## SSE 协议解析

后端固定输出以下四种事件，前端只处理这四种，其余丢弃：

```
data: {"type":"meta",  "requestId":"...", "sessionId":"..."}
data: {"type":"delta", "content":"..."}
data: {"type":"done"}
data: {"type":"error", "message":"..."}
```

### ArrayBuffer → UTF-8 解码

WeChat mini-program `onChunkReceived` 返回 `ArrayBuffer`，用兼容性写法解码：

```js
function decodeBuffer(buffer) {
  const bytes = new Uint8Array(buffer);
  let binary = '';
  for (let i = 0; i < bytes.length; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  try {
    return decodeURIComponent(escape(binary));
  } catch (e) {
    return binary;
  }
}
```

### SSE 行解析

网络分片可能在任意位置切断，用 buffer 拼行：

```js
_processSSEText(text) {
  this._sseBuffer += text;
  const lines = this._sseBuffer.split('\n');
  this._sseBuffer = lines.pop() || '';   // 末尾不完整行留给下一片

  for (const line of lines) {
    if (!line.startsWith('data: ')) continue;
    try { this._handleSSEEvent(JSON.parse(line.slice(6).trim())); } catch {}
  }
}
```

---

## 关键字段来源

| 字段 | 来源 |
|---|---|
| `birthDate` | `storage.getProfile().birthDate` |
| `timeIndex` | `format.getBackendTimeIndex(profile.birthHour)` |
| `gender` | `storage.getProfile().gender` |
| `occupation` | `storage.getProfile().profession` |
| `userId` | `storage.getProfile().userId` |
| `sessionId` | 页面 `ready` 时生成一次，整页复用 |
| `question` | 用户输入框内容 |

---

## 手工测试步骤

### 前置条件

1. 后端已启动（`npm run dev` 或 `pm2 start`），可访问 `https://bianyuan.art` 或本地 `http://127.0.0.1:3000`
2. 上游 AI 服务（`:8000`）已启动（仅 `/api/agent/stream` 需要）
3. 微信开发者工具中已完成验盘（`storage.isVerified() === true`），profile 中 `birthDate` 非空

### 测试一：命盘加载

1. 从首页点击"接口测试"（`key: 'api'`）进入 `pages/api-result`
2. 页面应短暂显示 spinner 和"正在推算命盘"
3. 成功后：显示个人信息卡 + 命盘摘要卡（命主/身主/五行局/生肖/星座/阴历），底部出现输入栏
4. 失败时：显示错误卡和"重新请求"按钮

### 测试二：提问（需上游 :8000 在线）

1. 在输入栏输入问题，例如"我今年的事业运势如何？"
2. 点击"发送"：用户气泡出现在右侧，assistant 气泡出现在左侧（显示 typing indicator）
3. SSE delta 到达：assistant 气泡内容逐字追加
4. SSE done 到达：游标消失，输入栏重新可用
5. 可继续输入下一问题，sessionId 不变，messages 列表追加

### 测试三：上游不可用时的错误处理

1. 确保 :8000 未启动
2. 发送问题后，assistant 气泡应显示 `[响应出错]`（若流已开始）或直接错误横幅（若 gen_fate 失败）
3. 错误横幅点击 × 可关闭，命盘摘要和历史消息保留

### 测试四：多轮对话

1. 完成一次问答后
2. 再次输入不同问题发送
3. 两轮消息均显示在列表中，sessionId 未变

---

## 已知限制

- `enableChunked` 需要微信基础库 ≥ 2.20.1；低版本会退化为 `success` 一次性回调，无流式效果但不崩溃
- `decodeBuffer` 对多字节 UTF-8 字符使用 `escape/decodeURIComponent` hack，在极少数边缘编码上可能乱码
- `sessionId` 仅在页面生命周期内有效；重新进入页面会生成新 sessionId
