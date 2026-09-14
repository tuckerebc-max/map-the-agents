# no1msd/seance -- full detail

[Back to orientation](seance.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/no1msd/seance/f3b74415085d6ef8627ec3f3faba5152f06569b4/88cf718b6e2c2927.json](../../../wiki/dossiers/no1msd/seance/f3b74415085d6ef8627ec3f3faba5152f06569b4/88cf718b6e2c2927.json)

## specifications (1 claim(s))

- [observation/documented] Séance is a GTK4 terminal multiplexer for Linux that auto-detects Claude Code, Codex, Pi, OpenCode, and Antigravity CLI sessions running inside it and tracks their status live in a sidebar. -- evidence: [README.md#L27-L27](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L27-L27) (`clm_0b432d9882c48a5c04da761fb14d60eee5ba9d69876cf91c4d9476cd9724309f`)

## components (2 claim(s))

- [observation/documented] Terminal rendering is GPU-accelerated via libghostty (Ghostty used as a library), and the app is built with Zig, GTK4, and libadwaita. -- evidence: [README.md#L163-L165](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L163-L165), [README.md#L31-L31](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L31-L31) (`clm_3c3752a63ed9393219506eed404d3fc8949dec80ea99af47b476b12b04d8edd7`)
- [observation/documented] Antigravity CLI tracking uses its status-line callback, which the wrapper adds to ~/.gemini/antigravity-cli/settings.json on first launch, keeping a backup at settings.json.seance-backup. -- evidence: [README.md#L54-L60](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L54-L60) (`clm_68d285b24c93ee4585c1ea420859df5bd63b8e22b6ca6ad58644bb26ca2fc7ad`)

## design-choices (2 claim(s))

- [observation/documented] Panes are arranged in a horizontally scrolling strip, a layout model borrowed from niri, described as fitting long linear agent sessions better than a tiling grid. -- evidence: [README.md#L35-L35](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L35-L35) (`clm_27e25a6d258d5404d5927eade9e5fa7cb9bed22f2c8586a636f2c75d07b756c3`)
- [observation/documented] The product includes workspaces, session persistence across restarts, tabs within columns, a command palette, focus-follows-mouse, and no telemetry; F11 toggles fullscreen and the header bar hides in fullscreen. -- evidence: [README.md#L80-L80](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L80-L80) (`clm_d9f6096a4449c892b9d9f7ab6c43e95fe78152eaa39f8bfdb4698a739a1bb893`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run `G_DEBUG=fatal-criticals GTK_A11Y=none xvfb-run -a zig build test` and `xvfb-run zig build e2e`, and CI must pass before merge. -- evidence: [CONTRIBUTING.md#L22-L26](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L22-L26), [CONTRIBUTING.md#L125-L128](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L125-L128) (`clm_803cd32fad2502b6317608c3b2717bfc976202452825fb6fb903bd1a7ab8c9d1`)
- [observation/documented] Repository development practice: Zig code should follow `zig fmt` with functions kept small (~80 lines), new dependencies require a Discussion first, and PRs should contain one focused change. -- evidence: [CONTRIBUTING.md#L118-L121](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L118-L121), [CONTRIBUTING.md#L125-L128](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/CONTRIBUTING.md#L125-L128) (`clm_f14ad48abc4727e5adc4c66261f05d08ddc2afc4cddfaff1ea9c0cbf252fbfc0`)
- [observation/documented] Repository development practice: security issues must be reported privately via GitHub's private vulnerability reporting rather than public issues, with acknowledgment aimed within 72 hours; only the latest pre-1.0 release is supported with security fixes. -- evidence: [SECURITY.md#L9-L9](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/SECURITY.md#L9-L9), [SECURITY.md#L13-L13](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/SECURITY.md#L13-L13), [SECURITY.md#L5-L5](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/SECURITY.md#L5-L5) (`clm_142cece552d1144c16f1fcbfbdbf52c20b6292bf20a9c78a9a042f2ddd574db9`)

## skills-patterns (1 claim(s))

- [observation/documented] A bundled skill file (skills/seance-skill.md) provides AI agents a complete reference for the seance ctl API so they can operate the multiplexer on their own. -- evidence: [README.md#L76-L76](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L76-L76) (`clm_048c54e97869dc7b77a73ae335767c79d87b866705adf3aa9ad9a75f31dafa47`)

## interfaces (1 claim(s))

- [observation/documented] Every action is available through `seance ctl`, which talks to the running instance over a Unix domain socket; scripts can create workspaces, open panes, send input, read terminal output, and query the session hierarchy, with JSON output for all commands. -- evidence: [README.md#L74-L74](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L74-L74) (`clm_edd8647667664411b743c2f02e1f5ed4ca3b6a8c1aef1bed7faa31699fbe158e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Zig 0.16.x, GTK4, libadwaita, OpenGL 4.3+, and Linux (X11 or Wayland). -- evidence: [README.md#L143-L143](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L143-L143) (`clm_0539637090f04212af5e9436b1a44647d26c50032299ea2867140cd44f7450c4`)

## limitations (1 claim(s))

- [observation/documented] Remote `opencode attach` sessions and `--pure` OpenCode launches are not tracked. -- evidence: [README.md#L46-L52](https://github.com/no1msd/seance/blob/f3b74415085d6ef8627ec3f3faba5152f06569b4/README.md#L46-L52) (`clm_4c9ff3aee28a9357e53c014246fb19988679dfe1317be7855c5d9c35b52db31b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

