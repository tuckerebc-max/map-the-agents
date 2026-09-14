# amersarhan/darce-cli -- full detail

[Back to orientation](darce-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/amersarhan/darce-cli/1b90c379ab746da96a1b099e905043895bd013ca/edcbe6956310fb55.json](../../../wiki/dossiers/amersarhan/darce-cli/1b90c379ab746da96a1b099e905043895bd013ca/edcbe6956310fb55.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Darce includes smart routing that automatically picks a model per task, and users can override routing with rules in a ~/.darcerc config file mapping conditions like large-context or complex-reasoning to specific models. -- evidence: [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101), [README.md#L152-L165](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L152-L165) (`clm_995cc8bc0a92f10e884a566b4cc04a29fd2f1c0402e50d2f6ac6bcec4a363058`)
- [observation/documented] The tool is git-aware, tracking branch, changes, and recent commits, and supports session resume via 'darce --resume' plus context compaction for long conversations. -- evidence: [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101) (`clm_3eea4d1e37df684178bd9aa458e9d7bc2153fb9c2495a34faceb35469baa8d35`)
- [observation/documented] The product tracks real-time token count and spend in a status bar and offers an account dashboard for usage stats. -- evidence: [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101) (`clm_f332c2f32c4cf436c358ceba75d88f3f38b6a20c408c71fc4172ccc67a940194`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm install, use 'npm run dev' to run from source, run tests with 'npx tsx test.ts' (106 tests), and build with 'npm run build'. -- evidence: [README.md#L169-L176](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L169-L176) (`clm_d30c239a92aa26218763f43ce2c6da99f3be9f22cb6da7a3158403b6a45455d5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes slash commands including /help, /model, /clear, /cost, /compact, and /quit, with short aliases such as /m, /c, and /q. -- evidence: [README.md#L139-L146](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L139-L146) (`clm_d96a9c1a7ad601b41374b93b05b64a7269974ddc2f50181c8fdfd1a426e85222`)
- [observation/documented] The agent provides seven tools: Read, Write, Edit, Bash, Glob, Grep, and WebFetch, plus keyboard shortcuts like Ctrl+M for model switching and triple-quote multi-line input. -- evidence: [README.md#L86-L92](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L86-L92), [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101) (`clm_a28056f839c4244b52d90f7058d57468c1f2bf260097de78c8a9ff9688e0edb0`)
- [observation/documented] Installation and startup are via npm global install of darce-cli followed by 'darce login' and 'darce'; the README states no config files, API keys, or Docker are needed to start. -- evidence: [README.md#L64-L68](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L64-L68), [README.md#L70-L70](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L70-L70) (`clm_f345526639d0995f70da8a862e65e4c7eca172db661bd857947a1a30fdfc0039`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Tool access is tier-gated: the free Starter plan limits users to 3 tools (Read, Grep, Glob) while paid tiers unlock all 7 tools, and resume/history is paid-only. -- evidence: [README.md#L121-L128](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L121-L128) (`clm_a96bb98da3278e45ce7dc196fbcf76992aa1515b25d7f3d03358eba4d1ceb4b8`)

## evaluation (1 claim(s))

- [inference/documented] No agent performance benchmarks or eval harness appear in the evidence; the only test-related content is the repository's own test suite instructions, so evaluation capability appears undocumented. -- evidence: [README.md#L169-L176](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L169-L176) (`clm_ef882d174a7fffcdd62a5fbc18dfa1876acec6fcbc55e006bd10c22a70162e85`)

## dependencies (1 claim(s))

- [observation/documented] The product routes to multiple external models, listing qwen3-coder (default), grok-4.1-fast, claude-sonnet-4, gemini-2.5-pro, deepseek-r1, deepseek-chat, and llama-4-maverick. -- evidence: [README.md#L107-L115](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L107-L115) (`clm_d58b422f60ea95bb5f62e1384d7570ba327c91945f5dc53cee24002505aa4f11`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Darce is a terminal AI coding agent that reads, writes, and edits code, runs shell commands, and searches codebases, positioning itself against Claude Code, Cursor, and Copilot CLI. -- evidence: [README.md#L10-L14](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L10-L14), [README.md#L50-L60](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L50-L60) (`clm_7d8bb49228aadd062f9e7a4bf2e4410d450139625f3ca20f51a65ca998436d57`)

