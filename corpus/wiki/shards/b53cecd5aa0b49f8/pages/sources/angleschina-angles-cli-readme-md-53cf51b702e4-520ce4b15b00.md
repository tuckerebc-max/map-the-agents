---
access: public
aliases: []
claim_ids:
- clm_08de510213784991acff3a7ddfd2d26a1bf56dcfd722e924b8530389771b4057
- clm_137c25aa3f9fb19b5e4975bee4ee14fe17e75143af74ac53b8d4a4e5ef77ce0f
- clm_195c7c2307fe68aa29cb4f2fdea4ace41a70c590cac5f7e9760dcf3f4e0696be
- clm_2c1b59e55b0b0464c09ba4fd8aee189e3548ef39726834691ab3c5420394c13f
- clm_41f06f5f6f6ba41e44dff6c443f3e2f8072039013482bd8e80437725096bb408
- clm_4d4d807e141d1bd3d70afcd9edfa68e1404cea81c818e12ae4ee31dd82c2ce34
- clm_5980932033004b1dda83155dc8829566ea84800f8f8e395219b104048a36bfdd
- clm_96d7777be6e1d4b437721b14c8e7fe3f84ad6bc56be5017ef3269c91c739fe41
- clm_b6fc85dcc26bb20d936a881ee7d164ce4beef12e2b683f6c8008e14e2fdc4c92
- clm_d2dbc13f5fe6943e4a298d68ed6d0e8738d4d7469348c0164edfa72109819ae6
- clm_d6957ea3dca3e0cd895169a043349e6a546e9b7e24b0d1aabfe86c3b58f6efe0
- clm_fbafde5fea1c06a8cf683e708f50dd842c8a351975b61be09d7ce184f9b2c7c1
maturity: draft
page_id: pg_01ca5da827305c90add8520ce4b15b00
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aeaab04e90e45dc8b5b3007da6ae6ef3
title: angleschina/angles-cli/README.md @ 53cf51b702e4
updated_at: '2026-09-14T03:35:15Z'
---

# angleschina/angles-cli/README.md @ 53cf51b702e4

<!-- rcw:begin owner=source:src_aeaab04e90e45dc8b5b3007da6ae6ef3 block=evidence -->
- angles serve starts an embedded axum HTTP server on 127.0.0.1:8080 exposing /health, /api/config, /api/providers, and /api/chat for a browser-based web console. [@claim:clm_08de510213784991acff3a7ddfd2d26a1bf56dcfd722e924b8530389771b4057]
- Repository development practice: the repo includes a release workflow (.github/workflows/release.yml), a Cross.toml for cross-compilation, and a docs/ directory published as a GitHub Pages site. [@claim:clm_137c25aa3f9fb19b5e4975bee4ee14fe17e75143af74ac53b8d4a4e5ef77ce0f]
- The CLI offers subcommands including an interactive default session (angles), angles exec for one-shot runs, angles plan, angles serve, angles gateway, angles config, angles doctor, and angles help. [@claim:clm_195c7c2307fe68aa29cb4f2fdea4ace41a70c590cac5f7e9760dcf3f4e0696be]
- The tool ships as a single static ~1.6 MB Rust binary with zero runtime dependencies (no Node, Python, or dynamic libc), aimed at constrained environments like ARM64 SBCs, rootless containers, and iSH. [@claim:clm_2c1b59e55b0b0464c09ba4fd8aee189e3548ef39726834691ab3c5420394c13f]
- All agent capabilities are exposed as curated angles-* commands rather than free-form shell improvisation, binding the model to a deterministic tool set. [@claim:clm_41f06f5f6f6ba41e44dff6c443f3e2f8072039013482bd8e80437725096bb408]
- Configuration persists at ~/.angles/config.json with fields for language, provider, base_url, wire_api, model, max_tokens, daily token budget, agent persona, search engine, and approval policy; API keys can come from ANGLES_API_KEY and are not sent through a relay. [@claim:clm_4d4d807e141d1bd3d70afcd9edfa68e1404cea81c818e12ae4ee31dd82c2ce34]
- The 13 KB instructions.txt system-prompt template uses handlebars-style {{variable}} injection for config values, persona, and architecture, and directs the agent to emit operation plans with fixed verbs before non-trivial tasks. [@claim:clm_5980932033004b1dda83155dc8829566ea84800f8f8e395219b104048a36bfdd]
- The codebase is organized into Rust modules including main.rs (entry/routing), cli.rs, config.rs, provider.rs, gateway.rs, instructions.rs, api.rs, search.rs, server.rs, and tools.rs, plus instructions.txt, providers.toml, and docs/. [@claim:clm_96d7777be6e1d4b437721b14c8e7fe3f84ad6bc56be5017ef3269c91c739fe41]
- A provider registry (provider.rs plus providers.toml) maps 11 providers to three wire protocols — OpenAI Chat Completions, Anthropic Messages, or Gemini Native — normalizing streaming and tool calls so the rest of the code is provider-agnostic. [@claim:clm_b6fc85dcc26bb20d936a881ee7d164ce4beef12e2b683f6c8008e14e2fdc4c92]
- The conversation loop lives in api.rs, an OpenAI/Anthropic/Gemini client with streaming and a tool-calling loop that resolves angles-* commands to implementations in tools.rs. [@claim:clm_d2dbc13f5fe6943e4a298d68ed6d0e8738d4d7469348c0164edfa72109819ae6]
- The safety model: reads need no approval, writes follow the configured approval policy, and deletions or dangerous operations always require user confirmation. [@claim:clm_d6957ea3dca3e0cd895169a043349e6a546e9b7e24b0d1aabfe86c3b58f6efe0]
- Repository development practice: building from source uses cargo build --release with Makefile targets for Linux ARM64/x64 and macOS ARM64 cross-compilation, and GitHub Actions produces prebuilt binaries for all 5 platforms on every tag push. [@claim:clm_fbafde5fea1c06a8cf683e708f50dd842c8a351975b61be09d7ce184f9b2c7c1]
<!-- rcw:end owner=source:src_aeaab04e90e45dc8b5b3007da6ae6ef3 block=evidence -->

## Researcher notes

