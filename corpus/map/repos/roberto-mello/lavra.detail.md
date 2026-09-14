# roberto-mello/lavra -- full detail

[Back to orientation](lavra.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/roberto-mello/lavra/2e7e512eb90baee2c45fa4e08e685d0328fe58db/955fc447d95d4f9a.json](../../../wiki/dossiers/roberto-mello/lavra/2e7e512eb90baee2c45fa4e08e685d0328fe58db/955fc447d95d4f9a.json)

## specifications (1 claim(s))

- [observation/documented] Lavra is a plugin for coding agents that orchestrates the development lifecycle from brainstorming to shipping while automatically capturing and recalling knowledge so each unit of work makes the next easier. -- evidence: [README.md#L9-L9](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L9-L9), [README.md#L7-L7](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L7-L7) (`clm_5d733233834c4894a26c48b8dc6fe1463eadd4ed476345a0e2833498866eef32`)

## components (1 claim(s))

- [observation/documented] The plugin ships 30 specialized agents (16 review, 5 research, 3 design, 5 workflow, 1 docs per the architecture tree), 16 core skills, 4 hooks, and a Context7 MCP server for framework documentation lookup. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L85-L108](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L85-L108), [site/src/content/docs/CATALOG.md#L83-L100](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/CATALOG.md#L83-L100), [site/src/content/docs/CATALOG.md#L116-L116](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/CATALOG.md#L116-L116), [site/src/content/docs/CATALOG.md#L120-L125](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/CATALOG.md#L120-L125), [README.md#L116-L116](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L116-L116) (`clm_e98223c3058e6b9c6255214e875511577ad93b2df1fc9a84850e38ebca0a7d24`)

## design-choices (1 claim(s))

- [observation/documented] Lavra is a fork of Every's compound-engineering-plugin (MIT), replacing markdown knowledge storage with beads-based JSONL memory, FTS5 search, and workflows that create and update beads instead of markdown files. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L116-L123](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L116-L123), [site/src/content/docs/ARCHITECTURE.md#L112-L112](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L112-L112), [README.md#L172-L172](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L172-L172) (`clm_5c1e51242568c4b9eb38a9fafccb8c353e3638f05a4d765141aef5b768ab1a54`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes slash commands: a four-command pipeline (/lavra-design, /lavra-work, /lavra-qa, /lavra-ship) plus supporting commands like /lavra-quick, /lavra-learn, /lavra-recall and power-user commands /lavra-work-ralph and /lavra-work-teams. -- evidence: [README.md#L110-L110](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L110-L110), [README.md#L112-L112](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L112-L112), [README.md#L114-L114](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L114-L114) (`clm_009dc27599a0a427ec6a49540852229555f699d297cd81941d651444b6b1c133`)
- [observation/documented] Behavior is configured via .lavra/config/lavra.json, which toggles workflow phases (research, plan_review, goal_verification, review_scope, testing_scope), execution parallelism, commit granularity, and model_profile; all fields are optional with documented defaults. -- evidence: [site/src/content/docs/configuration.md#L9-L9](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L9-L9), [site/src/content/docs/configuration.md#L28-L28](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L28-L28), [README.md#L137-L138](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L137-L138), [README.md#L144-L166](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L144-L166) (`clm_7e1c3ab25b0ee7dec7eff79888b3c423dddeb4e290579e02f9f9fc87c6a2b748`)

## memory-state (2 claim(s))

- [observation/documented] Knowledge is stored in a shared append-only JSONL log (.lavra/memory/knowledge.jsonl) committed to git, with a local SQLite FTS5 search index, a curated active cache, and an audit log of sanitizer filtering actions. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L15-L15](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L15-L15), [site/src/content/docs/ARCHITECTURE.md#L17-L21](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L17-L21) (`clm_51e4c4920a85e9d9d7259859ffb1bb9376dfe12e617d5468497e0504234c7a24`)
- [observation/documented] Six knowledge types (LEARNED, DECISION, FACT, PATTERN, INVESTIGATION, DEVIATION) are captured inline during work, and relevant entries are recalled automatically at session start based on current beads and the git branch. -- evidence: [README.md#L133-L133](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L133-L133) (`clm_0759237a21392774e6189540bbee5ad73a6b9e610d8d5c92cf7012e4220ca685`)

## orchestration (2 claim(s))

- [observation/documented] /lavra-work auto-routes between single-bead and multi-bead parallel execution, with a configurable max_parallel_agents (default 3) and per-task atomic commits whose bead IDs make git log grep useful. -- evidence: [site/src/content/docs/configuration.md#L90-L91](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L90-L91), [README.md#L70-L70](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L70-L70), [site/src/content/docs/configuration.md#L82-L82](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L82-L82), [README.md#L144-L166](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L144-L166) (`clm_324cc7c5b1f0dbb27e19261818620eff197ec378cbebffd88d48089893509bdc`)
- [observation/documented] Agents run at assigned model tiers (Haiku/Sonnet/Opus) by reasoning complexity; the 'quality' model_profile routes critical agents like security-sentinel and goal-verifier to Opus, with a documented claim of 60-70% cost reduction versus running everything on the top model. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L73-L73](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L73-L73), [site/src/content/docs/ARCHITECTURE.md#L127-L132](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L127-L132), [README.md#L116-L116](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L116-L116), [site/src/content/docs/configuration.md#L103-L104](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/configuration.md#L103-L104) (`clm_95fba6fe4638d0c11be02732049650374d8487396ca5d876c807f912a5aaf4b7`)

## tools-permissions (1 claim(s))

- [observation/documented] For autonomous modes (/lavra-work-ralph, /lavra-work-teams), the docs recommend a granular allow list in .claude/settings.json (git, bd, test runners, Read/Write/Edit/Grep/Glob) rather than --dangerously-skip-permissions, which bypasses all approval prompts globally. -- evidence: [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L86-L91](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L86-L91), [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L25-L42](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L25-L42), [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L23-L23](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L23-L23), [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L50-L50](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L50-L50), [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L65-L65](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L65-L65) (`clm_8947b8ae6060580fcb721a23c2b3096d92c301c22542e1f9f59c66e268e0cf3e`)

## evaluation (1 claim(s))

- [observation/documented] The architecture doc reports FTS5 search with BM25 ranking improved precision by 18%, recall by 17%, and MRR by 24% over grep-based search across 25 benchmark queries. -- evidence: [site/src/content/docs/ARCHITECTURE.md#L116-L123](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L116-L123) (`clm_3a585a3901557192b9c72fece8243a642d4be055681b4bf0dcd8021c2b202cc0`)

## dependencies (1 claim(s))

- [observation/documented] Lavra requires the beads CLI, jq, and sqlite3; the memory sanitizer compiles a Go helper when Go is available and falls back to a jq-based path otherwise, and grep-based search remains if sqlite3 is missing. -- evidence: [README.md#L90-L90](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/README.md#L90-L90), [site/src/content/docs/ARCHITECTURE.md#L23-L23](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/ARCHITECTURE.md#L23-L23) (`clm_53fb2d98d15ce3f271d638fdbc0247d92e588684a9c6dc2d36530b39cfe3a834`)

## limitations (1 claim(s))

- [observation/documented] The docs acknowledge autonomous-mode trade-offs: bash runs without review, file writes are unapproved with only advisory ownership enforcement, and there is no human checkpoint; mitigations include feature branches, low retry budgets, and worktree/container isolation. -- evidence: [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L82-L84](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L82-L84), [site/src/content/docs/AUTONOMOUS_EXECUTION.md#L86-L91](https://github.com/roberto-mello/lavra/blob/2e7e512eb90baee2c45fa4e08e685d0328fe58db/site/src/content/docs/AUTONOMOUS_EXECUTION.md#L86-L91) (`clm_2ba14b166d28f5a00d26af2ceef2efe4ff1a2a37afed8f5951009e7b5e50f760`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

