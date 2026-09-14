---
access: public
aliases: []
claim_ids:
- clm_0b514cbb947b741ec1c797a425cf3505288d34db966a872ed76c58c3151ad3ae
- clm_0e957804a6fde39af42bbf63f7dc13f496b87342bfb7d049e61f83cdced2bcb8
- clm_15cf1d0db2c4cccc6a46acb0b76d7eea0f05ff41c1f47ce920fe75484f6fe990
- clm_1d9f9ac6866d63bc8298d126deccc1fecaa2ce7c96b9b9f2073635243c8be4b6
- clm_362ac9079c62f9f7df5383f7988b6472e0f438c10aa6f0bfa2870bb41dce21ff
- clm_529591f0951196d4ec30731b943fa0fbfc9915c5fbd0fcaba7ecc87e32c497a3
- clm_670bee5f77ec370c6c4236289435da15ba5154dedf31b53a8195ad5232edaf3c
- clm_69e89c53c4d73c4f32d2e4d9de00c0621bc0ee727d3010877336d69043771a7a
- clm_74bd9c399e6905f97facddea1770f4494115d76e1207fb9a91e0e7a413f7c395
- clm_83f03932f1c26383f2cd62a57e6b019e7a3ba2c6c83f56b1d781a1518a84318e
- clm_a14beaeebf55d3dda63ff2a22a9253c1a555836c3f8768eade844eab6891d946
maturity: draft
page_id: pg_c51bea023aba526bb92607a63e17ec61
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_de05b9dbede4509687b6e48c6e693a78
title: solo-agent/solo/README.md @ 9d58e66769ed
updated_at: '2026-09-14T02:41:12Z'
---

# solo-agent/solo/README.md @ 9d58e66769ed

<!-- rcw:begin owner=source:src_de05b9dbede4509687b6e48c6e693a78 block=evidence -->
- Solo is described as an open-source, local-first workspace for humans and AI coding agents, coordinating multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. [@claim:clm_0b514cbb947b741ec1c797a425cf3505288d34db966a872ed76c58c3151ad3ae]
- Agent team templates let users choose an official workflow or describe a goal to Lucy, preview roles and working relationships, and create agents scoped to one channel with post-creation tuning. [@claim:clm_0e957804a6fde39af42bbf63f7dc13f496b87342bfb7d049e61f83cdced2bcb8]
- Solo runs three local layers: a Go API server on :8080 with WebSocket hub, auth, and PostgreSQL persistence; a daemon on :8081 that registers the machine and manages agent subprocesses; and the installed agent CLI driven over stdin/stdout. [@claim:clm_15cf1d0db2c4cccc6a46acb0b76d7eea0f05ff41c1f47ce920fe75484f6fe990]
- Agent backends are auto-detected from PATH at daemon startup: Claude Code via stream-json, Codex CLI via JSON-RPC, and OpenCode, Hermes, and OpenClaw via ACP. [@claim:clm_1d9f9ac6866d63bc8298d126deccc1fecaa2ce7c96b9b9f2073635243c8be4b6]
- Agents keep agent-specific MEMORY.md context that is loaded into future sessions, and the comparison table says agents retain long-term memory, their own environment, and a fixed workspace. [@claim:clm_362ac9079c62f9f7df5383f7988b6472e0f438c10aa6f0bfa2870bb41dce21ff]
- The runtime topology is Browser (Next.js :3000) to Server (Go :8080) over WebSocket, Server to Daemon over HTTP/SSE, and Daemon to Agent CLI over stdin/stdout. [@claim:clm_529591f0951196d4ec30731b943fa0fbfc9915c5fbd0fcaba7ecc87e32c497a3]
- Solo is intentionally a workspace rather than a company simulator, where agents can be mentioned, assigned, reviewed, remembered, and trusted with visible work. [@claim:clm_670bee5f77ec370c6c4236289435da15ba5154dedf31b53a8195ad5232edaf3c]
- Core concepts include channels, long-lived agents, Kanban tasks with states todo/in_progress/in_review/done/closed, channel-scoped teams, memory, an inbox for mentions and DMs, and reviewable artifacts. [@claim:clm_69e89c53c4d73c4f32d2e4d9de00c0621bc0ee727d3010877336d69043771a7a]
- Running Solo requires Go 1.25+, Node.js 20+, npm, Docker, and at least one supported agent CLI on PATH; README badges also display Go 1.22+ and Node 20+. [@claim:clm_74bd9c399e6905f97facddea1770f4494115d76e1207fb9a91e0e7a413f7c395]
- Each agent can override system_prompt, model_name, custom_env, and custom_args, and agents are described as having roles and tool access. [@claim:clm_83f03932f1c26383f2cd62a57e6b019e7a3ba2c6c83f56b1d781a1518a84318e]
- Repository development practice: `make dev` bootstraps the project by creating .env, installing frontend dependencies, starting PostgreSQL, running migrations, and launching the app, which is then opened at http://localhost:3000. [@claim:clm_a14beaeebf55d3dda63ff2a22a9253c1a555836c3f8768eade844eab6891d946]
<!-- rcw:end owner=source:src_de05b9dbede4509687b6e48c6e693a78 block=evidence -->

## Researcher notes

