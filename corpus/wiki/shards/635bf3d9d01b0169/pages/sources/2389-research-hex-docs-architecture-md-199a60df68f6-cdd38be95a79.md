---
access: public
aliases: []
claim_ids:
- clm_511356ffcc4b89c737077bcdfccfd5037b093cdb999c68b093d09fcc84c3cc65
- clm_6b13bdb3ed4a3af9da7c5ab5f17f713f2fa8c0dc55fff2e72c149c9d722052e9
- clm_8429bb805ee79bfe1985b9ccaa58782a09902fd6f844d4144d35d3920d467e2c
- clm_908a6d1bc938d7c975a4c56895954e886984af121547d45510ff0956c67e58b8
- clm_a74bef5b7f779018d63c022a590307ab8bc2be926572815406f10b5e27fa60d1
maturity: draft
page_id: pg_163dcdc2728d5b418a47cdd38be95a79
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9ac10410c80a53a49ace2b06c6fb05fa
title: 2389-research/hex/docs/ARCHITECTURE.md @ 199a60df68f6
updated_at: '2026-09-14T01:58:48Z'
---

# 2389-research/hex/docs/ARCHITECTURE.md @ 199a60df68f6

<!-- rcw:begin owner=source:src_9ac10410c80a53a49ace2b06c6fb05fa block=evidence -->
- The CLI includes setup and doctor subcommands for configuring the API key and checking configuration health, plus an mcp subcommand (e.g. hex mcp add, hex mcp list) for managing MCP servers. [@claim:clm_511356ffcc4b89c737077bcdfccfd5037b093cdb999c68b093d09fcc84c3cc65]
- Hex offers three modes: non-interactive print mode (e.g. hex --print with optional JSON output), an interactive TUI launched by running hex, and resume via --continue or --resume <id>. [@claim:clm_6b13bdb3ed4a3af9da7c5ab5f17f713f2fa8c0dc55fff2e72c149c9d722052e9]
- The codebase is organized into cmd/hex (CLI entry and mode routing), internal/core (Anthropic HTTP client, SSE streaming, types, config), internal/ui (Bubbletea TUI), internal/storage (SQLite persistence), and internal/tools (tool registry and executor). [@claim:clm_8429bb805ee79bfe1985b9ccaa58782a09902fd6f844d4144d35d3920d467e2c]
- Conversations persist in SQLite at ~/.hex/hex.db using a hybrid schema (normalized conversations/messages tables plus JSON columns for tool_calls and metadata), with WAL mode, foreign keys, embedded migrations, and resume support. [@claim:clm_908a6d1bc938d7c975a4c56895954e886984af121547d45510ff0956c67e58b8]
- The tool system uses a registry plus executor pattern; tools implement a Go interface with Name, Description, Execute, and RequiresApproval methods, and the executor handles approval callbacks and parameter validation. [@claim:clm_a74bef5b7f779018d63c022a590307ab8bc2be926572815406f10b5e27fa60d1]
<!-- rcw:end owner=source:src_9ac10410c80a53a49ace2b06c6fb05fa block=evidence -->

## Researcher notes

