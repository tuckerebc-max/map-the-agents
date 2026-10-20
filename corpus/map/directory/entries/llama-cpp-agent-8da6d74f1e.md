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
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/llama-cpp-agent.md)
