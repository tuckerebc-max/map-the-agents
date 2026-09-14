# 21st-dev/1code

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9f1bc76fa437 @ 963ce7c3d14e2d9a

## Summary (orientation draft, not independently verified)

1Code is documented as an open-source coding-agent client with isolated worktrees per chat, background cloud sandboxes, plan approval before execution, and custom skills and sub-agents. The inspected terminal module retries a failed shell launch and falls back to the home directory for an invalid working directory.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 2 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] 1Code is described as an open-source coding agent client for running Claude Code, Codex, and other coding agents locally or in the cloud. -- evidence: [README.md#L5-L5](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] Documented features include a Kanban board for visualizing agent sessions and a built-in Git client supporting staging, diffs, and pull request creation. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34)
  - [observation/code-inspected] The terminal session module's spawnPty function catches a failed PTY spawn and retries once using a fallback shell constant. -- evidence: [src/main/lib/terminal/session.ts#L93-L113](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L93-L113)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] The README states automations can be triggered from GitHub, Linear, or Slack events, or run manually from git events. -- evidence: [README.md#L109-L109](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L109-L109)
- skills-patterns (1 claim(s)):
  - [observation/documented] Documented features include custom skills and slash commands, plus custom sub-agents shown with a visual task display in the sidebar. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34)
- interfaces (1 claim(s)):
  - [observation/documented] The documented feature list includes a model selector for switching providers and an integrated terminal panel toggled with a Cmd+J shortcut. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34)
- memory-state (1 claim(s)):
  - [observation/documented] The documented feature list states the product supports persistent memory through CLAUDE.md and AGENTS.md files. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34)
- orchestration (1 claim(s)):
  - [observation/documented] Documentation states each chat session runs in its own isolated git worktree, and background agents execute in cloud sandboxes while the local machine sleeps. -- evidence: [README.md#L88-L88](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L88-L88), [README.md#L44-L48](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L44-L48)
- tools-permissions (1 claim(s)):
  - [observation/documented] Plan mode documentation states the agent's proposed plan must be reviewed and approved, or modified, by the user before the agent acts. -- evidence: [README.md#L77-L82](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L77-L82)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Build-from-source documentation states Python 3.11 is recommended for native module rebuilds, and setuptools must be installed manually on Python 3.12 and newer. -- evidence: [README.md#L153-L155](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L153-L155)
- limitations (1 claim(s)):
  - [observation/code-inspected] The terminal session code falls back to the user's home directory when the requested working directory does not exist or is not a directory. -- evidence: [src/main/lib/terminal/session.ts#L32-L43](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L32-L43), [src/main/lib/terminal/session.ts#L21-L30](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L21-L30)
- relevance (1 claim(s)):
More evidence: [full detail](1code.detail.md)

Metadata and full claim list: [full detail](1code.detail.md)
Human notes ([notes](1code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
