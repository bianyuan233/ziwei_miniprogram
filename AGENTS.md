# 项目协作与服务器维护说明

## 默认协作规则

- 默认中文沟通，代码和命令按项目现有风格处理。
- 先结论，后理由。
- 只做当前任务需要的最小改动，保护已有本地改动。
- 涉及构建、远程服务、同步、覆盖、删除时默认保守，先确认现状再执行。
- 修改后需要做最小但有效的验证，并说明验证结果。

## 重要文档入口

- 前端代码目录：`C:\Users\Administrator\Desktop\testAi`
- `PROGRAM_FLOW.md`：记录小程序、Node 后端、Python Agent 的前后端交互和业务流程。
- 后端参考：`C:\Users\Administrator\Desktop\testAi_backend\CLAUDE.md`。

后续处理业务或接口问题时，优先阅读 `PROGRAM_FLOW.md`。

## 远程服务器信息

- 服务器：`106.55.183.76`
- SSH 用户：`ubuntu`
- 不要把服务器密码写入仓库或文档；需要 SSH 时使用用户在会话中授权提供的凭据。
- 远程 Node 后端目录：`/home/ubuntu/backend_260314/ziwei_backend/backend`
- 远程 Python Agent 目录：`/home/ubuntu/ziwei_agent/workspace`
- 公网域名：`https://bianyuan.art`

## 推荐 SSH 流程

本机 Windows 环境可通过 WSL + `sshpass` 执行远程只读或维护命令。

基本模式：

```powershell
@'
SSHPASS='<由用户授权提供>'
export SSHPASS
sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ubuntu@106.55.183.76 'bash -s' <<'REMOTE'
set -e
# remote commands here
REMOTE
'@ | wsl.exe -e bash -lc "tr -d '\r' | bash"
```

注意：

- 不要把真实密码写入文件。
- Windows here-string 传给 WSL 时，建议使用 `tr -d '\r'` 去掉 CRLF。
- 远程维护前先查状态，再操作。

## 远程服务管理

当前服务使用 root PM2 + systemd 托管。

PM2 可执行环境：

```bash
PM2_PATH=/root/.nvm/versions/node/v22.22.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
sudo env PATH="$PM2_PATH" pm2 list
```

PM2 应用：

```text
miniprogram-backend  -> Node Express :3000
ziwei-python-agent   -> Python FastAPI :8000
```

PM2 配置：

```text
/home/ubuntu/backend_260314/ziwei_backend/backend/ecosystem.config.js
```

关键配置：

```text
Node interpreter: /home/ubuntu/runtime/node-v18.17.1/bin/node
Python command: /home/ubuntu/ziwei_agent/env/ziwei/bin/python app.py
POKEMON_AGENT_BASE_URL: http://127.0.0.1:8000
```

不要随意改回 `localhost:8000`，否则 Node 可能解析到 IPv6 `::1`，导致 `connect ECONNREFUSED ::1:8000`。

## 常用远程检查命令

端口：

```bash
ss -lntp | grep -E ':(3000|8000)\b'
```

PM2：

```bash
sudo env PATH="$PM2_PATH" pm2 list
sudo env PATH="$PM2_PATH" pm2 logs miniprogram-backend --lines 50 --nostream
sudo env PATH="$PM2_PATH" pm2 logs ziwei-python-agent --lines 50 --nostream
```

systemd 自启：

```bash
sudo systemctl is-enabled pm2-root
sudo systemctl is-active pm2-root
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

## 维护注意事项

- `better-sqlite3` 是原生模块，当前匹配 Node `18.17.1`。不要直接用 Node 22 跑后端。
- 如果误 rebuild 破坏了 `better-sqlite3`，需要确保 `PATH` 中 Node18 在最前，再 rebuild：

```bash
NODE18_HOME=/home/ubuntu/runtime/node-v18.17.1
PATH_NODE18="$NODE18_HOME/bin:/root/.nvm/versions/node/v22.22.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
sudo env PATH="$PATH_NODE18" bash -lc "cd /home/ubuntu/backend_260314/ziwei_backend/backend && /home/ubuntu/runtime/node-v18.17.1/bin/node /root/.nvm/versions/node/v22.22.0/lib/node_modules/npm/bin/npm-cli.js rebuild better-sqlite3"
```

- Python Agent 的 PM2 配置使用 `interpreter: none`，脚本是虚拟环境 python，参数是 `app.py`。不要改回直接 `script: app.py + interpreter: python`，PM2 可能把自己的 JS wrapper 交给 Python 解析。
- 每次改远程配置后执行：

```bash
sudo env PATH="$PM2_PATH" pm2 save
```
