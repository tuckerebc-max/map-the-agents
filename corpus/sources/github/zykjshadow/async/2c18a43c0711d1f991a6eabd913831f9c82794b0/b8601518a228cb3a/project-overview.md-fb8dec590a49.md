# 项目总览

- 状态：已根据 `README.md`、`README.zh-CN.md`、`package.json`、`main-src/index.ts`、`src/App.tsx` 校验。
- 主题：Async 作为产品的定位、边界和当前已实现能力。

## 一句话定义

Async IDE 是一个开源、桌面端、Agent-first 的 AI IDE Shell。它不是“给现有编辑器塞一个聊天侧栏”，而是把 Agent、编辑器、Git、终端、计划审阅、模型配置和工具执行放进同一个桌面工作区。

## 产品定位

- 对标对象：Cursor 一类 AI-native IDE 工作流。
- 交付方式：开源仓库，Apache 2.0。
- 模型接入：BYOK，支持 OpenAI-compatible、Anthropic、Gemini。
- 数据策略：本地优先，线程、设置、计划和大部分工作区状态都落本地。
- 技术基座：Electron 主进程 + React/Vite 渲染进程。

## 当前能力面

### Agent 与对话

- 支持 Agent、Plan、Ask、Debug 四类 Composer 模式。
- Agent 模式有多轮工具循环、工具参数流式展示、审批闸门、错误恢复。
- Team 模式允许 Team Lead + specialist/reviewer 角色编排。
- 支持嵌套子 Agent 和后台子 Agent。

### 编辑与工作区

- 使用 Monaco 作为编辑器。
- 使用 xterm.js 作为内嵌终端。
- 支持快速打开、文件树、差异预览、Agent 文件审阅。
- 工作区文件搜索、符号索引和 LSP 都有独立实现。

### 平台与集成

- 内置 Git 工作流：状态、diff、暂存、提交、推送、分支切换。
- 内置浏览器侧栏和浏览器工具。
- 支持 MCP 服务器配置与工具接入。
- 支持 Slack、Discord、Telegram、飞书等 bot 平台接入。
- 支持自动更新、使用统计、主题和布局配置。

## 产品边界

- 它更像一个“AI Shell”而不是全量通用 IDE。
- 主进程承担大量能力，所以很多行为不是前端组件就能解释清楚，必须同时看 `main-src/`。
- 运行时记忆体系分层明显：`docs/llm-wiki` 不是 `.async/memory` 的替代，而是更可审阅的上层知识层。

## 当前代码现实

- `main-src/` 是核心行为层，包含 Agent、LLM、IPC、存储、索引、MCP、shell、bot、browser 等。
- `src/` 是桌面 UI 和交互拼装层，很多复杂状态通过 hooks 组织。
- `electron/preload.cjs` 是 renderer 能访问主进程能力的白名单边界。

## 适合优先阅读的人

- 新接手这个仓库的开发者。
- 需要快速定位“某类功能归谁管”的 Agent。
- 需要判断“某个说法到底是 README 里的愿景还是代码里的现实”的维护者。

## Primary Sources

- `README.md`
- `README.zh-CN.md`
- `package.json`
- `main-src/index.ts`
- `src/App.tsx`

## 相关页面

- [仓库地图](./repo-map.md)
- [运行时架构](./architecture/runtime-architecture.md)
- [Agent 系统](./architecture/agent-system.md)
- [状态与记忆](./architecture/state-and-memory.md)

## 更新触发条件

- 产品定位发生变化。
- 新增或删除核心模式、平台集成、主流程能力。
- README 和实际代码出现显著偏差。
