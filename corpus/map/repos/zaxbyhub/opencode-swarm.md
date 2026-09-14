# zaxbyhub/opencode-swarm

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7f125e8f751b @ 1ea8b5b5f4e58f3d

## Summary (orientation draft, not independently verified)

README-only evidence for opencode-swarm, an OpenCode plugin that orchestrates specialized agents behind gated quality pipelines with shell-write guardrails, persistent .swarm/ state, and skill tooling. No code-inspected or development-practice evidence is present. Evidence coverage: 145 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 952 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The plugin registers a roster of specialized agents including architect, coder, reviewer, test_engineer, critic, explorer, sme, docs, designer, plus optional and conditional critic, curator, and council agents. -- evidence: [README.md#L315-L335](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L315-L335), [README.md#L40-L54](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L40-L54)
- design-choices (2 claim(s)):
  - [observation/documented] The pipeline is gated: code does not ship without reviewer and test-engineer approval, and agents never mutate the codebase in parallel. -- evidence: [README.md#L19-L19](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L19-L19), [README.md#L31-L31](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L31-L31)
  - [observation/documented] A Process Remediation Model detects five failure patterns (repetition loop, ping-pong, expansion drift, stuck-on-test, context thrashing) and escalates from advisory guidance to architect alert to hard stop. -- evidence: [README.md#L480-L484](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L480-L484), [README.md#L486-L489](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L486-L489), [README.md#L478-L478](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L478-L478)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skill propagation logs usage to .swarm/skill-usage.jsonl, scores relevance (threshold 0.5, max 5 recommendations), optionally enforces a SKILLS: field on delegations, and supports .opencode/skill-routing.yaml routing. -- evidence: [README.md#L616-L627](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L616-L627), [README.md#L585-L590](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L585-L590), [README.md#L592-L596](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L592-L596), [README.md#L583-L583](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L583-L583)
  - [observation/documented] Seven skill lifecycle tools (skill_generate through skill_improve) are opt-in via skills.enabled (default false); with the flag off they are host-denied for all agents except skill_improver. -- evidence: [README.md#L633-L633](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L633-L633)
- interfaces (2 claim(s)):
  - [observation/documented] Slash commands include /swarm help, status, show-plan, agents, diagnose, evidence, and reset --confirm; deprecated aliases like /swarm plan and /swarm info still function but are hidden from help. -- evidence: [README.md#L291-L291](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L291-L291), [README.md#L273-L281](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L273-L281), [README.md#L293-L305](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L293-L305), [README.md#L307-L307](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L307-L307)
  - [observation/documented] Session modes are toggled via slash commands (balanced default, turbo, lean turbo, full-auto) while project mode is set persistently via the execution_mode config key (strict, balanced, fast). -- evidence: [README.md#L157-L157](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L157-L157), [README.md#L149-L149](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L149-L149), [README.md#L138-L143](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L138-L143), [README.md#L151-L155](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L151-L155), [README.md#L136-L136](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L136-L136)
- memory-state (1 claim(s)):
  - [observation/documented] All project state lives under .swarm/: plan-ledger.jsonl as authoritative source, context.md, evidence/, telemetry.jsonl, and curator-summary.json; sessions are resumable, skipping discovery when state exists. -- evidence: [README.md#L518-L518](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L518-L518), [README.md#L520-L520](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L520-L520), [README.md#L512-L512](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L512-L512), [README.md#L514-L514](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L514-L514), [README.md#L516-L516](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L516-L516), [README.md#L128-L128](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L128-L128)
- orchestration (2 claim(s)):
  - [observation/documented] A Swarm architect coordinates all internal agents automatically; users never manually switch roles, and if the active OpenCode agent is not a Swarm architect the plugin workflow is bypassed. -- evidence: [README.md#L56-L56](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L56-L56), [README.md#L313-L313](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L313-L313)
More evidence: [full detail](opencode-swarm.detail.md)

Metadata and full claim list: [full detail](opencode-swarm.detail.md)
Human notes ([notes](opencode-swarm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
