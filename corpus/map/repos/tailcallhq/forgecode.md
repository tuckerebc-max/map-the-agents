# tailcallhq/forgecode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6ed5d37b6b45 @ 495877cd934128c0

## Summary (orientation draft, not independently verified)

Forge offers three usage modes: an interactive terminal UI launched by running `forge` with no arguments, a one-shot CLI mode via `-p`/`--prompt`, and a ZSH plugin mode using `:` prefix commands. CLI options include `-p` for direct prompts, `--agent` to pick an agent, `-C` to change directory, `--sandbox` to create an isolated git worktree plus branch, and `--conversation-id` to resume a conversation. Evidence coverage: 180 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Forge ships three built-in agents: `forge` (implementation, modifies files), `sage` (read-only research), and `muse` (planning, writes plans to `plans/`). -- evidence: [README.md#L245-L249](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L245-L249), [README.md#L243-L243](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L243-L243)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README badges indicate a CI workflow (ci.yml), GitHub releases, a Discord community, and CLA assistant for contributions. -- evidence: [README.md#L6-L9](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L6-L9)
- skills-patterns (2 claim(s)):
  - [observation/documented] Three built-in skills ship with Forge: create-skill, execute-plan, and github-pr-description; skills are reusable workflows the AI can invoke as tools. -- evidence: [README.md#L338-L340](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L338-L340), [README.md#L336-L336](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L336-L336)
  - [observation/documented] Custom skills are SKILL.md files with YAML front-matter, resolved with precedence: project-local `.forge/skills/` over global `~/forge/skills/` over built-in skills embedded in the binary. -- evidence: [README.md#L346-L350](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L346-L350), [README.md#L352-L352](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L352-L352), [README.md#L344-L344](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L344-L344)
- interfaces (3 claim(s)):
  - [observation/documented] Forge offers three usage modes: an interactive terminal UI launched by running `forge` with no arguments, a one-shot CLI mode via `-p`/`--prompt`, and a ZSH plugin mode using `:` prefix commands. -- evidence: [README.md#L216-L216](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L216-L216), [README.md#L201-L201](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L201-L201), [README.md#L182-L182](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L182-L182), [README.md#L186-L186](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L186-L186)
  - [observation/documented] CLI options include `-p` for direct prompts, `--agent` to pick an agent, `-C` to change directory, `--sandbox` to create an isolated git worktree plus branch, and `--conversation-id` to resume a conversation. -- evidence: [README.md#L415-L426](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L415-L426)
- memory-state (2 claim(s)):
  - [observation/documented] Forge saves every conversation and provides commands to list, resume, clone, rename, delete, dump as JSON/HTML, compact, and retry conversations, including toggling to the previous one. -- evidence: [README.md#L432-L443](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L432-L443), [README.md#L273-L273](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L273-L273), [README.md#L275-L290](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L275-L290)
  - [observation/documented] An AGENTS.md file in the project root or `~/forge/AGENTS.md` gives agents persistent instructions, and Forge reads it automatically at the start of every conversation. -- evidence: [README.md#L356-L356](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L356-L356)
- orchestration (1 claim(s)):
  - [observation/documented] Forge supports MCP servers with subcommands to list, import, show, remove, and reload configured servers. -- evidence: [README.md#L469-L473](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L469-L473)
- tools-permissions (1 claim(s)):
More evidence: [full detail](forgecode.detail.md)

Metadata and full claim list: [full detail](forgecode.detail.md)
Human notes ([notes](forgecode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
