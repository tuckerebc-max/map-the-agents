---
access: public
aliases: []
claim_ids:
- clm_4cd34d5551947c70c023e60edaea599eaf455d047999ce9b7367700f5b8de850
- clm_61492d9f3e9f75f75f39469e3f7c26a8b584acb6e188c5e64006f166e0d1f833
- clm_633cb0ad6019c0e33f7cf664d07e08be157d85ae54a5e8155c60e3dbddb9b37d
- clm_96c3735dbe748530c1d6eff3cad51502356ee5f541fe68705d84f0a6136c4823
- clm_b7a2d291f0141e3c5eb708aa713843124630d8401b7073f3b9f7e0bc140cb83d
- clm_cb8f0051563e620716136601473d9fcac79d6dacb92ec17441b849c7fe9db806
maturity: draft
page_id: pg_f73378f143a05d3da525ed030801a78f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6cbf6fb3cf05534792f93afcbada8d3e
title: Choeng-Rayu/rayu-cli/CHANGELOG.md @ c16466f3b068
updated_at: '2026-09-14T01:40:58Z'
---

# Choeng-Rayu/rayu-cli/CHANGELOG.md @ c16466f3b068

<!-- rcw:begin owner=source:src_6cbf6fb3cf05534792f93afcbada8d3e block=evidence -->
- The CLI includes a Telegram bridge for remote access with multi-session support, health monitoring showing connected/reconnecting/disconnected states, and a remote uninstall gated by local opt-in, device targeting, and single-use confirmation tokens. [@claim:clm_4cd34d5551947c70c023e60edaea599eaf455d047999ce9b7367700f5b8de850]
- The changelog describes a secure IPC layer using a Unix socket protocol with per-session token auth, enabling cross-session routing and multi-session coordination. [@claim:clm_61492d9f3e9f75f75f39469e3f7c26a8b584acb6e188c5e64006f166e0d1f833]
- The changelog documents an External Agent Orchestrator with an /agent command and ExternalAgent tool to launch and coordinate other agentic CLIs (Codex, Claude Code, OpenCode, ACP agents), with parallel/sequential/race/retry/fallback policies, git worktree isolation, and crash recovery. [@claim:clm_633cb0ad6019c0e33f7cf664d07e08be157d85ae54a5e8155c60e3dbddb9b37d]
- The CLI exposes slash commands including /model for mid-session model switching, /connect for provider setup, /sessions and /switch for Telegram bridge sessions, and /banner, /mascot, /brandmark for branding display. [@claim:clm_96c3735dbe748530c1d6eff3cad51502356ee5f541fe68705d84f0a6136c4823]
- The changelog references product permission modes, including a fix to the Ask User Question tool in 'full manage (full-control) permission mode' and brokered permissions in the external agent orchestrator. [@claim:clm_b7a2d291f0141e3c5eb708aa713843124630d8401b7073f3b9f7e0bc140cb83d]
- The changelog describes a planner subagent dispatching parallel Explore subagents, a collaborator swarm with persistent agent memory syncing, and /ultraplan and /ultrareview commands that run parallel planning/review subagents on the user's own provider. [@claim:clm_cb8f0051563e620716136601473d9fcac79d6dacb92ec17441b849c7fe9db806]
<!-- rcw:end owner=source:src_6cbf6fb3cf05534792f93afcbada8d3e block=evidence -->

## Researcher notes

