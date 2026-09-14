# Agent Framework Adaptation: From Claude Code to OpenDev

## Purpose

Adapt Anthropic's Claude Code agent orchestration patterns into OpenDev's Rust-based architecture, enabling background agent execution, inter-agent communication, and parallel work isolation — features that transform OpenDev from a single-agent tool into a multi-agent coding platform.

## Goal

Give users the ability to:
1. Spawn agents that run in the background while they continue working
2. Create teams of specialized agents that communicate and collaborate
3. Monitor all agents from a unified task watcher with rich progress display
4. Isolate agent work in git worktrees to prevent file conflicts

## Gap Analysis: Claude Code vs OpenDev (Before)

| Capability | Claude Code | OpenDev (Before) |
|-----------|------------|-----------------|
| Agent execution | 3 modes: sync, async (background), fork (cache-optimized) | Sync only — parent blocks until subagent completes |
| Background agents | `run_in_background: true` returns task_id immediately | Not supported |
| Mid-execution backgrounding | Ctrl+B moves running agent to background with resume | Ctrl+B signals yield, but no re-spawn in background |
| Agent communication | File-based mailbox with fd-lock, SendMessage tool | None — no lateral communication |
| Teams | TeamCreateTool, named teams, leader/member roles | None |
| Task tracking | Full lifecycle state machine with eviction, retain, notified flags | Simple `BackgroundAgentManager` with basic Running/Completed/Failed/Killed |
| Agent transcripts | Sidechain JSONL files for resume and UI viewing | Session persistence only (no per-agent transcripts) |
| Progress display | Rich ToolActivity objects, token counts, cost, recent activities | Plain string activity log |
| Ctrl+B hint | Shows "Ctrl+B to background" after 2s | No hint |
| Agent spec | permission_mode, isolation, background, mcpServers, hooks, skills | Basic: tools, model, max_steps, temperature |
| Worktree isolation | Full git worktree with symlinks, cleanup, merge-back | None |
| Tool approval for teammates | Routed to leader's UI with worker badge | Not supported |

## Why This Adaptation

OpenDev's synchronous-only subagent model creates two problems:

1. **Blocking**: When the LLM spawns an Explore agent to analyze a large codebase (30-60s), the user stares at a spinner. They can't type, ask questions, or redirect — they just wait. Claude Code solved this with background agents.

2. **No collaboration**: Complex tasks (analyze + plan + implement) require sequential handoffs. The LLM spawns Explore, waits for result, spawns Planner, waits, then codes. Claude Code's team system lets these agents run in parallel and share findings via mailbox.

## What Was Built

### 1. TaskManager (`opendev-runtime/src/task_manager/`)

**What**: A UI-agnostic task lifecycle state machine replacing the TUI-specific `BackgroundAgentManager` for new features.

**Why**: The existing `BackgroundAgentManager` lives in the TUI crate and can't be used from the REPL, web backend, or tools. TaskManager lives in `opendev-runtime` and is accessible everywhere.

**How**: `RwLock<HashMap<String, TaskInfo>>` with atomic state transitions (Pending → Running → Completed/Failed/Killed). Key features learned from Claude Code:
- **Idempotent transitions**: `kill_task()` on an already-killed task is a no-op (prevents double-kill bugs)
- **Atomic notified flag**: `mark_notified()` returns true only on first call (prevents duplicate completion notifications, matching Claude Code's `updateTaskState` pattern)
- **Eviction with grace period**: Terminal tasks keep `evict_after_ms = now + 5_000` (5s, matching Claude Code's `PANEL_GRACE_MS`) so the TUI shows them briefly before cleanup
- **Retain blocks eviction**: When the TUI detail view is open, `retain=true` prevents the task from disappearing mid-viewing

**Types**: `TaskState`, `TaskInfo` (30 fields including `recent_activities: Vec<ToolActivity>`, `pending_messages: Vec<PendingMessage>`, `notified`, `evict_after_ms`, `retain`), `TaskManagerEvent`, `ToolActivity`, `PendingMessage`

**Tests**: 30 unit tests covering lifecycle, idempotency, concurrency, eviction, and event emission.

---

### 2. Sidechain Transcripts (`opendev-history/src/sidechain/`)

**What**: Append-only JSONL writer/reader for agent conversation persistence.

**Why**: When an agent is backgrounded (Ctrl+B) or crashes, its message history needs to be saved for resume. Claude Code stores transcripts in `~/.claude/subagents/{agentId}.jsonl` and loads them for resume via `resumeAgentBackground()`.

**How**:
- `SidechainWriter`: Opens file in append mode, serializes `TranscriptEntry` as one JSON line per write, flushes immediately. Fire-and-forget — write failures are logged but don't stop the agent.
- `SidechainReader`: Reads JSONL line-by-line, skips malformed lines (handles partial writes from crashes). `into_messages()` reconstructs LLM-compatible message arrays with filters:
  - Removes whitespace-only assistant messages
  - Removes orphaned tool calls (tool_use without matching tool_result)
  - Skips system prompt, token usage, and state change entries

**Storage**: `~/.opendev/sessions/{session_id}/agents/{agent_id}.jsonl`

**Entry types**: `SystemPrompt`, `AssistantMsg`, `ToolResult`, `Tokens`, `StateChange`

**Tests**: 9 tests covering write/read, tail, resume cycle, corruption recovery, orphaned tool call filtering.

---

### 3. Background Agent Execution (`run_in_background`)

**What**: A `run_in_background: true` parameter on `spawn_subagent` that returns a task_id immediately and runs the agent in a detached `tokio::spawn`.

**Why**: This is the #1 gap. Claude Code's async agent mode lets the parent continue working while background agents research, build, or test. Without this, every subagent blocks the entire conversation.

**How** (end-to-end flow):

```
LLM calls spawn_subagent(agent_type="Explore", task="...", run_in_background=true)
    │
    ├─ SpawnSubagentTool::execute() checks run_in_background
    ├─ Creates InterruptToken for the background task
    ├─ Sends SubagentEvent::BackgroundSpawned to TUI
    ├─ Spawns tokio::spawn with BackgroundProgressCallback
    ├─ Returns immediately: "Background agent started. task_id: abc123"
    │
    │  (background task runs independently)
    ├─ BackgroundProgressCallback emits BackgroundProgress + BackgroundActivity events
    ├─ TUI task watcher shows live progress
    │
    │  (background task completes)
    ├─ Sends SubagentEvent::BackgroundCompleted
    ├─ TUI handler pushes to pending_queue
    ├─ When parent is idle: drain_next_pending() injects via \x00__BG_RESULT__ sentinel
    └─ Parent agent processes result in next turn
```

**Key adaptation from Claude Code**:
- Claude Code has `registerAgentForeground()` + promise race for auto-backgrounding. We use `tokio::spawn` + `SubagentEvent` channel.
- Claude Code prevents background-in-background via `isInProcessTeammate()` check. We use `ctx.values["is_background_agent"]` flag.
- Claude Code checks `spec.background` for auto-background agents. We check `SubAgentSpec.background` field.
- The existing `pending_queue` + `\x00__BG_RESULT__` sentinel mechanism (already in the codebase) was reused for result injection — no new TUI handlers needed.

**Skip eager display**: When `run_in_background=true`, `handle_tool_started()` skips creating a `SubagentDisplayState` in the conversation spinner. Background agents go directly to the task watcher.

---

### 4. Enhanced SubAgentSpec

**What**: Four new fields on the agent specification struct, all with `#[serde(default)]` for backward compatibility.

**Why**: Claude Code agent definitions support permission_mode, isolation, mcpServers, hooks, skills, background, omitClaudeMd. OpenDev's spec was limited to tools/model/temperature.

**Fields added**:
- `permission_mode: AgentPermissionMode` (Inherit/Autonomous/Manual) — controls tool approval behavior
- `isolation: IsolationMode` (None/Worktree) — enables git worktree isolation
- `background: bool` — auto-spawn as background agent
- `omit_instructions: bool` — skip project instruction files (CLAUDE.md) from system prompt

**Backward compatible**: Existing `.opendev/agents/*.md` custom agent definitions parse unchanged because all new fields default to their zero values.

---

### 5. Ctrl+B Background Hint

**What**: A dim italic "Ctrl+B to background" hint that appears inline next to the subagent spinner after 2 seconds of foreground execution.

**Why**: Claude Code shows a `BackgroundHint` component after `PROGRESS_THRESHOLD_MS = 2000` to nudge users. Without the hint, users don't know they can background a slow agent.

**How**:
- `SubagentDisplayState.foreground_start`: Set to `Instant::now()` when subagent starts
- `tick.rs`: Every 60ms tick, checks if `foreground_start.elapsed() > 2s` and sets `background_hint_shown = true`
- `spinner.rs`: When rendering a `spawn_subagent` tool line, appends `"  Ctrl+B to background"` span if hint flag is set
- Spinner animation continues alongside hint (`shouldContinueAnimation: true` equivalent)
- Hint auto-dismisses when subagent finishes or is backgrounded

---

### 6. Mailbox System (`opendev-runtime/src/mailbox/`)

**What**: File-based inbox per agent with exclusive file locking for concurrent-safe message passing.

**Why**: Claude Code uses `~/.claude/teams/{team}/inbox/{agent}.json` with `proper-lockfile` for inter-agent messaging. Teams need a communication channel that works across async contexts.

**How**:
- `Mailbox::send()`: Acquires fd-lock on `.lock` file, reads inbox JSON array, appends message, writes back, releases lock
- `Mailbox::receive()`: Same lock protocol, filters unread, marks as read atomically
- `Mailbox::peek()`: Read without marking (for polling)
- `Mailbox::poll()`: Async wait with 500ms sleep interval and timeout
- **Corruption recovery**: If JSON parse fails, renames to `.corrupt.{timestamp}`, creates fresh empty array (matches Claude Code's graceful degradation)
- **Message cap**: Trims oldest read messages when inbox exceeds 1000 entries

**Message types**: `Text`, `ShutdownRequest`, `ShutdownResponse`, `Idle`

**Tests**: 11 tests covering send/receive, concurrent writes (5 threads), corruption recovery, poll timeout.

---

### 7. TeamManager (`opendev-runtime/src/team_manager/`)

**What**: Creates named teams with a leader and member agents, persisted to disk.

**Why**: Claude Code's `TeamCreateTool` creates teams with `leadAgentId`, members, and a file-based mailbox directory. Teams enable multi-agent collaboration patterns.

**How**:
- `create_team()`: Creates `~/.opendev/teams/{name}/team.json` + `inboxes/` directory
- `add_member()`: Registers member with name, agent_type, task_id, status
- `update_member_status()`: Tracks Idle/Busy/Waiting/Done/Failed
- `delete_team()`: Removes all team files
- `cleanup_orphans()`: Scans for corrupt team configs on startup

**Tests**: 8 tests covering create, add member, delete, status update, disk persistence.

---

### 8. Team Tools

**What**: Three new LLM-callable tools for team management.

#### `create_team`
- Parameters: `team_name`, `members: [{name, agent_type, task}]`
- Creates team via TeamManager, registers members
- Emits `SubagentEvent::TeamCreated` for TUI notification

#### `send_message`
- Parameters: `to` (member name or `"*"` for broadcast), `message`, optional `team_name`
- Writes to recipient's `Mailbox::send()`
- Validates recipient exists in team
- Emits `SubagentEvent::TeamMessageSent` for TUI toast

#### `delete_team`
- Parameters: `team_name`
- Sends `ShutdownRequest` messages to all members via mailbox
- Deletes team files via TeamManager
- Emits `SubagentEvent::TeamDeleted`

---

### 9. Mailbox Polling in React Loop

**What**: Team member agents drain their mailbox before each react loop execution.

**Why**: Claude Code's in-process teammates poll their mailbox every 500ms via `waitForNextPromptOrShutdown()`. Messages need to reach the agent's LLM context.

**How**:
- `RunnerContext` gains optional `mailbox: Option<&Mailbox>` field
- `StandardReactRunner::run()`: Before calling `ReactLoop::run()`, drains mailbox and injects messages as user-role entries
- `SimpleReactRunner::run()`: Same pattern
- `inject_mailbox_messages()`: Shared helper that converts `MailboxMessage` → JSON user message
  - `Text` → `"[Message from teammate '{name}']: {content}"`
  - `ShutdownRequest` → `"[TEAM SHUTDOWN REQUEST]: {content}\nWrap up and call task_complete."`

---

### 10. Task Watcher Enhancements

**What**: Detail view, enhanced footer, and new keybindings.

**Why**: Claude Code's `BackgroundTasksDialog` has task pills, detail views, restart, and sorting. OpenDev's task watcher had basic grid cells with limited information.

**Changes**:

| Key | Action | Why |
|-----|--------|-----|
| Enter | Expand focused cell to full-size detail view | View full activity log, scrollable |
| Esc | Close detail view first, then close watcher | Layered dismiss (matches Claude Code's modal pattern) |
| r | Restart failed/killed task by re-queuing its query | Recovery without manual re-typing |
| t | Toggle sort order (time vs status) | Group running tasks first |

**Enhanced footer**: `"Working... · 45s · 12 tools · 3.2k tok · $0.023"` instead of just `"Working... · 45s · 12 tools"`

---

### 11. Team TUI Wiring

**What**: Full event pipeline from backend team events to TUI display.

**Flow**:
```
CreateTeamTool::execute()
    → SubagentEvent::TeamCreated
    → tui_runner bridge → AppEvent::TeamCreated
    → event_dispatch → handle_team_created()
    → Toast: "Team 'analysis' created with 2 members"
    → Status bar: "Team:2/3 busy"
```

**Toast patterns**:
- Team created: Info, 3s
- Agent message: Info, 2s (suppressed when task watcher is open)
- Team deleted: Info, 3s

**Status bar**: `"Team:busy/total"` pill in cyan bold, shown after background task count.

---

### 12. WorktreeManager (`opendev-runtime/src/worktree/`)

**What**: Creates and manages git worktrees for agent isolation.

**Why**: When multiple agents edit files in parallel, they conflict. Claude Code uses `git worktree add` with symlinks for efficiency. Agents with `isolation: worktree` get their own branch and working directory.

**How**:
- `create()`: `git worktree add -b opendev/agent-{short_id} {path}` from HEAD
- `has_changes()`: `git status --porcelain` in worktree
- `cleanup()`: If no changes, `git worktree remove --force` + `git branch -D`. If changes exist, preserves worktree for manual review.
- `list()`: Enumerates existing worktrees in base directory

**Tests**: 5 tests with real git repo fixtures (tempdir).

---

### 13. `resume_with_messages()`

**What**: Runtime method that continues an agent from existing message history without injecting a new user message.

**Why**: Needed for team member resume from sidechain transcript when a completed agent receives a new `SendMessage`. Claude Code uses `resumeAgentBackground()` with transcript reconstruction.

**How**: Prepends system prompt if missing, creates fresh ToolContext, runs ReactLoop with no cost tracking, no approval gates, no compaction (lightweight background execution).

---

### 14. LLM Prompt Templates

**What**: Updated `main-subagent-guide.md` and `main-available-tools.md` with background agent guidance.

**Why**: The LLM needs to know WHEN and HOW to use `run_in_background`. Claude Code teaches this via system prompt sections. Without guidance, the LLM won't discover or use the feature correctly.

**Added**:
- "Background Agents" section: when to use, how it works, example
- Available tools: `run_in_background=true` mention in subagent description

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        opendev-cli                           │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  TuiRunner   │  │ AgentRuntime │  │  WebExecutor      │  │
│  │  (bridge)    │  │ (query loop) │  │  (WebSocket)      │  │
│  └──────┬───────┘  └──────┬───────┘  └───────┬───────────┘  │
│         │                 │                   │              │
│         │   SubagentEvent channel             │              │
│         ├─────────────────┤───────────────────┤              │
│         │                 │                   │              │
│  ┌──────▼───────┐  ┌──────▼───────┐  ┌───────▼───────────┐  │
│  │   AppEvent    │  │ SpawnSubagent│  │  BackgroundProgress│  │
│  │   dispatch    │  │ Tool         │  │  Callback          │  │
│  └──────┬───────┘  │ (run_in_bg)  │  └───────────────────┘  │
│         │          └──────────────┘                          │
└─────────┼───────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────┐
│                        opendev-tui                           │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ TaskWatcher  │  │ StatusBar    │  │  Toast system      │  │
│  │ (detail,     │  │ (team pill)  │  │  (team/bg toasts)  │  │
│  │  footer,     │  └──────────────┘  └───────────────────┘  │
│  │  Enter/r/t)  │                                           │
│  └─────────────┘  ┌──────────────┐  ┌───────────────────┐  │
│                   │ Ctrl+B hint  │  │  handle_team.rs    │  │
│                   │ (spinner.rs) │  │  (create/msg/del)  │  │
│                   └──────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────┐
│                      opendev-agents                          │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ SubAgentSpec │  │ RunnerContext│  │  inject_mailbox_   │  │
│  │ (+4 fields)  │  │ (+mailbox)   │  │  messages()        │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────┐
│                      opendev-runtime                         │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ TaskManager  │  │   Mailbox    │  │  TeamManager       │  │
│  │ (lifecycle)  │  │ (fd-lock IPC)│  │  (team config)     │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│  ┌─────────────┐                                            │
│  │ Worktree    │                                            │
│  │ Manager     │                                            │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────┐
│                      opendev-history                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ SidechainWriter / SidechainReader (JSONL transcripts)│   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Files Changed

### New files (19)
```
crates/opendev-runtime/src/task_manager/mod.rs          (375 lines)
crates/opendev-runtime/src/task_manager/types.rs        (155 lines)
crates/opendev-runtime/src/task_manager/tests.rs        (453 lines)
crates/opendev-runtime/src/mailbox/mod.rs               (200 lines)
crates/opendev-runtime/src/mailbox/tests.rs             (180 lines)
crates/opendev-runtime/src/team_manager/mod.rs          (215 lines)
crates/opendev-runtime/src/team_manager/tests.rs        (130 lines)
crates/opendev-runtime/src/worktree/mod.rs              (185 lines)
crates/opendev-runtime/src/worktree/tests.rs            (115 lines)
crates/opendev-history/src/sidechain/mod.rs             (20 lines)
crates/opendev-history/src/sidechain/types.rs           (55 lines)
crates/opendev-history/src/sidechain/writer.rs          (105 lines)
crates/opendev-history/src/sidechain/reader.rs          (150 lines)
crates/opendev-history/src/sidechain/tests.rs           (195 lines)
crates/opendev-tools-impl/src/agents/team_tools.rs      (350 lines)
crates/opendev-tui/src/app/handle_team.rs               (53 lines)
docs/agent-framework-refactoring.md                     (2529 lines, design doc)
docs/agent-framework-adaptation.md                      (this file)
```

### Modified files (16)
```
crates/opendev-runtime/src/lib.rs                       (+modules, +re-exports, +now_ms)
crates/opendev-runtime/Cargo.toml                       (+fd-lock, +uuid dev-dep)
crates/opendev-history/src/lib.rs                       (+sidechain module)
crates/opendev-agents/src/subagents/spec/types.rs       (+4 fields, +2 enums)
crates/opendev-agents/src/subagents/spec/builder.rs     (+4 builder methods)
crates/opendev-agents/src/subagents/spec/mod.rs         (+re-exports)
crates/opendev-agents/src/subagents/mod.rs              (+re-exports)
crates/opendev-agents/src/subagents/runner/mod.rs       (+mailbox field, +inject helper)
crates/opendev-agents/src/subagents/runner/standard.rs  (+mailbox drain)
crates/opendev-agents/src/subagents/runner/simple.rs    (+mailbox drain)
crates/opendev-agents/src/subagents/manager/spawn.rs    (+mailbox: None)
crates/opendev-tools-impl/src/agents/events.rs          (+7 SubagentEvent variants, +BackgroundProgressCallback)
crates/opendev-tools-impl/src/agents/spawn.rs           (+run_in_background, +spawn_background)
crates/opendev-tools-impl/src/agents/mod.rs             (+team_tools module)
crates/opendev-tui/src/event/mod.rs                     (+3 team AppEvent variants)
crates/opendev-tui/src/event/recorder.rs                (+team event serialization)
crates/opendev-tui/src/app/mod.rs                       (+handle_team module)
crates/opendev-tui/src/app/state.rs                     (+task_watcher_detail, +sort)
crates/opendev-tui/src/app/event_dispatch.rs            (+team event routing)
crates/opendev-tui/src/app/key_handler.rs               (+Enter/r/t keys, +restart, +layered Esc)
crates/opendev-tui/src/app/handle_tools.rs              (+skip eager display for bg agents)
crates/opendev-tui/src/app/tick.rs                      (+Ctrl+B hint timing)
crates/opendev-tui/src/app/render.rs                    (+detail_idx pass-through)
crates/opendev-tui/src/widgets/background_tasks.rs      (+detail view, +enhanced footer)
crates/opendev-tui/src/widgets/status_bar.rs            (+team_status pill)
crates/opendev-tui/src/widgets/nested_tool/state.rs     (+hint fields, +cost)
crates/opendev-tui/src/widgets/conversation/spinner.rs  (+Ctrl+B hint rendering)
crates/opendev-cli/src/tui_runner/mod.rs                (+background + team event bridge)
crates/opendev-cli/src/web_executor.rs                  (+background + team WebSocket events)
crates/opendev-cli/src/runtime/query.rs                 (+resume_with_messages)
crates/opendev-agents/templates/system/main/main-subagent-guide.md    (+Background Agents section)
crates/opendev-agents/templates/system/main/main-available-tools.md   (+run_in_background mention)
```

## Test Coverage

| Module | Tests | Key coverage |
|--------|-------|-------------|
| TaskManager | 30 | Lifecycle, idempotency, concurrency (10 threads), eviction, events |
| Sidechain | 9 | Write/read, tail, resume cycle, corruption, orphaned tool calls |
| Mailbox | 11 | Send/receive, concurrent writes (5 threads), corruption, poll |
| TeamManager | 8 | Create, add member, delete, status, persistence |
| WorktreeManager | 5 | Create, cleanup, has_changes, list (real git repos) |
| **Total** | **72** | All new code, 0 failures across full workspace |

## Key Design Decisions

### 1. Reuse existing event pipeline instead of new channels
The existing `SubagentEvent → AppEvent` bridge in `tui_runner` was extended with new variants rather than creating separate team/background channels. This keeps one unified event flow.

### 2. Keep BackgroundAgentManager alongside TaskManager
Rather than a risky refactor of all TUI code to use TaskManager directly, the existing `BackgroundAgentManager` continues handling Ctrl+B tasks while `run_in_background` tasks flow through the same event pipeline. Both produce the same `AppEvent` types.

### 3. Mailbox polling at runner level, not react loop
Messages are drained once before each react loop execution, not during each iteration. This is simpler and sufficient — team members are typically short-lived agents. Real-time mid-iteration polling would require deeper react loop changes.

### 4. `now_ms()` as crate-level utility
Multiple modules needed epoch milliseconds. Rather than duplicating the function, it's exported from `opendev_runtime::now_ms()`.

### 5. Fire-and-forget for non-critical writes
Sidechain writes, mailbox sends, and team config updates follow Claude Code's pattern: log on failure but never block the agent. The agent's primary task always takes priority over bookkeeping.
