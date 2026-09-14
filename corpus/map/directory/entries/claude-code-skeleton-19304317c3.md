# claude-code (`claude-code-skeleton`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: yasasbanukaofficial
- License: unknown
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [yasasbanukaofficial/claude-code](../../repos/yasasbanukaofficial/claude-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A mirror/backup of Anthropic's official Claude Code CLI source code that was accidentally leaked via a sourcemap file (.map) bundled in the npm package. Reveals internal structure: 785KB main.tsx, 40+ tools, React terminal renderer (Ink), multi-agent orchestration (Swarm), ULTRAPLAN (deep planning via Opus), KAIROS (always-on assistant), Tamagotchi companion system (BUDDY), Undercover Mode, and Dream memory system. For educational/archival purposes only ...

(captured site page body (agents/claude-code-skeleton.md), not a verified repo-code finding)
The repository existed to preserve and expose the accidentally leaked TypeScript source of Anthropic's Claude Code CLI, which shipped inside the npm package's source map. Its documentation described the internal layout: the large main.tsx bundle, the tool registry, command definitions, and internal architecture that Anthropic does not publish. Developers and researchers consulted it to understand how a production agent harness is structured. The repository has been removed from GitHub and returns 404, so it is no longer available in any form.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-code-skeleton.md)
