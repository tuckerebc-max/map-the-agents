---
access: public
aliases: []
claim_ids:
- clm_0472c816e5e1567a64c9fb5f528503717900713ac1dc0a034c90818a04b512ad
- clm_071215cf671c5309749e756f9ccd993eacac7b4dfb85659f2065c6de3a0323a5
- clm_267e21a505cb5abef02ee8f841ccdfb8a8740d84c77d14dce9e13e08312c6011
- clm_26d5d598d767b361e06a00c4ceb4a4246722b25a63f3688ea0ab29cb9a2182da
- clm_31076e71e94b1e08a6eb7ad67300cbe2a6eaa18f2efd1c63b8368ee88bfd7736
- clm_37125d3f7f55a01e834bc4060e438fa241e1061f36211dead2e18e59fafa2ecd
- clm_44a45558cbb503f5be92c798957d58923e76e1d616be147648a8dc056b074539
- clm_4aefb87951f21dc0d7829388b0bacb848c124ea3a88729e01b3c94d880463286
- clm_6c0e75c44ada0711b0785cdbf0982f0742b6510d69494a609c4d2a07e4ae2185
- clm_722c218579a7fae6055f0a56b0287593bb14940c3b87f2abc5624c67f91bf681
- clm_7eec4fa07472284f1265b10901b07d69ce060728dedf449da3addc2963566a54
- clm_8434eeb3dc3d82771621c0156c261865f957029e6da3e11b503134ad252fd9fc
- clm_8d50777bac5605ed996fa4541a6b0736ec19d107bbfb7bef67216446e9acbed2
- clm_9bde2121bbb7063907cb602e8362fcfb84dbd4650a020f51d9f1cf475f5ac488
- clm_9e88a85f75c1e3eb2b609655ca96eca15b981755966689e36aaae5073562360a
- clm_c059d45f75c9fff58818efb9f1c830c8d7c7e67112a405d1abb34336e8c2706c
- clm_d33bbdea3e44236da7d21081fca986f0e2432a51dca71dde4544ab9fbb7c0a40
- clm_da31d9ef0d3f851a260971a2e50db0ab8d5f88dee4051fe08083dca8565d1c43
- clm_f788aaf1da425324104e323d414267d2a6bce09e9c5565a3a4986ef979aca5c8
maturity: draft
page_id: pg_a09c62eca44a585fbd4c45f463182390
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9f143dfb8d245ea4a08a657404b21094
title: jcast90/relay/README.md @ 7bd5a2f6a13c
updated_at: '2026-09-14T02:07:17Z'
---

# jcast90/relay/README.md @ 7bd5a2f6a13c

<!-- rcw:begin owner=source:src_9f143dfb8d245ea4a08a657404b21094 block=evidence -->
- The repo ships a TypeScript CLI/orchestrator core, a Rust ratatui TUI, a Tauri desktop GUI (React + Vite frontend, Rust backend), and a shared Rust crate harness-data that reads ~/.relay/ for both dashboards. [@claim:clm_0472c816e5e1567a64c9fb5f528503717900713ac1dc0a034c90818a04b512ad]
- The two CLI adapters (claude, codex) accept any endpoint speaking their wire protocol, so OpenAI- or Anthropic-compatible HTTP providers work by setting base-URL and key env vars; named profiles reference env-var names rather than storing secrets. [@claim:clm_071215cf671c5309749e756f9ccd993eacac7b4dfb85659f2065c6de3a0323a5]
- With GITHUB_TOKEN set, a background PR watcher polls every 30 seconds; CI failures and changes-requested reviews automatically become follow-up tickets via the scheduler's dynamic enqueue. [@claim:clm_267e21a505cb5abef02ee8f841ccdfb8a8740d84c77d14dce9e13e08312c6011]
- GitHub integration requires GITHUB_TOKEN (with project scope for Projects v2 sync) and Linear integration uses LINEAR_API_KEY or COMPOSIO_API_KEY; the CLI needs Node >= 20 and pnpm to build from source. [@claim:clm_26d5d598d767b361e06a00c4ceb4a4246722b25a63f3688ea0ab29cb9a2182da]
- Relay exposes an MCP server to Claude and Codex with harness tools (e.g. harness_approve_plan, harness_dispatch), channel tools (channel_create, channel_record_decision, channel_handoff_finalize), and crosslink tools (crosslink_discover/send/poll); rly inspect-mcp lists the live set. [@claim:clm_31076e71e94b1e08a6eb7ad67300cbe2a6eaa18f2efd1c63b8368ee88bfd7736]
- Cross-repo agents discover each other via heartbeat files under ~/.relay/crosslink/sessions/ and exchange messages directly through the crosslink MCP tools. [@claim:clm_37125d3f7f55a01e834bc4060e438fa241e1061f36211dead2e18e59fafa2ecd]
- Requests are classified into complexity tiers (trivial, bugfix, feature_small, feature_large, architectural, multi_repo); feature_large and above require user approval via MCP, while trivial/bugfix use heuristic matching. [@claim:clm_44a45558cbb503f5be92c798957d58923e76e1d616be147648a8dc056b074539]
- The project is explicitly beta, pre-v1: APIs, CLI flags, ~/.relay file layouts, and GUI surfaces may change between releases, and users are asked to file issues with reproductions. [@claim:clm_4aefb87951f21dc0d7829388b0bacb848c124ea3a88729e01b3c94d880463286]
- Autonomous runs are bounded by wall-clock hours, a token budget, and a STOP-file kill switch, and verification commands run against an allowlist rather than being shelled blindly. [@claim:clm_6c0e75c44ada0711b0785cdbf0982f0742b6510d69494a609c4d2a07e4ae2185]
- Relay converts a sentence, GitHub issue URL, or Linear ticket into a running plan: classify, plan, decompose into a ticket DAG, dispatch to Claude or Codex agents, verify, open a PR, and track until merged. [@claim:clm_722c218579a7fae6055f0a56b0287593bb14940c3b87f2abc5624c67f91bf681]
- Documented limits: cross-platform spawn is lightly tested off macOS, and cost guardrails (per-run dollar/token budget caps) are not yet implemented, though per-session context-window telemetry ships in v0.7.x. [@claim:clm_7eec4fa07472284f1265b10901b07d69ce060728dedf449da3addc2963566a54]
- Cross-repo work is designed to go through the primary repo's tools rather than file reads: quick questions use crosslink_send, longer tasks are tickets with assignedAlias routing, and the primary agent is told not to grep or edit associated repos directly. [@claim:clm_8434eeb3dc3d82771621c0156c261865f957029e6da3e11b503134ad252fd9fc]
- The pipeline runs classifier → planner (design doc if architectural) → decomposer into a dependency-DAG of tickets → scheduler running tickets in parallel capped by max-concurrency, then implement/verify/retry until a PR opens. [@claim:clm_8d50777bac5605ed996fa4541a6b0736ec19d107bbfb7bef67216446e9acbed2]
- Verification runs through an Executor abstraction whose only shipping implementation is LocalChildProcessExecutor; a pod-based executor was prototyped and removed, and a Postgres HarnessStore backend is stubbed but not wired (HARNESS_STORE=postgres falls back to files). [@claim:clm_9bde2121bbb7063907cb602e8362fcfb84dbd4650a020f51d9f1cf475f5ac488]
- Issue-tracker and SCM integrations build on Composio's @aoagents/ao-core leaf plugins, and Relay exports a HarnessChannelNotifier so it can act as a notifier plugin for Composio's ao orchestrator. [@claim:clm_9e88a85f75c1e3eb2b609655ca96eca15b981755966689e36aaae5073562360a]
- Repository development practice: contributors are told to keep PR scope tight, run pnpm test && pnpm typecheck && pnpm build before pushing, add tests for new behavior (no snapshot tests of orchestrator output), and follow two-space indent/double-quote formatting; Vitest tests live in test/ mirroring src/. [@claim:clm_c059d45f75c9fff58818efb9f1c830c8d7c7e67112a405d1abb34336e8c2706c]
- All state lives in ~/.relay/ as JSON/JSONL files with atomic tmp+rename writes, accessed through a single HarnessStore interface; channels hold feed.jsonl, tickets.json, decisions/<id>.json, sessions, and handoff briefs. [@claim:clm_d33bbdea3e44236da7d21081fca986f0e2432a51dca71dde4544ab9fbb7c0a40]
- Pre-release GUI builds are unsigned, so macOS Gatekeeper and Windows SmartScreen warn on first launch; code signing and notarization are roadmap items. [@claim:clm_da31d9ef0d3f851a260971a2e50db0ab8d5f88dee4051fe08083dca8565d1c43]
- Repository development practice: AGENTS.md sets conventions for coding agents working in the repo, first-time contributors pick 'good first issue' issues and comment "I'll take this", and larger changes require opening an issue first to align on shape. [@claim:clm_f788aaf1da425324104e323d414267d2a6bce09e9c5565a3a4986ef979aca5c8]
<!-- rcw:end owner=source:src_9f143dfb8d245ea4a08a657404b21094 block=evidence -->

## Researcher notes

