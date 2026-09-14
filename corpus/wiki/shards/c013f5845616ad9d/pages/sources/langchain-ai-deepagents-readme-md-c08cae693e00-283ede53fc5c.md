---
access: public
aliases: []
claim_ids:
- clm_2946bb3316cf14a7c5ad4825ddc58e21899f97318d28b25ad20b811e9e826d55
- clm_5a025992201f12d33b773cf68a10c9cb340e78f641c8efffae2e2185179477b0
- clm_762e9bec4b04cd8c319e7fc54e0bd24c7a3268637ea7ae88c0a96508a0cf567f
- clm_8eed8e4bd58b734c05360c1dee969544a02b890d0a97caf86884ff09f77540bf
- clm_ca65677fdf10d66c7a7a11caafd5d049235687dfc9147d98d6734c58832e2ecf
- clm_d1e54f5f9038b10b6dad7aa5734a9a9aa424eb229a12d98dcb7b73099896bcdd
- clm_d2591d701be68d53b9400b6ac5347f246c2961f917c1104778c0344774efe6b1
- clm_d331baed67d974ec520db3c44235208699bafcb5a02b71dfb6c0ad5e96e15a61
maturity: draft
page_id: pg_e8f72138e3555da8be4c283ede53fc5c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_10aa5f3656be5082b7eeddfffc0cbe0e
title: langchain-ai/deepagents/README.md @ c08cae693e00
updated_at: '2026-09-14T02:10:56Z'
---

# langchain-ai/deepagents/README.md @ c08cae693e00

<!-- rcw:begin owner=source:src_10aa5f3656be5082b7eeddfffc0cbe0e block=evidence -->
- Documented features include sub-agents with isolated context windows, pluggable filesystem backends, context summarization with tool-output offloading, shell access, persistent memory, human-in-the-loop tool approval, skills, and custom or MCP tools. [@claim:clm_2946bb3316cf14a7c5ad4825ddc58e21899f97318d28b25ad20b811e9e826d55]
- The package is distributed on PyPI as deepagents under an MIT license and is installed with uv; a separate JavaScript/TypeScript library exists in deepagentsjs. [@claim:clm_5a025992201f12d33b773cf68a10c9cb340e78f641c8efffae2e2185179477b0]
- The Python API exposes create_deep_agent, which accepts a model string, custom tools, and a system prompt, and is invoked with a messages payload. [@claim:clm_762e9bec4b04cd8c319e7fc54e0bd24c7a3268637ea7ae88c0a96508a0cf567f]
- The product follows a 'trust the LLM' security model: the agent can do anything its tools allow, and boundaries should be enforced at the tool or sandbox level rather than by model self-policing. [@claim:clm_8eed8e4bd58b734c05360c1dee969544a02b890d0a97caf86884ff09f77540bf]
- The harness is model-agnostic: it works with any tool-calling LLM, including frontier APIs, open-weight hosted models, and self-hosted models via Ollama, vLLM, or llama.cpp. [@claim:clm_ca65677fdf10d66c7a7a11caafd5d049235687dfc9147d98d6734c58832e2ecf]
- Deep Agents layers on LangChain's create_agent, which itself runs on the LangGraph graph runtime, bundling filesystem, sub-agents, context management, and skills on top. [@claim:clm_d1e54f5f9038b10b6dad7aa5734a9a9aa424eb229a12d98dcb7b73099896bcdd]
- Deep Agents is an open-source agent harness that runs out of the box and can be extended, overridden, or replaced piece by piece without forking. [@claim:clm_d2591d701be68d53b9400b6ac5347f246c2961f917c1104778c0344774efe6b1]
- Any LangGraph CompiledStateGraph can be passed in as a sub-agent, allowing custom orchestration to plug into the harness. [@claim:clm_d331baed67d974ec520db3c44235208699bafcb5a02b71dfb6c0ad5e96e15a61]
<!-- rcw:end owner=source:src_10aa5f3656be5082b7eeddfffc0cbe0e block=evidence -->

## Researcher notes

