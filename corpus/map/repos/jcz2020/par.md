# jcz2020/par

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4b593db4465d @ 8335b6fb3b4903ae

## Summary (orientation draft, not independently verified)

Selected evidence records: PAR is described as a modular, type-safe agent runtime written in OCaml, usable from Python or OCaml, positioned as a LangChain/LangGraph-style framework. The runtime exposes two API surfaces: an OCaml SDK (installed via opam pin) and Python bindings installable with pip as par-runtime.

## Source coverage

Source coverage (partial): 6 of 85 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] PAR is described as a modular, type-safe agent runtime written in OCaml, usable from Python or OCaml, positioned as a LangChain/LangGraph-style framework. -- evidence: [README.md#L5-L5](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L5-L5), [README.md#L20-L20](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L20-L20)
- components (1 claim(s)):
  - [observation/documented] The codebase is layered into core (types, runtime, ReAct engine, workflow engine, cancellation, persistence writer), providers (OpenAI, Anthropic, mock), tools, persistence, event bus, and middleware modules. -- evidence: [docs/explanation/architecture.md#L15-L27](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L15-L27), [docs/explanation/architecture.md#L33-L69](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L33-L69)
- design-choices (1 claim(s)):
  - [observation/documented] The bash tool uses a command ADT with no raw-shell constructor, so shell injection is claimed to be unrepresentable at the type level; duplicate tool names return an error rather than overwriting. -- evidence: [docs/explanation/architecture.md#L107-L110](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L107-L110), [docs/explanation/architecture.md#L112-L112](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L112-L112)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions follow CONTRIBUTING.md for dev setup, PR conventions, and code style, and docs follow the Diataxis tutorial/how-to/reference/explanation structure. -- evidence: [README.md#L165-L165](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L165-L165)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are markdown files under ~/.par/skills/<id>/skill.md with YAML frontmatter (schema_version, id, trigger, tool_filter, system_prompt_override), auto-discovered and activated by Auto, Manual, or Keyword triggers. -- evidence: [docs/sdk/skills.md#L83-L92](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L83-L92), [docs/sdk/skills.md#L6-L6](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L6-L6), [docs/sdk/skills.md#L33-L44](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L33-L44), [docs/sdk/skills.md#L102-L102](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L102-L102), [docs/sdk/skills.md#L72-L72](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L72-L72)
  - [observation/documented] Skill markdown bodies are lazy-loaded only on activation, and total skill description tokens are capped at 2048 by default via skill_token_budget, dropping lowest-priority descriptions with a warning. -- evidence: [docs/sdk/skills.md#L96-L96](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L96-L96), [docs/sdk/skills.md#L158-L158](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L158-L158)
- interfaces (1 claim(s)):
  - [observation/documented] The runtime exposes two API surfaces: an OCaml SDK (installed via opam pin) and Python bindings installable with pip as par-runtime. -- evidence: [README.md#L63-L66](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L63-L66), [README.md#L24-L25](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L24-L25), [README.md#L68-L71](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L68-L71)
- memory-state (1 claim(s)):
  - [observation/documented] A Memory_service provides cross-session memory with a default SQLite+FTS5 backend, search modes (keyword, vector, hybrid with RRF, auto), and get_fn/upsert_fn for stable-ID plan-then-execute updates. -- evidence: [docs/sdk/memory.md#L123-L124](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L123-L124), [docs/sdk/memory.md#L180-L180](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L180-L180), [docs/sdk/memory.md#L7-L7](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L7-L7), [docs/sdk/memory.md#L16-L20](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L16-L20), [docs/sdk/memory.md#L214-L214](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L214-L214)
- orchestration (1 claim(s)):
  - [observation/documented] PAR runs its stack on Eio structured concurrency: each Runtime has an Eio switch as cancellation root, and Runtime.close cancels all fibers including tool handlers and LLM streams. -- evidence: [docs/explanation/architecture.md#L118-L122](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L118-L122), [docs/explanation/architecture.md#L116-L116](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L116-L116)
- tools-permissions (1 claim(s)):
  - [observation/documented] When memory is configured, three builtin tools (recall_memory, remember_memory, search_history) are auto-registered and scoped per session via invoke_context.session_id. -- evidence: [docs/sdk/memory.md#L280-L280](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L280-L280), [docs/sdk/memory.md#L288-L288](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L288-L288), [docs/sdk/memory.md#L282-L286](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L282-L286)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](par.detail.md)

Metadata and full claim list: [full detail](par.detail.md)
Human notes ([notes](par.notes.md), never overwritten by build)

[Back to map index](../../index.md)
