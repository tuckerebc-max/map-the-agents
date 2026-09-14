# tmux (`tmux`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tmux
- License: ISC
- Language: C
- Interface: platforms=CLI; install=Binary packages (platform-specific), from release tarball (./configure && make && sudo make install), or from version control (git clone, sh autogen.sh, ./configure && make)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [tmux/tmux](../../repos/tmux/tmux.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal multiplexer that lets multiple terminals be created, accessed, and controlled from a single screen; sessions detach and keep running in the background, then reattach later. Runs on OpenBSD, FreeBSD, NetBSD, Linux, macOS, and Solaris. Not a coding agent harness; a foundational terminal tool. README does not describe a plugin system (third-party TPM exists but is not mentioned in the ...

(captured site page body (agents/tmux.md), not a verified repo-code finding)
tmux is a terminal multiplexer in the classic sense: it lets one screen create, access, and control many terminal sessions, with sessions detaching and continuing to run on a background server so work survives disconnections, SSH drops, and reboots. It is written in C against libevent and ncurses, runs on OpenBSD, FreeBSD, NetBSD, Linux, macOS, and Solaris, and is licensed ISC; sessions, windows, and panes are scriptable, which is why nearly every terminal agent workflow — including dedicated plugins like tmux-assistant-resurrect — treats tmux as the substrate for keeping coding agents alive across reboots and for watching several agent sessions at once. The project itself has no agent features, no plugin API beyond its configuration format (third-party TPM exists outside the repo), and no knowledge of AI tools; it is included in this census because practitioners overwhelmingly run harnesses inside it. Its role is foundational infrastructure rather than agent software.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tmux.md)
