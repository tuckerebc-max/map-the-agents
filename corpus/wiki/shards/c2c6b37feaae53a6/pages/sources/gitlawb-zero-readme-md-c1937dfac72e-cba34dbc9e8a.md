---
access: public
aliases: []
claim_ids:
- clm_02c62d4f688ecacca51411d6d6db52a725cccb6ca7e481e6ec3685635002e0d6
- clm_10ed2f3e26d51de4425a28e2af3c51fd2e10b38add9789743453dfae49d8626d
- clm_712430ddb125e2a28484c82e3f0433453faf89a92bed2c23707740346881290b
- clm_828e8c09a9d90a9c1bca579083ea62cd2d9833b9e62d72fceef5c78ff171cde7
- clm_891667e23e4716c22321a12e81412174f563cdce620f4a1ab44ad5e82eb84be6
- clm_af54df982615470ed9e6d69901214f47499068ba70ba88f8143e723ff2d9820b
- clm_b61168c694f9e71d8e64101868100f7b30014338aa75fcfd2c45932fce325417
- clm_be3324d5b9714a8e8ac2988c8b8dc6401a06e22005e5c6e9fd3d738342265382
- clm_bf9422ff6f5187c65d75864d5bb375bb320aa191b8f8f5d42943b9b87f37e918
- clm_df0ee0062fb01b6d5e391e268332a07f7a0b77642d06f84a219094f0aaa580b4
- clm_e5f097d92e89db263ed3e2bf39d4f6e2f38ee9afe3f946be285d50a102d8df39
- clm_ed4a89d9f2ffe489479c2ea7ba4637812d6eaca841b5a274cc9232478023fd5e
- clm_f937581a41e9eb47c8de8c28b35dfff381421fc8c6943ce9e2ba755a1aa382a9
maturity: draft
page_id: pg_0c51f81085b65b51aa1ccba34dbc9e8a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ae6d5e8ed8b0548596abde224658e4fd
title: Gitlawb/zero/README.md @ c1937dfac72e
updated_at: '2026-09-14T01:52:26Z'
---

# Gitlawb/zero/README.md @ c1937dfac72e

<!-- rcw:begin owner=source:src_ae6d5e8ed8b0548596abde224658e4fd block=evidence -->
- The TUI supports slash commands such as /model, /spec, /image, /resume, /rewind, /btw, /loop, /compact, /permissions, /add-dir, and /theme, plus Shift+Tab to cycle permission modes. [@claim:clm_02c62d4f688ecacca51411d6d6db52a725cccb6ca7e481e6ec3685635002e0d6]
- Source builds require Go 1.26.6+; the npm wrapper ships platform builds for Linux and macOS on x64/arm64 and Windows on x64 as an optional npm dependency. [@claim:clm_10ed2f3e26d51de4425a28e2af3c51fd2e10b38add9789743453dfae49d8626d]
- Workspace reads are allowed by default; file writes are limited to the workspace unless extra write roots are granted via --add-dir or /add-dir, and shell, network, destructive, and elevated actions are permission-gated. [@claim:clm_712430ddb125e2a28484c82e3f0433453faf89a92bed2c23707740346881290b]
- Zero supports many providers including OpenAI, Anthropic, Gemini, Groq, OpenRouter, DeepSeek, Mistral, xAI, Qwen, Kimi, Ollama, LM Studio, and any OpenAI- or Anthropic-compatible endpoint. [@claim:clm_828e8c09a9d90a9c1bca579083ea62cd2d9833b9e62d72fceef5c78ff171cde7]
- When HTTP_PROXY/HTTPS_PROXY is set, web_fetch's local address checks can be bypassed because the proxy decides the actual destination; leaving the variables unset keeps the checks enforced end to end. [@claim:clm_891667e23e4716c22321a12e81412174f563cdce620f4a1ab44ad5e82eb84be6]
- The CLI exposes subcommands including setup, providers, models, doctor, sessions, spec, skills, plugins, hooks, mcp, sandbox, worktrees, verify, usage, cron, and `serve --mcp` to expose Zero tools over MCP stdio. [@claim:clm_af54df982615470ed9e6d69901214f47499068ba70ba88f8143e723ff2d9820b]
- Zero offers an interactive TUI plus a scriptable headless mode (`zero exec`) supporting text, JSON, and stream-JSON I/O with meaningful exit codes for CI. [@claim:clm_b61168c694f9e71d8e64101868100f7b30014338aa75fcfd2c45932fce325417]
- The web_fetch tool refuses loopback, private, and special-use addresses by checking the URL, resolving the host, and dialing the validated address to prevent DNS rebinding. [@claim:clm_be3324d5b9714a8e8ac2988c8b8dc6401a06e22005e5c6e9fd3d738342265382]
- Sandbox policy and grants can be inspected at runtime with `zero sandbox policy` and `zero sandbox grants list`; Linux source builds can include a native sandbox helper binary. [@claim:clm_bf9422ff6f5187c65d75864d5bb375bb320aa191b8f8f5d42943b9b87f37e918]
- Repository development practice: contributors should run `make fmt`, `make vet`, `make lint-static`, and `make vulncheck` before committing, using repository-managed targets with pinned tool versions rather than globally installed binaries. [@claim:clm_df0ee0062fb01b6d5e391e268332a07f7a0b77642d06f84a219094f0aaa580b4]
- Sessions are stored on disk locally, searchable, resumable, and forkable, and the README states they are never uploaded as telemetry by Zero. [@claim:clm_e5f097d92e89db263ed3e2bf39d4f6e2f38ee9afe3f946be285d50a102d8df39]
- Zero injects project guidance into the system prompt from the first AGENTS.md, ZERO.md, or .zero/AGENTS.md found per directory from the git root to the cwd, capped at 8 KiB per file and 32 KiB total. [@claim:clm_ed4a89d9f2ffe489479c2ea7ba4637812d6eaca841b5a274cc9232478023fd5e]
- Repository development practice: contributors run `go test ./...`, and the internal/agenteval tests validate every suite JSON file, rejecting missing task IDs, empty verification commands, and malformed changed-file expectations. [@claim:clm_f937581a41e9eb47c8de8c28b35dfff381421fc8c6943ce9e2ba755a1aa382a9]
<!-- rcw:end owner=source:src_ae6d5e8ed8b0548596abde224658e4fd block=evidence -->

## Researcher notes

