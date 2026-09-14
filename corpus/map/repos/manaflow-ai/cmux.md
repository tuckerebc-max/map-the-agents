# manaflow-ai/cmux

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 419cf0a00cc3 @ 7737fb865abe78b6

## Summary (orientation draft, not independently verified)

The evidence is mostly README documentation for cmux, a native macOS (Swift/AppKit, libghostty-based) terminal for AI coding agents with notifications, an embedded scriptable browser, CLI/socket API, and session restore; plus a CLA and a PR audit document describing repository development/verification practice. Evidence: 6 of 31 candidate files stored (README.md, CLA.md, PR-10599-AUDIT.md, PROJECTS.md, and two translated READMEs); 25 omitted by file budget, including AGENTS.md and CONTRIBUTING.md; the repository's own file tree was truncated, so the candidate count is a partial listing, not the whole repository.

## Source coverage

Source coverage (partial): 6 of 31 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] cmux is a native macOS app built with Swift and AppKit (not Electron), using libghostty for GPU-accelerated terminal rendering. -- evidence: [README.md#L87-L94](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L87-L94), [README.md#L332-L332](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L332-L332), [README.md#L125-L125](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L125-L125)
  - [observation/documented] An in-app browser can be split beside the terminal, with a scriptable API ported from vercel-labs/agent-browser for snapshotting, clicking, filling forms, and evaluating JavaScript. -- evidence: [README.md#L30-L85](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L30-L85), [README.md#L364-L364](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L364-L364), [README.md#L129-L129](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L129-L129)
- design-choices (2 claim(s)):
  - [observation/documented] cmux positions itself as a non-prescriptive primitive: a terminal, browser, notifications, workspaces, splits, tabs, and CLI, without forcing an opinionated agent workflow. -- evidence: [README.md#L135-L135](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L135-L135), [README.md#L137-L137](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L137-L137)
  - [observation/documented] Resume bindings are security-gated: only trusted bindings auto-run, approved command prefixes are bound to working directory and environment values, and sensitive environment keys are dropped before storage. -- evidence: [README.md#L292-L299](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L292-L299)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors must sign a CLA (v2.2), which can be signed electronically by posting an exact phrase as a PR comment; the PR audit notes the contributor's unsigned CLA as an external blocker. -- evidence: [PR-10599-AUDIT.md#L87-L90](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L87-L90), [PR-10599-AUDIT.md#L142-L144](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L142-L144), [CLA.md#L5-L5](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/CLA.md#L5-L5)
  - [observation/documented] Repository development practice: the PR #10599 audit records focused Swift package test runs (e.g., 11 tests in CmuxFilePreviewCore, 24 in CmuxSyntaxHighlighting) plus project lint/check scripts such as check-pbxproj.sh and lint-pbxproj-test-wiring.sh. -- evidence: [PR-10599-AUDIT.md#L99-L110](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L99-L110)
- skills-patterns (1 claim(s)):
  - [observation/documented] cmux supports reusable skills for agents running in it (CLI control, workspace automation, settings, browser surfaces), with an open collection in the manaflow-ai/cmux-skills repository. -- evidence: [README.md#L368-L368](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L368-L368)
- interfaces (4 claim(s)):
  - [observation/documented] The product exposes a CLI and Unix socket API to create workspaces, split panes, send keystrokes, read screen contents, take screenshots, and drive the in-app browser. -- evidence: [README.md#L87-L94](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L87-L94), [README.md#L131-L131](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L131-L131), [README.md#L360-L360](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L360-L360)
  - [observation/documented] cmux provides a `cmux notify` CLI and picks up OSC 9/99/777 terminal escape sequences to trigger notifications, usable from agent hooks. -- evidence: [README.md#L356-L356](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L356-L356), [README.md#L127-L127](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L127-L127)
- memory-state (2 claim(s)):
More evidence: [full detail](cmux.detail.md)

Metadata and full claim list: [full detail](cmux.detail.md)
Human notes ([notes](cmux.notes.md), never overwritten by build)

[Back to map index](../../index.md)
