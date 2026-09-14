# LLama Cpp Agent (`llama-cpp-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: Maximilian-Winter
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: llama-cpp-python, llama.cpp server, TGI, vLLM
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [maximilian-winter/llama-cpp-agent](../../repos/maximilian-winter/llama-cpp-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Python framework for interacting with LLMs — chat, function calling, structured output, RAG, and agentic chains with tools. Key differentiator is guided sampling via grammars and JSON schema generation, enabling most 7B LLMs (even those not fine-tuned for function calling) to perform structured output and function calling. Supports parallel function calling, RAG with ColBERT reranking, and predefined message formatters for ...

(captured site page body (agents/llama-cpp-agent.md), not a verified repo-code finding)
The framework addressed a practical problem from the era before function calling was widespread: small local models frequently emitted malformed JSON, so agent chains built on them were unreliable. By constraining token sampling with grammars and JSON schemas during inference, it made structured output and tool invocation a decoding-time guarantee rather than a learned behavior. Developers building local assistants, RAG applications, and tool-using chains on llama.cpp-class hardware used it to add those capabilities without fine-tuning. The project has been abandoned; the author now points users to ToolAgents and other maintained Python agent frameworks.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/llama-cpp-agent.md)
