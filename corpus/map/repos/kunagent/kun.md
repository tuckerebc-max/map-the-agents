# kunagent/kun

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e67f656bca57 @ 2169da6efe174106

## Summary (orientation draft, not independently verified)

Evidence covers Kun's README, extension architecture doc, CLA, code of conduct, and a design-token file. Kun is a local-first AI agent workbench with a desktop GUI and TUI sharing one `kun serve` runtime, an extension platform with process isolation, and documented contributor workflows. Evidence coverage: 155 of 239 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 103 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Kun is described as a local-first AI agent workbench with two main modes: Code for software delivery (with a Design canvas in the same task) and Work for writing, document analysis, and presentations. -- evidence: [README.md#L35-L35](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L35-L35)
  - [observation/documented] The project is licensed under PolyForm Noncommercial 1.0.0 for learning, research, and noncommercial use; commercial use, SaaS/hosting, or resale requires separate written authorization from the author. -- evidence: [CLA.md#L59-L61](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/CLA.md#L59-L61), [README.md#L153-L153](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L153-L153)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The extension platform is documented as not creating a second agent runtime; extensions reach agent, tool, approval, and provider capabilities only through a public Host Context and Broker. -- evidence: [docs/extensions/architecture.md#L9-L9](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L9-L9)
  - [observation/documented] Sessions, preferences, logs, and runtime data are stored locally by default; when a cloud model is chosen, prompts, attachments, and task context are sent to the selected provider, and tool/extension permissions are surfaced in the UI for user approval. -- evidence: [README.md#L84-L84](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L84-L84)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions target the `develop` branch, contributors should read the contributing guide, and external contributions require signing a CLA; the CLA grants the project owner broad relicensing rights while contributors retain copyright. -- evidence: [CLA.md#L20-L24](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/CLA.md#L20-L24), [README.md#L149-L149](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L149-L149), [CLA.md#L14-L16](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/CLA.md#L14-L16)
  - [observation/documented] Repository development practice: README documents npm commands for development (`npm run dev`, `dev:tui`), typecheck, ESLint with file-size checks, tests, production build, and per-platform distribution builds. -- evidence: [README.md#L123-L131](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L123-L131)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The desktop GUI and terminal TUI share a single local `kun serve` runtime, sharing threads, goals, plans, approvals, and background tasks rather than separate sessions. -- evidence: [README.md#L104-L104](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L104-L104), [README.md#L37-L37](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L37-L37)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] ExtensionManager runs one Node child process per active Node extension over versioned private JSON IPC, lazily starts hosts on activation, merges concurrent activations, and enforces bounded time, concurrency, rate, and memory limits. -- evidence: [docs/extensions/architecture.md#L11-L29](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L11-L29), [docs/extensions/architecture.md#L48-L54](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L48-L54), [docs/extensions/architecture.md#L56-L56](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L56-L56)
- tools-permissions (1 claim(s)):
More evidence: [full detail](kun.detail.md)

Metadata and full claim list: [full detail](kun.detail.md)
Human notes ([notes](kun.notes.md), never overwritten by build)

[Back to map index](../../index.md)
