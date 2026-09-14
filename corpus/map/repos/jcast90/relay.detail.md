# jcast90/relay -- full detail

[Back to orientation](relay.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jcast90/relay/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/eb9f73091bfb91b5.json](../../../wiki/dossiers/jcast90/relay/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/eb9f73091bfb91b5.json)

## specifications (2 claim(s))

- [observation/documented] Relay converts a sentence, GitHub issue URL, or Linear ticket into a running plan: classify, plan, decompose into a ticket DAG, dispatch to Claude or Codex agents, verify, open a PR, and track until merged. -- evidence: [README.md#L46-L46](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L46-L46) (`clm_722c218579a7fae6055f0a56b0287593bb14940c3b87f2abc5624c67f91bf681`)
- [observation/documented] The project is explicitly beta, pre-v1: APIs, CLI flags, ~/.relay file layouts, and GUI surfaces may change between releases, and users are asked to file issues with reproductions. -- evidence: [README.md#L32-L32](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L32-L32) (`clm_4aefb87951f21dc0d7829388b0bacb848c124ea3a88729e01b3c94d880463286`)

## components (2 claim(s))

- [observation/documented] The repo ships a TypeScript CLI/orchestrator core, a Rust ratatui TUI, a Tauri desktop GUI (React + Vite frontend, Rust backend), and a shared Rust crate harness-data that reads ~/.relay/ for both dashboards. -- evidence: [README.md#L558-L560](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L558-L560), [README.md#L541-L556](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L541-L556) (`clm_0472c816e5e1567a64c9fb5f528503717900713ac1dc0a034c90818a04b512ad`)
- [observation/documented] Verification runs through an Executor abstraction whose only shipping implementation is LocalChildProcessExecutor; a pod-based executor was prototyped and removed, and a Postgres HarnessStore backend is stubbed but not wired (HARNESS_STORE=postgres falls back to files). -- evidence: [README.md#L475-L475](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L475-L475), [README.md#L471-L471](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L471-L471) (`clm_9bde2121bbb7063907cb602e8362fcfb84dbd4650a020f51d9f1cf475f5ac488`)

## design-choices (2 claim(s))

- [observation/documented] Cross-repo work is designed to go through the primary repo's tools rather than file reads: quick questions use crosslink_send, longer tasks are tickets with assignedAlias routing, and the primary agent is told not to grep or edit associated repos directly. -- evidence: [README.md#L250-L252](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L250-L252), [README.md#L246-L246](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L246-L246), [README.md#L248-L248](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L248-L248) (`clm_8434eeb3dc3d82771621c0156c261865f957029e6da3e11b503134ad252fd9fc`)
- [observation/documented] Autonomous runs are bounded by wall-clock hours, a token budget, and a STOP-file kill switch, and verification commands run against an allowlist rather than being shelled blindly. -- evidence: [README.md#L62-L62](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L62-L62), [README.md#L60-L60](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L60-L60), [README.md#L268-L272](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L268-L272) (`clm_6c0e75c44ada0711b0785cdbf0982f0742b6510d69494a609c4d2a07e4ae2185`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are told to keep PR scope tight, run pnpm test && pnpm typecheck && pnpm build before pushing, add tests for new behavior (no snapshot tests of orchestrator output), and follow two-space indent/double-quote formatting; Vitest tests live in test/ mirroring src/. -- evidence: [README.md#L610-L613](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L610-L613), [README.md#L593-L594](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L593-L594), [README.md#L572-L580](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L572-L580) (`clm_c059d45f75c9fff58818efb9f1c830c8d7c7e67112a405d1abb34336e8c2706c`)
- [observation/documented] Repository development practice: AGENTS.md sets conventions for coding agents working in the repo, first-time contributors pick 'good first issue' issues and comment "I'll take this", and larger changes require opening an issue first to align on shape. -- evidence: [README.md#L602-L602](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L602-L602), [AGENTS.md#L3-L3](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/AGENTS.md#L3-L3), [README.md#L604-L606](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L604-L606) (`clm_f788aaf1da425324104e323d414267d2a6bce09e9c5565a3a4986ef979aca5c8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Relay exposes an MCP server to Claude and Codex with harness tools (e.g. harness_approve_plan, harness_dispatch), channel tools (channel_create, channel_record_decision, channel_handoff_finalize), and crosslink tools (crosslink_discover/send/poll); rly inspect-mcp lists the live set. -- evidence: [README.md#L385-L385](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L385-L385), [README.md#L387-L387](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L387-L387), [README.md#L391-L391](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L391-L391), [README.md#L389-L389](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L389-L389), [README.md#L393-L393](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L393-L393) (`clm_31076e71e94b1e08a6eb7ad67300cbe2a6eaa18f2efd1c63b8368ee88bfd7736`)
- [observation/documented] The two CLI adapters (claude, codex) accept any endpoint speaking their wire protocol, so OpenAI- or Anthropic-compatible HTTP providers work by setting base-URL and key env vars; named profiles reference env-var names rather than storing secrets. -- evidence: [README.md#L442-L442](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L442-L442), [README.md#L422-L422](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L422-L422) (`clm_071215cf671c5309749e756f9ccd993eacac7b4dfb85659f2065c6de3a0323a5`)

## memory-state (2 claim(s))

- [observation/documented] All state lives in ~/.relay/ as JSON/JSONL files with atomic tmp+rename writes, accessed through a single HarnessStore interface; channels hold feed.jsonl, tickets.json, decisions/<id>.json, sessions, and handoff briefs. -- evidence: [README.md#L495-L537](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L495-L537), [README.md#L469-L469](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L469-L469) (`clm_d33bbdea3e44236da7d21081fca986f0e2432a51dca71dde4544ab9fbb7c0a40`)
- [observation/documented] Cross-repo agents discover each other via heartbeat files under ~/.relay/crosslink/sessions/ and exchange messages directly through the crosslink MCP tools. -- evidence: [README.md#L256-L256](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L256-L256) (`clm_37125d3f7f55a01e834bc4060e438fa241e1061f36211dead2e18e59fafa2ecd`)

## orchestration (3 claim(s))

- [observation/documented] The pipeline runs classifier → planner (design doc if architectural) → decomposer into a dependency-DAG of tickets → scheduler running tickets in parallel capped by max-concurrency, then implement/verify/retry until a PR opens. -- evidence: [README.md#L180-L217](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L180-L217) (`clm_8d50777bac5605ed996fa4541a6b0736ec19d107bbfb7bef67216446e9acbed2`)
- [observation/documented] Requests are classified into complexity tiers (trivial, bugfix, feature_small, feature_large, architectural, multi_repo); feature_large and above require user approval via MCP, while trivial/bugfix use heuristic matching. -- evidence: [README.md#L221-L228](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L221-L228) (`clm_44a45558cbb503f5be92c798957d58923e76e1d616be147648a8dc056b074539`)
- [observation/documented] With GITHUB_TOKEN set, a background PR watcher polls every 30 seconds; CI failures and changes-requested reviews automatically become follow-up tickets via the scheduler's dynamic enqueue. -- evidence: [README.md#L412-L412](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L412-L412) (`clm_267e21a505cb5abef02ee8f841ccdfb8a8740d84c77d14dce9e13e08312c6011`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Issue-tracker and SCM integrations build on Composio's @aoagents/ao-core leaf plugins, and Relay exports a HarnessChannelNotifier so it can act as a notifier plugin for Composio's ao orchestrator. -- evidence: [README.md#L640-L642](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L640-L642), [README.md#L418-L418](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L418-L418), [README.md#L399-L399](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L399-L399) (`clm_9e88a85f75c1e3eb2b609655ca96eca15b981755966689e36aaae5073562360a`)
- [observation/documented] GitHub integration requires GITHUB_TOKEN (with project scope for Projects v2 sync) and Linear integration uses LINEAR_API_KEY or COMPOSIO_API_KEY; the CLI needs Node >= 20 and pnpm to build from source. -- evidence: [README.md#L403-L404](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L403-L404), [README.md#L114-L114](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L114-L114) (`clm_26d5d598d767b361e06a00c4ceb4a4246722b25a63f3688ea0ab29cb9a2182da`)

## limitations (2 claim(s))

- [observation/documented] Documented limits: cross-platform spawn is lightly tested off macOS, and cost guardrails (per-run dollar/token budget caps) are not yet implemented, though per-session context-window telemetry ships in v0.7.x. -- evidence: [README.md#L619-L620](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L619-L620) (`clm_7eec4fa07472284f1265b10901b07d69ce060728dedf449da3addc2963566a54`)
- [observation/documented] Pre-release GUI builds are unsigned, so macOS Gatekeeper and Windows SmartScreen warn on first launch; code signing and notarization are roadmap items. -- evidence: [README.md#L124-L127](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L124-L127), [README.md#L626-L632](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L626-L632) (`clm_da31d9ef0d3f851a260971a2e50db0ab8d5f88dee4051fe08083dca8565d1c43`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

