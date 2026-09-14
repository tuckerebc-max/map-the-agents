# amix/dunk

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c82459356688 @ 39f303c315706246

## Summary (orientation draft, not independently verified)

Selected evidence records: The agent-facing comments CLI supports listing pending comments, showing one with 10 lines of post-image context (configurable via --context), and an atomic resolve that refuses partial success; --json returns a stable shape with drift state. Review comments are stored in .dunk/comments.json with the file path, hunk anchor line, body, and a context hash so comments survive small nearby edits; the file is meant to stay local and gitignored, and is deleted once the last comment is resolved.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] dunk exports a DunkDiffView component from dunkdiff/opentui so the diff renderer can be embedded in other OpenTUI applications. -- evidence: [README.md#L179-L179](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L179-L179)
- design-choices (3 claim(s)):
  - [observation/documented] Comments are hunk-scoped rather than line-scoped: the user picks a hunk with J/K and presses 'a' to comment, and drifted comments surface at the top of the diff (clearable with d/D) instead of getting lost. -- evidence: [README.md#L95-L95](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L95-L95), [README.md#L109-L109](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L109-L109), [README.md#L9-L14](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L9-L14), [README.md#L93-L93](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L93-L93)
  - [observation/documented] dunk is a hard fork of hunk that keeps the OpenTUI/Pierre diff-viewer foundation while removing the daemon, MCP, and session-broker layers; agent integration flows through the on-disk comments file. -- evidence: [README.md#L7-L7](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L7-L7), [CHANGELOG.md#L85-L88](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L85-L88)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use Bun commands (bun install, bun test, bun run typecheck/lint/format/test:integration/test:tty-smoke), colocate unit tests with source, keep tests in test/cli, test/pty, and test/smoke, follow Conventional Commits, and maintain CHANGELOG.md as the release-notes source of truth. -- evidence: [AGENTS.md#L106-L117](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L106-L117), [AGENTS.md#L70-L76](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L70-L76), [AGENTS.md#L158-L158](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L158-L158), [AGENTS.md#L139-L149](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L139-L149), [AGENTS.md#L127-L130](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L127-L130)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The agent-facing comments CLI supports listing pending comments, showing one with 10 lines of post-image context (configurable via --context), and an atomic resolve that refuses partial success; --json returns a stable shape with drift state. -- evidence: [CHANGELOG.md#L65-L71](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L65-L71)
  - [observation/documented] Configuration is read from ~/.config/dunk/config.toml or .dunk/config.toml, with keys for theme, layout mode, watch, exclude_untracked, line_numbers, wrap_lines, and selection_auto_copy; a CLI --watch flag overrides the config watch value. -- evidence: [README.md#L175-L175](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L175-L175), [README.md#L160-L161](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L160-L161), [README.md#L165-L173](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L165-L173)
- memory-state (1 claim(s)):
  - [observation/documented] Review comments are stored in .dunk/comments.json with the file path, hunk anchor line, body, and a context hash so comments survive small nearby edits; the file is meant to stay local and gitignored, and is deleted once the last comment is resolved. -- evidence: [README.md#L95-L95](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L95-L95), [CHANGELOG.md#L15-L15](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L15-L15), [README.md#L97-L97](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L97-L97)
- orchestration (1 claim(s)):
More evidence: [full detail](dunk.detail.md)

Metadata and full claim list: [full detail](dunk.detail.md)
Human notes ([notes](dunk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
