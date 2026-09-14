# sweepai/sweep

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a8b8b67bda4f @ b79cd7b55e35ef74

## Summary (orientation draft, not independently verified)

Sweep is invoked from GitHub by titling an issue with a 'Sweep: ' prefix or by adding the Sweep label to an existing issue or PR. A browser extension lets users create a Sweep issue from a repository page via a purple 'Make Sweep issue' button or ctrl-enter.

## Source coverage

Source coverage (partial): 6 of 48 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Sweep is configured through a sweep.yaml file placed in the repository root, and Sweep can open a PR adding that config file after the first issue. -- evidence: [docs/pages/usage/config.mdx#L3-L3](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L3-L3), [docs/pages/usage/config.mdx#L5-L5](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The sweep.yaml config supports keys gha_enabled, branch, blocked_dirs, draft, and description, controlling GitHub Actions reading, target branch, excluded directories, draft PRs, and repo context. -- evidence: [docs/pages/usage/config.mdx#L60-L63](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L60-L63), [docs/pages/usage/config.mdx#L74-L77](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L74-L77), [docs/pages/usage/config.mdx#L54-L57](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L54-L57), [docs/pages/usage/config.mdx#L35-L41](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L35-L41), [docs/pages/usage/config.mdx#L71-L71](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L71-L71)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the project's own sweep.yaml description instructs that sweepai/sweep is a Python 3.10 project with main API endpoints in sweepai/api.py and that code should adhere to PEP8. -- evidence: [docs/pages/usage/config.mdx#L84-L90](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L84-L90)
  - [observation/documented] Repository development practice: the docs directory is a Nextra documentation template, installed with pnpm i and run locally with pnpm dev on localhost:3000, deployable to Vercel. -- evidence: [docs/README.md#L3-L3](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L3-L3), [docs/README.md#L17-L17](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L17-L17), [docs/README.md#L19-L19](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L19-L19), [docs/README.md#L11-L11](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/README.md#L11-L11)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Sweep is invoked from GitHub by titling an issue with a 'Sweep: ' prefix or by adding the Sweep label to an existing issue or PR. -- evidence: [docs/installation.md#L13-L13](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L13-L13), [docs/installation.md#L11-L11](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/installation.md#L11-L11)
  - [observation/documented] A browser extension lets users create a Sweep issue from a repository page via a purple 'Make Sweep issue' button or ctrl-enter. -- evidence: [docs/extension-post-install.md#L5-L7](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/extension-post-install.md#L5-L7)
- memory-state (1 claim(s)):
  - [observation/documented] By default Sweep reads logs and outputs from the repository's existing GitHub Actions runs; gha_enabled: False disables this. -- evidence: [docs/pages/usage/config.mdx#L17-L17](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L17-L17), [docs/pages/usage/config.mdx#L51-L51](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L51-L51)
- orchestration (1 claim(s)):
  - [observation/documented] When draft mode is enabled, all pull requests are created as drafts and GitHub Actions are not triggered for them. -- evidence: [docs/pages/usage/config.mdx#L26-L26](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L26-L26), [docs/pages/usage/config.mdx#L71-L71](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L71-L71)
- tools-permissions (1 claim(s)):
  - [observation/documented] The blocked_dirs setting lists directories Sweep will not edit, e.g. .github/, restricting its write access within a repository. -- evidence: [docs/pages/usage/config.mdx#L60-L63](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L60-L63), [docs/pages/usage/config.mdx#L29-L30](https://github.com/sweepai/sweep/blob/a8b8b67bda4f89faac9314d34e7c7d5a64f76046/docs/pages/usage/config.mdx#L29-L30)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
More evidence: [full detail](sweep.detail.md)

Metadata and full claim list: [full detail](sweep.detail.md)
Human notes ([notes](sweep.notes.md), never overwritten by build)

[Back to map index](../../index.md)
