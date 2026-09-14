---
access: public
aliases: []
claim_ids:
- clm_0810525c4f98fb835b0c70c6eb56e5b0738a42da9913e318c79bbca598ac2b77
- clm_2fa9ca3b579f0d06808d44370250f41ebb4d5cf4da73009235b38eba9b13bcf6
- clm_402693a36a8723f2b7ebcf0ceaf4da9991dd76d46155796b5afd94b555987739
- clm_82d8c8082968192cff8bc2d1973c3f0392484bf2d0594c05a0978fc069470640
- clm_85b684cefe7b1f6b226965d2a9dd5af31985b68cc7d2b0eb6aa4b2f500aa84e7
- clm_a39f962ad548fdcf53b8eef7ca576ca0ca85389d77dcefe5153c2ce3948092be
- clm_ad2dff2d84b335eb4f7eff67ce8f546c835e0d16c5f42cc29097890abd4f63be
- clm_af2858ff9d218bc0cd948fea8072c18afb3e3502a408f43058d8204a7413a725
- clm_bb1ab7016a50d34c290b9ae46b34ea7ccd6e138e086fa52fce55a6e40a231f89
- clm_c1ef2f2c1496e9431403bbc215544bd8b2183f9bfa98dde0acf90dce1378fb55
- clm_d85b7930f41e70ca2aded742293af598331bce9a603873cfbcfca875f9e16088
- clm_e570d7b17b9d88894d3230dfc67c4d1fced1e9aded22b638681a1b3a508d9363
maturity: draft
page_id: pg_4e7781208a915345a25f41ffa43b8b6e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8fb9d84d31015275b76d61e5f74a1070
title: razzant/claudexor/README.md @ 87f08d28cf33
updated_at: '2026-09-14T02:35:22Z'
---

# razzant/claudexor/README.md @ 87f08d28cf33

<!-- rcw:begin owner=source:src_8fb9d84d31015275b76d61e5f74a1070 block=evidence -->
- The --delegate flag injects a scoped MCP belt exposing only ask/plan/run/best-of/status/result tools, with nesting depth 1, a default cap of 8 sub-runs per parent, and shared daemon-owned budget authority; only adapters declaring mcp_injection (claude, codex, cursor) can host it. [@claim:clm_0810525c4f98fb835b0c70c6eb56e5b0738a42da9913e318c79bbca598ac2b77]
- Canonical modes are ask (read-only, with --deep-scan multi-scout research), plan (with --council parallel multi-harness drafting merged into one plan), and agent (with --n best-of races, --attempts repair loops, --until-clean, and --delegate). [@claim:clm_2fa9ca3b579f0d06808d44370250f41ebb4d5cf4da73009235b38eba9b13bcf6]
- Live subscription-quota tracking and auto-rotation on typed vendor limits cover only harnesses with a vendor usage source (Antigravity, Claude, Codex); Cursor has none yet, and the portable Copilot plugin does not support Windows. [@claim:clm_402693a36a8723f2b7ebcf0ceaf4da9991dd76d46155796b5afd94b555987739]
- The product is local-first: everything runs on the user's machine, files are the source of truth, and the README states there is no telemetry. [@claim:clm_82d8c8082968192cff8bc2d1973c3f0392484bf2d0594c05a0978fc069470640]
- Read-only ask/plan turns resume the routed harness's native CLI session in a durable per-lane home; lane switches hydrate with a bounded continuation packet written to context/THREAD.md and disclosed via a typed session.continuity event. [@claim:clm_85b684cefe7b1f6b226965d2a9dd5af31985b68cc7d2b0eb6aa4b2f500aa84e7]
- Retired mode ids and verbs (audit, best_of_n, explore, orchestrate, etc.) hard-error with the new spelling rather than silently aliasing; unknown flags and invalid flag values exit with code 2. [@claim:clm_a39f962ad548fdcf53b8eef7ca576ca0ca85389d77dcefe5153c2ce3948092be]
- Repository development practice: contributors build with pnpm install --frozen-lockfile and pnpm build, then run typecheck, test, schema:gen with a generated-diff check, docs:check, and knip as gates. [@claim:clm_ad2dff2d84b335eb4f7eff67ce8f546c835e0d16c5f42cc29097890abd4f63be]
- Claudexor exposes a CLI, a loopback HTTP/SSE control API scoped to /v2 with POST /v2/handshake negotiation, MCP, ACP, and a macOS app as thin surfaces over the daemon. [@claim:clm_af2858ff9d218bc0cd948fea8072c18afb3e3502a408f43058d8204a7413a725]
- Protected paths configured in .claudexor/config.yaml pause apply for a human decision; --allow-protected-path covers only engine-derived gate/test paths and cannot suppress project rules, and mutating turns on such projects are promoted one-way to an isolated worktree. [@claim:clm_bb1ab7016a50d34c290b9ae46b34ea7ccd6e138e086fa52fce55a6e40a231f89]
- Prerequisites are Node.js >= 20.19, pnpm via corepack, Git for Git-backed worktrees, and at least one logged-in vendor CLI (codex, claude, cursor-agent, opencode, or agy) or a provider API key; the desktop app requires macOS while the CLI/daemon also run on Linux. [@claim:clm_c1ef2f2c1496e9431403bbc215544bd8b2183f9bfa98dde0acf90dce1378fb55]
- Cost accounting is typed: paid budgets are explicit via --max-usd with zero as a real cap, unknown cost is never reported as $0, and runs can end cost_unverifiable or budget_overshoot. [@claim:clm_d85b7930f41e70ca2aded742293af598331bce9a603873cfbcfca875f9e16088]
- The monorepo splits packages/schema (contracts and generated JSON Schema), harness-* adapters, workspace (Git/directory envelopes), orchestrator (canonical mode pipelines), and review/arbitration/synthesis/budget packages. [@claim:clm_e570d7b17b9d88894d3230dfc67c4d1fced1e9aded22b638681a1b3a508d9363]
<!-- rcw:end owner=source:src_8fb9d84d31015275b76d61e5f74a1070 block=evidence -->

## Researcher notes

