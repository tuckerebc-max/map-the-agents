# fusil (`fusil`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: devdanzin
- License: GPL-2.0
- Language: Python
- Interface: install=pip install -e '.\[numpy,h5py\]' (requires Python 3.13+)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [devdanzin/fusil](../../repos/devdanzin/fusil.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Revived Python fuzzing framework focused on finding crashes in CPython, C-extension modules, the CPython Tier-2 JIT, and OOM error paths. Multi-agent async-message-based fuzzing architecture with adaptive aggressivity driven by per-session scoring. Generates standalone test scripts run as sandboxed child processes. NOTE: This is a fuzzing framework, not a coding agent harness.

(captured site page body (agents/fusil.md), not a verified repo-code finding)
The original fusil fuzzing framework by Victor Stinner was dormant for years; this revival concentrates it on hunting crashes in CPython, C-extension modules, the Tier-2 JIT, and allocation-failure error paths. Sessions compose agents that exchange asynchronous messages, with per-session scores driving adaptive aggressivity, and each fuzzing session emits a standalone test script executed as a sandboxed child process with memory, CPU, and process limits plus privilege dropping. Only the Python fuzzing path (fusil-python-threaded, fusil.python, fusil.python.jit) is actively developed and tested, while historical fuzzers for Firefox, PHP, and mplayer sit in notworking/ directories. It serves CPython contributors looking for JIT and OOM-edge crashes, not application developers.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fusil.md)
