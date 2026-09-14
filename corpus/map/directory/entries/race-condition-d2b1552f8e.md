# race-condition (`race-condition`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: GoogleCloudPlatform
- License: Apache-2.0
- Language: Go (gateway/services), Python (AI agents), TypeScript/Angular (frontend)
- Interface: platforms=Autonomous, Web; install=git clone the repo, then make init
- Model providers: Gemini (Vertex AI),Ollama,vLLM on GKE
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [googlecloudplatform/race-condition](../../repos/googlecloudplatform/race-condition.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent marathon simulation where AI agents (Planner, Simulator, Runners) plan a Las Vegas marathon route, simulate environment (weather, traffic, crowds), and race autonomously over the A2A protocol; demoed at Google Cloud Next '26 Developer Keynote.

(captured site page body (agents/race-condition.md), not a verified repo-code finding)
Race-condition is the open-source release of the multi-agent marathon simulation Google demoed at Cloud Next '26, published as a deployable reference architecture rather than a product. Planner agents design a race course using Google Maps MCP tools, GIS data, and financial modeling; a Simulator agent advances the environment tick by tick; and Runner agents make per-tick pacing decisions, communicating over the A2A protocol through a Go WebSocket gateway that batches traffic from hundreds of concurrent runners. Three planner variants — baseline, LLM-as-judge evaluation, and AlloyDB-backed memory — demonstrate progressive capability additions, while a deterministic autopilot runner provides a zero-API-cost baseline. The frontend can replay recorded agent streams indistinguishably from live runs, a reliability measure from the keynote that doubles as a free testing path. Google Cloud engineers use it as a starting template for building A2A-based multi-agent systems on Cloud Run and Vertex AI.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/race-condition.md)
