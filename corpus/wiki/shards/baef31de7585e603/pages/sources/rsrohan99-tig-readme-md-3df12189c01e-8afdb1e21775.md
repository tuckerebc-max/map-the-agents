---
access: public
aliases: []
claim_ids:
- clm_0fada0e8b47bea460c653f71b2fc008a5605ad6b737b5fe18215bc3beab3a57d
- clm_399928b6fa686a1f334fd141b4ac87ed933874f4852a645f7046c54d59869faa
- clm_57924eb2a964f8b30b16883683ae0766eaad0101bfb6fcb9dd247153518924a0
- clm_8e8a405f9ca3d8568fd4bb348b0946c5f1ae032ef75fb02c35d8b064b1ca8b05
- clm_a4b342a90d9afa0ed9b1ce7c55b254e8b0c94433887c8b65519fda02f3638332
- clm_ae4bcf922f5e37a2ef0bea586f175f7bf7add26e6c13afc06f54760c8af663ed
- clm_c2a870957dfc98a6628a68aec3082a1dd109a5b5442d45672bd9b549f1a4b365
- clm_d8a96cf9f697b9e0daed31bb07f70e8f37ddea9f0cd372fe129a287c12b0d932
- clm_e0dba9763763ccf2c730d2aef217b3db34820b97bdea165638045d6a55ef968e
- clm_ee61f2a2f45d79041ef15196f6088a9e103a38871fb9e25de82cc1c08cad9f78
maturity: draft
page_id: pg_f33ea569482c56958eba8afdb1e21775
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_943392479c4c58a18175c7031ad2563e
title: rsrohan99/tig/README.md @ 3df12189c01e
updated_at: '2026-09-14T02:37:20Z'
---

# rsrohan99/tig/README.md @ 3df12189c01e

<!-- rcw:begin owner=source:src_943392479c4c58a18175c7031ad2563e block=evidence -->
- Tig is described as an autonomous AI coding agent that runs in the terminal, comparable to Claude Code and OpenAI Codex but supporting more LLMs. [@claim:clm_0fada0e8b47bea460c653f71b2fc008a5605ad6b737b5fe18215bc3beab3a57d]
- The agent can write code, fix bugs, execute shell commands, write tests, and analyze a codebase, all within the terminal. [@claim:clm_399928b6fa686a1f334fd141b4ac87ed933874f4852a645f7046c54d59869faa]
- Tig is installed via pip as the tig-code package and run with the tig command, optionally with a --mode flag choosing code or architect. [@claim:clm_57924eb2a964f8b30b16883683ae0766eaad0101bfb6fcb9dd247153518924a0]
- Tig offers task modes: an Architect mode that designs systems and saves designs to a markdown file, and a Code mode that implements the architect's plan step by step. [@claim:clm_8e8a405f9ca3d8568fd4bb348b0946c5f1ae032ef75fb02c35d8b064b1ca8b05]
- Ripgrep is listed as an external tool Tig depends on, with per-OS install instructions (Homebrew on macOS, pacman on Arch, dnf on Fedora). [@claim:clm_a4b342a90d9afa0ed9b1ce7c55b254e8b0c94433887c8b65519fda02f3638332]
- Supported LLM providers include Google Gemini, OpenAI, Claude, OpenRouter, Deepseek, Groq, and local models via Ollama. [@claim:clm_ae4bcf922f5e37a2ef0bea586f175f7bf7add26e6c13afc06f54760c8af663ed]
- Configuration is done through a .env file specifying the provider (google, openai, anthropic, deepseek, groq, ollama, openrouter), model (e.g. TIG_MODEL), and the matching provider API key. [@claim:clm_c2a870957dfc98a6628a68aec3082a1dd109a5b5442d45672bd9b549f1a4b365]
- By default Tig's file read/write/update actions appear to require approval; a --auto-approve flag lets users auto-approve all actions. [@claim:clm_d8a96cf9f697b9e0daed31bb07f70e8f37ddea9f0cd372fe129a287c12b0d932]
- Users start a session by running tig and entering a task at the 'New task' prompt. [@claim:clm_e0dba9763763ccf2c730d2aef217b3db34820b97bdea165638045d6a55ef968e]
- The toolchain uses LlamaIndex Workflows for orchestration and multi-LLM support, Tree-sitter for code-definition search and syntax-error checking, Ripgrep for regex search, and diff-match-patch for displaying diffs. [@claim:clm_ee61f2a2f45d79041ef15196f6088a9e103a38871fb9e25de82cc1c08cad9f78]
<!-- rcw:end owner=source:src_943392479c4c58a18175c7031ad2563e block=evidence -->

## Researcher notes

