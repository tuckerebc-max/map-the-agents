# ARCHITECTURE

最后更新：2026-02-27

## 1. Bird's-eye View

Formax 是一个“同一语义、三种入口”的代理系统：
1. 终端入口（CLI/TUI）
2. app-server 入口（JSON-RPC over stdio）
3. Web reference 入口（React 客户端）

系统目标不是“多端各写一套逻辑”，而是“共享同一语义核心，由不同 renderer 呈现”。

## 2. Code Map（粗粒度）

以下是稳定的模块地图，回答两个问题：
1. “功能 X 大概在哪一层？”
2. “我当前看的模块在整体里负责什么？”

### 2.1 Shared Semantics（语义真值）

`packages/core/src/features/semantics/*`

职责：
1. 定义 canonical event
2. 把 event 投影为 transcript/runtime 语义状态
3. 提供跨端一致的 input 生命周期与线程运行态

这是跨端行为的一致性核心，优先级高于任一端内实现细节。

### 2.2 Runtime Orchestration（运行编排）

1. REPL 编排：`packages/core/src/features/repl/controller/*`
2. app-server turn 执行：`packages/core/src/app-server/turnRunner.ts`
3. tool 执行与 preflight：`packages/core/src/tools/executor/*`
4. 会话保存与恢复：`packages/core/src/features/repl/sessionSave/*`

职责：把语义层接到实际运行流程（streaming、tool loop、session、interrupt）。

### 2.3 Interface Adapters（接口适配）

1. app-server 协议与传输：`packages/core/src/app-server/{protocol,server,transport}*`
2. Web runtime/state：`packages/web-reference-react/src/app/*`
3. TUI 屏幕与输入：`packages/core/src/screens/*`, `packages/core/src/components/*`

职责：协议适配、输入输出、渲染容器。这里不拥有语义真值。

### 2.4 Governance Docs（治理文档）

1. 顶层导航：`AGENTS.md`, `CODEMAP.md`, `ARCHITECTURE.md`
2. 合同/规范事实源：`docs/{contracts,references,frontend}/*` 与 `docs/environment-variables.md`
3. 过程计划与交接：`plans/app-server/{PRODUCT-SPEC.md,TODO-INDEX.md,HANDOFF.md}`

职责：定义可维护的“先改哪层、后改哪层”的工程秩序。

### 2.5 Minimal Dependency Graph（ASCII）

```text
                         +------------------------------+
                         | docs/contracts/*     |
                         | (normative contracts)        |
                         +---------------+--------------+
                                         |
                                         v
+----------------------------+   +-------------------------------+
| packages/core/src/features/semantics/*   |-->| packages/core/src/features/repl/controller/*|
| (canonical + projection)   |   | packages/core/src/app-server/turnRunner.ts  |
+-------------+--------------+   | packages/core/src/tools/executor/*          |
              |                  +---------------+---------------+
              |                                  |
              v                                  v
+----------------------------+       +----------------------------+
| app-server protocol/transport|     | session/runtime adapters   |
| packages/core/src/app-server/{protocol,...}|     | thread/input stores        |
+-------------+--------------+       +---------------+------------+
              |                                      |
              v                                      v
+----------------------------+          +-------------------------+
| TUI renderer               |          | Web renderer            |
| packages/core/src/screens/*              |          | packages/web-reference-react|
| packages/core/src/components/*           |          | packages/web-reference-react/src/components/*       |
+----------------------------+          +-------------------------+
```

读图约定：
1. 上到下表示“约束/语义 -> 编排 -> 适配 -> 渲染”的主流向。
2. 左右两侧 renderer 可不同步迭代 UI，但不能回写或分叉语义。
3. 合同文档是行为来源，代码实现应向合同收敛，而不是反过来。

## 3. Architectural Boundaries

### 3.1 语义边界

TUI / app-server / Web 必须共享 `packages/core/src/features/semantics/*` 语义模型。  
端内只允许做交互与渲染适配，不允许发明新的语义状态机分支。

### 3.2 输入与权限边界

`approval` / `ask_user_question` 统一走 `turn/inputRequested -> turn/input/submit -> turn/inputResolved`。  
policy/preflight 的解释与 remember 生效由执行层拥有，renderer 不得改写其语义。

### 3.3 文档边界

1. 合同（Normative）在 `docs/contracts/*`
2. 接口摘要与 UI 规范在 `docs/{references,frontend}/*`，不覆盖合同真值
3. `plans/app-server/*` 主要承载过程计划、交接与滚动 TODO
4. 同一能力不能存在两份同级权威说明

## 4. Architectural Invariants

1. Single semantic source: transcript 真值来自 semantics/projection，不是 renderer 拼接。
2. Single-writer discipline: 业务流程不绕过 canonical/projection 直接写最终 transcript。
3. Replay parity: realtime 与 replay 在同一事件序列下必须收敛到同一语义结果。
4. Ordering authority: 跨端排序主键是 `replaySeq`，不是本地时间顺序。
5. Input lifecycle closure: 每个 pending input 必须收敛到一个终态。

## 5. Cross-cutting Concerns

1. 配置分层：环境变量 + 全局配置 + 项目覆盖（见 `packages/core/src/config/config.ts` 与 `docs/environment-variables.md`）
2. 可观测性/审计：tool 执行、hook 运行、turn 事件需可追踪
3. 回归门禁：`type-check`、`test:repl-semantic-gate`、layer/golden principle 检查
4. 漂移治理：pitfalls 与 contracts 同步维护，禁止“代码改了文档没改”

## 6. Change Workflow（默认）

当改动语义或用户可见行为时：
1. 先更新事实源合同（`docs/contracts/*.md`）
2. 再改 semantics 与 adapter/runtime
3. 再改 TUI/Web renderer
4. 最后更新 `docs/{references,frontend,learnings}/*` 与相关测试（必要时同步 `plans/app-server/*` 过程文档）

## 7. References

1. OpenAI: [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/zh-Hans-CN/index/harness-engineering/)
2. Matklad: [ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html)

注：本文只记录“低频变化、跨模块稳定”的结构信息，不追求与每个实现细节逐行同步。
