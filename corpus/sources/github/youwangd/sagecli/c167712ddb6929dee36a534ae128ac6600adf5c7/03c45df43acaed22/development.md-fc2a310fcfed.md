# sage Development Guide

## Architecture

```
sage (CLI)
  │
  ├── sage init          → creates ~/.sage/ with tools/, runtimes/, runner.sh
  ├── sage create <name> → creates agent dir with inbox/, workspace/, runtime.json
  ├── sage start <name>  → launches runner.sh in tmux pane
  ├── sage send/call     → writes JSON to agent's inbox/, returns task ID
  │
  └── runner.sh (per agent, runs in tmux)
        ├── polls inbox/ every 300ms
        ├── sources runtimes/<runtime>.sh
        ├── calls runtime_inject() for each message
        └── writes task status + results to results/
```

### File Layout

```
~/.sage/
├── agents/
│   ├── .cli/                  # pseudo-agent for sage call replies
│   │   └── replies/
│   └── <agent>/
│       ├── inbox/             # incoming messages (JSON files)
│       ├── replies/           # sync call responses
│       ├── results/           # task tracking
│       │   ├── <task-id>.status.json   # {status, queued_at, started_at, finished_at}
│       │   └── <task-id>.result.json   # {status, agent, output}
│       ├── workspace/         # agent's working directory
│       ├── state/             # persistent agent state
│       ├── runtime.json       # {runtime, model, parent, workdir, acp_agent, created}
│       ├── instructions.md    # auto-generated prompt for CLI runtimes
│       ├── steer.md           # steering context (injected into prompts)
│       ├── handler.sh         # bash runtime only
│       └── .pid               # runner process ID
├── runtimes/
│   ├── bash.sh
│   ├── cline.sh
│   ├── claude-code.sh
│   └── acp.sh                 # Universal ACP bridge (cline, claude-code, goose, kiro, gemini...)
├── tools/
│   ├── common.sh              # send_msg, call_agent, reply, broadcast
│   └── llm.sh                 # raw LLM API helper (120s timeout)
├── tasks/                     # Task templates (review, test, spec, implement, refactor, document, debug)
│   ├── review.md
│   ├── test.md
│   ├── spec.md
│   ├── implement.md
│   ├── refactor.md
│   ├── document.md
│   └── debug.md
├── plans/                     # Saved execution plans (JSON)
├── logs/
│   └── <agent>.log
└── runner.sh                  # agent process loop
```

## Task Lifecycle

Every message creates a trackable task. Status transitions are mechanical (written by runner code, not LLM behavior).

```
sage send worker "your task description" → task ID returned immediately
sage send worker @prompt.md              → reads message from file
                                         │
                                    ┌─────▼─────┐
                                    │  queued    │  status.json created by send_msg
                                    └─────┬─────┘
                                          │  runner picks up from inbox
                                    ┌─────▼─────┐
                                    │  running   │  runner updates status.json
                                    └─────┬─────┘
                                          │  runtime_inject() completes
                                    ┌─────▼─────┐
                                    │  done │    │  runner updates status + runtime writes result
                                    │  failed   │  if runtime_inject() returns nonzero
                                    └────────────┘
```

Track with: `sage tasks [name]` · `sage result <task-id>` · `sage peek <name>`

## Live Streaming

CLI runtimes stream events to the tmux pane in real-time. The pattern:

1. CLI outputs structured JSON events (one per line)
2. A `while read` loop in the runtime parses each event
3. Meaningful events (tool calls, text, completion) are printed to stdout (the tmux pane)
4. Text is also appended to `.live_output` for `sage peek`'s Live output section

### Claude Code events (`--output-format stream-json --verbose`)
- `system` — init (model, tools, session_id)
- `assistant` — text content + tool_use blocks
- `tool_result` — tool execution results
- `result` — final summary text + cost + duration

### Cline events (`--json`)
- `task_started` — task begins
- `say:api_req_started` — API call in progress
- `say:reasoning` — thinking/reasoning text
- `say:text` — response text
- `say:tool` — tool execution
- `say:completion_result` — task complete

### Why not just pipe stdout?

`claude -p` in print mode buffers ALL output until completion, regardless of TTY. Even with `tee`, `script(1)`, or process substitution — nothing appears during execution. The `--output-format stream-json` flag is the only way to get real-time events. Similarly, `cline --json` streams while plain `cline --act` may buffer.

## Parent-Child Tracking

When an agent creates a sub-agent, the parent is automatically recorded:

```bash
# Inside orch (SAGE_AGENT_NAME=orch):
sage create sub1 --runtime claude-code
# → sub1/runtime.json gets {"parent":"orch", ...}
```

`sage status` shows the tree:
```
  orch           claude-code  running
    └─ sub1      claude-code  running
    └─ sub2      claude-code  running
```

`sage steer orch "..." --restart` cascades: stops all children recursively, then restarts orch.

## Steering

Agents can be course-corrected mid-flight via `steer.md`:

**Soft steer** — writes `steer.md` + queues a message:
```bash
sage steer orch "Use PostgreSQL instead of SQLite"
# steer.md is injected into prompt BEFORE instructions on every runtime_inject()
# Message queued — processed after current task finishes
```

**Hard steer** (`--restart`) — cascades stop + re-queues:
```bash
sage steer orch "Wrong approach" --restart
# 1. Stops all children (recursive)
# 2. Stops orch
# 3. Writes steer.md
# 4. Re-queues the in-flight task
# 5. Restarts orch → picks up task with steering context
# Children were stopped — orch re-creates them as needed
```

Runtime prompt construction:
```
[instructions.md]
[steer.md — if exists]
---
## Current Task (from: ...)
<task>
---
<completion instruction>
```

## ACP Runtime (Agent Client Protocol)

The `acp` runtime speaks JSON-RPC 2.0 over stdio to any ACP-compatible agent. Unlike the `cline` and `claude-code` runtimes (which are one-shot per task), ACP maintains a **persistent session** — follow-up messages go into the same conversation, enabling true live steering.

### How It Works

```
sage create worker --runtime acp --agent cline
sage start worker
  → runner spawns cline --acp as subprocess
  → initialize (capability negotiation)
  → session/new (create workspace session)

sage send worker "Build a Flask app"
  → session/prompt #1 → cline works → end_turn

sage send worker "Add a /health endpoint"
  → session/prompt #2 into SAME session → cline has full context → modifies app
```

### ACP vs One-Shot Runtimes

| Feature | cline/claude-code runtime | acp runtime |
|---|---|---|
| Process lifecycle | Spawn per task, exits after | Persistent across tasks |
| Follow-up context | None (fresh process each time) | Full conversation history |
| Live steering | steer.md on next task only | Follow-up prompt in same session |
| Output | Custom JSON parser per agent | Universal ACP event stream |
| Agent support | 1 runtime per agent | Any ACP agent with one runtime |

### Supported Agents

Any agent with ACP support works. Tested:

| Agent | ACP command | Status |
|---|---|---|
| Cline | `cline --acp` | ✅ Verified |
| Claude Code | `claude-agent-acp` (via Zed adapter) | ✅ Verified |
| Goose | `goose --acp` | Should work |
| Kiro | `kiro --acp` | Should work |
| Gemini CLI | `gemini --experimental-acp` | Should work |

### ACP Event Types

The runtime parses these `session/update` notifications:

- `agent_message_chunk` — text from the agent (accumulated, displayed)
- `tool_call` — agent started using a tool (title displayed)
- `tool_call_update` — tool status change (completed/failed)
- `plan` — agent's execution plan
- `agent_thought_chunk` — thinking (silently consumed)

### Permission Handling

When an agent requests permission (e.g., to write a file):
- **Cline**: handles tools internally, rarely asks
- **Claude Code adapter**: sends `session/request_permission` — runtime auto-approves with `outcome.selected + optionId`

### Agent-Specific Quirks

Both Cline and Claude Code's adapter require `cwd` and `mcpServers` in `session/new` params (not in base ACP spec). The runtime includes these automatically.

### Creating ACP Agents

```bash
# Explicit
sage create worker --runtime acp --agent cline

# --agent implies --runtime acp
sage create worker --agent goose

# Runtime config
cat ~/.sage/agents/worker/runtime.json
# {"runtime":"acp","acp_agent":"cline",...}
```

## Message Flow

### Fire & Forget (sage send)
```
sage send worker "do X"                  # inline
sage send worker @task.md                # from file
  → auto-starts agent if not running
  → returns task ID immediately (non-blocking)
  → writes JSON to ~/.sage/agents/worker/inbox/<task-id>.json
  → creates results/<task-id>.status.json (queued)
  → runner picks it up, updates status → running
  → calls runtime_inject()
  → runtime writes results/<task-id>.result.json
  → runner updates status → done
```

### Sync Call (sage call)
```
sage call worker "do X" 60               # inline, 60s timeout
sage call worker @task.md 120            # from file, 120s timeout
  → auto-starts agent if not running
  → writes JSON with reply_dir to worker's inbox
  → polls reply_dir for response (up to 60s)
  → runner picks up message, calls runtime_inject()
  → runtime does work, captures output
  → runtime writes reply to reply_dir/<task-id>.json
  → sage call reads reply, prints to stdout
```

### Key Design: Sync vs Async Prompt

When `reply_dir` is present (sync call via `sage call`):
- Prompt says: "Your output will be automatically returned. Do NOT run sage send."
- Result flows through reply_dir mechanism only

When `reply_dir` is absent (async via `sage send`):
- Prompt says: "Report result via sage send <from> ..."
- Agent may send results back (but results/ is the reliable source)

### Caller Identity

`sage call` uses `$SAGE_AGENT_NAME` if set (inside an agent), falls back to `.cli` from terminal.
This ensures sub-agents see `from=orch` (not `from=.cli`) when the orchestrator delegates.

## Runtime Interface

Every runtime implements exactly **two functions**:

```bash
runtime_start() {
  local agent_dir="$1" name="$2"
  # One-time setup when agent starts
}

runtime_inject() {
  local name="$1" msg="$2"
  # Called for each incoming message
  # Parse msg, build prompt, invoke CLI, write reply + result
}
```

## Adding a New Runtime

### Step 1: Create the bridge file

Create `runtimes/<name>.sh`:

```bash
#!/bin/bash
# Runtime: <name> bridge

runtime_start() {
  local agent_dir="$1" name="$2"
  mkdir -p "$agent_dir/workspace"
}

runtime_inject() {
  local name="$1" msg="$2"
  local agent_dir="$AGENTS_DIR/$name"

  # ── Parse message (copy this block as-is) ──
  local task=$(echo "$msg" | jq -r '.payload.task // .payload.text // (.payload | tostring)')
  local from=$(echo "$msg" | jq -r '.from')
  local msg_id=$(echo "$msg" | jq -r '.id')
  local reply_dir=$(echo "$msg" | jq -r '.reply_dir // empty')
  local workdir=$(jq -r '.workdir // "."' "$agent_dir/runtime.json")
  local model=$(jq -r '.model // empty' "$agent_dir/runtime.json")
  local instructions="$agent_dir/instructions.md"
  local steer_file="$agent_dir/steer.md"

  # ── Build prompt ──
  local completion_instruction
  if [[ -n "$reply_dir" ]]; then
    completion_instruction="Your output will be automatically returned. Do NOT run sage send."
  else
    completion_instruction="When done: sage send $from \"Done: <brief summary>\""
  fi

  local prompt_file=$(mktemp /tmp/sage-XXXXX.txt)
  cat > "$prompt_file" << PROMPT
$(cat "$instructions" 2>/dev/null)
$(if [[ -f "$steer_file" ]]; then echo ""; cat "$steer_file"; fi)

---
## Current Task (from: $from)
$task
---
$completion_instruction
PROMPT

  # Remove steer file after reading (prevents leaking into subsequent tasks)
  [[ -f "$steer_file" ]] && rm -f "$steer_file"

  # ── Invoke the CLI (THIS IS THE ONLY PART YOU CUSTOMIZE) ──
  log "invoking <name>..."
  cd "$workdir"
  local live_output="$agent_dir/.live_output"
  > "$live_output"

  # Option A: Streaming (preferred — live output in tmux pane)
  <YOUR_CLI> --json "$(cat "$prompt_file")" 2>&1 | while IFS= read -r line; do
    # Parse events and echo to terminal + live_output
    echo "$line"  # customize parsing per CLI
  done
  local output=$(cat "$live_output")

  # Option B: Simple capture (no live output, result only after completion)
  # local output=$(<YOUR_CLI_COMMAND> "$(cat "$prompt_file")" 2>&1) || true

  rm -f "$prompt_file"

  log "<name> finished: $(echo "$output" | tail -1 | head -c 120)"

  # ── Write result for task tracking (copy as-is — atomic write) ──
  local results_dir="$AGENTS_DIR/$name/results"
  if [[ -d "$results_dir" && -n "$msg_id" ]]; then
    local json_out
    json_out=$(echo "$output" | jq -Rs .) || json_out="\"encoding failed\""
    local _rtmp=$(mktemp "$results_dir/.tmp.XXXXXX")
    echo "{\"status\":\"done\",\"agent\":\"$name\",\"output\":$json_out}" > "$_rtmp" && mv "$_rtmp" "$results_dir/${msg_id}.result.json" || rm -f "$_rtmp"
  fi

  # ── Write reply for sync calls (copy as-is — atomic write) ──
  if [[ -n "$reply_dir" ]]; then
    mkdir -p "$reply_dir"
    local _rptmp=$(mktemp "$reply_dir/.tmp.XXXXXX")
    echo "{\"status\":\"done\",\"agent\":\"$name\",\"output\":$(echo "$output" | jq -Rs .)}" > "$_rptmp" && mv "$_rptmp" "$reply_dir/${msg_id}.json" || rm -f "$_rptmp"
  fi
}
```

### Step 2: The CLI invocation patterns

**Streaming (preferred) — output appears live in tmux pane:**

```bash
# Claude Code (stream-json — events parsed live)
cd "$workdir"
cat "$prompt_file" | claude -p --output-format stream-json --verbose \
  --allowedTools "Bash(*)" "Write(*)" "Read(*)" "Edit(*)" \
  ${model:+--model "$model"} 2>&1 | while IFS= read -r line; do
  local evt=$(echo "$line" | jq -r '.type // empty' 2>/dev/null)
  case "$evt" in
    assistant)
      local tools text
      tools=$(echo "$line" | jq -r '[.message.content[]? | select(.type == "tool_use") | .name] | join(", ")' 2>/dev/null)
      text=$(echo "$line" | jq -r '[.message.content[]? | select(.type == "text") | .text] | join("")' 2>/dev/null)
      [[ -n "$tools" ]] && printf "\033[36m  → %s\033[0m\n" "$tools"
      [[ -n "$text" ]] && { echo "$text"; echo "$text" >> "$live_output"; }
      ;;
    result)
      local result_text
      result_text=$(echo "$line" | jq -r '.result // empty' 2>/dev/null)
      [[ -n "$result_text" ]] && { echo "$result_text"; echo "$result_text" >> "$live_output"; }
      ;;
  esac
done

# Cline (--json — events parsed live)
cd "$workdir"
cline --act -c "$workdir" --json ${model:+-m "$model"} "$(cat "$prompt_file")" 2>&1 | while IFS= read -r line; do
  local say_type
  say_type=$(echo "$line" | jq -r '.say // .type // empty' 2>/dev/null)
  case "$say_type" in
    text|completion_result)
      local text=$(echo "$line" | jq -r '.text // empty' 2>/dev/null)
      [[ -n "$text" ]] && { echo "$text"; echo "$text" >> "$live_output"; }
      ;;
    tool)
      local tool_name=$(echo "$line" | jq -r '.text // empty' | jq -r '.tool // empty' 2>/dev/null)
      [[ -n "$tool_name" ]] && printf "\033[36m  → %s\033[0m\n" "$tool_name"
      ;;
  esac
done
```

**Simple (for CLIs without streaming JSON):**

```bash
# Aider
output=$(aider --yes --message "$(cat "$prompt_file")" 2>&1) || true

# Gemini CLI
output=$(gemini -p "$(cat "$prompt_file")" 2>&1) || true

# Codex CLI
output=$(codex -q "$(cat "$prompt_file")" 2>&1) || true

# Ollama (local)
output=$(ollama run llama3 "$(cat "$prompt_file")" 2>&1) || true
```

### Step 3: Embed in sage init

Add the runtime to the `cmd_init()` function in `sage`:

```bash
  cat > "$RUNTIMES_DIR/<name>.sh" << 'RTEOF'
  <paste your runtime here>
  RTEOF
```

### Step 4: Test

```bash
sage init --force
sage create test-agent --runtime <name>
sage start test-agent

# Quick test
sage call test-agent "Create hello.py that prints hello" 60
cat ~/.sage/agents/test-agent/workspace/hello.py

# Task tracking test
sage send test-agent "Create world.py that prints world"
sage tasks test-agent        # should show running → done
sage result <task-id>        # should show output

# Orchestrator test
sage create orch --runtime <name>
sage start orch
sage call orch "Create a sub-agent, delegate, collect result" 120

# Clean up
sage stop --all; sage rm test-agent; sage rm orch
```

### Checklist

- [ ] `runtimes/<name>.sh` with `runtime_start` + `runtime_inject`
- [ ] steer.md read, injected into prompt, and **deleted after reading**
- [ ] Result written atomically to `results/<task-id>.result.json` (mktemp + mv)
- [ ] Reply written atomically for sync calls (reply_dir check, mktemp + mv)
- [ ] Embedded in `sage init`
- [ ] Help text updated
- [ ] E2E: `sage call` returns result
- [ ] E2E: `sage send` → `sage tasks` shows done → `sage result` works
- [ ] E2E: failed runtime returns nonzero → task status shows "failed"
- [ ] Orchestrator test: orch creates sub-agents with this runtime

## Known Patterns

### Multi-Orchestrator (Parallel)
Multiple independent orchestrators running simultaneously:
```bash
sage create orch-frontend --runtime claude-code
sage create orch-backend --runtime claude-code
sage start --all
sage send orch-frontend "Build React UI"
sage send orch-backend "Build REST API"
sage tasks    # track all tasks across all agents
```

### Persistent Agent
Agents stay alive between messages. The runner loops forever, processing each inbox message. Useful for multi-turn conversations.

### Mixed Runtimes
```bash
sage create orch --runtime claude-code
sage create fast-worker --runtime cline
sage create smart-worker --runtime claude-code
```

### Long-Running Supervisor Pattern
```bash
sage send orch "Build entire app"    # submit
sage tasks orch                                  # monitor
sage peek orch                                   # live view
sage steer orch "Add auth module too"            # soft steer
sage steer orch "Start over with Go" --restart   # hard restart + cascade
sage result <task-id>                            # collect result
```

## Dependencies

### Required
- `bash` (4.0+)
- `jq` (1.6+)
- `tmux` (3.0+)

### Optional (per runtime)
- `cline` — Cline CLI
- `claude` — Claude Code CLI (supports Bedrock)
- `claude-agent-acp` — Claude Code ACP adapter (`npm i -g @zed-industries/claude-agent-acp`)
- Any ACP-compatible agent CLI (goose, kiro, gemini, etc.)
- Future: `aider`, `gemini`, `codex`, `ollama`

## Security Model

sage enforces security at multiple layers:

### Agent Name Validation
All agent names are validated against `^[a-zA-Z0-9][a-zA-Z0-9._-]*$` — preventing path traversal attacks (`../escape`). This is enforced at:
- `agent_exists()` — single point of enforcement for all commands that reference agents
- `cmd_create()` — agent creation
- `send_msg()` / `call_agent()` — agent-to-agent messaging (prevents a compromised agent from targeting paths outside `$AGENTS_DIR`)

### Workspace Sandboxing (ACP Runtime)
The ACP runtime sandboxes file I/O to the agent's working directory:
- `fs/write_text_file` — resolved via `realpath`, blocked if outside `$cwd`
- `fs/read_text_file` — same sandbox check
- Blocked writes/reads are logged: `"BLOCKED write to /etc/shadow (outside workspace /home/user/project)"`
- Note: ACP agents still have `terminal` capability (shell access) — this is by design in the ACP protocol

### Runtime Validation
The runner validates runtime names against `^[a-zA-Z0-9_-]+$` before sourcing `runtimes/<name>.sh`, preventing path injection via a malicious `runtime.json`.

### Atomic Writes
All result and reply files use `mktemp` + `mv` to prevent readers (like `cmd_call`'s 0.3s poll loop) from seeing partially-written JSON. This applies to:
- `results/<task-id>.result.json` (all 3 runtimes)
- `reply_dir/<task-id>.json` (all 3 runtimes + `reply()` in common.sh)
- Status file updates (via `jq > tmp && mv tmp`)

### FIFO Security (ACP)
ACP FIFOs are created inside a secure temporary directory (`mktemp -d`) rather than using `mktemp -u` (which has a TOCTOU race between name generation and `mkfifo`).

### Steer File Lifecycle
All runtimes delete `steer.md` after reading it, preventing stale steering context from leaking into subsequent tasks.

## Task Templates

Templates live in `~/.sage/tasks/` as markdown files with YAML frontmatter:

```yaml
---
name: review
description: Code review with prioritized findings
input: files
output: structured
parallel: true
runtime: auto
---

# Code Review Template

Review the provided code for:
1. Security vulnerabilities (🔴 Critical)
2. Correctness bugs (🟡 Important)
3. Performance issues (🟠 Warning)
...
```

### Frontmatter Fields

| Field | Values | Description |
|---|---|---|
| `name` | string | Template identifier |
| `description` | string | Human-readable description |
| `input` | `files` / `description` / `both` | What the template expects |
| `output` | `structured` / `freeform` | Output format hint |
| `parallel` | `true` / `false` | Whether tasks using this template can run in parallel |
| `runtime` | `auto` / `acp` / `bash` | Preferred runtime (`auto` → `acp`) |

### Template Body

Everything after the second `---` is injected as the agent's instructions. Templates can include:
- Checklists the agent must follow
- Output format requirements
- Constraints and priorities
- Example output

### Custom Templates

Add your own templates to `~/.sage/tasks/`:

```bash
cat > ~/.sage/tasks/security-audit.md << 'EOF'
---
name: security-audit
description: Security audit with OWASP Top 10 focus
input: files
output: structured
parallel: true
runtime: auto
---

# Security Audit

Audit the provided code against OWASP Top 10:
1. Injection (SQL, command, LDAP)
2. Broken authentication
...
EOF
```

## Plan Orchestrator

Plans decompose goals into dependency-aware task waves.

### Plan File Format

```json
{
  "plan_id": "plan-1710347041",
  "goal": "Build a REST API with auth and tests",
  "status": "completed",
  "tasks": [
    {
      "id": 1,
      "template": "spec",
      "description": "Define API schema and auth strategy",
      "depends": [],
      "files": [],
      "status": "done"
    },
    {
      "id": 2,
      "template": "implement",
      "description": "Build auth module",
      "depends": [1],
      "files": ["src/auth/"],
      "status": "done",
      "agent": "sage-plan-2-1710347060",
      "sage_task_id": "t-1710347065-12345"
    }
  ]
}
```

### Wave Computation

Dependencies are resolved using recursive topological sort with cycle detection:
- Tasks with no dependencies go in Wave 1
- Each task's wave = `max(wave of dependencies) + 1`
- Circular dependencies are detected and broken (task placed in Wave 1)
- Tasks in the same wave execute in parallel

### Execution Phases (per wave)

1. **Phase 1: Create + Start** — Create ephemeral agents for each task, start them with 1s stagger
2. **Phase 2: Init Wait** — 4s pause for ACP runtime initialization
3. **Phase 3: Send Messages** — Send task descriptions + dependency context to all agents
4. **Phase 4: Wait** — Poll status files until all tasks complete or timeout (600s per task)

### Resume Mode

`sage plan --resume <file>` skips completed tasks and resets stale "running" tasks (from crashes) back to "pending". Results from previously completed tasks are passed as context to downstream dependencies.

### LLM Output Normalization

Planning agents return wildly different JSON formats. The normalizer handles:
- `steps` → `tasks`, `dependencies` → `depends`, `title` → `description`
- Auto-assigns templates by keyword matching when not specified
- Strips markdown code fences (`\`\`\`json ... \`\`\``)
- Extracts the first valid JSON object from the response
