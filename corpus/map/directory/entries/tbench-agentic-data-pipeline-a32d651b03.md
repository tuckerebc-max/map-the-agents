# tbench-agentic-data-pipeline (`tbench-agentic-data-pipeline`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Danau5tin
- License: unknown
- Language: Python
- Interface: platforms=CLI; install=git clone then uv sync
- Model providers: Claude (Anthropic)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [danau5tin/tbench-agentic-data-pipeline](../../repos/danau5tin/tbench-agentic-data-pipeline.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent synthetic data generation pipeline that produces validated training data for terminal-based coding tasks for RL training. Uses 20+ Claude Code instances working in parallel through three specialized agent stages (idea generation, datapoint building, quality review) coordinated by a central Task Manager. Generated 331+ validated datapoints across software engineering, sysadmin, security, and other categories. Docker-based validation pipeline (build, test discovery, ...

(captured site page body (agents/tbench-agentic-data-pipeline.md), not a verified repo-code finding)
The pipeline exists because RL training for terminal agents needs large quantities of verified, executable tasks, and hand-curation does not scale. It turns Terminal Bench seed tasks into training datapoints through a three-stage agent workforce: idea-generation agents diversify seed tasks, datapoint-builder agents construct each task's dockerfile, tests, and weights and iterate until validation passes, and quality-review agents approve or reject the result. A central Task Manager hands out work atomically over a shared filesystem, tracks parent-child provenance, and recovers from timeouts, while validation requires tests to fail before any fix and weights to normalize. The output — 331+ validated datapoints spanning software engineering, sysadmin, security, and debugging — fed the author's terminal-bench-rl training work. It is tooling for RL data production rather than a user-facing agent, and it has no license file.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tbench-agentic-data-pipeline.md)
