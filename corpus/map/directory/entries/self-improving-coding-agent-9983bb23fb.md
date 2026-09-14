# self_improving_coding_agent (`self-improving-coding-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: MaximeRobeyns
- License: MIT
- Language: Python
- Interface: install=git clone, export API keys, make image, pip install -r base_agent/requirements.txt
- Model providers: Anthropic, OpenAI, Gemini, Vertex (GCP), Fireworks AI, DeepSeek, Modal
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [maximerobeyns/self_improving_coding_agent](../../repos/maximerobeyns/self_improving_coding_agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-improving coding agent that runs an iterative loop (evaluate on benchmarks, store results, modify its own codebase, repeat), bootstrapping capabilities without human intervention. Research artifact from ICLR 2025 Workshop.

(captured site page body (agents/self-improving-coding-agent.md), not a verified repo-code finding)
The project operationalizes a simple question: if a coding agent can modify code, what happens when its own source is the task? Each iteration evaluates the current agent on benchmark tasks, stores the results, then has the agent edit its repository to improve, with the loop repeating without human intervention; an ICLR 2025 workshop paper documents the method. The base agent is intentionally minimal — no tree-sitter, LSP, or sophisticated planning — because the point is to observe bootstrapped specialization on the bundled SWE-bench-style tasks, not to ship a product. Everything runs inside a provided Docker image because the agent executes arbitrary shell commands, and the authors are explicit about that safety boundary. Providers span Anthropic, OpenAI, Gemini, Vertex, Fireworks, and DeepSeek. As a frozen two-commit research artifact with a citable paper, its audience is researchers studying self-improvement, not practitioners.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/self-improving-coding-agent.md)
