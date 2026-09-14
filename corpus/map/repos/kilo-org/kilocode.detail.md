# kilo-org/kilocode -- full detail

[Back to orientation](kilocode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kilo-org/kilocode/c36e22634860e06e0aa63234fae37bbd83d3b182/9a09d74283c90a85.json](../../../wiki/dossiers/kilo-org/kilocode/c36e22634860e06e0aa63234fae37bbd83d3b182/9a09d74283c90a85.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Kilo ships specialized agents: Code (default, implements code), Plan (architecture and plans), Ask (answers without touching files), Debug, and Review, and users can build custom agents. -- evidence: [README.md#L125-L129](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L125-L129), [README.md#L123-L123](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L123-L123) (`clm_5557ca92e1957cfa412537786b0a1863464170391d330837433f34cf36118c0c`)
- [observation/documented] Documented capabilities include multi-file code generation, inline ghost-text autocomplete, self-checking, terminal and browser control, an MCP marketplace, and 500+ models with mid-task switching. -- evidence: [README.md#L135-L140](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L135-L140) (`clm_e7599b7c3bfd1f687b597d4f8bb46f0172b4e31f5462e0ce81146961b282727a`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: releases run through an automated GitHub Actions publish workflow whose four sequential jobs are version, build-cli, build-vscode, and publish, gated to the Kilo-Org/kilocode repo and requiring write access. -- evidence: [RELEASING.md#L44-L48](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L44-L48), [RELEASING.md#L25-L29](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L25-L29), [RELEASING.md#L3-L3](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L3-L3), [RELEASING.md#L21-L21](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L21-L21), [RELEASING.md#L33-L40](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L33-L40), [RELEASING.md#L52-L52](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L52-L52), [RELEASING.md#L90-L91](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L90-L91) (`clm_ddda51c390e059c73dedd6bf74cc01edb8c13b1d5451b1ddfd223b13a692fd43`)
- [observation/documented] Repository development practice: an automated reviewer bot is guided by REVIEW.md to catch bugs, design issues, and fork-merge hygiene beyond what CI reports, minimizing diff against the upstream opencode fork. -- evidence: [REVIEW.md#L3-L3](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/REVIEW.md#L3-L3), [REVIEW.md#L57-L57](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/REVIEW.md#L57-L57), [REVIEW.md#L5-L5](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/REVIEW.md#L5-L5) (`clm_02f6b19bf7dd641b1cbf9ea0c2cf372754428725e0e9715e4a8e13b6445dfc53`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Kilo Code is an AI coding agent available for VS Code, JetBrains IDEs, and as a CLI, installable via npm, curl, pnpm, bun, Homebrew, and AUR. -- evidence: [README.md#L49-L49](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L49-L49), [README.md#L24-L24](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L24-L24), [README.md#L46-L46](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L46-L46), [README.md#L58-L58](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L58-L58), [README.md#L9-L9](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L9-L9), [README.md#L55-L55](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L55-L55), [README.md#L61-L62](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L61-L62), [README.md#L52-L52](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L52-L52) (`clm_93523d95a1c2cce4d77642b75496c70cfa3c308fb57a32fe5bda137ba0039e88`)
- [observation/documented] The CLI ships as platform binaries for Windows, macOS (Intel and Apple Silicon), and Linux x64/ARM, including a musl build for Alpine and a non-AVX baseline build for older CPUs. -- evidence: [README.md#L117-L117](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L117-L117), [README.md#L109-L115](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L109-L115) (`clm_5d282645eb1235d4da66f19328fbcf5d5bbb3267d973b1fdec99e2c8d6c2a85e`)
- [observation/documented] The architecture exposes a public HttpApi from which Promise and Effect clients are generated, plus an Embedded OpenCode in-process host using an in-memory HTTP transport against the same router. -- evidence: [CONTEXT.md#L73-L75](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L73-L75), [CONTEXT.md#L203-L203](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L203-L203), [CONTEXT.md#L80-L82](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L80-L82) (`clm_c5148cdb21b2e43917cead849e0db5672cb0a2e6768276469370f2ceb19246df`)

## memory-state (3 claim(s))

- [observation/documented] The runtime defines a session context model: a System Context assembled from typed Context Sources, Session History projected per provider turn, and a Context Snapshot tracking each source's last-admitted value. -- evidence: [CONTEXT.md#L7-L9](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L7-L9), [CONTEXT.md#L15-L17](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L15-L17), [CONTEXT.md#L33-L34](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L33-L34), [CONTEXT.md#L3-L3](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L3-L3), [CONTEXT.md#L11-L13](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L11-L13) (`clm_82a1dc7ff3dc65c425b84d05768f618fea08a90c56049220bcd51a6e2ccfba6e`)
- [observation/documented] Context changes are admitted lazily at a Safe Provider-Turn Boundary rather than pushed asynchronously, and changes from multiple sources at one boundary combine into a single Mid-Conversation System Message. -- evidence: [CONTEXT.md#L22-L24](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L22-L24), [CONTEXT.md#L90-L199](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L90-L199), [CONTEXT.md#L39-L40](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L39-L40) (`clm_97c56a1931f126ae17e420eb8a81d0d87e8ee25f72f11ab519f9017da33f74be`)
- [observation/documented] Tool output persisted in session history is size-bounded by the Tool Registry; oversized output is retained in a temporary managed tool-output file under a shared directory. -- evidence: [CONTEXT.md#L57-L58](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L57-L58), [CONTEXT.md#L54-L55](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L54-L55) (`clm_7065836d8d126c3c73cab862751e87c3c8b23879aef152eebaba77b39db2cbeb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The CLI's `kilo run --auto` mode disables all permission prompts and executes actions without confirmation, intended for trusted CI/CD environments. -- evidence: [README.md#L144-L144](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L144-L144), [README.md#L146-L148](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L146-L148), [README.md#L150-L150](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L150-L150) (`clm_21c520353e67b952c43e9e79d36a1d03fc4d24209560ab4f298070e5bab1002b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The privacy policy states prompts and relevant project context are sent to the user's chosen AI model provider (e.g., OpenAI, Anthropic, OpenRouter), and API keys are stored locally on the device. -- evidence: [PRIVACY.md#L9-L12](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/PRIVACY.md#L9-L12) (`clm_a7a407485803ccc1d971b27f77e4784e547fbf571c766cdfa415cf59767a651b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

