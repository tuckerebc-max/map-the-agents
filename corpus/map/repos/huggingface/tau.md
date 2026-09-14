# huggingface/tau

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a8f18e7bc645 @ e787110266cc3f66

## Summary (orientation draft, not independently verified)

Tau is a terminal coding agent published as tau-ai, structured as three packages (tau_ai, tau_agent, tau_coding) with an event-driven harness core. Evidence is mostly README/CONTRIBUTING documentation; contributor instructions cover development practice only.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Tau is split into three layers: tau_ai (provider/model streaming), tau_agent (portable harness with loop, tools, events, sessions), and tau_coding (CLI, TUI, skills, on-disk sessions). -- evidence: [README.md#L42-L46](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L42-L46), [AGENTS.md#L25-L29](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/AGENTS.md#L25-L29)
- design-choices (2 claim(s)):
  - [observation/documented] The architecture treats a typed event stream as the contract: providers, renderers, the TUI, and custom frontends all consume events rather than the core rendering UI itself. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L221-L222](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L221-L222)
  - [observation/documented] The core harness is kept portable: it does not depend on Textual, Rich, local config paths, slash commands, or rendering, and frontends consume its events. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L56-L57](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L56-L57)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run checks via uv (uv run pytest, ruff check, ruff format --check, mypy), keep commits atomic, and add tests for behavior changes before expanding features. -- evidence: [AGENTS.md#L47-L53](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/AGENTS.md#L47-L53), [README.md#L228-L234](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L228-L234), [CONTRIBUTING.md#L62-L67](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L62-L67), [CONTRIBUTING.md#L104-L108](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L104-L108)
  - [observation/documented] Repository development practice: releases to PyPI are intentional — a version bump in pyproject.toml merged via PR triggers publishing, not every merge to main. -- evidence: [CONTRIBUTING.md#L127-L128](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L127-L128), [CONTRIBUTING.md#L130-L135](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L130-L135)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] As a library, users construct AgentHarness with AgentHarnessConfig (provider, model, system prompt, tools) and consume an async event stream from harness.prompt(). -- evidence: [README.md#L205-L206](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L205-L206), [README.md#L208-L215](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L208-L215), [README.md#L217-L219](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L217-L219)
  - [observation/documented] The CLI supports interactive TUI and one-shot print mode (tau -p), a --cwd option, and slash commands such as /login and /model for provider and model selection. -- evidence: [README.md#L148-L151](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L148-L151), [README.md#L159-L164](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L159-L164), [README.md#L176-L185](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L176-L185)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are stored as durable, append-only JSONL files under ~/.tau/sessions/ with resume and branching, and active context can be compacted without rewriting the record. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L176-L185](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L176-L185)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Tau ships built-in coding tools named read, write, edit, and bash, described as typed functions with a schema and an async executor returning structured results. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L176-L185](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L176-L185)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](tau.detail.md)

Metadata and full claim list: [full detail](tau.detail.md)
Human notes ([notes](tau.notes.md), never overwritten by build)

[Back to map index](../../index.md)
