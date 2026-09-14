# gi-dellav/zerostack

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit efd142b3ac46 @ a1aca222966d5bd8

## Summary (orientation draft, not independently verified)

README and ARCHITECTURE.md describe zerostack, a minimal Rust coding agent with multi-provider LLM support, a five-mode permission system, session/memory/worktree/loop features (several feature-gated), and a documented single-crate architecture. Evidence is documentation-based; no code slices are included. Evidence coverage: 127 of 397 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] zerostack is a minimal coding agent written in Rust, inspired by pi and opencode. -- evidence: [README.md#L6-L6](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L6-L6)
- components (1 claim(s)):
  - [observation/documented] The project is a single Rust crate with source under src/, including agent, session, permission, ui, context, and config modules; the TUI is custom on crossterm without ratatui. -- evidence: [ARCHITECTURE.md#L8-L24](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L8-L24), [ARCHITECTURE.md#L3-L4](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L3-L4), [ARCHITECTURE.md#L95-L101](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L95-L101)
- design-choices (1 claim(s)):
  - [observation/documented] Provider abstraction uses type-erased enums (AnyClient/AnyModel/AnyAgent) instead of trait objects, and tokio runs single-threaded by default unless the multithread feature is enabled. -- evidence: [ARCHITECTURE.md#L28-L40](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L28-L40), [ARCHITECTURE.md#L95-L101](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L95-L101)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: unit tests live in src/tests/ and headless TUI-loop integration tests drive the real loop with a FakeBackend and mock agent models, without a terminal or network. -- evidence: [ARCHITECTURE.md#L44-L45](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L44-L45)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The agent supports multiple LLM providers: OpenRouter (default), OpenAI-compatible, Anthropic, Gemini, and Ollama, plus custom providers configured via config.yaml. -- evidence: [README.md#L536-L540](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L536-L540), [README.md#L542-L543](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L542-L543), [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32)
  - [observation/documented] A prompts system lets users switch built-in system prompts (code, plan, review, debug, ask, etc.) at runtime via /prompt, and custom prompts can be added as markdown files under the config prompts directory. -- evidence: [README.md#L206-L208](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L206-L208), [README.md#L212-L227](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L212-L227), [README.md#L229-L230](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L229-L230)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions are saved as JSON under $XDG_DATA_HOME/zerostack/sessions/ and can be resumed with -c, -r, or --session <id>; auto-compaction summarizes old messages near the context-window limit. -- evidence: [README.md#L331-L333](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L331-L333), [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32), [ARCHITECTURE.md#L95-L101](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L95-L101), [ARCHITECTURE.md#L91-L91](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L91-L91)
  - [observation/documented] The gated memory feature keeps plain-Markdown notes (global MEMORY.md plus per-project logs) injected into the system prompt each session; it is not in the default build. -- evidence: [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32), [README.md#L337-L338](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L337-L338), [README.md#L344-L344](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L344-L344), [README.md#L340-L342](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L340-L342)
- orchestration (2 claim(s)):
  - [observation/documented] Git worktree integration offers /worktree, /wt-merge, and /wt-exit slash commands for a branch-per-task workflow, with optional auto-merge on exit; the feature is labeled experimental. -- evidence: [README.md#L442-L442](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L442-L442), [README.md#L463-L466](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L463-L466), [README.md#L448-L452](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L448-L452), [README.md#L440-L440](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L440-L440)
More evidence: [full detail](zerostack.detail.md)

Metadata and full claim list: [full detail](zerostack.detail.md)
Human notes ([notes](zerostack.notes.md), never overwritten by build)

[Back to map index](../../index.md)
