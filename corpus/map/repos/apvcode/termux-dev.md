# apvcode/termux-dev

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a87cf5f64332 @ 0ede1806afb1f442

## Summary (orientation draft, not independently verified)

The snapshot contains only README content for 'devx' (termux-dev), a terminal AI coding agent for Termux/Windows/macOS/Linux distributed via npm. Claims below are documentation-based descriptions of its advertised CLI, modes, commands, and memory features.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The product includes a built-in local HTTP server (/serve, default port 3000) for previewing web apps and HTML5 games, opening on Android via termux-open-url. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54)
  - [observation/documented] Self-healing diagnostics run external checkers for TypeScript (tsc), JavaScript (node --check), Python (py_compile), and Rust (cargo check), with the AI fixing errors before finishing a turn. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54)
- design-choices (2 claim(s)):
  - [observation/documented] The agent uses a dual-mode architecture: PLAN mode acts as a safe architect with a requirements questionnaire and no code edits, while AGENT mode autonomously edits files, runs terminal commands, and installs packages. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54)
  - [observation/documented] Finalized architectural plans are approved via a one-click `[Go / Other]` prompt, after which the coder agent begins implementation. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: developers can build from source by cloning the GitHub repo, running npm install, and npm link; a CI workflow badge (ci.yml) is shown in the README. -- evidence: [README.md#L85-L90](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L85-L90), [README.md#L10-L15](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L10-L15)
  - [observation/documented] Repository development practice: complete uninstall instructions cover removing the global npm package plus ~/.devx and ~/.devxrc.json on Unix-like systems, with equivalent PowerShell commands for Windows. -- evidence: [README.md#L94-L94](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L94-L94), [README.md#L101-L101](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L101-L101), [README.md#L104-L105](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L104-L105)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is launched as `devx`, supports starting in PLAN mode via `--plan`, and offers a headless one-shot mode using `-p "<prompt>"` with an optional `--yolo` flag. -- evidence: [README.md#L117-L126](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L117-L126)
  - [observation/documented] A slash-command palette (opened by typing `/`) includes commands such as /plan, /agent, /mcp, /usage, /export, /theme, /doctor, /image, /serve, /memory, /undo, /diff, /commit, /status, /session, /resume, /settings, and /update. -- evidence: [README.md#L134-L161](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L134-L161), [README.md#L132-L132](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L132-L132)
- memory-state (2 claim(s)):
  - [observation/documented] A persistent project memory bank is stored in `.devx/memory.md` and managed with `/memory add <rule>`, intended to carry project context across sessions. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54)
  - [observation/documented] Sessions are saved and can be listed, resumed, or deleted via /resume, /session, and /session del; /resume reportedly renders the last 20 messages of a session. -- evidence: [README.md#L134-L161](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L134-L161), [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](termux-dev.detail.md)

Metadata and full claim list: [full detail](termux-dev.detail.md)
Human notes ([notes](termux-dev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
