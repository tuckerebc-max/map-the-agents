# smtg-ai/claude-squad

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ce1ffb4392b0 @ 930f92076f14d5f0

## Summary (orientation draft, not independently verified)

Claude Squad is a terminal TUI app that manages multiple AI coding agents (Claude Code, Codex, Gemini, Aider) in isolated tmux/git-worktree workspaces. Evidence covers its CLI, keybindings, configuration, and contributor docs; no code internals or evaluation results are shown.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Claude Squad is a terminal application that manages multiple local AI coding agents such as Claude Code, Codex, Gemini, and Aider in separate workspaces for parallel tasks. -- evidence: [README.md#L3-L3](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The app uses tmux for isolated per-agent terminal sessions and git worktrees so each session works on its own branch, with a TUI for navigation. -- evidence: [README.md#L152-L154](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L152-L154)
  - [observation/documented] Profiles allow named program configurations selectable at session creation; a `profiles` array with name/program fields and `default_program` is set in the config file. -- evidence: [README.md#L119-L119](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L119-L119), [README.md#L136-L139](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L136-L139), [README.md#L123-L132](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L123-L132), [README.md#L121-L121](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L121-L121)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork and clone the repo, add upstream, run `go mod download`, lint with `gofmt -w .`, and should include tests for new features or fixes. -- evidence: [CONTRIBUTING.md#L18-L20](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CONTRIBUTING.md#L18-L20), [CONTRIBUTING.md#L24-L24](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CONTRIBUTING.md#L24-L24), [CONTRIBUTING.md#L7-L10](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CONTRIBUTING.md#L7-L10)
  - [observation/documented] Repository development practice: contributors accept a CLA via the CLA assistant bot on their first pull request, granting copyright, patent, and relicensing rights to maintainers. -- evidence: [CLA.md#L43-L43](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L43-L43), [CLA.md#L19-L19](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L19-L19), [CLA.md#L35-L35](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L35-L35), [CLA.md#L17-L17](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L17-L17)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is invoked as `cs` with subcommands including completion, debug, help, reset, and version, plus flags like --autoyes and --program. -- evidence: [README.md#L22-L22](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L22-L22), [README.md#L54-L57](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L54-L57), [README.md#L59-L64](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L59-L64), [README.md#L66-L70](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L66-L70)
  - [observation/documented] Keybindings support session creation (`n`, `N`), deletion (`D`), attach/detach (`↵/o`, ctrl-q), commit-push (`s`), checkout (`c`), resume (`r`), and diff-view navigation. -- evidence: [README.md#L109-L111](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L109-L111), [README.md#L101-L106](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L101-L106), [README.md#L95-L98](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L95-L98)
- memory-state (1 claim(s)):
  - [observation/documented] Configuration is stored in `~/.claude-squad/config.json`, and the exact path can be found via `cs debug`. -- evidence: [README.md#L115-L115](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L115-L115)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] An experimental `-y/--autoyes` flag makes all instances automatically accept prompts for Claude Code and Aider; the README also mentions background yolo/auto-accept mode. -- evidence: [README.md#L9-L12](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L9-L12), [README.md#L66-L70](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L66-L70)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The product requires tmux and the GitHub CLI (gh) as prerequisites. -- evidence: [README.md#L49-L50](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L49-L50)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](claude-squad.detail.md)

Metadata and full claim list: [full detail](claude-squad.detail.md)
Human notes ([notes](claude-squad.notes.md), never overwritten by build)

[Back to map index](../../index.md)
