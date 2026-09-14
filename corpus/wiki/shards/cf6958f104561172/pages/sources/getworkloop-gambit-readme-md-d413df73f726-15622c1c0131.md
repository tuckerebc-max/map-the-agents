---
access: public
aliases: []
claim_ids:
- clm_3ccf856f8ed99b98df277c9f281ed99950ad24e0b00563408f16459f20a264a4
- clm_6aea9f97532c1dfbd65f414f1573e3e4b9dcc067ca23428779a09659508686d8
- clm_7d1636da56a9b3727319591ef16797afd4720c58a7ade1783d4153ad4c8d2873
- clm_807729aedb2b4ee2bc982b74ffe9849a0851c0f186345df34e1ca49cded7245c
- clm_8eeec2927abf1419eb755a09a923144eacf6443a7973ce0df53e38d72ec18dbd
- clm_a5e0e9041b1c820f90f64accaa12a7d7ca839e20c6f5690e8c14f8ba312efff1
- clm_b28cf857ea9828016e2ea2676da8e6be751f871943eded74869b89a75cf4aec2
- clm_bb36d30ea3ac72aaa88a61a1666fe104497b94c7a329859a6ec85c005396b83d
- clm_d0354c65b218e32d4f12a729a8c709ca12f3f39d679ee915f2b3e7ba0627c10c
- clm_d2d37cffc8967c56ef7d6769d876be44f2cfcd42366adec847f58261efcdb422
- clm_d65aa4a8fa25fdf42de60d1825a60f1e87972ad4e7e04fae4959dc37dbf099c1
- clm_e6b03fb9a47137a804801fe92d644d2dace36c74c1447e119c6c5ec481fd91e8
maturity: draft
page_id: pg_cb6f991aa76258fd930715622c1c0131
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4df85a562e185678b53099f553b07ff1
title: getworkloop/gambit/README.md @ d413df73f726
updated_at: '2026-09-14T03:53:40Z'
---

# getworkloop/gambit/README.md @ d413df73f726

<!-- rcw:begin owner=source:src_4df85a562e185678b53099f553b07ff1 block=evidence -->
- Agent definitions use a Markdown 'deck' file format with TOML-like frontmatter (label, modelParams, actions); the README notes 'deck' remains the exact implementation term. [@claim:clm_3ccf856f8ed99b98df277c9f281ed99950ad24e0b00563408f16459f20a264a4]
- The library exports defineDeck and defineCard helpers from JSR for TypeScript agent definitions, and runDeckResponses is described as the canonical Gambit 1.0 runtime entrypoint returning structured Responses output. [@claim:clm_6aea9f97532c1dfbd65f414f1573e3e4b9dcc067ca23428779a09659508686d8]
- The CLI offers commands including run (one-shot with --context/--message), repl, chat, scenario, and grade, runnable via npx without installation. [@claim:clm_7d1636da56a9b3727319591ef16797afd4720c58a7ade1783d4153ad4c8d2873]
- Sessions support persisted state and JSONL traces via --state and --trace flags; the Debug UI stores local-first state (sessions, traces, notes) under .gambit/. [@claim:clm_807729aedb2b4ee2bc982b74ffe9849a0851c0f186345df34e1ca49cded7245c]
- Gambit's product purpose is agent evaluation: generating scenarios, validating scenario quality, running agents against suites, grading behavior from transcripts/traces/typed outputs, and turning failures into regression checks. [@claim:clm_8eeec2927abf1419eb755a09a923144eacf6443a7973ce0df53e38d72ec18dbd]
- Compute agents are TypeScript decks using Zod contextSchema/responseSchema and a run() function, with no model call; child actions are referenced by path in deck frontmatter. [@claim:clm_a5e0e9041b1c820f90f64accaa12a7d7ca839e20c6f5690e8c14f8ba312efff1]
- The simulator package @bolt-foundry/gambit-simulator serves a local Debug UI with /test, /grade, and /verify routes (verify enabled by default, disable via GAMBIT_SIMULATOR_VERIFY_TAB=0). [@claim:clm_b28cf857ea9828016e2ea2676da8e6be751f871943eded74869b89a75cf4aec2]
- CLI commands that execute decks default to worker sandbox execution; --no-worker-sandbox (or --legacy-exec) forces legacy in-process execution, and gambit.toml can set worker_sandbox equivalently. [@claim:clm_bb36d30ea3ac72aaa88a61a1666fe104497b94c7a329859a6ec85c005396b83d]
- Quickstart requires Node.js 18+ and an OPENROUTER_API_KEY (with optional OPENROUTER_BASE_URL for proxied OpenRouter-style APIs); a Deno path via jsr:@bolt-foundry/gambit is also documented. [@claim:clm_d0354c65b218e32d4f12a729a8c709ca12f3f39d679ee915f2b3e7ba0627c10c]
- The `--context` flag replaced the older `--init` flag, which remains accepted as a deprecated alias for script compatibility. [@claim:clm_d2d37cffc8967c56ef7d6769d876be44f2cfcd42366adec847f58261efcdb422]
- Compute decks can call child agent definitions from code via ctx.spawnAndWait({ path, input }) and emit structured trace events with ctx.log(...). [@claim:clm_d65aa4a8fa25fdf42de60d1825a60f1e87972ad4e7e04fae4959dc37dbf099c1]
- Runtime tools can be supplied via Markdown/TOML files with [[tools]] entries (name, description, optional inputSchema and action), where action bindings run Gambit agent definitions with tool arguments as context. [@claim:clm_e6b03fb9a47137a804801fe92d644d2dace36c74c1447e119c6c5ec481fd91e8]
<!-- rcw:end owner=source:src_4df85a562e185678b53099f553b07ff1 block=evidence -->

## Researcher notes

