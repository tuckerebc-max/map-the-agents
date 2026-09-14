---
access: public
aliases: []
claim_ids:
- clm_06c0c8d808e3415b0079d5265ddab81b741eb2f0db99d365c49e55aec0c1d94f
- clm_0e8e01b736a37147daf48c02dbd9f84b6dbb2d743192fde4f9f674bdc7658823
- clm_12c7b18a122f2b80a8518ffe771b0312576d9877f370f3ae54617b29c10330cd
- clm_54f38b09322b5a051f001d517e9d52f9e6c40a293aca04698fbd9125742bcfbf
- clm_8c22eb9ee4a201647dc88eb2cb86ee050b39f8e4fbe8fa9c3d92b22ad5d2a161
- clm_a1d75f5dc152d0af92a2c04f55654d4279a5d377a96cee4c1b5ec64117f612d9
- clm_c73caeb46327c64d7614220398aff12b28c6b88b7bc05a0d3954334771124eaf
- clm_fccf4c08bf006e90479704661f754874ea704b5f43fb901a69cd238bf991c0bf
maturity: draft
page_id: pg_37147285fcf45f59acbc673270f4376c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8686524fb1765efcb829ba3538313f7b
title: cline/cline/README.md @ c1c0b55ca03a
updated_at: '2026-09-14T01:42:03Z'
---

# cline/cline/README.md @ c1c0b55ca03a

<!-- rcw:begin owner=source:src_8686524fb1765efcb829ba3538313f7b block=evidence -->
- The CLI exposes commands including `cline auth` for sign-in, `cline mcp` for MCP server management, and `cline connect` for messaging integrations such as Telegram and Slack. [@claim:clm_06c0c8d808e3415b0079d5265ddab81b741eb2f0db99d365c49e55aec0c1d94f]
- The SDK (`@cline/sdk`) exposes the agent core programmatically, allowing custom tools via createTool and plugins with lifecycle hooks, and powers the CLI, desktop app, VS Code extension, and JetBrains plugin. [@claim:clm_0e8e01b736a37147daf48c02dbd9f84b6dbb2d743192fde4f9f674bdc7658823]
- Cline supports multiple model providers including Anthropic, OpenAI, Google, OpenRouter (200+ models), AWS Bedrock, Azure/GCP Vertex, Cerebras/Groq, Ollama/LM Studio for local models, and any OpenAI-compatible API. [@claim:clm_12c7b18a122f2b80a8518ffe771b0312576d9877f370f3ae54617b29c10330cd]
- Repository development practice: contributors are directed to start with the Contributing Guide (CONTRIBUTING.md) and join the #contributors Discord channel. [@claim:clm_54f38b09322b5a051f001d517e9d52f9e6c40a293aca04698fbd9125742bcfbf]
- The CLI installs via `npm i -g cline` and supports interactive chat or fully headless mode for CI/CD and scripting, including JSON output and piped input. [@claim:clm_8c22eb9ee4a201647dc88eb2cb86ee050b39f8e4fbe8fa9c3d92b22ad5d2a161]
- The repository ships several products: an SDK, a CLI, a VS Code extension, a native macOS/Windows desktop app (Tauri shell, Bun sidecar, Next.js UI), and docs; the JetBrains plugin is not open-sourced. [@claim:clm_a1d75f5dc152d0af92a2c04f55654d4279a5d377a96cee4c1b5ec64117f612d9]
- Cline offers Plan and Act modes: Plan mode explores the codebase and proposes a strategy, Act mode executes, and every file edit and terminal command requires user approval unless auto-approve is toggled. [@claim:clm_c73caeb46327c64d7614220398aff12b28c6b88b7bc05a0d3954334771124eaf]
- In multi-agent teams, team state persists across sessions so work can be resumed, and scheduled cron agents persist across restarts and run independently of any terminal session. [@claim:clm_fccf4c08bf006e90479704661f754874ea704b5f43fb901a69cd238bf991c0bf]
<!-- rcw:end owner=source:src_8686524fb1765efcb829ba3538313f7b block=evidence -->

## Researcher notes

