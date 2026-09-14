---
access: public
aliases: []
claim_ids:
- clm_439e3f633817c52838301cc383057e473323fb20160a465d960e6f70c5c6e847
- clm_75dce6abfbee0b1567e3e9b0878d6a67b1c79b2eaff5cd7e63a1d58eed0d5b00
- clm_8d87254c007a6e75368aaa368883bf6a3ca167f742d6647f8238b3fda772ca95
- clm_99b8774410b3ce7a4897fd45e8ce97d46db2396597f4a7f597f86c7584f53418
- clm_bcc2ac089106d922c486721aee7f7b144af0ddcbbcc82de5e85a74214e3c3bea
- clm_c080489a54e4ad673de5a8c7c7a47688a9842147cdaa4e02b886b266ce075fca
- clm_d988da27935246e353da36ed956c4f392fe0a98a543ba4dda8cf14794b64718d
maturity: draft
page_id: pg_7b750c21b1795e9684093e64045176e3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_20ff18a02775564699c724d18b72dd0b
title: codeany-ai/codeany/CODEANY.md @ 7e614dc436ef
updated_at: '2026-09-14T01:41:43Z'
---

# codeany-ai/codeany/CODEANY.md @ 7e614dc436ef

<!-- rcw:begin owner=source:src_20ff18a02775564699c724d18b72dd0b block=evidence -->
- The agent maintains memory files under ~/.codeany/memory/ (MEMORY.md plus files per the architecture doc), session history with save/restore/resume, and per-session context such as files accessed. [@claim:clm_439e3f633817c52838301cc383057e473323fb20160a465d960e6f70c5c6e847]
- The project appears positioned as a feature-parity, fully open-source alternative to Claude Code, and even instructs contributors to compare against the original TypeScript codebase when adding features. [@claim:clm_75dce6abfbee0b1567e3e9b0878d6a67b1c79b2eaff5cd7e63a1d58eed0d5b00]
- The internal package layout includes modules for config, permissions, memory, pipe mode, plugins, sessions, skills, slash command registry, team/mailbox, theme, TUI model/input/render, version, and git worktree isolation. [@claim:clm_8d87254c007a6e75368aaa368883bf6a3ca167f742d6647f8238b3fda772ca95]
- Repository development practice: slash commands must be registered in both AllCommands() for autocomplete and Handle() for routing, and go.work links the SDK locally while go.mod uses the published version for CI. [@claim:clm_99b8774410b3ce7a4897fd45e8ce97d46db2396597f4a7f597f86c7584f53418]
- The agent depends on the open-agent-sdk-go SDK, which provides the agent loop, tools, MCP, permissions, hooks, and cost tracking; Codeany itself adds TUI, slash commands, skills, plugins, teams, sessions, and config management. [@claim:clm_bcc2ac089106d922c486721aee7f7b144af0ddcbbcc82de5e85a74214e3c3bea]
- Configuration lives in ~/.codeany/ with settings.json (model, permissions, MCP, hooks), an alternative config.yaml, persisted permissions.json, and directories for memory, sessions, skills, plugins, teams, and worktrees. [@claim:clm_c080489a54e4ad673de5a8c7c7a47688a9842147cdaa4e02b886b266ce075fca]
- Repository development practice: contributors build with `make build` or `go build -o codeany ./cmd/codeany/`, run `make vet`, cross-compile six platforms with `make dist`, and test pipe mode via `go run ./cmd/codeany -p -y`. [@claim:clm_d988da27935246e353da36ed956c4f392fe0a98a543ba4dda8cf14794b64718d]
<!-- rcw:end owner=source:src_20ff18a02775564699c724d18b72dd0b block=evidence -->

## Researcher notes

