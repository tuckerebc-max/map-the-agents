# codeflash (`codeflash`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: codeflash-ai
- License: BSL-1.1
- Language: Python
- Interface: platforms=IDE; install=pip install codeflash
- Model providers: Codeflash's LLMs (via API key)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [codeflash-ai/codeflash](../../repos/codeflash-ai/codeflash.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A general-purpose Python code optimizer that uses LLMs to generate multiple optimization ideas, tests them for correctness, benchmarks for performance, and creates merge-ready pull requests with the best optimization found. Used by teams at Pydantic, Roboflow, Unstructured, Langflow. Excels at optimizing AI agents, computer vision algorithms, PyTorch code, numerical code, and backend code. Available as VS Code Extension and GitHub ...

(captured site page body (agents/codeflash.md), not a verified repo-code finding)
Codeflash automates performance work that ordinarily waits for a human to profile, rewrite, and benchmark by hand. The tool generates multiple optimization candidates for Python functions with LLMs, checks each candidate against the existing test suite for correctness, benchmarks runtime against the original, and opens a pull request containing the fastest verified optimization. Teams run it continuously through a GitHub Action so new code gets optimized in every pull request, or run one-off optimizations over an existing codebase or script from the CLI and a VS Code extension. It focuses on performance rather than general development: typical targets include AI agent code, computer vision, PyTorch, numerical, and backend Python, and teams such as Pydantic, Roboflow, Unstructured, and Langflow use it. Access requires an API key from Codeflash's hosted service.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codeflash.md)
