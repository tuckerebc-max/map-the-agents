---
access: public
aliases: []
claim_ids:
- clm_0cadeb6a36d409e0cb419b90f4174c914f962ee1f4f80966de22d36a084d87c3
- clm_5130a8f5cf0854f85ac00097eb5126d919a0a0b668b210af37002e56f6b51c77
- clm_5dcd0bde4228996289ce35903bec6e0476078a104eec2ad37afc0dab35d1a122
- clm_a63cae1fd563bbc78b1c26143e013ea32969294204e3c131d85fce1858f93d35
- clm_e309c7cd5ff22e5344f5af2cf56f04cf3e327ce1b9470d11a572c3883df8c725
- clm_e918e9ec99f0ad6c53f14ef09370ae171e13d803b1e72db8fafacc3251917fb0
maturity: draft
page_id: pg_a2892eaa0a215b20a3bfa4e524ec7c94
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8f54858cf0185b0d9d792c6b0b590505
title: d-kuro/gwq/docs/release-notes/v0.0.1.md @ c4247734968b
updated_at: '2026-09-14T03:44:22Z'
---

# d-kuro/gwq/docs/release-notes/v0.0.1.md @ c4247734968b

<!-- rcw:begin owner=source:src_8f54858cf0185b0d9d792c6b0b590505 block=evidence -->
- gwq generates shell completions for Bash, Zsh, Fish, and PowerShell via a completion subcommand. [@claim:clm_0cadeb6a36d409e0cb419b90f4174c914f962ee1f4f80966de22d36a084d87c3]
- gwq is positioned for parallel AI coding agent workflows: multiple agents work in isolated worktrees simultaneously, monitored via gwq status --watch, without merge conflicts. [@claim:clm_5130a8f5cf0854f85ac00097eb5126d919a0a0b668b210af37002e56f6b51c77]
- PowerShell is not supported for shell integration, and the v0.0.1 release was explicitly labeled experimental with possible breaking changes in future versions. [@claim:clm_5dcd0bde4228996289ce35903bec6e0476078a104eec2ad37afc0dab35d1a122]
- Worktrees are organized in a URL-based hierarchy (e.g. ~/worktrees/github.com/user/repo/branch) to prevent naming conflicts, with a configurable naming template. [@claim:clm_a63cae1fd563bbc78b1c26143e013ea32969294204e3c131d85fce1858f93d35]
- Requirements are Git 2.5+ for worktree support and Go 1.24+ for building from source; release notes also mention a dependency update to github.com/bmatcuk/doublestar/v4 v4.10.0. [@claim:clm_e309c7cd5ff22e5344f5af2cf56f04cf3e327ce1b9470d11a572c3883df8c725]
- Global worktree discovery uses filesystem scanning of a configured base directory rather than a separate registry, and behavior is context-aware inside versus outside Git repositories. [@claim:clm_e918e9ec99f0ad6c53f14ef09370ae171e13d803b1e72db8fafacc3251917fb0]
<!-- rcw:end owner=source:src_8f54858cf0185b0d9d792c6b0b590505 block=evidence -->

## Researcher notes

