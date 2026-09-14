# Control Plane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Go binary (`control`) that observes and manages running AI agents via tmux introspection, with a daemon, CLI, MCP server, and TUI.

**Architecture:** Daemon polls tmux, maintains an in-memory agent registry (sync.RWMutex), persists history to SQLite (WAL mode), and serves HTTP/1.1 over a Unix domain socket. CLI and MCP server are thin clients over the same HTTP API. Single binary with subcommands.

**Tech Stack:** Go, modernc.org/sqlite (CGO-free, hard constraint — never use mattn/go-sqlite3), bubbletea/lipgloss, net/http over Unix socket, JSON-RPC 2.0 over stdio (MCP).

**Spec:** `docs/superpowers/specs/2026-03-23-control-plane-design.md`

**Import DAG (no cycles allowed):**
```
cmd/control → cli → api (client)
                  → tui → api (client)
daemon (server) → api (handlers) → registry (interfaces)
                                  → history (interfaces)
                                  → process (interfaces)
daemon (poller) → tmux → (no internal imports)
                → registry
                → history
                → classifier → (no internal imports)
mcp → api (client)
```
`api` MUST NEVER import `daemon`. `registry` MUST NEVER import `tmux` (use `AgentSnapshot` boundary type).

**Commit hygiene:** Stage specific files per commit (not `git add -A`). Use `git add <file1> <file2>` with exact paths.

**Test hygiene:** Use `-race` flag on all tests for packages using concurrency (registry, daemon, server). Use `-timeout 30s` on integration tests. All integration tests must use unique socket paths from `t.TempDir()`.

**SQLite driver note:** Import `modernc.org/sqlite` with blank import `_ "modernc.org/sqlite"` for `database/sql` driver registration.

---

## File Map

```
control/
  cmd/control/main.go                    # Entrypoint, subcommand routing
  internal/
    config/config.go                     # Config loading, validation, defaults
    config/config_test.go
    iface/interfaces.go                  # Package interfaces (AgentRegistry, HistoryStore, etc.)
    history/store.go                     # SQLite open, migrations, pragmas
    history/store_test.go
    history/sessions.go                  # Session CRUD operations
    history/sessions_test.go
    history/actions.go                   # Action CRUD operations
    history/actions_test.go
    history/retention.go                 # Data retention/pruning
    history/retention_test.go
    tmux/runner.go                       # Safe exec.Command wrappers for tmux
    tmux/runner_test.go
    tmux/parser.go                       # Parse tmux list-panes output
    tmux/parser_test.go
    tmux/scrollback.go                   # capture-pane, diffing, high-water mark
    tmux/scrollback_test.go
    tmux/redact.go                       # Secret redaction
    tmux/redact_test.go
    classifier/classify.go              # Agent type detection
    classifier/classify_test.go
    registry/types.go                    # AgentSnapshot boundary type
    registry/registry.go                 # In-memory agent registry with RWMutex
    registry/registry_test.go
    daemon/poller.go                     # Tmux polling loop
    daemon/poller_test.go
    daemon/lifecycle.go                  # PID file, socket cleanup, signal handling
    daemon/lifecycle_test.go
    daemon/server.go                     # HTTP server over Unix socket
    daemon/server_test.go
    daemon/recovery.go                   # Crash recovery on startup
    daemon/recovery_test.go
    api/types.go                         # Shared request/response types
    api/handlers.go                      # HTTP handlers (used by daemon server)
    api/handlers_test.go
    api/client.go                        # HTTP client over Unix socket (used by CLI)
    api/client_test.go
    process/tree.go                      # Process tree walking, PID verification
    process/tree_test.go
    process/signal.go                    # Signal strategy (SIGINT->SIGTERM->SIGKILL)
    process/signal_test.go
    cli/root.go                          # CLI root command, global flags
    cli/daemon.go                        # daemon start/stop/status subcommands
    cli/agents.go                        # ls, show, stop subcommands
    cli/history.go                       # history subcommand
    cli/format.go                        # Table and JSON output formatting
    cli/format_test.go
    cli/root_test.go                     # CLI routing and flag tests
    mcp/server.go                        # JSON-RPC 2.0 stdio framing
    mcp/server_test.go
    mcp/tools.go                         # MCP tool definitions and handlers
    mcp/tools_test.go
    tui/app.go                           # Bubbletea app, view routing
    tui/app_test.go                      # TUI model update tests
    tui/list.go                          # Agent list view
    tui/detail.go                        # Agent detail view
    tui/history.go                       # History view
    tui/styles.go                        # Lipgloss styles
  go.mod
  go.sum
  Makefile
  .gitignore
```

---

### Task 1: Project Scaffolding and Config

**Files:**
- Create: `go.mod`, `cmd/control/main.go`, `internal/config/config.go`, `internal/config/config_test.go`, `.gitignore`, `Makefile`

- [ ] **Step 1: Initialize Go module**

```bash
cd /Users/harper/Public/src/2389/control
go mod init github.com/2389/control
```

Note: If `2389` is not a real GitHub org, use a local module path like `control` instead. The module path only matters for external consumers.

- [ ] **Step 2: Write config test**

Create `internal/config/config_test.go`:
```go
// ABOUTME: Tests for configuration loading, validation, and defaults.
// ABOUTME: Covers TOML parsing, session name validation, socket path checks, and env var overrides.
package config

import (
    "os"
    "path/filepath"
    "strings"
    "testing"
)

func TestDefaultConfig(t *testing.T) {
    cfg := Default()
    if cfg.PollInterval.String() != "5s" {
        t.Errorf("expected poll interval 5s, got %s", cfg.PollInterval)
    }
    if cfg.ScrollbackLines != 500 {
        t.Errorf("expected 500 scrollback lines, got %d", cfg.ScrollbackLines)
    }
    if cfg.HistoryRetentionDays != 90 {
        t.Errorf("expected 90 retention days, got %d", cfg.HistoryRetentionDays)
    }
}

func TestSessionNameValidation(t *testing.T) {
    valid := []string{"disaster", "my-session", "work_01"}
    for _, name := range valid {
        if err := ValidateSessionName(name); err != nil {
            t.Errorf("expected %q to be valid, got error: %v", name, err)
        }
    }
    invalid := []string{"my.session", "has space", "semi;colon", "", "$(whoami)", "name\nnewline"}
    for _, name := range invalid {
        if err := ValidateSessionName(name); err == nil {
            t.Errorf("expected %q to be invalid, got nil error", name)
        }
    }
}

func TestSocketPathLength(t *testing.T) {
    short := "/tmp/x.sock"
    if err := ValidateSocketPath(short); err != nil {
        t.Errorf("short path should be valid: %v", err)
    }
    longPath := "/tmp/" + strings.Repeat("a", 100) + "/control.sock"
    if err := ValidateSocketPath(longPath); err == nil {
        t.Errorf("path of %d bytes should be invalid (>= 104)", len(longPath))
    }
}

func TestSocketPathFromEnvVar(t *testing.T) {
    t.Setenv("CONTROL_SOCKET", "/tmp/custom.sock")
    cfg := Default()
    resolved := ResolveSocketPath(cfg)
    if resolved != "/tmp/custom.sock" {
        t.Errorf("expected CONTROL_SOCKET override, got %s", resolved)
    }
}

func TestLoadFromTOML(t *testing.T) {
    dir := t.TempDir()
    tomlPath := filepath.Join(dir, "config.toml")
    os.WriteFile(tomlPath, []byte(`
session_name = "mybox"
poll_interval = "10s"
scrollback_lines = 200
history_retention_days = 30
`), 0600)

    cfg, err := LoadFromFile(tomlPath)
    if err != nil {
        t.Fatalf("failed to load config: %v", err)
    }
    if cfg.SessionName != "mybox" {
        t.Errorf("expected session_name mybox, got %s", cfg.SessionName)
    }
    if cfg.ScrollbackLines != 200 {
        t.Errorf("expected 200 scrollback lines, got %d", cfg.ScrollbackLines)
    }
}

func TestDefaultConfigFileIsOptional(t *testing.T) {
    cfg, err := LoadFromFile("/nonexistent/path/config.toml")
    if err != nil {
        t.Fatalf("missing config should use defaults, got error: %v", err)
    }
    if cfg.ScrollbackLines != 500 {
        t.Errorf("expected default 500, got %d", cfg.ScrollbackLines)
    }
}
```

- [ ] **Step 3: Run test to verify it fails**

```bash
cd /Users/harper/Public/src/2389/control && go test ./internal/config/ -v
```
Expected: FAIL — package doesn't exist yet.

- [ ] **Step 4: Implement config**

Create `internal/config/config.go` with `Default()`, `LoadFromFile()`, `ValidateSessionName()`, `ValidateSocketPath()`, `ResolveSocketPath()` (checks `CONTROL_SOCKET` env var, then config, then default `~/.control/control.sock`). See spec for implementation details. Hostname dots stripped for tmux compatibility.

- [ ] **Step 5: Add TOML dependency and run tests**

```bash
cd /Users/harper/Public/src/2389/control && go get github.com/BurntSushi/toml && go test ./internal/config/ -v
```
Expected: All tests PASS.

- [ ] **Step 6: Create main.go stub**

Create `cmd/control/main.go` — minimal entrypoint that prints usage and exits. Just enough to verify the binary builds.

- [ ] **Step 7: Create .gitignore and Makefile**

`.gitignore`:
```
control
*.db
.superpowers/
```

`Makefile`:
```makefile
.PHONY: build test lint clean

build:
	go build -o control ./cmd/control/

test:
	go test -race ./... -timeout 30s

lint:
	go vet ./...

clean:
	rm -f control
```

- [ ] **Step 8: Verify it builds**

```bash
cd /Users/harper/Public/src/2389/control && make build
```

- [ ] **Step 9: Commit**

```bash
git add go.mod cmd/control/main.go internal/config/ .gitignore Makefile && git commit -m "feat: project scaffolding with config loading and validation"
```

---

### Task 2: SQLite History Store

**Files:**
- Create: `internal/history/store.go`, `internal/history/store_test.go`

- [ ] **Step 1: Write store test (open, migrations, pragmas)**

Create `internal/history/store_test.go` — test `Open()` creates both tables, sets WAL mode, enables foreign keys, creates DB file with `0600` permissions. Use `t.TempDir()` for isolation.

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/history/ -v -run TestOpen
```

- [ ] **Step 3: Implement store.go**

Create `internal/history/store.go` with `Open(dbPath)`. Use `_ "modernc.org/sqlite"` blank import for driver registration. Schema creation SQL from spec. Pragma setup. `user_version` migration check. Set file permissions to `0600` via `os.Chmod` after creation.

```bash
go get modernc.org/sqlite
```

- [ ] **Step 4: Run store tests**

```bash
go test ./internal/history/ -v -run TestOpen
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/history/store.go internal/history/store_test.go go.mod go.sum && git commit -m "feat: SQLite store with schema, pragmas, and migrations"
```

---

### Task 3: Session CRUD

**Files:**
- Create: `internal/history/sessions.go`, `internal/history/sessions_test.go`

- [ ] **Step 1: Write sessions tests**

Test `CreateSession`, `EndSession` (sets ended_at and status), `ListSessions` with filters (project, type, time range, limit/offset), `GetSession`, `FindRunningSessions` (returns sessions where status='running'), `CountActionsForSession`. Include adversarial SQL input tests: `project = "'; DROP TABLE sessions; --"` should return empty results, not SQL errors.

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/history/ -v -run TestSession
```

- [ ] **Step 3: Implement sessions.go**

Session CRUD with parameterized queries only. Dynamic WHERE clause building uses parameter placeholders, never string concatenation for values. LIKE queries escape `%` and `_` wildcards in user input.

- [ ] **Step 4: Run sessions tests**

```bash
go test ./internal/history/ -v -run TestSession
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/history/sessions.go internal/history/sessions_test.go && git commit -m "feat: session CRUD with parameterized queries"
```

---

### Task 4: Action CRUD

**Files:**
- Create: `internal/history/actions.go`, `internal/history/actions_test.go`

- [ ] **Step 1: Write actions tests**

Test `RecordAction` with dedup (same content_hash is ignored via INSERT OR IGNORE), `ListActions` with filters (session_id, action_type, limit/offset), action count per session. Test metadata JSON column round-trip. Test adversarial inputs in action_type and description.

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/history/ -v -run TestAction
```

- [ ] **Step 3: Implement actions.go**

Action CRUD. SHA-256 content hash for dedup. `INSERT OR IGNORE` on unique constraint. Metadata stored as JSON TEXT.

- [ ] **Step 4: Run actions tests**

```bash
go test ./internal/history/ -v -run TestAction
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/history/actions.go internal/history/actions_test.go && git commit -m "feat: action CRUD with content-hash deduplication"
```

---

### Task 5: Data Retention

**Files:**
- Create: `internal/history/retention.go`, `internal/history/retention_test.go`

- [ ] **Step 1: Write retention tests**

Test that `Prune(days)` deletes sessions and their actions older than N days, leaves recent ones, handles empty DB. Test that foreign key cascade works (actions deleted when session deleted).

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/history/ -v -run TestPrune
```

- [ ] **Step 3: Implement retention.go**

Delete actions for old sessions first (foreign key), then sessions. Run `PRAGMA optimize` after.

- [ ] **Step 4: Run retention tests**

```bash
go test ./internal/history/ -v -run TestPrune
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/history/retention.go internal/history/retention_test.go && git commit -m "feat: history data retention and pruning"
```

---

### Task 6: Tmux Parser

**Files:**
- Create: `internal/tmux/parser.go`, `internal/tmux/parser_test.go`

- [ ] **Step 1: Write parser tests**

```go
func TestParseListPanes(t *testing.T) {
    raw := "%0 12345 /Users/harper/project1 claude\n%1 12346 /Users/harper/project2 python\n%2 12347 /Users/harper/project3 node\n"
    panes, err := ParseListPanes(raw)
    if err != nil {
        t.Fatalf("parse error: %v", err)
    }
    if len(panes) != 3 {
        t.Fatalf("expected 3 panes, got %d", len(panes))
    }
    if panes[0].PaneID != "%0" || panes[0].PID != 12345 || panes[0].CurrentPath != "/Users/harper/project1" || panes[0].CurrentCommand != "claude" {
        t.Errorf("unexpected pane 0: %+v", panes[0])
    }
}

func TestParseListPanesEmptyInput(t *testing.T) {
    panes, err := ParseListPanes("")
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
    if len(panes) != 0 {
        t.Errorf("expected 0 panes, got %d", len(panes))
    }
}

func TestParseListPanesPathWithSpaces(t *testing.T) {
    raw := "%0 12345 /Users/harper/My Projects/foo claude\n"
    panes, err := ParseListPanes(raw)
    if err != nil {
        t.Fatalf("parse error: %v", err)
    }
    if panes[0].CurrentPath != "/Users/harper/My Projects/foo" {
        t.Errorf("path with spaces not handled: %s", panes[0].CurrentPath)
    }
}
```

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/tmux/ -v -run TestParse
```

- [ ] **Step 3: Implement parser.go**

`PaneInfo` struct and `ParseListPanes(raw string) ([]PaneInfo, error)`. Handle paths with spaces by splitting from the right (command is last field, PID is second, pane ID is first, everything in between is the path).

- [ ] **Step 4: Run parser tests**

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/tmux/parser.go internal/tmux/parser_test.go && git commit -m "feat: tmux list-panes output parser"
```

---

### Task 7: Tmux Runner (Safe Command Execution)

**Files:**
- Create: `internal/tmux/runner.go`, `internal/tmux/runner_test.go`

- [ ] **Step 1: Write runner tests**

Define `CommandExecutor` interface in runner.go: `Execute(name string, args ...string) ([]byte, error)`. Write tests using a recording executor (test double that captures the exact args passed, returns canned output). Test:
- `ListPanes` constructs correct args: `["tmux", "list-panes", "-s", "-t", session, "-F", formatStr]`
- `CapturePaneScrollback` constructs correct args
- `Version` constructs correct args
- Adversarial pane ID `%0; rm -rf /` is passed as a single discrete arg, not split
- `IsAvailable` returns false when executor returns error

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/tmux/ -v -run TestRunner
```

- [ ] **Step 3: Implement runner.go**

`Runner` struct with `CommandExecutor` interface. Default executor uses `exec.Command`. All tmux commands pass args discretely — NEVER use `sh -c` or string concatenation. Add `context.Context` with timeout (10s) on all exec.Command calls to prevent tmux hangs.

- [ ] **Step 4: Run runner tests**

```bash
go test ./internal/tmux/ -v -run TestRunner
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/tmux/runner.go internal/tmux/runner_test.go && git commit -m "feat: tmux runner with safe command execution"
```

---

### Task 8: Scrollback Processing and Secret Redaction

**Files:**
- Create: `internal/tmux/scrollback.go`, `internal/tmux/scrollback_test.go`, `internal/tmux/redact.go`, `internal/tmux/redact_test.go`

- [ ] **Step 1: Write comprehensive redaction tests**

Table-driven tests with 20+ patterns. Use obviously fake values to avoid tripping secret scanners:

```go
func TestRedact(t *testing.T) {
    tests := []struct{ name, input, expected string }{
        // OpenAI keys
        {"openai sk-", "export KEY=sk-FAKE000000000000000000000000", "export KEY=[REDACTED]"},
        // AWS keys
        {"aws akia", "AWS_ACCESS_KEY_ID=AKIAFAKEEXAMPLE00000", "AWS_ACCESS_KEY_ID=[REDACTED]"},
        // Bearer tokens
        {"bearer", "Authorization: Bearer eyJFAKE.eyJGQUtF.FAKE", "Authorization: Bearer [REDACTED]"},
        // GitHub tokens
        {"github ghp", "GITHUB_TOKEN=ghp_FAKE00000000000000000000000000000000", "GITHUB_TOKEN=[REDACTED]"},
        {"github gho", "token=gho_FAKE0000000000000000000000000000", "token=[REDACTED]"},
        {"github ghs", "GH=ghs_FAKE00000000000000000000000000000", "GH=[REDACTED]"},
        // Anthropic keys
        {"anthropic", "ANTHROPIC_API_KEY=ant-api-FAKE00000000000000", "ANTHROPIC_API_KEY=[REDACTED]"},
        // Stripe keys
        {"stripe sk", "STRIPE_KEY=sk_live_FAKE000000000000000000", "STRIPE_KEY=[REDACTED]"},
        {"stripe pk", "STRIPE_PUB=pk_live_FAKE00000000000000000", "STRIPE_PUB=[REDACTED]"},
        // Env vars with secret-like names
        {"env PASSWORD", "DB_PASSWORD=hunter2", "DB_PASSWORD=[REDACTED]"},
        {"env SECRET", "APP_SECRET=mysecretvalue", "APP_SECRET=[REDACTED]"},
        {"env TOKEN", "AUTH_TOKEN=abc123", "AUTH_TOKEN=[REDACTED]"},
        {"env with spaces", "OPENAI_KEY =  sk-FAKE000000000000", "OPENAI_KEY =  [REDACTED]"},
        // Connection strings
        {"postgres", "DATABASE_URL=postgres://user:pass@host/db", "DATABASE_URL=[REDACTED]"},
        {"mysql", "MYSQL_URL=mysql://user:pass@host/db", "MYSQL_URL=[REDACTED]"},
        {"redis", "REDIS_URL=redis://user:pass@host:6379", "REDIS_URL=[REDACTED]"},
        {"mongodb", "MONGO=mongodb+srv://user:pass@cluster.example.com", "MONGO=[REDACTED]"},
        {"amqp", "AMQP_URL=amqp://user:pass@host:5672", "AMQP_URL=[REDACTED]"},
        // PEM blocks
        {"pem header", "-----BEGIN RSA PRIVATE KEY-----", "[REDACTED]"},
        {"pem ec", "-----BEGIN EC PRIVATE KEY-----", "[REDACTED]"},
        // Safe content (should NOT be redacted)
        {"normal output", "just normal output", "just normal output"},
        {"code with sk var", "var skipCount = 5", "var skipCount = 5"},
        {"url without creds", "https://example.com/api", "https://example.com/api"},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Redact(tt.input)
            if got != tt.expected {
                t.Errorf("Redact(%q) = %q, want %q", tt.input, got, tt.expected)
            }
        })
    }
}
```

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/tmux/ -v -run TestRedact
```

- [ ] **Step 3: Implement redact.go**

Regex-based redaction. Patterns for: `sk-`, `pk-`, `pk_live_`, `sk_live_`, `sk_test_`, `AKIA`, bearer tokens, `ghp_`, `gho_`, `ghs_`, `ghr_`, `ant-api-`, env vars with KEY/SECRET/TOKEN/PASSWORD in the name, connection strings (`postgres://`, `mysql://`, `redis://`, `mongodb+srv://`, `amqp://`), PEM private key headers.

- [ ] **Step 4: Run redaction tests**

Expected: PASS.

- [ ] **Step 5: Write scrollback diff tests**

Test `ScrollbackTracker` — given two captures, it returns only the new lines. Test high-water mark tracking. Test trailing whitespace normalization. Test empty captures. Test pane reset (shorter capture than previous = reset high-water mark).

- [ ] **Step 6: Run to verify failure**

- [ ] **Step 7: Implement scrollback.go**

`ScrollbackTracker` struct per agent. Stores high-water mark (line count). `Diff(paneID, newCapture)` returns new lines since last capture. Normalizes trailing whitespace. The tracker is single-goroutine only (called by the poller) — scrollback summaries are written INTO the registry (protected by registry's RWMutex) so handlers can read them safely.

- [ ] **Step 8: Run scrollback tests**

Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add internal/tmux/redact.go internal/tmux/redact_test.go internal/tmux/scrollback.go internal/tmux/scrollback_test.go && git commit -m "feat: scrollback diffing with comprehensive secret redaction"
```

---

### Task 9: Agent Classifier

**Files:**
- Create: `internal/classifier/classify.go`, `internal/classifier/classify_test.go`

- [ ] **Step 1: Write classifier tests**

```go
func TestClassify(t *testing.T) {
    tests := []struct{ command, expected string }{
        {"claude", "claude-code"},
        {"/opt/homebrew/bin/claude", "claude-code"},
        {"python", "python"},
        {"python3", "python"},
        {"python3.12", "python"},
        {"node", "node"},
        {"vim", "unclassified"},
        {"bash", "unclassified"},
        {"", "unclassified"},
    }
    for _, tt := range tests {
        got := Classify(tt.command)
        if got != tt.expected {
            t.Errorf("Classify(%q) = %q, want %q", tt.command, got, tt.expected)
        }
    }
}
```

- [ ] **Step 2: Run to verify failure**

- [ ] **Step 3: Implement classify.go**

Simple string matching on the command basename (`filepath.Base`). Returns one of: `claude-code`, `python`, `node`, `unclassified`.

- [ ] **Step 4: Run classifier tests**

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/classifier/ && git commit -m "feat: agent type classifier"
```

---

### Task 10: Package Interfaces and Boundary Types

**Files:**
- Create: `internal/iface/interfaces.go`, `internal/registry/types.go`

- [ ] **Step 1: Define interfaces and boundary types**

Create `internal/iface/interfaces.go` — defines the interfaces that decouple packages:

```go
// ABOUTME: Package interfaces for decoupling daemon, handlers, and data stores.
// ABOUTME: All cross-package dependencies go through these interfaces.
package iface

import "time"

// AgentRegistry provides read access to the live agent registry.
type AgentRegistry interface {
    List(filter AgentFilter) []AgentSnapshot
    Get(id string) (AgentSnapshot, bool) // supports pane ID or project prefix match
}

// HistoryStore provides read/write access to session/action history.
type HistoryStore interface {
    CreateSession(s SessionRecord) (int64, error)
    EndSession(id int64, status string) error
    GetSession(id int64) (SessionRecord, error)
    ListSessions(filter SessionFilter) ([]SessionRecord, int, error) // results, total, error
    FindRunningSessions() ([]SessionRecord, error)
    RecordAction(sessionID int64, a ActionRecord) error
    ListActions(sessionID int64, filter ActionFilter) ([]ActionRecord, int, error)
    Prune(days int) error
    Close() error
}

// AgentStopper handles the process signal strategy.
type AgentStopper interface {
    Stop(pid int, processStartTime time.Time, expectedCommand string, force bool) (StopResult, error)
}

// TmuxLister abstracts tmux command execution.
type TmuxLister interface {
    ListPanes(session string) ([]PaneInfo, error)
    CapturePaneScrollback(paneID string, lines int) (string, error)
    Version() (string, error)
    IsAvailable() bool
}

// Filter/record types follow...
```

Create `internal/registry/types.go` — defines `AgentSnapshot` as the boundary type between tmux/poller and registry. The poller converts `tmux.PaneInfo` to `AgentSnapshot` before calling `registry.Update()`. This prevents registry from importing tmux.

- [ ] **Step 2: Verify it compiles**

```bash
go build ./internal/iface/ && go build ./internal/registry/
```

- [ ] **Step 3: Commit**

```bash
git add internal/iface/ internal/registry/types.go && git commit -m "feat: package interfaces and boundary types"
```

---

### Task 11: Agent Registry

**Files:**
- Create: `internal/registry/registry.go`, `internal/registry/registry_test.go`

- [ ] **Step 1: Write registry tests**

Test `Registry.Update([]AgentSnapshot)` — adds new agents, removes departed ones, returns lists of added/removed. Test `Get(id)` with exact pane ID match. Test `Get(prefix)` with project-name fuzzy match. Test `List()` with filters. Test concurrent read/write safety using goroutines with `-race` flag.

- [ ] **Step 2: Run to verify failure**

```bash
go test -race ./internal/registry/ -v
```

- [ ] **Step 3: Implement registry.go**

`Registry` with `sync.RWMutex`. Implements `iface.AgentRegistry`. `Update()` takes `[]AgentSnapshot` (not `PaneInfo`). `Get(id)` supports exact pane ID or project-name prefix match. `List()` with optional filters. Scrollback summary is stored in the `AgentSnapshot` and updated by the poller under write lock.

- [ ] **Step 4: Run registry tests**

```bash
go test -race ./internal/registry/ -v
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/registry/registry.go internal/registry/registry_test.go && git commit -m "feat: in-memory agent registry with RWMutex"
```

---

### Task 12: Process Tree and Signal Handling

**Files:**
- Create: `internal/process/tree.go`, `internal/process/tree_test.go`, `internal/process/signal.go`, `internal/process/signal_test.go`

- [ ] **Step 1: Write process tree tests**

Test `FindChildProcess(parentPID)` — returns child PIDs. Test `VerifyProcess(pid, expectedStartTime, expectedCommand)` — returns true only if PID still matches. Test PID recycling scenario: spawn a process, record its PID and start time, kill it, verify that `VerifyProcess` rejects the stale entry (start time won't match even if PID is reused). Note: `ps -p <pid> -o lstart=,comm=` output format varies between macOS and Linux — handle both.

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/process/ -v -run TestTree
```

- [ ] **Step 3: Implement tree.go**

Use `pgrep -P <pid>` to find child processes. Use `ps -p <pid> -o lstart=,comm=` to verify PID identity. All via `exec.Command` with discrete args. Implements `iface.AgentStopper` partially (PID verification portion).

- [ ] **Step 4: Run process tree tests**

Expected: PASS.

- [ ] **Step 5: Write signal tests**

Test `StopAgent(pid, startTime, command, force)`:
- Spawn a subprocess (`sleep 3600`), record its PID and start time
- Send SIGINT, verify it exits (test with a subprocess that handles SIGINT)
- Test escalation: subprocess ignores SIGINT → SIGTERM sent after 5s
- Test `--force`: SIGKILL after SIGTERM fails
- Test PID verification before each signal in the chain
- Test that stale PID (process already dead) returns success immediately

- [ ] **Step 6: Run to verify failure**

```bash
go test ./internal/process/ -v -run TestStop
```

- [ ] **Step 7: Implement signal.go**

Signal strategy from spec: SIGINT → 5s wait → SIGTERM → 5s wait → SIGKILL (if force). Verify PID before each signal via `VerifyProcess`. Return structured `StopResult` with success/failure/reason and appropriate exit code mapping.

- [ ] **Step 8: Run signal tests**

```bash
go test ./internal/process/ -v -run TestStop
```
Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add internal/process/ && git commit -m "feat: process tree walking and signal strategy"
```

---

### Task 13: Shared API Types

**Files:**
- Create: `internal/api/types.go`

- [ ] **Step 1: Create types.go**

Define all shared request/response types matching the spec's tool schemas: `AgentSummary`, `AgentDetail`, `SessionSummary`, `ActionEntry`, `PingResponse`, `StopRequest`, `StopResponse`, `ListParams`, `HistoryParams`, `ErrorResponse`. Include JSON tags. Error code string constants (`NOT_FOUND`, `INVALID_PARAMS`, `STOP_FAILED`, `TMUX_UNAVAILABLE`, `INTERNAL_ERROR`). Exit code int constants (0-5). All responses include only `error` and `code` fields — never expose stack traces, file paths, or internal SQLite errors.

- [ ] **Step 2: Verify it compiles**

```bash
go build ./internal/api/
```

- [ ] **Step 3: Commit**

```bash
git add internal/api/types.go && git commit -m "feat: shared API types and error codes"
```

---

### Task 14: HTTP API Handlers

**Files:**
- Create: `internal/api/handlers.go`, `internal/api/handlers_test.go`

- [ ] **Step 1: Write handler tests**

Test each endpoint using `httptest.NewRecorder`. Inject test doubles implementing `iface.AgentRegistry`, `iface.HistoryStore`, and `iface.AgentStopper`. Use Go 1.22+ `http.ServeMux` with `{id}` wildcards (not Express `:id` syntax).

Tests for each endpoint:
- `GET /agents` — returns list, respects filters, returns `Content-Type: application/json`
- `GET /agents/{id}` — returns agent detail, returns `NOT_FOUND` for missing agent
- `POST /agents/{id}/stop` — returns stop result, handles force param, returns `STOP_FAILED` on failure
- `GET /history` — returns sessions with pagination (`limit`, `offset`, `total_count`)
- `GET /history/{id}/actions` — returns actions with pagination
- `GET /ping` — returns status, uptime, agent count

Error response tests:
- Invalid `{id}` (path traversal `../../../etc/passwd`) → `INVALID_PARAMS`
- Negative limit/offset → `INVALID_PARAMS`
- Error responses contain ONLY `error` and `code` fields (no extra keys)

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/api/ -v -run TestHandler
```

- [ ] **Step 3: Implement handlers.go**

HTTP handlers that accept `iface.AgentRegistry`, `iface.HistoryStore`, `iface.AgentStopper` via constructor. Return JSON responses. Map errors to error codes. Validate `{id}` against pattern `^%\d+$` for pane IDs or alphanumeric for fuzzy match. Clamp limit to [1, 200], offset to [0, max]. Build `http.ServeMux` with Go 1.22+ `{id}` wildcard syntax.

- [ ] **Step 4: Run handler tests**

```bash
go test ./internal/api/ -v -run TestHandler
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/api/handlers.go internal/api/handlers_test.go && git commit -m "feat: HTTP API handlers for all endpoints"
```

---

### Task 15: API Client (CLI uses this)

**Files:**
- Create: `internal/api/client.go`, `internal/api/client_test.go`

- [ ] **Step 1: Write client tests**

Use `httptest` with Unix socket — start a test server on a temp socket, connect via the client. Test all methods: `ListAgents`, `GetAgent`, `StopAgent`, `GetHistory`, `GetActions`, `Ping`. Test daemon-down detection (connection refused → returns error with exit code 2). Each test uses a unique socket path from `t.TempDir()`.

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/api/ -v -run TestClient
```

- [ ] **Step 3: Implement client.go**

`Client` struct with socket path. Custom `http.Transport` with `DialContext` for Unix socket. Methods for each API operation. Returns typed responses or exit-code-aware errors.

- [ ] **Step 4: Run client tests**

```bash
go test ./internal/api/ -v -run TestClient
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/api/client.go internal/api/client_test.go && git commit -m "feat: API client over Unix socket"
```

---

### Task 16: Daemon Lifecycle

**Files:**
- Create: `internal/daemon/lifecycle.go`, `internal/daemon/lifecycle_test.go`, `internal/daemon/recovery.go`, `internal/daemon/recovery_test.go`

- [ ] **Step 1: Write lifecycle tests**

Concrete test cases:
- `TestCreateDirectory` — creates `~/.control/` with `0700`, verifies mode bits via `os.Stat`
- `TestPIDFileCreation` — writes PID, verifies file has `0600` permissions, PID matches
- `TestPIDFileRemoval` — cleanup removes PID file
- `TestStaleSocketDetection` — stale socket file (no running daemon) is removed on startup
- `TestDaemonAlreadyRunning` — PID file exists with alive PID → returns error
- `TestGracefulShutdown` — send SIGTERM, verify sessions finalized, socket removed, PID file removed
- `TestSIGHUPReload` — send SIGHUP, verify config re-read from disk, poll interval updated on running daemon
- `TestSocketPathFallback` — when default path > 104 bytes, falls back to `/tmp/control-<uid>/` with `0700`
- `TestSocketPermissions` — after bind, socket file has `0600` permissions (explicit `os.Chmod` after `net.Listen`)

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/daemon/ -v -run TestLifecycle -run TestPID -run TestStale -run TestDaemon -run TestGraceful -run TestSIGHUP -run TestSocket
```

- [ ] **Step 3: Implement lifecycle.go**

`Lifecycle` struct managing startup/shutdown sequence from spec. PID file at `~/.control/controld.pid` with `0600`. Socket with explicit `os.Chmod(sockPath, 0600)` after `net.Listen`. Socket path validation (104 byte limit with fallback). Signal handlers: SIGTERM/SIGINT for graceful shutdown (drain with 5s timeout), SIGHUP to reload config from disk.

- [ ] **Step 4: Run lifecycle tests**

```bash
go test -race ./internal/daemon/ -v
```
Expected: PASS.

- [ ] **Step 5: Write recovery tests**

- `TestCrashRecovery` — create sessions with `status = 'running'` in test DB, run recovery, verify dead ones get `status = 'crashed'`, `ended_at = now`
- `TestCrashRecoveryLivePID` — session with alive PID and existing pane → left as running

- [ ] **Step 6: Run to verify failure**

- [ ] **Step 7: Implement recovery.go**

Query `FindRunningSessions`, check each PID (via `VerifyProcess`) and pane (via `TmuxLister.ListPanes`), mark dead ones as crashed.

- [ ] **Step 8: Run recovery tests**

Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add internal/daemon/lifecycle.go internal/daemon/lifecycle_test.go internal/daemon/recovery.go internal/daemon/recovery_test.go && git commit -m "feat: daemon lifecycle with crash recovery and SIGHUP reload"
```

---

### Task 17: Daemon Poller

**Files:**
- Create: `internal/daemon/poller.go`, `internal/daemon/poller_test.go`

- [ ] **Step 1: Write poller tests**

Test poll cycle using test doubles for `iface.TmuxLister`, registry, and history store:
- Given pane list → registry gets updated with `AgentSnapshot` (converted from `PaneInfo` by poller, not registry)
- New agents → `CreateSession` called on history store
- Scrollback captured → actions recorded
- Departed agents → `EndSession` called
- Tmux unavailable → no crash, returns gracefully
- `capture-pane` fails for one pane (race: pane closed between list and capture) → skip pane, continue with others
- Daily retention ticker fires → `Prune` called
- Tmux version check on startup: warn if < 2.6

- [ ] **Step 2: Run to verify failure**

```bash
go test -race ./internal/daemon/ -v -run TestPoller
```

- [ ] **Step 3: Implement poller.go**

`Poller` struct accepting `iface.TmuxLister`, registry, `iface.HistoryStore`, classifier, and `ScrollbackTracker`. Converts `PaneInfo` → `AgentSnapshot` at the boundary (poller owns this conversion, keeping registry decoupled from tmux). `Poll()` runs one cycle. `Start(ctx)` runs poll loop on interval. Handles tmux unavailability gracefully. Daily retention ticker calls `store.Prune(retentionDays)`. Checks tmux version >= 2.6 on first poll and logs warning if older.

- [ ] **Step 4: Run poller tests**

```bash
go test -race ./internal/daemon/ -v -run TestPoller
```
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/daemon/poller.go internal/daemon/poller_test.go && git commit -m "feat: tmux polling loop with scrollback tracking and retention"
```

---

### Task 18: Daemon Server (Wiring)

**Files:**
- Create: `internal/daemon/server.go`, `internal/daemon/server_test.go`

- [ ] **Step 1: Write server integration test**

Start a daemon server on a temp Unix socket with a temp DB. Use the API client to:
- Verify `Ping` returns uptime and agent count
- Verify `ListAgents` returns empty list
- Verify error responses have correct format
This is the first full integration test — real HTTP over real Unix socket. Each test uses unique paths from `t.TempDir()`.

- [ ] **Step 2: Run to verify failure**

```bash
go test -race ./internal/daemon/ -v -run TestServer -timeout 30s
```

- [ ] **Step 3: Implement server.go — struct and constructor**

`Server` struct with fields: lifecycle, config, history store, registry, poller, HTTP handler mux, start time (for uptime).

- [ ] **Step 4: Implement server.go — Start()**

Wire up: open history store, create registry, create poller, run crash recovery, build HTTP mux from handlers, start lifecycle (PID file, socket listen), start poller goroutine, start HTTP server.

- [ ] **Step 5: Implement server.go — Shutdown()**

Stop poller, finalize active sessions, drain HTTP connections (5s timeout), close store, lifecycle cleanup.

- [ ] **Step 6: Run server tests**

```bash
go test -race ./internal/daemon/ -v -run TestServer -timeout 30s
```
Expected: PASS.

- [ ] **Step 7: Test SQLite failure resilience**

Add tests:
- `TestServerWithCorruptDB` — server starts and operates without history when DB is corrupt
- `TestServerDiskFull` — writes fail with logged warning, daemon continues serving live data

- [ ] **Step 8: Run failure resilience tests**

Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add internal/daemon/server.go internal/daemon/server_test.go && git commit -m "feat: daemon server wiring with integration tests"
```

---

### Task 19: CLI Output Formatting

**Files:**
- Create: `internal/cli/format.go`, `internal/cli/format_test.go`

- [ ] **Step 1: Write format tests**

Test `FormatAgentTable([]AgentSummary)` — produces aligned table. Test `FormatJSON(any)` — produces newline-delimited JSON. Test empty results (prints message to stderr). Test `FormatHistory`, `FormatActions`, `FormatPing`.

- [ ] **Step 2: Run to verify failure**

- [ ] **Step 3: Implement format.go**

Table formatting with lipgloss. JSON formatting. Handles zero-result messages.

```bash
go get github.com/charmbracelet/lipgloss
```

- [ ] **Step 4: Run format tests**

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add internal/cli/format.go internal/cli/format_test.go && git commit -m "feat: CLI output formatting with table and JSON modes"
```

---

### Task 20: CLI Commands

**Files:**
- Create: `internal/cli/root.go`, `internal/cli/root_test.go`, `internal/cli/daemon.go`, `internal/cli/agents.go`, `internal/cli/history.go`

- [ ] **Step 1: Write CLI routing tests**

Create `internal/cli/root_test.go`:
- Test subcommand dispatch: `ls` routes to list handler, `daemon start` routes to daemon handler
- Test unknown command prints help to stderr, exits 1
- Test `--json` flag is parsed and propagated
- Test `--socket` flag overrides default socket path
- Test `--auto-start` forks daemon when socket is missing (use a test double for the forking)
- Test daemon-down detection: socket missing → stderr message, exit code 2
- Test each exit code maps to correct scenario (agent not found → 3, stop failed → 4, etc.)

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/cli/ -v
```

- [ ] **Step 3: Implement root.go**

Root command with global flag parsing (`--json`, `--socket`, `--auto-start`). Subcommand routing. Help text with per-subcommand descriptions. `--auto-start` forks daemon via `os/exec`, waits for socket (poll every 100ms, timeout 5s).

- [ ] **Step 4: Implement daemon.go**

`daemon start` (foreground by default, `--background` to fork), `daemon stop` (connects to socket, sends shutdown), `daemon status` (ping + uptime + agent count).

- [ ] **Step 5: Implement agents.go**

`ls` (with `--project`, `--type`, `--limit` filters), `show <id>`, `stop <id>` (with `--force`).

- [ ] **Step 6: Implement history.go**

`history [id]` — without ID lists sessions with `--project`, `--type`, `--since`, `--until`, `--limit` filters. With ID lists actions for that session.

- [ ] **Step 7: Run CLI tests**

```bash
go test ./internal/cli/ -v
```
Expected: PASS.

- [ ] **Step 8: Wire into main.go**

Update `cmd/control/main.go` to use the CLI root command.

- [ ] **Step 9: Build and test help output**

```bash
make build && ./control --help && ./control ls --help && ./control daemon --help
```

- [ ] **Step 10: Commit**

```bash
git add internal/cli/ cmd/control/main.go && git commit -m "feat: CLI commands with subcommand routing and exit codes"
```

---

### Task 21: MCP Server

**Files:**
- Create: `internal/mcp/server.go`, `internal/mcp/server_test.go`, `internal/mcp/tools.go`, `internal/mcp/tools_test.go`

**Decision gate:** Before starting, evaluate `mcp-go` (`github.com/mark3labs/mcp-go`). Check: does it support stdio transport, protocol version `2024-11-05`, and the `initialize`/`tools/list`/`tools/call` methods? If yes and well-maintained, use it. If not, hand-roll JSON-RPC 2.0 framing (~200 lines). Document the decision in a code comment.

- [ ] **Step 1: Write JSON-RPC framing tests**

Test reading JSON-RPC 2.0 messages from stdin (newline-delimited). Test writing responses to stdout. Test `initialize` handshake returns server info `{ name: "control", version: "0.1.0" }` and capabilities `{ tools: {} }` with protocol version `2024-11-05`. Test `tools/list` response contains all 6 tool schemas. Test stderr-only logging (nothing written to stdout except JSON-RPC).

- [ ] **Step 2: Run to verify failure**

```bash
go test ./internal/mcp/ -v -run TestServer
```

- [ ] **Step 3: Implement server.go**

JSON-RPC 2.0 message framing over stdin/stdout. Handle `initialize`, `tools/list`, `tools/call`. Route tool calls to handlers. All logging to stderr exclusively.

- [ ] **Step 4: Run server tests**

Expected: PASS.

- [ ] **Step 5: Write tool handler tests**

Test each MCP tool handler: `list_agents`, `get_agent`, `stop_agent`, `get_history`, `get_actions`, `ping`. Tests:
- Invalid params → JSON-RPC error code `-32602`
- Agent not found → tool result with `isError: true` and human-readable message
- Internal error → JSON-RPC error code `-32603`
- Tmux unavailable → tool result with `isError: true` explaining tmux is not running
- Pagination params (limit/offset) respected, `total_count` returned
- `stop_agent` tool description includes: "Terminates a running agent process. The agent will lose any unsaved work. Use with caution."

- [ ] **Step 6: Run to verify failure**

```bash
go test ./internal/mcp/ -v -run TestTool
```

- [ ] **Step 7: Implement tools.go**

Tool definitions with JSON Schema inputs matching spec exactly. Handlers call the same API client as the CLI (CLI/MCP parity). Map errors to MCP error format. `stop_agent` description includes safety warning text.

- [ ] **Step 8: Run tool handler tests**

Expected: PASS.

- [ ] **Step 9: Wire into main.go**

Add `mcp` subcommand to `cmd/control/main.go`.

- [ ] **Step 10: Commit**

```bash
git add internal/mcp/ cmd/control/main.go && git commit -m "feat: MCP server with JSON-RPC 2.0 stdio transport"
```

---

### Task 22: TUI

**Files:**
- Create: `internal/tui/app.go`, `internal/tui/app_test.go`, `internal/tui/list.go`, `internal/tui/detail.go`, `internal/tui/history.go`, `internal/tui/styles.go`

- [ ] **Step 1: Add bubbletea dependency**

```bash
go get github.com/charmbracelet/bubbletea github.com/charmbracelet/lipgloss
```

- [ ] **Step 2: Write TUI model tests**

Using bubbletea's `teatest` package, test:
- `TestListViewInit` — model starts in list view
- `TestNavigationKeys` — `j`/`k` move selection, `Enter` switches to detail view, `Esc` returns to list
- `TestQuitKey` — `q` produces `tea.Quit`
- `TestHelpToggle` — `?` toggles help overlay
- `TestHistoryToggle` — `h` switches to history view
- `TestStopConfirmation` — `s` shows confirmation, `y` confirms, `n` cancels
- `TestFilterToggle` — `f` enters filter mode
- `TestTickRefresh` — tick message triggers data refresh

- [ ] **Step 3: Run to verify failure**

```bash
go test ./internal/tui/ -v
```

- [ ] **Step 4: Implement styles.go**

Lipgloss styles for headers, tables, status indicators, help text.

- [ ] **Step 5: Implement list.go**

Agent list view: table of agents, auto-refresh via tick command (2s), navigation (j/k/arrows), enter to select.

- [ ] **Step 6: Implement detail.go**

Agent detail view: full info, recent actions, scrollback summary. Back with Esc.

- [ ] **Step 7: Implement history.go**

History view: past sessions list, navigable.

- [ ] **Step 8: Implement app.go**

Main bubbletea model: view routing (list/detail/history), keybindings, confirmation dialogs. Uses API client for data.

- [ ] **Step 9: Run TUI tests**

```bash
go test ./internal/tui/ -v
```
Expected: PASS.

- [ ] **Step 10: Wire into main.go**

Add `tui` subcommand.

- [ ] **Step 11: Build and smoke test**

```bash
make build && ./control tui
```
Expected: TUI launches (may show "daemon not running" if daemon isn't started).

- [ ] **Step 12: Commit**

```bash
git add internal/tui/ cmd/control/main.go && git commit -m "feat: TUI dashboard with agent list, detail, and history views"
```

---

### Task 23: End-to-End Integration Tests

**Files:**
- Create: `test/e2e_test.go`

- [ ] **Step 1: Write E2E test (daemon + client)**

Start a daemon on a temp socket with a temp DB. If tmux is available (check with `tmux -V`), create a test tmux session with a known pane (e.g., `sleep 3600`). Wait for poller to discover it. Use API client to verify `ListAgents` returns the pane. Test `GetAgent`. Test `StopAgent`. Test that history records the session. Clean up tmux session after.

If tmux is not available (CI), skip the tmux-dependent tests with `t.Skip("tmux not available")` — do NOT substitute a test double. The remaining tests (daemon startup/shutdown, ping, history queries on empty DB) still run.

- [ ] **Step 2: Run E2E test**

```bash
go test -race ./test/ -v -timeout 60s
```
Expected: PASS (tmux tests skipped if tmux unavailable).

- [ ] **Step 3: Write MCP server E2E test**

Pipe JSON-RPC messages to `control mcp` stdin and read responses from stdout. Test:
- `initialize` returns correct server info and protocol version
- `tools/list` returns all 6 tools with schemas
- `list_agents` tool call returns results
- Invalid tool call returns `-32602`

- [ ] **Step 4: Run MCP E2E test**

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add test/ && git commit -m "test: end-to-end integration tests for daemon, CLI, and MCP"
```

---

### Task 24: Final Polish and Build Verification

**Files:**
- Modify: `cmd/control/main.go` (ensure all subcommands wired)

- [ ] **Step 1: Run full test suite with race detector**

```bash
make test
```
Expected: All tests PASS.

- [ ] **Step 2: Run linter**

```bash
make lint
```
Expected: No issues.

- [ ] **Step 3: Build final binary**

```bash
make build
```

- [ ] **Step 4: Verify binary runs**

```bash
./control --help
./control daemon status
./control ls
```

- [ ] **Step 5: Verify CGO-free build**

```bash
CGO_ENABLED=0 go build -o control ./cmd/control/
```
Expected: Builds successfully with no CGO.

- [ ] **Step 6: Verify no `sh -c` patterns in tmux package**

```bash
grep -r 'exec.Command("sh"' internal/tmux/ internal/process/
```
Expected: No matches.

- [ ] **Step 7: Commit**

```bash
git add cmd/control/main.go && git commit -m "chore: final polish and build verification"
```

---

## Backlog

Items identified during expert panel review that are not blocking v1 but should be addressed:

| # | Item | Priority | Source |
|---|------|----------|--------|
| 1 | **Configurable redaction patterns** — allow users to add custom secret patterns via config instead of hardcoding | Medium | Sandwich Person, Security |
| 2 | **exec.Command timeouts** — add context.Context with timeout to all external command calls to prevent hangs | Medium | Sandwich Person |
| 3 | **Intermediate integration tests** — add integration tests between poller + registry + history (not just E2E) | Medium | TDD Expert |
| 4 | **Refactoring pass after Task 18** — clean up interfaces, reduce coupling, consolidate error patterns | Medium | TDD Expert |
| 5 | **Cross-project MCP scoping** — restrict `stop_agent` via MCP to same-project agents | Medium | Security |
| 6 | **capture-pane race condition test** — explicit test for pane disappearing between list and capture | Low | QA Lead |
| 7 | **Duration parsing for --since/--until** — support both ISO8601 and relative durations (`24h`, `7d`) | Low | QA Lead |
| 8 | **Content-Type header verification** — test that all API responses include `application/json` | Low | QA Lead |
| 9 | **Shutdown drain timeout parameter** — make the 5s drain timeout configurable | Low | QA Lead |
| 10 | **CI workflow** — GitHub Actions for build + test + lint | Low | Go Architect |
| 11 | **Error response sanitization test** — verify no stack traces, file paths, or SQLite internals in error messages | Low | Security |
| 12 | **Rate limiting on stop endpoint** — log/cooldown for rapid stop requests | Low | Security |
