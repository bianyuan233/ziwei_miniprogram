# 接口问答故障根因与网络知识点

更新时间：2026-04-21

## 结论

本次小程序问答失败不是单一前端问题，而是多层链路问题叠加：

1. 命盘接口返回结构为 `res.data.data.bySolar`，前端原先读取 `res.data.bySolar`，导致“命盘加载失败”。
2. Node 后端问答接口配置 `POKEMON_AGENT_BASE_URL=http://localhost:8000`，服务器上 `localhost` 解析到 IPv6 `::1`，但 Python Agent 只监听 IPv4 `0.0.0.0:8000`，导致 `connect ECONNREFUSED ::1:8000`。
3. Node 后端传给 Python `/chat/gen_fate` 的 `user_fate` 是字符串，但 Python Pydantic 模型要求 `dict`，导致 `gen_fate 返回 422`。
4. Python Agent 曾运行在 Trae sandbox 进程里，命盘文件写入不稳定；已改为 PM2 管理的普通后台进程。
5. Python Agent SSE 返回的 `content` 是数组结构，Node 原先只处理字符串，导致即使上游返回了内容，前端也可能只看到 `done`。
6. 旧 PM2 使用 Node 22 启动 Node 后端，而 `better-sqlite3` 原生模块匹配 Node 18，导致 PM2 进程持续重启；已固定 PM2 后端解释器为 Node 18.17.1。

## 当前修复状态

已修复：

- 小程序 `pages/api-result/index.js` 兼容 `res.data.data.bySolar`。
- 远程后端 `.env` 已改为 `POKEMON_AGENT_BASE_URL=http://127.0.0.1:8000`。
- Node 后端 `routes/agent.js` 调用 `initFate(userId, sessionId, aiData)`，向 Python 传命盘对象。
- Node 后端 `services/pokemonAgentService.js` 支持提取 Python SSE 的 `content[].text`。
- PM2 已托管：
  - `miniprogram-backend`：监听 `3000`
  - `ziwei-python-agent`：监听 `8000`
- `pm2-root` systemd 服务已启用并处于 active 状态。

## 关键网络知识点

### 1. `localhost` 不等于固定的 `127.0.0.1`

`localhost` 可能解析成：

- IPv4：`127.0.0.1`
- IPv6：`::1`

如果服务只监听 IPv4，例如：

```text
0.0.0.0:8000
```

而客户端连接：

```text
::1:8000
```

就会出现：

```text
connect ECONNREFUSED ::1:8000
```

本项目中，Node 后端访问 Python Agent 必须使用：

```text
http://127.0.0.1:8000
```

### 2. 监听地址决定哪些连接能进来

常见监听含义：

```text
127.0.0.1:8000  只接受本机 IPv4 loopback
0.0.0.0:8000    接受所有 IPv4 网卡
::1:8000        只接受本机 IPv6 loopback
[::]:8000       接受 IPv6，是否兼容 IPv4 取决于系统配置
```

本项目 Python Agent 当前监听：

```text
0.0.0.0:8000
```

因此 `127.0.0.1:8000` 可访问，`::1:8000` 不可访问。

### 3. Nginx 只代理到 Node，Node 再代理到 Python

公网访问路径：

```text
小程序
  -> https://bianyuan.art/api/agent/stream
  -> Nginx
  -> Node Express :3000
  -> Python FastAPI :8000
  -> LLM/Agent
```

因此公网 HTTPS 正常不代表内部 `3000 -> 8000` 正常，需要分别检查。

### 4. SSE 的 HTTP 状态和业务错误是两回事

`/api/agent/stream` 使用 Server-Sent Events。

可能出现 HTTP 200，但 SSE 内容是：

```text
data: {"type":"error","message":"..."}
```

所以排查时不能只看 HTTP status，还要看 SSE event。

正常返回应类似：

```text
data: {"type":"meta",...}
data: {"type":"delta","content":"..."}
data: {"type":"done"}
```

### 5. 原生 Node 模块依赖 Node ABI

`better-sqlite3` 是原生模块，编译产物绑定 Node ABI。

本项目原先可用版本匹配：

```text
Node 18.17.1
NODE_MODULE_VERSION 108
```

PM2 原先用 Node 22 启动，导致 ABI 不匹配或 rebuild 失败。当前 PM2 明确使用：

```text
/home/ubuntu/runtime/node-v18.17.1/bin/node
```

### 6. 进程工作目录会影响 `.env`

Node `dotenv.config()` 默认读取 `process.cwd()/.env`。

PM2 必须设置：

```text
cwd=/home/ubuntu/backend_260314/ziwei_backend/backend
```

否则 `.env` 可能不加载，进而回退到代码默认值 `http://localhost:8000`。

## 排查命令摘要

端口监听：

```bash
ss -lntp | grep -E ':(3000|8000)\b'
```

PM2 状态：

```bash
sudo env PATH=/root/.nvm/versions/node/v22.22.0/bin:$PATH pm2 list
```

本机链路测试：

```bash
curl -N -X POST http://127.0.0.1:3000/api/agent/stream \
  -H 'Content-Type: application/json' \
  -H 'Accept: text/event-stream' \
  -d '{"birthDate":"1990-01-01","timeIndex":6,"gender":"男","userId":"u1","sessionId":"s1","question":"hello"}'
```

公网链路测试：

```bash
curl -N -X POST https://bianyuan.art/api/agent/stream \
  -H 'Content-Type: application/json' \
  -H 'Accept: text/event-stream' \
  -d '{"birthDate":"1990-01-01","timeIndex":6,"gender":"男","userId":"u1","sessionId":"s1","question":"hello"}'
```

