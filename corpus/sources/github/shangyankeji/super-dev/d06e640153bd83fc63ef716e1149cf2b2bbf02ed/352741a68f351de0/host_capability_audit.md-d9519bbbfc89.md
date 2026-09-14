# Super Dev 宿主能力审计（2.4.0）

> 维护者文档。普通用户优先看 `docs/HOST_USAGE_GUIDE.md`，不需要先读这份审计表。

这份文档记录当前宿主矩阵的能力依据，只回答四件事：

1. 宿主官方公开了什么能力
2. Super Dev 当前采用哪种接入模型
3. 用户在宿主里应该输入什么
4. 当前结论属于什么级别

## 审计结论

| 宿主 | 当前接入模型 | 用户触发方式 | 官方依据 | 当前结论 |
| --- | --- | --- | --- | --- |
| Antigravity | recommended GEMINI.md + TOML commands + optional workflows model | `/super-dev 你的需求` | [Antigravity documentation](https://antigravity.im/documentation) | 当前按 `GEMINI.md + .gemini/commands/*.toml` 收敛到推荐接入模型；`.agent/workflows` 与 `~/.gemini/skills` 都只按增强层保留，不再过度宣称为唯一官方合同 |
| Claude Code | native slash + official `CLAUDE.md` + official skills + optional repo plugin enhancement | `/super-dev 你的需求` | [Claude Code slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) / [Claude Code memory](https://docs.anthropic.com/en/docs/claude-code/settings#claude-md-memory) / [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) | 当前按项目根 `CLAUDE.md` + `.claude/skills/` + `~/.claude/skills/` 收敛，`.claude/commands/` 与 `.claude/agents/` 作为兼容增强面保留，repo plugin enhancement 作为可选增强层 |
| Cline | official rules + official skills + AGENTS compatibility | `super-dev: 你的需求` | [Cline documentation](https://docs.cline.bot/) | 当前按 `.clinerules/super-dev.md` + `.cline/skills/` / `~/.cline/skills/` 建模，`AGENTS.md` 作为兼容增强面保留 |
| CodeBuddy CLI | native slash + official CODEBUDDY.md/skills/task continuity | `/super-dev 你的需求` | [CodeBuddy CLI slash commands](https://www.codebuddy.ai/docs/cli/slash-commands) / [CodeBuddy skills](https://www.codebuddy.ai/docs/cli/skills) / [CodeBuddy memory](https://www.codebuddy.ai/docs/cli/memory-and-rules) | CLI 模式已对齐 `CODEBUDDY.md` + `.codebuddy/commands/` + `.codebuddy/skills/`，任务连续性是主要官方闭环；`.codebuddy/AGENTS.md` 仅保留兼容观察面 |
| CodeBuddy | native slash + official CODEBUDDY.md/rules/skills/workspace continuity | `/super-dev 你的需求` | [CodeBuddy IDE integrations](https://www.codebuddy.ai/docs/cli/ide-integrations) / [CodeBuddy Subagents](https://www.codebuddy.ai/docs/ide/Features/Subagents) / [CodeBuddy skills](https://www.codebuddy.ai/docs/cli/skills) / [CodeBuddy IDE Rules](https://www.codebuddy.ai/docs/zh/ide/User-guide/Rules) | IDE 已收敛到 `CODEBUDDY.md` + `.codebuddy/rules/` + `.codebuddy/skills/` + workspace/task continuity，commands/agents 只作为当前增强层 |
| Cursor CLI | native slash + AGENTS compatibility | `/super-dev 你的需求` | [Cursor CLI slash commands](https://docs.cursor.com/en/cli/reference/slash-commands) / [Cursor CLI using](https://docs.cursor.com/en/cli/using) | slash 模式成立，官方文档确认 `.cursor/rules/` 之外还会读取项目根 `AGENTS.md` / `CLAUDE.md` |
| Cursor IDE | native slash + AGENTS compatibility | `/super-dev 你的需求` | [Cursor Agent commands](https://docs.cursor.com/en/agent/chat/commands) / [Cursor rules](https://docs.cursor.com/en/context/rules) | Agent Chat 命令模式可用，官方 rules 面与 `AGENTS.md` compatibility 已补进仓库模型 |
| Gemini CLI | native slash + official commands/GEMINI.md | `/super-dev 你的需求` | [Gemini CLI docs](https://google-gemini.github.io/gemini-cli/docs/) / [Gemini commands](https://google-gemini.github.io/gemini-cli/docs/cli/custom-commands.html) | 维持 slash 模式，项目级 `GEMINI.md` + `.gemini/commands/super-dev.toml` 与用户级 `~/.gemini/commands/` 已纳入正式接入面 |
| Kiro CLI | AGENTS.md + steering + skills + native resume | `/super-dev 你的需求` | [Kiro CLI](https://kiro.dev/docs/cli/) / [Kiro skills](https://kiro.dev/docs/cli/skills/) / [Kiro steering](https://kiro.dev/docs/steering/) / [Kiro slash entry changelog](https://kiro.dev/changelog/powers-auto-summarization-and-slash-commands) | 当前按 `.kiro/steering/` + `.kiro/skills/` + `~/.kiro/steering/` + `~/.kiro/skills/` 建模；steering 是长期上下文层，skills / slash 才是显式执行面 |
| Kiro IDE | AGENTS.md + steering + skills + agent continuity | `/super-dev 你的需求` | [Kiro steering](https://kiro.dev/docs/steering/) / [Kiro skills](https://kiro.dev/docs/cli/skills/) / [Kiro slash entry changelog](https://kiro.dev/changelog/powers-auto-summarization-and-slash-commands) | 当前按 project steering + project/global skills + `~/.kiro/steering/` 建模，不再把 steering 自身写成 slash entry |
| Kilo Code | official rules + compatibility skill | `super-dev: 你的需求` | [Kilo Code rules](https://kilocode.ai/docs/features/rules) | 规则面已收敛到 `.kilocode/rules/super-dev.md`，若检测到 `~/.kilocode/skills/` 则作为兼容增强路径协同生效 |
| OpenCode | native slash + official AGENTS/commands/skills | `/super-dev 你的需求` | [OpenCode commands](https://opencode.ai/docs/commands/) / [OpenCode skills](https://opencode.ai/docs/skills/) / [OpenCode agents](https://opencode.ai/docs/agents/) | slash/commands 模式成立，当前按 `AGENTS.md + commands + skills` 收敛；`.opencode/agents/` 继续作为增强层 |
| Qoder CLI | native slash + official AGENTS/rules/commands/skills | `/super-dev 你的需求` | [Qoder CLI](https://docs.qoder.com/cli/using-cli) / [Qoder rules](https://docs.qoder.com/zh/user-guide/rules) / [Qoder CLI skills](https://docs.qoder.com/cli/skills) / [Qoder commands](https://docs.qoder.com/zh/user-guide/commands) | CLI 模式可用，已改到 `AGENTS.md` + `.qoder/rules/` + `.qoder/commands/` + `.qoder/skills/`；`.qoder/agents/` 继续作为增强层 |
| Qoder IDE | native slash + official AGENTS/rules/commands/skills | `/super-dev 你的需求` | [Qoder rules](https://docs.qoder.com/zh/user-guide/rules) / [Qoder commands](https://docs.qoder.com/user-guide/commands) / [Qoder skills](https://docs.qoder.com/user-guide/skills) | 项目级 `AGENTS.md` + `.qoder/commands/super-dev.md` + `.qoder/rules/super-dev.md` + `.qoder/skills/` 协同生效；`.qoder/agents/` 与 `~/.qoder/agents/` 继续作为增强层 |
| Roo Code | native slash + official commands/rules | `/super-dev 你的需求` | [Roo Code slash commands](https://docs.roocode.com/features/slash-commands) / [Roo Code custom instructions](https://docs.roocode.com/features/custom-instructions) / [Roo Code custom modes](https://docs.roocode.com/features/custom-modes) | slash 与 `.roo/commands/`、`.roo/rules/` 都已按官方面建模，当前不再虚报未实际安装的 modes |
| VS Code Copilot | context/rules-first + text trigger | `super-dev: 你的需求` | [Copilot custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) | 当前按 `.github/copilot-instructions.md + AGENTS.md` 建模，兼容 Copilot Chat |
| Windsurf | native slash / workflow + official AGENTS/workflows/skills | `/super-dev 你的需求` | [Windsurf workflows](https://docs.windsurf.com/plugins/cascade/workflows) / [Windsurf skills](https://docs.windsurf.com/windsurf/cascade/memories#custom-skills) | workflow 命令模式成立，`AGENTS.md`、`.windsurf/workflows/` 与 skills 面已纳入正式接入面；`.windsurf/rules/` 继续作为项目约束层 |
| Codex | official AGENTS.md + official skills + enabled App/Desktop skill entry | `App/Desktop: /super-dev` / `CLI: $super-dev` / `回退: super-dev: 你的需求` | [Codex CLI](https://developers.openai.com/codex/cli) / [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md) / [Codex Skills](https://developers.openai.com/codex/skills) / [Codex app commands](https://developers.openai.com/codex/app/commands) / [Codex plugins](https://developers.openai.com/codex/plugins/build) | 不支持项目级自定义 slash；当前收敛为项目 `AGENTS.md` + 官方 skills。桌面端 `/` 列表里的 `super-dev` 是启用 Skill 的入口，CLI 优先 `$super-dev`，repo plugin enhancement 只保留为可选增强层 |
| Trae | recommended project context + compatibility rules/optional skills | `super-dev: 你的需求` | [Trae rules](https://docs.trae.ai/docs/what-is-trae-rules) | 公开文档确认 project/user rules；仓库当前把 `.trae/project_rules.md` + compatibility `rules.md` + optional skills 收成推荐项目上下文模型，而不是硬写唯一官方文件布局 |

## 当前产品规则

1. 支持原生 slash 的宿主：
   - 直接输入 `/super-dev 你的需求`
2. 不支持 slash 的宿主：
   - 直接输入 `super-dev: 你的需求`
3. Codex 属于单独的三入口模型：
   - App/Desktop 优先 `/` 列表里的 `super-dev`
   - CLI 优先 `$super-dev`
   - 回退仍可使用 `super-dev: 你的需求`
4. Antigravity 当前按 `GEMINI.md + .gemini/commands/*.toml + .agent/workflows` 收敛到推荐 slash 模式；项目级 workflow 与 Gemini 上下文会一起生效。
5. CodeBuddy、Qoder、Windsurf、OpenCode 这些宿主，官方文档已经公开 skills 面；Super Dev 当前按“宿主原生命令/规则/steering + Skills 协议”建模。
6. Trae 当前收敛到推荐 project context + compatibility rules/optional skills；Cline 已补齐 project/user skills；Kiro CLI / IDE 已收正为 steering 是上下文层、skills/slash 才是执行层；Qoder CLI / IDE 已收正为 AGENTS.md + commands + rules + official skills。
7. 接入完成后优先回宿主里做标准化触发与恢复验证；只有维护者在补正式验收证据时，才进入 `integrate smoke / validate` 维护链。

## 后续审计顺序

下一批继续做运行级收紧：

1. Claude Code
2. Codex CLI
3. Cursor / Cursor CLI
4. Qoder / Qoder CLI
5. VS Code Copilot / Trae

目标不是继续堆“支持列表”，而是把每个宿主都压到明确的真实入口模型：

- slash
- rules-first
- AGENTS + Skill
- workflow command

## 系统级适配执行规约（2.1.1）

为确保“不同宿主下体验一致”，当前仓库改为三层校验：

1. 声明层（Declared）
   - 每个宿主维护多条官方依据，而不是单 URL。
   - 这些依据由维护面生成和消费，不属于普通用户公开命令。
2. 在线层（Live Verify）
   - 维护面会对官方链接做在线可达性核验，并输出 `docs_checks` / `official_compares`。
3. 运行层（Runtime）
   - 普通用户优先在宿主里完成真实触发与恢复。
   - 维护者只在补真人验收闭环时，才进入 `integrate smoke / validate`。

4. 深适配层（System Harden）
   - 维护者对单宿主或全宿主执行深适配时，会产出 `output/*-host-hardening.{json,md}`。
   - 深适配报告同时输出 `host_parity_summary`，用于校验各宿主在触发格式、Smoke 语句、协议模式与能力标签上的一致体验。
   - 深适配报告同时输出 `host_gate_summary`，用于校验各宿主在 docs_confirm_gate 与 preview_confirm_gate 上的一致门禁行为。
   - 深适配报告同时输出 `host_runtime_script_summary`，用于校验各宿主在真人验收脚本（trigger + smoke prompt/signal + smoke steps）上的一致性。
   - 深适配报告同时输出 `host_recovery_summary`，用于校验各宿主在恢复命令模板（setup/skill/audit/onboard）上的一致性。
   - 深适配与审计同时输出 `host_parity_index`，并通过 `--parity-threshold` 执行总分门禁（默认 95.0，低于阈值即返回失败码）。
   - 深适配额外输出一页可读报告 `output/*-host-parity-onepage.md`，用于快速查看每个宿主的 PASS/FAIL、失败维度与下一条修复命令。

统一目标：

- 触发一致：支持 slash 的宿主统一 `/super-dev 需求`；不支持 slash 的宿主统一 `super-dev: 需求`。
- 协议一致：所有宿主都遵循 research → 三文档确认 → spec → 前端预览确认 → 后续交付。
- 能力一致：通过 `capability_labels` 统一表达 `slash/rules/skills/trigger`，避免宿主间语义漂移。
