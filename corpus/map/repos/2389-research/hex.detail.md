# 2389-research/hex -- full detail

[Back to orientation](hex.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/hex/199a60df68f688512a5bc10b1f5376afae89894a/661da7e02f8d3220.json](../../../wiki/dossiers/2389-research/hex/199a60df68f688512a5bc10b1f5376afae89894a/661da7e02f8d3220.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The codebase is organized into cmd/hex (CLI entry and mode routing), internal/core (Anthropic HTTP client, SSE streaming, types, config), internal/ui (Bubbletea TUI), internal/storage (SQLite persistence), and internal/tools (tool registry and executor). -- evidence: [docs/ARCHITECTURE.md#L150-L150](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L150-L150), [docs/ARCHITECTURE.md#L237-L237](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L237-L237), [README.md#L413-L423](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L413-L423), [docs/ARCHITECTURE.md#L180-L180](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L180-L180), [docs/ARCHITECTURE.md#L203-L203](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L203-L203), [docs/ARCHITECTURE.md#L142-L146](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L142-L146), [docs/ARCHITECTURE.md#L70-L127](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L70-L127) (`clm_8429bb805ee79bfe1985b9ccaa58782a09902fd6f844d4144d35d3920d467e2c`)
- [observation/documented] The tool system uses a registry plus executor pattern; tools implement a Go interface with Name, Description, Execute, and RequiresApproval methods, and the executor handles approval callbacks and parameter validation. -- evidence: [docs/ARCHITECTURE.md#L224-L228](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L224-L228), [docs/ARCHITECTURE.md#L209-L217](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L209-L217), [docs/ARCHITECTURE.md#L205-L205](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L205-L205) (`clm_a74bef5b7f779018d63c022a590307ab8bc2be926572815406f10b5e27fa60d1`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors install pre-commit hooks (go fmt, go vet, goimports, go test with 60s timeout, go mod tidy, golangci-lint) that run on git commit, build with make build, and run tests via make test or go test ./... with coverage. -- evidence: [README.md#L386-L386](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L386-L386), [README.md#L381-L382](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L381-L382), [README.md#L375-L375](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L375-L375), [README.md#L388-L395](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L388-L395), [README.md#L355-L355](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L355-L355), [README.md#L378-L378](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L378-L378), [README.md#L365-L365](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L365-L365) (`clm_134bac3cafc2ce75a0c781795a0d9ddb07c388443fc7fb0870752247e062ec10`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Hex offers three modes: non-interactive print mode (e.g. hex --print with optional JSON output), an interactive TUI launched by running hex, and resume via --continue or --resume <id>. -- evidence: [README.md#L134-L135](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L134-L135), [README.md#L113-L114](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L113-L114), [README.md#L122-L122](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L122-L122), [README.md#L125-L126](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L125-L126), [docs/ARCHITECTURE.md#L21-L23](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L21-L23), [README.md#L12-L12](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L12-L12), [README.md#L131-L131](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L131-L131) (`clm_6b13bdb3ed4a3af9da7c5ab5f17f713f2fa8c0dc55fff2e72c149c9d722052e9`)
- [observation/documented] The CLI includes setup and doctor subcommands for configuring the API key and checking configuration health, plus an mcp subcommand (e.g. hex mcp add, hex mcp list) for managing MCP servers. -- evidence: [README.md#L276-L276](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L276-L276), [README.md#L108-L109](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L108-L109), [README.md#L105-L105](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L105-L105), [docs/ARCHITECTURE.md#L135-L140](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L135-L140), [README.md#L273-L273](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L273-L273) (`clm_511356ffcc4b89c737077bcdfccfd5037b093cdb999c68b093d09fcc84c3cc65`)
- [observation/documented] The interactive TUI supports keyboard shortcuts including Enter to send, Alt+Enter for newline, j/k scrolling, gg/G jumps, / search, and Ctrl+C to quit, with vim-style navigation and streaming markdown rendering via Glamour. -- evidence: [README.md#L149-L154](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L149-L154), [README.md#L190-L197](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L190-L197) (`clm_5a24f2ec72262ac73aaa8e0e7696cabd63150be9401d2668139dc82caf314416`)
- [observation/documented] Hex integrates the Model Context Protocol so external MCP servers' tools become available in conversations, with documented official servers for filesystem, fetch, SQLite, and PostgreSQL, and support for custom servers in any language. -- evidence: [README.md#L283-L287](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L283-L287), [README.md#L273-L273](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L273-L273), [README.md#L269-L269](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L269-L269), [README.md#L289-L289](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L289-L289), [README.md#L279-L281](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L279-L281) (`clm_e267a5fe96ea9f28f9f49f6ef5d7de54fef9401348e8fc2cd8236baa498f52f3`)

## memory-state (1 claim(s))

- [observation/documented] Conversations persist in SQLite at ~/.hex/hex.db using a hybrid schema (normalized conversations/messages tables plus JSON columns for tool_calls and metadata), with WAL mode, foreign keys, embedded migrations, and resume support. -- evidence: [docs/ARCHITECTURE.md#L182-L182](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L182-L182), [docs/ARCHITECTURE.md#L398-L406](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L398-L406), [README.md#L156-L160](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L156-L160), [docs/ARCHITECTURE.md#L387-L396](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L387-L396), [docs/ARCHITECTURE.md#L385-L385](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L385-L385), [docs/ARCHITECTURE.md#L186-L189](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L186-L189), [docs/ARCHITECTURE.md#L408-L409](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/docs/ARCHITECTURE.md#L408-L409) (`clm_908a6d1bc938d7c975a4c56895954e886984af121547d45510ff0956c67e58b8`)

## orchestration (1 claim(s))

- [observation/documented] The Task tool launches sub-agents for complex tasks, and the README describes multi-agent capabilities including event-sourced audit trails, per-agent cost tracking, tree/timeline visualization with HTML export, and graceful cascading shutdown. -- evidence: [README.md#L174-L179](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L174-L179), [README.md#L162-L166](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L162-L166) (`clm_aa6b790c440b46acfe86d5df09412224712a4471268b824a430ec0ae2966f6c9`)

## tools-permissions (1 claim(s))

- [observation/documented] Tool execution requires user approval through an interactive prompt (Approve? y/N); safety features include sensitive-path detection for Read, overwrite confirmation for Write, Bash timeout limits and dangerous-command detection, with approval always required for dangerous operations. -- evidence: [README.md#L250-L256](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L250-L256), [README.md#L201-L211](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L201-L211), [README.md#L213-L213](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L213-L213), [README.md#L457-L461](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L457-L461) (`clm_4f6c8e22b7264e54edb80c059ccc38871c1a24134962854b49c184de7fd8e14d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Hex is built with Go 1.24+ (v1.0 requires Go 1.24.1+ per a security audit note) and uses Bubbletea, Lipgloss, Glamour, Cobra, Viper, and the pure-Go modernc.org/sqlite driver. -- evidence: [README.md#L72-L72](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L72-L72), [README.md#L531-L537](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L531-L537), [README.md#L465-L467](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L465-L467), [README.md#L184-L184](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L184-L184), [README.md#L438-L442](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L438-L442) (`clm_dd4f3d546ba9d6d7192d248bf77e8b5ddfc5087723524513b79793e20f372d19`)
- [observation/documented] Hex requires an Anthropic API key, configurable via a TOML config file, environment variables (ANTHROPIC_API_KEY, HEX_MODEL), or a project .env file; the default model shown is claude-sonnet-4-5-20250929. -- evidence: [README.md#L225-L228](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L225-L228), [README.md#L230-L232](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L230-L232), [README.md#L234-L238](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L234-L238), [README.md#L465-L467](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L465-L467), [README.md#L240-L244](https://github.com/2389-research/hex/blob/199a60df68f688512a5bc10b1f5376afae89894a/README.md#L240-L244) (`clm_854631eb1412cb90ec38e5805e896247be78063b20cd97d958ee4fa9e6f9a20d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

