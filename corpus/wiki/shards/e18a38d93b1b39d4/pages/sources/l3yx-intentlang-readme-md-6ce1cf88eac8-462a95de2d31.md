---
access: public
aliases: []
claim_ids:
- clm_0f48ad752585c91c6a4524b363297a47d9901e34f400d6a8f2f898993aa1a4d0
- clm_320a1022e820daf3050e08fcf567375648470e69eb675ba157ba597d001a4ce7
- clm_336698533c04cb8a1969d775b9c3be03af53644fbe4882aef159ba88eb19ec37
- clm_3d5cc94278cea046d8a662d202a7c3210b678c19914fda5cccfb0372df15f8e7
- clm_4cea85e719945404bfcd175ca632c9ff9ff086d254c3155cb069d513e04caf3a
- clm_6a37d86ecccb7eb9d59f45e6d2c536d8e00f84ccde8d2a40e58b0aa951ac6def
- clm_6c1aaf2da36d4586feca8dd80a906e46d52430cb6b9b755437313d03ae128bb9
- clm_931fe75c4a5a849156014886c3d880475f188441fe085d1965ee442e06c20dbf
- clm_967e305c0b597a66976316159a788428fee4e8011f90759a21f95f3157ee78b4
- clm_c689bd90fe69218852fef1f8e47cbcf221d40f373bba409843b7295437355305
- clm_d7423604228fb39bfb58a6c98cc21fe4ea8fe5eb3c10f353c97ecfc0a34d3708
- clm_f2b0499fee0cb7787ad050378055d09cd00b465948f92afab82ef9eaf0b126df
maturity: draft
page_id: pg_c6995666473452c78a1f462a95de2d31
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d251e6483af75a968d1362f123466bc0
title: l3yx/intentlang/README.md @ 6ce1cf88eac8
updated_at: '2026-09-14T02:11:21Z'
---

# l3yx/intentlang/README.md @ 6ce1cf88eac8

<!-- rcw:begin owner=source:src_d251e6483af75a968d1362f123466bc0 block=evidence -->
- IntentLang replaces discrete function calling with continuous, stateful Python code generation and execution, treating tools as embedded objects rather than external APIs. [@claim:clm_0f48ad752585c91c6a4524b363297a47d9901e34f400d6a8f2f898993aa1a4d0]
- compile() accepts engine_factory, max_iterations (default 30), cache (default False), and record (default True) parameters for finer control over execution. [@claim:clm_320a1022e820daf3050e08fcf567375648470e69eb675ba157ba597d001a4ce7]
- Input data is passed by reference and not serialized into the LLM context; the model receives only names and descriptions and must generate code to access in-memory objects. [@claim:clm_336698533c04cb8a1969d775b9c3be03af53644fbe4882aef159ba88eb19ec37]
- The Executor iteratively runs LLM-generated Python until output matches the declared OutputModel or the preset maximum iteration count is reached. [@claim:clm_3d5cc94278cea046d8a662d202a7c3210b678c19914fda5cccfb0372df15f8e7]
- LLM configuration is supplied through environment variables (OPENAI_BASE_URL, OPENAI_API_KEY, OPENAI_MODEL_NAME, OPENAI_EXTRA_BODY) set in a .env file, or via an LLMConfig object. [@claim:clm_4cea85e719945404bfcd175ca632c9ff9ff086d254c3155cb069d513e04caf3a]
- The README warns that AI-generated code executes in the user's runtime and recommends running in isolated environments such as Docker containers, sandboxed Python environments, or virtual machines. [@claim:clm_6a37d86ecccb7eb9d59f45e6d2c536d8e00f84ccde8d2a40e58b0aa951ac6def]
- Intents execute via compile() returning an Executor, or via run()/run_sync() convenience methods that compile and execute, returning an IntentResult with structured output and usage info. [@claim:clm_6c1aaf2da36d4586feca8dd80a906e46d52430cb6b9b755437313d03ae128bb9]
- The runtime captures print output as observations and feeds exceptions back to the LLM so it can self-correct across iterations. [@claim:clm_931fe75c4a5a849156014886c3d880475f188441fe085d1965ee442e06c20dbf]
- Intent elements (Goal, Contexts, Tools, Input, Strategy, Constraints, Output) are transformed into an XML-based Intent IR that guides progressive code generation. [@claim:clm_967e305c0b597a66976316159a788428fee4e8011f90759a21f95f3157ee78b4]
- Runtime is an embedded Python REPL with top-level await support that shares the host process space, so generated code can directly access host-provided input and tool objects. [@claim:clm_c689bd90fe69218852fef1f8e47cbcf221d40f373bba409843b7295437355305]
- The core API is an Intent object built by method chaining, with builder methods .goal, .ctxs, .tools, .input, .how, .rules, and .output for defining a task. [@claim:clm_d7423604228fb39bfb58a6c98cc21fe4ea8fe5eb3c10f353c97ecfc0a34d3708]
- IntentLang requires Python 3.10 or higher and is installable via pip or uv; examples also use pydantic and Playwright. [@claim:clm_f2b0499fee0cb7787ad050378055d09cd00b465948f92afab82ef9eaf0b126df]
<!-- rcw:end owner=source:src_d251e6483af75a968d1362f123466bc0 block=evidence -->

## Researcher notes

