# maxkle1nz/m1nd

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5e208d6ccdff @ 6b14714f4ee27673

## Summary (orientation draft, not independently verified)

The MCP surface exposes verbs including impact, seek, why, north, ghost_edges, xray_gate, antibody_scan, missing, trust_selftest, and predict. north(task) is described as the front door returning one orientation packet with binding trust, memory, sufficiency, next_move, and honest_gaps. Evidence coverage: 129 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 207 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The runtime is a single Rust binary fetched as a signed release by the npm installer package @maxkle1nz/m1nd; cargo install m1nd-mcp is an alternative. -- evidence: [README.md#L7-L7](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L7-L7), [README.md#L177-L177](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L177-L177), [README.md#L181-L181](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L181-L181), [README.md#L198-L198](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L198-L198)
- design-choices (1 claim(s)):
  - [observation/documented] Everything runs locally with no telemetry, no account, and no cloud; memory is stored as plain markdown under agent-memory/ so it survives without m1nd installed. -- evidence: [README.md#L7-L7](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L7-L7), [README.md#L206-L206](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L206-L206), [README.md#L117-L117](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L117-L117)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the demo smoke path (initialize, tools/list, trust_selftest, ingest, seek, doctor, recovery) can be run via cargo build -p m1nd-mcp and m1nd smoke --repo . --transport stdio. -- evidence: [docs/AGENT-FIRST-DEMO.md#L9-L11](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-FIRST-DEMO.md#L9-L11), [docs/AGENT-FIRST-DEMO.md#L17-L20](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-FIRST-DEMO.md#L17-L20)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repo ships installable agent skills (m1nd-first, m1nd-operator, a portable universal pack) teaching an OMEGA loop: north-first orientation, calibrated verdicts, memorize-at-close. -- evidence: [docs/AGENT-PACKS.md#L11-L19](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L11-L19), [docs/AGENT-PACKS.md#L94-L98](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L94-L98)
- interfaces (2 claim(s)):
  - [observation/documented] The MCP surface exposes verbs including impact, seek, why, north, ghost_edges, xray_gate, antibody_scan, missing, trust_selftest, and predict. -- evidence: [README.md#L53-L53](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L53-L53)
  - [observation/documented] north(task) is described as the front door returning one orientation packet with binding trust, memory, sufficiency, next_move, and honest_gaps. -- evidence: [README.md#L152-L152](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L152-L152), [README.md#L159-L169](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L159-L169), [docs/AGENT-PACKS.md#L64-L92](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L64-L92)
- memory-state (2 claim(s)):
  - [observation/documented] Each repository gets one brain with its own graph and memory bound to a repo root; a served owner on port 1337 hosts many brains and refuses unhosted repos with a typed refusal. -- evidence: [README.md#L129-L129](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L129-L129), [README.md#L131-L136](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L131-L136)
  - [observation/documented] Conclusions memorized with evidence persist across sessions and agents, are flagged stale if code changed, and confirmed results reinforce edges Hebbian-style. -- evidence: [README.md#L67-L67](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L67-L67), [README.md#L171-L171](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L171-L171), [README.md#L31-L31](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L31-L31)
- orchestration (2 claim(s)):
  - [observation/documented] Multiple agents on one repo register presences with TTLs; overlapping work triggers collision warnings in both agents' orientation packets before changes land. -- evidence: [README.md#L91-L91](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L91-L91), [README.md#L93-L98](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L93-L98)
  - [observation/documented] Mission tools (mission_start, mission_event, mission_next, mission_verify, mission_handoff, mission_close) create repo-scoped routes and budgets and reject graph-only claims. -- evidence: [docs/AGENT-PACKS.md#L100-L110](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L100-L110), [README.md#L101-L101](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L101-L101)
- tools-permissions (1 claim(s)):
More evidence: [full detail](m1nd.detail.md)

Metadata and full claim list: [full detail](m1nd.detail.md)
Human notes ([notes](m1nd.notes.md), never overwritten by build)

[Back to map index](../../index.md)
