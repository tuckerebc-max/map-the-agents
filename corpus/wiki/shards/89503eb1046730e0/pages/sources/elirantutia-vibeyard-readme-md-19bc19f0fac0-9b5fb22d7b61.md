---
access: public
aliases: []
claim_ids:
- clm_2a87da2b694494b4bb676f10f32dfbc40007d82c2161ab3afa47492cab02c109
- clm_44b916a9bcfff319ae139421728796832813139cab7a625a7f862f9d0b390e12
- clm_5fc7125c9ed8a8f2a1ffdfaf93ce4ded35454ecca6a9a32f6c2bdccc42e4f4e2
- clm_c1f5a5e3af4e3d39a34287010605679fd525ac789bc8dca1b69553693e584ca6
- clm_cd1dd5c2a27ef7b09646ac0d9c961942353f62a4df313b4f8436558e18979cbf
- clm_d803cc054004706a8e3cb6a609255a59179d79534008bea812b1de5a201f00bf
- clm_f59bf33c1a0b43e39e80f2c3e4c8c2b29e16cdd459aa05679156ab5218072901
- clm_f6ec59acb66df9fa496c4b57fd76c388928b2954080e0a4ead3cf76b54f80a44
maturity: draft
page_id: pg_dd5873073d2750b5bbc79b5fb22d7b61
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8985ff70f7ba57339207c7e7909570a1
title: elirantutia/vibeyard/README.md @ 19bc19f0fac0
updated_at: '2026-09-14T03:07:17Z'
---

# elirantutia/vibeyard/README.md @ 19bc19f0fac0

<!-- rcw:begin owner=source:src_8985ff70f7ba57339207c7e7909570a1 block=evidence -->
- Repository development practice: building from source clones the repo and runs npm install && npm start, requiring Node v24+. [@claim:clm_2a87da2b694494b4bb676f10f32dfbc40007d82c2161ab3afa47492cab02c109]
- Distribution channels documented are macOS .dmg, Linux .deb and AppImage, Windows NSIS installer and portable .exe, and a global npm package that downloads and launches the app on first run. [@claim:clm_44b916a9bcfff319ae139421728796832813139cab7a625a7f862f9d0b390e12]
- The product exposes keyboard-driven interfaces, including Cmd+\ to spin up new sessions in swarm mode and Cmd+Shift+I to open the session inspector. [@claim:clm_5fc7125c9ed8a8f2a1ffdfaf93ce4ded35454ecca6a9a32f6c2bdccc42e4f4e2]
- The app requires at least one supported CLI (Claude Code, OpenAI Codex CLI, or Gemini CLI) to be installed and authenticated. [@claim:clm_c1f5a5e3af4e3d39a34287010605679fd525ac789bc8dca1b69553693e584ca6]
- Documented features include a customizable per-project dashboard with widgets, a kanban task board, P2P session sharing, multi-session management, cost/context tracking, a session inspector, and an AI Readiness Score. [@claim:clm_cd1dd5c2a27ef7b09646ac0d9c961942353f62a4df313b4f8436558e18979cbf]
- Each agent session runs in its own PTY, and multiple Claude profiles are supported with each session backed by an isolated config directory so credentials and history do not mix. [@claim:clm_d803cc054004706a8e3cb6a609255a59179d79534008bea812b1de5a201f00bf]
- Vibeyard is described as an IDE built for AI coding agents: it manages multiple agent sessions, runs them in parallel, tracks costs, and supports Claude Code, Codex CLI, and Gemini CLI. [@claim:clm_f59bf33c1a0b43e39e80f2c3e4c8c2b29e16cdd459aa05679156ab5218072901]
- P2P session sharing uses encrypted WebRTC connections with read-only or read-write modes and PIN-based authentication. [@claim:clm_f6ec59acb66df9fa496c4b57fd76c388928b2954080e0a4ead3cf76b54f80a44]
<!-- rcw:end owner=source:src_8985ff70f7ba57339207c7e7909570a1 block=evidence -->

## Researcher notes

