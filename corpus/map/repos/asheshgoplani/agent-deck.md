# asheshgoplani/agent-deck

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7d2302fb8a41 @ 5d1b37ace8d9fdef

## Summary (orientation draft, not independently verified)

Agent Deck is documented as a terminal command center for many AI coding-agent sessions, with git-worktree isolation per session, a documented setup/destruction script contract around worktree lifecycle, a Docker sandbox mode, session forking, and two supported bare-repository layout conventions.

## Source coverage

Source coverage (partial): 2 of 62 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes Agent Deck as a command center for managing many AI coding-agent sessions (such as Claude Code and OpenCode) from one terminal, with grouping, search, forking, git worktrees, cost tracking, and a phone-controlled conductor. -- evidence: [README.md#L22-L22](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L22-L22)
- components (2 claim(s)):
  - [observation/documented] Documentation states each session's git worktree is an isolated working directory on its own branch, letting multiple agents work on one repository without conflicting, and a dedicated command merges the branch, removes the worktree, and deletes the session once a task is finished. -- evidence: [README.md#L321-L321](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L321-L321), [README.md#L323-L326](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L323-L326)
  - [observation/documented] Documentation states forking a Claude, OpenCode, Pi, or Codex session inherits the parent conversation history through each tool's own native fork support, and that Codex forking specifically needs a Codex CLI build with fork support, which the project reports verifying against one named CLI version. -- evidence: [README.md#L150-L150](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L150-L150), [README.md#L152-L154](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L152-L154)
- design-choices (1 claim(s)):
  - [observation/documented] The docs describe supporting two bare-repository worktree layout conventions, distinguished by whether the bare git directory is named .bare inside a project folder or is itself the project root, with worktree placement and config resolution differing between the two. -- evidence: [README.md#L400-L400](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L400-L400), [README.md#L432-L432](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L432-L432)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project states every incoming pull request is validated - applied, built, and tested - within about a day, and points contributors to CONTRIBUTING.md and a pinned onboarding issue. -- evidence: [README.md#L28-L28](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L28-L28), [README.md#L34-L36](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L34-L36)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] A documented worktree-setup script runs automatically once a worktree is created, under a 60-second timeout; if the script fails, documentation states the worktree is still created and only a warning is shown, rather than the session being blocked. -- evidence: [README.md#L372-L373](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L372-L373), [README.md#L384-L384](https://github.com/asheshgoplani/agent-deck/blob/7d2302fb8a41c5fcab7a441d56729b4b6547885a/README.md#L384-L384)
More evidence: [full detail](agent-deck.detail.md)

Metadata and full claim list: [full detail](agent-deck.detail.md)
Human notes ([notes](agent-deck.notes.md), never overwritten by build)

[Back to map index](../../index.md)
