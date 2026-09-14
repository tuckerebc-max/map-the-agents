# context-labs/halo -- full detail

[Back to orientation](halo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/context-labs/halo/b7f8509745d67b499b4e80efe20ea37c03426a74/9f2700ac05de7f87.json](../../../wiki/dossiers/context-labs/halo/b7f8509745d67b499b4e80efe20ea37c03426a74/9f2700ac05de7f87.json)

## specifications (2 claim(s))

- [observation/documented] HALO is described as a methodology for building recursively self-improving agent harnesses using RLMs, with the repo containing a desktop app, methodology docs, a Python engine package, and demos. -- evidence: [README.md#L125-L125](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L125-L125), [README.md#L127-L131](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L127-L131) (`clm_6921439416cf368d91e329598a3d02a70295ef10e309770768eebd65384d5f7a`)
- [observation/documented] The HALO loop: collect OpenTelemetry-compatible traces from an agent harness, feed them to the HALO-RLM engine, which decomposes traces into common failure modes and produces a report that a coding agent turns into harness changes, then the cycle repeats. -- evidence: [README.md#L138-L142](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L138-L142) (`clm_7df3a5dbdf9586bcc6b93014c53bdce9205c527e0f92a5f6efce6638c00bbef7`)

## components (1 claim(s))

- [observation/documented] The project ships a HALO Desktop App for local use, a Python package (halo-engine on PyPI) implementing the core HALO-RLM engine, and a demo project showing HALO loops with the OpenAI Agents SDK. -- evidence: [README.md#L156-L156](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L156-L156), [README.md#L158-L159](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L158-L159), [README.md#L127-L131](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L127-L131) (`clm_0c59b8f0b1df3804d825264dd20858df9ce3e9d132caea80644c1baf5ed829c4`)

## design-choices (1 claim(s))

- [observation/documented] The authors argue general harnesses like Claude Code overfit to errors in single traces when analyzing long traces, motivating a specialized RLM for systemic trace analysis. -- evidence: [README.md#L148-L148](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L148-L148) (`clm_d539bc03b6fc4b52f2c80abc382ed3c484755af10320f5dce1a14a17e618e5f6`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: local development uses uv and go-task; task env:setup installs uv, syncs the venv from uv.lock, and configures git hooks, with tasks for pre-commit checks, unit tests, and integration tests. -- evidence: [README.md#L298-L303](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L298-L303), [README.md#L292-L292](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L292-L292), [README.md#L282-L282](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L282-L282) (`clm_0b29ad6fd633ae791ef5d8d0edf63959f0b5278dcf6cf56dcb2b34701f66da7b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI takes a required JSONL trace path and prompt, with flags like --model (default gpt-5.4-mini) and --synthesis-model for trace summarization, and supports --base-url and custom headers as shown in an OpenRouter example. -- evidence: [README.md#L185-L204](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L185-L204), [README.md#L176-L177](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L176-L177), [README.md#L208-L213](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L208-L213) (`clm_13a6fe5ae0fec041c39ce21da4e5b3bb1b56ca137bb945c283ae26efdab0c8b0`)
- [observation/documented] HALO uses OPENAI_API_KEY and OPENAI_BASE_URL; if the base URL is unset it defaults to https://api.openai.com/v1, and CLI settings mirror the SDK's ModelConfig and ModelProviderConfig. -- evidence: [README.md#L179-L181](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L179-L181) (`clm_05d8215d865e467a426d0800ac395d2ee6a65ddabc98a0c34fe34a4945c88f1f`)
- [observation/documented] The engine exposes multiple entry points from engine.main (e.g. stream_engine_async, run_engine_async, stream_engine_output) yielding AgentOutputItem and AgentTextDelta types, trading off streaming observability versus simplicity. -- evidence: [README.md#L238-L242](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L238-L242), [README.md#L244-L251](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L244-L251) (`clm_938980f911fb84af243f7cd646c194a223807ef28a246a2acad88b54d40351c2`)
- [observation/documented] The integration writes one JSONL span per line with OTLP identity fields, resource/scope blocks, and inference.* projection attributes (project_id, observation_kind, token counts, tool/agent attributes) that the Engine indexes on, filtering on inference.project_id. -- evidence: [docs/integrations/openai-agents-sdk.md#L141-L142](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/docs/integrations/openai-agents-sdk.md#L141-L142), [docs/integrations/openai-agents-sdk.md#L35-L37](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/docs/integrations/openai-agents-sdk.md#L35-L37), [docs/integrations/openai-agents-sdk.md#L85-L85](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/docs/integrations/openai-agents-sdk.md#L85-L85), [docs/integrations/openai-agents-sdk.md#L89-L102](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/docs/integrations/openai-agents-sdk.md#L89-L102) (`clm_198a146ae41ab9d1b32ff045c8bf5804e594ccad82fef1ca108b482751b10c3e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] HALO's own telemetry is off by default; passing --telemetry emits OpenInference-shaped traces, uploaded over OTLP to inference.net when INFERENCE_API_KEY is set, otherwise written to a local JSONL file. -- evidence: [README.md#L217-L217](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L217-L217), [README.md#L223-L223](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L223-L223) (`clm_1f2479b10825892ed072c522fdd035ab32d873b95f6858e675277628f62e7570`)

## evaluation (1 claim(s))

- [observation/documented] On AppWorld, harness-only optimization reportedly raised SGC: Gemini 3 Flash dev 36.8%→52.6% and test_normal 37.5%→48.2%; Sonnet 4.6 dev 73.7%→89.5% and test_normal 62.5%→73.2%, iterating on dev and checking test_normal for overfitting. -- evidence: [README.md#L267-L267](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L267-L267), [README.md#L271-L278](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L271-L278) (`clm_71b5236595fb74ee0a762d5c5f921f39791c7ad91c404752097a678aeac7edf3`)

## dependencies (1 claim(s))

- [observation/documented] The OpenAI Agents SDK integration's tracing.py is a self-contained ~450-line module using only stdlib plus openai-agents, with no OpenTelemetry packages, exporter, collector, or instrumentor required. -- evidence: [docs/integrations/openai-agents-sdk.md#L33-L33](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/docs/integrations/openai-agents-sdk.md#L33-L33), [docs/integrations/openai-agents-sdk.md#L29-L29](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/docs/integrations/openai-agents-sdk.md#L29-L29) (`clm_fd62ac594fe5a1a08da02d6eb1ad53b140e96b4eef647e2b80f4154b61b0bbd8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

