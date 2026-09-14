---
access: public
aliases: []
claim_ids:
- clm_08fb405b72b2c0bb16a3104a6e87a82a3a492af034239a62dfddca91a2d4ebba
- clm_0acec8cdfb88ff976cc741d744f39dba0536401929f99dd575c56dfe8042c604
- clm_1dfbfe277a7c842f13110017175d273c64fe52071a8f9a42946d4a6a39c6e9cb
- clm_2acbee0e8a939871a5c82c573cfeab37ea6a3aa1331b464966774c28c80ad3eb
- clm_35d36aec574f8d37576229b63f62e777349d4ae371fb4c05366f06739cc1aabd
- clm_3e8ff4c49e097a084ac2dd6c255fdebdac747699473276d5520e622be0657cf8
- clm_4a1120b3227eba79da191c605a69e8f2f334eb309fd540e8d64e98c65a5329b2
- clm_5671a3f6ef07539da294b8bf459da43366c346462e0b584465486c03275d2679
- clm_9ff72cbbd858ddf1a4252b7188d80a8108325f7741d8a8928bbd7bbba5615ad5
- clm_c77b49d113a6933f2730bc3722886aec4c4fa81fea79a2bc3125442267fa16e6
- clm_f3bc6146ff4637351677567c2cf95d90e80fe989ee9cdcba1f2635bab51e3d11
- clm_f5df732c136864cdf27d5792aff39630d5e6a1ba46458ccf8b5900c872f874cd
maturity: draft
page_id: pg_938a972e6e0e507dbdaf53cdb3571d23
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ff1230f396fb5ef7b368701f32d18a85
title: Mng-dev-ai/agentrove/README.md @ 53ef8fc0dea3
updated_at: '2026-09-14T02:20:04Z'
---

# Mng-dev-ai/agentrove/README.md @ 53ef8fc0dea3

<!-- rcw:begin owner=source:src_ff1230f396fb5ef7b368701f32d18a85 block=evidence -->
- The stack is React 19, TypeScript, Vite, Tailwind, Monaco, and xterm.js on the frontend; FastAPI, SQLAlchemy, SQLite, and Redis on the backend; ACP with Docker or host sandboxes at runtime. [@claim:clm_08fb405b72b2c0bb16a3104a6e87a82a3a492af034239a62dfddca91a2d4ebba]
- Ships as a Docker web app, a macOS desktop app built with Tauri (bundled Python backend sidecar on a local port), and a native iOS thin client that talks to an already-hosted instance over https/wss. [@claim:clm_0acec8cdfb88ff976cc741d744f39dba0536401929f99dd575c56dfe8042c604]
- Orchestrated turns run in the agent's full-execution mode, so workers finish without permission prompts. [@claim:clm_1dfbfe277a7c842f13110017175d273c64fe52071a8f9a42946d4a6a39c6e9cb]
- Sub-threads created via send_message(parent_chat_id=...) are worker chats grouped under the lead in the same workspace and branch, and stay flat with no nesting. [@claim:clm_2acbee0e8a939871a5c82c573cfeab37ea6a3aa1331b464966774c28c80ad3eb]
- The workspace combines chat, code editor, terminal, file tree, diffs, secrets, and git tools, and streams agent sessions with cancellation, permission prompts, queued follow-ups, file mentions, slash commands, and attachments. [@claim:clm_35d36aec574f8d37576229b63f62e777349d4ae371fb4c05366f06739cc1aabd]
- Agents are run through ACP adapters, and each workspace gets its own Docker or host sandbox. [@claim:clm_3e8ff4c49e097a084ac2dd6c255fdebdac747699473276d5520e622be0657cf8]
- Workers can run on any installed agent, model, and persona; worktree=true gives a worker its own git worktree so parallel workers edit concurrently without conflicts. [@claim:clm_4a1120b3227eba79da191c605a69e8f2f334eb309fd540e8d64e98c65a5329b2]
- Repository development practice: building the iOS app from source requires macOS with Xcode, Rust iOS targets via rustup, and CocoaPods; a helper script (npm run ios:install) builds, signs, exports, and installs using APPLE_DEVELOPMENT_TEAM. [@claim:clm_5671a3f6ef07539da294b8bf459da43366c346462e0b584465486c03275d2679]
- Agentrove is a self-hosted AI coding workspace that runs and orchestrates Antigravity, Claude Code, Codex, Copilot, Cursor, Grok, and OpenCode agents from one interface. [@claim:clm_9ff72cbbd858ddf1a4252b7188d80a8108325f7741d8a8928bbd7bbba5615ad5]
- The lead polls get_messages until a worker's turn completes, judges results against the code, and sends rework to the worker's thread; follow-ups inherit prior model, persona, and reasoning settings. [@claim:clm_c77b49d113a6933f2730bc3722886aec4c4fa81fea79a2bc3125442267fa16e6]
- A bundled MCP server exposes the instance as tools such as send_message, get_messages, list_models, and list_personas, letting any chat's agent act as an orchestrator that decomposes work and reviews results. [@claim:clm_f3bc6146ff4637351677567c2cf95d90e80fe989ee9cdcba1f2635bab51e3d11]
- Quick start requires Docker and Docker Compose, cloning the repo, copying .env.example to .env, and setting SECRET_KEY before docker compose up -d; the app is served at localhost:3000. [@claim:clm_f5df732c136864cdf27d5792aff39630d5e6a1ba46458ccf8b5900c872f874cd]
<!-- rcw:end owner=source:src_ff1230f396fb5ef7b368701f32d18a85 block=evidence -->

## Researcher notes

