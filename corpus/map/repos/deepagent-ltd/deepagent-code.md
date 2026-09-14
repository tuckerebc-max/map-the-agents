# deepagent-ltd/deepagent-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 57be03002bc4 @ 0b8d0383da0604bb

## Summary (orientation draft, not independently verified)

The snapshot documents DeepAgent Code, an AI coding workspace with durable sessions, governed memory, multi-agent orchestration, and provider-agnostic model access, described across README (English and Chinese), CONTEXT.md, CHANGELOG.md, and PRIVACY.md. Claims below are limited to what the cited slices state. Evidence coverage: 149 of 206 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Three collaboration modes are offered: Auto (end-to-end execution), Loop (editable `goal+plan.md` advanced through plan, execute, verify, iterate ticks), and Design (faithful execution of a user-written plan); autonomy and permission levels are independent of mode. -- evidence: [README.md#L38-L42](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L38-L42), [README.md#L44-L44](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L44-L44)
  - [observation/documented] Context assembly uses a durable Context Epoch: stable system instructions stay byte-stable for prompt caching while volatile state is appended in a dedicated tail block, and context changes are admitted only at safe provider-turn boundaries. -- evidence: [CONTEXT.md#L39-L40](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/CONTEXT.md#L39-L40), [README.md#L79-L79](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L79-L79), [README.md#L81-L81](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L81-L81)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships as a desktop app and a terminal CLI; the CLI supports `deepagent auth login`, `deepagent auth list`, and `deepagent-code run "<task>"`. -- evidence: [README.md#L107-L108](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L107-L108), [README.md#L161-L161](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L161-L161), [README.md#L164-L165](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L164-L165), [README.md#L202-L204](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L202-L204), [README.md#L143-L143](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L143-L143)
  - [observation/documented] Providers are configured in `~/.deepagent/code/config.jsonc`; a custom OpenAI-compatible endpoint can set `discovery: true` for runtime model refresh or list models explicitly under `models`. -- evidence: [README.md#L169-L171](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L169-L171), [README.md#L173-L188](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L173-L188)
- memory-state (2 claim(s)):
  - [observation/documented] Persistent state lives in typed documents (knowledge, strategy, methodology, skill, memory, design, worklog, diagnosis, eval) linked via supports/blocks/conflicts/validates into a traversable graph, with scope layers from session-private to sealed audit-only material. -- evidence: [README.md#L218-L218](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L218-L218), [README.md#L220-L220](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L220-L220)
  - [observation/documented] Learning follows a governed lifecycle: evidence creates a candidate, isolated review or human decision changes its status, and regression/ablation gates publish a reproducible knowledge snapshot; rejection reasons persist so discarded patterns are not silently relearned. -- evidence: [README.md#L66-L66](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L66-L66)
- orchestration (2 claim(s)):
  - [observation/documented] Write-capable subagents get dedicated worktrees and return compact summaries; a Reviewer session checks each exact worker SHA, the coordinator performs serial `--no-ff` merges, and generation fencing prevents stale workers from settling or overwriting newer work. -- evidence: [README.md#L97-L97](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L97-L97), [README.md#L95-L95](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L95-L95)
More evidence: [full detail](deepagent-code.detail.md)

Metadata and full claim list: [full detail](deepagent-code.detail.md)
Human notes ([notes](deepagent-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
