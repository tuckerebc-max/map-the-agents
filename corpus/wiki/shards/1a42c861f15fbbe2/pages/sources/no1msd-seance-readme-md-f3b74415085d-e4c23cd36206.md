---
access: public
aliases: []
claim_ids:
- clm_048c54e97869dc7b77a73ae335767c79d87b866705adf3aa9ad9a75f31dafa47
- clm_0539637090f04212af5e9436b1a44647d26c50032299ea2867140cd44f7450c4
- clm_0b432d9882c48a5c04da761fb14d60eee5ba9d69876cf91c4d9476cd9724309f
- clm_27e25a6d258d5404d5927eade9e5fa7cb9bed22f2c8586a636f2c75d07b756c3
- clm_3c3752a63ed9393219506eed404d3fc8949dec80ea99af47b476b12b04d8edd7
- clm_4c9ff3aee28a9357e53c014246fb19988679dfe1317be7855c5d9c35b52db31b
- clm_68d285b24c93ee4585c1ea420859df5bd63b8e22b6ca6ad58644bb26ca2fc7ad
- clm_d9f6096a4449c892b9d9f7ab6c43e95fe78152eaa39f8bfdb4698a739a1bb893
- clm_edd8647667664411b743c2f02e1f5ed4ca3b6a8c1aef1bed7faa31699fbe158e
maturity: draft
page_id: pg_8aa6fba0bef15404a796e4c23cd36206
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_70dc1db2c3785338b20263c990e638bc
title: no1msd/seance/README.md @ f3b74415085d
updated_at: '2026-09-14T03:10:48Z'
---

# no1msd/seance/README.md @ f3b74415085d

<!-- rcw:begin owner=source:src_70dc1db2c3785338b20263c990e638bc block=evidence -->
- A bundled skill file (skills/seance-skill.md) provides AI agents a complete reference for the seance ctl API so they can operate the multiplexer on their own. [@claim:clm_048c54e97869dc7b77a73ae335767c79d87b866705adf3aa9ad9a75f31dafa47]
- Building from source requires Zig 0.16.x, GTK4, libadwaita, OpenGL 4.3+, and Linux (X11 or Wayland). [@claim:clm_0539637090f04212af5e9436b1a44647d26c50032299ea2867140cd44f7450c4]
- Séance is a GTK4 terminal multiplexer for Linux that auto-detects Claude Code, Codex, Pi, OpenCode, and Antigravity CLI sessions running inside it and tracks their status live in a sidebar. [@claim:clm_0b432d9882c48a5c04da761fb14d60eee5ba9d69876cf91c4d9476cd9724309f]
- Panes are arranged in a horizontally scrolling strip, a layout model borrowed from niri, described as fitting long linear agent sessions better than a tiling grid. [@claim:clm_27e25a6d258d5404d5927eade9e5fa7cb9bed22f2c8586a636f2c75d07b756c3]
- Terminal rendering is GPU-accelerated via libghostty (Ghostty used as a library), and the app is built with Zig, GTK4, and libadwaita. [@claim:clm_3c3752a63ed9393219506eed404d3fc8949dec80ea99af47b476b12b04d8edd7]
- Remote `opencode attach` sessions and `--pure` OpenCode launches are not tracked. [@claim:clm_4c9ff3aee28a9357e53c014246fb19988679dfe1317be7855c5d9c35b52db31b]
- Antigravity CLI tracking uses its status-line callback, which the wrapper adds to ~/.gemini/antigravity-cli/settings.json on first launch, keeping a backup at settings.json.seance-backup. [@claim:clm_68d285b24c93ee4585c1ea420859df5bd63b8e22b6ca6ad58644bb26ca2fc7ad]
- The product includes workspaces, session persistence across restarts, tabs within columns, a command palette, focus-follows-mouse, and no telemetry; F11 toggles fullscreen and the header bar hides in fullscreen. [@claim:clm_d9f6096a4449c892b9d9f7ab6c43e95fe78152eaa39f8bfdb4698a739a1bb893]
- Every action is available through `seance ctl`, which talks to the running instance over a Unix domain socket; scripts can create workspaces, open panes, send input, read terminal output, and query the session hierarchy, with JSON output for all commands. [@claim:clm_edd8647667664411b743c2f02e1f5ed4ca3b6a8c1aef1bed7faa31699fbe158e]
<!-- rcw:end owner=source:src_70dc1db2c3785338b20263c990e638bc block=evidence -->

## Researcher notes

