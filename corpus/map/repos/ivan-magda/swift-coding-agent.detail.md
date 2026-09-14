# ivan-magda/swift-coding-agent -- full detail

[Back to orientation](swift-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ivan-magda/swift-coding-agent/88ed290dff95789929a823603cc54cf7cc530da2/025e7d256d46b7f0.json](../../../wiki/dossiers/ivan-magda/swift-coding-agent/88ed290dff95789929a823603cc54cf7cc530da2/025e7d256d46b7f0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] It is a two-target Swift Package Manager project: a Core library holding the API client, shell executor, agent loop, and tools, plus a thin CLI entry point. -- evidence: [README.md#L101-L101](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L101-L101), [README.md#L97-L97](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L97-L97), [README.md#L99-L99](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L99-L99) (`clm_b345c5f2e5bf97a35f9c545bfff0620a6c7a5adeeecd3abe1a672b519bb6b281`)

## design-choices (1 claim(s))

- [observation/documented] The project's thesis is that coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers, deliberately rebuilding Claude Code's restrained design in Swift. -- evidence: [README.md#L3-L3](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L3-L3), [README.md#L17-L17](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L17-L17), [README.md#L21-L21](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L21-L21) (`clm_b7841256fffa30db1bd6bcb091df7255cd1d760c01aeba69c1c2f0ca2f83c4f7`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the stage-0 guide walks contributors through a two-target SPM layout with a Swift Testing test target (CoreTests importing Core), .env-based ANTHROPIC_API_KEY configuration, and swift build/run/test verification commands. -- evidence: [docs/s00.md#L152-L154](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L152-L154), [docs/s00.md#L28-L36](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L28-L36), [docs/s00.md#L167-L167](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L167-L167), [docs/s00.md#L142-L142](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L142-L142), [docs/s00.md#L132-L135](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L132-L135), [docs/s00.md#L162-L164](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L162-L164) (`clm_4470697a9f676492f651f4239cdfed50f8c1c47aac9eed66ad8cd875686cd213`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The agent communicates with POST https://api.anthropic.com/v1/messages over raw HTTP built on AsyncHTTPClient, and the CLI executable is named `agent`. -- evidence: [README.md#L101-L101](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L101-L101), [README.md#L103-L103](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L103-L103) (`clm_fcfa9bdf7269b6fa9e851458f14f25b152fa49487509ccfce62586eeaf5e7e2d`)

## memory-state (1 claim(s))

- [observation/documented] The messages array lives on the Agent instance so conversation history persists across REPL turns, and each API call sends the entire accumulated history, which grows without bound until later context compaction. -- evidence: [docs/s01.md#L197-L197](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L197-L197), [docs/s01.md#L199-L199](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L199-L199), [docs/s01.md#L58-L58](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L58-L58) (`clm_924396de8ef692691ef2d159ba6a789a144038b0b84c8766fd8c8bc7a9504ee5`)

## orchestration (2 claim(s))

- [observation/documented] The agent runs a fixed while-true loop: append the user query, call the Anthropic API, and if the stop reason is tool use, execute tools and append results as a user message; otherwise return the text content. -- evidence: [README.md#L39-L41](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L39-L41), [README.md#L43-L48](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L43-L48), [README.md#L50-L52](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L50-L52), [README.md#L54-L64](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L54-L64) (`clm_77541a28832fe82155a6c0d3835a0406919afbc5387de7db5e727a5039f04db3`)
- [observation/documented] The loop body is invariant across stages; each stage only adds tool handler entries and injection points before the API call, with tools varying while the loop stays identical. -- evidence: [docs/s01.md#L156-L156](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L156-L156), [README.md#L66-L66](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L66-L66) (`clm_573f0405798151bd993c21f5aa24d5deb4759da65039fad1081e0ec518841e03`)

## tools-permissions (3 claim(s))

- [observation/documented] Stage 01 gives the model a single bash tool, executed via Foundation's Process running /bin/bash -c, with pipe data read before waitUntilExit to avoid a roughly 64 KB buffer deadlock. -- evidence: [docs/s01.md#L184-L184](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L184-L184), [docs/s01.md#L170-L174](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L170-L174), [docs/s01.md#L164-L168](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L164-L168), [docs/s01.md#L160-L160](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L160-L160) (`clm_5601df09bb8dad95d73edc0f749ecee859d71fb5bded3288e1a217f90834e305`)
- [observation/documented] File tools enforce path sandboxing: paths are resolved against the working directory and any resolved location that escapes it is rejected with an executionFailed error. -- evidence: [docs/s02.md#L70-L75](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s02.md#L70-L75), [docs/s02.md#L54-L54](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s02.md#L54-L54) (`clm_15612b25f88a32f89245cdbcc3f944aff628a6f7662223c8638da6631f2ca647`)
- [observation/documented] Tool dispatch is a dictionary mapping tool names to handlers (bash, read_file, write_file, edit_file), returning an unknownTool failure for unregistered names, chosen over a protocol registry for its simplicity. -- evidence: [docs/s02.md#L50-L50](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s02.md#L50-L50), [docs/s02.md#L42-L44](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s02.md#L42-L44), [docs/s02.md#L32-L40](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s02.md#L32-L40) (`clm_0e977347b396a584775b1845f3bdd2f7bf5e5a3c6a5f7c39262396efd8a83e6f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package depends on AsyncHTTPClient (from 1.32.0, SwiftNIO-based) rather than URLSession for cross-platform macOS/Linux HTTP and streaming SSE, built with Swift 6.2 strict concurrency. -- evidence: [docs/s00.md#L118-L118](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L118-L118), [docs/s00.md#L83-L116](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L83-L116), [docs/s00.md#L120-L120](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L120-L120), [README.md#L117-L120](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L117-L120) (`clm_7447858dcbdcaaab82e209d5632265ba932ebf12cde85ecddd1a98d0ed5276e5`)

## limitations (1 claim(s))

- [observation/documented] The README states the project is explicitly not a full Claude Code clone, a general-purpose multi-agent framework, or production-ready IDE tooling; the gaps are deliberate. -- evidence: [README.md#L113-L113](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L113-L113), [README.md#L109-L111](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L109-L111) (`clm_0559886f40371a94cc44038d98afcf1d5526e595ac5604ee00dd42030966ae81`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

