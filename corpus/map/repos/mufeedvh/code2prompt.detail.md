# mufeedvh/code2prompt -- full detail

[Back to orientation](code2prompt.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mufeedvh/code2prompt/66585136062c04275ddd5a01c5518a4d78c4aa76/44061f456b2f99ce.json](../../../wiki/dossiers/mufeedvh/code2prompt/66585136062c04275ddd5a01c5518a4d78c4aa76/44061f456b2f99ce.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The ecosystem comprises a Rust core library for file traversal, gitignore handling, and Git metadata; a CLI/TUI; a Python SDK with bindings to the Rust core published on PyPI; and an MCP server. -- evidence: [README.md#L109-L111](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L109-L111) (`clm_9021b31f6a2716e56028a92d3444c4426037dd3a5439242180b3ea43fd5aa884`)

## design-choices (3 claim(s))

- [observation/documented] Prompt generation respects .gitignore rules, supports glob-based include/exclude filtering, and uses Handlebars templates that users can customize. -- evidence: [README.md#L121-L128](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L121-L128), [README_ES.md#L28-L37](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L28-L37), [README_ES.md#L98-L98](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L98-L98) (`clm_3b102fe8eeff36f54ad5676bb23d1a70c2d64747b8c9e6786e5bbd5a96fa8295`)
- [observation/documented] Token counts are estimated via parallel per-file counts plus estimated template overhead; the full rendered prompt is not re-tokenized and the JSON envelope is excluded from the estimate. -- evidence: [README.md#L121-L128](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L121-L128) (`clm_f8d18be7088dd821d582f6aee9e3a54df42f184f13ce6f9d36272c5aa065f051`)
- [observation/documented] Templates can include user-defined variables outside the default context (absolute_code_path, source_tree, files); the tool prompts the user for their values at generation time. -- evidence: [README_ES.md#L239-L239](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L239-L239), [README_ES.md#L241-L241](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L241-L241), [README_ES.md#L237-L237](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L237-L237) (`clm_f45a47bfd2091789a085d9887f7d884344134876c4b4e611feaaf2a25072287f`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to follow existing patterns, place reusable logic in code2prompt-core, keep Python bindings thin, include regression tests for bug fixes, and map changed paths to verification skills (verify-core, verify-cli, verify-python, verify-website). -- evidence: [AGENTS.md#L9-L19](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L9-L19), [AGENTS.md#L23-L28](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L23-L28) (`clm_138b4163003d8f6b373a9a28adfb8451b8b0a6ed5a223a033a0f667dd8ba9661`)
- [observation/documented] Repository development practice: root cargo test does not exercise the Python bindings, and contributors should not claim completion until the relevant verification skill passes. -- evidence: [AGENTS.md#L30-L31](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L30-L31), [AGENTS.md#L9-L19](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L9-L19) (`clm_72a6c3746aaefe962cb95fbcf90706785c204331ccd0cf25f8d5c3116e5772f7`)

## skills-patterns (2 claim(s))

- [observation/documented] An installable agent skill (skills/code2prompt/SKILL.md) teaches coding agents to use code2prompt for repository navigation and scoped context gathering, installable via the Skills CLI (npx skills add mufeedvh/code2prompt). -- evidence: [README.md#L85-L87](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L85-L87), [README.md#L82-L83](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L82-L83), [README.md#L89-L93](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L89-L93) (`clm_1bf8957122c5db5db52bd23a0d3416154f87ae22df82df1bd95d938759b3c41b`)
- [observation/documented] The skill installer adds only the skill folder and its template, possibly cloning the repository temporarily; the rest of the repository is not installed. -- evidence: [README.md#L95-L97](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L95-L97) (`clm_ac3eff7f44cd12487c2e51b7b902e8c857b0e7d4b2ffc51be50b7659668fdf32`)

## interfaces (2 claim(s))

- [observation/documented] With --json, the tool outputs a JSON object containing prompt, directory_name, token_count, model_info, and files fields. -- evidence: [README_ES.md#L144-L144](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L144-L144), [README_ES.md#L152-L160](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L152-L160) (`clm_88f93e79164fa4465e0844b3e24c700547d3db554b8a634db9a3cc58110d81dc`)
- [observation/documented] The project ships an MCP server (code2prompt-mcp) that exposes codebase context generation to LLM applications like Claude Desktop, Cursor, Roo Code, and Cline, configured via an mcpServers JSON entry. -- evidence: [llms-install.md#L52-L65](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/llms-install.md#L52-L65), [llms-install.md#L3-L3](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/llms-install.md#L3-L3), [llms-install.md#L7-L7](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/llms-install.md#L7-L7) (`clm_bc95c53df1713d43524d914e9f11599fe20256de2aacb1b677414078af46ceac`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Tokenization is implemented with tiktoken-rs, supporting encodings cl100k_base, p50k_base, p50k_edit, r50k_base, and o200k_base for OpenAI model families. -- evidence: [README_ES.md#L134-L136](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L134-L136), [README_ES.md#L247-L247](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L247-L247), [README_ES.md#L249-L255](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L249-L255) (`clm_22d3e8339c0a7c3eb8a1111cf7b5ad3495c48728818bf597fce2a95d3eab0692`)

## limitations (1 claim(s))

- [observation/documented] The token estimate is approximate by design: it relies on per-file counts and estimated template overhead rather than tokenizing the fully rendered prompt. -- evidence: [README.md#L121-L128](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L121-L128) (`clm_89f6e0da0c6cdbf76dd21284ed73c7529549a2c1467d25bdc56724c0812de97d`)

## relevance (1 claim(s))

- [observation/documented] The tool targets LLM context preparation: generating prompts from codebases for chat models, AI agents, RAG pipelines, and MCP-based agentic workflows. -- evidence: [README.md#L119-L119](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L119-L119), [README.md#L36-L36](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L36-L36), [README.md#L109-L111](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L109-L111) (`clm_f5a8dd5955c8625c98428866b0f3c363cd47a414d854ac7ab96d1a89ed61445d`)

