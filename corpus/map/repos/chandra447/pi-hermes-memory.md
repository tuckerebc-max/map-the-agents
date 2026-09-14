# chandra447/pi-hermes-memory

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 71ce9f0cf298 @ c661b291c1be6aa1

## Summary (orientation draft, not independently verified)

Selected evidence records: The extension manages three knowledge types: MEMORY.md facts (5,000-char cap), USER.md profile (5,000-char cap), and Pi-native SKILL.md procedures with unlimited size. Memory is stored at two tiers: global facts under ~/.pi/agent/pi-hermes-memory/ and per-project facts under ~/.pi/agent/projects-memory/<project>/, with project memories searchable when the cwd matches.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The extension manages three knowledge types: MEMORY.md facts (5,000-char cap), USER.md profile (5,000-char cap), and Pi-native SKILL.md procedures with unlimited size. -- evidence: [README.md#L81-L85](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L81-L85)
- design-choices (2 claim(s)):
  - [observation/documented] Standing instructions (/memory-pin) are a user-authored file injected into every session in every memory mode, capped at 20 entries / 2,000 characters, stored in STANDING.md which background processes cannot write; the feature is explicitly not tool enforcement. -- evidence: [README.md#L196-L196](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L196-L196), [README.md#L207-L212](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L207-L212), [README.md#L216-L216](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L216-L216)
  - [observation/documented] Memory blocks are wrapped in <memory-context> XML tags with a guard note stating they are not new user input, to prevent the model from treating stored facts as instructions. -- evidence: [README.md#L252-L252](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L252-L252)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] For create and update, skill_manage prefers structured fields (when_to_use, procedure_steps, pitfalls, verification_steps) rendered into SKILL.md sections, and global creation has duplicate/similarity guards blocking exact slug matches and near-name collisions. -- evidence: [README.md#L305-L307](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L305-L307), [README.md#L294-L294](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L294-L294), [README.md#L301-L301](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L301-L301), [README.md#L296-L299](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L296-L299)
  - [observation/documented] Project-scoped skills are exposed to Pi via the resources_discover hook, which returns the active project's skills directory so Pi discovers them natively without copying into the global folder. -- evidence: [README.md#L343-L343](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L343-L343), [README.md#L337-L337](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L337-L337), [README.md#L339-L339](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L339-L339)
- interfaces (4 claim(s)):
  - [observation/documented] The agent gets memory write tools memory_add, memory_replace, and memory_remove with targets memory, user, project, and failure, plus a skill_manage tool with create, view, patch, update, and delete actions. -- evidence: [README.md#L274-L280](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L274-L280), [README.md#L268-L268](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L268-L268), [README.md#L262-L266](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L262-L266)
  - [observation/documented] Search tools include session_search over past conversations and memory_search over the extended store; FTS5 with a trigram tokenizer supports multi-word, quoted-phrase, OR-operator, and CJK substring queries of three or more characters. -- evidence: [README.md#L364-L368](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L364-L368), [README.md#L359-L362](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L359-L362), [README.md#L357-L357](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L357-L357)
- memory-state (4 claim(s)):
  - [observation/documented] Memory is stored at two tiers: global facts under ~/.pi/agent/pi-hermes-memory/ and per-project facts under ~/.pi/agent/projects-memory/<project>/, with project memories searchable when the cwd matches. -- evidence: [README.md#L172-L175](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L172-L175)
  - [observation/documented] By default full Markdown memories are not injected into the system prompt; instead a <memory-policy> block tells the agent when to call memory_search, keeping first-turn token usage low. -- evidence: [README.md#L177-L177](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L177-L177)
- orchestration (3 claim(s)):
More evidence: [full detail](pi-hermes-memory.detail.md)

Metadata and full claim list: [full detail](pi-hermes-memory.detail.md)
Human notes ([notes](pi-hermes-memory.notes.md), never overwritten by build)

[Back to map index](../../index.md)
