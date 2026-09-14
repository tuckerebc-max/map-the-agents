# swadhinbiswas/mervelas -- full detail

[Back to orientation](mervelas.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swadhinbiswas/mervelas/1aa7b039e52186f646d2bc472e4dbbe68e812625/0619a7e59a3a7e60.json](../../../wiki/dossiers/swadhinbiswas/mervelas/1aa7b039e52186f646d2bc472e4dbbe68e812625/0619a7e59a3a7e60.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [inference/documented] The CLI appears to render its terminal UI with a custom React Ink abstraction compiled natively via Bun, per the README's performance description. -- evidence: [README.md#L30-L33](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L30-L33) (`clm_e14eb98e5411580c58a750a3228009d45e7db8a1668de946dbc08d33572c61ff`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors must not import ink directly from npm; UI layout components must be routed through src/ink.ts. -- evidence: [README.md#L132-L134](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L132-L134) (`clm_a802b606acef22cec104a1c107a5cfa3e882911e5590343a4721e6e452d5d78f`)
- [observation/documented] Repository development practice: contributors should run strict type checking via npm run typecheck (tsc --noEmit) and use lazy load: () => import(...) for tools and execute loops. -- evidence: [README.md#L132-L134](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L132-L134) (`clm_0284db2eace540db761d84acc05a4141fc6fe2b1208ce7278593e7a1dd698f76`)
- [observation/documented] Repository development practice: setup involves cloning the repo, running bun install, building with bun run scripts/build.ts, and executing node dist/cli.mjs. -- evidence: [README.md#L88-L89](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L88-L89), [README.md#L82-L82](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L82-L82), [README.md#L78-L79](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L78-L79), [README.md#L85-L85](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L85-L85) (`clm_157163d6e2a0bf03f37a27f107ca1b9cc28e836ce19c2205f43323e6394392e2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes slash commands including /config, /context, /agents, /mcp, /status, and /login for provider setup, context inspection, agent switching, and MCP integration. -- evidence: [README.md#L101-L106](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L101-L106) (`clm_7092a80ba1c4cc334d3ecc3e7d525de41164a25c74c521855b64de82ba074ad2`)
- [observation/documented] Providers can be configured via environment variables such as MERVELAS_API_PROVIDER, OPENAI_API_KEY, and OPENROUTER_API_KEY for headless and CI setups. -- evidence: [README.md#L121-L124](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L121-L124), [README.md#L112-L112](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L112-L112), [README.md#L116-L118](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L116-L118) (`clm_95b9156179e814aefde6cc13aca699f4f54ec6bd9108efd3eedab49870fa5ce1`)
- [observation/documented] A recent fix changed the OpenAI-compatible tools payload to nest a function object in the tools array and removed the strict field for third-party model compatibility. -- evidence: [fix-commit.md#L4-L4](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/fix-commit.md#L4-L4), [fix-commit.md#L1-L2](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/fix-commit.md#L1-L2) (`clm_1e9679429e4e5889ae6f571f04a0df2c81a74c3a5300c41138228b3e30236d64`)

## memory-state (1 claim(s))

- [observation/documented] Conversational session history is written locally to ~/.mervelas/projects/ in JSONL format, per the README's privacy description. -- evidence: [README.md#L30-L33](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L30-L33) (`clm_4866cac7d64689a937736a0ebb37f2c6afc0ee226be0529bb2a4819154da7d56`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The project is built with Bun and requires Bun to compile and run locally. -- evidence: [README.md#L13-L14](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L13-L14), [README.md#L72-L72](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L72-L72) (`clm_2bede27fcc5fb4d408655c3fddaadae73ba8b8a35100bddeb4bf4486b94460d6`)
- [observation/documented] The README claims out-of-the-box support for OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, and locally hosted models. -- evidence: [README.md#L30-L33](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L30-L33) (`clm_0040fa924c2c2a72c9248576d56129331e5e5823dd9efe1e1e587cdc0815dc19`)
- [observation/documented] The repository includes a list of NVIDIA NIM model identifiers, suggesting curated support for many NVIDIA-hosted models. -- evidence: [nvidia_models.txt#L1-L188](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/nvidia_models.txt#L1-L188) (`clm_ed1bb94f81850e64485092a5b52f60f0a4497f8252e89cc828494a997c7a084f`)

## limitations (1 claim(s))

- [observation/documented] The project is in active development, has not been published to NPM, and users must build it locally and supply their own API keys. -- evidence: [README.md#L16-L16](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L16-L16) (`clm_bd9eaced431533c64c0f0dd5dede6f876241bbc2545e4bfbbf2d38dbd44b9caf`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

