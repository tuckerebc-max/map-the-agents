# control

You're running 10 Claude Code instances across tmux panes. Tab 3 is refactoring
auth. Tab 7 is stuck on a test. Tab 12 finished twenty minutes ago and you
didn't notice. You have no idea what any of them are doing without switching to
each one manually.

`control` fixes that. It is a control plane for AI coding agents running in
tmux panes. It polls scrollback, classifies what each pane is doing, records
session history to SQLite, and gives you a single CLI, TUI, and API to see
everything at once.

```
$ control ls
  ID      Type          Project                  Status    Last Activity
  %3      claude-code   ~/src/auth-service       running   2m ago
  %4      claude-code   ~/src/billing-api        running   30s ago
  %7      claude-code   ~/src/billing-api        idle      18m ago
  %9      shell         ~/src/control            idle      1h ago
  %12     claude-code   ~/src/frontend            done     22m ago
```

```
$ control conversation %4
[assistant] I'll refactor the payment handler to use the new gateway interface.
  Let me start by reading the current implementation...
[tool]     Read src/payments/handler.go
[assistant] I see the issue. The handler is calling the old v1 endpoint...
```

## Prerequisites

- Go 1.22+
- tmux

## Quick Start

```bash
# Build
go build -o control ./cmd/control/

# Interactive setup -- picks your tmux session(s) to monitor
./control setup

# Start the daemon in the background
./control daemon start --background

# See what's running
./control ls
```

## CLI Commands

| Command | Description | Flags |
|---|---|---|
| `setup` | Interactive first-time configuration | |
| `daemon start` | Start the daemon | `--background` |
| `daemon stop` | Stop the daemon | |
| `daemon status` | Health check | |
| `ls` | List monitored tmux panes | `--project P` `--type T` `--limit N` |
| `show <id>` | Pane detail with scrollback summary | |
| `stop <id>` | Stop a pane's process | `--force` |
| `send <id> <text>` | Send text/keystrokes to a pane | |
| `conversation <id>` | Show Claude Code conversation | `--limit N` |
| `history [id]` | List sessions or session actions | `--project P` `--type T` `--since S` `--until U` `--limit N` |
| `tui` | Launch interactive TUI dashboard | |
| `mcp` | Start MCP server on stdio | |

`<id>` is a tmux pane ID (like `%4`) or a project name substring (like `billing`).

### Global Flags

These work before or after the subcommand (`control --json ls` and `control ls --json` are equivalent):

| Flag | Description |
|---|---|
| `--json` | JSON output for scripting |
| `--socket <path>` | Override daemon socket path |
| `--auto-start` | Auto-start daemon if not running |

## MCP Integration

MCP (Model Context Protocol) lets a Claude Code instance use the control plane
as a tool -- so one agent can check on other agents, read their conversations,
or send them instructions.

Add this to your Claude Code MCP settings (typically `~/.claude/settings.json`
or your project's `.claude/settings.json`):

```json
{
  "mcpServers": {
    "control": {
      "command": "/absolute/path/to/control",
      "args": ["mcp"],
      "env": {}
    }
  }
}
```

The MCP server exposes tools for listing panes, viewing conversations, stopping
processes, and querying session history.

## TUI Dashboard

Launch with `control tui`. Keybindings:

| Key | Action |
|---|---|
| `j` / `k` | Navigate up / down |
| `Enter` | View detail / session actions |
| `Esc` | Go back |
| `:` | Send text to pane |
| `c` | View conversation |
| `s` | Stop pane |
| `f` | Cycle filter (all / claude / shells) |
| `a` | Attach to pane (exits TUI) |
| `h` | Toggle history view |
| `?` | Toggle help |
| `q` | Quit |

## Configuration

Config file: `~/.control/config.toml`

```toml
# Tmux session to monitor (defaults to hostname)
session_name = "my-session"

# Additional sessions to monitor
additional_sessions = ["other-session"]

# Polling interval for tmux pane updates
poll_interval = "5s"

# Lines of scrollback to capture per pane
scrollback_lines = 500

# Days to retain session history in SQLite
history_retention_days = 90

# Unix socket path (default: ~/.control/control.sock)
socket_path = "/path/to/control.sock"
```

The `CONTROL_SOCKET` environment variable overrides `socket_path` from the
config file.

## How It Works

The daemon polls your tmux sessions on a configurable interval, captures each
pane's scrollback buffer, identifies AI agent processes by their command
signatures, classifies pane status (running, idle, done), and records session
history to a local SQLite database. Everything is served over a Unix domain
socket as a REST API. The CLI, TUI, and MCP server are all clients of that API.
