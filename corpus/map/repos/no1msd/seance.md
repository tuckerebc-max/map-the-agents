# no1msd/seance

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f3b74415085d @ 88cf718b6e2c2927

## Summary (orientation draft, not independently verified)

Séance is a GTK4/Linux terminal multiplexer that auto-tracks AI coding agent sessions and exposes a socket-based control CLI; the packet is README/SECURITY/CONTRIBUTING documentation only, with no runtime source code shown.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Séance is a GTK4 terminal multiplexer for Linux that auto-detects Claude Code, Codex, Pi, OpenCode, and Antigravity CLI sessions running inside it and tracks their status live in a sidebar. -- evidence: [README.md#L27-L27](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L27-L27)
- components (2 claim(s)):
  - [observation/documented] Terminal rendering is GPU-accelerated via libghostty (Ghostty used as a library), and the app is built with Zig, GTK4, and libadwaita. -- evidence: [README.md#L163-L165](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L163-L165), [README.md#L31-L31](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L31-L31)
  - [observation/documented] Antigravity CLI tracking uses its status-line callback, which the wrapper adds to ~/.gemini/antigravity-cli/settings.json on first launch, keeping a backup at settings.json.seance-backup. -- evidence: [README.md#L54-L60](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L54-L60)
- design-choices (2 claim(s)):
  - [observation/documented] Panes are arranged in a horizontally scrolling strip, a layout model borrowed from niri, described as fitting long linear agent sessions better than a tiling grid. -- evidence: [README.md#L35-L35](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L35-L35)
  - [observation/documented] The product includes workspaces, session persistence across restarts, tabs within columns, a command palette, focus-follows-mouse, and no telemetry; F11 toggles fullscreen and the header bar hides in fullscreen. -- evidence: [README.md#L80-L80](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L80-L80)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run `G_DEBUG=fatal-criticals GTK_A11Y=none xvfb-run -a zig build test` and `xvfb-run zig build e2e`, and CI must pass before merge. -- evidence: [CONTRIBUTING.md#L22-L26](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L22-L26), [CONTRIBUTING.md#L125-L128](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L125-L128)
  - [observation/documented] Repository development practice: Zig code should follow `zig fmt` with functions kept small (~80 lines), new dependencies require a Discussion first, and PRs should contain one focused change. -- evidence: [CONTRIBUTING.md#L118-L121](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L118-L121), [CONTRIBUTING.md#L125-L128](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L125-L128)
- skills-patterns (1 claim(s)):
  - [observation/documented] A bundled skill file (skills/seance-skill.md) provides AI agents a complete reference for the seance ctl API so they can operate the multiplexer on their own. -- evidence: [README.md#L76-L76](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L76-L76)
- interfaces (1 claim(s)):
  - [observation/documented] Every action is available through `seance ctl`, which talks to the running instance over a Unix domain socket; scripts can create workspaces, open panes, send input, read terminal output, and query the session hierarchy, with JSON output for all commands. -- evidence: [README.md#L74-L74](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L74-L74)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](seance.detail.md)

Metadata and full claim list: [full detail](seance.detail.md)
Human notes ([notes](seance.notes.md), never overwritten by build)

[Back to map index](../../index.md)
