---
access: public
aliases: []
claim_ids:
- clm_1b2915ca7f513bb5c07da25cf265a93ad9a4b2ab5f9675ad0eab07dc8c4c5d55
- clm_2607a16fbd2b6bdcbc7671aedbb0a916f93d572735438875cea79b4e78616ef1
- clm_6903522209cb84f5619861bd8e8cf7862cac297085674097993e482b78f616d3
- clm_75bf046c7638b7cf34ed5f7d79e5b33f5afd868ca1d92c96264fe00845082c80
- clm_8ff4f6c20b31733d436aa12c83dc90103433908a649aef0e9ece4cc53bf3d866
- clm_96c3735dbe748530c1d6eff3cad51502356ee5f541fe68705d84f0a6136c4823
- clm_ab618ed4391846bd3f2388ee3744be8b970961ab16d4dbf268663014e9afaf2f
maturity: draft
page_id: pg_9c6e6a16799a5aa980e00aa545a59add
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d3d184409a675ed2aaa998aba60d97b2
title: Choeng-Rayu/rayu-cli/README.md @ c16466f3b068
updated_at: '2026-09-14T01:40:58Z'
---

# Choeng-Rayu/rayu-cli/README.md @ c16466f3b068

<!-- rcw:begin owner=source:src_d3d184409a675ed2aaa998aba60d97b2 block=evidence -->
- The CLI is distributed as the npm package @rayu-dev/rayu-cli, installable globally via npm, runnable via npx, or via curl/PowerShell install scripts that the README says require no Node, npm, or sudo. [@claim:clm_1b2915ca7f513bb5c07da25cf265a93ad9a4b2ab5f9675ad0eab07dc8c4c5d55]
- Repository development practice: contributions are directed to a Contributing Guide covering issues, code formatting, and pull requests, and the project adopts a Contributor Covenant 2.1 code of conduct with a correction/warning/ban enforcement ladder and GitHub-based reporting. [@claim:clm_2607a16fbd2b6bdcbc7671aedbb0a916f93d572735438875cea79b4e78616ef1]
- The README claims a custom React/Ink terminal renderer with zero-GC cell buffers and a Go gateway with sub-millisecond routing overhead, with time-to-first-token under 500ms for cached sessions. [@claim:clm_6903522209cb84f5619861bd8e8cf7862cac297085674097993e482b78f616d3]
- The README lists supported LLM providers including Anthropic, OpenAI, DeepSeek, Google Gemini, Kimi, and locally hosted models via Ollama/LM Studio, connectable via BYOK API keys or a Rayu-hosted connection. [@claim:clm_75bf046c7638b7cf34ed5f7d79e5b33f5afd868ca1d92c96264fe00845082c80]
- The repository is a monorepo of four services plus a deploy stack: a TypeScript/Bun/Ink CLI, a NestJS/Prisma/MySQL accounts API, a Go/chi/Redis AI gateway, and a Next.js 15 website, with Docker Compose + Caddy for deployment. [@claim:clm_8ff4f6c20b31733d436aa12c83dc90103433908a649aef0e9ece4cc53bf3d866]
- The CLI exposes slash commands including /model for mid-session model switching, /connect for provider setup, /sessions and /switch for Telegram bridge sessions, and /banner, /mascot, /brandmark for branding display. [@claim:clm_96c3735dbe748530c1d6eff3cad51502356ee5f541fe68705d84f0a6136c4823]
- The README's performance and competitor-comparison claims (sub-500ms responses, superiority over other CLI agents) appear to be marketing assertions without cited benchmarks in the provided evidence, so they should be treated as unverified. [@claim:clm_ab618ed4391846bd3f2388ee3744be8b970961ab16d4dbf268663014e9afaf2f]
<!-- rcw:end owner=source:src_d3d184409a675ed2aaa998aba60d97b2 block=evidence -->

## Researcher notes

