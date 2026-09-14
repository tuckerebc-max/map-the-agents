# Control Plane for Agent Management

## Overview

A Go binary (`control`) that observes and manages running AI agents across projects via tmux introspection. It provides visibility into what agents are doing, the ability to stop them, and a history of past sessions and actions. Interaction happens through a CLI, a TUI dashboard, and an MCP server (Model Context Protocol) that gives Claude Code the same capabilities.

## Core Principles

- **Observer, not launcher** — the control plane watches and manages agents that are already running; it does not start them.
- **Zero agent instrumentation** — agents don't need to know about the control plane. Discovery is pull-based via tmux.
- **CLI/MCP parity** — every operation available in the CLI is available through the MCP server. They are thin wrappers over the same internal API.
- **Single binary** — one Go binary handles all subcommands: daemon, CLI client, TUI, and MCP server.
- **Safe command execution** — all tmux and process interactions use `exec.Command` with discrete argument lists. No shell interpolation, no string concatenation into `sh -c`. This prevents command injection from pane names, window names, or any tmux-controlled values.
- **CGO-free** — the build must never depend on CGO. `modernc.org/sqlite` is the only acceptable SQLite driver. `mattn/go-sqlite3` must never be used.
- **No elevated privileges** — the daemon runs as a regular user and must not require root. If any operation would require elevated privileges, it is a bug.

## Architecture

Three layers sharing one Go module:

### 1. `controld` (daemon)

A background Go process that:

- **Polls tmux** every ~5 seconds against the machine-named tmux session (configurable to watch additional sessions)
- **Maintains an agent registry** in memory with live state for each discovered agent, protected by `sync.RWMutex` (poller takes write lock, request handlers take read lock)
- **Persists history** to SQLite at `~/.control/history.db` (WAL mode enabled)
- **Serves an HTTP/1.1 API over Unix domain socket** at `~/.control/control.sock`
- **Manages its own lifecycle** via PID file at `~/.control/controld.pid`

#### Daemon Lifecycle

**Startup:**
1. Create `~/.control/` directory with `0700` permissions if it doesn't exist
2. Check if `controld.pid` exists and if that PID is alive — if so, abort ("daemon already running")
3. Check if `control.sock` exists — if PID file is absent or PID is dead, remove the stale socket file
4. Write current PID to `controld.pid`
5. Bind and listen on `control.sock` with `0600` permissions
6. Run crash recovery: scan for sessions where `ended_at IS NULL`, check if those PIDs/panes still exist, mark dead ones as `status = 'crashed'` with `ended_at = now`
7. Start the tmux poller goroutine
8. Start the HTTP request handler

**Shutdown (SIGTERM/SIGINT):**
1. Stop accepting new connections
2. Drain in-flight requests (with timeout)
3. Finalize any active sessions in SQLite (`ended_at = now, status = 'daemon_shutdown'`)
4. Close SQLite database handle
5. Remove `control.sock` and `controld.pid`

**SIGHUP:** Reload config (poll interval, session names, scrollback lines).

#### Auto-Start

When a CLI command (e.g., `control ls`) cannot connect to the daemon:
- Print: `Daemon is not running. Start it with: control daemon &`
- Exit with code 2
- A `--auto-start` flag forks the daemon in the background via `os/exec`, waits for the socket to appear, then connects.

### 2. `control` (CLI)

A Go binary that connects to the daemon's HTTP API over the Unix socket. All commands support `--json` for machine-readable output. Default output is human-readable tables.

#### Commands

- `control daemon start` — starts the daemon (foreground by default, `--background` to fork)
- `control daemon stop` — sends shutdown signal to the daemon
- `control daemon status` — reports whether daemon is running, uptime, agent count
- `control ls` — list all live agents
- `control show <id>` — detailed view of one agent, including recent scrollback
- `control stop <id>` — stop an agent (see Signal Strategy below)
- `control history [id]` — without ID: session history with filters. With ID: action log for that session.
- `control tui` — interactive dashboard (bubbletea/lipgloss)
- `control mcp` — start MCP server (stdio transport)

Global flags: `--json`, `--socket <path>`, `--help`

Filter flags on `history` and `ls`: `--project <path>`, `--type <agent-type>`, `--since <duration|ISO8601>`, `--until <duration|ISO8601>`, `--limit <n>` (default 50)

#### Agent Identification

Agents are identified by a short, stable ID derived from tmux's internal pane ID (`#{pane_id}`, e.g., `%0`, `%1`) which is unique and stable for the lifetime of a pane. Commands also support prefix matching and project-name fuzzy matching for convenience (e.g., `control show myproj` matches the agent whose working directory contains "myproj").

In history, sessions use auto-incrementing surrogate keys. The tmux pane ID is stored as a separate column for reference but is never used as a primary key.

#### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Daemon not running |
| 3 | Agent not found |
| 4 | Stop failed |
| 5 | Invalid arguments |

#### Signal Strategy for `control stop`

1. Resolve the agent's process tree — tmux `#{pane_pid}` is the shell; walk child processes to find the actual agent process
2. Verify the PID still matches: check process start time and command match the registry entry
3. Send SIGINT (graceful — this is what Ctrl-C does, which agents handle best)
4. Wait 5 seconds, check if process exited
5. If still alive, send SIGTERM
6. Wait 5 more seconds
7. If still alive and `--force` was passed, send SIGKILL
8. If still alive and `--force` was not passed, report failure (exit code 4)

#### Daemon-Down Behavior

Every CLI command that requires the daemon checks for the socket on startup. If the socket is missing or connection is refused:
- Print: `Error: daemon is not running. Start it with: control daemon start`
- Exit with code 2

#### Output Formatting

- Default: human-readable tables (using lipgloss for alignment and color)
- `--json`: newline-delimited JSON objects
- `control ls` with zero agents: prints "No agents running" to stderr, exits 0
- `control history` with no results: prints "No sessions found" to stderr, exits 0

### 3. MCP Server

Stdio-transport MCP server launched by Claude Code (`control mcp`). Implements MCP protocol version `2024-11-05`.

#### Initialization

Server info: `{ name: "control", version: "0.1.0" }`
Capabilities: `{ tools: {} }`

All logging goes to stderr. Stdout is exclusively for JSON-RPC 2.0 messages (newline-delimited).

#### Claude Code Registration

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "control": {
      "command": "control",
      "args": ["mcp"]
    }
  }
}
```

The `control` binary must be on PATH, or use an absolute path.

#### Tool Schemas

**`list_agents`**
```json
{
  "input": {
    "type": "object",
    "properties": {
      "project": { "type": "string", "description": "Filter by project path (substring match)" },
      "agent_type": { "type": "string", "enum": ["claude-code", "python", "node", "unclassified"] },
      "limit": { "type": "integer", "default": 20, "maximum": 100 }
    }
  },
  "output": {
    "agents": [{ "id": "string", "type": "string", "project": "string", "status": "string", "started_at": "ISO8601", "last_activity": "ISO8601" }],
    "total_count": "integer"
  }
}
```

**`get_agent`**
```json
{
  "input": {
    "type": "object",
    "properties": {
      "id": { "type": "string", "description": "Agent ID or project name prefix" }
    },
    "required": ["id"]
  },
  "output": {
    "id": "string", "type": "string", "project": "string", "pid": "integer",
    "started_at": "ISO8601", "last_activity": "ISO8601",
    "recent_activity": [{ "timestamp": "ISO8601", "action_type": "string", "description": "string" }],
    "scrollback_summary": "string"
  }
}
```

Note: `scrollback_summary` returns a parsed summary of recent activity, not raw scrollback. Raw scrollback may contain secrets and is never exposed through the API.

**`stop_agent`**
```json
{
  "input": {
    "type": "object",
    "properties": {
      "id": { "type": "string", "description": "Agent ID to stop" },
      "force": { "type": "boolean", "default": false, "description": "If true, escalate to SIGKILL. WARNING: this terminates the agent process immediately without cleanup." }
    },
    "required": ["id"]
  },
  "output": { "success": "boolean", "message": "string" }
}
```

Tool description must include: "Terminates a running agent process. The agent will lose any unsaved work. Use with caution."

**`get_history`**
```json
{
  "input": {
    "type": "object",
    "properties": {
      "project": { "type": "string" },
      "agent_type": { "type": "string", "enum": ["claude-code", "python", "node", "unclassified"] },
      "since": { "type": "string", "description": "ISO8601 timestamp or duration like '24h', '7d'" },
      "until": { "type": "string" },
      "limit": { "type": "integer", "default": 50, "maximum": 200 },
      "offset": { "type": "integer", "default": 0 }
    }
  },
  "output": {
    "sessions": [{ "id": "integer", "type": "string", "project": "string", "started_at": "ISO8601", "ended_at": "ISO8601", "status": "string", "action_count": "integer" }],
    "total_count": "integer"
  }
}
```

**`get_actions`**
```json
{
  "input": {
    "type": "object",
    "properties": {
      "session_id": { "type": "integer", "description": "Session ID from get_history" },
      "action_type": { "type": "string" },
      "limit": { "type": "integer", "default": 50, "maximum": 200 },
      "offset": { "type": "integer", "default": 0 }
    },
    "required": ["session_id"]
  },
  "output": {
    "actions": [{ "timestamp": "ISO8601", "action_type": "string", "description": "string", "metadata": "object" }],
    "total_count": "integer"
  }
}
```

**`ping`**
```json
{
  "input": { "type": "object", "properties": {} },
  "output": { "status": "string", "uptime_seconds": "integer", "agent_count": "integer" }
}
```

#### MCP Error Handling

- Invalid parameters → JSON-RPC error code `-32602` (Invalid params)
- Agent not found → tool result with `isError: true` and human-readable message
- Daemon internal error → JSON-RPC error code `-32603` (Internal error)
- Tmux unavailable → tool result with `isError: true` explaining tmux is not running

## Tmux Introspection

Minimum supported tmux version: **2.6**. The daemon checks tmux version on startup and warns if older.

The Tmux Poller runs on a ~5s interval and performs:

### Discovery

Runs `tmux list-panes -s -t <session> -F '#{pane_id} #{pane_pid} #{pane_current_path} #{pane_current_command}'` against the configured session. Each pane is a potential agent.

All tmux commands use `exec.Command("tmux", arg1, arg2, ...)` with discrete arguments. No shell interpolation.

### Tmux Unavailability

The poller distinguishes between:
- **tmux not installed** — daemon logs warning, reports "tmux unavailable" via API, continues running (history queries still work)
- **tmux server not running** — same as above
- **Configured session not found** — daemon logs warning, reports "session not found" via API, continues polling (session may appear later)
- **No panes with agents** — normal state, reports zero agents

### Session Name Handling

The default session name is the short hostname (`hostname -s` equivalent, no domain suffix). Dots in hostnames are stripped because tmux interprets `.` as a window/pane delimiter in target specifications.

Config values for `session_name` and `additional_sessions` are validated on load: must match `[a-zA-Z0-9_-]+`. Invalid values are rejected with an error.

### Classification

Determines agent type from the running process (`#{pane_current_command}`):

- `claude` process → Claude Code agent
- `python` with known agent scripts → custom Python agent
- `node` running agent framework → JS agent
- Unknown → tagged "unclassified" but still tracked

### Status Extraction

Captures recent scrollback via `tmux capture-pane -p -S -<scrollback_lines> -t <pane_id>` and parses for activity signals:

- Claude Code agents: recognizes tool calls, file edits, test runs, commits from output format
- Other agents: best-effort pattern matching
- Diffs against previously seen scrollback using a high-water mark (line count) per agent to record only new actions
- Trailing whitespace is normalized across tmux versions

#### Secret Redaction

Before storing scrollback content in memory or persisting action descriptions to SQLite, a redaction pass strips common secret patterns:
- API keys (patterns: `sk-`, `pk-`, `AKIA`, bearer tokens)
- Environment variable assignments containing `KEY`, `SECRET`, `TOKEN`, `PASSWORD`
- Connection strings (`postgres://`, `mysql://`, `redis://`)

Redacted content is replaced with `[REDACTED]`. Raw scrollback is never persisted or served through the API — only parsed action summaries.

### Session Lifecycle

When an agent disappears (pane closes or process exits), the poller marks it as ended and finalizes the session record in history.

## Data Model

### Live State (in-memory)

Protected by `sync.RWMutex`. Poller goroutine takes write lock; HTTP handlers take read lock.

| Field | Description |
|-------|-------------|
| Agent ID | Stable tmux pane ID (`#{pane_id}`, e.g., `%0`, `%1`) |
| Agent Type | claude-code, python, node, unclassified |
| Working Directory | Project path |
| Tmux Session | Which tmux session this agent is in |
| Window/Pane Name | Tmux identifiers |
| PID | Process ID of the agent (child of shell) |
| Process Start Time | Used for PID verification before signaling |
| Started At | First seen timestamp |
| Last Activity | Last observed activity timestamp |
| Status Summary | Parsed recent activity (redacted) |
| Scrollback High-Water Mark | Line count for dedup |

Only parsed summaries are kept in memory, not raw scrollback. Memory footprint is bounded.

### History (SQLite)

Database: `~/.control/history.db`, created with `0600` permissions.

Pragmas set on every connection open:
- `PRAGMA journal_mode=WAL`
- `PRAGMA foreign_keys=ON`

Schema version tracked via `PRAGMA user_version`. On startup, the daemon checks the version and runs migrations in sequence.

**`sessions`** table:
```sql
CREATE TABLE sessions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tmux_pane_id TEXT NOT NULL,
  tmux_session_name TEXT NOT NULL,
  agent_type TEXT NOT NULL CHECK(agent_type IN ('claude-code', 'python', 'node', 'unclassified')),
  project_path TEXT NOT NULL,
  window_name TEXT,
  pane_name TEXT,
  pid INTEGER NOT NULL,
  status TEXT NOT NULL DEFAULT 'running' CHECK(status IN ('running', 'ended', 'crashed', 'daemon_shutdown')),
  started_at TEXT NOT NULL,
  ended_at TEXT
);

CREATE INDEX idx_sessions_project ON sessions(project_path);
CREATE INDEX idx_sessions_type ON sessions(agent_type);
CREATE INDEX idx_sessions_started ON sessions(started_at);
CREATE INDEX idx_sessions_project_started ON sessions(project_path, started_at);
```

**`actions`** table:
```sql
CREATE TABLE actions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id INTEGER NOT NULL REFERENCES sessions(id),
  timestamp TEXT NOT NULL,
  action_type TEXT NOT NULL,
  description TEXT NOT NULL,
  metadata TEXT,
  content_hash TEXT NOT NULL,
  UNIQUE(session_id, content_hash)
);

CREATE INDEX idx_actions_session ON actions(session_id);
CREATE INDEX idx_actions_timestamp ON actions(timestamp);
CREATE INDEX idx_actions_type ON actions(action_type);
```

Action deduplication: each action is hashed (`SHA-256` of `action_type + description + timestamp rounded to 1s`). The `UNIQUE` constraint on `(session_id, content_hash)` prevents duplicates via `INSERT OR IGNORE`.

`metadata` is a JSON TEXT column for structured data (file paths for file_edit, commit SHAs for commit, test results for test_run).

#### Data Retention

Config: `history_retention_days` (default 90). On daemon startup and daily thereafter, prune sessions and their actions older than the retention period. Run `PRAGMA optimize` after large deletes.

#### Crash Recovery

On daemon startup, scan for `sessions WHERE status = 'running'`:
- If the PID is still alive and the tmux pane still exists → leave as running
- Otherwise → set `status = 'crashed'`, `ended_at = now`

## IPC Protocol

The daemon serves **HTTP/1.1 over a Unix domain socket** using Go's `net/http` with a custom `net.Dialer`. JSON request/response bodies.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/agents` | List agents (query params: `project`, `type`, `limit`) |
| GET | `/agents/:id` | Get agent detail |
| POST | `/agents/:id/stop` | Stop agent (body: `{"force": false}`) |
| GET | `/history` | Session history (query params: `project`, `type`, `since`, `until`, `limit`, `offset`) |
| GET | `/history/:id/actions` | Actions for a session (query params: `action_type`, `limit`, `offset`) |
| GET | `/ping` | Health check |

All responses include `Content-Type: application/json`.

Error responses:
```json
{ "error": "agent not found", "code": "NOT_FOUND" }
```

Error codes: `NOT_FOUND`, `INVALID_PARAMS`, `STOP_FAILED`, `TMUX_UNAVAILABLE`, `INTERNAL_ERROR`

### Socket Security

- `~/.control/` directory: `0700` permissions
- `control.sock`: `0600` permissions
- `history.db`: `0600` permissions
- `controld.pid`: `0600` permissions

The trust boundary is same-user access. Any process running as the same user can connect to the socket.

### Socket Path

Default: `~/.control/control.sock`. On startup, validate that the full socket path is under 104 bytes (macOS `sun_path` limit). If it exceeds the limit, fall back to `/tmp/control-<uid>/control.sock` (directory created with `0700`) and print a warning.

Override via `CONTROL_SOCKET` environment variable or `--socket` CLI flag.

## TUI

The TUI (`control tui`) provides a live-updating dashboard using bubbletea + lipgloss.

### Views

- **Agent list** (default view) — table showing all live agents with ID, type, project, status, last activity. Auto-refreshes every 2 seconds.
- **Agent detail** — selected agent's full info, recent actions, scrollback summary. Press Enter on an agent to enter this view.
- **History** — past sessions, navigable with filters.

### Interactions

- `j`/`k` or arrow keys — navigate list
- `Enter` — view agent detail
- `s` — stop selected agent (with confirmation prompt)
- `f` — filter by project or type
- `h` — toggle history view
- `q` — quit
- `?` — help

The TUI is read-heavy and interactive. It does not expose any capability beyond what `ls`, `show`, `stop`, and `history` provide.

## Project Structure

```
control/
  cmd/
    control/
      main.go           # routes subcommands
  internal/
    daemon/             # controld: poller, registry, HTTP server, lifecycle
    api/                # shared API types, HTTP handlers, MCP tool handlers
    tmux/               # tmux command wrappers, scrollback parsing, redaction
    classifier/         # agent type detection from process info
    history/            # SQLite persistence, migrations, retention
    mcp/                # MCP stdio server, JSON-RPC framing, tool schemas
    tui/                # bubbletea TUI
  go.mod
  go.sum
```

## Tech Stack

- **Language**: Go
- **MCP**: Hand-rolled stdio JSON-RPC 2.0 layer (~200 lines), or [mcp-go](https://github.com/mark3labs/mcp-go) if it proves mature. Evaluate before committing. Community claude-agent-sdk-go is a fallback option.
- **TUI**: bubbletea + lipgloss
- **Database**: SQLite via `modernc.org/sqlite` (pure Go, no CGO — hard constraint)
- **IPC**: HTTP/1.1 over Unix domain socket (`net/http` + custom dialer)
- **MCP transport**: stdio (newline-delimited JSON-RPC 2.0)

## Configuration

Config at `~/.control/config.toml` (optional — all values have defaults):

```toml
# tmux session to watch (default: short hostname)
session_name = "disaster"

# additional tmux sessions to watch
additional_sessions = []

# polling interval (default: 5s)
poll_interval = "5s"

# scrollback lines to capture per pane (default: 500)
scrollback_lines = 500

# history retention in days (default: 90)
history_retention_days = 90
```

Config values for session names are validated: must match `[a-zA-Z0-9_-]+`.

Override socket path via `CONTROL_SOCKET` env var.

## Error Handling

### Tmux Unavailability

| Condition | Behavior |
|-----------|----------|
| `tmux` not on PATH | Daemon starts, logs warning, reports "tmux unavailable" via API |
| tmux server not running | Same — daemon continues, history queries still work |
| Configured session not found | Logs warning, continues polling (session may appear) |
| `capture-pane` fails for one pane | Skip that pane for this poll cycle, log warning |

### Partial Failures

If `capture-pane` fails for a pane that was listed (race: pane closed between list and capture), skip it and continue. This is expected and not an error.

### SQLite Failures

- Corruption: daemon logs error, continues operating without history (live state still works)
- Disk full: writes fail with logged warning, daemon continues
- The daemon holds a single persistent connection with WAL mode

## Non-Goals

- Agent launching/dispatching — agents are started externally
- Cost tracking — no token/spend monitoring
- Configuration management — no centralized settings for agents
- Remote monitoring — local only, Unix socket
- Detecting agents outside tmux — the control plane only sees what's in tmux

## Backlog

Items identified during expert review that are not blocking v1 but should be addressed:

| # | Item | Priority | Notes |
|---|------|----------|-------|
| 1 | **MCP resources** — expose agents as `agent:///<id>` resources for subscription-based status updates | Medium | Enables "keep me updated on agent X" without polling tools |
| 2 | **Tab completion** — shell completion scripts for fish, zsh, bash | Medium | Post-v1, generate via cobra/urfave CLI framework |
| 3 | **Streaming MCP responses** — for large history/action queries | Low | Tools with pagination are sufficient for v1 |
| 4 | **MCP tool name prefixing** — prefix tools with `control_` to avoid cross-server collisions | Low | Claude Code handles disambiguation; revisit if collisions observed |
| 5 | **XDG Base Directory compliance** — respect `$XDG_CONFIG_HOME`, `$XDG_DATA_HOME`, `$XDG_RUNTIME_DIR` on Linux | Low | `~/.control/` is fine for macOS-primary use; add XDG resolution if Linux becomes a target |
| 6 | **tmux hook integration** — use `set-hook pane-exited` for faster session finalization alongside polling | Low | Polling is pragmatic and sufficient; hooks add tmux config coupling |
| 7 | **Binary naming** — `control` is generic and hard to Google. Alternatives: `watchtower`, `foreman`, `rangle`, `agentctl` | Low | Renaming is cheap while there's no ecosystem; decide before v1 release |
| 8 | **Encrypted database** — SQLCipher or equivalent for environments with stricter data-at-rest requirements | Low | File permissions are sufficient for personal use |
| 9 | **Remote monitoring** — expose API over TCP for checking agents from another machine | Low | Out of scope for v1; Unix socket only |
| 10 | **Non-tmux agent detection** — discover agents running outside tmux via process table scanning | Low | Scoping to tmux keeps the system simple and predictable |
| 11 | **MCP project scoping** — restrict MCP tool access by the calling agent's working directory | Medium | Currently all agents are visible cross-project; consider scoping `stop_agent` at minimum |
| 12 | **Daemon auto-start via launchd** — generate and install a launchd plist for automatic daemon startup on macOS | Medium | Currently requires manual `control daemon start` |

## Implementation Notes (Post-Build)

The following changes were made during implementation:

- **Renamed "agent" to "pane"** — all API endpoints, MCP tools, and types use "pane" instead of "agent". Panes are the correct abstraction since not all tmux panes contain agents.
- **API endpoints** use `/panes/` prefix (not `/agents/`)
- **MCP tools**: `list_panes`, `get_pane`, `stop_pane`, `send_to_pane`, `get_pane_conversation`, `get_history`, `get_actions`, `ping`
- **New features added**:
  - `send_to_pane` — sends text input to a tmux pane via tmux send-keys
  - `get_pane_conversation` — reads Claude Code JSONL conversation files
  - `control setup` — interactive first-time configuration wizard
  - `control send` — CLI command for send_to_pane
  - `control conversation` — CLI command for get_pane_conversation
- **TUI expanded** with scrollback viewport, send mode (`:` key), attach (`a` key), conversation view (`c` key), and filter cycling (`f` key)
