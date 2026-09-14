# InstallCursorEditorLinux (`installcursoreditorlinux`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: IsRengel
- License: Apache-2.0
- Language: Shell
- Interface: platforms=IDE; install=git clone https://github.com/IsRengel/InstallCursorEditorLinux.git --depth=1 && cd InstallCursorEditorLinux && ./install.sh
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [isrengel/installcursoreditorlinux](../../repos/isrengel/installcursoreditorlinux.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Shell script installer that sets up Cursor AI Code Editor as a desktop application on any Linux distribution (creates .desktop file, configures automatic updates via systemd). Deprecated: Cursor now ships an official .deb package; the repo is kept for historical/educational purposes.

(captured site page body (agents/installcursoreditorlinux.md), not a verified repo-code finding)
InstallCursorEditorLinux existed because Cursor initially shipped only as an AppImage with no Linux packaging. The script downloaded the AppImage, installed it under /opt/cursor, generated a .desktop entry, and wired a systemd unit for automatic updates across Debian, Arch, Fedora, OpenSUSE, Gentoo, and Solus. Once Cursor shipped an official .deb, the README added a deprecation notice directing users to cursor.com. The 160-star repo survives as an educational example of packaging AppImage software for multiple distributions.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/installcursoreditorlinux.md)
