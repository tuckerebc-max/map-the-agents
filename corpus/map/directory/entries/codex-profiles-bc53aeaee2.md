# codex-profiles (`codex-profiles`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Ducksss
- License: MIT
- Language: Bash
- Interface: platforms=CLI, Desktop; install=npm install -g codex-profiles | brew install Ducksss/tap/codex-profile | curl install.sh | nix run
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [ducksss/codex-profiles](../../repos/ducksss/codex-profiles.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Isolates CODEX_HOME and Electron user data per named profile without copying, parsing, or migrating tokens; on macOS opens separate named ChatGPT windows with their own local state using the original signed ChatGPT.app (no cloning/patching/re-signing); --share-with shares config selectively without sharing auth or runtime state; workspace binding auto-selects profile per directory; dependency-free single Bash script. Community-maintained, not affiliated with OpenAI.

(captured site page body (agents/codex-profiles.md), not a verified repo-code finding)
Codex-profiles solves a workflow problem for people who use Codex across separate contexts — personal, work, client, and test accounts — where mixing conversation history, config, and authentication state causes friction. A wrapper maps each profile name to its own CODEX_HOME directory and, on macOS, to a named ChatGPT Desktop window with isolated Electron user data, using the original signed application binary rather than a clone. The script deliberately never reads, copies, or migrates auth.json, so account separation is at the local-state level rather than a security boundary, and the README states this explicitly. Workspace binding selects a profile automatically per project directory, --share-with shares specific configuration without sharing authentication, and a doctor command verifies the setup. It is distributed as a single dependency-free Bash script via npm, Homebrew, curl, and Nix.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codex-profiles.md)
