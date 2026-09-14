# hkuds/deepcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4bb4fd9cb9e8 @ 13ff9f4a8d3f5a21

## Summary (orientation draft, not independently verified)

The evidence is README-only for DeepCode, an open-source coding agent (HKU Data Intelligence Lab) offering TUI, Desktop, and Web clients over one shared local service, with durable sessions, goal-driven loops, skills, MCP plugins, and a permission model. Claims below restate documented product behavior; no development-practice or benchmark evidence appears in these slices. Evidence coverage: 107 of 329 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 37 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Completion is evidence-driven rather than rule-based: the agent selects task-appropriate evidence such as test results, build output, static checks, diagnostics, diffs, or artifacts, and a failed verification feeds the next repair instead of being reported as success. -- evidence: [README.md#L681-L683](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L681-L683), [README.md#L677-L679](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L677-L679)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are discovered from project `.agents/skills` and personal `~/.agents/skills`, plus bundled pinned upstream skills for authoring, review, security, frontend, MCP, and web testing; a Skill can narrow already-allowed tools but cannot grant new permissions. -- evidence: [README.md#L426-L430](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L426-L430), [README.md#L482-L501](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L482-L501), [README.md#L710-L715](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L710-L715), [README.md#L717-L719](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L717-L719)
  - [observation/documented] Skills can declare tool and skill dependencies that are expanded in order with cycle detection, failing before the first model request if a requirement is unavailable; sessions persist only skill identity, invocation kind, and revision, not the instruction body. -- evidence: [README.md#L482-L501](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L482-L501)
- interfaces (2 claim(s)):
  - [observation/documented] DeepCode ships TUI, Desktop, and Web clients over one shared local service, launched via `deepcode`, `deepcode desktop`, or `deepcode web`; all three share projects, sessions, models, skills, permissions, goals, and automations. -- evidence: [README.md#L637-L639](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L637-L639), [README.md#L81-L84](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L81-L84)
  - [observation/documented] The TUI exposes slash commands such as /model, /preset, /effort, /permissions, /transcript, /skill, /resume, /compact, and /context, with bare invocations opening a picker and argument forms keeping text paths. -- evidence: [README.md#L368-L404](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L368-L404), [README.md#L186-L197](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L186-L197), [README.md#L304-L316](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L304-L316)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions are stored locally and linked to their project, keeping tool calls, permission decisions, goals, model configuration, and verification records; history survives restarts and model switches, and compaction preserves the recent tail verbatim. -- evidence: [README.md#L691-L694](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L691-L694), [README.md#L248-L267](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L248-L267), [README.md#L566-L592](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L566-L592), [README.md#L687-L689](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L687-L689)
  - [observation/documented] Compaction summaries are written into workspace memory on a background thread, and injected memory content is wrapped in an escaped `<untrusted-data>` boundary so a poisoned note cannot forge instructions. -- evidence: [README.md#L186-L197](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L186-L197)
- orchestration (2 claim(s)):
More evidence: [full detail](deepcode.detail.md)

Metadata and full claim list: [full detail](deepcode.detail.md)
Human notes ([notes](deepcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
