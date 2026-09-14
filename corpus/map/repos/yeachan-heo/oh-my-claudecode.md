# yeachan-heo/oh-my-claudecode

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5281b19e0d64 @ 1fded3a5854f6853

## Summary (orientation draft, not independently verified)

The README documents oh-my-claudecode (npm package oh-my-claude-sisyphus), a multi-agent orchestration layer for Claude Code with terminal CLI and in-session skill surfaces, team/autopilot orchestration modes, custom skills, .omc state management, and external provider integrations. Evidence coverage: 144 of 255 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 65 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: CONTRIBUTING.md is the developer guide covering forking, local checkout setup, linking as the active plugin, running tests, and submitting PRs. -- evidence: [README.md#L338-L338](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L338-L338)
- skills-patterns (1 claim(s)):
  - [observation/documented] Custom skills are stored at `.omc/skills/` (project, higher priority) or `~/.omc/skills/` (user fallback), with frontmatter triggers, and matching skills auto-inject into context; `/skillify` extracts patterns with quality gates. -- evidence: [README.md#L352-L359](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L352-L359), [README.md#L361-L363](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L361-L363), [README.md#L344-L348](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L344-L348)
- interfaces (3 claim(s)):
  - [observation/documented] OMC exposes two surfaces: terminal CLI commands (`omc ...`) run from a shell, and in-session slash skills (`/...`) run inside a Claude Code session after plugin setup. -- evidence: [README.md#L141-L142](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L141-L142)
  - [observation/documented] The npm package installs both `oh-my-claudecode` and a short `omc` command alias, while the repo/plugin branding is oh-my-claudecode. -- evidence: [README.md#L245-L245](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L245-L245), [README.md#L255-L255](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L255-L255)
- memory-state (2 claim(s)):
  - [observation/documented] OMC writes runtime state, session data, plans, logs, and artifacts under `.omc/` by default; gitignore keeps it local except `.omc/skills/**` which stays committable, and `OMC_STATE_DIR` or a `.omc-workspace` marker can relocate or share state. -- evidence: [README.md#L371-L371](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L371-L371), [README.md#L369-L369](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L369-L369), [README.md#L379-L379](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L379-L379)
  - [observation/documented] Outside a git repository OMC uses a canonical state root at `~/.omc/` (or `$OMC_STATE_DIR/non-git`) and avoids creating per-cwd state roots or writing into sensitive directories like `~/.ssh` or `~/Downloads`. -- evidence: [README.md#L373-L373](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L373-L373)
- orchestration (3 claim(s)):
  - [observation/documented] Team is the canonical orchestration surface as of v4.1.7, running a staged pipeline: team-plan, team-prd, team-exec, team-verify, and team-fix (loop); the legacy `swarm` alias was removed. -- evidence: [README.md#L181-L181](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L181-L181), [README.md#L171-L171](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L171-L171), [README.md#L412-L414](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L412-L414)
  - [observation/documented] `omc team N:<provider>` spawns on-demand tmux worker panes for claude, codex, gemini, antigravity, grok, or cursor CLIs; workers die when their task completes, and the selected CLI plus tmux must be installed and authenticated. -- evidence: [README.md#L199-L207](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L199-L207), [README.md#L216-L224](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L216-L224), [README.md#L226-L226](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L226-L226)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](oh-my-claudecode.detail.md)

Metadata and full claim list: [full detail](oh-my-claudecode.detail.md)
Human notes ([notes](oh-my-claudecode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
