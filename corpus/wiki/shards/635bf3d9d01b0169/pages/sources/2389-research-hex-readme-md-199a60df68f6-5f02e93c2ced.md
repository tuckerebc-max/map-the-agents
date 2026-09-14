---
access: public
aliases: []
claim_ids:
- clm_134bac3cafc2ce75a0c781795a0d9ddb07c388443fc7fb0870752247e062ec10
- clm_4f6c8e22b7264e54edb80c059ccc38871c1a24134962854b49c184de7fd8e14d
- clm_511356ffcc4b89c737077bcdfccfd5037b093cdb999c68b093d09fcc84c3cc65
- clm_5a24f2ec72262ac73aaa8e0e7696cabd63150be9401d2668139dc82caf314416
- clm_6b13bdb3ed4a3af9da7c5ab5f17f713f2fa8c0dc55fff2e72c149c9d722052e9
- clm_8429bb805ee79bfe1985b9ccaa58782a09902fd6f844d4144d35d3920d467e2c
- clm_854631eb1412cb90ec38e5805e896247be78063b20cd97d958ee4fa9e6f9a20d
- clm_908a6d1bc938d7c975a4c56895954e886984af121547d45510ff0956c67e58b8
- clm_aa6b790c440b46acfe86d5df09412224712a4471268b824a430ec0ae2966f6c9
- clm_dd4f3d546ba9d6d7192d248bf77e8b5ddfc5087723524513b79793e20f372d19
- clm_e267a5fe96ea9f28f9f49f6ef5d7de54fef9401348e8fc2cd8236baa498f52f3
maturity: draft
page_id: pg_8fdd6639e3b257b3a1405f02e93c2ced
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_97522521a9aa5f019bd5a09763ae8a2b
title: 2389-research/hex/README.md @ 199a60df68f6
updated_at: '2026-09-14T01:58:48Z'
---

# 2389-research/hex/README.md @ 199a60df68f6

<!-- rcw:begin owner=source:src_97522521a9aa5f019bd5a09763ae8a2b block=evidence -->
- Repository development practice: contributors install pre-commit hooks (go fmt, go vet, goimports, go test with 60s timeout, go mod tidy, golangci-lint) that run on git commit, build with make build, and run tests via make test or go test ./... with coverage. [@claim:clm_134bac3cafc2ce75a0c781795a0d9ddb07c388443fc7fb0870752247e062ec10]
- Tool execution requires user approval through an interactive prompt (Approve? y/N); safety features include sensitive-path detection for Read, overwrite confirmation for Write, Bash timeout limits and dangerous-command detection, with approval always required for dangerous operations. [@claim:clm_4f6c8e22b7264e54edb80c059ccc38871c1a24134962854b49c184de7fd8e14d]
- The CLI includes setup and doctor subcommands for configuring the API key and checking configuration health, plus an mcp subcommand (e.g. hex mcp add, hex mcp list) for managing MCP servers. [@claim:clm_511356ffcc4b89c737077bcdfccfd5037b093cdb999c68b093d09fcc84c3cc65]
- The interactive TUI supports keyboard shortcuts including Enter to send, Alt+Enter for newline, j/k scrolling, gg/G jumps, / search, and Ctrl+C to quit, with vim-style navigation and streaming markdown rendering via Glamour. [@claim:clm_5a24f2ec72262ac73aaa8e0e7696cabd63150be9401d2668139dc82caf314416]
- Hex offers three modes: non-interactive print mode (e.g. hex --print with optional JSON output), an interactive TUI launched by running hex, and resume via --continue or --resume <id>. [@claim:clm_6b13bdb3ed4a3af9da7c5ab5f17f713f2fa8c0dc55fff2e72c149c9d722052e9]
- The codebase is organized into cmd/hex (CLI entry and mode routing), internal/core (Anthropic HTTP client, SSE streaming, types, config), internal/ui (Bubbletea TUI), internal/storage (SQLite persistence), and internal/tools (tool registry and executor). [@claim:clm_8429bb805ee79bfe1985b9ccaa58782a09902fd6f844d4144d35d3920d467e2c]
- Hex requires an Anthropic API key, configurable via a TOML config file, environment variables (ANTHROPIC_API_KEY, HEX_MODEL), or a project .env file; the default model shown is claude-sonnet-4-5-20250929. [@claim:clm_854631eb1412cb90ec38e5805e896247be78063b20cd97d958ee4fa9e6f9a20d]
- Conversations persist in SQLite at ~/.hex/hex.db using a hybrid schema (normalized conversations/messages tables plus JSON columns for tool_calls and metadata), with WAL mode, foreign keys, embedded migrations, and resume support. [@claim:clm_908a6d1bc938d7c975a4c56895954e886984af121547d45510ff0956c67e58b8]
- The Task tool launches sub-agents for complex tasks, and the README describes multi-agent capabilities including event-sourced audit trails, per-agent cost tracking, tree/timeline visualization with HTML export, and graceful cascading shutdown. [@claim:clm_aa6b790c440b46acfe86d5df09412224712a4471268b824a430ec0ae2966f6c9]
- Hex is built with Go 1.24+ (v1.0 requires Go 1.24.1+ per a security audit note) and uses Bubbletea, Lipgloss, Glamour, Cobra, Viper, and the pure-Go modernc.org/sqlite driver. [@claim:clm_dd4f3d546ba9d6d7192d248bf77e8b5ddfc5087723524513b79793e20f372d19]
- Hex integrates the Model Context Protocol so external MCP servers' tools become available in conversations, with documented official servers for filesystem, fetch, SQLite, and PostgreSQL, and support for custom servers in any language. [@claim:clm_e267a5fe96ea9f28f9f49f6ef5d7de54fef9401348e8fc2cd8236baa498f52f3]
<!-- rcw:end owner=source:src_97522521a9aa5f019bd5a09763ae8a2b block=evidence -->

## Researcher notes

