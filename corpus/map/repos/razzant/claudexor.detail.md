# razzant/claudexor -- full detail

[Back to orientation](claudexor.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/razzant/claudexor/87f08d28cf3366a27e099e05d489cf4631255c65/ffa685ceb1e6d91a.json](../../../wiki/dossiers/razzant/claudexor/87f08d28cf3366a27e099e05d489cf4631255c65/ffa685ceb1e6d91a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The monorepo splits packages/schema (contracts and generated JSON Schema), harness-* adapters, workspace (Git/directory envelopes), orchestrator (canonical mode pipelines), and review/arbitration/synthesis/budget packages. -- evidence: [README.md#L798-L807](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L798-L807) (`clm_e570d7b17b9d88894d3230dfc67c4d1fced1e9aded22b638681a1b3a508d9363`)

## design-choices (2 claim(s))

- [observation/documented] The product is local-first: everything runs on the user's machine, files are the source of truth, and the README states there is no telemetry. -- evidence: [README.md#L22-L32](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L22-L32) (`clm_82d8c8082968192cff8bc2d1973c3f0392484bf2d0594c05a0978fc069470640`)
- [observation/documented] Cost accounting is typed: paid budgets are explicit via --max-usd with zero as a real cap, unknown cost is never reported as $0, and runs can end cost_unverifiable or budget_overshoot. -- evidence: [README.md#L549-L562](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L549-L562) (`clm_d85b7930f41e70ca2aded742293af598331bce9a603873cfbcfca875f9e16088`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors build with pnpm install --frozen-lockfile and pnpm build, then run typecheck, test, schema:gen with a generated-diff check, docs:check, and knip as gates. -- evidence: [README.md#L827-L836](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L827-L836) (`clm_ad2dff2d84b335eb4f7eff67ce8f546c835e0d16c5f42cc29097890abd4f63be`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Claudexor exposes a CLI, a loopback HTTP/SSE control API scoped to /v2 with POST /v2/handshake negotiation, MCP, ACP, and a macOS app as thin surfaces over the daemon. -- evidence: [README.md#L690-L693](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L690-L693), [README.md#L798-L807](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L798-L807), [README.md#L615-L623](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L615-L623) (`clm_af2858ff9d218bc0cd948fea8072c18afb3e3502a408f43058d8204a7413a725`)
- [observation/documented] Retired mode ids and verbs (audit, best_of_n, explore, orchestrate, etc.) hard-error with the new spelling rather than silently aliasing; unknown flags and invalid flag values exit with code 2. -- evidence: [README.md#L259-L267](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L259-L267), [README.md#L34-L36](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L34-L36), [README.md#L404-L410](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L404-L410) (`clm_a39f962ad548fdcf53b8eef7ca576ca0ca85389d77dcefe5153c2ce3948092be`)

## memory-state (1 claim(s))

- [observation/documented] Read-only ask/plan turns resume the routed harness's native CLI session in a durable per-lane home; lane switches hydrate with a bounded continuation packet written to context/THREAD.md and disclosed via a typed session.continuity event. -- evidence: [README.md#L427-L439](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L427-L439), [README.md#L412-L425](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L412-L425) (`clm_85b684cefe7b1f6b226965d2a9dd5af31985b68cc7d2b0eb6aa4b2f500aa84e7`)

## orchestration (2 claim(s))

- [observation/documented] Canonical modes are ask (read-only, with --deep-scan multi-scout research), plan (with --council parallel multi-harness drafting merged into one plan), and agent (with --n best-of races, --attempts repair loops, --until-clean, and --delegate). -- evidence: [README.md#L339-L353](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L339-L353) (`clm_2fa9ca3b579f0d06808d44370250f41ebb4d5cf4da73009235b38eba9b13bcf6`)
- [observation/documented] The --delegate flag injects a scoped MCP belt exposing only ask/plan/run/best-of/status/result tools, with nesting depth 1, a default cap of 8 sub-runs per parent, and shared daemon-owned budget authority; only adapters declaring mcp_injection (claude, codex, cursor) can host it. -- evidence: [README.md#L357-L379](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L357-L379) (`clm_0810525c4f98fb835b0c70c6eb56e5b0738a42da9913e318c79bbca598ac2b77`)

## tools-permissions (1 claim(s))

- [observation/documented] Protected paths configured in .claudexor/config.yaml pause apply for a human decision; --allow-protected-path covers only engine-derived gate/test paths and cannot suppress project rules, and mutating turns on such projects are promoted one-way to an isolated worktree. -- evidence: [README.md#L326-L333](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L326-L333), [README.md#L300-L316](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L300-L316) (`clm_bb1ab7016a50d34c290b9ae46b34ea7ccd6e138e086fa52fce55a6e40a231f89`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Node.js >= 20.19, pnpm via corepack, Git for Git-backed worktrees, and at least one logged-in vendor CLI (codex, claude, cursor-agent, opencode, or agy) or a provider API key; the desktop app requires macOS while the CLI/daemon also run on Linux. -- evidence: [README.md#L90-L102](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L90-L102) (`clm_c1ef2f2c1496e9431403bbc215544bd8b2183f9bfa98dde0acf90dce1378fb55`)

## limitations (1 claim(s))

- [observation/documented] Live subscription-quota tracking and auto-rotation on typed vendor limits cover only harnesses with a vendor usage source (Antigravity, Claude, Codex); Cursor has none yet, and the portable Copilot plugin does not support Windows. -- evidence: [README.md#L22-L32](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L22-L32), [README.md#L755-L760](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L755-L760) (`clm_402693a36a8723f2b7ebcf0ceaf4da9991dd76d46155796b5afd94b555987739`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

