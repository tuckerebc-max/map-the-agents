# 架构与边界

> Extension API：v1
> English: [Architecture and boundaries](./architecture.en.md)
> 继续阅读：[快速开始](./quick-start.md) · [权限与信任](./security-and-resources.md)

## 核心不变量

Kun 扩展平台不会创建第二套 Agent runtime。Agent 对话、线程、工具、审批、事件、Provider 路由与用量仍由唯一的 `kun serve` 负责。扩展只能通过公开 Host Context 和 Broker 调用这些能力。

```text
Renderer / Workbench
  | host-rendered contributions
  | sandboxed extension Webviews
  v
Electron Main
  | sender validation / protected consent / kun-extension://
  | existing preload -> runtime boundary
  v
kun serve
  ExtensionManager
    | one child process per active Node extension
    | versioned private JSON IPC
    v
  Extension Host processes
    | public Host Context / SDK only
    v
  AgentLoop / ToolHost / EventBus / stores / ModelClient routing
```

`rpcVersion` 只属于 Kun 与随版本分发的 Host runner，是私有协议。扩展不得直接连接它，也不得持有 GUI/runtime bearer token。

## 执行位置

| 扩展内容 | 执行位置 | 适合用途 | 安全/兼容说明 |
| --- | --- | --- | --- |
| `main` | 每个扩展独立 Node 子进程 | 工具、Provider、认证处理器、Agent、后台命令 | 有当前用户 OS 权限；进程隔离不是安全沙箱 |
| `browser` / View | 独立、宿主创建的 Chromium Webview | 复杂侧栏、编辑区、面板 UI | Node 关闭；只暴露窄 bridge；默认禁止直连网络 |
| 声明式贡献 | Kun React 树中的宿主组件 | 命令按钮、菜单、设置、通知 | 不运行插件 React；宿主负责可访问性和 UX |
| `hostContentScripts` | 插件专属 Electron isolated world | 必须直接读取/修改宿主 DOM 的极少场景 | 高风险；DOM/选择器不稳定；不进入受保护窗口 |

一个 browser-only 扩展不会启动 Node 子进程。任何需要 headless 的工具、Agent profile、模型 Provider、认证处理器、计划任务或后台命令都必须有 `main`，且绝不以 `browser` 作为 headless fallback。

## ExtensionManager 与 Host

`ExtensionManager` 位于 Kun runtime composition root，由 `kun serve`、`kun exec` 和 GUI 请求共用。它负责：

- 读取已安装版本、选择版本、全局/工作区 enablement 和权限快照；
- 在激活事件到达后惰性启动对应 Node Host；
- 将扩展身份、版本、工作区、权限和 lifecycle nonce 绑定到父子连接；
- 限制启动/操作时间、并发、队列、消息、事件速率、流缓冲和内存；
- 传播取消、等待 deactivation、释放注册项并阻止孤儿进程；
- 对崩溃执行有界退避和按扩展熔断；
- 提供扩展级状态、轮转日志与脱敏诊断。

同一 Kun runtime 中，一个扩展版本最多有一个 Node Host；不同扩展永不共享 Node 进程。并发激活请求会合并为一次激活。

## 身份、权限与 Broker

身份来自宿主建立的连接或 WebContents/View Session，不相信 payload 中的 `extensionId`。每次 Broker 操作重新检查：

1. 扩展和版本是否仍启用、兼容且未熔断；
2. 当前工作区的 trust、scope 和 permission grant；
3. 资源是否属于调用者（thread、account、state、view session 等）；
4. 请求 Schema、大小、速率、并发与配额；
5. 操作是否需要受保护的用户确认或 Kun ApprovalGate。

Node 可以绕过 Broker 直接调用 Node 文件、网络或进程 API。Manifest 权限对 Broker 是强制授权，对 Node 直接 OS 访问只能作为风险披露和审计。详见[权限与信任](./security-and-resources.md)。

## UI 数据路径

声明式贡献从 Manifest 静态发现，不需激活代码。用户真正打开 View 或触发命令时才激活拥有者。

```text
Manifest metadata -> ContributionRegistry -> host-rendered icon/action
user opens view -> protected session creation -> Webview preload bridge
guest request -> Electron sender/session validation -> Kun Broker -> Node Host
extension event -> bounded/replayable event channel -> owning View Session only
```

View Session 绑定扩展 ID、版本、贡献 ID、工作区、WebContents 和不可猜 nonce。调用方自报的身份或 session 不会改变绑定。Webview 资源只允许通过 `kun-extension://<extension-id>/...` 读取当前安装版本内声明的 resource roots。

## Agent、工具和 Provider 数据路径

扩展调用 Agent 时，Kun 创建或恢复一个持久化的 extension-owned thread，记录 owner、创建版本、profile、Provider/account、预算和 tool catalog epoch。事件来自 Kun 的持久化事件源，可按 sequence 重放。

Kun 调用扩展工具时，模型工具调用仍经过 `CapabilityRegistry -> ToolHost -> ExtensionToolProvider`。参数、审批、授权、取消、输出上限和历史顺序都由 Kun 控制。工具 Catalog 在 thread/epoch 边界固定，避免插件启停或注册顺序造成模型前缀漂移。

扩展 Provider 由 `RemoteModelClient` 归一化请求，再路由到 Node Host。Provider 返回有序的 text、reasoning、tool-call、usage 和 terminal 事件。选定 Provider 不可用时必须显式失败，不能静默切换 Provider、账号或同名模型。

## Headless 行为

GUI 关闭不会改变 Node 工具或 Provider 的注册和语义。相同 Kun data directory 下，GUI、`kun serve` 和 `kun exec` 观察同一 selected version、enablement、权限、熔断、状态和账号绑定。

需要登录、重新确认、审批或用户输入时，headless 路径返回结构化 `interaction-required`/gated 结果；不得隐式拉起 GUI，也不得因为没有 GUI 自动批准。

## 持久化边界

- 不可变包：`~/.kun/extensions/<publisher.name>/<version>/`。
- Registry：安装版本、active selection、来源、摘要、签名状态、权限快照和 enablement。
- 扩展数据：按扩展身份和 global/workspace scope 隔离，位于包目录之外。
- Host health：`~/.kun/extension-data/host-health.json` 保存扩展级 restart/circuit 等非秘密健康状态。
- 账号秘密：OS credential facility，必要时使用带认证的加密 fallback；普通设置只保存 account/credential reference。
- 日志：按扩展和进程实例分隔、轮转、限量并脱敏。

卸载包代码默认不删除状态、日志或账号引用；清除数据是单独的显式确认操作。

## 失败边界

单个扩展的激活错误、协议违规、超限或崩溃只能失败该扩展的调用。取消或 terminal fence 之后到达的消息被丢弃。对于可能已经产生外部副作用、但 Host 在确认结果前崩溃的工具，Kun 报告 unknown outcome，除非工具声明幂等且策略允许复用稳定 invocation key，否则不会自动重试。

## 公开与私有接口

扩展只能依赖官方 SDK、Schema、CLI、公开诊断、贡献点和文档。以下属于私有实现：

- Electron IPC channel 和 WebPreferences 细节；
- `window.kunGui` 与 renderer store/React module；
- Kun HTTP bearer token 和内部 `/v1/*` route shape；
- Node Host JSON IPC 与 `rpcVersion` wire format；
- `AgentLoop`、`ModelClient`、`ToolHost` 等内部类；
- 宿主 DOM/CSS/React 结构。

内部实现可以变化，只要受支持 API major 的公开行为保持兼容。
