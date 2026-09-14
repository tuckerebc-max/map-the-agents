---
access: public
aliases: []
claim_ids:
- clm_05da2199c8cbefd3d715c7fc7795486b35a72e2e67b2780131609550d4708336
- clm_1471504e3f262621d255002347a22c61acf67e4e95af3d8185a31e9b8fa7dc7e
- clm_49501f1b98b09b75d69a22cab16b61dd0d53928aaaab173f2bbcc1ca0b05e2e0
- clm_9445284e2146a59245061fe01141bbd51f4ef4b6e8db1bc58657abea916ef249
- clm_a819b4da41daf5c2dbe1db3e709b06ac0bdb4e969f1223a5ee8d366f48a88d60
- clm_ab0639465f1e7fff79e5cec4903ced71ec8b736dc0dfdfacdfbb862d4acaa208
- clm_aca1767cd9d8929f9e05307db2817ab2ff1f939eef3904df91511b568702ac3d
- clm_e2553660f069fc179c37fc6b213858c828575630d6d1313facd0a9d1b242b063
- clm_f382a85c34006e18520b3e2a88346d45e32c42de27b2042721812aafac564c79
- clm_ffb49ff8ed633bd5177c42c0238ce0db7a3f945904cda8a03ef1490b2f242399
maturity: draft
page_id: pg_d4cce1002783598f8b53d4fc321f5582
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_94d5a5c6dc3e5260842f69d1ba8fe399
title: littlebearapps/untether/README.md @ 4285dad5a12e
updated_at: '2026-09-14T02:13:52Z'
---

# littlebearapps/untether/README.md @ 4285dad5a12e

<!-- rcw:begin owner=source:src_94d5a5c6dc3e5260842f69d1ba8fe399 block=evidence -->
- Interactive permissions, plan mode, ask mode, diff preview, and auto-approve of safe tools are Claude Code-only; other engines use pre-run approval policies or none. [@claim:clm_05da2199c8cbefd3d715c7fc7795486b35a72e2e67b2780131609550d4708336]
- Requirements are Python 3.12+, uv, and at least one agent CLI (claude, codex, opencode, pi, gemini, or amp) on PATH. [@claim:clm_1471504e3f262621d255002347a22c61acf67e4e95af3d8185a31e9b8fa7dc7e]
- Interactive permission buttons let users approve plan transitions and answer clarifying questions; tools auto-execute, and a 'Pause & Outline Plan' option holds the session open for plan review. [@claim:clm_49501f1b98b09b75d69a22cab16b61dd0d53928aaaab173f2bbcc1ca0b05e2e0]
- Messages can be prefixed with /<engine> to pick an engine for that task, or /<project> to target a specific repository. [@claim:clm_9445284e2146a59245061fe01141bbd51f4ef4b6e8db1bc58657abea916ef249]
- The setup wizard offers three workflow modes: Assistant (ongoing chat with auto-resume), Workspace (forum topics bound to project/branch), and Handoff (reply-to-continue). [@claim:clm_a819b4da41daf5c2dbe1db3e709b06ac0bdb4e969f1223a5ee8d366f48a88d60]
- Untether stores chat preferences, session state, and usage stats as JSON files under ~/.untether/, plus an optional per-project .untether-outbox/ directory for agent-delivered files. [@claim:clm_ab0639465f1e7fff79e5cec4903ced71ec8b736dc0dfdfacdfbb862d4acaa208]
- Configuration lives in ~/.untether/untether.toml with sections for default engine, Telegram transport, projects, and cost budgets (per-run and daily limits). [@claim:clm_aca1767cd9d8929f9e05307db2817ab2ff1f939eef3904df91511b568702ac3d]
- Voice transcription uses a configurable Whisper-compatible endpoint and is disabled by default, opt-in via config. [@claim:clm_e2553660f069fc179c37fc6b213858c828575630d6d1313facd0a9d1b242b063]
- Users interact via Telegram bot commands including /cancel, /agent, /model, /planmode, /usage, /export, /browse, /config, /continue, /file put/get, /topic, /restart, /stats, and /auth. [@claim:clm_f382a85c34006e18520b3e2a88346d45e32c42de27b2042721812aafac564c79]
- For several engines (Codex, Pi, Gemini, Amp), cost tracking reports token usage counts only, with no USD cost reporting. [@claim:clm_ffb49ff8ed633bd5177c42c0238ce0db7a3f945904cda8a03ef1490b2f242399]
<!-- rcw:end owner=source:src_94d5a5c6dc3e5260842f69d1ba8fe399 block=evidence -->

## Researcher notes

