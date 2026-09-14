# sweepai/sweep -- full detail

[Back to orientation](sweep.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sweepai/sweep/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/b79cd7b55e35ef74.json](../../../wiki/dossiers/sweepai/sweep/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/b79cd7b55e35ef74.json)

## specifications (1 claim(s))

- [observation/documented] Sweep is configured through a sweep.yaml file placed in the repository root, and Sweep can open a PR adding that config file after the first issue. -- evidence: [docs/pages/usage/config.mdx#L3-L3](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L3-L3), [docs/pages/usage/config.mdx#L5-L5](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L5-L5) (`clm_87d6f46280444c64c484e474c34a3cafde30b29dc8cadc3e1c7e355f7642348f`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The sweep.yaml config supports keys gha_enabled, branch, blocked_dirs, draft, and description, controlling GitHub Actions reading, target branch, excluded directories, draft PRs, and repo context. -- evidence: [docs/pages/usage/config.mdx#L60-L63](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L60-L63), [docs/pages/usage/config.mdx#L74-L77](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L74-L77), [docs/pages/usage/config.mdx#L54-L57](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L54-L57), [docs/pages/usage/config.mdx#L35-L41](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L35-L41), [docs/pages/usage/config.mdx#L71-L71](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L71-L71) (`clm_d97216d1dd68b61fa06a0d1d5ee7ecbfd8d2909a479c2f0e1e100bf92a09bc68`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the project's own sweep.yaml description instructs that sweepai/sweep is a Python 3.10 project with main API endpoints in sweepai/api.py and that code should adhere to PEP8. -- evidence: [docs/pages/usage/config.mdx#L84-L90](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L84-L90) (`clm_d1115bd2a6c72aca659cafa27940cbf4cacacc2ceadff376c4017b34b79f7d6b`)
- [observation/documented] Repository development practice: the docs directory is a Nextra documentation template, installed with pnpm i and run locally with pnpm dev on localhost:3000, deployable to Vercel. -- evidence: [docs/README.md#L3-L3](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L3-L3), [docs/README.md#L17-L17](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L17-L17), [docs/README.md#L19-L19](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L19-L19), [docs/README.md#L11-L11](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L11-L11) (`clm_2cac8dca2e17d02754e8714a055336499d283c65596622727dd39fa1b7bbbb49`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Sweep is invoked from GitHub by titling an issue with a 'Sweep: ' prefix or by adding the Sweep label to an existing issue or PR. -- evidence: [docs/installation.md#L13-L13](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L13-L13), [docs/installation.md#L11-L11](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L11-L11) (`clm_d3d9ea9a6cd9fe3e4e74e73c7d279d62309a14699c7897b976885c67a4245213`)
- [observation/documented] A browser extension lets users create a Sweep issue from a repository page via a purple 'Make Sweep issue' button or ctrl-enter. -- evidence: [docs/extension-post-install.md#L5-L7](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/extension-post-install.md#L5-L7) (`clm_981faf4e4ac6c4757410ea7d5d889806321539f9bfca6f8c15eae3df5ee8cd91`)

## memory-state (1 claim(s))

- [observation/documented] By default Sweep reads logs and outputs from the repository's existing GitHub Actions runs; gha_enabled: False disables this. -- evidence: [docs/pages/usage/config.mdx#L17-L17](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L17-L17), [docs/pages/usage/config.mdx#L51-L51](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L51-L51) (`clm_0819eb7020fb14be456ce1284b0ccb9b6f9305f7e4593a98c855f8df64fdadbf`)

## orchestration (1 claim(s))

- [observation/documented] When draft mode is enabled, all pull requests are created as drafts and GitHub Actions are not triggered for them. -- evidence: [docs/pages/usage/config.mdx#L26-L26](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L26-L26), [docs/pages/usage/config.mdx#L71-L71](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L71-L71) (`clm_b89cb351da0d7fd4344434d8b81ada1f14a922c4efa1822d6399c8a92d93788c`)

## tools-permissions (1 claim(s))

- [observation/documented] The blocked_dirs setting lists directories Sweep will not edit, e.g. .github/, restricting its write access within a repository. -- evidence: [docs/pages/usage/config.mdx#L60-L63](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L60-L63), [docs/pages/usage/config.mdx#L29-L30](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L29-L30) (`clm_59e6a2953b2025f067819b07959a163447c9c670c2aaefceb97e88044a9f4860`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Documented limitations include repos over 5000 files, large refactors beyond 5 files or 300 changed lines, editing images/non-text assets, and accessing external APIs or fetching tokens. -- evidence: [docs/installation.md#L61-L62](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L61-L62), [docs/installation.md#L58-L59](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L58-L59), [docs/installation.md#L55-L56](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L55-L56), [docs/installation.md#L64-L65](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L64-L65) (`clm_94979290ff5f027d97b614993fece62d5061e2afc3c484d232fe3c111644f1c1`)

## relevance (1 claim(s))

- [observation/documented] The README states the team is now building an AI coding assistant for JetBrains, available as a plugin, and thanks users for support of Sweep. -- evidence: [README.md#L3-L5](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/README.md#L3-L5) (`clm_6b2051dd99a975751d363ca7d5ed6eb7c2748764940074f0453410a27889a65a`)

