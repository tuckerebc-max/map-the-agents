# jhutchings1/create-actionsprs -- full detail

[Back to orientation](create-actionsprs.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jhutchings1/create-actionsprs/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/ded660563025e942.json](../../../wiki/dossiers/jhutchings1/create-actionsprs/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/ded660563025e942.json)

## specifications (1 claim(s))

- [observation/documented] The repository's script creates pull requests that push a GitHub Actions workflow to multiple repositories. -- evidence: [README.md#L2-L2](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L2-L2) (`clm_ddec173ab775c5b335bdca307787228fe8ab25b0e1b5da80f5a543ce7d3e0aea`)

## components (1 claim(s))

- [observation/documented] Workflow files to be pushed live in a 'workflows' directory, which already includes a CodeQL workflow file. -- evidence: [README.md#L31-L35](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L31-L35), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17) (`clm_0df66f3ae78c05abea0975178045485cc8299ae2b9935b193a57535dcc6fd196`)

## design-choices (1 claim(s))

- [observation/documented] Authentication uses a .env file (renamed from .env-example) holding a GitHub token with the repo scope, authorized for SSO when the organization requires it. -- evidence: [README.md#L31-L35](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L31-L35), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17) (`clm_0182a7c5a5b0ab0d84a1d1d8ad03ef9a1a80680f62a91a43cae28d0e868dd9ff`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The tool exposes PowerShell commands CreatePullRequestForRepositories, CreatePullRequestsFromFile, and CreatePullRequestsForCodeQLLanguages, run after installing via ./Create-ActionsPRs.ps1. -- evidence: [README.md#L31-L35](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L31-L35), [README.md#L22-L28](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L22-L28), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17) (`clm_9aa421c20fa8fc6e90a39f376eda615373f239c97756933d60748eb15fec5c40`)
- [observation/documented] PR creation commands accept CommitMessage, PRBody, and BranchName parameters to customize the resulting pull requests. -- evidence: [README.md#L22-L28](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L22-L28), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17) (`clm_57b5196c83192534e18b5565101f6029e92f73c6242a00b9b3907cf2e7315c6b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] One mode targets all repositories in an organization using GetReposFromOrganization, creating PRs in every repository where the user has push permissions. -- evidence: [README.md#L19-L19](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L19-L19), [README.md#L12-L17](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L12-L17) (`clm_5dd261b65deeccba5f49db36f7ffcad49a5129c3331172aa5d357a9fbd67c86d`)
- [observation/documented] Another mode reads a user-created file of repository URLs, one per line, and creates PRs for those repositories via CreatePullRequestsFromFile. -- evidence: [README.md#L22-L28](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L22-L28) (`clm_58e9a0e3ce31723c29588b00429d0b55a1903faaff7e761d45ad03add8cd8559`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are PowerShell, git configured for GitHub access (with SSH key setup guidance), and the GitHub CLI. -- evidence: [README.md#L5-L7](https://github.com/jhutchings1/Create-ActionsPRs/blob/e10f42920c1f01eb2c0cb9014afcbfffe8f943a9/README.md#L5-L7) (`clm_40ec941cf5b6ca6994040e95c493a00de8085c5282e858e5341681e958f6d0d8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

