# rizwan3d/stemcode -- full detail

[Back to orientation](stemcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rizwan3d/stemcode/dfe4dd78998824cb61ad508e07050c4ab884e7e6/7835cc5cd29fd935.json](../../../wiki/dossiers/rizwan3d/stemcode/dfe4dd78998824cb61ad508e07050c4ab884e7e6/7835cc5cd29fd935.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Built-in tracked edit tools include `file_write`, `apply_patch`, `insert_content`, and `search_and_replace`, which record before/after state and participate in `/undo`, `/redo`, and edit summaries. -- evidence: [docs/documentation.md#L412-L412](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L412-L412), [docs/documentation.md#L403-L403](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L403-L403), [docs/documentation.md#L407-L410](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L407-L410), [docs/documentation.md#L405-L405](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L405-L405) (`clm_e4010c7b6011cc99f0b548fc133c4a9b34ece1f04cb5b2df5986df952c6230fa`)

## design-choices (2 claim(s))

- [observation/documented] Budget controls are disabled by default and activate only via `/budget local`, `/budget cloud`, or an existing `.stemcode/budget-controls.*.json` file; while disabled, no usage is recorded and provider requests are never blocked. -- evidence: [docs/documentation.md#L212-L212](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L212-L212) (`clm_eee98137ca9d49a20d6d4e07890519935a319aac12d3a7e9c7b574fbe8889c59`)
- [observation/documented] Subagents run delegated tasks with independent contexts to keep the main conversation focused, and interactive user questions support clarification, multiple-choice, multi-select, and free-form input. -- evidence: [README.md#L81-L90](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L81-L90) (`clm_c1032f0da4048c2d00d8e56ec33f93fb4488855e37ab4e527038043f5362a6d8`)

## workflows (1 claim(s))

- [observation/documented] Release assets publish SHA256SUMS and GitHub artifact attestations; the release pipeline verifies each checksum before publishing, and `gh attestation verify` is documented for provenance checks. -- evidence: [docs/documentation.md#L53-L53](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L53-L53), [README.md#L119-L119](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L119-L119) (`clm_728277689f0f0bdd63bc54d7630decaee69658e9775f2ae2ecda039be7b47c8a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] StemCode ships as a desktop app, a `stemcode` terminal command, VS Code and Visual Studio extensions, and an ACP-compatible editor server. -- evidence: [docs/documentation.md#L3-L3](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L3-L3) (`clm_ed148cfccefa9fe98049544ee7bfda1add4f97113aa25bf37af9bc16301e3f4e`)
- [observation/documented] The CLI supports options including `--acp`, `--stdin`, `--json`, `-p/--prompt`, `--sandbox-mode`, `--session`, `--profile`, `--thinking`, and `--doctor`. -- evidence: [docs/documentation.md#L327-L345](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L327-L345) (`clm_d975a0b6cdce10dfefc6859497e00509664da66c578689ee0e97c5b38c0e4316`)
- [observation/documented] The CLI binary is documented as self-contained and AOT-compiled, and all installers expose the same `stemcode` command from the same release assets. -- evidence: [docs/documentation.md#L57-L59](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L57-L59), [README.md#L134-L134](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L134-L134) (`clm_16d43335a7bcd44660f219cba308ffe4536c5339080eb465f626b5022a30707c`)

## memory-state (2 claim(s))

- [observation/documented] Reusable commands live in `.stemcode/commands` and long-lived project knowledge in `.stemcode/memory`, stored as versionable files users can review and commit. -- evidence: [README.md#L94-L102](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L94-L102), [README.md#L81-L90](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L81-L90) (`clm_0121697644bf3855c02ab40a15d01c565b26f7def740dba8c5afbf739366b089`)
- [observation/documented] Desktop sections are saved local conversation threads per workspace that preserve history, active model, profile, thinking mode, plan state, and session state when available. -- evidence: [docs/documentation.md#L183-L183](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L183-L183) (`clm_27928b1a8f71bd1151c07835a1ccf7c68ecdd7652558b8b94a6a2e014bf15d3a`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product uses approval prompts, permissions, and profiles to keep actions under human control; `--sandbox-mode` overrides sandbox policy per run with read-only, workspace-write, or danger-full-access values. -- evidence: [docs/documentation.md#L305-L305](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L305-L305), [docs/documentation.md#L327-L345](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L327-L345), [docs/documentation.md#L307-L309](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L307-L309), [README.md#L81-L90](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L81-L90), [README.md#L54-L55](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L54-L55) (`clm_5c22cc44217616e2d5d904e69206b0f7eb528f2deef6a42c5fe78b70315bbb12`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The npm `stemcode` package is a thin installer that downloads the matching release binary and verifies it against published SHA256SUMS, with no .NET toolchain required; targets include win-x64, osx-x64, osx-arm64, linux-x64, and linux-arm64. -- evidence: [docs/documentation.md#L87-L87](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L87-L87) (`clm_65681661242f27f44d30df6e5eccdbe69e23ebda9676a62bce250c5c465bdca5`)
- [observation/documented] Providers span subscription sign-in (ChatGPT Plus/Pro, Claude Pro/Max, GitHub Copilot), API-key providers (OpenAI, Anthropic, Gemini, OpenRouter, Groq, DeepSeek, and others), OpenAI-compatible endpoints, and local providers such as Ollama. -- evidence: [docs/documentation.md#L152-L169](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L152-L169) (`clm_598591c31020e723ccfe711ca433001074cfef4c3f9841053120198bc15a26e8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

