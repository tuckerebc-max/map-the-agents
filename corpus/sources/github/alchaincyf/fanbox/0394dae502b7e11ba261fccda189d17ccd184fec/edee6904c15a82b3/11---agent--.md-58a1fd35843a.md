# 可配置 Agent 路线图（#38 建议一）

> 来源：社区 issue [#38](https://github.com/alchaincyf/fanbox/issues/38) 建议一。目标是把现在硬编码的 Claude Code / Codex 两个 agent，改成用户能在配置里自己声明任意 CLI agent（Aider、pi、SWE-agent 等）。

## 现状

FanBox 把「agent」这个概念硬编码成了 claude 和 codex 两套，散落在多处：

- 终端顶栏的启动按钮（写死两个）
- Agent 项目发现：扫 `~/.claude/projects` 和 `~/.codex/sessions` 出历史会话
- 续会话：`claude --resume` / `codex resume`
- AI 整理引擎：可选 claude / codex
- Skills 扫描：claude skills 体系
- 微信 ClawBot 大脑：`driver.js` 里 `runClaude` / `runCodex` 两条独立链路

## 目标配置形态

沿用 issue 里提的 `agents` 数组（放 settings.json）：

```json
{
  "agents": [
    { "id": "claude", "label": "Claude Code", "cmd": "claude --dangerously-skip-permissions", "sessionDir": "~/.claude/projects", "resumeCmd": "claude --dangerously-skip-permissions --resume" },
    { "id": "codex",  "label": "Codex",        "cmd": "codex",                                  "sessionDir": "~/.codex/sessions",  "resumeCmd": "codex resume" },
    { "id": "pi",     "label": "Pi AI",        "cmd": "pi",                                     "sessionDir": "~/.pi/agent/sessions", "resumeCmd": "pi -r" }
  ]
}
```

## 难点：纯配置覆盖不了「会话发现 / 续会话」

`cmd` / `label` 这种是纯字符串，配置即可。但**会话发现和续会话**没法只靠配置：

- claude 的会话落盘是 `~/.claude/projects/<编码后的cwd>/<uuid>.jsonl`，第一句话当标题、记录改过的文件、触发的 skill。
- codex 的会话落盘格式、thread_id 抓取、resume 调用方式都和 claude 不同。
- 第三方 agent（Aider 等）可能根本没有可读的会话历史。

所以要么放弃对自定义 agent 的「项目记忆 / 续会话」能力，要么为每个 agent 写一个**会话适配器**（怎么列会话、怎么取标题、怎么 resume）。

## 分两步落地

**第一步：纯配置能覆盖的（先发）**
- settings.json 读 `agents` 数组，终端顶栏启动按钮按它动态生成
- 自定义 `cmd` 启动、`label` 展示
- AI 整理引擎下拉、微信大脑选择都吃这份列表
- 没有会话适配器的 agent：只给「启动」，项目记忆/续会话区域显示「该 agent 暂不支持会话回溯」

**第二步：会话适配器（逐个补）**
- 定义一个适配器接口：`listSessions(cwd)` / `sessionTitle(s)` / `resumeArgs(id)` / `changedFiles(s)`
- 内置 claude / codex 两个适配器（把现有硬编码逻辑抽进去）
- 留扩展位，社区可按格式补别的 agent 适配器

## 不做 / 暂缓

- 不做 GUI 配置面板，先靠手编 settings.json（克制，等真有人用再说）
- 不替第三方 agent 猜会话格式，没有官方稳定落盘格式的就只给「启动」
- 不保证近期排期，记录在此备查
