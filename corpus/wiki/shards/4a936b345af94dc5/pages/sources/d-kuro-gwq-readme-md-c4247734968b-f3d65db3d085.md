---
access: public
aliases: []
claim_ids:
- clm_0cadeb6a36d409e0cb419b90f4174c914f962ee1f4f80966de22d36a084d87c3
- clm_164b95f801e99deb7557780d5865e388fcc345210150a7b9d8e63d6a55df4aea
- clm_5130a8f5cf0854f85ac00097eb5126d919a0a0b668b210af37002e56f6b51c77
- clm_5dcd0bde4228996289ce35903bec6e0476078a104eec2ad37afc0dab35d1a122
- clm_671990e08de1c5fdbf50b07290c9b879cb363bd213c9b6dabd2cf588353c6459
- clm_86a0f270b9d76f6c3bf885d239d46a9d15151f4c14cfc0249cc7e4a0fc5a445d
- clm_a63cae1fd563bbc78b1c26143e013ea32969294204e3c131d85fce1858f93d35
- clm_e309c7cd5ff22e5344f5af2cf56f04cf3e327ce1b9470d11a572c3883df8c725
- clm_e48a0f7117c7a9abea400e100095f0034be2ec0703c2c19c9637887b4c2db544
- clm_e918e9ec99f0ad6c53f14ef09370ae171e13d803b1e72db8fafacc3251917fb0
maturity: draft
page_id: pg_e8ed3cb20cde53d7b982f3d65db3d085
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_70460236cd1c5869915a51431d2f4e37
title: d-kuro/gwq/README.md @ c4247734968b
updated_at: '2026-09-14T03:44:22Z'
---

# d-kuro/gwq/README.md @ c4247734968b

<!-- rcw:begin owner=source:src_70460236cd1c5869915a51431d2f4e37 block=evidence -->
- gwq generates shell completions for Bash, Zsh, Fish, and PowerShell via a completion subcommand. [@claim:clm_0cadeb6a36d409e0cb419b90f4174c914f962ee1f4f80966de22d36a084d87c3]
- Per-repository setup_commands are rendered with Go text/template (variables like {{.Branch}} and {{.Path}}) and executed via POSIX sh -c; unknown template keys cause the command to be skipped with an error logged. [@claim:clm_164b95f801e99deb7557780d5865e388fcc345210150a7b9d8e63d6a55df4aea]
- gwq is positioned for parallel AI coding agent workflows: multiple agents work in isolated worktrees simultaneously, monitored via gwq status --watch, without merge conflicts. [@claim:clm_5130a8f5cf0854f85ac00097eb5126d919a0a0b668b210af37002e56f6b51c77]
- PowerShell is not supported for shell integration, and the v0.0.1 release was explicitly labeled experimental with possible breaking changes in future versions. [@claim:clm_5dcd0bde4228996289ce35903bec6e0476078a104eec2ad37afc0dab35d1a122]
- Setup commands are described as a code-execution vector, and local .gwq.toml files must be trusted before they run, referencing a trust prompt mechanism. [@claim:clm_671990e08de1c5fdbf50b07290c9b879cb363bd213c9b6dabd2cf588353c6459]
- Configuration uses a global TOML file (~/.config/gwq/config.toml) plus a local .gwq.toml that takes precedence, with repository_settings merged by repository key where local overrides global for the same repository. [@claim:clm_86a0f270b9d76f6c3bf885d239d46a9d15151f4c14cfc0249cc7e4a0fc5a445d]
- Worktrees are organized in a URL-based hierarchy (e.g. ~/worktrees/github.com/user/repo/branch) to prevent naming conflicts, with a configurable naming template. [@claim:clm_a63cae1fd563bbc78b1c26143e013ea32969294204e3c131d85fce1858f93d35]
- Requirements are Git 2.5+ for worktree support and Go 1.24+ for building from source; release notes also mention a dependency update to github.com/bmatcuk/doublestar/v4 v4.10.0. [@claim:clm_e309c7cd5ff22e5344f5af2cf56f04cf3e327ce1b9470d11a572c3883df8c725]
- The status command supports watch mode, filtering, sorting, and JSON/CSV output formats per its documented flags. [@claim:clm_e48a0f7117c7a9abea400e100095f0034be2ec0703c2c19c9637887b4c2db544]
- Global worktree discovery uses filesystem scanning of a configured base directory rather than a separate registry, and behavior is context-aware inside versus outside Git repositories. [@claim:clm_e918e9ec99f0ad6c53f14ef09370ae171e13d803b1e72db8fafacc3251917fb0]
<!-- rcw:end owner=source:src_70460236cd1c5869915a51431d2f4e37 block=evidence -->

## Researcher notes

