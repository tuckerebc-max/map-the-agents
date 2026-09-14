# openai/codex-security -- full detail

[Back to orientation](codex-security.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openai/codex-security/75914c46386e010b549f94acc02c9356551247ac/3eddbd4694246bb5.json](../../../wiki/dossiers/openai/codex-security/75914c46386e010b549f94acc02c9356551247ac/3eddbd4694246bb5.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A findings service (preview) runs from the same ghcr.io/openai/codex-security image, stores findings and embeddings in SQLite, serves a read-only /dashboard refreshing every five seconds, and returns duplicate candidates by embedding similarity. -- evidence: [README.md#L74-L86](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L74-L86) (`clm_8231562a344e80320068977e13af1913161345bed4c613decfa278fab6631769`)

## design-choices (4 claim(s))

- [observation/documented] Project configuration files use snake_case keys while SDK options use camelCase and CLI flags kebab-case; a shared ScanSettings type underlies all three resolution paths. -- evidence: [docs/project-configuration.md#L95-L98](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L95-L98), [docs/project-configuration.md#L100-L119](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L100-L119) (`clm_18328b54eba69035bddc8cf88ccce85a6b4bc3c7ae71b378d15a81d269fd50de`)
- [observation/documented] Config loading is deliberately literal: no JavaScript evaluation, environment interpolation, remote includes, or multi-file merging; unknown keys and invalid types are errors, and YAML anchors are supported with alias-expansion guards. -- evidence: [docs/project-configuration.md#L52-L59](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L52-L59) (`clm_aaaf86f72f1cb8a6fbe88d44d815d5b6878878711f18bd2d71abf7012a53326e`)
- [observation/documented] Settings precedence is built-in defaults, legacy deep settings, the project file, then explicit CLI values; lists are replaced rather than concatenated, and scope selectors from the CLI override the file's scope variant. -- evidence: [docs/project-configuration.md#L182-L184](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L182-L184), [docs/project-configuration.md#L202-L206](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L202-L206) (`clm_2f62067f36b9b46e934c430d2f741d85ceafbe390c4ac1e975c87653276385fa`)
- [observation/documented] The policy command drafts SECURITY.md guidance outside the checkout without installing it or scanning, and supporting architecture or threat-model documents are kept outside the repository. -- evidence: [README.md#L32-L36](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L32-L36), [README.md#L25-L25](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L25-L25) (`clm_e7431597e8b814377aa9179a759376552573e5b742a70641f2783c2eb4d0ebdb`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: pull request titles must follow a Conventional Commit form (<type>[scope][!]: <description>), which drives release categories and version bumping under a 0.x policy where features are patch releases. -- evidence: [RELEASING.md#L12-L12](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L12-L12), [RELEASING.md#L67-L71](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L67-L71), [RELEASING.md#L31-L38](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L31-L38), [RELEASING.md#L14-L16](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L14-L16) (`clm_3455ec9b588d4f19b3e1f68d740824c7bc7db574da880d32e9c911b5e3a31580`)
- [observation/documented] Repository development practice: releases are automated via node-release-pr, node-release-cut, node-release, and node-github-release workflows; Dependabot applies a seven-day age policy to non-OpenAI dependencies, and updates still require review and passing CI. -- evidence: [RELEASING.md#L219-L225](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L219-L225), [RELEASING.md#L48-L52](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L48-L52), [RELEASING.md#L82-L84](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L82-L84) (`clm_ec080d87d2db66b25791e412032384cfef92df5be88304a8e7a9298069b68fbe`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product ships as a CLI and TypeScript SDK; the SDK exposes a CodexSecurity class with run() accepting options like mode, workers, subagents, and maxTimeHours, plus a close() method. -- evidence: [README.md#L3-L3](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L3-L3), [README.md#L45-L54](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L45-L54), [README.md#L40-L40](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L40-L40), [README.md#L56-L58](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L56-L58) (`clm_47b50309adebda75fb9fc8a606567e889b95406e9565faf4757cce5d24a50888`)
- [observation/documented] Alternative inference providers are supported via --provider with documented examples for amazon-bedrock, openrouter, and fireworks, each using its own API-key environment variable. -- evidence: [README.md#L103-L104](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L103-L104), [README.md#L98-L101](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L98-L101), [README.md#L96-L96](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L96-L96), [README.md#L106-L108](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L106-L108) (`clm_c9debfacb60ec1a1b56f75fa257fbb2a436596415e251c5e30a1cb6c969b8b43`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool requires Node.js 22.13.0 or later and Python 3.10 or later, and is installed via npm as @openai/codex-security. -- evidence: [README.md#L15-L19](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L15-L19), [README.md#L13-L13](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L13-L13) (`clm_8a0fc9831562973ae8549085492350895a3737bb5a1e172577c5e6b51cdc1fc6`)

## limitations (1 claim(s))

- [observation/documented] Deep diff scans and custom validation remain unsupported in deep mode, and discovery time cannot exceed 96 hours; the cost limit is per scan attempt and in-flight work may exceed it. -- evidence: [docs/project-configuration.md#L248-L251](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L248-L251), [docs/project-configuration.md#L243-L246](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L243-L246) (`clm_8ad1ae0be8c3b10cd6cbcbdef14751b4938ec90f4cfa90e9fc335b3d7d05684d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

