# nam271212/strategic-advisor-orchestrator -- full detail

[Back to orientation](strategic-advisor-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nam271212/strategic-advisor-orchestrator/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/4962fdac2b393b1c.json](../../../wiki/dossiers/nam271212/strategic-advisor-orchestrator/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/4962fdac2b393b1c.json)

## specifications (1 claim(s))

- [observation/documented] Synaptic Compass is described as an advisory orchestration framework that deploys a secondary, higher-order reasoning model to guide AI coding agents on architecture, security, performance, and debugging. -- evidence: [README.md#L5-L5](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L5-L5) (`clm_18717ad39db8fd8ae98ae08317b7513eb2c705203d59af5ec9935a38f4171686`)

## components (1 claim(s))

- [observation/documented] Documented components include an orchestrator module, context aggregator, configurable reasoning engine, feedback interface, and a memory buffer retaining pattern awareness across sessions. -- evidence: [README.md#L77-L81](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L77-L81) (`clm_3469e33fb11471d3e0dea4d24e2d3b09e7b2c47a3614b426314ed69c1224c5a1`)

## design-choices (1 claim(s))

- [observation/documented] The product is documented as a stateless, event-driven orchestrator positioned between the user's prompt and the coding agent's execution layer. -- evidence: [README.md#L56-L56](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L56-L56) (`clm_e59158bf9fb3e5e391fd44a03b755b68b48ea1049baea3f5a3bf3951ea3d9992`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcomed for new validation modules, agent adapters, and orchestration-loop optimization, with CONTRIBUTING.md referenced for the code of conduct and pull request process. -- evidence: [README.md#L218-L218](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L218-L218), [README.md#L226-L226](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L226-L226), [README.md#L221-L224](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L221-L224) (`clm_db6abf3e80398365ddc11ff1b5e404c342a3b6c1436c275c74313203f5f27896`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Integration is documented for agents exposing streaming output hooks, session context injection, or external tool calling (MCP, plugins, API endpoints), with Claude Code, Cursor, Gemini CLI, and Cline listed as stable integrations. -- evidence: [README.md#L141-L144](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L141-L144), [README.md#L146-L153](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L146-L153) (`clm_537824c46a6e73bdf161248591ab26d17feb765a4014c76d369b64d5b588f7cd`)
- [observation/documented] Configuration uses a compass.yaml or compass.json file defining advisor model, feedback mode (blocking, non_blocking, advisory_only), validation layers, security scan depth, and output format, overridable per session via environment variables or flags. -- evidence: [README.md#L192-L194](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L192-L194), [README.md#L186-L190](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L186-L190), [README.md#L196-L199](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L196-L199), [README.md#L180-L184](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L180-L184), [README.md#L178-L178](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L178-L178), [README.md#L201-L201](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L201-L201) (`clm_cc8ae33c43d0a792cecbd8b21a4b82b031c6dffaedbb02f38e33030c27d271f0`)

## memory-state (1 claim(s))

- [observation/documented] Advisor contexts are documented as ephemeral and discarded after each orchestration cycle unless the memory buffer is explicitly preserved. -- evidence: [README.md#L207-L210](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L207-L210) (`clm_a999e89005ff357cc6a3d619f4153b93c5ef0fabc997fd4c6a6fb3bd8cd45123`)

## orchestration (1 claim(s))

- [observation/documented] The documented workflow captures prompt, agent reasoning, and project context, dispatches it to the advisor for architecture, security, performance, and edge-case analysis, then injects structured feedback the agent may accept, override, or escalate. -- evidence: [README.md#L122-L126](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L122-L126), [README.md#L119-L119](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L119-L119), [README.md#L129-L132](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L129-L132) (`clm_6cb883017dd5c08eaf99214efa1d2c3c02a787d446cb0c0a133d819a9e22860a`)

## tools-permissions (1 claim(s))

- [observation/documented] The security posture is documented as minimum privilege: no data leaves the environment unless a cloud advisor endpoint is configured, local models are supported, and the security layer never transmits credentials even in diagnostic logs. -- evidence: [README.md#L212-L212](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L212-L212), [README.md#L207-L210](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L207-L210) (`clm_cc2eb3133e6418fe59c5523d3484c55d641db004908753583da6645c03acd130`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The advisor model appears configurable across providers (Claude, GPT, Gemini, or local LLMs such as Llama 3 and Mistral), suggesting no hard dependency on a single model vendor. -- evidence: [README.md#L180-L184](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L180-L184), [README.md#L207-L210](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L207-L210) (`clm_d7b8d4dabb921312004629f99342020564404b723f2fbf0d869e76ad26b40111`)

## limitations (1 claim(s))

- [observation/documented] The README's disclaimer states the tool is advisory, not a replacement for human judgment, does not guarantee bug-free or secure software, and its advisor feedback may be inaccurate or incomplete. -- evidence: [README.md#L238-L238](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L238-L238), [README.md#L240-L240](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L240-L240) (`clm_b10d9d7192a4f23e89bc6a372286012de54afa6ebead2308d3c383f6b5e55940`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

