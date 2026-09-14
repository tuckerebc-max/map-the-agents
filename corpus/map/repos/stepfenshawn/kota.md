# stepfenshawn/kota

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 989cc1c148e5 @ 3c083603b8cbf1b6

## Summary (orientation draft, not independently verified)

The snapshot contains only README slices for kota, a Rust-based AI code agent distributed as a CLI and library crate, describing Lua configuration, a skills system, built-in tools, and multi-provider model support. All claims below are documentation-based; no code, tests, or contributor workflow details are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Kota is described as a lightweight, highly extensible AI code agent written in Rust, usable both as a CLI tool and as a Rust library. -- evidence: [README.md#L19-L19](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L19-L19), [README.md#L4-L4](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L4-L4)
- components (1 claim(s)):
  - [observation/documented] The library exposes AgentBuilder and ContextManager (from kota::kota_code) for building agents with persistent session-based conversation history. -- evidence: [README.md#L136-L138](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L136-L138), [README.md#L141-L143](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L141-L143), [README.md#L145-L151](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L145-L151)
- design-choices (1 claim(s)):
  - [observation/documented] The project states a vim-inspired philosophy: lightweight, highly extensible, simple plain-text configuration, and focus on practical development tasks. -- evidence: [README.md#L10-L10](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L10-L10), [README.md#L14-L17](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L14-L17)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] A skills system offers built-in skills (code_review, refactor, debug, documentation), each restricting the agent to a listed set of tools, activated via /skill and deactivated via /skill-off. -- evidence: [README.md#L308-L309](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L308-L309), [README.md#L284-L284](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L284-L284), [README.md#L302-L302](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L302-L302), [README.md#L288-L293](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L288-L293)
- interfaces (3 claim(s)):
  - [observation/documented] Configuration is Lua-based, inspired by Neovim, via a .kota/config.lua file in the project root with a kota.setup call. -- evidence: [README.md#L40-L45](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L40-L45), [README.md#L38-L38](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L38-L38)
  - [observation/documented] The interactive CLI exposes commands such as /config, /history, /skills, /skill, /load, /sessions, /delete, and /quit, with tab completion for partial commands. -- evidence: [README.md#L196-L205](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L196-L205), [README.md#L251-L253](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L251-L253), [README.md#L249-L249](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L249-L249)
- memory-state (1 claim(s)):
  - [observation/documented] ContextManager stores conversation history in sessions under a .chat_sessions directory, and context is maintained automatically across chat calls. -- evidence: [README.md#L141-L143](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L141-L143), [README.md#L157-L159](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L157-L159)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Built-in tools include read_file, write_file, edit_file, delete_file, make_dir, scan_codebase, grep_find, exec_cmd, and update_plan for structured task plans. -- evidence: [README.md#L268-L278](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L268-L278)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Kota supports OpenAI-compatible models, DeepSeek, and Anthropic Claude, plus any OpenAI-compatible endpoint and local models via Ollama or similar services. -- evidence: [README.md#L185-L186](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L185-L186), [README.md#L180-L182](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L180-L182)
  - [observation/documented] Library usage requires adding kota 0.1.3, tokio with full features, and anyhow as Cargo dependencies. -- evidence: [README.md#L124-L130](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L124-L130)
- limitations (1 claim(s)):
  - [observation/documented] Per the README, MCP server support, custom UI components, and workflow definitions are planned/future features, not yet shipped. -- evidence: [README.md#L104-L110](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L104-L110), [README.md#L83-L100](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L83-L100), [README.md#L315-L318](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L315-L318)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](kota.detail.md)

Metadata and full claim list: [full detail](kota.detail.md)
Human notes ([notes](kota.notes.md), never overwritten by build)

[Back to map index](../../index.md)
