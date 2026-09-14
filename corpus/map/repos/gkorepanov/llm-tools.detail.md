# gkorepanov/llm-tools -- full detail

[Back to orientation](llm-tools.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gkorepanov/llm-tools/49867219956ad3cba942d3b4c78be79ffd1dffbf/2eddf75b8b535de6.json](../../../wiki/dossiers/gkorepanov/llm-tools/49867219956ad3cba942d3b4c78be79ffd1dffbf/2eddf75b8b535de6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The package is described as a small shared library for Voicebot's streamed LLM calls. -- evidence: [README.md#L3-L3](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L3-L3) (`clm_56c4f5020f3a450dc46aaa917a17ac19db7b2ab89aa90f83adfa53be4069f5f3`)
- [observation/documented] It provides LiteLLM-based async chat streaming with bounded initial-request and mid-stream retries. -- evidence: [README.md#L7-L13](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L7-L13) (`clm_825fed1aba3b0c3157d91b29dfaa6d7d4cf7fe13b5443e6c2eb99d0e61271da7`)
- [observation/documented] It supports ordered fallback across configured model providers, plus empty-response and context-window error handling. -- evidence: [README.md#L7-L13](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L7-L13) (`clm_8169d6398e89f30b308fcd978634d37af491e34e82e1fd1a53cb4c681f6c97fb`)
- [observation/documented] The package includes input/output token accounting with price estimation, message conversion helpers, and UI translation utilities. -- evidence: [README.md#L7-L13](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L7-L13) (`clm_12d19271dfc920f21baf1fe644fa0568ed95a9ca4fe0d10c9f32355bd64ba5dd`)

## design-choices (1 claim(s))

- [observation/documented] Production model chains live in the bot's private configuration and are constructed by bot/parsing/generator.py, currently using Google Gemini as primary with OpenAI GPT-5.4 mini as fallback. -- evidence: [README.md#L15-L17](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L15-L17) (`clm_7407c05f5ff68c89eab7ab378bdebb10b997fdd6e45c5ac6be78e1060c108874`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Model chains are built on LiteLLM, and the README states the package no longer uses LangChain. -- evidence: [README.md#L7-L13](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L7-L13), [README.md#L19-L19](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L19-L19) (`clm_52f50981951a2a209868ecf981b93327b8fb28f862fe92889e546da364cb500c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

