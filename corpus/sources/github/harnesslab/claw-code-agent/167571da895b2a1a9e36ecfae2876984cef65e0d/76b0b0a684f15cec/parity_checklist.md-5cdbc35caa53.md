# Parity Checklist Against npm `src`

This document tracks what is already implemented in Python and what is still missing compared with the upstream npm runtime.

This is a functionality-oriented checklist, not a line-by-line source equivalence claim. Large parts of the mirrored Python workspace still act as inventory or scaffolding, while the working Python runtime currently lives mainly in [`src/agent_runtime.py`](src/agent_runtime.py), [`src/query_engine.py`](src/query_engine.py), [`src/agent_tools.py`](src/agent_tools.py), [`src/agent_prompting.py`](src/agent_prompting.py), [`src/agent_context.py`](src/agent_context.py), [`src/agent_manager.py`](src/agent_manager.py), [`src/plugin_runtime.py`](src/plugin_runtime.py), [`src/agent_slash_commands.py`](src/agent_slash_commands.py), [`src/openai_compat.py`](src/openai_compat.py), [`src/builtin_agents.py`](src/builtin_agents.py), [`src/microcompact.py`](src/microcompact.py), [`src/compact.py`](src/compact.py), [`src/bundled_skills.py`](src/bundled_skills.py), and [`src/session_memory_compact.py`](src/session_memory_compact.py).

---

## 1. Core Agent Runtime

Done:

- [x] One-shot agent loop with iterative tool calling
- [x] OpenAI-compatible `chat/completions` client
- [x] Streaming token-by-token assistant output
- [x] Local-model execution against `vLLM`
- [x] Local-model execution through `Ollama`
- [x] Local-model execution through `LiteLLM Proxy`
- [x] Transcript-aware session object for the Python runtime
- [x] Session save and resume support
- [x] Configurable max-turn execution
- [x] Permission-aware tool execution
- [x] Structured output / JSON schema request mode
- [x] Cost tracking and usage budget enforcement
- [x] Scratchpad directory integration
- [x] File history journaling for write/edit/shell tool actions
- [x] Incremental `bash` tool-result streaming events
- [x] Incremental tool-result streaming for read-only text tools
- [x] Incremental tool-result streaming across the current Python text tool surface
- [x] Mutable tool transcript updates during tool execution
- [x] Transcript mutation history for replaced/tombstoned messages
- [x] Assistant streaming and tool-call transcript mutation history
- [x] Session-wide mutation serial tracking across transcript updates
- [x] Structured transcript block export for messages, tool calls, and tool results
- [x] Resume-time file-history replay reminders
- [x] Resume-time file-history snapshot previews for file edits
- [x] File-history snapshot ids and replay summaries for file edits
- [x] File-history result previews for shell and delegated-tool entries
- [x] Truncated-response continuation flow for `finish_reason=length`
- [x] Basic snipping of older tool/tool-call messages for context control
- [x] Basic automatic compact-boundary insertion with preserved recent tail
- [x] Reactive compaction retry after prompt-too-long backend failures
- [x] Reasoning-token budget enforcement
- [x] Tool-call and delegated-task budget enforcement
- [x] Resume-aware cumulative model-call budgets
- [x] Resume-aware cumulative session usage/cost persistence
- [x] Basic nested-agent delegation tool
- [x] Sequential multi-subtask delegation with parent-context carryover
- [x] Dependency-aware delegated subtasks
- [x] Topological dependency-batch delegation planning
- [x] Basic agent-manager lineage tracking for nested agents
- [x] Managed agent-group membership tracking with child indices
- [x] Agent-manager strategy and batch summary tracking for delegated groups
- [x] Delegated child-session resume by saved session id
- [x] Agent-manager tracking for resumed child-session lineage
- [x] Plugin-cache discovery and prompt-context injection
- [x] Manifest-based plugin runtime discovery
- [x] Manifest-defined plugin hooks for before-prompt and after-turn runtime injection
- [x] Manifest-defined plugin lifecycle hooks for resume, persist, and delegate phases
- [x] Manifest-defined plugin tool aliases over base runtime tools
- [x] Manifest-defined executable virtual tools
- [x] Manifest-defined plugin tool blocking
- [x] Manifest-defined plugin `beforeTool` guidance
- [x] Manifest-defined plugin tool-result guidance injected back into the transcript
- [x] Plugin runtime session-state persistence and resume restoration
- [x] Manifest-based hook/policy runtime discovery
- [x] Hook/policy before-prompt runtime injection
- [x] Hook/policy after-turn runtime events
- [x] Hook/policy tool preflight guidance
- [x] Hook/policy tool blocking
- [x] Hook/policy after-tool guidance
- [x] Hook/policy budget override loading
- [x] Hook/policy safe-environment overlay for shell tools
- [x] Local manifest-backed MCP resource discovery
- [x] Local MCP resource listing and reading
- [x] MCP-backed runtime tools for local resource access
- [x] Real stdio MCP client transport for `initialize`, `resources/list`, `resources/read`, `tools/list`, and `tools/call`
- [x] Transport-backed MCP tool listing and execution
- [x] Local manifest-backed remote runtime discovery
- [x] Local remote profile listing and summary reporting
- [x] Local remote connect/disconnect state persistence
- [x] Local manifest/env-backed search runtime discovery
- [x] Local search-provider activation persistence
- [x] Provider-backed web search execution against configured search backends
- [x] Local heuristic LSP runtime for definitions, references, hover, document symbols, workspace symbols, call hierarchy, and diagnostics
- [x] Local persistent task runtime discovery
- [x] Local task create/get/list/update runtime flows
- [x] Local todo-list replacement runtime flow
- [x] Local persistent plan runtime discovery
- [x] Local plan get/update/clear runtime flows
- [x] Local plan-to-task sync flow
- [x] Dependency-aware local task state with blocking and actionable-task selection
- [x] Local task start/complete/block/cancel execution flows
- [x] Compaction metadata with compacted message ids
- [x] Compaction metadata with preserved-tail ids and compaction depth
- [x] Compaction metadata with compacted/preserved lineage ids and revision summaries
- [x] Compaction metadata with source mutation serials and mutation totals
- [x] Snipped-message metadata with source role/kind lineage
- [x] Snipped-message metadata with source lineage id and revision
- [x] Resume-time compaction / snipping replay reminder
- [x] Resume-time compaction replay of source mutation summaries
- [x] Preflight prompt-length validation before each model call
- [x] Hard prompt-length stop before backend calls when the effective input budget is exceeded
- [x] Token-budget calculation with projected prompt size, chat framing overhead, output reserve, and soft/hard input limits
- [x] Preflight auto-compact/context collapse fallback before the next model call
- [x] Query-engine facade that can drive the real Python runtime agent
- [x] Query-engine runtime event counters and transcript-kind summaries
- [x] Query-engine runtime mutation counters
- [x] Query-engine stream-level runtime summary event
- [x] Query-engine transcript-store compaction summaries
- [x] Delegate-group and delegated-subtask runtime events
- [x] Delegate-batch runtime events and summaries
- [x] Query-engine runtime orchestration summaries for group status and child stop reasons
- [x] Query-engine runtime context-reduction summaries
- [x] Query-engine runtime lineage summaries
- [x] Query-engine runtime resumed-child orchestration summaries
- [x] Filesystem-backed custom agent discovery from `~/.claude/agents` and `./.claude/agents`
- [x] Active agent override precedence across built-in, user, and project agent definitions
- [x] Custom agent resolution in the `Agent` tool with model, tool-filter, and initial-prompt support
- [x] Local custom-agent file creation, update, and deletion flows for project/user agent definitions

Missing:

- [ ] Full partial tool-result streaming parity across the complete upstream/npm tool surface
- [ ] Full rich transcript mutation behavior like the npm runtime beyond the current lineage, counters, block export, and mutation-serial tracking
- [ ] Full reasoning budgets and task budgets parity beyond the current cumulative model/tool/delegation/session-call enforcement
- [ ] Full multi-agent orchestration parity beyond dependency-aware batched delegation, resumed-child flows, and current agent-manager summaries
- [ ] Full file history snapshots and replay flows beyond the current preview/id-based implementation and delegated-batch replay metadata
- [ ] Full executable plugin lifecycle beyond manifest-driven prompt/tool/session hooks, blocking, aliases, virtual tools, and persisted runtime state
- [ ] Full session compaction / snipping parity beyond lineage-aware summaries, mutation-serial compaction metadata, and replay reminders
- [ ] Full `QueryEngine.ts` parity (session init, message normalization, SDK-compatible message transforms, attachment handling)
- [x] Auto-compact and context collapse features from `query.ts`
- [x] Prompt length validation from `query.ts`
- [x] Token budget calculations from `query/tokenBudget.ts`

## 2. CLI Entrypoints And Runtime Modes

Done:

- [x] Python CLI entrypoint
- [x] `agent` command
- [x] `agent-chat` command
- [x] `agent-resume` command
- [x] `agent-prompt` command
- [x] `agent-context` command
- [x] `agent-context-raw` command
- [x] `token-budget` command
- [x] `agents` command
- [x] `agents-create` command
- [x] `agents-update` command
- [x] `agents-delete` command
- [x] Local background session mode
- [x] Local background session listing (`agent-ps`)
- [x] Local background session logs (`agent-logs`)
- [x] Local background attach snapshot (`agent-attach`)
- [x] Local background kill flow (`agent-kill`)
- [x] Local daemon-style background command family (`daemon start/ps/logs/attach/kill`)
- [x] Local daemon worker command path (`daemon worker`)
- [x] Local remote runtime CLI modes (`remote-mode`, `ssh-mode`, `teleport-mode`, `direct-connect-mode`, `deep-link-mode`)
- [x] Local remote runtime inspection commands (`remote-status`, `remote-profiles`, `remote-disconnect`)
- [x] Local account runtime inspection commands (`account-status`, `account-profiles`, `account-login`, `account-logout`)
- [x] Local search runtime inspection commands (`search-status`, `search-providers`, `search-activate`, `search`)
- [x] Local LSP runtime inspection commands (`lsp-status`, `lsp-symbols`, `lsp-workspace-symbols`, `lsp-definition`, `lsp-references`, `lsp-hover`, `lsp-diagnostics`, `lsp-call-hierarchy`, `lsp-incoming-calls`, `lsp-outgoing-calls`)
- [x] Local MCP runtime inspection commands (`mcp-status`, `mcp-resources`, `mcp-resource`, `mcp-tools`, `mcp-call-tool`)
- [x] Inventory/helper commands such as `summary`, `manifest`, `commands`, and `tools`

Missing:

- [ ] Full daemon supervisor parity beyond the current local daemon wrapper and worker flow
- [ ] Remote-control / bridge runtime mode (`src/bridge/` — 30+ files: bridgeMain, bridgeApi, bridgeConfig, bridgeMessaging, bridgePermissionCallbacks, replBridge, sessionRunner, trustedDevice, etc.)
- [ ] Browser/native-host runtime mode
- [ ] Computer-use MCP mode (`src/entrypoints/mcp.ts`)
- [ ] Template job mode
- [ ] Environment runner mode
- [ ] Self-hosted runner mode
- [ ] tmux fast paths
- [ ] Worktree fast paths at the CLI entrypoint level
- [x] Python (Node.js equivalent) version check and platform detection from `setup.ts`
- [ ] Worktree creation/setup from `setup.ts`
- [ ] Terminal backup/restore from `setup.ts`
- [x] Release notes checking from `setup.ts` (local CHANGELOG.md, no network/cache layer)
- [ ] Full `entrypoints/cli.tsx` parity (version flag, feature flags, env setup, dynamic imports)
- [ ] Full `entrypoints/init.ts` parity (settings validation, OAuth, policy limits, telemetry, cleanup handlers)
- [ ] SDK entrypoint (`entrypoints/sdk/` — controlTypes, coreTypes, runtimeTypes, settingsTypes, toolTypes) — partial: HOOK_EVENTS, EXIT_REASONS, ModelUsage, ThinkingConfig, MCP server configs, JsonSchemaOutputFormat ported in `src/sdk_core_types.py`
- [x] Sandbox types/network config schema (`entrypoints/sandboxTypes.ts`)

## 3. Prompt Assembly

Done:

- [x] Structured Python system prompt builder
- [x] Intro/system/task/tool/tone/output sections
- [x] Session-specific prompt guidance
- [x] Environment-aware prompt sections
- [x] User context reminder injection
- [x] Custom system prompt override and append support
- [x] Local hook/policy guidance section in the Python system prompt
- [x] Local MCP guidance section in the Python system prompt
- [x] MCP transport/tool guidance section in the Python system prompt
- [x] Local remote-runtime guidance section in the Python system prompt
- [x] Local search-runtime guidance section in the Python system prompt
- [x] Local account-runtime guidance section in the Python system prompt
- [x] Local planning guidance section in the Python system prompt
- [x] Local task guidance section in the Python system prompt
- [x] Local LSP guidance section in the Python system prompt
- [x] Local agent-configuration guidance section in the Python system prompt

- [x] Product metadata/branding from `constants/product.ts` — ported to `src/prompt_constants.py`
- [x] API limits constants from `constants/apiLimits.ts` — ported to `src/prompt_constants.py`
- [x] Tool limits constants from `constants/toolLimits.ts` — ported to `src/prompt_constants.py`
- [x] Spinner verbs from `constants/spinnerVerbs.ts` (187 verbs) — ported to `src/prompt_constants.py`
- [x] Turn-completion verbs from `constants/turnCompletionVerbs.ts` (8 verbs) — ported to `src/prompt_constants.py`
- [x] Figures/UI symbols from `constants/figures.ts` — ported to `src/prompt_constants.py`
- [x] XML tag constants from `constants/xml.ts` — ported to `src/prompt_constants.py`
- [x] Message constants from `constants/messages.ts` — ported to `src/prompt_constants.py`
- [x] Date utilities from `constants/common.ts` — ported to `src/prompt_constants.py`
- [x] System prompt section caching from `constants/systemPromptSections.ts` — ported to `src/prompt_constants.py`
- [x] Output-style variants from `constants/outputStyles.ts` — ported to `src/prompt_constants.py`
- [x] Cyber / risk instruction from `constants/cyberRiskInstruction.ts` — ported to `src/prompt_constants.py`
- [x] System prompt prefixes from `constants/system.ts` — ported to `src/prompt_constants.py`
- [x] Knowledge cutoff / model family info from `constants/prompts.ts` — ported to `src/prompt_constants.py`
- [x] Hook instruction section template — ported to `src/prompt_constants.py`
- [x] System reminders section — ported to `src/prompt_constants.py`
- [x] Summarize tool results section — ported to `src/prompt_constants.py`
- [x] Language-control section helper — ported to `src/prompt_constants.py`
- [x] Scratchpad prompt instructions helper — ported to `src/prompt_constants.py`
- [x] Default agent prompt — ported to `src/prompt_constants.py`

Missing:

- [ ] Full parity with `constants/prompts.ts` runtime section assembly (many sections already exist in agent_prompting.py)
- [ ] MCP instruction sections (runtime MCP integration)
- [ ] Model-family-specific prompt variations (runtime)
- [ ] More exact autonomous/proactive behavior sections
- [ ] Growthbook / feature-gated prompt sections (N/A for external builds)

## 4. Context Building And Memory

Done:

- [x] Current working directory snapshot
- [x] Shell / platform / date capture
- [x] Git status snapshot
- [x] `CLAUDE.md` discovery
- [x] Extra directory injection through `--add-dir`
- [x] Session context usage report
- [x] Tokenizer-aware context accounting with cached model-specific backends and heuristic fallback
- [x] Raw context inspection command
- [x] Plugin cache snapshot injection
- [x] Manifest-based plugin runtime summary injection
- [x] Manifest-based hook/policy summary injection
- [x] Trust-mode, managed-settings, and safe-env context injection
- [x] Manifest-based MCP runtime summary injection
- [x] Manifest-based MCP transport server summary injection
- [x] Manifest-based remote runtime summary injection
- [x] Manifest/env-based search runtime summary injection
- [x] Manifest-based account runtime summary injection
- [x] Local LSP runtime summary injection
- [x] Manifest-based plan runtime summary injection
- [x] Manifest-based task runtime summary injection

Missing:

- [ ] Full tokenizer/chat-message framing parity beyond the current model-aware text token counters
- [ ] Full parity with `utils/queryContext.ts` (context analysis, suggestions, cache shaping)
- [x] Session memory compact (`services/SessionMemory/` partial) → `src/session_memory_compact.py` — remaining: background LLM extraction, full template handling
- [ ] Internal permission-aware memory handling
- [ ] Resume-aware prompt cache shaping used upstream
- [ ] More exact context cache invalidation rules
- [ ] Session context analysis parity (`utils/contextAnalysis.ts`, `utils/contextSuggestions.ts`)
- [ ] Full memory subsystem parity (`utils/memory/`, `services/extractMemories/`)
- [ ] Memory extraction from conversations (`services/extractMemories/extractMemories.ts`)
- [ ] Team memory sync (`services/teamMemorySync/`)
- [ ] Away summary generation (`services/awaySummary.ts`)
- [ ] Token estimation service (`services/tokenEstimation.ts`)
- [x] Paste content storage and reference parsing (`history.ts`) → `src/paste_refs.py` (parse/format/expand `[Pasted text #N +M lines]`); GUI composer auto-collapses pastes ≥500 chars and ships them via `pasted_contents` for server-side expansion before `agent.run`
- [ ] Image paste handling

## 5. Slash Commands

Done (53 slash command names in 37 specs):

- [x] `/help`, `/commands`
- [x] `/context`, `/usage`
- [x] `/context-raw`, `/env`
- [x] `/token-budget`, `/budget`
- [x] `/mcp` (with subcommands: `tools`, `tool <name>`)
- [x] `/search` (with subcommands: `providers`, `provider`, `use`)
- [x] `/remote` (with `enter`, `exit`)
- [x] `/worktree` (with `enter`, `exit`)
- [x] `/account` (with `profiles`, `profile`)
- [x] `/ask` (with `history`)
- [x] `/login`
- [x] `/logout`
- [x] `/config`, `/settings` (with `effective`, `source`, `get`, `set`)
- [x] `/remotes`
- [x] `/ssh`
- [x] `/teleport`
- [x] `/direct-connect`
- [x] `/deep-link`
- [x] `/disconnect`, `/remote-disconnect`
- [x] `/resources`
- [x] `/resource`
- [x] `/tasks`, `/todo`
- [x] `/workflows`, `/workflow`
- [x] `/triggers`, `/trigger`
- [x] `/teams`, `/team`, `/messages`
- [x] `/task-next`, `/next-task`
- [x] `/plan`, `/planner`
- [x] `/task`
- [x] `/prompt`, `/system-prompt`
- [x] `/permissions`
- [x] `/hooks`, `/policy`
- [x] `/trust`
- [x] `/model`
- [x] `/tools`
- [x] `/memory`
- [x] `/status`, `/session`
- [x] `/clear`

Missing npm slash commands (from `src/commands/` — 80+ commands total):

- [x] `/add-dir` — Add a new working directory
- [x] `/agents` — Inspect, create, update, and delete local agent definitions
- [x] `/branch` — Create a branch of the current conversation
- [x] `/bridge` — Connect for remote-control sessions (read-only status in this runtime)
- [x] `/btw` — Quick side question without interrupting main conversation
- [x] `/chrome` — Chrome extension settings
- [x] `/color` — Set the prompt bar color for this session
- [x] `/compact` — Clear history but keep a summary in context
- [x] `/copy` — Copy Claude's last response to clipboard
- [x] `/cost` — Show total cost and duration of session
- [x] `/desktop` — Continue session in Claude Desktop
- [x] `/diff` — View uncommitted changes and per-turn diffs
- [x] `/doctor` — Diagnose and verify installation and settings
- [x] `/effort` — Set effort level for model usage
- [x] `/exit` — Exit the REPL
- [x] `/export` — Export conversation to file or clipboard
- [x] `/extra-usage` — Configure extra usage for rate limits
- [x] `/fast` — Toggle fast mode
- [x] `/feedback` — Submit feedback (alias `/bug`)
- [x] `/files` — List all files currently in context
- [x] `/ide` — Manage IDE integrations and show status
- [x] `/install-github-app` — Set up GitHub Actions
- [x] `/install-slack-app` — Install Slack app
- [x] `/keybindings` — Open keybindings config file
- [x] `/mobile` — Mobile app store links (aliases `/ios`, `/android`)
- [x] `/output-style` — Deprecation pointer to `/config`
- [x] `/passes` — Passes management
- [x] `/plugin` — Plugin management (read-only listing)
- [x] `/pr-comments`, `/pr_comments` — Get comments from a GitHub PR (prompt-type)
- [x] `/privacy-settings` — View/update privacy settings
- [x] `/rate-limit-options` — Show options when rate limited
- [x] `/release-notes` — View release notes
- [x] `/reload-plugins` — Activate pending plugin changes
- [x] `/remote-env` — Configure default remote environment
- [x] `/remote-setup` — Remote setup configuration (gh auth status + Claude.ai/code link)
- [x] `/rename` — Rename current conversation
- [x] `/resume`, `/continue` — Resume a previous conversation
- [x] `/rewind`, `/checkpoint` — Restore code/conversation to a previous point
- [x] `/sandbox-toggle` — Toggle sandbox mode (alias `/sandbox`)
- [x] `/skills` — List available bundled skills (mirrors `commands/skills/SkillsMenu.tsx`; lists `bundled_skills.BUNDLED_SKILLS`, not slash commands)
- [x] `/stats` — Usage statistics and activity
- [x] `/stickers` — Order stickers
- [x] `/tag` — Toggle a searchable tag on the session
- [x] `/theme` — Change the theme
- [x] `/upgrade` — Upgrade to Max
- [x] `/vim` — Toggle Vim/Normal editing modes
- [x] `/voice` — Toggle voice mode
- [ ] Feature-gated: `/buddy`, `/fork`, `/peers`, `/proactive`, `/torch`, `/workflows` (full), etc.
- [ ] Internal: `/backfill-sessions`, `/break-cache`, `/bughunter`, `/commit-push-pr`, `/init-verifiers`, `/mock-limits`, `/version`, `/ultraplan`, `/autofix-pr`, etc.
- [x] `/commit` — Create a git commit (prompt-type with injected git context)
- [ ] Full `/agents` parity for interactive TUI/editor flows, plugin sources, and full multi-source management UX

## 6. Built-in Tools

### Tools implemented in Python (65 tools):

- [x] `list_dir`
- [x] `read_file`
- [x] `write_file`
- [x] `edit_file`
- [x] `notebook_edit`
- [x] `glob_search`
- [x] `grep_search`
- [x] `bash`
- [x] `web_fetch`
- [x] `search_status`
- [x] `search_list_providers`
- [x] `search_activate_provider`
- [x] `web_search`
- [x] `LSP`
- [x] `tool_search`
- [x] `sleep`
- [x] `ask_user_question`
- [x] `account_status`
- [x] `account_list_profiles`
- [x] `account_login`
- [x] `account_logout`
- [x] `config_list`
- [x] `config_get`
- [x] `config_set`
- [x] `mcp_list_resources`
- [x] `mcp_read_resource`
- [x] `mcp_list_tools`
- [x] `mcp_call_tool`
- [x] `remote_status`
- [x] `remote_list_profiles`
- [x] `remote_connect`
- [x] `remote_disconnect`
- [x] `worktree_status`
- [x] `worktree_enter`
- [x] `worktree_exit`
- [x] `workflow_list`
- [x] `workflow_get`
- [x] `workflow_run`
- [x] `remote_trigger`
- [x] `plan_get`
- [x] `update_plan`
- [x] `plan_clear`
- [x] `task_next`
- [x] `task_list`
- [x] `task_get`
- [x] `task_create`
- [x] `task_update`
- [x] `task_start`
- [x] `task_complete`
- [x] `task_block`
- [x] `task_cancel`
- [x] `todo_write`
- [x] `delegate_agent`
- [x] `team_list`
- [x] `team_get`
- [x] `team_create`
- [x] `team_delete`
- [x] `send_message`
- [x] `team_messages`
- [x] `EnterPlanMode`
- [x] `ExitPlanMode`
- [x] `TaskOutput`
- [x] `TaskStop`

### Tools in npm `tools.ts` not yet ported with full fidelity (40 tool dirs):

Core tools needing full port:
- [x] `AgentTool` — Sub-agent spawning with built-in agents (explore, general-purpose, verification, plan, claudeCodeGuide, statusline) → `src/builtin_agents.py` — remaining: fork support, agent memory/snapshots, resume agent, color management
- [x] `SkillTool` — Skill execution via slash commands and bundled skills → `src/agent_tools.py`, `src/agent_runtime.py`, `src/bundled_skills.py` — remaining: forked skill execution
- [ ] `BriefTool` — Brief mode with attachments and file upload
- [ ] `LSPTool` — Full upstream LSP fidelity beyond the current local heuristic runtime (server-backed diagnostics, go-to-definition, references, hover, symbol search, formatting)
- [ ] `PowerShellTool` — Full PowerShell execution with security, path validation, CLM types, git safety
- [ ] `REPLTool` — Interactive REPL with primitive tools (ant-only)
- [ ] `MCPTool` — Full MCP tool execution with collapse classification
- [ ] `McpAuthTool` — MCP authentication handling
- [ ] `ConfigTool` — Full config management with supported settings list
- [ ] `SyntheticOutputTool` — Synthetic output injection
- [x] `EnterPlanModeTool` — Enter plan mode → `src/agent_tools.py`
- [x] `ExitPlanModeTool` — Exit plan mode → `src/agent_tools.py`
- [ ] `EnterWorktreeTool` — Full worktree enter with UI
- [ ] `ExitWorktreeTool` — Full worktree exit with UI
- [x] `TaskOutputTool` — Task output display → `src/agent_tools.py`
- [x] `TaskStopTool` — Stop a running task → `src/agent_tools.py`

Feature-gated tools:
- [ ] `CronCreateTool` / `CronDeleteTool` / `CronListTool` — Cron scheduling (AGENT_TRIGGERS)
- [ ] `RemoteTriggerTool` — Full remote triggers with UI (AGENT_TRIGGERS_REMOTE)
- [ ] `MonitorTool` — MCP server monitoring (MONITOR_TOOL)
- [ ] `SendUserFileTool` — Send file to user (KAIROS)
- [ ] `PushNotificationTool` — Push notifications (KAIROS)
- [ ] `SubscribePRTool` — PR subscription (KAIROS_GITHUB_WEBHOOKS)
- [ ] `SuggestBackgroundPRTool` — Background PR (ant-only)
- [ ] `VerifyPlanExecutionTool` — Plan verification
- [ ] `TungstenTool` — Tungsten tool
- [ ] `WebBrowserTool` — Full web browser
- [ ] `TerminalCaptureTool` — Terminal capture
- [ ] `SnipTool` — Force history snipping
- [ ] `ListPeersTool` — List peers (UDS_INBOX)
- [ ] `EmbeddedSearchTool` — Embedded search
- [ ] `CtxInspectTool` — Context inspection
- [ ] `WorkflowTool` — Workflow scripts (WORKFLOW_SCRIPTS)

Note: Python has basic tool execution for `bash`, `read_file`, etc., but lacks per-tool UI components, prompt files, constants, and deep security validations (e.g., BashTool has 15 supporting files in npm).

## 7. Commands And Task Systems

Done:

- [x] Basic local command dispatch for the Python runtime
- [x] Inventory view of mirrored command names
- [x] Local persistent task runtime with create/get/list/update flows
- [x] Local todo-list replacement flow
- [x] Local persistent plan runtime with get/update/clear flows
- [x] Local plan-to-task sync flow
- [x] Local dependency-aware task execution flow with next-task selection and blocked/unblocked state
- [x] Local remote profile/runtime flow with persisted connect/disconnect state
- [x] Local background task management for agent worker sessions
- [x] Local ask-user runtime with queued answers, history, and slash/CLI inspection flows
- [x] Local team runtime with persisted teams, messages, and slash/CLI inspection flows
- [x] Local workflow runtime with manifest discovery, run history, and workflow CLI/slash flows
- [x] Local remote trigger runtime with create/update/run flows and trigger CLI/slash flows
- [x] Local managed git worktree runtime with session cwd switching and worktree CLI/slash flows

Missing:

- [ ] Real implementation of the larger upstream command tree (80+ commands)
- [ ] Task types: `LocalShellTask`, `LocalAgentTask`, `RemoteAgentTask`, `DreamTask`, `LocalWorkflowTask`, `MonitorMcpTask`, `InProcessTeammateTask`
- [ ] Task stall detection (45s threshold) and prompt detection for interactive input
- [ ] Remote agent task session URL tracking and completion checkers
- [ ] Dream/auto-consolidation task with file tracking and turn history
- [ ] Task orchestration system beyond the current local dependency-aware task runtime
- [ ] Planner / task execution parity beyond the current local plan persistence, sync, and next-task flow
- [ ] Team / collaboration command flows beyond the current local team runtime and message recording flows
- [ ] Command-specific session behaviors
- [ ] Full `src/commands/*` parity (80+ command directories)
- [ ] Full `src/tasks/*` parity (7 task types)

## 8. Permissions, Hooks, And Policy

Done:

- [x] Read-only default mode
- [x] Write-gated mode
- [x] Shell-gated mode
- [x] Unsafe mode for destructive shell actions
- [x] Local hook/policy manifest discovery
- [x] Hook before-prompt and after-turn runtime handling
- [x] Hook/policy tool preflight, deny, and after-tool handling
- [x] Policy budget override loading
- [x] Managed settings loading and reporting
- [x] Safe environment loading for shell tool context
- [x] Trust reporting and hook/policy slash commands
- [x] Permission-denial runtime events for policy/tool blocks

Missing:

- [x] Full BashTool security: `bashSecurity.ts`, `sedValidation.ts`, `sedEditParser.ts`, `pathValidation.ts`, `readOnlyValidation.ts`, `modeValidation.ts`, `commandSemantics.ts`, `destructiveCommandWarning.ts`, `shouldUseSandbox.ts` → `src/bash_security.py` (18 validators, destructive warnings, command semantics, read-only detection, 163 tests)
- [ ] Full PowerShellTool security: `powershellSecurity.ts`, `gitSafety.ts`, `clmTypes.ts`
- [ ] Tool-permission workflow parity (`bashPermissions.ts`, `powershellPermissions.ts`)
- [ ] Trust-gated initialization
- [ ] Hook-config management (`schemas/hooks.ts` with Zod schemas)
- [ ] Policy limits service (`services/policyLimits/`)
- [ ] Remote managed settings (`services/remoteManagedSettings/`)
- [ ] Full hooks and policy parity

## 9. MCP, Plugins, And Skills

Done:

- [x] Placeholder mirrored package layout for plugins, skills, services, and remote subsystems
- [x] Local manifest-backed MCP discovery
- [x] Local MCP resource listing and reading
- [x] MCP-backed runtime tools for local resource access
- [x] Real MCP client support over local stdio transport
- [x] MCP server integration for stdio child-process servers
- [x] MCP-backed tool listing and execution over transport

Missing:

- [ ] Full MCP service (`services/mcp/` — 25+ files: InProcessTransport, MCPConnectionManager, SdkControlTransport, auth, channelAllowlist, channelPermissions, client, config, elicitationHandler, envExpansion, normalization, oauthPort, officialRegistry, vscodeSdkMcp, xaa, xaaIdpLogin, etc.)
- [ ] MCP server approval dialogs (`services/mcpServerApproval.tsx`)
- [ ] Plugin discovery, loading, and installation (`services/plugins/PluginInstallationManager.ts`, `pluginCliCommands.ts`, `pluginOperations.ts`)
- [ ] Bundled plugin support (`plugins/bundledPlugins.ts`, `plugins/bundled/`)
- [ ] Plugin lifecycle management
- [ ] Plugin update/cache behavior
- [x] Skill discovery and execution → `src/bundled_skills.py` (simplify, verify, debug, update-config) — remaining: loadSkillsDir, mcpSkillBuilders, disk-based SKILL.md loading
- [x] Bundled skill support → `src/bundled_skills.py` — remaining: skillify, batch, loop, schedule, claude-api, chrome, and feature-gated skills
- [ ] Full plugin and skill parity

## 10. Interactive UI / REPL / TUI

Done:

- [x] Non-interactive CLI execution
- [x] Basic interactive REPL-style agent chat loop
- [x] Transcript printing for debugging

Missing:

- [ ] Interactive REPL parity (`screens/REPL.tsx`)
- [ ] Ink/TUI framework (`ink/` — 40+ files: custom renderer, reconciler, DOM, layout engine, text wrapping, ANSI handling, focus management, selection)
- [ ] Screen system (`screens/Doctor.tsx`, `screens/ResumeConversation.tsx`)
- [ ] Component library (`components/` — 100+ components in 12+ subdirectories):
  - Message rendering: Message, MessageRow, Messages, MessageSelector, MessageResponse
  - Dialogs: ApproveApiKey, AutoModeOptIn, Bridge, CostThreshold, IdeAutoConnect, MCPServerApproval
  - Settings: ThemePicker, LanguagePicker, ModelPicker, OutputStylePicker
  - Search: GlobalSearchDialog, QuickOpenDialog, HistorySearchDialog
  - Status: AgentProgressLine, BashModeProgress, MemoryUsageIndicator, TokenWarning
  - Design system, agent, team, task, skill, memory, permissions, sandbox, shell components
- [ ] Keyboard interaction parity
- [ ] Interactive status panes
- [ ] Approval UI flows
- [ ] Rich incremental rendering
- [ ] Virtual scrolling
- [ ] Copy-on-select behavior

## 11. Remote, Background, And Team Features

Done:

- [x] Session save/resume on local disk
- [x] Local manifest-backed remote profile/runtime state
- [x] Local remote connect/disconnect session state
- [x] Local background agent processes
- [x] Local background attach/log/kill workflows
- [x] Local daemon-style wrapper over background agent sessions

Missing:

- [ ] Real remote session management (`remote/` — 4 files: RemoteSessionManager, SessionsWebSocket, remotePermissionBridge, sdkMessageAdapter)
- [ ] Bridge subsystem (`bridge/` — 30+ files: bridgeMain, bridgeApi, bridgeConfig, bridgeMessaging, bridgePermissionCallbacks, replBridge, replBridgeHandle, replBridgeTransport, sessionRunner, trustedDevice, jwtUtils, capacityWake, inboundAttachments, inboundMessages, etc.)
- [ ] Direct connect subsystem (`server/createDirectConnectSession.ts`, `directConnectManager.ts`)
- [ ] Real team collaboration beyond local recording
- [ ] Shared remote state
- [ ] Upstream proxy (`upstreamproxy/upstreamproxy.ts`, `upstreamproxy/relay.ts`)

## 12. Editor, Platform, And Native Integrations

Done:

- [x] Standard shell-based local workflow

Missing:

- [ ] Voice mode (`voice/`, `services/voice.ts`, `services/voiceKeyterms.ts`, `services/voiceStreamSTT.ts`, hooks)
- [ ] VIM mode (`vim/` — 5 files: motions, operators, textObjects, transitions, types)
- [ ] Keybinding system (`keybindings/` — 13 files: defaultBindings, loadUserBindings, match, parser, resolver, schema, template, validate, etc.)
- [ ] Notification hooks (`services/notifier.ts`, `services/preventSleep.ts`)
- [ ] Native TypeScript / platform helpers (`native-ts/`)
- [ ] JetBrains/editor integration (`utils/jetbrains.ts`, `utils/ide.ts`, `utils/idePathConversion.ts`)
- [ ] Browser/native host integrations
- [ ] IDE integration hooks (useIDEIntegration, useIdeAtMentioned, useIdeSelection, useIdeLogging, useDiffInIDE, useLspPluginRecommendation)
- [ ] Platform-specific startup/shutdown logic
- [ ] Chrome extension integration

## 13. Services And Internal Subsystems

Done:

- [x] Minimal internal service layer required by the current Python runtime
- [x] Local account/auth runtime for manifest-backed profile discovery and persisted login state

Missing:

- [ ] Analytics service (`services/analytics/` — 10+ files: config, Datadog, Growthbook, first-party event logger, sink, killswitch)
- [ ] API service (`services/api/` — 20+ files: claude client, dumpPrompts, errorUtils, filesApi, firstTokenDate, grove, logging, metricsOptOut, promptCacheBreakDetection, sessionIngress, usage, withRetry, etc.)
- [ ] LSP service (`services/lsp/` — 7 files: LSPClient, LSPDiagnosticRegistry, LSPServerInstance, LSPServerManager, config, manager, passiveFeedback)
- [ ] Tools service (`services/tools/` — 4 files: StreamingToolExecutor, toolExecution, toolHooks, toolOrchestration)
- [ ] Compact service (`services/compact/` — 6 files) — partially ported: compact → `src/compact.py`, microCompact → `src/microcompact.py`, sessionMemoryCompact → `src/session_memory_compact.py`; remaining: autoCompact trigger, apiMicrocompact, compactWarningHook
- [ ] Auto-dream service (`services/autoDream/` — 4 files: autoDream, config, consolidationLock, consolidationPrompt)
- [ ] Agent summary service (`services/AgentSummary/`)
- [ ] Magic docs service (`services/MagicDocs/`)
- [ ] Session memory service (`services/SessionMemory/`)
- [ ] Prompt suggestion service (`services/PromptSuggestion/`)
- [ ] Extract memories service (`services/extractMemories/`)
- [ ] Diagnostic tracking service (`services/diagnosticTracking.ts`)
- [ ] OAuth service (`services/oauth/` — 5 files)
- [ ] Rate limiting (`services/claudeAiLimits.ts`, `services/rateLimitMessages.ts`, etc.)
- [ ] Settings sync (`services/settingsSync/`)
- [ ] Tips service (`services/tips/`)
- [ ] Tool use summary service (`services/toolUseSummary/`)
- [ ] VCR playback (`services/vcr.ts`)
- [ ] Internal/container logging (`services/internalLogging.ts`)
- [ ] Plugin installation management (`services/plugins/`)

## 14. State Management

Done:

- [x] Session state via `AgentSessionState` dataclass
- [x] Basic session persistence

Missing:

- [ ] Zustand store (`state/AppStateStore.ts`, `state/store.ts`)
- [ ] Store selectors (`state/selectors.ts`)
- [ ] State change callbacks (`state/onChangeAppState.ts`)
- [ ] React context providers (`state/AppState.tsx`)

## 15. React Hooks (84+ hooks in `src/hooks/`)

Not applicable for Python (no React TUI), but these represent features needing alternative implementations:

- [ ] File suggestions and unified suggestions
- [ ] Remote session / SSH / direct connect hooks
- [ ] Input buffer, text input, vim input, typeahead, search input, paste handling
- [ ] Arrow key history, history search, background task navigation
- [ ] Main loop model selection, assistant history, merged clients/commands/tools
- [ ] Tool permission checking, cancel request, manage plugins
- [ ] Global/command keybindings, exit handling, double-press detection
- [ ] Terminal size, virtual scroll, copy-on-select
- [ ] Voice recording, voice integration
- [ ] IDE integration, @mention, selection, diff-in-IDE
- [ ] Settings management, dynamic config
- [ ] Timeout, elapsed time, scheduled tasks, delayed notifications
- [ ] Prompt suggestion, update notification, feature hints
- [ ] Queue processor, command queue
- [ ] Memory usage, away summary, teleport resume
- [ ] Diff data, turn diffs
- [ ] Task list watcher, tasks v2, PR status
- [ ] Session backgrounding, swarm initialization/permission
- [ ] API key verification, mailbox bridge, inbox poller

## 16. Utilities (200+ files in `src/utils/`)

Done:

- [x] Basic file operations in tool implementations
- [x] Basic git status snapshot
- [x] Basic shell/subprocess handling
- [x] Bundled small portable utilities — `utils/array.ts`, `utils/set.ts`, `utils/objectGroupBy.ts`, `utils/xml.ts`, `utils/uuid.ts` ported in `src/small_utils.py`
- [x] Session-scoped env-var registry (`utils/sessionEnvVars.ts`) ported in `src/session_env_vars.py`, merged into spawned subprocess env via `_build_subprocess_env` (mirrors `utils/shell/bashProvider.ts`), and dropped on `/clear` via `clear_runtime_state` (mirrors `commands/clear/caches.ts`)
- [x] Display formatters from `utils/format.ts` (`formatFileSize`, `formatSecondsShort`, `formatDuration`, `formatNumber`, `formatTokens`) ported in `src/format_utils.py`

Missing major utility categories:

- [ ] Shell utilities (`utils/bash/`, `utils/shell/`, `Shell.ts`, `ShellCommand.ts`)
- [ ] Git operations (`utils/git.ts`, `utils/gitDiff.ts`, `utils/gitSettings.ts`, `utils/commitAttribution.ts`) — partial: `findGitRoot`, `normalizeGitRemoteUrl`, `getRepoRemoteHash`, and `shouldIncludeGitInstructions` ported in `src/git_utils.py`
- [ ] File operations (`utils/file.ts`, `utils/fileRead.ts`, `utils/fileHistory.ts`, `utils/fileStateCache.ts`, `utils/fsOperations.ts`, `utils/ripgrep.ts`, `utils/glob.ts`)
- [ ] AI/Model utilities (`utils/modelCost.ts`, `utils/model/`, `utils/context.ts`, `utils/queryContext.ts`) — partial: modelCost ported in `src/model_cost.py`
- [ ] Config/Settings (`utils/config.ts`, `utils/settings/`)
- [ ] Message handling (`utils/messages.ts`, `utils/messages/`, `utils/messageQueueManager.ts`)
- [ ] API/Network (`utils/api.ts`, `utils/http.ts`, `utils/proxy.ts`, `utils/auth.ts`)
- [ ] Session management (`utils/sessionStorage.ts`, `utils/sessionState.ts`, `utils/sessionStart.ts`, `utils/sessionRestore.ts`)
- [ ] Plugin/Skill utilities (`utils/plugins/`, `utils/skills/`)
- [ ] Memory/Context (`utils/memory/`, `utils/claudemd.ts`, `utils/contextAnalysis.ts`)
- [ ] IDE integration (`utils/ide.ts`, `utils/jetbrains.ts`) — partial: `utils/idePathConversion.ts` ported in `src/ide_path_conversion.py` (`WindowsToWSLConverter`, `checkWSLDistroMatch`)
- [ ] Platform/OS (`utils/platform.ts`, `utils/terminal.ts`, `utils/systemDirectories.ts`) — partial: platform detection (`getPlatform`, `getWslVersion`, `getLinuxDistroInfo`, `detectVcs`) and `getSystemDirectories` ported in `src/platform_info.py`
- [ ] Debugging (`utils/debug.ts`, `utils/diagLogs.ts`, `utils/log.ts`, `utils/profilerBase.ts`)
- [ ] Telemetry (`utils/telemetry/`)
- [ ] Deep link utilities (`utils/deepLink/`)

## 17. Coordinator And Buddy

Missing:

- [ ] Coordinator mode (`coordinator/coordinatorMode.ts` — agent tool filtering and async agent allowlist)
- [ ] Buddy/companion system (`buddy/` — 6 files: CompanionSprite, companion procedural generation, personality prompts, sprites, types, notification UI)

## 18. Migrations

Missing:

- [ ] Data/config migration system (`migrations/` — 11 migration scripts):
  - Model migrations: migrateFennecToOpus, migrateLegacyOpusToCurrent, migrateOpusToOpus1m, migrateSonnet1mToSonnet45, migrateSonnet45ToSonnet46
  - Feature migrations: migrateAutoUpdatesToSettings, migrateBypassPermissionsAcceptedToSettings, migrateEnableAllProjectMcpServersToSettings, migrateReplBridgeEnabledToRemoteControlAtStartup
  - Config resets: resetAutoModeOptInForDefaultOffer, resetProToOpusDefault

## 19. Type Definitions

Missing:

- [ ] Full type system from `types/` (command.ts, hooks.ts, ids.ts, logs.ts, permissions.ts, plugin.ts, textInputTypes.ts, generated/)

## 20. Mirrored Workspace Versus Working Runtime

Working Python runtime today (21,193 lines across 51 source files, 10,480 lines across 37 test files):

- [x] `src/main.py` (1,353 lines)
- [x] `src/agent_runtime.py` (4,318 lines)
- [x] `src/agent_tools.py` (3,183 lines)
- [x] `src/agent_prompting.py` (390 lines)
- [x] `src/agent_context.py` (459 lines)
- [x] `src/agent_context_usage.py` (356 lines)
- [x] `src/agent_session.py` (718 lines)
- [x] `src/agent_slash_commands.py` (633 lines)
- [x] `src/agent_manager.py` (296 lines)
- [x] `src/agent_plugin_cache.py` (154 lines)
- [x] `src/agent_types.py` (193 lines)
- [x] `src/account_runtime.py` (470 lines)
- [x] `src/ask_user_runtime.py` (320 lines)
- [x] `src/background_runtime.py` (371 lines)
- [x] `src/config_runtime.py` (296 lines)
- [x] `src/hook_policy.py` (339 lines)
- [x] `src/mcp_runtime.py` (880 lines)
- [x] `src/openai_compat.py` (413 lines)
- [x] `src/permissions.py` (20 lines)
- [x] `src/plan_runtime.py` (396 lines)
- [x] `src/plugin_runtime.py` (654 lines)
- [x] `src/query_engine.py` (655 lines)
- [x] `src/remote_runtime.py` (571 lines)
- [x] `src/remote_trigger_runtime.py` (371 lines)
- [x] `src/search_runtime.py` (606 lines)
- [x] `src/session_store.py` (295 lines)
- [x] `src/task.py` (130 lines)
- [x] `src/task_runtime.py` (595 lines)
- [x] `src/team_runtime.py` (386 lines)
- [x] `src/tokenizer_runtime.py` (202 lines)
- [x] `src/workflow_runtime.py` (319 lines)
- [x] `src/worktree_runtime.py` (448 lines)
- [x] `src/builtin_agents.py` (426 lines)
- [x] `src/microcompact.py` (236 lines)
- [x] Plus 19 supporting modules

Mirrored / scaffold areas needing real implementation:

- [ ] `src/commands.py` — currently minimal dispatch, needs full command tree
- [ ] `src/tools.py` — reference-data based tool loading, needs real per-tool implementations
- [ ] `src/query_engine.py` — facade layer, needs full QueryEngine.ts parity
- [ ] `src/runtime.py` — routing layer, needs full runtime parity
- [ ] Remaining inventory surfaces under `src/reference_data/*`

---

## High-Priority Next Steps

### Tier 1 — Core Feature Gaps (highest user impact)
- [x] Full BashTool security parity (sed validation, path validation, sandbox, destructive command warnings, command semantics) → `src/bash_security.py`
- [x] LSP tool integration for code intelligence
- [x] Full AgentTool with built-in agent types (explore, general-purpose, verification, plan, statusline-setup, claude-code-guide) → `src/builtin_agents.py`, `src/agent_tools.py`, `src/agent_runtime.py`
- [ ] Auto-compact and context collapse from `query.ts`
- [x] Microcompact service (time-based tool-result clearing) → `src/microcompact.py`
- [x] Compact PTL retry loop and circuit-breaker tracking → `src/compact.py`
- [ ] Full compact service (sessionMemoryCompact, cached microcompact)
- [ ] Interactive REPL improvements

### Tier 2 — Important Feature Gaps
- [x] SkillTool for slash command execution → `src/agent_tools.py`, `src/agent_runtime.py`
- [ ] Full MCP service parity (auth, permissions, config, registry)
- [ ] Plugin discovery, loading, and installation
- [ ] Real remote session management (WebSocket, bridge)
- [ ] Full command tree implementation (80+ commands)
- [ ] Migration system for config/model upgrades
- [ ] Token budget calculations

### Tier 3 — Nice-to-Have Features
- [x] Local web GUI (FastAPI + vanilla JS SPA) → `src/gui/__main__.py`, `src/gui/server.py`, `src/gui/static/*`; launch with `python -m src.gui` or `claw-code-gui`
- [ ] TUI/Ink component library
- [ ] Voice mode
- [ ] VIM mode and keybinding system
- [ ] IDE integrations (JetBrains, VS Code)
- [ ] Chrome extension integration
- [ ] Buddy/companion system
- [ ] Analytics/telemetry
- [ ] Coordinator mode
- [ ] Feature flag system (Growthbook)

### Tier 4 — Platform/Enterprise Features
- [ ] Full bridge subsystem (30+ files)
- [ ] Upstream proxy
- [ ] Direct connect server
- [ ] OAuth service
- [ ] Settings sync
- [ ] Rate limiting and policy limits
- [ ] Dream/auto-consolidation service
