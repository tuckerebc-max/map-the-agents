---
access: public
aliases: []
claim_ids:
- clm_14571f2290ebc55febcdc46a4bb40def3470ac79f66868295bcfdf15fabd0cea
- clm_48f3414a230ea43a10887f6e6861efe1e4ff8fdc5440503271c72e6c675b624e
- clm_65cf00780d4f07718226eae1a26da217219985d373045518e0de39091763f1bf
- clm_68821c5d4852b33fa4210e587093a776a5c9101453878e18dd635fc0b9b51fe2
- clm_94e66f6e6fbbcc586ddf284bd30d34f4d63364bfb126e87fff2ad7c1969488bb
- clm_acb94360ef1f441b69bdbf73cde7c4ebbf6115edd3baa81bf45f616540ba7c18
- clm_c006d9232cba52d1aab4fd8e674d1604ad01321cb285cdcd3dc55e167d210632
- clm_d0ff5ac873f6207e95b546debce6147a2628a3f10d622477772e2d4c2f22ce7f
- clm_d1d0bd3ef3c5bea3aa82d4ec6a60e604b755d58608782991a4227bf843176e33
- clm_d4f2c143576f72c17b29e346fd4affe3de9c10d38f31e299eb333f8a0697fd79
- clm_e7384455ef5657337aee8f18de3759367f7cdbe54b5f004d55836bbb51d187c4
- clm_fed551d34d91f84d971dd2a7474833e2a48bc6a5fa7203a9e8cd9a5daed43c3e
maturity: draft
page_id: pg_e89ad3c1e1bb5335801bbce094ac777b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_acb354116db656d79018bb0a218f23d6
title: chaitanyagiri/munder-difflin/README.md @ 417d8decf08c
updated_at: '2026-09-14T02:00:05Z'
---

# chaitanyagiri/munder-difflin/README.md @ 417d8decf08c

<!-- rcw:begin owner=source:src_acb354116db656d79018bb0a218f23d6 block=evidence -->
- Repository development practice: every pull request must include before/after evidence under the PR template's '### Before' and '### After' headings, enforced by an automated 'PR evidence' check; PRs failing it do not merge, with only a maintainer-applied no-visual-change label as exemption. [@claim:clm_14571f2290ebc55febcdc46a4bb40def3470ac79f66868295bcfdf15fabd0cea]
- Supported agent CLIs include Claude Code, Codex, Grok, Kimi, Gemini CLI, Antigravity, Qwen, OpenCode, Crush, pi.dev, Copilot CLI, and Cursor, plus custom commands and local models via Ollama, LM Studio, or vLLM. [@claim:clm_48f3414a230ea43a10887f6e6861efe1e4ff8fdc5440503271c72e6c675b624e]
- Repository development practice: contributors run npm install && npm run dev, keep npm run typecheck green, run npm run test:focused, confirm npm run build works, derive new UI from DESIGN.md tokens, and keep changes scoped to one improvement per PR. [@claim:clm_65cf00780d4f07718226eae1a26da217219985d373045518e0de39091763f1bf]
- Running from source requires Node.js 18+, npm, a C/C++ toolchain for node-pty's native addon, and at least one supported agent CLI on PATH; missing CLIs can self-heal via an in-terminal installer. [@claim:clm_68821c5d4852b33fa4210e587093a776a5c9101453878e18dd635fc0b9b51fe2]
- A GOD agent acts as orchestrator: it reads requests, resolves routine ones autonomously, routes messages between agent inboxes, and escalates critical items (spend, destructive ops, scope changes) to a human approvals queue. [@claim:clm_94e66f6e6fbbcc586ddf284bd30d34f4d63364bfb126e87fff2ad7c1969488bb]
- The UI includes a Command Center with kanban tasks, scheduled missions, live fleet monitoring, memory search, a Skills catalog of 227 installable skills, and a built-in Monaco IDE with git rails; all fs/git access is brokered through main. [@claim:clm_acb94360ef1f441b69bdbf73cde7c4ebbf6115edd3baa81bf45f616540ba7c18]
- The hive is a local git repo of plain files: agents write to their own outbox, a router delivers to recipients' inboxes, and only the harness touches git (single-committer design to avoid index.lock corruption). [@claim:clm_c006d9232cba52d1aab4fd8e674d1604ad01321cb285cdcd3dc55e167d210632]
- Per-agent autonomy settings control how far agents act alone; spend, scope, and destructive operations escalate to the user, and a circuit breaker steers, constrains, then stops looping or runaway agents. [@claim:clm_d0ff5ac873f6207e95b546debce6147a2628a3f10d622477772e2d4c2f22ce7f]
- The architecture has two data planes — a terminal plane owning PTYs, filesystem and git, and an event plane running the hive, hook server, and router — with the renderer accessing both only through a typed bridge. [@claim:clm_d1d0bd3ef3c5bea3aa82d4ec6a60e604b755d58608782991a4227bf843176e33]
- Each agent keeps markdown memory mined into a shared searchable memory palace with a semantic recall index, persisting across sessions; the semantic index is optional and markdown memory works without it. [@claim:clm_d4f2c143576f72c17b29e346fd4affe3de9c10d38f31e299eb333f8a0697fd79]
- The product is a desktop app that wraps real terminal-agent CLIs as agents, wires them into a hive mind, and puts a clone agent (Michael) in charge of coordination. [@claim:clm_e7384455ef5657337aee8f18de3759367f7cdbe54b5f004d55836bbb51d187c4]
- The app is built with Electron, React, TypeScript, Pixi.js, xterm.js, and node-pty; each agent session runs as a real process in a pseudo-terminal rendered with xterm.js. [@claim:clm_fed551d34d91f84d971dd2a7474833e2a48bc6a5fa7203a9e8cd9a5daed43c3e]
<!-- rcw:end owner=source:src_acb354116db656d79018bb0a218f23d6 block=evidence -->

## Researcher notes

