# agent-field/swe-af -- full detail

[Back to orientation](swe-af.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agent-field/swe-af/311f376a2f12df01134acd80384d599dd8039178/3876c9a6cfec396b.json](../../../wiki/dossiers/agent-field/swe-af/311f376a2f12df01134acd80384d599dd8039178/3876c9a6cfec396b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Three runtimes are supported via a flat config map: claude_code (Claude), open_code (OpenCode with OpenRouter/OpenAI/Google/Anthropic IDs), and codex (OpenAI Codex CLI). -- evidence: [README.md#L207-L210](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L207-L210) (`clm_72867db9eb66dfa5f3b70a3f62a1df832118bb7e345a6a5f8caf55fae46c1b1f`)
- [observation/documented] With only an OpenRouter or Infron key set and no SWE_DEFAULT_RUNTIME, the system auto-selects the open_code runtime and defaults roles to a deepseek model id. -- evidence: [README.md#L386-L386](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L386-L386), [README.md#L249-L250](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L249-L250) (`clm_a744c784aabe7959650a82e5309f1963bb5ab19a31b7d7301a3cc1399fea1758`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's Tests badge points to a make check command run via GitHub Actions CI (.github/workflows/ci.yml). -- evidence: [README.md#L9-L16](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L9-L16) (`clm_8e29e0cb3fb655a071817e723834b97830dbf4dda5cc03a47bb368a776899408`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] Builds are triggered through the af CLI (af >= 0.1.87) via `af call swe-planner.build --in ...`, or by POSTing to the AgentField HTTP endpoint /api/v1/execute/async/swe-planner.build. -- evidence: [README.md#L44-L54](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L44-L54), [README.md#L58-L78](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L58-L78), [README.md#L42-L42](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L42-L42) (`clm_5a15e494dc1550e43b7789c4ac9f6e342fee2309cdb28cd07de6253a8dcccd1a`)
- [observation/documented] Input accepts repo_url for remote repos or repo_path for local workspaces, plus a config map with runtime, per-role models, and enable_learning. -- evidence: [README.md#L357-L376](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L357-L376), [README.md#L88-L88](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L88-L88) (`clm_b721df68cc56ba5aa86e4b8a2008a09e7ee7bd608fd1b0768ef2d4247c3cf16d`)
- [observation/documented] Multi-repo builds pass config.repos as an array where each repo has a role: primary (failures block) or dependency (failures captured but non-blocking). -- evidence: [README.md#L131-L133](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L131-L133), [README.md#L103-L103](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L103-L103) (`clm_1a668e271c5add279af2f48e0ea4f672036e3a5e9459022f2714f94e722b0f8f`)
- [observation/documented] An issue-level entry point swe-planner.implement_issue (and swe-fast.implement_issue) skips planning agents, runs a coder-reviewer loop on an isolated branch, and returns the branch name as the deliverable. -- evidence: [README.md#L696-L705](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L696-L705), [README.md#L674-L681](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L674-L681), [README.md#L738-L738](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L738-L738), [README.md#L740-L753](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L740-L753) (`clm_c0c2403bb545078012dc55a89a8a74a39c85bd011e780a33cf311354fd0007e5`)
- [observation/documented] Entry points register with the control plane carrying an entrypoint tag and routing description, discoverable via af ls --entrypoints or GET /api/v1/discovery/capabilities on agentfield >= 0.1.113. -- evidence: [README.md#L690-L694](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L690-L694) (`clm_6ee0275603cdfa3373cbff18e23f542ff7cf503efa7a4e6153fac2ea4ca44182`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (3 claim(s))

- [observation/documented] Three nested control loops adapt to difficulty: coder retries on QA/review failure, an issue advisor retries/splits/accepts with debt, and a replanner restructures the remaining DAG on escalated failures. -- evidence: [README.md#L214-L214](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L214-L214), [README.md#L222-L222](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L222-L222), [README.md#L216-L220](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L216-L220) (`clm_19c2136da4b1cdaabb4b5ded8c0fba28e27fb12024c7540bbdcc632c101e87d7`)
- [observation/documented] Issues are dependency-sorted and executed in parallel across isolated git worktrees; a typical run reportedly spins up 400-500+ agent instances, scaling to thousands for larger DAGs. -- evidence: [README.md#L448-L448](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L448-L448), [README.md#L437-L442](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L437-L442) (`clm_f182ba75c9b9b63e44b09d78f9d6061e8adf2dfe2f970f694bcbbb9e33ca2522`)
- [observation/documented] After opening a PR, a post-PR CI gate watches GitHub Actions and runs a bounded fix-and-repush loop (default max_ci_fix_cycles=2) whose agent is forbidden from silencing tests; unresolved failures leave the PR open for human review. -- evidence: [README.md#L665-L670](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L665-L670), [README.md#L654-L661](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L654-L661) (`clm_c88adf230f94d1830a7e147620fc5fcaf1a4ceaa0df9a77f9750cf00f81e22cb`)

## tools-permissions (1 claim(s))

- [observation/documented] Web search is opt-in for the open runtime: setting OPENCODE_ENABLE_EXA=1 and EXA_API_KEY exposes opencode's websearch/webfetch tools to reasoners, with a restraint guideline appended to the coder's system prompt. -- evidence: [README.md#L424-L427](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L424-L427), [README.md#L431-L431](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L431-L431), [README.md#L429-L429](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L429-L429), [README.md#L422-L422](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L422-L422) (`clm_02ebf19d5e146f12eb7238bfc87736620d0974a08f7f894a7826969b0fbbe990`)

## evaluation (1 claim(s))

- [observation/documented] A self-reported benchmark scores SWE-AF 95/100 with haiku (~$20) and MiniMax M2.5 (~$6) versus Claude Code sonnet (73), Codex o3 (62), and Claude Code haiku (59) on a Node.js todo-app prompt, using a five-dimension scoring framework. -- evidence: [README.md#L476-L482](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L476-L482), [README.md#L472-L472](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L472-L472), [README.md#L452-L452](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L452-L452), [README.md#L454-L463](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L454-L463) (`clm_810fc6edb526b6513c0f756926e61190287412ac420255517b3e929cdab5bdba`)

## dependencies (1 claim(s))

- [observation/documented] Local requirements are Python 3.12+, the AgentField control plane (af), and an AI provider API key (Anthropic, OpenRouter, OpenAI, or Google). -- evidence: [README.md#L267-L269](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L267-L269) (`clm_f3462955576b931bd0217aa053cab42bdef9e60cfd33a3c6f25e10da1a1f72b6`)

## limitations (2 claim(s))

- [observation/documented] The Claude runtime's first-party WebSearch/WebFetch is not wired in; web search works only on the open (opencode) runtime. -- evidence: [README.md#L433-L433](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L433-L433) (`clm_54e6e494f81ce807e81a4826e1f0b5918770143fe869871e68f6d4826bab8640`)
- [observation/documented] ANTHROPIC_BASE_URL is process-wide, so a single deployment cannot route Claude and MiniMax Anthropic-compatible traffic to different endpoints. -- evidence: [README.md#L412-L412](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L412-L412) (`clm_6d4c517fccd3534f6e655998d55c72368ab1386ef9ca80af806634dfe581def7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

