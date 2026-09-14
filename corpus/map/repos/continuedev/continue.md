# continuedev/continue

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5522c6f44ca0 @ 41756b650b1e5612

## Summary (orientation draft, not independently verified)

Evidence covers the Continue coding agent's distribution forms (CLI, VS Code, JetBrains), its YAML-based configuration system, and repository-level build/CI secret documentation, a CLA, and a testing checklist. The repository is stated to be read-only and no longer maintained.

## Source coverage

Source coverage (partial): 6 of 160 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] User-level configuration lives in `~/.continue/config.yaml` (or `%USERPROFILE%\.continue\config.yaml` on Windows), and saving it in the IDE triggers an automatic config refresh. -- evidence: [docs/customize/deep-dives/configuration.mdx#L23-L23](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L23-L23), [docs/customize/deep-dives/configuration.mdx#L16-L17](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L16-L17), [docs/customize/deep-dives/configuration.mdx#L14-L14](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L14-L14)
  - [observation/documented] Legacy configuration methods are deprecated: `config.json`, workspace-level `.continuerc.json` (with a `mergeBehavior` of merge or overwrite), and programmatic `config.ts` exporting `modifyConfig`. -- evidence: [docs/customize/deep-dives/configuration.mdx#L29-L31](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L29-L31), [docs/customize/deep-dives/configuration.mdx#L33-L37](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L33-L37), [docs/customize/deep-dives/configuration.mdx#L58-L58](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L58-L58), [docs/customize/deep-dives/configuration.mdx#L56-L56](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L56-L56), [docs/customize/deep-dives/configuration.mdx#L41-L41](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L41-L41)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: CI workflows reference many secrets, including marketplace publishing tokens (VSCE_TOKEN, VSX_REGISTRY_TOKEN), JetBrains signing/notarization credentials, semantic-release npm/GitHub tokens, and AI provider API keys used in PR checks and releases. -- evidence: [BUILD_DEPENDENCIES.md#L9-L12](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L9-L12), [BUILD_DEPENDENCIES.md#L54-L66](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L54-L66), [BUILD_DEPENDENCIES.md#L42-L46](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L42-L46), [BUILD_DEPENDENCIES.md#L18-L27](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L18-L27), [BUILD_DEPENDENCIES.md#L52-L52](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L52-L52)
  - [observation/documented] Repository development practice: contributors accept an Individual CLA by commenting an agreement phrase on a pull request; the CLA grants Continue Dev, Inc. copyright and patent licenses and terminates patent licenses upon litigation. -- evidence: [CLA.md#L5-L7](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L5-L7), [CLA.md#L32-L34](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L32-L34), [CLA.md#L20-L23](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L20-L23), [CLA.md#L27-L30](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L27-L30)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] Continue is shipped as a CLI, a VS Code extension, and a JetBrains plugin. -- evidence: [README.md#L21-L21](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L21-L21)
  - [observation/documented] The CLI (`cn`) resolves configuration in order: a `--config` file path flag, the last-used saved config, then the default `~/.continue/config.yaml`. -- evidence: [docs/cli/configuration.mdx#L7-L9](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L7-L9), [docs/cli/configuration.mdx#L5-L5](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L5-L5)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The CLI uses `CONTINUE_API_BASE` (defaulting to https://api.continue.dev/) and `CONTINUE_API_KEY` for Continue API authentication, per the repository's build-dependency catalog. -- evidence: [BUILD_DEPENDENCIES.md#L33-L36](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L33-L36)
- limitations (2 claim(s)):
  - [observation/documented] The README states the continuedev/continue repository is no longer actively maintained and is read-only for all users. -- evidence: [README.md#L19-L19](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L19-L19)
  - [observation/documented] The project recommends using the Continue CLI instead of the JetBrains plugin. -- evidence: [README.md#L43-L43](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L43-L43)
- relevance: unknown (no source-linked claim submitted for this facet)

(6 additional claim(s) omitted for length; see [full detail](continue.detail.md) for every claim.)

Metadata and full claim list: [full detail](continue.detail.md)
Human notes ([notes](continue.notes.md), never overwritten by build)

[Back to map index](../../index.md)
