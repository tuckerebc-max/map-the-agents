# 2389-research/tracker -- full detail

[Back to orientation](tracker.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/tracker/de156192ce90ec59e00039e0f37f174754a3aeb5/573327dee8852ffb.json](../../../wiki/dossiers/2389-research/tracker/de156192ce90ec59e00039e0f37f174754a3aeb5/573327dee8852ffb.json)

## specifications (2 claim(s))

- [observation/documented] Pipelines are defined in .dip files using the Dippin DSL, with workflow headers declaring goal, start, exit, defaults (model/provider), and edges between nodes. -- evidence: [README.md#L136-L140](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L136-L140), [README.md#L116-L118](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L116-L118), [README.md#L110-L114](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L110-L114), [README.md#L108-L108](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L108-L108) (`clm_f34931e1a6a9ce2d1a87a7a94feb49fc536c11d46cab9276ef2c87e5699da537`)
- [observation/documented] Workflows can declare environmental requirements via a requires: header line; as of v0.29.0 only git is checked, and unrecognized entries warn and continue. -- evidence: [README.md#L144-L144](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L144-L144), [README.md#L154-L154](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L154-L154) (`clm_0c4d60a1490d8accd9e220c00e9b0f2b38c5b4addaaa71031528cc263ade3e99`)

## components (2 claim(s))

- [observation/documented] Tracker is a three-layer stack: an LLM client with provider adapters, an agent session with turn loop and context compaction, and a pipeline engine with graph execution, checkpoints, and TUI. -- evidence: [README.md#L355-L355](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L355-L355), [README.md#L357-L376](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L357-L376) (`clm_bafb075e18422d7b049382327a8b22195e3ad3626b9181d9175553aab650c188`)
- [observation/documented] The engine supports eight node types: agent, human gate, tool, parallel, fan_in, subgraph, manager_loop, and conditional. -- evidence: [README.md#L158-L167](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L158-L167) (`clm_1b44954215456db181435ebd6f1d5594c5e9dee32ebc8974d1c33de4c2829bb8`)

## design-choices (3 claim(s))

- [observation/documented] The core engine is UI-agnostic: TUI, Slack bot, and terminal REPL are peers on one library boundary sharing a transport-neutral transport/chatops core. -- evidence: [README.md#L378-L384](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L378-L384), [README.md#L472-L476](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L472-L476) (`clm_e8dd87589465e420d15b1242aea80672aa91435e6564d5169cce667669d5965c`)
- [observation/documented] Variable expansion is single-pass so resolved values are never re-scanned, preventing recursive expansion; unknown --param keys hard-fail at startup. -- evidence: [README.md#L192-L192](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L192-L192), [README.md#L186-L188](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L186-L188), [README.md#L190-L190](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L190-L190) (`clm_875620f8d8be213726cb6b23a92683f08dd62fbfe6931f5ebea93653520bb1d4`)
- [observation/documented] Secret inputs are staged to a 0600 file and ${inputs.<name>} resolves only to the path, so secret values never enter prompts, the provider wire, traces, or checkpoints. -- evidence: [README.md#L386-L397](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L386-L397) (`clm_0033f403061d1fcd65a53659f6a29b0db8154a50c7f1e67c4b944c44290eb9d1`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Human gates support five modes: choice, freeform, hybrid, yes/no, and interview, with interview answers stored as JSON plus a markdown summary. -- evidence: [README.md#L246-L250](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L246-L250), [README.md#L282-L282](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L282-L282), [README.md#L244-L244](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L244-L244) (`clm_c76187eedf2a776c182839941f859ef5e0a4e2ecbb0e276d65e141e1f0c8dd79`)
- [observation/documented] Headless operation is supported via --webhook-url: human gates are POSTed as JSON and the pipeline resumes on callback, with flags for timeout, timeout action, and auth header. -- evidence: [README.md#L672-L678](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L672-L678), [README.md#L655-L658](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L655-L658), [README.md#L662-L668](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L662-L668), [README.md#L649-L649](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L649-L649) (`clm_108f48d0af773248d06641ebeb5ba4e7569d86c768659edd76ee1edb39f410c3`)

## memory-state (2 claim(s))

- [observation/documented] Each agent node runs a fresh LLM session; data flows between nodes via context keys (ctx.*, params.*, graph.*), not conversation history, with per-node scoping available. -- evidence: [README.md#L173-L175](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L173-L175), [README.md#L171-L171](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L171-L171), [README.md#L194-L194](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L194-L194) (`clm_4452831a294aa151c7597473296fd2bfaec3d5fc41f4180a9e04161fdecbf0d3`)
- [observation/documented] Agent, tool, and interview nodes can declare writes:/reads: context keys; missing declared writes hard-fail the node, and reads: pins fidelity of upstream keys. -- evidence: [README.md#L215-L215](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L215-L215), [README.md#L227-L227](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L227-L227) (`clm_5f8e67187f605287fceff8497556b07ba7cc355861fe2a5f7457e60b68fec3a0`)

## orchestration (1 claim(s))

- [observation/documented] Both build workflows run a SpecLint preflight (dangling refs, contradictory constants, contract mismatches) that fails closed before decomposition. -- evidence: [README.md#L63-L63](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L63-L63) (`clm_ec3407f15420378be2f4267fbe90627330ac76ace1963f7a9270b87e0fe055db`)

## tools-permissions (1 claim(s))

- [observation/documented] The working_dir attribute for per-node working directories is validated against path traversal and shell metacharacters. -- evidence: [README.md#L240-L240](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L240-L240), [README.md#L231-L231](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L231-L231) (`clm_c487bff315a8566467bfc106adaadce4e00114698e3688cec0f7c2ce292bd714`)

## evaluation (1 claim(s))

- [observation/documented] The superspec workflow includes per-phase mechanical quality gates (build, test, lint, coverage, complexity) and a final TraceabilityAudit gate verifying spec requirements map to implementation and test coverage. -- evidence: [README.md#L65-L68](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L65-L68) (`clm_9ef92e1cb7f5544b14d523f0ec508e729692d4eb228be6885c7a2220c74047b6`)

## dependencies (2 claim(s))

- [observation/documented] Tracker supports four LLM providers: anthropic, openai, gemini, and openai-compat, configured via tracker setup or environment variables stored in ~/.config/2389/tracker/.env. -- evidence: [README.md#L294-L294](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L294-L294), [README.md#L300-L300](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L300-L300), [README.md#L302-L306](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L302-L306), [README.md#L290-L290](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L290-L290) (`clm_501f196bd2976c0d357d8f4f5bc916c6a43edf2554e6c7391f1847534e5482da`)
- [observation/documented] All providers can be routed through Cloudflare AI Gateway via TRACKER_GATEWAY_URL or --gateway-url, with per-provider base-URL overrides taking precedence over the gateway. -- evidence: [README.md#L321-L321](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L321-L321), [README.md#L314-L314](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L314-L314), [README.md#L346-L346](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L346-L346), [README.md#L333-L335](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L333-L335) (`clm_8069d8372df06538b2c1c7b3fde1e1f59c88207188e1dbe7bd42cfdb8de2f070`)

## limitations (1 claim(s))

- [observation/documented] Git artifact commits per terminal node outcome are enabled only via the library's WithGitArtifacts(true) option; the README states there is no CLI flag for this today. -- evidence: [README.md#L513-L513](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L513-L513) (`clm_2ace9cc7463af402aed1ac779f0b4264c4d94066f742ef78cf6ca7acc379b71a`)

## relevance (1 claim(s))

- [observation/documented] Tracker targets teams running multi-agent LLM build/review pipelines, offering human gates, budget ceilings, audit trails, and front-ends for terminal, TUI, and Slack. -- evidence: [README.md#L453-L457](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L453-L457), [README.md#L490-L490](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L490-L490), [README.md#L425-L431](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L425-L431), [README.md#L3-L3](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L3-L3) (`clm_1afe1f84d910bdc2750434ec146a76b632d9c4b508a0d8a8b6e4c2ccf6ac7a8a`)

