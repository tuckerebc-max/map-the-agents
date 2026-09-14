# continuedev/continue -- full detail

[Back to orientation](continue.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/continuedev/continue/5522c6f44ca0ac3528b37244818fbfa39b5af470/41756b650b1e5612.json](../../../wiki/dossiers/continuedev/continue/5522c6f44ca0ac3528b37244818fbfa39b5af470/41756b650b1e5612.json)

## specifications (3 claim(s))

- [observation/documented] User-level configuration lives in `~/.continue/config.yaml` (or `%USERPROFILE%\.continue\config.yaml` on Windows), and saving it in the IDE triggers an automatic config refresh. -- evidence: [docs/customize/deep-dives/configuration.mdx#L23-L23](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L23-L23), [docs/customize/deep-dives/configuration.mdx#L16-L17](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L16-L17), [docs/customize/deep-dives/configuration.mdx#L14-L14](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L14-L14) (`clm_83ca78537b40bc9481f2493212ed4bcb03bf2661f7c885378b838a101c15d7a0`)
- [observation/documented] Legacy configuration methods are deprecated: `config.json`, workspace-level `.continuerc.json` (with a `mergeBehavior` of merge or overwrite), and programmatic `config.ts` exporting `modifyConfig`. -- evidence: [docs/customize/deep-dives/configuration.mdx#L29-L31](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L29-L31), [docs/customize/deep-dives/configuration.mdx#L33-L37](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L33-L37), [docs/customize/deep-dives/configuration.mdx#L58-L58](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L58-L58), [docs/customize/deep-dives/configuration.mdx#L56-L56](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L56-L56), [docs/customize/deep-dives/configuration.mdx#L41-L41](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L41-L41) (`clm_a3e393526097aad75f6d81295342d9aeb3a4c008e5a02cbfedd29f17293332ab`)
- [observation/documented] The final 2.0.0 release removed anonymous telemetry and pulled out authentication across the VS Code extension, CLI, and JetBrains plugin. -- evidence: [README.md#L31-L31](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L31-L31), [README.md#L29-L29](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L29-L29) (`clm_7db55eaed9461d1ed54dc03c85da04248d70fa3d1cfe4c5860456f1a0a08d6a9`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: CI workflows reference many secrets, including marketplace publishing tokens (VSCE_TOKEN, VSX_REGISTRY_TOKEN), JetBrains signing/notarization credentials, semantic-release npm/GitHub tokens, and AI provider API keys used in PR checks and releases. -- evidence: [BUILD_DEPENDENCIES.md#L9-L12](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L9-L12), [BUILD_DEPENDENCIES.md#L54-L66](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L54-L66), [BUILD_DEPENDENCIES.md#L42-L46](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L42-L46), [BUILD_DEPENDENCIES.md#L18-L27](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L18-L27), [BUILD_DEPENDENCIES.md#L52-L52](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L52-L52) (`clm_d22f21a396d154d7cd6b5b8a43ea95021f04dafe26f5557f0887365651e93db9`)
- [observation/documented] Repository development practice: contributors accept an Individual CLA by commenting an agreement phrase on a pull request; the CLA grants Continue Dev, Inc. copyright and patent licenses and terminates patent licenses upon litigation. -- evidence: [CLA.md#L5-L7](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L5-L7), [CLA.md#L32-L34](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L32-L34), [CLA.md#L20-L23](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L20-L23), [CLA.md#L27-L30](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/CLA.md#L27-L30) (`clm_4e7fe7c6a75f64fbda130b207761a141f7578bbea4b1ddfa8dd3399cb91f9a09`)
- [observation/documented] Repository development practice: a TESTING.md checklist records manual verification items (extension cold start, onboarding, config reload, MCP server connections) plus Vitest suites and `tsc --noEmit` compilation checks. -- evidence: [TESTING.md#L5-L9](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/TESTING.md#L5-L9), [TESTING.md#L13-L17](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/TESTING.md#L13-L17), [TESTING.md#L21-L25](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/TESTING.md#L21-L25) (`clm_6293fa60805d9a51f966f96785d545a6474bbe19e1c36010d9dde2f69ffea076`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] Continue is shipped as a CLI, a VS Code extension, and a JetBrains plugin. -- evidence: [README.md#L21-L21](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L21-L21) (`clm_121fbb2742fb703817bcfc68fbe77539468ed59f5dcc0d00181ce04e5ed0d378`)
- [observation/documented] The CLI (`cn`) resolves configuration in order: a `--config` file path flag, the last-used saved config, then the default `~/.continue/config.yaml`. -- evidence: [docs/cli/configuration.mdx#L7-L9](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L7-L9), [docs/cli/configuration.mdx#L5-L5](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L5-L5) (`clm_f9793019a66b0a2c3af655f952dc21515f4050463a82f67fa81f4793e5939c12`)
- [observation/documented] Inside a CLI TUI session, the `/config` command lists available local configurations and the selection persists to the next session. -- evidence: [docs/cli/configuration.mdx#L29-L29](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L29-L29), [docs/cli/configuration.mdx#L23-L23](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L23-L23) (`clm_41906ac0ec4c107b0537188a2ee3562a0c21a39a665fb5bf1dfd99a2dd56cc6b`)
- [observation/documented] The CLI supports repeatable launch flags such as `--rule` (file path or inline string) and `--agent` (e.g. `my-org/pr-reviewer`) to inject configuration without editing files. -- evidence: [docs/cli/configuration.mdx#L45-L46](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L45-L46), [docs/cli/configuration.mdx#L48-L48](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L48-L48), [docs/cli/configuration.mdx#L41-L42](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L41-L42) (`clm_674a2ff212bbf8940bc4e473505cab6f4e14bb849447d9e59682a44bf99ef4c9`)
- [observation/documented] In the IDE extensions, configuration is reached from the Continue Chat sidebar (cmd/ctrl+L in VS Code, cmd/ctrl+J in JetBrains) via the Agent selector's gear icon. -- evidence: [docs/customize/deep-dives/configuration.mdx#L8-L8](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/customize/deep-dives/configuration.mdx#L8-L8) (`clm_08a1e1cdf234c9db83ebef6554a72b39e3866ed045c17e295af6ac029efa0cd8`)
- [observation/documented] Sensitive values in config are referenced as environment variables using the `${{ secrets.MY_API_KEY }}` syntax. -- evidence: [docs/cli/configuration.mdx#L54-L56](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L54-L56), [docs/cli/configuration.mdx#L52-L52](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/docs/cli/configuration.mdx#L52-L52) (`clm_eb9bd6021c717d81109cfea7204c6bdbf9dd32bfc05f15c807a07c72a106d138`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The CLI uses `CONTINUE_API_BASE` (defaulting to https://api.continue.dev/) and `CONTINUE_API_KEY` for Continue API authentication, per the repository's build-dependency catalog. -- evidence: [BUILD_DEPENDENCIES.md#L33-L36](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/BUILD_DEPENDENCIES.md#L33-L36) (`clm_4d5864539bcdf51e95a81c3e778b258bbf1afc348a88eb2603a8c9d83372070a`)

## limitations (2 claim(s))

- [observation/documented] The README states the continuedev/continue repository is no longer actively maintained and is read-only for all users. -- evidence: [README.md#L19-L19](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L19-L19) (`clm_09c19f0310c7ed476f7b7d3f50c5900b375e8fbf42ae4b06d2ccef79099a5878`)
- [observation/documented] The project recommends using the Continue CLI instead of the JetBrains plugin. -- evidence: [README.md#L43-L43](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md#L43-L43) (`clm_b9805a083b12d5aac53af94492af3febcf9049c14a40bcdbfd5fd354cf60e30a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

