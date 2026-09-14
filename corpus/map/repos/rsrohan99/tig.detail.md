# rsrohan99/tig -- full detail

[Back to orientation](tig.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rsrohan99/tig/3df12189c01e2674991bc998404af7217ae5b9d8/ebda47659608a8ec.json](../../../wiki/dossiers/rsrohan99/tig/3df12189c01e2674991bc998404af7217ae5b9d8/ebda47659608a8ec.json)

## specifications (1 claim(s))

- [observation/documented] Tig is described as an autonomous AI coding agent that runs in the terminal, comparable to Claude Code and OpenAI Codex but supporting more LLMs. -- evidence: [README.md#L2-L2](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L2-L2) (`clm_0fada0e8b47bea460c653f71b2fc008a5605ad6b737b5fe18215bc3beab3a57d`)

## components (2 claim(s))

- [observation/documented] The agent can write code, fix bugs, execute shell commands, write tests, and analyze a codebase, all within the terminal. -- evidence: [README.md#L4-L9](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L4-L9), [README.md#L11-L11](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L11-L11) (`clm_399928b6fa686a1f334fd141b4ac87ed933874f4852a645f7046c54d59869faa`)
- [observation/documented] The toolchain uses LlamaIndex Workflows for orchestration and multi-LLM support, Tree-sitter for code-definition search and syntax-error checking, Ripgrep for regex search, and diff-match-patch for displaying diffs. -- evidence: [README.md#L35-L38](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L35-L38) (`clm_ee61f2a2f45d79041ef15196f6088a9e103a38871fb9e25de82cc1c08cad9f78`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Users start a session by running tig and entering a task at the 'New task' prompt. -- evidence: [README.md#L95-L100](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L95-L100) (`clm_e0dba9763763ccf2c730d2aef217b3db34820b97bdea165638045d6a55ef968e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Tig offers task modes: an Architect mode that designs systems and saves designs to a markdown file, and a Code mode that implements the architect's plan step by step. -- evidence: [README.md#L19-L21](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L19-L21) (`clm_8e8a405f9ca3d8568fd4bb348b0946c5f1ae032ef75fb02c35d8b064b1ca8b05`)
- [observation/documented] Tig is installed via pip as the tig-code package and run with the tig command, optionally with a --mode flag choosing code or architect. -- evidence: [README.md#L68-L72](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L68-L72), [README.md#L86-L93](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L86-L93) (`clm_57924eb2a964f8b30b16883683ae0766eaad0101bfb6fcb9dd247153518924a0`)
- [observation/documented] Configuration is done through a .env file specifying the provider (google, openai, anthropic, deepseek, groq, ollama, openrouter), model (e.g. TIG_MODEL), and the matching provider API key. -- evidence: [README.md#L78-L84](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L78-L84), [README.md#L76-L76](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L76-L76) (`clm_c2a870957dfc98a6628a68aec3082a1dd109a5b5442d45672bd9b549f1a4b365`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] By default Tig's file read/write/update actions appear to require approval; a --auto-approve flag lets users auto-approve all actions. -- evidence: [README.md#L86-L93](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L86-L93) (`clm_d8a96cf9f697b9e0daed31bb07f70e8f37ddea9f0cd372fe129a287c12b0d932`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Supported LLM providers include Google Gemini, OpenAI, Claude, OpenRouter, Deepseek, Groq, and local models via Ollama. -- evidence: [README.md#L23-L30](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L23-L30) (`clm_ae4bcf922f5e37a2ef0bea586f175f7bf7add26e6c13afc06f54760c8af663ed`)
- [observation/documented] Ripgrep is listed as an external tool Tig depends on, with per-OS install instructions (Homebrew on macOS, pacman on Arch, dnf on Fedora). -- evidence: [README.md#L56-L59](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L56-L59), [README.md#L45-L45](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L45-L45), [README.md#L43-L43](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L43-L43), [README.md#L61-L64](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L61-L64), [README.md#L49-L52](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L49-L52) (`clm_a4b342a90d9afa0ed9b1ce7c55b254e8b0c94433887c8b65519fda02f3638332`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

