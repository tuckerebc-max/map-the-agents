---
access: public
aliases: []
claim_ids:
- clm_034c6f43ea2e356be32619a1578c08bfb253d4ed33e7989723f5fed75224f34e
- clm_3f27353aacc7bae583f8cc1176865eaf234c7a4ba50592a758e73ff4f83abdcf
- clm_3f60bf2048d798af310564f39b659a5373ae702628a5efa6200e8d8320886cf8
- clm_4c8cef09c2db3e11dc37a7c185ae2fd2219ce4880ddf4734aa921858c8d72b39
- clm_4fda252b71cfc4b110549a099e65ddbd0383175d29ddf59c3b31f2c1eed75f21
- clm_59968ad4db375c2ae8c5e50fdfca5d79284e16f09f9636e309b52ebf0d73cbcf
- clm_6dec9a6b2ff27ceddced7415554e2e6da0215fee9dec2d407c408d31a24b628c
- clm_91bd966f3045ba6b84d3532c858f5b7a4e43372a8803acced213d412c3914876
- clm_93639689bc448f8e6662c76aec6a5bdb60ef4f69f5b9c8314f01f9ce4b0b9b4b
- clm_9c3ca1cd7146692bef11644694eed86f9578314e1b755ab03089d04ba32561f9
- clm_a640aa2239f7f5ad12f0c7bd7f44cb54808e29f3156cf1fbf307d4910ca32bb5
- clm_ab5855f79fa29cbf9df4c3b58929120011e7536d7f4777845e4903b6316e9ca0
- clm_c120cb7d03f032d195bfdf809b8d14bb0d5bc9beb5dff550be2d2532390223d6
- clm_c3b7c3ca324439612472f28348b31f0ba630ec60a2d3bf83a4f493912c44e7a6
- clm_efc27c64d267a89ecf576c272a9c1be6157ca0380f8db5fa81e9e3304be47c9e
maturity: draft
page_id: pg_b3ac718644a355d38bbd679b4af00609
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_458b8a781ef05b4a90207679c38f0ade
title: ohad6k/VibeRaven/README.md @ f64e97730fd5
updated_at: '2026-09-14T02:24:31Z'
---

# ohad6k/VibeRaven/README.md @ f64e97730fd5

<!-- rcw:begin owner=source:src_458b8a781ef05b4a90207679c38f0ade block=evidence -->
- Provider state is not inferred from repo code alone: analytics ingestion like PostHog is flagged for dashboard proof, and undetected providers are reported as "Not detected" rather than claiming repo evidence. [@claim:clm_034c6f43ea2e356be32619a1578c08bfb253d4ed33e7989723f5fed75224f34e]
- The product is invoked via npx as `viberaven` (Studio), `viberaven check` (terminal verdict), `viberaven fix`, `viberaven init --agents`, `viberaven doctor --agents`, and `viberaven audit --vercel-supabase`, with a `--strict` gate and `--mcp` mode. [@claim:clm_3f27353aacc7bae583f8cc1176865eaf234c7a4ba50592a758e73ff4f83abdcf]
- The MCP server exposes tools including viberaven_check_readiness, viberaven_heal_apply, viberaven_verify, viberaven_audit, viberaven_provider_verify, and viberaven_validate_npm_package. [@claim:clm_3f60bf2048d798af310564f39b659a5373ae702628a5efa6200e8d8320886cf8]
- A six-skill skills.sh pack routes agents: viberaven (router), architecture-context, architecture-plan, what-broke, production-context, and go-live, installable via `skills add ohad6k/VibeRaven --skill viberaven`. [@claim:clm_4c8cef09c2db3e11dc37a7c185ae2fd2219ce4880ddf4734aa921858c8d72b39]
- The MCP tool viberaven_validate_npm_package is intended to be run before adding npm dependencies, suggesting the product offers dependency validation as part of its checks. [@claim:clm_4fda252b71cfc4b110549a099e65ddbd0383175d29ddf59c3b31f2c1eed75f21]
- Fix recipes are described as guarded and non-destructive: cleanup is plan-only and nothing is pushed or deployed automatically. [@claim:clm_59968ad4db375c2ae8c5e50fdfca5d79284e16f09f9636e309b52ebf0d73cbcf]
- `viberaven init --agents all` writes bounded VIBERAVEN:START/END rule blocks into AGENTS.md, CLAUDE.md, GEMINI.md, Cursor rules, copilot instructions, and .viberaven context files, with a --dry-run preview. [@claim:clm_6dec9a6b2ff27ceddced7415554e2e6da0215fee9dec2d407c408d31a24b628c]
- The repo doubles as an agent plugin (plugin.yaml, .claude-plugin/, .codex-plugin/, gemini-extension.json) exposing the six skills plus /viberaven-work, /viberaven-help, /viberaven-production-context, and /viberaven-launch commands. [@claim:clm_91bd966f3045ba6b84d3532c858f5b7a4e43372a8803acced213d412c3914876]
- The tool is local-first: CLI and Studio run on the user's machine with no login, API key, telemetry, or scan quota, and all context is written to .viberaven/ as markdown and JSON readable by git and any agent. [@claim:clm_93639689bc448f8e6662c76aec6a5bdb60ef4f69f5b9c8314f01f9ce4b0b9b4b]
- The installed agent rules teach a loop: run check, read .viberaven/, fix one gap, then re-check until gate.status equals "clear". [@claim:clm_9c3ca1cd7146692bef11644694eed86f9578314e1b755ab03089d04ba32561f9]
- The public repo is described as the agent discovery/installation surface, while product source development happens in a private repository; current release is viberaven@1.4.2 (AGENTS.md references 1.4.3). [@claim:clm_a640aa2239f7f5ad12f0c7bd7f44cb54808e29f3156cf1fbf307d4910ca32bb5]
- VibeRaven targets developers of AI-built apps who want a pre-launch safety verdict on auth, RLS, webhooks, and deploy before real users hit the app. [@claim:clm_ab5855f79fa29cbf9df4c3b58929120011e7536d7f4777845e4903b6316e9ca0]
- Provider detection covers Supabase, Vercel, GitHub, Stripe, Sentry, Resend, Clerk, Auth.js, PostHog, and Upstash, rendered as trading-card style cards in the Studio. [@claim:clm_c120cb7d03f032d195bfdf809b8d14bb0d5bc9beb5dff550be2d2532390223d6]
- `viberaven check` prints one line per finding with file:line evidence in artifacts and exits with code 1 when blockers exist. [@claim:clm_c3b7c3ca324439612472f28348b31f0ba630ec60a2d3bf83a4f493912c44e7a6]
- The Studio browser UI offers agent chat, draggable provider cards and releases, an architecture map, a worktree view, and access-mode selection (ask/approve/full) that changes the actual agent command run. [@claim:clm_efc27c64d267a89ecf576c272a9c1be6157ca0380f8db5fa81e9e3304be47c9e]
<!-- rcw:end owner=source:src_458b8a781ef05b4a90207679c38f0ade block=evidence -->

## Researcher notes

