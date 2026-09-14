# shai (`shai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ovh
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=binary
- Model providers: OVHCloud, OpenAI
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [ovh/shai](../../repos/ovh/shai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-based pair programming agent with headless mode for scripting/automation, HTTP server mode with OpenAI-compatible API and SSE streaming, shell assistant that auto-suggests fixes for failed commands, project context via SHAI.md, and MCP-powered custom agents

(captured site page body (agents/shai.md), not a verified repo-code finding)
OVH built shai as an open-source terminal pair programmer, distinguished by treating the agent as a component: pipe a prompt in for automation with full conversation traces out, or run \`shai serve\` to expose the agent through OpenAI-compatible HTTP endpoints with SSE streaming and persistent sessions. The shell assistant mode hooks the user's shell so a failed command's context goes to the model and a fix comes back inline. Project context loads from a SHAI.md file at the repo root, custom agents are configurable with MCP servers and OAuth, and OVHcloud provides anonymous rate-limited access as the default provider. It is Apache-2.0, community-maintained under the OVH organization with active issues and CI, and installs via a curl script or cargo. The audience is terminal-first developers and teams wanting a self-hostable agent endpoint.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/shai.md)
