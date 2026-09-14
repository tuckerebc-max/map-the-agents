# timvw/tmux-assistant-resurrect

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4d740923614a @ 819817bffcc019b3

## Summary (orientation draft, not independently verified)

A tmux-resurrect plugin that saves and restores AI coding assistant sessions (Claude Code, Cursor, Copilot, OpenCode, Codex, Pi, Oh My Pi, Grok) by detecting assistant processes, extracting session IDs via hooks/plugins/process args, and replaying resume commands after tmux restarts. Evidence is README-only documentation of the product's design, configuration, and testing workflow. Evidence coverage: 134 of 163 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository contains a TPM plugin entry point, hook scripts for Claude/Cursor session tracking and cleanup, an OpenCode session-tracker plugin, and save/restore hook scripts under scripts/. -- evidence: [README.md#L158-L182](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L158-L182)
- design-choices (2 claim(s)):
  - [observation/documented] Assistant detection is done by taking a single ps snapshot, finding children of each tmux pane shell, and matching known assistant binary names such as claude, copilot, opencode, codex, pi, omp, and grok. -- evidence: [README.md#L57-L60](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L57-L60)
  - [observation/documented] Each supported tool has a primary session-ID extraction method plus fallbacks (e.g. hook state files, process args, transcript or SQLite lookups) to handle cases where hooks have not yet fired after a restore. -- evidence: [README.md#L75-L78](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L75-L78), [README.md#L64-L73](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L64-L73)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the full test suite runs in Docker with real CLI binaries via 'just test', covering install, save, restore, uninstall, hooks, session ID extraction, and regression scenarios; fast hermetic suites exist for save hardening, restore, cursor, and plugin hardening. -- evidence: [README.md#L188-L188](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L188-L188), [README.md#L190-L192](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L190-L192), [README.md#L203-L211](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L203-L211), [README.md#L196-L201](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L196-L201)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The plugin exposes tmux options including @assistant-resurrect-capture-env for extra environment variables, per-tool and global drop-flags/drop-env exclusions, @assistant-resurrect-relaunch, and a save-timeout watchdog option. -- evidence: [README.md#L687-L689](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L687-L689), [README.md#L476-L478](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L476-L478), [README.md#L551-L554](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L551-L554), [README.md#L564-L567](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L564-L567), [README.md#L640-L640](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L640-L640)
  - [observation/documented] Session-less commands such as 'claude agents' are only relaunched if the user explicitly vouches the exact canonical command in a plain-text voucher file; restore reads the current voucher, never the sidecar value, and missing vouchers leave panes as bare shells. -- evidence: [README.md#L629-L634](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L629-L634), [README.md#L621-L627](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L621-L627), [README.md#L607-L610](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L607-L610)
- memory-state (2 claim(s)):
  - [observation/documented] Session tracking files are written to $HOME/.local/state/tmux-assistant-resurrect on every platform; the path deliberately uses a plain $HOME literal so the assistant-side hook and tmux-server-side save hook agree even when their environments differ. -- evidence: [README.md#L421-L422](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L421-L422), [README.md#L424-L432](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L424-L432)
More evidence: [full detail](tmux-assistant-resurrect.detail.md)

Metadata and full claim list: [full detail](tmux-assistant-resurrect.detail.md)
Human notes ([notes](tmux-assistant-resurrect.notes.md), never overwritten by build)

[Back to map index](../../index.md)
