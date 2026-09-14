# jcz2020/par -- full detail

[Back to orientation](par.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jcz2020/par/4b593db4465d7f7c5312269774b17d4bf15b333a/8335b6fb3b4903ae.json](../../../wiki/dossiers/jcz2020/par/4b593db4465d7f7c5312269774b17d4bf15b333a/8335b6fb3b4903ae.json)

## specifications (1 claim(s))

- [observation/documented] PAR is described as a modular, type-safe agent runtime written in OCaml, usable from Python or OCaml, positioned as a LangChain/LangGraph-style framework. -- evidence: [README.md#L5-L5](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L5-L5), [README.md#L20-L20](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L20-L20) (`clm_17efa93249569ba14f7061a5f1ff973c4d021c391ed930da6aa077a7e5358c4d`)

## components (1 claim(s))

- [observation/documented] The codebase is layered into core (types, runtime, ReAct engine, workflow engine, cancellation, persistence writer), providers (OpenAI, Anthropic, mock), tools, persistence, event bus, and middleware modules. -- evidence: [docs/explanation/architecture.md#L15-L27](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L15-L27), [docs/explanation/architecture.md#L33-L69](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L33-L69) (`clm_38b3b614dd6b2158cdac338005f9ced0ecc5692948609452d83720acd17ceea6`)

## design-choices (1 claim(s))

- [observation/documented] The bash tool uses a command ADT with no raw-shell constructor, so shell injection is claimed to be unrepresentable at the type level; duplicate tool names return an error rather than overwriting. -- evidence: [docs/explanation/architecture.md#L107-L110](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L107-L110), [docs/explanation/architecture.md#L112-L112](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L112-L112) (`clm_287d7a6bdf205125f9a6aebb9a620f644db55db6c308a7ac2a3f10a5cb69631a`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions follow CONTRIBUTING.md for dev setup, PR conventions, and code style, and docs follow the Diataxis tutorial/how-to/reference/explanation structure. -- evidence: [README.md#L165-L165](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L165-L165) (`clm_52ca1815796eb74a0131afeb6334200c72f4887b33bac4dae1b52dff9ac4c638`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are markdown files under ~/.par/skills/<id>/skill.md with YAML frontmatter (schema_version, id, trigger, tool_filter, system_prompt_override), auto-discovered and activated by Auto, Manual, or Keyword triggers. -- evidence: [docs/sdk/skills.md#L83-L92](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L83-L92), [docs/sdk/skills.md#L6-L6](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L6-L6), [docs/sdk/skills.md#L33-L44](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L33-L44), [docs/sdk/skills.md#L102-L102](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L102-L102), [docs/sdk/skills.md#L72-L72](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L72-L72) (`clm_12c5c4229190e5f94a6a6c4c22a3841cfc4f3c8ace3ee99e1a065d0199f9e961`)
- [observation/documented] Skill markdown bodies are lazy-loaded only on activation, and total skill description tokens are capped at 2048 by default via skill_token_budget, dropping lowest-priority descriptions with a warning. -- evidence: [docs/sdk/skills.md#L96-L96](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L96-L96), [docs/sdk/skills.md#L158-L158](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/skills.md#L158-L158) (`clm_4594211eef566e525b89c7fe4560ec6c21a9052567f49a20c1ef8211caec6d1b`)

## interfaces (1 claim(s))

- [observation/documented] The runtime exposes two API surfaces: an OCaml SDK (installed via opam pin) and Python bindings installable with pip as par-runtime. -- evidence: [README.md#L63-L66](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L63-L66), [README.md#L24-L25](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L24-L25), [README.md#L68-L71](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L68-L71) (`clm_4f835b48204545903ae290e8d4f5018038f42faac4ab64a3f60992ff22b6f2c8`)

## memory-state (1 claim(s))

- [observation/documented] A Memory_service provides cross-session memory with a default SQLite+FTS5 backend, search modes (keyword, vector, hybrid with RRF, auto), and get_fn/upsert_fn for stable-ID plan-then-execute updates. -- evidence: [docs/sdk/memory.md#L123-L124](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L123-L124), [docs/sdk/memory.md#L180-L180](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L180-L180), [docs/sdk/memory.md#L7-L7](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L7-L7), [docs/sdk/memory.md#L16-L20](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L16-L20), [docs/sdk/memory.md#L214-L214](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L214-L214) (`clm_4e6d0dcfda74efaaaa32a88ce824bed5daef8bfe4a891d2b072463f372f747a9`)

## orchestration (1 claim(s))

- [observation/documented] PAR runs its stack on Eio structured concurrency: each Runtime has an Eio switch as cancellation root, and Runtime.close cancels all fibers including tool handlers and LLM streams. -- evidence: [docs/explanation/architecture.md#L118-L122](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L118-L122), [docs/explanation/architecture.md#L116-L116](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/explanation/architecture.md#L116-L116) (`clm_fc38c0b95d1f3b738f6983995e6d5826619227dd4b46394b29a6442b274dc80b`)

## tools-permissions (1 claim(s))

- [observation/documented] When memory is configured, three builtin tools (recall_memory, remember_memory, search_history) are auto-registered and scoped per session via invoke_context.session_id. -- evidence: [docs/sdk/memory.md#L280-L280](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L280-L280), [docs/sdk/memory.md#L288-L288](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L288-L288), [docs/sdk/memory.md#L282-L286](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L282-L286) (`clm_aaeb50c938b30d1eb43a048573f133afc3ef11d77e5125f031c6535936f6de5e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] PAR builds on OCaml 5.4 effects, the Eio concurrency library, and dune, and is MIT-licensed; Python bindings are published on PyPI. -- evidence: [README.md#L9-L12](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L9-L12), [README.md#L173-L173](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L173-L173), [README.md#L169-L169](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/README.md#L169-L169) (`clm_3d9ff12e2445ecbd994c1603fa82082ec7f8dd89782e87f5f7adb0b3b85b19ba`)

## limitations (1 claim(s))

- [observation/documented] Each Runtime has its own memory service; cross-agent knowledge sharing requires a shared SQLite file or a future remote backend, per the memory docs. -- evidence: [docs/sdk/memory.md#L316-L316](https://github.com/jcz2020/par/blob/4b593db4465d7f7c5312269774b17d4bf15b333a/docs/sdk/memory.md#L316-L316) (`clm_c8099bb7d88629e43b01524e418d0c8503408ca30ffca88a56a4aa6ea049e035`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

