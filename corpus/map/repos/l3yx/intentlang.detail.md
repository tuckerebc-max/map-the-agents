# l3yx/intentlang -- full detail

[Back to orientation](intentlang.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/l3yx/intentlang/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/1ecf66ae56c28c19.json](../../../wiki/dossiers/l3yx/intentlang/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/1ecf66ae56c28c19.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] IntentLang replaces discrete function calling with continuous, stateful Python code generation and execution, treating tools as embedded objects rather than external APIs. -- evidence: [README.md#L58-L63](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L58-L63), [README.md#L87-L88](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L87-L88), [README.md#L75-L76](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L75-L76) (`clm_0f48ad752585c91c6a4524b363297a47d9901e34f400d6a8f2f898993aa1a4d0`)
- [observation/documented] Input data is passed by reference and not serialized into the LLM context; the model receives only names and descriptions and must generate code to access in-memory objects. -- evidence: [README.md#L81-L82](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L81-L82), [README.md#L349-L349](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L349-L349), [README.md#L153-L153](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L153-L153) (`clm_336698533c04cb8a1969d775b9c3be03af53644fbe4882aef159ba88eb19ec37`)
- [observation/documented] Intent elements (Goal, Contexts, Tools, Input, Strategy, Constraints, Output) are transformed into an XML-based Intent IR that guides progressive code generation. -- evidence: [README.md#L69-L70](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L69-L70) (`clm_967e305c0b597a66976316159a788428fee4e8011f90759a21f95f3157ee78b4`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The core API is an Intent object built by method chaining, with builder methods .goal, .ctxs, .tools, .input, .how, .rules, and .output for defining a task. -- evidence: [README.md#L377-L378](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L377-L378), [README.md#L306-L307](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L306-L307), [README.md#L302-L302](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L302-L302), [README.md#L316-L317](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L316-L317), [README.md#L328-L329](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L328-L329), [README.md#L344-L345](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L344-L345), [README.md#L368-L369](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L368-L369), [README.md#L389-L390](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L389-L390) (`clm_d7423604228fb39bfb58a6c98cc21fe4ea8fe5eb3c10f353c97ecfc0a34d3708`)
- [observation/documented] Intents execute via compile() returning an Executor, or via run()/run_sync() convenience methods that compile and execute, returning an IntentResult with structured output and usage info. -- evidence: [README.md#L140-L143](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L140-L143), [README.md#L420-L427](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L420-L427), [README.md#L429-L432](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L429-L432) (`clm_6c1aaf2da36d4586feca8dd80a906e46d52430cb6b9b755437313d03ae128bb9`)
- [observation/documented] compile() accepts engine_factory, max_iterations (default 30), cache (default False), and record (default True) parameters for finer control over execution. -- evidence: [README.md#L420-L427](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L420-L427) (`clm_320a1022e820daf3050e08fcf567375648470e69eb675ba157ba597d001a4ce7`)
- [observation/documented] LLM configuration is supplied through environment variables (OPENAI_BASE_URL, OPENAI_API_KEY, OPENAI_MODEL_NAME, OPENAI_EXTRA_BODY) set in a .env file, or via an LLMConfig object. -- evidence: [README.md#L123-L125](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L123-L125), [README.md#L246-L251](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L246-L251), [README.md#L118-L118](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L118-L118) (`clm_4cea85e719945404bfcd175ca632c9ff9ff086d254c3155cb069d513e04caf3a`)

## memory-state (1 claim(s))

- [observation/documented] Runtime is an embedded Python REPL with top-level await support that shares the host process space, so generated code can directly access host-provided input and tool objects. -- evidence: [README.md#L453-L453](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L453-L453), [README.md#L442-L442](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L442-L442) (`clm_c689bd90fe69218852fef1f8e47cbcf221d40f373bba409843b7295437355305`)

## orchestration (2 claim(s))

- [observation/documented] The Executor iteratively runs LLM-generated Python until output matches the declared OutputModel or the preset maximum iteration count is reached. -- evidence: [README.md#L438-L438](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L438-L438), [README.md#L420-L427](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L420-L427) (`clm_3d5cc94278cea046d8a662d202a7c3210b678c19914fda5cccfb0372df15f8e7`)
- [observation/documented] The runtime captures print output as observations and feeds exceptions back to the LLM so it can self-correct across iterations. -- evidence: [README.md#L449-L449](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L449-L449), [README.md#L451-L451](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L451-L451) (`clm_931fe75c4a5a849156014886c3d880475f188441fe085d1965ee442e06c20dbf`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] IntentLang requires Python 3.10 or higher and is installable via pip or uv; examples also use pydantic and Playwright. -- evidence: [README.md#L112-L114](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L112-L114), [README.md#L106-L108](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L106-L108), [README.md#L180-L183](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L180-L183), [README.md#L238-L243](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L238-L243), [README.md#L102-L102](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L102-L102), [README.md#L5-L8](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L5-L8) (`clm_f2b0499fee0cb7787ad050378055d09cd00b465948f92afab82ef9eaf0b126df`)

## limitations (1 claim(s))

- [observation/documented] The README warns that AI-generated code executes in the user's runtime and recommends running in isolated environments such as Docker containers, sandboxed Python environments, or virtual machines. -- evidence: [README.md#L165-L165](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L165-L165), [README.md#L159-L159](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L159-L159), [README.md#L163-L163](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L163-L163), [README.md#L167-L167](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L167-L167), [README.md#L161-L161](https://github.com/l3yx/intentlang/blob/6ce1cf88eac8d096a5d4d2d3eaaa1dd5ad8a0191/README.md#L161-L161) (`clm_6a37d86ecccb7eb9d59f45e6d2c536d8e00f84ccde8d2a40e58b0aa951ac6def`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

