# codinit-dev/codinit-dev -- full detail

[Back to orientation](codinit-dev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codinit-dev/codinit-dev/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/f8e285c9eafac7bd.json](../../../wiki/dossiers/codinit-dev/codinit-dev/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/f8e285c9eafac7bd.json)

## specifications (1 claim(s))

- [observation/documented] CodinIT.dev is described as an open-source AI full-stack development platform for building Node.js applications, combining code generation, project management, and deployment in one workflow. -- evidence: [README.md#L43-L43](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L43-L43) (`clm_952f5b58a8d8bccc0ae9b3e5e237a68c84f41a0cc15170a8d57f08c66018ba3c`)

## components (1 claim(s))

- [observation/documented] The README claims an integrated suite with semantic search, diff visualization, concurrency file-locking, Supabase integration, real-time data visualization, and voice-command interfaces. -- evidence: [README.md#L95-L101](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L95-L101) (`clm_f08f2f8b4e6521250633a8fd33b466b62b44dc880d2d5557f08ce652d20b24d8`)

## design-choices (1 claim(s))

- [observation/documented] Users can configure AI provider keys in a .env file and mix multiple providers, switching providers dynamically per task; the architecture is described as vendor-neutral to avoid lock-in. -- evidence: [README.md#L95-L101](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L95-L101), [README.md#L107-L107](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L107-L107), [README.md#L80-L80](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L80-L80) (`clm_724cb279ac40241046226c57ed93de601e7997a13d9d35879cfb9a3ad8be018d`)

## workflows (7 claim(s))

- [observation/documented] Repository development practice: contributors branch from main using feature/, fix/, or chore/ prefixes and are asked to use conventional commits such as 'feat: add X'. -- evidence: [CONTRIBUTING.md#L84-L86](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L84-L86), [CONTRIBUTING.md#L80-L82](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L80-L82) (`clm_51125bf6ebd5bddbe59b2fedf457dd6acdf5891ef8dec945e52db2f57a46594d`)
- [observation/documented] Repository development practice: before requesting review, PRs must target main, build locally, pass linting and formatting, include passing tests, and update documentation when applicable. -- evidence: [CONTRIBUTING.md#L104-L108](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L104-L108) (`clm_1237d0054c9c9546007f261e427acb6ca3adf1a6d752bf8d1e331eee583f0168`)
- [observation/documented] Repository development practice: the project uses Prettier and ESLint, has a __tests__ folder and Playwright configuration for end-to-end tests, and contributors should check package.json for test, lint, format, and dev scripts. -- evidence: [CONTRIBUTING.md#L94-L96](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L94-L96), [CONTRIBUTING.md#L92-L92](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L92-L92) (`clm_84acd0456a20266752241b931258bc5a5aa57db10af4a9acd7dc8201f92eb9ef`)
- [observation/documented] Repository development practice: bug reports should search existing issues first and include expected vs actual behavior, reproduction steps, environment details, and error output. -- evidence: [CONTRIBUTING.md#L41-L42](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L41-L42), [CONTRIBUTING.md#L44-L48](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L44-L48) (`clm_59490d55d679d2c285eb94a746d77b8a369d0dcaf4c870689cc7b77d1640ee9f`)
- [observation/documented] Repository development practice: security vulnerabilities must follow the repository's SECURITY.yaml guidance and not be disclosed in public issues. -- evidence: [CONTRIBUTING.md#L114-L114](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L114-L114) (`clm_5b362885e06126c6d3a3b9894f9351ee9d8765c988ab039687a760cbcefc7436`)
- [observation/documented] Repository development practice: contributions are licensed under the repository's MIT license, and the project adopts a Contributor Covenant 2.0 code of conduct with an enforcement ladder up to permanent bans. -- evidence: [CODE_OF_CONDUCT.md#L117-L119](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CODE_OF_CONDUCT.md#L117-L119), [CONTRIBUTING.md#L120-L120](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L120-L120), [CODE_OF_CONDUCT.md#L112-L113](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CODE_OF_CONDUCT.md#L112-L113) (`clm_e063959a9ec49f2b2c2880a823440ac46f122c116b944307a92cf5792114df4e`)
- [observation/documented] Repository development practice: contributors fork the repo, install dependencies with pnpm (preferred), create .env.local from .env.example, and confirm the app runs before making changes. -- evidence: [CONTRIBUTING.md#L69-L72](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/CONTRIBUTING.md#L69-L72) (`clm_1cf170cab058ceebd7324ebbdc0f0f30a9a5a25670a0438654408e65b1549c39`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The product supports both web browser and desktop (Electron) environments, and prebuilt desktop releases are offered for macOS, Windows, and Linux. -- evidence: [README.md#L95-L101](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L95-L101), [README.md#L53-L53](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L53-L53) (`clm_75c29c9373a02dc1cb47e4c973bdd2c9ce476aab77cfc9496d1d69a65a0cfca3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README lists cloud AI providers including OpenAI, Anthropic, Google, Groq, xAI, DeepSeek, Cohere, Mistral, Together, Perplexity, HuggingFace, and OpenRouter, plus local options Ollama, LM Studio, and OpenAI-compatible endpoints. -- evidence: [README.md#L111-L111](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L111-L111), [README.md#L115-L115](https://github.com/codinit-dev/codinit-dev/blob/daab8c9ef39b24204aa2cccd5e7aa7ab2f149ae8/README.md#L115-L115) (`clm_b13578ec76dbc89b3898ef74a2e5bb78fe98bfac07e3e7d56645796aaff3e1ed`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

