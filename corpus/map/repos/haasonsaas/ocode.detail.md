# haasonsaas/ocode -- full detail

[Back to orientation](ocode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/haasonsaas/ocode/b1877260448f82269aeecfff3d36b13f0958a542/be083d75cb1a2abf.json](../../../wiki/dossiers/haasonsaas/ocode/b1877260448f82269aeecfff3d36b13f0958a542/be083d75cb1a2abf.json)

## specifications (1 claim(s))

- [observation/documented] OCode is described as a terminal-native AI coding assistant built to work with local Ollama models, offering codebase intelligence and autonomous task execution. -- evidence: [README.md#L5-L5](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L5-L5) (`clm_146399fc3688144856f263090d46a1f4d441553e884e95a7e95c7691bdc00609`)

## components (1 claim(s))

- [observation/documented] MCP (Model Context Protocol) is described as an extensible plugin layer for third-party integrations, exposed via an mcp tool. -- evidence: [README.md#L10-L14](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L10-L14), [README.md#L62-L63](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L62-L63) (`clm_e0f7d93b06e0bd1e2093e92901cf070f0f9364ad3bd55382a7584d49535d17b0`)

## design-choices (1 claim(s))

- [observation/documented] The README describes multi-action query detection that maps compound prompts to multiple tools, plus context strategies (none/minimal/targeted/full) based on query complexity. -- evidence: [README.md#L351-L357](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L351-L357), [README.md#L366-L368](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L366-L368) (`clm_577d2811c621c3738641c66f8d2dc8ee879762bc786a10149675b20c36b90242`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is invoked via a Python CLI (python -m ocode_python.core.cli) supporting interactive mode, single-prompt mode with -p, model selection with -m, and JSON/stream-json output formats. -- evidence: [README.md#L374-L375](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L374-L375), [README.md#L412-L412](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L412-L412), [README.md#L388-L389](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L388-L389), [README.md#L400-L401](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L400-L401), [README.md#L391-L391](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L391-L391), [README.md#L377-L377](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L377-L377), [README.md#L403-L403](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L403-L403), [README.md#L415-L416](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L415-L416) (`clm_4eb8156ad1fb9b441936e0edb5bc8f4a04dc11a25816e5092df8ad961d4da664`)
- [observation/documented] Behavior is configurable through environment variables including OCODE_MODEL, OLLAMA_HOST, OCODE_VERBOSE, OCODE_TEMPERATURE, and OCODE_TIMEOUT. -- evidence: [README.md#L441-L441](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L441-L441), [README.md#L450-L451](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L450-L451), [README.md#L601-L603](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L601-L603), [README.md#L444-L444](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L444-L444), [README.md#L447-L447](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L447-L447) (`clm_e8724ed61f697fd8372577f308ad9f97abc4cff152566620d4b7d2c181619dc7`)

## memory-state (1 claim(s))

- [observation/documented] The toolset includes memory_tools for managing context and session memory. -- evidence: [README.md#L56-L59](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L56-L59) (`clm_dc3fd546d942ee9a6ac9881b9a1d280f59f5449b3f80534e90bb3db8cc0b256c`)

## orchestration (1 claim(s))

- [observation/documented] An agent tool is included to delegate complex tasks to specialized agents, with the README noting agent delegation recommendations for multi-step workflows. -- evidence: [README.md#L360-L363](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L360-L363), [README.md#L56-L59](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L56-L59) (`clm_d7181f461def0da71713d81915062f8316dd29b3a557134c9598553c9ded3d68`)

## tools-permissions (1 claim(s))

- [observation/documented] Runtime permissions are configurable via settings, including allow_file_read/write, allow_shell_exec, allow_git_ops, allowed_paths, blocked_paths, and blocked_commands such as rm and sudo. -- evidence: [README.md#L455-L470](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L455-L470), [README.md#L425-L429](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L425-L429), [README.md#L431-L436](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L431-L436), [README.md#L607-L620](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L607-L620), [README.md#L622-L634](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L622-L634) (`clm_1a94fe3c6379fc50ce50cc773aeede7472b8d2014ea577f5bc77649368b86f5b`)

## evaluation (1 claim(s))

- [observation/documented] The README claims enhanced accuracy of over 97% for query categorization, though this is a documentation assertion not backed by visible benchmark code. -- evidence: [README.md#L366-L368](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L366-L368) (`clm_3e3a392edf6c35cdc48c5a4741c7c389ab410a4bd7f06c5a404f0cc6beeded04`)

## dependencies (1 claim(s))

- [observation/documented] Required prerequisites are Python 3.8+ and pip; Ollama (a local LLM server) and Git are listed as needed for full functionality. -- evidence: [README.md#L94-L96](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L94-L96), [README.md#L90-L92](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L90-L92) (`clm_2f67450b07cfa481c5c338f38141624a9e7d664ae5da3985fe5c912178eb319e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

