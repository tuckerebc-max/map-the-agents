# OpenAlpha_Evolve (`openalpha-evolve`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: shyamsaktawat
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=pip, docker
- Model providers: OpenAI, Anthropic, Google (Gemini/Vertex AI), Cohere (via LiteLLM)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [shyamsaktawat/openalpha_evolve](../../repos/shyamsaktawat/openalpha_evolve.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source framework inspired by DeepMind's AlphaEvolve that combines evolutionary algorithms with LLM-driven code generation using diff-based mutations and bug fixes. Sandboxed Docker execution for security, modular multi-agent architecture (PromptDesigner, CodeGenerator, Evaluator, Database, SelectionController, TaskManager), and Gradio web UI for interactive task definition.

(captured site page body (agents/openalpha-evolve.md), not a verified repo-code finding)
DeepMind's AlphaEvolve showed that evolutionary search over LLM-generated programs can produce algorithms that beat hand-written baselines, but the system was never released. OpenAlpha_Evolve reconstructs the concept in Python: a PromptDesignerAgent frames the task, a CodeGeneratorAgent writes and mutates candidate programs as diffs, an EvaluatorAgent runs them against tests inside Docker containers, a DatabaseAgent archives the population, and a SelectionControllerAgent drives generations forward. Models route through LiteLLM with Gemini as the default configuration, and candidates can also be inspected through a Gradio web UI. Tasks are defined in YAML examples (shortest path among them), and the whole loop runs from a single python -m main invocation after cloning and pip installing. Researchers and hobbyists in evolutionary computation and LLM-driven program synthesis use it as an accessible AlphaEvolve-style testbed; the repo is experimental and community-maintained.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openalpha-evolve.md)
