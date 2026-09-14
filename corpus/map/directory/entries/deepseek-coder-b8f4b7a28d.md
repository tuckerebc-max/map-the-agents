# DeepSeek Coder (`deepseek-coder`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: DeepSeek
- License: MIT
- Language: Python
- Interface: platforms=API, CLI; install=pip install -r requirements.txt
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [deepseek-ai/deepseek-coder](../../repos/deepseek-ai/deepseek-coder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A family of code LLMs (1B-33B) trained from scratch on 2T tokens (87% code, 13% NL) for code completion, insertion, chat, and repository-level completion. 16K context with fill-in-the-blank; 7B matches CodeLlama-34B; 33B instruct beats GPT-3.5-turbo on HumanEval; supports 87+ languages. A model, not an agent harness.

(captured site page body (agents/deepseek-coder.md), not a verified repo-code finding)
DeepSeek Coder is a series of open-weight code language models from 1.3B to 33B parameters, trained from scratch on two trillion tokens dominated by source code in roughly 90 programming languages plus English and Chinese. The training mix includes a project-level repository corpus and a fill-in-the-blank objective, giving the models 16K-context completion and infilling behavior that made them useful for IDE-style completion as well as chat. Released as Base and Instruct checkpoints (the Instruct variants arrived January 2024), they set open-source records at the time on HumanEval and related benchmarks. The models are consumed through Hugging Face weights, the DeepSeek API, or local runtimes — by other harnesses rather than as one — and the repository's own activity wound down as DeepSeek moved to later model generations.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepseek-coder.md)
