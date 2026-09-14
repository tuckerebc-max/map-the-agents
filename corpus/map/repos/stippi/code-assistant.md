# stippi/code-assistant

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ba818a46c472 @ 114d3c2ae22361f3

## Summary (orientation draft, not independently verified)

Evidence describes code-assistant, an open-source Rust AI coding agent with GUI/TUI/ACP/MCP interfaces, multiple LLM providers, sessions, sandboxing, browser-agency plans, and context compaction; claims below are restricted to product behavior documented in README and design/configuration docs. Evidence coverage: 129 of 267 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 52 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The GUI is built on Zed's GPUI framework; the codebase is organized into crates including llm, code_assistant, and web, with the web crate already owning chromiumoxide for browser automation. -- evidence: [docs/context-compaction.md#L41-L44](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/context-compaction.md#L41-L44), [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/browser-agency-plan.md#L67-L70](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/browser-agency-plan.md#L67-L70)
- design-choices (3 claim(s)):
  - [observation/documented] Tool-invocation syntax is adaptive per session: native function calling, XML tags, or triple-caret blocks, selectable via --tool-syntax native|xml|caret. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/configuration.md#L187-L190](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L187-L190)
  - [observation/documented] Format-on-save runs project formatters after the assistant modifies matching files and updates tool parameters to reflect formatted content, keeping the model's view in sync without re-reading files; mappings pair glob patterns with shell commands. -- evidence: [docs/configuration.md#L144-L150](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L144-L150), [README.md#L60-L75](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L60-L75)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source requires the Rust toolchain via rustup, specific Linux system libraries for gpui, the Metal toolchain on macOS, and 'cargo build --release'; browser-agency work followed a TDD/checkpoint style where each step compiles, is tested, and is committable on its own. -- evidence: [README.md#L36-L39](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L36-L39), [README.md#L33-L33](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L33-L33), [README.md#L42-L42](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L42-L42), [README.md#L45-L48](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L45-L48), [docs/browser-agency-plan.md#L192-L193](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/browser-agency-plan.md#L192-L193)
- skills-patterns (1 claim(s)):
  - [observation/documented] The agent supports reusable, task-specific skills (playbooks) loadable on demand, and auto-loads AGENTS.md or CLAUDE.md from the project root as repo-specific guidance. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98)
- interfaces (4 claim(s)):
  - [observation/documented] The binary offers four interface modes: a native GUI by default, a terminal mode via --tui, an ACP agent via 'acp' for editors like Zed, and a headless MCP server via 'server'. -- evidence: [README.md#L102-L107](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L102-L107)
  - [observation/documented] Any mode can accept an initial task via a --task flag, e.g. asking it to explain the codebase. -- evidence: [README.md#L109-L109](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L109-L109)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions are per project with branching and persistent state; each chat session is permanently tied to its initial project/folder and tool syntax, which cannot be changed later. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/configuration.md#L133-L140](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L133-L140)
  - [observation/documented] Automatic context compaction was implemented: when prior assistant usage crosses the configured context-window threshold, a summary request is injected and the result is persisted as a user message tagged is_compaction_summary, with a collapsible UI banner. -- evidence: [docs/context-compaction.md#L41-L44](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/context-compaction.md#L41-L44)
More evidence: [full detail](code-assistant.detail.md)

Metadata and full claim list: [full detail](code-assistant.detail.md)
Human notes ([notes](code-assistant.notes.md), never overwritten by build)

[Back to map index](../../index.md)
