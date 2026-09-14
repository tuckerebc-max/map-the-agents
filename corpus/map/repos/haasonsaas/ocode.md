# haasonsaas/ocode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b1877260448f @ be083d75cb1a2abf

## Summary (orientation draft, not independently verified)

Selected evidence records: OCode is described as a terminal-native AI coding assistant built to work with local Ollama models, offering codebase intelligence and autonomous task execution. The product is invoked via a Python CLI (python -m ocode_python.core.cli) supporting interactive mode, single-prompt mode with -p, model selection with -m, and JSON/stream-json output formats.

## Source coverage

Source coverage (partial): 6 of 32 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] OCode is described as a terminal-native AI coding assistant built to work with local Ollama models, offering codebase intelligence and autonomous task execution. -- evidence: [README.md#L5-L5](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] MCP (Model Context Protocol) is described as an extensible plugin layer for third-party integrations, exposed via an mcp tool. -- evidence: [README.md#L10-L14](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L10-L14), [README.md#L62-L63](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L62-L63)
- design-choices (1 claim(s)):
  - [observation/documented] The README describes multi-action query detection that maps compound prompts to multiple tools, plus context strategies (none/minimal/targeted/full) based on query complexity. -- evidence: [README.md#L351-L357](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L351-L357), [README.md#L366-L368](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L366-L368)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is invoked via a Python CLI (python -m ocode_python.core.cli) supporting interactive mode, single-prompt mode with -p, model selection with -m, and JSON/stream-json output formats. -- evidence: [README.md#L374-L375](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L374-L375), [README.md#L412-L412](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L412-L412), [README.md#L388-L389](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L388-L389), [README.md#L400-L401](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L400-L401), [README.md#L391-L391](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L391-L391), [README.md#L377-L377](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L377-L377), [README.md#L403-L403](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L403-L403), [README.md#L415-L416](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L415-L416)
  - [observation/documented] Behavior is configurable through environment variables including OCODE_MODEL, OLLAMA_HOST, OCODE_VERBOSE, OCODE_TEMPERATURE, and OCODE_TIMEOUT. -- evidence: [README.md#L441-L441](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L441-L441), [README.md#L450-L451](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L450-L451), [README.md#L601-L603](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L601-L603), [README.md#L444-L444](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L444-L444), [README.md#L447-L447](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L447-L447)
- memory-state (1 claim(s)):
  - [observation/documented] The toolset includes memory_tools for managing context and session memory. -- evidence: [README.md#L56-L59](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L56-L59)
- orchestration (1 claim(s)):
  - [observation/documented] An agent tool is included to delegate complex tasks to specialized agents, with the README noting agent delegation recommendations for multi-step workflows. -- evidence: [README.md#L360-L363](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L360-L363), [README.md#L56-L59](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L56-L59)
- tools-permissions (1 claim(s)):
  - [observation/documented] Runtime permissions are configurable via settings, including allow_file_read/write, allow_shell_exec, allow_git_ops, allowed_paths, blocked_paths, and blocked_commands such as rm and sudo. -- evidence: [README.md#L455-L470](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L455-L470), [README.md#L425-L429](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L425-L429), [README.md#L431-L436](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L431-L436), [README.md#L607-L620](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L607-L620), [README.md#L622-L634](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L622-L634)
- evaluation (1 claim(s)):
  - [observation/documented] The README claims enhanced accuracy of over 97% for query categorization, though this is a documentation assertion not backed by visible benchmark code. -- evidence: [README.md#L366-L368](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L366-L368)
- dependencies (1 claim(s)):
  - [observation/documented] Required prerequisites are Python 3.8+ and pip; Ollama (a local LLM server) and Git are listed as needed for full functionality. -- evidence: [README.md#L94-L96](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L94-L96), [README.md#L90-L92](https://github.com/haasonsaas/ocode/blob/b1877260448f82269aeecfff3d36b13f0958a542/README.md#L90-L92)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](ocode.detail.md).

Metadata and full claim list: [full detail](ocode.detail.md)
Human notes ([notes](ocode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
