# langchain-ai/deepagents -- full detail

[Back to orientation](deepagents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/langchain-ai/deepagents/c08cae693e0036fcd45d979a7dfa3a7e306a0515/a946885b8fc52b92.json](../../../wiki/dossiers/langchain-ai/deepagents/c08cae693e0036fcd45d979a7dfa3a7e306a0515/a946885b8fc52b92.json)

## specifications (1 claim(s))

- [observation/documented] Deep Agents is an open-source agent harness that runs out of the box and can be extended, overridden, or replaced piece by piece without forking. -- evidence: [README.md#L24-L24](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L24-L24), [README.md#L28-L31](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L28-L31) (`clm_d2591d701be68d53b9400b6ac5347f246c2961f917c1104778c0344774efe6b1`)

## components (1 claim(s))

- [observation/documented] Documented features include sub-agents with isolated context windows, pluggable filesystem backends, context summarization with tool-output offloading, shell access, persistent memory, human-in-the-loop tool approval, skills, and custom or MCP tools. -- evidence: [README.md#L35-L42](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L35-L42) (`clm_2946bb3316cf14a7c5ad4825ddc58e21899f97318d28b25ad20b811e9e826d55`)

## design-choices (2 claim(s))

- [observation/documented] The harness is model-agnostic: it works with any tool-calling LLM, including frontier APIs, open-weight hosted models, and self-hosted models via Ollama, vLLM, or llama.cpp. -- evidence: [README.md#L79-L79](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L79-L79), [README.md#L28-L31](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L28-L31) (`clm_ca65677fdf10d66c7a7a11caafd5d049235687dfc9147d98d6734c58832e2ecf`)
- [observation/documented] Deep Agents layers on LangChain's create_agent, which itself runs on the LangGraph graph runtime, bundling filesystem, sub-agents, context management, and skills on top. -- evidence: [README.md#L75-L75](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L75-L75), [README.md#L87-L87](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L87-L87) (`clm_d1e54f5f9038b10b6dad7aa5734a9a9aa424eb229a12d98dcb7b73099896bcdd`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors follow Conventional Commits with scopes, branch naming of username/scope/description, a PR template with a release-note summary, and unit tests split into tests/unit_tests and tests/integration_tests with warnings treated as errors. -- evidence: [AGENTS.md#L42-L42](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L42-L42), [AGENTS.md#L81-L83](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L81-L83), [AGENTS.md#L87-L87](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L87-L87), [AGENTS.md#L48-L51](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L48-L51), [AGENTS.md#L32-L32](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L32-L32) (`clm_ab2f6ab52b0f8017b7999413b4b354e9b677cab8c8b6095addd9526241b3e7ca`)
- [observation/documented] Repository development practice: the monorepo layout includes libs/deepagents, libs/code, libs/acp, libs/talon, libs/evals, and partner packages, with benchmarks run via package bench and bench-memory Make targets rather than pytest directly. -- evidence: [AGENTS.md#L111-L116](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L111-L116), [AGENTS.md#L131-L131](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L131-L131) (`clm_d5ae1a55633b923136eb1490946c05a8cb0dc2fd4f5069d00a5e0e5e10d8bc90`)
- [observation/documented] Repository development practice: public API changes must preserve exported signatures, add new parameters as keyword-only with defaults, and mark experimental features with docstring warnings. -- evidence: [AGENTS.md#L59-L62](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L59-L62), [AGENTS.md#L57-L57](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L57-L57) (`clm_ba95cf42718fa9c3fa5c76de85ce4d5951458f61707cfb0b24eeb10e6c452daa`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The Python API exposes create_deep_agent, which accepts a model string, custom tools, and a system prompt, and is invoked with a messages payload. -- evidence: [README.md#L58-L64](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L58-L64), [README.md#L55-L56](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L55-L56) (`clm_762e9bec4b04cd8c319e7fc54e0bd24c7a3268637ea7ae88c0a96508a0cf567f`)
- [observation/documented] Any LangGraph CompiledStateGraph can be passed in as a sub-agent, allowing custom orchestration to plug into the harness. -- evidence: [README.md#L89-L89](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L89-L89) (`clm_d331baed67d974ec520db3c44235208699bafcb5a02b71dfb6c0ad5e96e15a61`)
- [observation/documented] The repository's root action.yml runs dcode non-interactively in GitHub Actions, with inputs for prompt, model, API keys, shell_allow_list, max_turns, task_timeout, quiet, and json output. -- evidence: [ACTION.md#L34-L41](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L34-L41), [ACTION.md#L3-L3](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L3-L3) (`clm_34f4a5ebe5ed14fae7dc3a7447090b3c64d3944acbbb844011d8ee9b204b5ba5`)

## memory-state (1 claim(s))

- [observation/documented] The GitHub Action enables persistent memory by default through actions/cache, with memory_scope (pr, branch, or repo) and agent_name inputs controlling cache sharing and separation. -- evidence: [ACTION.md#L57-L59](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L57-L59), [ACTION.md#L55-L55](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L55-L55) (`clm_e0d10f5857f8e11d9dfa4e38506e90c283187c0f5e18c995f0920290f54f9c26`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The product follows a 'trust the LLM' security model: the agent can do anything its tools allow, and boundaries should be enforced at the tool or sandbox level rather than by model self-policing. -- evidence: [README.md#L112-L112](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L112-L112) (`clm_8eed8e4bd58b734c05360c1dee969544a02b890d0a97caf86884ff09f77540bf`)
- [observation/documented] In the GitHub Action, shell commands are permitted via a shell_allow_list input; interactive-only options like --auto-approve are intentionally not exposed. -- evidence: [ACTION.md#L34-L41](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L34-L41), [ACTION.md#L45-L45](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L45-L45) (`clm_aedaaa38be07471c52dcdf1792330f70e02144a092d146315056d4296228620e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is distributed on PyPI as deepagents under an MIT license and is installed with uv; a separate JavaScript/TypeScript library exists in deepagentsjs. -- evidence: [README.md#L44-L44](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L44-L44), [README.md#L15-L20](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L15-L20), [README.md#L51-L53](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L51-L53) (`clm_5a025992201f12d33b773cf68a10c9cb340e78f641c8efffae2e2185179477b0`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

