# touchpoint-labs/gadfly

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2798406b5d27 @ 8e44562db5006424

## Summary (orientation draft, not independently verified)

Gadfly is a documented (README + spec.md) Socratic supervision layer for Claude Code that reviews tool calls pre-execution via two isolated read-only LLM supervisors, grounded in a five-file memory system with an autonomy dial and CLI commands. Evidence is documentation-only; no code inspection is available.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Gadfly is a Socratic supervision layer that sits inside an AI coding agent's live tool-call loop, questioning consequential moves before they happen. -- evidence: [README.md#L5-L5](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L5-L5), [README.md#L20-L24](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L20-L24)
- components (1 claim(s)):
  - [observation/documented] Two isolated, read-only supervisors review each action: an Architect (default Opus) catching spec drift and undiscussed decisions, and a Code Reviewer (default Sonnet) catching real defects. -- evidence: [spec.md#L16-L16](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L16-L16), [README.md#L91-L97](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L91-L97), [README.md#L89-L89](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L89-L89)
- design-choices (2 claim(s)):
  - [observation/documented] An autonomy dial (autonomous, balanced, collaborative) controls how often undiscussed decisions surface to the user; irreversible operations always ask regardless of the setting. -- evidence: [spec.md#L50-L50](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L50-L50), [README.md#L149-L151](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L149-L151), [README.md#L153-L153](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L153-L153), [README.md#L147-L147](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L147-L147)
  - [observation/documented] Architecture is a pure, agent- and LLM-agnostic core wrapped by two swappable adapters (host-agent format and LLM provider); supervisors call a provider-neutral client with models set in config. -- evidence: [README.md#L227-L229](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L227-L229), [spec.md#L76-L80](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L76-L80), [README.md#L231-L244](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L231-L244)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Reviews produce four verdicts: silent allow, a question sent back to the agent, a surface that pauses and asks the user, and a block on spec-violating or buggy actions. -- evidence: [README.md#L62-L66](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L62-L66), [README.md#L28-L33](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L28-L33)
  - [observation/documented] CLI commands include gadfly init (requires spec.md), status, config, disable/enable, and uninstall; configuration lives in gadfly.toml with optional keys and defaults. -- evidence: [README.md#L178-L184](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L178-L184), [README.md#L188-L190](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L188-L190), [README.md#L167-L169](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L167-L169)
- memory-state (2 claim(s)):
  - [observation/documented] Supervision is grounded in five project files: spec.md (human, required), claude.md (human, optional), codemap.md (builder), decisions.md and memory.md (Gadfly-owned), with a defined trust order. -- evidence: [spec.md#L28-L28](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L28-L28), [spec.md#L20-L26](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L20-L26), [README.md#L119-L125](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L119-L125)
  - [observation/documented] An append-only edit-ledger records agent edits; out-of-band human edits are diffed against them by a separate idle-time extractor that distills generalizable corrections into durable rules. -- evidence: [spec.md#L68-L68](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L68-L68), [README.md#L18-L18](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L18-L18), [README.md#L104-L107](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L104-L107)
- orchestration (1 claim(s)):
  - [observation/documented] A deterministic first pass auto-allows reads and safe commands without any model call, so LLM supervisors only engage for consequential actions. -- evidence: [README.md#L58-L60](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L58-L60), [spec.md#L36-L40](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L36-L40)
- tools-permissions (1 claim(s)):
  - [observation/documented] The agent can read the memory files but is denied direct writes to spec.md, claude.md, and decisions.md; those files change only via the human or Gadfly. -- evidence: [README.md#L127-L129](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L127-L129), [spec.md#L36-L40](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L36-L40)
More evidence: [full detail](gadfly.detail.md)

Metadata and full claim list: [full detail](gadfly.detail.md)
Human notes ([notes](gadfly.notes.md), never overwritten by build)

[Back to map index](../../index.md)
