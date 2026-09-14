# nam271212/strategic-advisor-orchestrator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fedbb4fb4afc @ 4962fdac2b393b1c

## Summary (orientation draft, not independently verified)

The snapshot contains only README documentation for 'Synaptic Compass', an advisory orchestration framework that runs a secondary strategic-advisor model alongside AI coding agents. All claims below are documentation-based; no source code is present in the evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Synaptic Compass is described as an advisory orchestration framework that deploys a secondary, higher-order reasoning model to guide AI coding agents on architecture, security, performance, and debugging. -- evidence: [README.md#L5-L5](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] Documented components include an orchestrator module, context aggregator, configurable reasoning engine, feedback interface, and a memory buffer retaining pattern awareness across sessions. -- evidence: [README.md#L77-L81](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L77-L81)
- design-choices (1 claim(s)):
  - [observation/documented] The product is documented as a stateless, event-driven orchestrator positioned between the user's prompt and the coding agent's execution layer. -- evidence: [README.md#L56-L56](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L56-L56)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcomed for new validation modules, agent adapters, and orchestration-loop optimization, with CONTRIBUTING.md referenced for the code of conduct and pull request process. -- evidence: [README.md#L218-L218](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L218-L218), [README.md#L226-L226](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L226-L226), [README.md#L221-L224](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L221-L224)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Integration is documented for agents exposing streaming output hooks, session context injection, or external tool calling (MCP, plugins, API endpoints), with Claude Code, Cursor, Gemini CLI, and Cline listed as stable integrations. -- evidence: [README.md#L141-L144](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L141-L144), [README.md#L146-L153](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L146-L153)
  - [observation/documented] Configuration uses a compass.yaml or compass.json file defining advisor model, feedback mode (blocking, non_blocking, advisory_only), validation layers, security scan depth, and output format, overridable per session via environment variables or flags. -- evidence: [README.md#L192-L194](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L192-L194), [README.md#L186-L190](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L186-L190), [README.md#L196-L199](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L196-L199), [README.md#L180-L184](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L180-L184), [README.md#L178-L178](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L178-L178), [README.md#L201-L201](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L201-L201)
- memory-state (1 claim(s)):
  - [observation/documented] Advisor contexts are documented as ephemeral and discarded after each orchestration cycle unless the memory buffer is explicitly preserved. -- evidence: [README.md#L207-L210](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L207-L210)
- orchestration (1 claim(s)):
  - [observation/documented] The documented workflow captures prompt, agent reasoning, and project context, dispatches it to the advisor for architecture, security, performance, and edge-case analysis, then injects structured feedback the agent may accept, override, or escalate. -- evidence: [README.md#L122-L126](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L122-L126), [README.md#L119-L119](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L119-L119), [README.md#L129-L132](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L129-L132)
- tools-permissions (1 claim(s)):
  - [observation/documented] The security posture is documented as minimum privilege: no data leaves the environment unless a cloud advisor endpoint is configured, local models are supported, and the security layer never transmits credentials even in diagnostic logs. -- evidence: [README.md#L212-L212](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L212-L212), [README.md#L207-L210](https://github.com/nam271212/strategic-advisor-orchestrator/blob/fedbb4fb4afc9bd101ebb7e0a75ca1ef14a1ce59/README.md#L207-L210)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](strategic-advisor-orchestrator.detail.md)

Metadata and full claim list: [full detail](strategic-advisor-orchestrator.detail.md)
Human notes ([notes](strategic-advisor-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
