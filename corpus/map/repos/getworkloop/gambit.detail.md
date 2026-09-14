# getworkloop/gambit -- full detail

[Back to orientation](gambit.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/getworkloop/gambit/d413df73f7262f7eb9dee56721249caeb8e759a2/8445de880a1b3f7a.json](../../../wiki/dossiers/getworkloop/gambit/d413df73f7262f7eb9dee56721249caeb8e759a2/8445de880a1b3f7a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Agent definitions use a Markdown 'deck' file format with TOML-like frontmatter (label, modelParams, actions); the README notes 'deck' remains the exact implementation term. -- evidence: [README.md#L397-L399](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L397-L399), [README.md#L440-L448](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L440-L448), [README.md#L150-L152](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L150-L152), [README.md#L401-L404](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L401-L404) (`clm_3ccf856f8ed99b98df277c9f281ed99950ad24e0b00563408f16459f20a264a4`)
- [observation/documented] Compute agents are TypeScript decks using Zod contextSchema/responseSchema and a run() function, with no model call; child actions are referenced by path in deck frontmatter. -- evidence: [README.md#L417-L420](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L417-L420), [README.md#L440-L448](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L440-L448), [README.md#L422-L430](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L422-L430) (`clm_a5e0e9041b1c820f90f64accaa12a7d7ca839e20c6f5690e8c14f8ba312efff1`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: docs/external is designated external-only, excluding internal debates, open risks, and execution details, while internal doctrine lives elsewhere. -- evidence: [docs/external/ABOUT.md#L12-L13](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/external/ABOUT.md#L12-L13), [docs/README.md#L6-L7](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/README.md#L6-L7), [docs/README.md#L3-L4](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/README.md#L3-L4) (`clm_af78773d5843c164dab8b3dfe98026d231e5d8886944b87d5e4cbdb393741ca1`)
- [observation/documented] Repository development practice: docs/posts/ is a chronological digest of notable updates, with each post expected to cross-link back to the internal execution notes holding goals, owners, and decision logs. -- evidence: [docs/posts/2026-01-19-introducing-posts.md#L20-L23](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/posts/2026-01-19-introducing-posts.md#L20-L23), [docs/posts/2026-01-19-introducing-posts.md#L7-L10](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/posts/2026-01-19-introducing-posts.md#L7-L10), [docs/posts/2026-01-19-introducing-posts.md#L33-L36](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/posts/2026-01-19-introducing-posts.md#L33-L36) (`clm_447d1f016052a7c8af76b62444c44476de53f282f11b5056dcee2d4d665348af`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI offers commands including run (one-shot with --context/--message), repl, chat, scenario, and grade, runnable via npx without installation. -- evidence: [README.md#L210-L212](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L210-L212), [README.md#L162-L164](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L162-L164), [README.md#L204-L206](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L204-L206), [README.md#L171-L173](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L171-L173), [README.md#L177-L179](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L177-L179), [README.md#L150-L152](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L150-L152) (`clm_7d1636da56a9b3727319591ef16797afd4720c58a7ade1783d4153ad4c8d2873`)
- [observation/documented] The `--context` flag replaced the older `--init` flag, which remains accepted as a deprecated alias for script compatibility. -- evidence: [README.md#L166-L167](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L166-L167) (`clm_d2d37cffc8967c56ef7d6769d876be44f2cfcd42366adec847f58261efcdb422`)
- [observation/documented] The library exports defineDeck and defineCard helpers from JSR for TypeScript agent definitions, and runDeckResponses is described as the canonical Gambit 1.0 runtime entrypoint returning structured Responses output. -- evidence: [README.md#L307-L309](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L307-L309), [README.md#L328-L332](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L328-L332) (`clm_6aea9f97532c1dfbd65f414f1573e3e4b9dcc067ca23428779a09659508686d8`)
- [observation/documented] The simulator package @bolt-foundry/gambit-simulator serves a local Debug UI with /test, /grade, and /verify routes (verify enabled by default, disable via GAMBIT_SIMULATOR_VERIFY_TAB=0). -- evidence: [README.md#L268-L272](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L268-L272), [README.md#L245-L246](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L245-L246) (`clm_b28cf857ea9828016e2ea2676da8e6be751f871943eded74869b89a75cf4aec2`)

## memory-state (1 claim(s))

- [observation/documented] Sessions support persisted state and JSONL traces via --state and --trace flags; the Debug UI stores local-first state (sessions, traces, notes) under .gambit/. -- evidence: [README.md#L222-L224](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L222-L224), [README.md#L281-L284](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L281-L284), [README.md#L177-L179](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L177-L179) (`clm_807729aedb2b4ee2bc982b74ffe9849a0851c0f186345df34e1ca49cded7245c`)

## orchestration (1 claim(s))

- [observation/documented] Compute decks can call child agent definitions from code via ctx.spawnAndWait({ path, input }) and emit structured trace events with ctx.log(...). -- evidence: [README.md#L321-L324](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L321-L324) (`clm_d65aa4a8fa25fdf42de60d1825a60f1e87972ad4e7e04fae4959dc37dbf099c1`)

## tools-permissions (2 claim(s))

- [observation/documented] CLI commands that execute decks default to worker sandbox execution; --no-worker-sandbox (or --legacy-exec) forces legacy in-process execution, and gambit.toml can set worker_sandbox equivalently. -- evidence: [README.md#L228-L238](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L228-L238), [README.md#L240-L241](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L240-L241) (`clm_bb36d30ea3ac72aaa88a61a1666fe104497b94c7a329859a6ec85c005396b83d`)
- [observation/documented] Runtime tools can be supplied via Markdown/TOML files with [[tools]] entries (name, description, optional inputSchema and action), where action bindings run Gambit agent definitions with tool arguments as context. -- evidence: [README.md#L189-L189](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L189-L189), [README.md#L191-L194](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L191-L194), [README.md#L196-L200](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L196-L200) (`clm_e6b03fb9a47137a804801fe92d644d2dace36c74c1447e119c6c5ec481fd91e8`)

## evaluation (1 claim(s))

- [observation/documented] Gambit's product purpose is agent evaluation: generating scenarios, validating scenario quality, running agents against suites, grading behavior from transcripts/traces/typed outputs, and turning failures into regression checks. -- evidence: [README.md#L67-L76](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L67-L76), [docs/external/README.md#L6-L9](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/external/README.md#L6-L9), [README.md#L6-L8](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L6-L8) (`clm_8eeec2927abf1419eb755a09a923144eacf6443a7973ce0df53e38d72ec18dbd`)

## dependencies (1 claim(s))

- [observation/documented] Quickstart requires Node.js 18+ and an OPENROUTER_API_KEY (with optional OPENROUTER_BASE_URL for proxied OpenRouter-style APIs); a Deno path via jsr:@bolt-foundry/gambit is also documented. -- evidence: [README.md#L504-L507](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L504-L507), [README.md#L18-L19](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L18-L19) (`clm_d0354c65b218e32d4f12a729a8c709ca12f3f39d679ee915f2b3e7ba0627c10c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

