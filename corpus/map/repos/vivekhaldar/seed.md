# vivekhaldar/seed

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cd79a60acafe @ 1c4ee6f29e9155bf

## Summary (orientation draft, not independently verified)

seed is documented as a minimal terminal coding agent: a single script calling a model with one exec tool, growing all further capability into a self/ directory the agent edits itself. Its design doc frames this as a deliberately auditable, ungated kernel with no sandbox, positioned against prior minimal-agent and self-improving-agent research. Evidence: all 3 of 3 candidate files stored (README.md, docs/DESIGN.md, SovereignLicense.md); selection complete.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes seed.py as calling a language model with a single exec tool that runs shell commands, loading its system prompt from self/SELF.md, with the agent able to edit self/ to retain tools, notes, and behavior between sessions. -- evidence: [README.md#L5-L7](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L5-L7)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The design doc states the seed prompt and the agent's self-description were collapsed into the same mutable file: the loop's only hardcoded context decision is reading self/SELF.md, re-read every turn so self-edits take effect immediately. -- evidence: [docs/DESIGN.md#L116-L125](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L116-L125)
  - [observation/documented] The license text labels itself Sovereign Source License v0.3 and describes an Apache 2.0 extension with optional development-data services. It says basic use under Apache 2.0 terms involves no data collection. -- evidence: [SovereignLicense.md#L135-L135](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/SovereignLicense.md#L135-L135), [SovereignLicense.md#L11-L11](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/SovereignLicense.md#L11-L11), [README.md#L99-L101](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L99-L101)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state (1 claim(s)):
  - [observation/documented] Documentation states each session is fresh and its conversation is discarded on exit, so nothing survives except what the agent wrote into self/; a separate verbatim transcript is recorded per session as a flight recorder that is never loaded at boot. -- evidence: [README.md#L42-L45](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L42-L45), [docs/DESIGN.md#L127-L132](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L127-L132)
- orchestration (1 claim(s)):
  - [observation/documented] Documentation states planting creates a fresh, private git repo at the target directory (or nests git under self/ inside an existing repo) and never overwrites an existing seed.py or run_seed.sh, so a grown loop cannot be clobbered by a later plant. -- evidence: [docs/DESIGN.md#L151-L158](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L151-L158), [docs/DESIGN.md#L160-L173](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L160-L173), [README.md#L27-L32](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L27-L32)
- tools-permissions (2 claim(s)):
  - [observation/documented] The design doc states the one irreducible primitive is exec: the seed ships exactly one tool that runs a bash command and returns its output, with every other capability expressed through it rather than compressed further. -- evidence: [docs/DESIGN.md#L101-L107](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L101-L107)
More evidence: [full detail](seed.detail.md)

Metadata and full claim list: [full detail](seed.detail.md)
Human notes ([notes](seed.notes.md), never overwritten by build)

[Back to map index](../../index.md)
