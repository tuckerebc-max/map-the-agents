# l3yx/intentlang

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6ce1cf88eac8 @ 1ecf66ae56c28c19

## Summary (orientation draft, not independently verified)

IntentLang is a Python-based, intent-driven AI programming framework whose README documents an Intent builder API, compile/run execution over an iterative Executor and embedded REPL Runtime, reference-based data passing, and a security warning about executing AI-generated code. All evidence is from README.md; no code or evaluation evidence is present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] IntentLang replaces discrete function calling with continuous, stateful Python code generation and execution, treating tools as embedded objects rather than external APIs. -- evidence: [README.md#L58-L63](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L58-L63), [README.md#L87-L88](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L87-L88), [README.md#L75-L76](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L75-L76)
  - [observation/documented] Input data is passed by reference and not serialized into the LLM context; the model receives only names and descriptions and must generate code to access in-memory objects. -- evidence: [README.md#L81-L82](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L81-L82), [README.md#L349-L349](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L349-L349), [README.md#L153-L153](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L153-L153)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The core API is an Intent object built by method chaining, with builder methods .goal, .ctxs, .tools, .input, .how, .rules, and .output for defining a task. -- evidence: [README.md#L377-L378](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L377-L378), [README.md#L306-L307](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L306-L307), [README.md#L302-L302](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L302-L302), [README.md#L316-L317](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L316-L317), [README.md#L328-L329](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L328-L329), [README.md#L344-L345](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L344-L345), [README.md#L368-L369](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L368-L369), [README.md#L389-L390](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L389-L390)
  - [observation/documented] Intents execute via compile() returning an Executor, or via run()/run_sync() convenience methods that compile and execute, returning an IntentResult with structured output and usage info. -- evidence: [README.md#L140-L143](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L140-L143), [README.md#L420-L427](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L420-L427), [README.md#L429-L432](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L429-L432)
- memory-state (1 claim(s)):
  - [observation/documented] Runtime is an embedded Python REPL with top-level await support that shares the host process space, so generated code can directly access host-provided input and tool objects. -- evidence: [README.md#L453-L453](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L453-L453), [README.md#L442-L442](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L442-L442)
- orchestration (2 claim(s)):
  - [observation/documented] The Executor iteratively runs LLM-generated Python until output matches the declared OutputModel or the preset maximum iteration count is reached. -- evidence: [README.md#L438-L438](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L438-L438), [README.md#L420-L427](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L420-L427)
  - [observation/documented] The runtime captures print output as observations and feeds exceptions back to the LLM so it can self-correct across iterations. -- evidence: [README.md#L449-L449](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L449-L449), [README.md#L451-L451](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L451-L451)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] IntentLang requires Python 3.10 or higher and is installable via pip or uv; examples also use pydantic and Playwright. -- evidence: [README.md#L112-L114](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L112-L114), [README.md#L106-L108](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L106-L108), [README.md#L180-L183](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L180-L183), [README.md#L238-L243](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L238-L243), [README.md#L102-L102](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L102-L102), [README.md#L5-L8](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L5-L8)
- limitations (1 claim(s)):
More evidence: [full detail](intentlang.detail.md)

Metadata and full claim list: [full detail](intentlang.detail.md)
Human notes ([notes](intentlang.notes.md), never overwritten by build)

[Back to map index](../../index.md)
