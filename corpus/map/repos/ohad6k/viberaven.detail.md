# ohad6k/viberaven -- full detail

[Back to orientation](viberaven.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ohad6k/viberaven/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/c3cd057bf9b81d82.json](../../../wiki/dossiers/ohad6k/viberaven/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/c3cd057bf9b81d82.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Provider detection covers Supabase, Vercel, GitHub, Stripe, Sentry, Resend, Clerk, Auth.js, PostHog, and Upstash, rendered as trading-card style cards in the Studio. -- evidence: [README.md#L45-L45](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L45-L45), [README.md#L47-L49](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L47-L49) (`clm_c120cb7d03f032d195bfdf809b8d14bb0d5bc9beb5dff550be2d2532390223d6`)
- [observation/documented] The public repo is described as the agent discovery/installation surface, while product source development happens in a private repository; current release is viberaven@1.4.2 (AGENTS.md references 1.4.3). -- evidence: [README.md#L196-L196](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L196-L196), [README.md#L200-L200](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L200-L200), [AGENTS.md#L3-L3](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/AGENTS.md#L3-L3) (`clm_a640aa2239f7f5ad12f0c7bd7f44cb54808e29f3156cf1fbf307d4910ca32bb5`)

## design-choices (2 claim(s))

- [observation/documented] The tool is local-first: CLI and Studio run on the user's machine with no login, API key, telemetry, or scan quota, and all context is written to .viberaven/ as markdown and JSON readable by git and any agent. -- evidence: [README.md#L173-L176](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L173-L176), [README.md#L106-L106](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L106-L106), [README.md#L51-L51](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L51-L51), [README.md#L67-L67](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L67-L67) (`clm_93639689bc448f8e6662c76aec6a5bdb60ef4f69f5b9c8314f01f9ce4b0b9b4b`)
- [observation/documented] Fix recipes are described as guarded and non-destructive: cleanup is plan-only and nothing is pushed or deployed automatically. -- evidence: [README.md#L173-L176](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L173-L176) (`clm_59968ad4db375c2ae8c5e50fdfca5d79284e16f09f9636e309b52ebf0d73cbcf`)

## workflows (4 claim(s))

- [observation/documented] `viberaven init --agents all` writes bounded VIBERAVEN:START/END rule blocks into AGENTS.md, CLAUDE.md, GEMINI.md, Cursor rules, copilot instructions, and .viberaven context files, with a --dry-run preview. -- evidence: [README.md#L125-L128](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L125-L128), [README.md#L112-L115](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L112-L115), [README.md#L123-L123](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L123-L123), [README.md#L119-L121](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L119-L121) (`clm_6dec9a6b2ff27ceddced7415554e2e6da0215fee9dec2d407c408d31a24b628c`)
- [observation/documented] The installed agent rules teach a loop: run check, read .viberaven/, fix one gap, then re-check until gate.status equals "clear". -- evidence: [README.md#L130-L130](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L130-L130) (`clm_9c3ca1cd7146692bef11644694eed86f9578314e1b755ab03089d04ba32561f9`)
- [observation/documented] Repository development practice: AGENTS.md directs contributors to read the local-UI sources before changing behavior, keep changes scoped to the Studio path, and verify with focused package checks like typecheck, targeted tests, and build. -- evidence: [AGENTS.md#L26-L34](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/AGENTS.md#L26-L34) (`clm_917eedb49c66aa3eed20638de3b56803633d348156307f54f4fc3721ae8f287b`)
- [observation/documented] Repository development practice: AGENTS.md marks the old --agent-mode scan/pro-gate loop, old scan artifacts, private VSIX/editor work, and marketing surfaces as legacy to avoid unless explicitly requested. -- evidence: [AGENTS.md#L22-L22](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/AGENTS.md#L22-L22), [AGENTS.md#L14-L14](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/AGENTS.md#L14-L14), [AGENTS.md#L16-L20](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/AGENTS.md#L16-L20) (`clm_96eee0a27ae636d65c69b354349e8307c7965510cffe0fdee50b82ba14c1fca7`)

## skills-patterns (2 claim(s))

- [observation/documented] A six-skill skills.sh pack routes agents: viberaven (router), architecture-context, architecture-plan, what-broke, production-context, and go-live, installable via `skills add ohad6k/VibeRaven --skill viberaven`. -- evidence: [README.md#L145-L147](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L145-L147), [README.md#L136-L143](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L136-L143), [README.md#L134-L134](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L134-L134) (`clm_4c8cef09c2db3e11dc37a7c185ae2fd2219ce4880ddf4734aa921858c8d72b39`)
- [observation/documented] The repo doubles as an agent plugin (plugin.yaml, .claude-plugin/, .codex-plugin/, gemini-extension.json) exposing the six skills plus /viberaven-work, /viberaven-help, /viberaven-production-context, and /viberaven-launch commands. -- evidence: [README.md#L151-L151](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L151-L151) (`clm_91bd966f3045ba6b84d3532c858f5b7a4e43372a8803acced213d412c3914876`)

## interfaces (4 claim(s))

- [observation/documented] The product is invoked via npx as `viberaven` (Studio), `viberaven check` (terminal verdict), `viberaven fix`, `viberaven init --agents`, `viberaven doctor --agents`, and `viberaven audit --vercel-supabase`, with a `--strict` gate and `--mcp` mode. -- evidence: [README.md#L83-L85](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L83-L85), [README.md#L157-L159](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L157-L159), [README.md#L112-L115](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L112-L115), [README.md#L100-L104](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L100-L104), [README.md#L31-L33](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L31-L33), [README.md#L165-L167](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L165-L167), [README.md#L119-L121](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L119-L121) (`clm_3f27353aacc7bae583f8cc1176865eaf234c7a4ba50592a758e73ff4f83abdcf`)
- [observation/documented] `viberaven check` prints one line per finding with file:line evidence in artifacts and exits with code 1 when blockers exist. -- evidence: [README.md#L98-L98](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L98-L98) (`clm_c3b7c3ca324439612472f28348b31f0ba630ec60a2d3bf83a4f493912c44e7a6`)
- [observation/documented] The MCP server exposes tools including viberaven_check_readiness, viberaven_heal_apply, viberaven_verify, viberaven_audit, viberaven_provider_verify, and viberaven_validate_npm_package. -- evidence: [README.md#L161-L161](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L161-L161) (`clm_3f60bf2048d798af310564f39b659a5373ae702628a5efa6200e8d8320886cf8`)
- [observation/documented] The Studio browser UI offers agent chat, draggable provider cards and releases, an architecture map, a worktree view, and access-mode selection (ask/approve/full) that changes the actual agent command run. -- evidence: [README.md#L55-L60](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L55-L60), [README.md#L51-L51](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L51-L51), [README.md#L71-L77](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L71-L77) (`clm_efc27c64d267a89ecf576c272a9c1be6157ca0380f8db5fa81e9e3304be47c9e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The MCP tool viberaven_validate_npm_package is intended to be run before adding npm dependencies, suggesting the product offers dependency validation as part of its checks. -- evidence: [README.md#L161-L161](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L161-L161) (`clm_4fda252b71cfc4b110549a099e65ddbd0383175d29ddf59c3b31f2c1eed75f21`)

## limitations (1 claim(s))

- [observation/documented] Provider state is not inferred from repo code alone: analytics ingestion like PostHog is flagged for dashboard proof, and undetected providers are reported as "Not detected" rather than claiming repo evidence. -- evidence: [CHANGELOG.md#L17-L19](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/CHANGELOG.md#L17-L19), [README.md#L169-L169](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L169-L169) (`clm_034c6f43ea2e356be32619a1578c08bfb253d4ed33e7989723f5fed75224f34e`)

## relevance (1 claim(s))

- [observation/documented] VibeRaven targets developers of AI-built apps who want a pre-launch safety verdict on auth, RLS, webhooks, and deploy before real users hit the app. -- evidence: [README.md#L29-L29](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L29-L29), [README.md#L90-L92](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L90-L92) (`clm_ab5855f79fa29cbf9df4c3b58929120011e7536d7f4777845e4903b6316e9ca0`)

