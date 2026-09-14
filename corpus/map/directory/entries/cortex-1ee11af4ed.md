# cortex (`cortex`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: urbint
- License: MIT
- Language: Elixir
- Interface: install=Add {:cortex, '~\> 0.1', only: \[:dev, :test\]} to mix.exs
- Model providers: None (deterministic file-watcher, no AI)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [urbint/cortex](../../repos/urbint/cortex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Intelligent coding assistant for Elixir that automatically recompiles/reloads modified files and runs the appropriate tests, with pluggable adapters for custom builds and a focus mode for filtering test runs.

(captured site page body (agents/cortex.md), not a verified repo-code finding)
The cortex entry in this census is Urbint's Elixir development tool, whose 'intelligent coding assistant' description dates from 2017 and has nothing to do with LLMs. Running alongside \`iex -S mix\` as a dev dependency, it watched the filesystem, recompiled and hot-reloaded modified modules in the running session, and triggered the relevant tests automatically under MIX_ENV=test, removing the manual compile-test cycle from Elixir work. Pluggable adapters let teams wire custom build steps, and commands like Cortex.all and Cortex.focus scoped what reran. Development wound down years before Urbint archived the repository on November 25, 2025. It appears in the census as 'other': real developer automation whose name and tagline merely collide with the modern agent vocabulary.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cortex.md)
