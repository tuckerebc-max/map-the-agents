# asheshgoplani/agent-deck -- full detail

[Back to orientation](agent-deck.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/asheshgoplani/agent-deck/7d2302fb8a41c5fcab7a441d56729b4b6547885a/5d1b37ace8d9fdef.json](../../../wiki/dossiers/asheshgoplani/agent-deck/7d2302fb8a41c5fcab7a441d56729b4b6547885a/5d1b37ace8d9fdef.json)

## specifications (1 claim(s))

- [observation/documented] The README describes Agent Deck as a command center for managing many AI coding-agent sessions (such as Claude Code and OpenCode) from one terminal, with grouping, search, forking, git worktrees, cost tracking, and a phone-controlled conductor. -- evidence: [README.md#L22-L22](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L22-L22) (`clm_50f6ec0cc6e769ea015cc3873815b15dd42b7877b3175c4d91ed2a302bad7814`)

## components (2 claim(s))

- [observation/documented] Documentation states each session's git worktree is an isolated working directory on its own branch, letting multiple agents work on one repository without conflicting, and a dedicated command merges the branch, removes the worktree, and deletes the session once a task is finished. -- evidence: [README.md#L321-L321](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L321-L321), [README.md#L323-L326](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L323-L326) (`clm_70f4b0d5f44843c0dd4bc024cdcdb29bc44ff9c048174e8026a6843e8af78840`)
- [observation/documented] Documentation states forking a Claude, OpenCode, Pi, or Codex session inherits the parent conversation history through each tool's own native fork support, and that Codex forking specifically needs a Codex CLI build with fork support, which the project reports verifying against one named CLI version. -- evidence: [README.md#L150-L150](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L150-L150), [README.md#L152-L154](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L152-L154) (`clm_1a9e72c3ae1e7b08d45b5a7e07c36ed6a9a2a76b51a78200c48d49599a291c7c`)

## design-choices (1 claim(s))

- [observation/documented] The docs describe supporting two bare-repository worktree layout conventions, distinguished by whether the bare git directory is named .bare inside a project folder or is itself the project root, with worktree placement and config resolution differing between the two. -- evidence: [README.md#L400-L400](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L400-L400), [README.md#L432-L432](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L432-L432) (`clm_8da53ad7e76084d500a4ac33facd157cfe01a56f606413c1643533d545884d90`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the project states every incoming pull request is validated - applied, built, and tested - within about a day, and points contributors to CONTRIBUTING.md and a pinned onboarding issue. -- evidence: [README.md#L28-L28](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L28-L28), [README.md#L34-L36](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L34-L36) (`clm_538d46c91e0c77de6e61fd85265c6a8dd3c3f83e5d77c5a424303c3aff083298`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] A documented worktree-setup script runs automatically once a worktree is created, under a 60-second timeout; if the script fails, documentation states the worktree is still created and only a warning is shown, rather than the session being blocked. -- evidence: [README.md#L372-L373](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L372-L373), [README.md#L384-L384](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L384-L384) (`clm_5db25d72190bd966017afcfbc976d6926a46a05b8b7082c6122b946ba8bc2c59`)
- [observation/documented] The documented Docker sandbox bind-mounts the project directory read-write into an isolated container and shares host tool authentication automatically, except that the macOS Claude Code login keeps its own sandbox credential to avoid disrupting the host's OAuth session. -- evidence: [README.md#L472-L472](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L472-L472), [README.md#L466-L466](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L466-L466) (`clm_147a10f8112622078b21254da35dcbcba78b2db2b03c73ddeeb5bad6e08a9e77`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Documentation states that inheriting sparse-checkout patterns into a new worktree requires Git 2.32 or newer, while the default, non-inheriting checkout behavior carries no such version requirement. -- evidence: [README.md#L348-L348](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L348-L348) (`clm_d6d8dad287b08e63c3f61e696b03bf72e1932f058303dfc12ba6a3c1034f29a8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

