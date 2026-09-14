# cuga-project/cuga-agent -- full detail

[Back to orientation](cuga-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cuga-project/cuga-agent/65bdf2fb376d9edaa8e929334dbc665d24b9a079/17a8859526cc0069.json](../../../wiki/dossiers/cuga-project/cuga-agent/65bdf2fb376d9edaa8e929334dbc665d24b9a079/17a8859526cc0069.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The provider side uses a supervisor YAML declaring one internal agent (digital_sales) that pulls tools from the registry; DYNACONF_A2A__ENABLED=true and a supervisor config path env var route inbound A2A requests through it. -- evidence: [docs/examples/a2a_two_cuga/README.md#L80-L84](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L80-L84) (`clm_d5c6ed66aec551da1a1b2b4ea80dba83a4be9f8321f7ef27a0f8f6f106cf2b57`)
- [observation/documented] A registry component serves the digital_sales OpenAPI tool catalog on http://localhost:8001, started with 'cuga start registry' in the example. -- evidence: [docs/examples/a2a_two_cuga/README.md#L73-L76](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L73-L76), [docs/examples/a2a_two_cuga/README.md#L32-L36](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L32-L36) (`clm_834c5449ca673302c888da5ed60bd4150578ef77b440b160d1f53f9d9c1f4d89`)

## design-choices (3 claim(s))

- [observation/documented] Configuration resolution priority is documented as environment variables highest, TOML configuration medium, and default values lowest. -- evidence: [README.md#L206-L208](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L206-L208) (`clm_1933f7b06f479954cf4e927e175d9d24c20a1e3559135d64be36c83ab5b71e38`)
- [observation/documented] The optional run receipt (run_receipt, default false) records tool data in timings-only mode: name, app, and duration only, never arguments, results, or errors, unless track_tool_calls=True is set. -- evidence: [README.md#L542-L544](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L542-L544), [README.md#L564-L567](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L564-L567) (`clm_6a3dcfe435be68dfe795142ab616268cb78e4c87b9c1a9dd96357fa7855fadcd`)
- [inference/documented] The final answer appears to be composed by a separately configurable LLM step that can be disabled in fast mode and shaped by a deterministic (str)->str function pointed at trusted code. -- evidence: [README.md#L573-L578](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L573-L578) (`clm_2dcca38688ee0625eab95ed44b9ed9193fc99e8598ea5ec0d570a4ca0f9a2aec`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are SKILL.md files with YAML frontmatter requiring name and description; CUGA lists short descriptions in the prompt and exposes a load_skill tool that returns the full markdown body on demand. -- evidence: [README.md#L420-L420](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L420-L420), [README.md#L403-L403](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L403-L403) (`clm_88be92335b0883c5d5ad2646d943896646fa529af360bcf0e3ccdd8102b48187`)
- [observation/documented] A single skills root is configured via [skills] root in settings.toml or DYNACONF_SKILLS__ROOT (default 'cuga'); CUGA scans one directory only, with no merge across paths. -- evidence: [README.md#L407-L407](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L407-L407) (`clm_806b4d140395e05f2309adbc0152cd9e79f7f65d9d09b1ba0499ee427f88786f`)

## interfaces (2 claim(s))

- [observation/documented] The provider exposes an A2A surface: a JSON-RPC endpoint at /a2a and an AgentCard at /.well-known/agent.json, per the example's documented URLs. -- evidence: [docs/examples/a2a_two_cuga/README.md#L47-L53](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L47-L53), [docs/examples/a2a_two_cuga/README.md#L73-L76](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L73-L76), [docs/examples/a2a_two_cuga/README.md#L38-L44](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L38-L44) (`clm_3143a24bf47827b11ebaef5c10415e984df06a6786fe9250b1aaf5ee07e3ef75`)
- [observation/documented] The Python SDK exposes CugaAgent(tools=[...]) with await agent.invoke(message), real-time agent.stream(), per-user thread_id session isolation, and access to the underlying LangGraph graph. -- evidence: [README.md#L473-L473](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L473-L473), [README.md#L521-L531](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L521-L531) (`clm_44ecd83571c6a22f7d89b48e6e9ff9ceda1d8216fe6dbd4da09e47a80acb2169`)

## memory-state (1 claim(s))

- [observation/documented] A built-in knowledge engine ingests PDFs, Office files, HTML, Markdown, and images via Docling, with documents scoped either agent-level (permanent, shared) or session-level (per-thread, isolated). -- evidence: [README.md#L76-L76](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L76-L76) (`clm_02367a87d2e4f4f8b05da1cbb3dabfdcf9736ddf92d5d645602e66a2af37c40a`)

## orchestration (1 claim(s))

- [observation/documented] A consumer supervisor config declares an external agent with a2a_protocol.transport=http; CUGA fetches the provider's AgentCard at startup, surfaces it as a tool, and delegates via delegate_task_via_a2a_sdk as JSON-RPC. -- evidence: [docs/examples/a2a_two_cuga/README.md#L86-L91](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L86-L91) (`clm_387132402162083678b17ab5dfc856bd77ecd06fd5b861bbc9f7539349432432`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README claims #1 rankings on AppWorld (07/25–02/26, 750 tasks across 457 APIs) and WebArena (02/25–09/25); these are self-reported leaderboard positions, not measured in this snapshot. -- evidence: [README.md#L59-L60](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L59-L60), [README.md#L57-L57](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L57-L57) (`clm_9e245e5659bbe63b23023cc50a9638cada6778118bc72cbe36ecb10809cff9c3`)

## dependencies (1 claim(s))

- [observation/documented] Documented LLM provider support includes OpenAI (plus LiteLLM via base URL override), IBM WatsonX, Azure OpenAI, Groq, RITS, OpenRouter, and watsonx Orchestrate, each with a dedicated settings TOML. -- evidence: [README.md#L196-L202](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L196-L202), [README.md#L382-L389](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L382-L389) (`clm_c034bbe750f478f3d047b29b135dce470854222ee16ea19a1d8e36add1daf7d6`)

## limitations (1 claim(s))

- [observation/documented] In the A2A example both CUGAs run with auth_required=false, and the auth-token forwarding integration test is marked xfail until v1. -- evidence: [docs/examples/a2a_two_cuga/README.md#L93-L95](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L93-L95) (`clm_ae66b098d51a65b6acaedc17838de1120965c3910ae0b55a9e365fd5335cf33b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_71ef0694311cf4d8ec9078d7281465cbc1baaea86209fec77b0a8c15cc0eb62d

