---
access: public
aliases: []
claim_ids:
- clm_0182a7c5a5b0ab0d84a1d1d8ad03ef9a1a80680f62a91a43cae28d0e868dd9ff
- clm_0df66f3ae78c05abea0975178045485cc8299ae2b9935b193a57535dcc6fd196
- clm_40ec941cf5b6ca6994040e95c493a00de8085c5282e858e5341681e958f6d0d8
- clm_57b5196c83192534e18b5565101f6029e92f73c6242a00b9b3907cf2e7315c6b
- clm_58e9a0e3ce31723c29588b00429d0b55a1903faaff7e761d45ad03add8cd8559
- clm_5dd261b65deeccba5f49db36f7ffcad49a5129c3331172aa5d357a9fbd67c86d
- clm_9aa421c20fa8fc6e90a39f376eda615373f239c97756933d60748eb15fec5c40
- clm_ddec173ab775c5b335bdca307787228fe8ab25b0e1b5da80f5a543ce7d3e0aea
maturity: draft
page_id: pg_6a3378d111fa5901bf5a1855c0d5ec9b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e699a666b3745abfb1623ccac9db4c0a
title: jhutchings1/Create-ActionsPRs/README.md @ e10f42920c1f
updated_at: '2026-09-14T04:00:37Z'
---

# jhutchings1/Create-ActionsPRs/README.md @ e10f42920c1f

<!-- rcw:begin owner=source:src_e699a666b3745abfb1623ccac9db4c0a block=evidence -->
- Authentication uses a .env file (renamed from .env-example) holding a GitHub token with the repo scope, authorized for SSO when the organization requires it. [@claim:clm_0182a7c5a5b0ab0d84a1d1d8ad03ef9a1a80680f62a91a43cae28d0e868dd9ff]
- Workflow files to be pushed live in a 'workflows' directory, which already includes a CodeQL workflow file. [@claim:clm_0df66f3ae78c05abea0975178045485cc8299ae2b9935b193a57535dcc6fd196]
- Prerequisites are PowerShell, git configured for GitHub access (with SSH key setup guidance), and the GitHub CLI. [@claim:clm_40ec941cf5b6ca6994040e95c493a00de8085c5282e858e5341681e958f6d0d8]
- PR creation commands accept CommitMessage, PRBody, and BranchName parameters to customize the resulting pull requests. [@claim:clm_57b5196c83192534e18b5565101f6029e92f73c6242a00b9b3907cf2e7315c6b]
- Another mode reads a user-created file of repository URLs, one per line, and creates PRs for those repositories via CreatePullRequestsFromFile. [@claim:clm_58e9a0e3ce31723c29588b00429d0b55a1903faaff7e761d45ad03add8cd8559]
- One mode targets all repositories in an organization using GetReposFromOrganization, creating PRs in every repository where the user has push permissions. [@claim:clm_5dd261b65deeccba5f49db36f7ffcad49a5129c3331172aa5d357a9fbd67c86d]
- The tool exposes PowerShell commands CreatePullRequestForRepositories, CreatePullRequestsFromFile, and CreatePullRequestsForCodeQLLanguages, run after installing via ./Create-ActionsPRs.ps1. [@claim:clm_9aa421c20fa8fc6e90a39f376eda615373f239c97756933d60748eb15fec5c40]
- The repository's script creates pull requests that push a GitHub Actions workflow to multiple repositories. [@claim:clm_ddec173ab775c5b335bdca307787228fe8ab25b0e1b5da80f5a543ce7d3e0aea]
<!-- rcw:end owner=source:src_e699a666b3745abfb1623ccac9db4c0a block=evidence -->

## Researcher notes

