# langwatch/scenario -- full detail

[Back to orientation](scenario.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/langwatch/scenario/29dea3374ef4abffbd25233a3bfff4184fd6852d/38fb07a586afa0be.json](../../../wiki/dossiers/langwatch/scenario/29dea3374ef4abffbd25233a3bfff4184fd6852d/38fb07a586afa0be.json)

## specifications (1 claim(s))

- [observation/documented] Scenario is described as an agent testing framework based on simulations, able to test real agent behavior by simulating users across scenarios and edge cases. -- evidence: [README.md#L17-L21](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L17-L21), [README.md#L15-L15](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L15-L15) (`clm_de79f4f9009aa18f84d25a0ea22c8d4c9ad5c82bc42070a08d8be4ad378be12b`)

## components (2 claim(s))

- [observation/documented] Shipped agent components include a UserSimulatorAgent, a JudgeAgent evaluated against criteria, and a RedTeamAgent for multi-turn adversarial attacks such as Crescendo escalation with per-turn scoring and refusal detection. -- evidence: [README.md#L370-L375](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L370-L375), [README.md#L44-L48](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L44-L48), [README.md#L130-L151](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L130-L151), [README.md#L368-L368](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L368-L368) (`clm_daf4e583f416bb6e19a3f09b11cbfaacf117b27af3d458bfa9457b9dab85b892`)
- [observation/documented] Voice support ships platform adapters for ElevenLabs, OpenAI Realtime, Twilio Media Streams, Pipecat WebSocket and Gemini Live, with LiveKit, Vapi and generic WebRTC tracked as follow-up work. -- evidence: [README.md#L406-L406](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L406-L406) (`clm_068dba450ade9409355fe467ce7202c7e7891ee50b6aecef40c2ad3166cf05d6`)

## design-choices (3 claim(s))

- [observation/documented] An accepted ADR replaces environment-variable configuration with per-call programmatic config: each run() gets its own EventBus, config and batchRunId, removing process-wide shared state and the need for a mutex. -- evidence: [docs/adr/001-scenario-concurrency-model.md#L5-L5](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/001-scenario-concurrency-model.md#L5-L5), [docs/adr/001-scenario-concurrency-model.md#L25-L29](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/001-scenario-concurrency-model.md#L25-L29), [docs/adr/001-scenario-concurrency-model.md#L17-L17](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/001-scenario-concurrency-model.md#L17-L17) (`clm_e5a3c19708be321cfb2b10e3c6bab24f61b70f189e7116de019ca46db314ecf5`)
- [observation/documented] A proposed ADR moves voice STT/TTS provider state from module-global singletons to per-run ScenarioConfig.voice, because global provider state is unsafe under concurrent runs; Python still carries the global-state design. -- evidence: [docs/adr/002-voice-provider-state.md#L52-L54](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L52-L54), [docs/adr/002-voice-provider-state.md#L25-L29](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L25-L29), [docs/adr/002-voice-provider-state.md#L5-L5](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L5-L5), [docs/adr/002-voice-provider-state.md#L99-L116](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L99-L116) (`clm_c70d919d7bd61b458207f87e2c464837cc45b4884c07431f2f7ea130ec6da592`)
- [observation/documented] A cache_key option makes the simulated user's input repeatable for a given scenario, and a @scenario.cache decorator caches decorated calls keyed by arguments, scenario, and cache_key. -- evidence: [README.md#L453-L453](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L453-L453), [README.md#L445-L445](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L445-L445), [README.md#L465-L465](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L465-L465) (`clm_55862db130039e88f82b05c442f3be1e8f927add7e5b1481687a7597816a4c68`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Agents are integrated by implementing a single call() method, and the framework is documented as available in Python, TypeScript and Go. -- evidence: [README.md#L17-L21](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L17-L21) (`clm_9ab498d6322a3f7e85de5638ef37882a8135902285b8692f80400301a3459312`)
- [observation/documented] The core entrypoint is scenario.run(), taking a name, description, agents list, optional script of steps, and optional max_turns; script steps are functions receiving the scenario state. -- evidence: [README.md#L280-L298](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L280-L298), [README.md#L50-L57](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L50-L57), [README.md#L306-L306](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L306-L306), [README.md#L35-L36](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L35-L36) (`clm_64c7a59044579d505e427546a8ccfc05eda760202ef5c28490a7fd71db34c5c4`)
- [observation/documented] Voice surface includes scenario.audio() for injecting clips, background_noise effects, scenario.interrupt(), result.audio.save() capture, and result.latency reporting TTFB plus p50/p95. -- evidence: [README.md#L408-L408](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L408-L408) (`clm_21e0c175660cab9d8b725ef55a3c38fd3a157f2ff9850e9029692256bc265bcd`)
- [observation/documented] Debug mode shows messages step by step and allows human intervention mid-conversation; it is enabled via configure(debug=True), a per-scenario field, or the --scenario-debug pytest flag. -- evidence: [README.md#L431-L431](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L431-L431), [README.md#L429-L429](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L429-L429), [README.md#L439-L441](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L439-L441) (`clm_e504805d98f09534bb566fd3b02ad22a2b5ca49b769937560e4606978c0a5f9f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The JudgeAgent evaluates agent performance in real time against stated criteria at each turn, deciding whether the simulation proceeds or ends with a verdict. -- evidence: [README.md#L270-L270](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L270-L270), [README.md#L130-L151](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L130-L151) (`clm_028099985f51dc5bce17d0da496d557abb257483a092e4079bece7c660245f6d`)

## dependencies (1 claim(s))

- [observation/documented] Audio dependencies such as ffmpeg, webrtcvad and websockets ship as hard dependencies of the Python package, included in a plain pip install with no extras flag. -- evidence: [README.md#L387-L387](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L387-L387) (`clm_8ad4adc84db8c80636513c166125c588ab4243bc851216c4450407b3b29bca50`)

## limitations (1 claim(s))

- [observation/documented] The judge and user simulator rely on LLMs, so even an ElevenLabs-only voice test requires an OPENAI_API_KEY unless both are swapped via scenario.configure. -- evidence: [README.md#L415-L415](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L415-L415) (`clm_cf6ae7c67e0e99424a020fbea9b3910acfab18c2fe87cfd4a8d08bde248cfd36`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

