# langwatch/scenario

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 29dea3374ef4 @ 38fb07a586afa0be

## Summary (orientation draft, not independently verified)

Scenario is a simulation-based agent testing framework (Python, TypeScript, Go) with user-simulator, judge, red-team and voice adapters, per-call concurrency configuration (ADR-001) and a proposed per-run voice-provider design (ADR-002). All claims below are product/runtime documentation claims; development-practice workflow claims were omitted per correction instructions. Evidence coverage: 149 of 226 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 102 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Scenario is described as an agent testing framework based on simulations, able to test real agent behavior by simulating users across scenarios and edge cases. -- evidence: [README.md#L17-L21](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L17-L21), [README.md#L15-L15](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L15-L15)
- components (2 claim(s)):
  - [observation/documented] Shipped agent components include a UserSimulatorAgent, a JudgeAgent evaluated against criteria, and a RedTeamAgent for multi-turn adversarial attacks such as Crescendo escalation with per-turn scoring and refusal detection. -- evidence: [README.md#L370-L375](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L370-L375), [README.md#L44-L48](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L44-L48), [README.md#L130-L151](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L130-L151), [README.md#L368-L368](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L368-L368)
  - [observation/documented] Voice support ships platform adapters for ElevenLabs, OpenAI Realtime, Twilio Media Streams, Pipecat WebSocket and Gemini Live, with LiveKit, Vapi and generic WebRTC tracked as follow-up work. -- evidence: [README.md#L406-L406](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L406-L406)
- design-choices (3 claim(s)):
  - [observation/documented] An accepted ADR replaces environment-variable configuration with per-call programmatic config: each run() gets its own EventBus, config and batchRunId, removing process-wide shared state and the need for a mutex. -- evidence: [docs/adr/001-scenario-concurrency-model.md#L5-L5](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/001-scenario-concurrency-model.md#L5-L5), [docs/adr/001-scenario-concurrency-model.md#L25-L29](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/001-scenario-concurrency-model.md#L25-L29), [docs/adr/001-scenario-concurrency-model.md#L17-L17](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/001-scenario-concurrency-model.md#L17-L17)
  - [observation/documented] A proposed ADR moves voice STT/TTS provider state from module-global singletons to per-run ScenarioConfig.voice, because global provider state is unsafe under concurrent runs; Python still carries the global-state design. -- evidence: [docs/adr/002-voice-provider-state.md#L52-L54](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L52-L54), [docs/adr/002-voice-provider-state.md#L25-L29](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L25-L29), [docs/adr/002-voice-provider-state.md#L5-L5](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L5-L5), [docs/adr/002-voice-provider-state.md#L99-L116](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/docs/adr/002-voice-provider-state.md#L99-L116)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Agents are integrated by implementing a single call() method, and the framework is documented as available in Python, TypeScript and Go. -- evidence: [README.md#L17-L21](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L17-L21)
  - [observation/documented] The core entrypoint is scenario.run(), taking a name, description, agents list, optional script of steps, and optional max_turns; script steps are functions receiving the scenario state. -- evidence: [README.md#L280-L298](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L280-L298), [README.md#L50-L57](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L50-L57), [README.md#L306-L306](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L306-L306), [README.md#L35-L36](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L35-L36)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The JudgeAgent evaluates agent performance in real time against stated criteria at each turn, deciding whether the simulation proceeds or ends with a verdict. -- evidence: [README.md#L270-L270](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L270-L270), [README.md#L130-L151](https://github.com/langwatch/scenario/blob/29dea3374ef4abffbd25233a3bfff4184fd6852d/README.md#L130-L151)
- dependencies (1 claim(s)):
More evidence: [full detail](scenario.detail.md)

Metadata and full claim list: [full detail](scenario.detail.md)
Human notes ([notes](scenario.notes.md), never overwritten by build)

[Back to map index](../../index.md)
