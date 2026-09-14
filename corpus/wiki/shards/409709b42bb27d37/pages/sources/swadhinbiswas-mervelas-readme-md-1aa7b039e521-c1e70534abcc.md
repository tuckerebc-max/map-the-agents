---
access: public
aliases: []
claim_ids:
- clm_0040fa924c2c2a72c9248576d56129331e5e5823dd9efe1e1e587cdc0815dc19
- clm_0284db2eace540db761d84acc05a4141fc6fe2b1208ce7278593e7a1dd698f76
- clm_157163d6e2a0bf03f37a27f107ca1b9cc28e836ce19c2205f43323e6394392e2
- clm_2bede27fcc5fb4d408655c3fddaadae73ba8b8a35100bddeb4bf4486b94460d6
- clm_4866cac7d64689a937736a0ebb37f2c6afc0ee226be0529bb2a4819154da7d56
- clm_7092a80ba1c4cc334d3ecc3e7d525de41164a25c74c521855b64de82ba074ad2
- clm_95b9156179e814aefde6cc13aca699f4f54ec6bd9108efd3eedab49870fa5ce1
- clm_a802b606acef22cec104a1c107a5cfa3e882911e5590343a4721e6e452d5d78f
- clm_bd9eaced431533c64c0f0dd5dede6f876241bbc2545e4bfbbf2d38dbd44b9caf
- clm_e14eb98e5411580c58a750a3228009d45e7db8a1668de946dbc08d33572c61ff
maturity: draft
page_id: pg_d6925cf4bc2e5841b846c1e70534abcc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_adb72f8916385d3c98252033e69e2b30
title: swadhinbiswas/Mervelas/README.md @ 1aa7b039e521
updated_at: '2026-09-14T03:16:47Z'
---

# swadhinbiswas/Mervelas/README.md @ 1aa7b039e521

<!-- rcw:begin owner=source:src_adb72f8916385d3c98252033e69e2b30 block=evidence -->
- The README claims out-of-the-box support for OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, and locally hosted models. [@claim:clm_0040fa924c2c2a72c9248576d56129331e5e5823dd9efe1e1e587cdc0815dc19]
- Repository development practice: contributors should run strict type checking via npm run typecheck (tsc --noEmit) and use lazy load: () => import(...) for tools and execute loops. [@claim:clm_0284db2eace540db761d84acc05a4141fc6fe2b1208ce7278593e7a1dd698f76]
- Repository development practice: setup involves cloning the repo, running bun install, building with bun run scripts/build.ts, and executing node dist/cli.mjs. [@claim:clm_157163d6e2a0bf03f37a27f107ca1b9cc28e836ce19c2205f43323e6394392e2]
- The project is built with Bun and requires Bun to compile and run locally. [@claim:clm_2bede27fcc5fb4d408655c3fddaadae73ba8b8a35100bddeb4bf4486b94460d6]
- Conversational session history is written locally to ~/.mervelas/projects/ in JSONL format, per the README's privacy description. [@claim:clm_4866cac7d64689a937736a0ebb37f2c6afc0ee226be0529bb2a4819154da7d56]
- The CLI exposes slash commands including /config, /context, /agents, /mcp, /status, and /login for provider setup, context inspection, agent switching, and MCP integration. [@claim:clm_7092a80ba1c4cc334d3ecc3e7d525de41164a25c74c521855b64de82ba074ad2]
- Providers can be configured via environment variables such as MERVELAS_API_PROVIDER, OPENAI_API_KEY, and OPENROUTER_API_KEY for headless and CI setups. [@claim:clm_95b9156179e814aefde6cc13aca699f4f54ec6bd9108efd3eedab49870fa5ce1]
- Repository development practice: contributors must not import ink directly from npm; UI layout components must be routed through src/ink.ts. [@claim:clm_a802b606acef22cec104a1c107a5cfa3e882911e5590343a4721e6e452d5d78f]
- The project is in active development, has not been published to NPM, and users must build it locally and supply their own API keys. [@claim:clm_bd9eaced431533c64c0f0dd5dede6f876241bbc2545e4bfbbf2d38dbd44b9caf]
- The CLI appears to render its terminal UI with a custom React Ink abstraction compiled natively via Bun, per the README's performance description. [@claim:clm_e14eb98e5411580c58a750a3228009d45e7db8a1668de946dbc08d33572c61ff]
<!-- rcw:end owner=source:src_adb72f8916385d3c98252033e69e2b30 block=evidence -->

## Researcher notes

