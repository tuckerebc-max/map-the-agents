---
access: public
aliases: []
claim_ids:
- clm_147a10f8112622078b21254da35dcbcba78b2db2b03c73ddeeb5bad6e08a9e77
- clm_1a9e72c3ae1e7b08d45b5a7e07c36ed6a9a2a76b51a78200c48d49599a291c7c
- clm_50f6ec0cc6e769ea015cc3873815b15dd42b7877b3175c4d91ed2a302bad7814
- clm_538d46c91e0c77de6e61fd85265c6a8dd3c3f83e5d77c5a424303c3aff083298
- clm_5db25d72190bd966017afcfbc976d6926a46a05b8b7082c6122b946ba8bc2c59
- clm_70f4b0d5f44843c0dd4bc024cdcdb29bc44ff9c048174e8026a6843e8af78840
- clm_8da53ad7e76084d500a4ac33facd157cfe01a56f606413c1643533d545884d90
- clm_d6d8dad287b08e63c3f61e696b03bf72e1932f058303dfc12ba6a3c1034f29a8
maturity: draft
page_id: pg_267520dd0c6352de97b425bfddd59e1e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f336b6278b9559e28285acfeedc96a95
title: asheshgoplani/agent-deck/README.md @ 7d2302fb8a41
updated_at: '2026-09-14T02:48:49Z'
---

# asheshgoplani/agent-deck/README.md @ 7d2302fb8a41

<!-- rcw:begin owner=source:src_f336b6278b9559e28285acfeedc96a95 block=evidence -->
- The documented Docker sandbox bind-mounts the project directory read-write into an isolated container and shares host tool authentication automatically, except that the macOS Claude Code login keeps its own sandbox credential to avoid disrupting the host's OAuth session. [@claim:clm_147a10f8112622078b21254da35dcbcba78b2db2b03c73ddeeb5bad6e08a9e77]
- Documentation states forking a Claude, OpenCode, Pi, or Codex session inherits the parent conversation history through each tool's own native fork support, and that Codex forking specifically needs a Codex CLI build with fork support, which the project reports verifying against one named CLI version. [@claim:clm_1a9e72c3ae1e7b08d45b5a7e07c36ed6a9a2a76b51a78200c48d49599a291c7c]
- The README describes Agent Deck as a command center for managing many AI coding-agent sessions (such as Claude Code and OpenCode) from one terminal, with grouping, search, forking, git worktrees, cost tracking, and a phone-controlled conductor. [@claim:clm_50f6ec0cc6e769ea015cc3873815b15dd42b7877b3175c4d91ed2a302bad7814]
- Repository development practice: the project states every incoming pull request is validated - applied, built, and tested - within about a day, and points contributors to CONTRIBUTING.md and a pinned onboarding issue. [@claim:clm_538d46c91e0c77de6e61fd85265c6a8dd3c3f83e5d77c5a424303c3aff083298]
- A documented worktree-setup script runs automatically once a worktree is created, under a 60-second timeout; if the script fails, documentation states the worktree is still created and only a warning is shown, rather than the session being blocked. [@claim:clm_5db25d72190bd966017afcfbc976d6926a46a05b8b7082c6122b946ba8bc2c59]
- Documentation states each session's git worktree is an isolated working directory on its own branch, letting multiple agents work on one repository without conflicting, and a dedicated command merges the branch, removes the worktree, and deletes the session once a task is finished. [@claim:clm_70f4b0d5f44843c0dd4bc024cdcdb29bc44ff9c048174e8026a6843e8af78840]
- The docs describe supporting two bare-repository worktree layout conventions, distinguished by whether the bare git directory is named .bare inside a project folder or is itself the project root, with worktree placement and config resolution differing between the two. [@claim:clm_8da53ad7e76084d500a4ac33facd157cfe01a56f606413c1643533d545884d90]
- Documentation states that inheriting sparse-checkout patterns into a new worktree requires Git 2.32 or newer, while the default, non-inheriting checkout behavior carries no such version requirement. [@claim:clm_d6d8dad287b08e63c3f61e696b03bf72e1932f058303dfc12ba6a3c1034f29a8]
<!-- rcw:end owner=source:src_f336b6278b9559e28285acfeedc96a95 block=evidence -->

## Researcher notes

