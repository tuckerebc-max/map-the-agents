# roberto-mello/lavra

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2e7e512eb90b @ 955fc447d95d4f9a

## Summary (orientation draft, not independently verified)

Selected evidence records: Lavra is a plugin for coding agents that orchestrates the development lifecycle from brainstorming to shipping while automatically capturing and recalling knowledge so each unit of work makes the next easier. The product exposes slash commands: a four-command pipeline (/lavra-design, /lavra-work, /lavra-qa, /lavra-ship) plus supporting commands like /lavra-quick, /lavra-learn, /lavra-recall and power-user commands /lavra-work-ralph and /lavra-work-teams.

## Source coverage

Source coverage (partial): 6 of 28 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Lavra is a plugin for coding agents that orchestrates the development lifecycle from brainstorming to shipping while automatically capturing and recalling knowledge so each unit of work makes the next easier. -- evidence: [README.md#L9-L9](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L9-L9), [README.md#L7-L7](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] The plugin ships 30 specialized agents (16 review, 5 research, 3 design, 5 workflow, 1 docs per the architecture tree), 16 core skills, 4 hooks, and a Context7 MCP server for framework documentation lookup. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L85-L108](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L85-L108), [site/src/content/docs/CATALOG.md#L83-L100](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/CATALOG.md#L83-L100), [site/src/content/docs/CATALOG.md#L116-L116](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/CATALOG.md#L116-L116), [site/src/content/docs/CATALOG.md#L120-L125](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/CATALOG.md#L120-L125), [README.md#L116-L116](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L116-L116)
- design-choices (1 claim(s)):
  - [observation/documented] Lavra is a fork of Every's compound-engineering-plugin (MIT), replacing markdown knowledge storage with beads-based JSONL memory, FTS5 search, and workflows that create and update beads instead of markdown files. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L116-L123](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L116-L123), [site/src/content/docs/ARCHITECTURE.md#L112-L112](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L112-L112), [README.md#L172-L172](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L172-L172)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes slash commands: a four-command pipeline (/lavra-design, /lavra-work, /lavra-qa, /lavra-ship) plus supporting commands like /lavra-quick, /lavra-learn, /lavra-recall and power-user commands /lavra-work-ralph and /lavra-work-teams. -- evidence: [README.md#L110-L110](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L110-L110), [README.md#L112-L112](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L112-L112), [README.md#L114-L114](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L114-L114)
  - [observation/documented] Behavior is configured via .lavra/config/lavra.json, which toggles workflow phases (research, plan_review, goal_verification, review_scope, testing_scope), execution parallelism, commit granularity, and model_profile; all fields are optional with documented defaults. -- evidence: [site/src/content/docs/configuration.md#L9-L9](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L9-L9), [site/src/content/docs/configuration.md#L28-L28](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L28-L28), [README.md#L137-L138](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L137-L138), [README.md#L144-L166](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L144-L166)
- memory-state (2 claim(s)):
  - [observation/documented] Knowledge is stored in a shared append-only JSONL log (.lavra/memory/knowledge.jsonl) committed to git, with a local SQLite FTS5 search index, a curated active cache, and an audit log of sanitizer filtering actions. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L15-L15](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L15-L15), [site/src/content/docs/ARCHITECTURE.md#L17-L21](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L17-L21)
  - [observation/documented] Six knowledge types (LEARNED, DECISION, FACT, PATTERN, INVESTIGATION, DEVIATION) are captured inline during work, and relevant entries are recalled automatically at session start based on current beads and the git branch. -- evidence: [README.md#L133-L133](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L133-L133)
- orchestration (2 claim(s)):
  - [observation/documented] /lavra-work auto-routes between single-bead and multi-bead parallel execution, with a configurable max_parallel_agents (default 3) and per-task atomic commits whose bead IDs make git log grep useful. -- evidence: [site/src/content/docs/configuration.md#L90-L91](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L90-L91), [README.md#L70-L70](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L70-L70), [site/src/content/docs/configuration.md#L82-L82](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L82-L82), [README.md#L144-L166](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L144-L166)
More evidence: [full detail](lavra.detail.md)

Metadata and full claim list: [full detail](lavra.detail.md)
Human notes ([notes](lavra.notes.md), never overwritten by build)

[Back to map index](../../index.md)
