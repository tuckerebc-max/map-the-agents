# jhutchings1/create-actionsprs

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e10f42920c1f @ ded660563025e942

## Summary (orientation draft, not independently verified)

Selected evidence records: The repository's script creates pull requests that push a GitHub Actions workflow to multiple repositories. The tool exposes PowerShell commands CreatePullRequestForRepositories, CreatePullRequestsFromFile, and CreatePullRequestsForCodeQLLanguages, run after installing via ./Create-ActionsPRs.ps1.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository's script creates pull requests that push a GitHub Actions workflow to multiple repositories. -- evidence: [README.md#L2-L2](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L2-L2)
- components (1 claim(s)):
  - [observation/documented] Workflow files to be pushed live in a 'workflows' directory, which already includes a CodeQL workflow file. -- evidence: [README.md#L31-L35](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L31-L35), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17)
- design-choices (1 claim(s)):
  - [observation/documented] Authentication uses a .env file (renamed from .env-example) holding a GitHub token with the repo scope, authorized for SSO when the organization requires it. -- evidence: [README.md#L31-L35](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L31-L35), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The tool exposes PowerShell commands CreatePullRequestForRepositories, CreatePullRequestsFromFile, and CreatePullRequestsForCodeQLLanguages, run after installing via ./Create-ActionsPRs.ps1. -- evidence: [README.md#L31-L35](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L31-L35), [README.md#L22-L28](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L22-L28), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17)
  - [observation/documented] PR creation commands accept CommitMessage, PRBody, and BranchName parameters to customize the resulting pull requests. -- evidence: [README.md#L22-L28](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L22-L28), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] One mode targets all repositories in an organization using GetReposFromOrganization, creating PRs in every repository where the user has push permissions. -- evidence: [README.md#L19-L19](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L19-L19), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17)
  - [observation/documented] Another mode reads a user-created file of repository URLs, one per line, and creates PRs for those repositories via CreatePullRequestsFromFile. -- evidence: [README.md#L22-L28](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L22-L28)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Prerequisites are PowerShell, git configured for GitHub access (with SSH key setup guidance), and the GitHub CLI. -- evidence: [README.md#L5-L7](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L5-L7)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](create-actionsprs.detail.md).

Metadata and full claim list: [full detail](create-actionsprs.detail.md)
Human notes ([notes](create-actionsprs.notes.md), never overwritten by build)

[Back to map index](../../index.md)
