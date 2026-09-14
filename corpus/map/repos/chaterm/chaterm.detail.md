# chaterm/chaterm -- full detail

[Back to orientation](chaterm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/chaterm/chaterm/1ca378cb7eda1371269034d01d9556f911a1de58/64cc986d19eee1ed.json](../../../wiki/dossiers/chaterm/chaterm/1ca378cb7eda1371269034d01d9556f911a1de58/64cc986d19eee1ed.json)

## specifications (1 claim(s))

- [observation/documented] Chaterm is described as an AI-native terminal for infrastructure and cloud resource management, letting engineers perform tasks like deployment and troubleshooting via natural language. -- evidence: [README.md#L51-L51](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L51-L51) (`clm_95a4686d2b5ff45cf122b813227919d7019167f9714d232cd4349b1fc544a2de`)

## components (1 claim(s))

- [observation/documented] The project structure includes an Electron main process, preload scripts, a Vue.js renderer, scripts, resources, tests, and docs directories. -- evidence: [CONTRIBUTING_zh.md#L72-L82](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L72-L82) (`clm_a78f09f49530523a8a7f742d65b83a29b4d00c688de46c77b8cbe77d2a69300c`)

## design-choices (1 claim(s))

- [observation/documented] Knowledge retrieval combines vector and keyword search using RRF fusion into a unified ranking, with visible embedding, hybrid search, and reranking stages. -- evidence: [README.md#L100-L100](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L100-L100), [README.md#L98-L98](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L98-L98) (`clm_dea4d502b43f17ab330ed718c5b4ea42944b354faa906807dfa1a3e04afda5ac`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork the repo, branch from main, and submit PRs that require approval from at least one maintainer before merging. -- evidence: [CONTRIBUTING_zh.md#L18-L23](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L18-L23) (`clm_e84f28194cc92622bfc81ff3c0263019803d26535915967c1f8680a27840f772`)
- [observation/documented] Repository development practice: conventional commit message formats (feat, fix, docs, refactor, test) are required, with ESLint, Prettier, and TypeScript recommended for code style. -- evidence: [CONTRIBUTING_zh.md#L88-L90](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L88-L90), [CONTRIBUTING_zh.md#L109-L115](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L109-L115), [CONTRIBUTING_zh.md#L107-L107](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L107-L107) (`clm_040524f28ef577b0fb44702f800c2163d6541316712c0dc646b260d13bb1a6fa`)

## skills-patterns (1 claim(s))

- [observation/documented] Agent Skills encapsulate complex maintenance procedures into reusable AI skills for structured, reliable automated execution. -- evidence: [README.md#L104-L104](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L104-L104) (`clm_b71903cc7194bf5d4544131350e9c972687ea2ed6f0444970de73485be117e7c`)

## interfaces (2 claim(s))

- [observation/documented] A database workspace supports connecting to MySQL, PostgreSQL, SQLite, and Oracle for schema browsing, queries, DDL inspection, row editing, and database-aware AI assistance. -- evidence: [README.md#L116-L116](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L116-L116) (`clm_59e9906f04d4363da295ab52406dba8a486558d8e724ef08acb96c867595cf4f`)
- [observation/documented] Settings allow configuring per-model context window and maximum output tokens, used for both context management and API requests. -- evidence: [README.md#L120-L120](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L120-L120) (`clm_51f4c8629351baabaacebe70bd708a25fc6a16d20ba49026ccaca0480a6ebccc`)

## memory-state (1 claim(s))

- [observation/documented] The product claims long-term memory and team knowledge bases from which it learns team knowledge and user habits. -- evidence: [README.md#L55-L55](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L55-L55) (`clm_58a23a26a818eec81554d72339cea619a28d90c9f64958e2668ab9fd58999ed4`)

## orchestration (1 claim(s))

- [observation/documented] The agent is documented to understand targets, autonomously plan, and perform multi-host problem analysis and root-cause localization, closing the loop on complex processes. -- evidence: [README.md#L80-L80](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L80-L80) (`clm_95241ed94d0eca9a272a200df12a28d6a627ff8ffcc033ea4cee4f9314ffc2c6`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] New retrieval configurations default to Qwen-Plus in the China edition and Gemini 2.5 Flash in the global edition for reranking. -- evidence: [README.md#L100-L100](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L100-L100) (`clm_e6d4dc258bf08c3895dd83abdae0cf7f3499b3fb24416bcea3dcb298055d9ef6`)
- [observation/documented] Portions of the AI Agent system are adapted from Cline, and RTK is used for command output filtering to reduce token usage in agent workflows. -- evidence: [README.md#L174-L175](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L174-L175) (`clm_69de236be9a4ce11db71fe6ba5e26820c5e30b33da666d951919455078afd177`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

