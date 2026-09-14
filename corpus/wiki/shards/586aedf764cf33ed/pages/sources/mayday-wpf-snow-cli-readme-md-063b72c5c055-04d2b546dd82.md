---
access: public
aliases: []
claim_ids:
- clm_35cfba37f73622135ae6e7fde0ede9d7dade02f39838d8b69a1a3c309a9a1f10
- clm_39d397a37459b4d4c13ec7435c234880113f5df3066204af384673b4d63bec1c
- clm_4d3a07c029465e382278cad08c0bc65ad747cf9053a2336ef9192f4570abfd6b
- clm_6c8de81be64769c55bfa4963963099cc815faad911097084d75a67b86e4353da
- clm_9fab0fdea8402b7da855ddec0821340bcd7264964f11bd86085e3314dff9a79a
- clm_a2ae32f2e35c2fb58f64d7fb3ed86804deacf3c40e56bc5525b5c573c0f707b9
- clm_b1206245df85850980fdc35cbe6f81934221c459a27379794ceb3819f660a43f
- clm_b39d06b41c7f4444d55910eb85e08566674ef242066dfb1499be60248b7e2818
- clm_c8b6a1fce49c37e55ef7ff1a58253e86fe4e93592e6c252887024b28f9d2f424
- clm_f0f20bfcda544932e59786454330b851154384fbef08913dffaf659ace9a5487
maturity: draft
page_id: pg_eb568d7add7250c09f8404d2b546dd82
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2dfd4138119f59a99c24cd9b1aeec3f5
title: MayDay-wpf/snow-cli/README.md @ 063b72c5c055
updated_at: '2026-09-14T02:17:29Z'
---

# MayDay-wpf/snow-cli/README.md @ 063b72c5c055

<!-- rcw:begin owner=source:src_2dfd4138119f59a99c24cd9b1aeec3f5 block=evidence -->
- Running snow creates a `~/.snow/` directory holding logs, configuration profiles, session history, async tasks, hooks, config.json for API settings, and settings.json including mcpServers. [@claim:clm_35cfba37f73622135ae6e7fde0ede9d7dade02f39838d8b69a1a3c309a9a1f10]
- Documentation describes IDE integrations: a VSCode extension (source in VSIX/, published as mufasa.snow-cli) and a JetBrains plugin (source in Jetbrains/), with configurable terminal, bell, git-blame, inline-completion, and next-edit settings. [@claim:clm_39d397a37459b4d4c13ec7435c234880113f5df3066204af384673b4d63bec1c]
- After installation the product is launched with the `snow` command, and installation can be verified with `snow --version` and `snow --help`. [@claim:clm_4d3a07c029465e382278cad08c0bc65ad747cf9053a2336ef9192f4570abfd6b]
- Documented operating modes include headless mode for command-line conversations and script integration, command injection in messages with security mechanisms, a vulnerability hunting mode, and an SSE service mode exposing API endpoints. [@claim:clm_6c8de81be64769c55bfa4963963099cc815faad911097084d75a67b86e4353da]
- A recommended ROLE.md defines the assistant's behavior: plan every step using a Plan Agent, maintain a TODO list via todo-manage (get/add/update/delete), locate files before reading, and record risks with notebook-add. [@claim:clm_9fab0fdea8402b7da855ddec0821340bcd7264964f11bd86085e3314dff9a79a]
- The documented runtime prerequisites are Node.js >= 18.x (ES2020 feature support) and npm >= 8.3.0. [@claim:clm_a2ae32f2e35c2fb58f64d7fb3ed86804deacf3c40e56bc5525b5c573c0f707b9]
- The documented source layout includes agents, LLM API adapters, React hooks for conversation, i18n, MCP, prompt templates, TypeScript types, Ink-based UI components, and utilities under source/. [@claim:clm_b1206245df85850980fdc35cbe6f81934221c459a27379794ceb3819f660a43f]
- Snow CLI is described as an agentic coding tool that runs in the terminal, distributed as the npm package snow-ai. [@claim:clm_b39d06b41c7f4444d55910eb85e08566674ef242066dfb1499be60248b7e2818]
- Feature docs cover sub-agent management and custom agents (including project Markdown agents), hooks for workflow automation, async background task management with sensitive-command approval, and a Team mode for multi-agent collaboration. [@claim:clm_c8b6a1fce49c37e55ef7ff1a58253e86fe4e93592e6c252887024b28f9d2f424]
- Repository development practice: building from source is done by cloning the repo, running npm install, then npm run link to build and globally link the snow command (npm run unlink to remove). [@claim:clm_f0f20bfcda544932e59786454330b851154384fbef08913dffaf659ace9a5487]
<!-- rcw:end owner=source:src_2dfd4138119f59a99c24cd9b1aeec3f5 block=evidence -->

## Researcher notes

