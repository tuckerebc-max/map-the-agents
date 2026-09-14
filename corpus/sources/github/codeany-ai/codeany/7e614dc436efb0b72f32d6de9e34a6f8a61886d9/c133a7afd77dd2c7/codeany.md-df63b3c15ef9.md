# CODEANY.md

## Project Overview

Codeany is an open-source AI-powered terminal agent, written in Go with Bubble Tea TUI. It aims to be a full-featured replacement for Claude Code with no proprietary code.

## Architecture

- **Runtime**: Go 1.23+, single binary
- **TUI**: Bubble Tea + Lipgloss + Glamour (markdown)
- **Agent SDK**: github.com/codeany-ai/open-agent-sdk-go (local dev via go.work)
- **Build**: `go build -o codeany ./cmd/codeany/` or `make build`

### Directory Structure

```
cmd/codeany/main.go           Entry point, version ldflags
internal/
  cli/root.go                  Cobra CLI, flags, update/upgrade
  config/config.go             Config loading (JSON+YAML+env)
  config/permissions.go        Permission rules persistence
  memory/memory.go             Memory system (MEMORY.md + files)
  pipe/pipe.go                 Non-interactive pipe mode
  plugins/plugins.go           Plugin loading from ~/.codeany/plugins/
  session/session.go           Session save/restore/resume
  skills/skills.go             Skill loading from .codeany/skills/
  slash/slash.go               Command registry + routing + autocomplete
  slash/commands.go            All command implementations
  team/team.go                 Team management + mailbox
  theme/theme.go               Colors and styles
  theme/spinners.go            Spinner verb list
  tui/model.go                 Main Bubble Tea model (TUI core)
  tui/input.go                 Input component (textarea + history)
  tui/render.go                Message/tool rendering
  version/version.go           Build-time version info
  worktree/worktree.go         Git worktree isolation
```

### Config Directory: ~/.codeany/

```
settings.json                  Main config (model, permissions, MCP, hooks)
config.yaml                    YAML config (alternative/legacy)
permissions.json               Persisted permission rules
memory/                        Memory files
sessions/                      Session history + conversation logs
skills/                        User skills
plugins/                       User plugins
teams/                         Team configs + mailboxes
worktrees/                     Git worktree metadata
```

## Commands

```bash
# Build
make build           # or: go build -o codeany ./cmd/codeany/
make install         # go install with ldflags
make vet             # go vet ./...
make dist            # cross-compile 6 platforms

# Dev
go run ./cmd/codeany # run directly
echo "test" | go run ./cmd/codeany -p -y  # pipe mode test
```

## Key Design Decisions

- SDK at open-agent-sdk-go provides: agent loop, tools, MCP, permissions, hooks, cost tracking
- Codeany adds: TUI, slash commands, skills, plugins, teams, sessions, config management
- go.work used for local dev linking to SDK; go.mod uses published version for CI
- All slash commands must be registered in BOTH AllCommands() (for autocomplete) and Handle() (for routing)
- Permission callback in model.go is the single source of truth for tool approval
- Hooks from config are converted to SDK HookFn functions via shell execution

## Reference: Claude Code

The original Claude Code is at ~/code/open-claude-code (TypeScript/Ink).
When improving codeany, scan that codebase for feature parity.
Key areas to compare: src/commands.ts, src/tools/, src/components/, src/screens/
