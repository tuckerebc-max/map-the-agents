# Bullet (`bullet`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: trybullet
- License: Proprietary
- Language: unknown
- Interface: platforms=CLI, Desktop; install=npm install -g @trybullet/cli (Node 18+), or download the desktop app
- Model providers: multi-model routing (fast models for simple work, deeper reasoning on escalation)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Speed-first routing architecture that sends straightforward work to fast models and escalates to deeper reasoning only for complex tasks, finds relevant code without embedding the whole repo, and runs independent tool calls in parallel while intercepting duplicate calls and stuck loops. Claims 95.8% on SWE-Bench Verified.

(captured site page body (agents/bullet.md), not a verified repo-code finding)
Bullet is a YC-backed coding agent built by a team that got frustrated waiting on agent runs while building with Claude Code, and its whole pitch is keeping up with the developer rather than the other way around. Three protocols drive the speed: routing tasks to the right model tier, targeted search that finds relevant code without ingesting the entire repository, and parallel execution of independent tool calls with interception of duplicate calls and stuck loops. The same agent loop and tools are available both as a desktop GUI app and as a CLI installed via npm, and the team reports 95.8% on SWE-Bench Verified. Access is currently free with no subscription or API key required to start, and it runs on macOS, Linux, and Windows.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bullet.md)
