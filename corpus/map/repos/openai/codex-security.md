# openai/codex-security

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 75914c46386e @ 3eddbd4694246bb5

## Summary (orientation draft, not independently verified)

The product ships as a CLI and TypeScript SDK; the SDK exposes a CodexSecurity class with run() accepting options like mode, workers, subagents, and maxTimeHours, plus a close() method. A findings service (preview) runs from the same ghcr.io/openai/codex-security image, stores findings and embeddings in SQLite, serves a read-only /dashboard refreshing every five seconds, and returns duplicate candidates by embedding similarity. Evidence coverage: 118 of 143 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A findings service (preview) runs from the same ghcr.io/openai/codex-security image, stores findings and embeddings in SQLite, serves a read-only /dashboard refreshing every five seconds, and returns duplicate candidates by embedding similarity. -- evidence: [README.md#L74-L86](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L74-L86)
- design-choices (4 claim(s)):
  - [observation/documented] Project configuration files use snake_case keys while SDK options use camelCase and CLI flags kebab-case; a shared ScanSettings type underlies all three resolution paths. -- evidence: [docs/project-configuration.md#L95-L98](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L95-L98), [docs/project-configuration.md#L100-L119](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L100-L119)
  - [observation/documented] Config loading is deliberately literal: no JavaScript evaluation, environment interpolation, remote includes, or multi-file merging; unknown keys and invalid types are errors, and YAML anchors are supported with alias-expansion guards. -- evidence: [docs/project-configuration.md#L52-L59](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/docs/project-configuration.md#L52-L59)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: pull request titles must follow a Conventional Commit form (<type>[scope][!]: <description>), which drives release categories and version bumping under a 0.x policy where features are patch releases. -- evidence: [RELEASING.md#L12-L12](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L12-L12), [RELEASING.md#L67-L71](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L67-L71), [RELEASING.md#L31-L38](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L31-L38), [RELEASING.md#L14-L16](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L14-L16)
  - [observation/documented] Repository development practice: releases are automated via node-release-pr, node-release-cut, node-release, and node-github-release workflows; Dependabot applies a seven-day age policy to non-OpenAI dependencies, and updates still require review and passing CI. -- evidence: [RELEASING.md#L219-L225](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L219-L225), [RELEASING.md#L48-L52](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L48-L52), [RELEASING.md#L82-L84](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/RELEASING.md#L82-L84)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships as a CLI and TypeScript SDK; the SDK exposes a CodexSecurity class with run() accepting options like mode, workers, subagents, and maxTimeHours, plus a close() method. -- evidence: [README.md#L3-L3](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L3-L3), [README.md#L45-L54](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L45-L54), [README.md#L40-L40](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L40-L40), [README.md#L56-L58](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L56-L58)
  - [observation/documented] Alternative inference providers are supported via --provider with documented examples for amazon-bedrock, openrouter, and fireworks, each using its own API-key environment variable. -- evidence: [README.md#L103-L104](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L103-L104), [README.md#L98-L101](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L98-L101), [README.md#L96-L96](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L96-L96), [README.md#L106-L108](https://github.com/openai/codex-security/blob/75914c46386e010b549f94acc02c9356551247ac/README.md#L106-L108)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](codex-security.detail.md)

Metadata and full claim list: [full detail](codex-security.detail.md)
Human notes ([notes](codex-security.notes.md), never overwritten by build)

[Back to map index](../../index.md)
