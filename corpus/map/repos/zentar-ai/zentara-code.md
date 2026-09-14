# zentar-ai/zentara-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 57038931fbae @ 340c80d7850dd1e8

## Summary (orientation draft, not independently verified)

Zentara Code is distributed as a VS Code extension, installable from the marketplace, and built for VS Code 1.96.4 and later. The product exposes 25+ LSP tools for semantic code intelligence, including document symbols, workspace-wide semantic usages, call hierarchy, and targeted snippets. Evidence coverage: 143 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 23 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The product exposes 25+ LSP tools for semantic code intelligence, including document symbols, workspace-wide semantic usages, call hierarchy, and targeted snippets. -- evidence: [README.md#L129-L135](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L129-L135), [README.md#L92-L96](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L92-L96)
  - [observation/documented] A debugging tool suite of 35+ operations covers session management, execution control, breakpoint management, stack/source inspection, and state evaluation. -- evidence: [docs/Debugging.md#L58-L58](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L58-L58), [README.md#L112-L116](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L112-L116), [docs/Debugging.md#L97-L102](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L97-L102), [docs/Debugging.md#L67-L72](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L67-L72), [docs/Debugging.md#L76-L84](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L76-L84), [docs/Debugging.md#L88-L93](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L88-L93), [docs/Debugging.md#L62-L63](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L62-L63)
- design-choices (1 claim(s)):
  - [observation/documented] Code understanding is LSP-first: the workflow moves from document symbols to usages, call hierarchy, and targeted snippets rather than text matching. -- evidence: [README.md#L149-L153](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L149-L153), [README.md#L83-L87](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L83-L87)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors build from source by cloning the repo, installing dependencies with pnpm, and running 'pnpm vsix' to compile TypeScript and package a .vsix into bin/. -- evidence: [README.md#L69-L69](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L69-L69), [README.md#L47-L47](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L47-L47), [README.md#L58-L63](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L58-L63), [README.md#L65-L67](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L65-L67)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Zentara Code is distributed as a VS Code extension, installable from the marketplace, and built for VS Code 1.96.4 and later. -- evidence: [README.md#L23-L23](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L23-L23), [README.md#L25-L29](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L25-L29), [README.md#L19-L19](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L19-L19)
  - [observation/documented] Named debug operations include debug_launch, debug_quit, debug_continue, debug_step_in/out, debug_jump, debug_until, debug_set_breakpoint, debug_evaluate, and debug_execute_statement, among others. -- evidence: [docs/Debugging.md#L97-L102](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L97-L102), [docs/Debugging.md#L67-L72](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L67-L72), [docs/Debugging.md#L76-L84](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L76-L84), [docs/Debugging.md#L62-L63](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L62-L63)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Independent subagents run in parallel with isolated contexts, non-overlapping scope separation, opt-in write permissions (read-only by default), and per-agent timeouts. -- evidence: [README.md#L99-L103](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L99-L103), [README.md#L13-L15](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L13-L15), [README.md#L139-L143](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L139-L143)
- tools-permissions (1 claim(s)):
  - [observation/documented] Subagent writes are opt-in and constrained to allowed paths, with workers read-only by default; impactful actions like file writes and network access require explicit user approval. -- evidence: [README.md#L139-L143](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L139-L143), [README.md#L83-L87](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L83-L87)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Effective Python debugging requires a correctly configured Python interpreter in VS Code settings, and pytest must be installed for pytest-based debugging; TypeScript debugging needs npm and tsx. -- evidence: [README.md#L37-L42](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L37-L42), [README.md#L25-L29](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L25-L29)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](zentara-code.detail.md)

Metadata and full claim list: [full detail](zentara-code.detail.md)
Human notes ([notes](zentara-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
