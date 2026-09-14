# storozhenko98/beehive

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 42e6a36ead6d @ 45e04241f2153fbd

## Summary (orientation draft, not independently verified)

Beehive is a Tauri v2 desktop GUI plus a standalone Rust TUI for orchestrating coding agents across isolated git workspace clones ('combs') organized into hives and nests, with persistent PTY terminals, agent panes, and shared on-disk state under ~/.beehive/. Evidence is mostly README product documentation; CLAUDE.md slices are contributor guidance and are excluded from product claims.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Beehive manages multiple repos, creates isolated workspace clones on different branches, and runs terminals and AI agents side-by-side from one window, shipped as both a desktop GUI app and a terminal TUI. -- evidence: [README.md#L3-L3](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L3-L3), [README.md#L7-L7](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] The stack comprises a React 19/TypeScript/Vite frontend with xterm.js, a Rust Tauri v2 backend using portable-pty, a Ratatui/Crossterm-based Rust TUI, and git operations performed by shelling out to git and gh CLIs. -- evidence: [README.md#L121-L128](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L121-L128)
- design-choices (1 claim(s)):
  - [observation/documented] A configured comb startup command (e.g. a tmux session) runs once per comb the first time it opens after launch, after which the app returns to an interactive shell in the comb directory. -- evidence: [README.md#L175-L175](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L175-L175), [README.md#L177-L181](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L177-L181), [README.md#L183-L183](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L183-L183)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the GUI is built with npm install plus 'npm run tauri dev' for hot-reload development or 'npm run tauri build' for production, the TUI is built with cargo build --release from cli/, and CONTRIBUTING.md covers development setup and guidelines. -- evidence: [README.md#L112-L115](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L112-L115), [README.md#L94-L100](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L94-L100), [README.md#L196-L196](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L196-L196)
  - [observation/documented] Repository development practice: CLAUDE.md serves as AI-assistant context and documents contributor commands such as cargo check for Rust type-checking and npx tsc --noEmit for TypeScript type-checking. -- evidence: [CLAUDE.md#L64-L64](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/CLAUDE.md#L64-L64), [CLAUDE.md#L67-L67](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/CLAUDE.md#L67-L67), [README.md#L132-L159](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L132-L159)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The TUI installs via a curl-piped shell script, asks the user to choose 'bh' or 'beehive' as the command name, and auto-updates on startup. -- evidence: [README.md#L25-L25](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L25-L25), [README.md#L21-L23](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L21-L23)
  - [observation/documented] The TUI binary can set the comb startup command programmatically via a --startup-cmd flag, and passing an empty string clears it, per the documented examples. -- evidence: [README.md#L33-L33](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L33-L33), [README.md#L35-L37](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L35-L37), [README.md#L27-L27](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L27-L27), [README.md#L29-L31](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L29-L31)
- memory-state (2 claim(s)):
  - [observation/documented] All config lives under ~/.beehive/: config.json for app settings, a beehive.json directory marker, and per-hive .hive/state.json holding repo info, nests, combs, pane layouts, and custom buttons; combs are full git clones on disk. -- evidence: [README.md#L163-L163](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L163-L163), [README.md#L171-L171](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L171-L171), [README.md#L165-L169](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L165-L169)
More evidence: [full detail](beehive.detail.md)

Metadata and full claim list: [full detail](beehive.detail.md)
Human notes ([notes](beehive.notes.md), never overwritten by build)

[Back to map index](../../index.md)
