---
access: public
aliases: []
claim_ids:
- clm_02ebf19d5e146f12eb7238bfc87736620d0974a08f7f894a7826969b0fbbe990
- clm_19c2136da4b1cdaabb4b5ded8c0fba28e27fb12024c7540bbdcc632c101e87d7
- clm_1a668e271c5add279af2f48e0ea4f672036e3a5e9459022f2714f94e722b0f8f
- clm_54e6e494f81ce807e81a4826e1f0b5918770143fe869871e68f6d4826bab8640
- clm_5a15e494dc1550e43b7789c4ac9f6e342fee2309cdb28cd07de6253a8dcccd1a
- clm_6d4c517fccd3534f6e655998d55c72368ab1386ef9ca80af806634dfe581def7
- clm_6ee0275603cdfa3373cbff18e23f542ff7cf503efa7a4e6153fac2ea4ca44182
- clm_72867db9eb66dfa5f3b70a3f62a1df832118bb7e345a6a5f8caf55fae46c1b1f
- clm_810fc6edb526b6513c0f756926e61190287412ac420255517b3e929cdab5bdba
- clm_8e29e0cb3fb655a071817e723834b97830dbf4dda5cc03a47bb368a776899408
- clm_a744c784aabe7959650a82e5309f1963bb5ab19a31b7d7301a3cc1399fea1758
- clm_b721df68cc56ba5aa86e4b8a2008a09e7ee7bd608fd1b0768ef2d4247c3cf16d
- clm_c0c2403bb545078012dc55a89a8a74a39c85bd011e780a33cf311354fd0007e5
- clm_c88adf230f94d1830a7e147620fc5fcaf1a4ceaa0df9a77f9750cf00f81e22cb
- clm_f182ba75c9b9b63e44b09d78f9d6061e8adf2dfe2f970f694bcbbb9e33ca2522
- clm_f3462955576b931bd0217aa053cab42bdef9e60cfd33a3c6f25e10da1a1f72b6
maturity: draft
page_id: pg_7f4685db743e55b1a10ae743abc5eebc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_147f9ac28c835f33b59d862016901cbf
title: Agent-Field/SWE-AF/README.md @ 311f376a2f12
updated_at: '2026-09-14T01:30:51Z'
---

# Agent-Field/SWE-AF/README.md @ 311f376a2f12

<!-- rcw:begin owner=source:src_147f9ac28c835f33b59d862016901cbf block=evidence -->
- Web search is opt-in for the open runtime: setting OPENCODE_ENABLE_EXA=1 and EXA_API_KEY exposes opencode's websearch/webfetch tools to reasoners, with a restraint guideline appended to the coder's system prompt. [@claim:clm_02ebf19d5e146f12eb7238bfc87736620d0974a08f7f894a7826969b0fbbe990]
- Three nested control loops adapt to difficulty: coder retries on QA/review failure, an issue advisor retries/splits/accepts with debt, and a replanner restructures the remaining DAG on escalated failures. [@claim:clm_19c2136da4b1cdaabb4b5ded8c0fba28e27fb12024c7540bbdcc632c101e87d7]
- Multi-repo builds pass config.repos as an array where each repo has a role: primary (failures block) or dependency (failures captured but non-blocking). [@claim:clm_1a668e271c5add279af2f48e0ea4f672036e3a5e9459022f2714f94e722b0f8f]
- The Claude runtime's first-party WebSearch/WebFetch is not wired in; web search works only on the open (opencode) runtime. [@claim:clm_54e6e494f81ce807e81a4826e1f0b5918770143fe869871e68f6d4826bab8640]
- Builds are triggered through the af CLI (af >= 0.1.87) via `af call swe-planner.build --in ...`, or by POSTing to the AgentField HTTP endpoint /api/v1/execute/async/swe-planner.build. [@claim:clm_5a15e494dc1550e43b7789c4ac9f6e342fee2309cdb28cd07de6253a8dcccd1a]
- ANTHROPIC_BASE_URL is process-wide, so a single deployment cannot route Claude and MiniMax Anthropic-compatible traffic to different endpoints. [@claim:clm_6d4c517fccd3534f6e655998d55c72368ab1386ef9ca80af806634dfe581def7]
- Entry points register with the control plane carrying an entrypoint tag and routing description, discoverable via af ls --entrypoints or GET /api/v1/discovery/capabilities on agentfield >= 0.1.113. [@claim:clm_6ee0275603cdfa3373cbff18e23f542ff7cf503efa7a4e6153fac2ea4ca44182]
- Three runtimes are supported via a flat config map: claude_code (Claude), open_code (OpenCode with OpenRouter/OpenAI/Google/Anthropic IDs), and codex (OpenAI Codex CLI). [@claim:clm_72867db9eb66dfa5f3b70a3f62a1df832118bb7e345a6a5f8caf55fae46c1b1f]
- A self-reported benchmark scores SWE-AF 95/100 with haiku (~$20) and MiniMax M2.5 (~$6) versus Claude Code sonnet (73), Codex o3 (62), and Claude Code haiku (59) on a Node.js todo-app prompt, using a five-dimension scoring framework. [@claim:clm_810fc6edb526b6513c0f756926e61190287412ac420255517b3e929cdab5bdba]
- Repository development practice: the README's Tests badge points to a make check command run via GitHub Actions CI (.github/workflows/ci.yml). [@claim:clm_8e29e0cb3fb655a071817e723834b97830dbf4dda5cc03a47bb368a776899408]
- With only an OpenRouter or Infron key set and no SWE_DEFAULT_RUNTIME, the system auto-selects the open_code runtime and defaults roles to a deepseek model id. [@claim:clm_a744c784aabe7959650a82e5309f1963bb5ab19a31b7d7301a3cc1399fea1758]
- Input accepts repo_url for remote repos or repo_path for local workspaces, plus a config map with runtime, per-role models, and enable_learning. [@claim:clm_b721df68cc56ba5aa86e4b8a2008a09e7ee7bd608fd1b0768ef2d4247c3cf16d]
- An issue-level entry point swe-planner.implement_issue (and swe-fast.implement_issue) skips planning agents, runs a coder-reviewer loop on an isolated branch, and returns the branch name as the deliverable. [@claim:clm_c0c2403bb545078012dc55a89a8a74a39c85bd011e780a33cf311354fd0007e5]
- After opening a PR, a post-PR CI gate watches GitHub Actions and runs a bounded fix-and-repush loop (default max_ci_fix_cycles=2) whose agent is forbidden from silencing tests; unresolved failures leave the PR open for human review. [@claim:clm_c88adf230f94d1830a7e147620fc5fcaf1a4ceaa0df9a77f9750cf00f81e22cb]
- Issues are dependency-sorted and executed in parallel across isolated git worktrees; a typical run reportedly spins up 400-500+ agent instances, scaling to thousands for larger DAGs. [@claim:clm_f182ba75c9b9b63e44b09d78f9d6061e8adf2dfe2f970f694bcbbb9e33ca2522]
- Local requirements are Python 3.12+, the AgentField control plane (af), and an AI provider API key (Anthropic, OpenRouter, OpenAI, or Google). [@claim:clm_f3462955576b931bd0217aa053cab42bdef9e60cfd33a3c6f25e10da1a1f72b6]
<!-- rcw:end owner=source:src_147f9ac28c835f33b59d862016901cbf block=evidence -->

## Researcher notes

