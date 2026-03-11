# 顺顺念微信小程序

基于提供的 HTML 原型，从 0 搭建的微信小程序工程示例，包含：

- 新用户生辰录入
- 三步命盘校准
- 命盘结果页
- 首页、命盘、我的 3 个主页面
- 本地存储的用户状态、支付状态、历史记录 mock

## 目录结构

```text
.
|-- app.js
|-- app.json
|-- app.wxss
|-- project.config.json
|-- project.private.config.json
|-- sitemap.json
|-- pages
|   |-- welcome
|   |-- verify
|   |-- result
|   |-- home
|   |-- chart
|   `-- profile
`-- utils
    |-- mock.js
    |-- format.js
    `-- storage.js
```

## 使用方式

1. 打开微信开发者工具。
2. 选择“导入项目”。
3. 项目目录选择当前目录：`C:\Users\Administrator\Desktop\testAi`
4. `AppID` 可先使用测试号或无 AppID 模式调试。
5. 导入后直接编译运行。

## 说明

- 当前版本使用本地 mock 数据，不依赖后端接口。
- 支付、命理分析、流年记录均为原型态演示逻辑。
- 如果你希望，我下一步可以继续帮你补成“可交付的软件工程版本”，包括：
  - 云开发或 Node.js 后端
  - 用户登录
  - 真实支付接入
  - 业务接口分层
  - 单元测试与发布配置
