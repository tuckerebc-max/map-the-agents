# Smallest Agent (`smallest-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: obra
- License: unknown
- Language: JavaScript
- Interface: platforms=CLI; install=git clone and npm install; run npm test for the API smoke test (no published package)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: unknown (unknown)

Repository map entry: [obra/smallest-agent](../../repos/obra/smallest-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Minimalism challenge coding agent golfed down to just 493 bytes (src/smallest-agent.js); functional coding agent with unrestricted bash access; commented readable version at src/smallest-agent.commented.js; created as a demonstration of how small a Claude Code-like agent can be

(captured site page body (agents/smallest-agent.md), not a verified repo-code finding)
The project is a demonstration built to answer how little code a functional agent needs. Jesse Vincent wrote a first draft comparable in behavior to Claude Code, then used the agent itself to golf its own source down to a few hundred bytes, documenting the process in HACKING-TRANSCRIPT.md. The minified loop calls a hosted LLM API and gives the model unrestricted bash, which the README flags in capital letters as capable of destructive actions; a commented companion file and an npm smoke test make the mechanics studyable. There is no MCP, plugin, hook, or subagent machinery by design. Its audience is developers studying the minimal anatomy of an agent loop, not teams shipping software.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/smallest-agent.md)
