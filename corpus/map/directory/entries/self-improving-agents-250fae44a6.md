# self-improving-agents (`self-improving-agents`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: BetterForAll
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=pip install -r requirements.txt; create .env with GEMINI_API_KEY
- Model providers: Google Gemini
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [betterforall/self-improving-agents](../../repos/betterforall/self-improving-agents.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Research presenting 4 progressive levels of self-improving code agents; the Arena Loop (L4) uses adversarial co-evolution where code agents and test agents compete, demonstrating that agents scoring 90-100% on original tests dropped to 62-66% under adversarial suites. L3 agents rewrite their own source code with crash-recovery validation.

(captured site page body (agents/self-improving-agents.md), not a verified repo-code finding)
The repository is a controlled comparison of self-improvement strategies for coding agents, built as four progressively more complex loops: an LLM improving a solution against a benchmark, the same loop with an explanatory reviewer, an agent rewriting its own source, and finally an arena where code agents and test agents co-evolve. Tasks ship as small self-contained problems (snake, support, email validation) with checkpoint and resume, and new tasks slot in via a config/benchmark folder, making the ladder reproducible by others. The experiment harness is Gemini-driven Python with CLI runners, and results are framed as research findings rather than product features. With 23 commits and a single contributor it is a personal research artifact, but a documented and runnable one. It suits researchers studying self-improvement dynamics and educators demonstrating the verifiable-rewards pattern.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/self-improving-agents.md)
