---
access: public
aliases: []
claim_ids:
- clm_0f1b91cc92b93d26e096484baf5445f4dc5bd6b1aebf80fb42557d110037cd1a
- clm_1514bca954507da6077cc47dfe99e0c4746f3602a85cbf7aa8e46ad417177ecf
- clm_29121366b984960178770f2b86797f3182694daa76db2f8371223a4b1998b4fa
- clm_330c7d586383df4b4d3f15f05bb7ed63bc959977788cd8f00361dc0437651d4a
- clm_353d9a7d81fda036d67aa24bbca27f16df3d8c815e80f383cdcc589a5cb11f7e
- clm_3fca21040a10f86abb1ad201431e9a5425c52d01470b0fb53b7b7516b4e47214
- clm_46f587a7b683a4f1df69d9c6499f7610eaf58734ad6090d611497fbaec330ea4
- clm_6524358f8ea020f90c44269c575966149d3434d89aee58b1e6133b3ae65c0c51
- clm_7f1d60229243aa44a3a735bef6e286a2059571f7dd5c510c5a9e8bf18861b637
- clm_80c3f6bbe92b22ca892cc8aa682d73d0d7e22c2e5333ed8efdc9fc95a2b26f91
- clm_990900e6c75a742ff4b2374cdf41f966989cdd96f3cedc57301a713e5a858d37
- clm_c49998f58098f61fcbb321b230105bd82a5b7f69bed7607b0bd060939eff54eb
- clm_dffb020f6f5d6e1f8ada354fc07232594384f67d49a0e9626e78b0713830f1bf
- clm_f68da8f92fe9fcafcc131e07be048059a7e17c7092b7a4adbb49ff6227598d5a
- clm_f841e2cca6472ab1ed2a2f8332dcb4a371dc86a91bb4e88bd3249d259d920201
maturity: draft
page_id: pg_5ac75a1bac185f6eb48230f9486627de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_feb76105800d589e9fbe93288d71fd7f
title: OpenBMB/PilotDeck/README.md @ 97633a08a73e
updated_at: '2026-09-14T02:26:20Z'
---

# OpenBMB/PilotDeck/README.md @ 97633a08a73e

<!-- rcw:begin owner=source:src_feb76105800d589e9fbe93288d71fd7f block=evidence -->
- Repository development practice: contributions follow a fork, feature branch, and pull-request workflow, and bugs or feature requests go through GitHub Issues. [@claim:clm_0f1b91cc92b93d26e096484baf5445f4dc5bd6b1aebf80fb42557d110037cd1a]
- The system natively supports the Model Context Protocol (MCP) and is described as behaving consistently across Web, CLI, and IM front-ends. [@claim:clm_1514bca954507da6077cc47dfe99e0c4746f3602a85cbf7aa8e46ad417177ecf]
- The installer requires Node.js 22.13+ and below v23 for the built-in SQLite runtime, and the Windows installer checks node:sqlite support and uses prebuilt native packages such as node-pty, better-sqlite3, bcrypt, and sharp. [@claim:clm_29121366b984960178770f2b86797f3182694daa76db2f8371223a4b1998b4fa]
- The WorkSpace is the fundamental isolation unit: each project gets its own file system, memory store, and skill set, so parallel work does not interfere and retrieval stays scoped. [@claim:clm_330c7d586383df4b4d3f15f05bb7ed63bc959977788cd8f00361dc0437651d4a]
- PilotDeck is an open-source agent operating system organized around a 'WorkSpace' concept, jointly developed by THUNLP, ModelBest, OpenBMB, and AI9Stars, targeting general-purpose multi-task scenarios. [@claim:clm_353d9a7d81fda036d67aa24bbca27f16df3d8c815e80f383cdcc589a5cb11f7e]
- Smart Routing auto-detects task difficulty and sends complex calls to flagship models while simple tasks go to lighter sub-agent models, aiming to reduce token cost. [@claim:clm_3fca21040a10f86abb1ad201431e9a5425c52d01470b0fb53b7b7516b4e47214]
- The README reports benchmarks: on 7 complex tasks, a Sonnet 4.6 main plus MiniMax-M2.7 sub setup scored 70.6 at $3.15 versus 69.1 at $18.36 for a Sonnet 4.6 single agent, and Smart Routing cut a social-media workload's cost from $12.58 to $2.83. [@claim:clm_46f587a7b683a4f1df69d9c6499f7610eaf58734ad6090d611497fbaec330ea4]
- Configuration is read from ~/.pilotdeck/pilotdeck.yaml; if the file is missing, the Web UI starts without the Gateway, and saving a valid provider and key writes the config and starts the Gateway automatically. [@claim:clm_6524358f8ea020f90c44269c575966149d3434d89aee58b1e6133b3ae65c0c51]
- Repository development practice: source installs use corepack pnpm with a committed pnpm-lock.yaml and workspace filters, and Git LFS demo media is skipped by default for a lightweight clone. [@claim:clm_7f1d60229243aa44a3a735bef6e286a2059571f7dd5c510c5a9e8bf18861b637]
- Memory is white-box and traceable: generation, extraction, storage, and retrieval are visible, entries can be edited or deleted, and a Dream Mode consolidates memory in idle windows with one-click rollback. [@claim:clm_80c3f6bbe92b22ca892cc8aa682d73d0d7e22c2e5333ed8efdc9fc95a2b26f91]
- The system supports always-on background execution: after the user signs off, the agent continues discovering tasks, running long-horizon monitors, and writing deliverables as local files with a summary report. [@claim:clm_990900e6c75a742ff4b2374cdf41f966989cdd96f3cedc57301a713e5a858d37]
- PilotDeck ships a Web UI with WorkSpace management, white-box memory editing, and visualization of multi-agent collaboration; the 'pilotdeck' command starts the server at http://localhost:3001. [@claim:clm_c49998f58098f61fcbb321b230105bd82a5b7f69bed7607b0bd060939eff54eb]
- An open plugin architecture separates the open-source core from plugin customization, supporting MCP servers, custom tools and skills, lifecycle hooks such as PreToolUse and UserPromptSubmit, and pluggable memory store providers. [@claim:clm_dffb020f6f5d6e1f8ada354fc07232594384f67d49a0e9626e78b0713830f1bf]
- The project is licensed under the GNU Affero General Public License v3.0. [@claim:clm_f68da8f92fe9fcafcc131e07be048059a7e17c7092b7a4adbb49ff6227598d5a]
- Supported model provider protocols include OpenAI, Anthropic, native Google Gemini, DeepSeek, Qwen, Kimi, MiniMax, and other OpenAI-compatible endpoints, including local Ollama without an API key. [@claim:clm_f841e2cca6472ab1ed2a2f8332dcb4a371dc86a91bb4e88bd3249d259d920201]
<!-- rcw:end owner=source:src_feb76105800d589e9fbe93288d71fd7f block=evidence -->

## Researcher notes

