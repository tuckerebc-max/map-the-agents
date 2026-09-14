# live-swe-agent (`live-swe-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: OpenAutoCoder
- License: MIT
- Language: Python
- Interface: install=Install mini-swe-agent, then run: mini --config config/livesweagent.yaml
- Model providers: Anthropic (Claude Opus 4.5), Google (Gemini 3 Pro)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [openautocoder/live-swe-agent](../../repos/openautocoder/live-swe-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First runtime self-evolving software engineering agent that treats agents as software systems which can modify their own behavior at runtime; achieves SOTA 79.2% on SWE-bench Verified (Claude Opus 4.5) and 45.8% on SWE-Bench Pro with a minimal open scaffold

(captured site page body (agents/live-swe-agent.md), not a verified repo-code finding)
Live-SWE-agent rests on the observation that an agent is itself software, so an LLM-driven agent can extend and revise its own behavior while working — the implementation is deliberately a small config delta on mini-swe-agent rather than a new scaffold. Published results claim 79.2% on SWE-bench Verified with Claude Opus 4.5 and 45.8% on SWE-Bench Pro, self-reported through the project's own public leaderboard, which also serves as a platform for apples-to-apples model comparison. Trajectories, patches, and full run artifacts are published on Hugging Face for verification. Agent researchers use it to study runtime self-evolution and as a minimal baseline for fair model comparisons.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/live-swe-agent.md)
