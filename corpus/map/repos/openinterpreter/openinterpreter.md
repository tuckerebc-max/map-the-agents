# openinterpreter/openinterpreter

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 860153a5318d @ 5584e08deae693c9

## Summary (orientation draft, not independently verified)

Open Interpreter is a Rust-based fork of OpenAI's Codex positioned as a coding agent for low-cost models, with multiple emulated harnesses, ACP/Codex-SDK compatibility, TOML configuration, sandboxing/approval controls, execution policies, and permission profiles. Evidence is documentation-only; no code inspection or evaluation results are present.

## Source coverage

Source coverage (partial): 6 of 115 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project describes itself as a fork of OpenAI's Codex focused on emulating the agent harness that gets the best performance from low-cost models. -- evidence: [README.md#L47-L47](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L47-L47)
- components (1 claim(s)):
  - [observation/documented] The product ships a QA skill that can drive web apps in a real browser via agent-browser or operate native apps via trycua. -- evidence: [README.md#L101-L101](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L101-L101)
- design-choices (1 claim(s)):
  - [observation/documented] Portability is a stated product goal: shared AGENTS.md, `.agents/skills` directories, MCP, ACP, and the Codex exec protocol are preferred, with `~/.openinterpreter` reserved for config and runtime state lacking shared standards. -- evidence: [README.md#L89-L94](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L89-L94), [README.md#L84-L87](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L84-L87)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: provider and model membership is generated rather than maintained as Rust lists, refreshed from `codex-rs` with `python3 scripts/write_provider_catalog.py`, and a `scripts/test-codex-sdk-compat.sh` script provides a local provider-free compatibility check. -- evidence: [README.md#L134-L139](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L134-L139), [README.md#L80-L80](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L80-L80)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills live in shared `.agents/skills` or `~/.agents/skills` directories; legacy product-specific skill directories remain readable for compatibility. -- evidence: [README.md#L89-L94](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L89-L94)
- interfaces (4 claim(s)):
  - [observation/documented] A `/harness` TUI command switches the active harness among listed modes including native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent, and minimal. -- evidence: [README.md#L49-L49](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L49-L49), [README.md#L54-L64](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L54-L64), [README.md#L51-L52](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L51-L52)
  - [observation/documented] The product runs as an Agent Client Protocol agent via `interpreter acp` and speaks the Codex exec protocol, allowing a one-line Codex SDK binary override to `interpreter`. -- evidence: [README.md#L70-L70](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L70-L70), [README.md#L72-L73](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L72-L73), [README.md#L80-L80](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L80-L80), [README.md#L75-L78](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L75-L78)
- memory-state (1 claim(s)):
  - [observation/documented] AGENTS.md instructions are loaded from a global path (`~/.openinterpreter/AGENTS.md`) and project files from repo root to the current directory, with closer files taking precedence and a `project_doc_max_bytes` cap. -- evidence: [docs/agents_md.md#L30-L30](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L30-L30), [docs/agents_md.md#L52-L54](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L52-L54), [docs/agents_md.md#L32-L35](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L32-L35), [docs/agents_md.md#L37-L38](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L37-L38)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (3 claim(s)):
  - [observation/documented] An execution policy labels each command as safe, unsafe, or forbid before it runs; forbid blocks outright, safe runs without prompting, and unsafe defers to the approval mode. -- evidence: [docs/execpolicy.md#L45-L47](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L45-L47), [docs/execpolicy.md#L6-L7](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L6-L7), [docs/execpolicy.md#L42-L43](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L42-L43), [docs/execpolicy.md#L9-L13](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L9-L13)
More evidence: [full detail](openinterpreter.detail.md)

Metadata and full claim list: [full detail](openinterpreter.detail.md)
Human notes ([notes](openinterpreter.notes.md), never overwritten by build)

[Back to map index](../../index.md)
