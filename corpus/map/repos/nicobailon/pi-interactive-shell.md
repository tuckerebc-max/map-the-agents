# nicobailon/pi-interactive-shell

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit eedb89a9e461 @ 8fd72b37ae0f9648

## Summary (orientation draft, not independently verified)

pi-interactive-shell is a Pi coding agent extension exposing an `interactive_shell` tool that runs interactive CLIs in a PTY-backed TUI overlay with four modes (interactive, hands-free, dispatch, monitor), background session management, structured spawn of coding agents, and configurable settings. Evidence is README/CHANGELOG documentation only; no source code slices are present. Evidence coverage: 142 of 223 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Architecture: interactive_shell routes through zigpty to the subprocess, with xterm-headless terminal emulation feeding a TUI overlay rendered by Pi; the subprocess gets a full PTY. -- evidence: [README.md#L556-L556](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L556-L556), [README.md#L548-L554](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L548-L554)
- design-choices (2 claim(s)):
  - [observation/documented] New sessions use Pi's Bash resolver rather than ambient $SHELL/COMSPEC; on Windows it discovers Git Bash, and legacy WSL stdin-only bash is rejected for interactive PTYs. -- evidence: [README.md#L442-L446](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L442-L446), [README.md#L457-L462](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L457-L462), [CHANGELOG.md#L15-L17](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/CHANGELOG.md#L15-L17)
  - [observation/documented] Dispatch defaults autoExitOnQuiet with a 15s startup grace period and 8s silence threshold; both are configurable per-call or globally via autoExitGracePeriod. -- evidence: [README.md#L156-L156](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L156-L156), [README.md#L295-L295](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L295-L295), [README.md#L305-L305](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L305-L305)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's example workflow templates are opt-in user-facing prompts to copy into agent config, not contributor contribution rules; no contributor/CI guidance appears in the provided slices. -- evidence: [README.md#L582-L582](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L582-L582)
- skills-patterns (1 claim(s)):
  - [observation/documented] Installation symlinks an interactive-shell skill into ~/.pi/agent/skills/, and optional example skills (codex-cli, cursor-cli, prompting skills) and prompt templates ship under examples/ for opt-in copy. -- evidence: [README.md#L594-L595](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L594-L595), [README.md#L582-L582](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L582-L582), [README.md#L589-L591](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L589-L591), [README.md#L33-L33](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L33-L33), [README.md#L86-L86](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L86-L86)
- interfaces (5 claim(s)):
  - [observation/documented] The extension exposes an `interactive_shell` tool for the Pi coding agent; end users do not call it directly but ask Pi in natural language or use /spawn, /attach, /dismiss commands. -- evidence: [README.md#L15-L15](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L15-L15), [README.md#L7-L7](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L7-L7)
  - [observation/documented] The tool supports four modes: interactive (default), hands-free, dispatch, and monitor, all returning immediately without the agent waiting. -- evidence: [README.md#L39-L44](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L39-L44)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions can be backgrounded by user (Ctrl+B/Ctrl+Q) or agent, listed via listBackground, reattached with a chosen mode, and dismissed individually or all at once. -- evidence: [README.md#L370-L370](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L370-L370), [README.md#L385-L388](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L385-L388), [README.md#L377-L378](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L377-L378), [README.md#L380-L383](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L380-L383)
- orchestration (3 claim(s)):
  - [observation/documented] Dispatch mode notifies the agent via triggerTurn on completion with a 5-line output tail; the PTY is preserved for 5 minutes so the agent can attach and review scrollback. -- evidence: [README.md#L50-L50](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L50-L50), [README.md#L154-L154](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L154-L154)
More evidence: [full detail](pi-interactive-shell.detail.md)

Metadata and full claim list: [full detail](pi-interactive-shell.detail.md)
Human notes ([notes](pi-interactive-shell.notes.md), never overwritten by build)

[Back to map index](../../index.md)
