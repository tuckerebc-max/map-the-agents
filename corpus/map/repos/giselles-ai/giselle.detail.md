# giselles-ai/giselle -- full detail

[Back to orientation](giselle.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/giselles-ai/giselle/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/7d22789bbb7ad9c3.json](../../../wiki/dossiers/giselles-ai/giselle/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/7d22789bbb7ad9c3.json)

## specifications (2 claim(s))

- [observation/documented] Giselle is described as an open-source AI for agentic workflows enabling human-AI collaboration, positioned as an AI agent studio for product delivery. -- evidence: [README.md#L33-L33](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L33-L33), [README.md#L10-L10](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L10-L10) (`clm_a397ac3eebaf6f69522daa2644358902ebe60f2cfe3d3e2cd04808a5ae24a032`)
- [observation/documented] The project is licensed under Apache License Version 2.0, with third-party package licenses documented separately. -- evidence: [README.md#L128-L128](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L128-L128), [README.md#L130-L130](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L130-L130) (`clm_7c34b727992804b238658c0cbb43004479b4e1e0738db4121476609212066617`)

## components (1 claim(s))

- [observation/documented] Advertised features include GitHub AI operations, a drag-and-drop visual agent builder, multi-model composition, and a knowledge store with GitHub vector store integration. -- evidence: [README.md#L76-L81](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L76-L81) (`clm_38aba3dcb5dad85f9cfaf7e31956c8c083556a52cc5cd75c8d18035320270f73`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: local setup involves cloning, pnpm install, creating .env.local with an API key, and starting the dev server with pnpm turbo dev on port 3000. -- evidence: [README.md#L53-L53](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L53-L53), [README.md#L50-L50](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L50-L50), [README.md#L59-L59](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L59-L59), [README.md#L47-L47](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L47-L47), [README.md#L56-L57](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L56-L57), [README.md#L43-L44](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L43-L44) (`clm_4275190ae9c7a2fa9f707adfc322091bcfb7822596acf91da3b10a0b79f43c97`)
- [observation/documented] Repository development practice: after every code change contributors run pnpm format, build-sdk, check-types, tidy, and test in order, then update the .continuity per-branch ledger. -- evidence: [AGENTS.md#L125-L131](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/AGENTS.md#L125-L131) (`clm_4de8a7e1fcc5d8fcb4858097a717051a9839936e7aa515fc552afd8acc230479`)
- [observation/documented] Repository development practice: PRs should be meaningful minimum units, with roughly 500 lines suggested as a wrap-up point and 1000 lines as a maximum threshold; feature flags protect unreleased features. -- evidence: [AGENTS.md#L310-L310](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/AGENTS.md#L310-L310), [AGENTS.md#L150-L153](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/AGENTS.md#L150-L153) (`clm_ca937638a1bad53963bca30a0416ef7750d718699d1c43c0a71cd7a6076f0693`)
- [observation/documented] Repository development practice: a two-layer continuity system keeps a low-churn CONTINUITY.md snapshot plus high-churn per-branch ledgers in .continuity/ that AI assistants must locate and update per request. -- evidence: [AGENTS.md#L395-L397](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/AGENTS.md#L395-L397), [AGENTS.md#L400-L408](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/AGENTS.md#L400-L408) (`clm_fb1bfd42fa778168d0d6958b2a39efa4a5cb8cc7c81bbe1f0c2087a0f1771b14`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running Giselle locally requires at least one AI provider API key, with OpenAI, Anthropic, and Google AI listed as supported providers. -- evidence: [README.md#L61-L61](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L61-L61) (`clm_3711e4941978bca9141534343174dbf449ed4e428938ac2ec75875dc15fc2f10`)

## limitations (1 claim(s))

- [observation/documented] Team Collaboration and Template Hub features are explicitly marked as in development in the README feature list. -- evidence: [README.md#L76-L81](https://github.com/giselles-ai/giselle/blob/7dca22434e3dfcd4cf4b32aec20d4d7813a06fb5/README.md#L76-L81) (`clm_b2c00a40e97faa9d205359046ebf0e030b1a9eac7520a13d922bb0d6aa81fc9e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

