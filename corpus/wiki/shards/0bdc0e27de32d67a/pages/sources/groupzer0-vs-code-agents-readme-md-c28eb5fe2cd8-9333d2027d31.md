---
access: public
aliases: []
claim_ids:
- clm_2cd3fbab82a7579f5103bae6e4881f480d4b0f6d2efb95a5fab97862a78a895b
- clm_3dcf52e09a293b8a48971a00354ec04249984a3828ce5ba846db54352935535e
- clm_5f93700e454a8c7c3057b9ade14a0d7a2d64465d9cee84ea03c38bff10212241
- clm_706d9884ee617657335128d85a1f4bcc79d5a616e3d2e18d1f685c75f9bec8b3
- clm_7d0a4d51754cffb43ef8242451bbea844e0f8ee13d0c0263675dd5b84fe91387
- clm_9e4410ad90882b3d6192781296375d23fbf410dc5b0200c8dbaa57a4f53ac63c
- clm_9f62af18ad3c6241793e9bc91980badc26a08408c2569ca3e7d20990df0bcc6b
- clm_a02e28628bcd81723183da7836797d2924630366d60299a1cd32a9ad291dd481
- clm_aa4dba30575a6c1bb0b0b7b2e501bd57143ab28e568cae9e4f32242143ca8125
- clm_baeefc3cbcbc2ad83071b9f0d2480ce8957ee388e2d4ca2c0cbb8b7208df2804
- clm_cae3cfe55c559b186903c08b6189c994d9735e8c2dce2e5d4d17e3109b192fb2
- clm_d80b7a6681aa592db734a8270c04c10e9c38de0218351736265dd54ad01d815e
- clm_e18849a789eb2578ecce0e8b4b3f79970a93aedf86f24f3afaca745cf57e63c5
- clm_f535595cd8fc0e62b71d6a72a3d7aff31963dd92152389a291227802bd52296f
maturity: draft
page_id: pg_909ea19ccf5c58989b099333d2027d31
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_899d0b0aedac560ba5cec6025bf1724c
title: groupzer0/vs-code-agents/README.md @ c28eb5fe2cd8
updated_at: '2026-09-14T03:54:59Z'
---

# groupzer0/vs-code-agents/README.md @ c28eb5fe2cd8

<!-- rcw:begin owner=source:src_899d0b0aedac560ba5cec6025bf1724c block=evidence -->
- A skills system provides modular, on-demand instruction sets including memory-contract, analysis-methodology, security-patterns, testing-patterns, release-procedures, and cross-repo-contract, placed in .claude/skills/ (stable) or .github/skills/ (Insiders). [@claim:clm_2cd3fbab82a7579f5103bae6e4881f480d4b0f6d2efb95a5fab97862a78a895b]
- Quality gates are built in: Critic reviews plans, Code Reviewer gates code before QA and can reject, Security audits at any phase, and DevOps releases only with explicit user approval. [@claim:clm_3dcf52e09a293b8a48971a00354ec04249984a3828ce5ba846db54352935535e]
- Repository development practice: contributions are welcome, and the repo runs an automatic markdownlint-cli2 check in GitHub Actions on pushes and PRs touching .md files. [@claim:clm_5f93700e454a8c7c3057b9ade14a0d7a2d64465d9cee84ea03c38bff10212241]
- The repo defines 13 specialized agents, each owning one workflow part: Roadmap, Planner, Analyst, Architect, Critic, Security, Implementer, Code Reviewer, QA, UAT, DevOps, Retrospective, and ProcessImprovement. [@claim:clm_706d9884ee617657335128d85a1f4bcc79d5a616e3d2e18d1f685c75f9bec8b3]
- Agents carry explicit constraints, e.g. Planner plans without writing code, Implementer follows plans without redesigning, and Security produces findings without implementing remediations. [@claim:clm_7d0a4d51754cffb43ef8242451bbea844e0f8ee13d0c0263675dd5b84fe91387]
- The workflow is document-driven: agents write Markdown artifacts into agent-output/ subfolders (planning, analysis, security, qa, etc.) with sequential NNN naming, status fields, and closure into closed/ subfolders. [@claim:clm_9e4410ad90882b3d6192781296375d23fbf410dc5b0200c8dbaa57a4f53ac63c]
- Agent definitions are Markdown files (e.g. planner.agent.md, security.agent.md) under vs-code-agents/, intended to be copied into a project's .github/agents/ directory or installed at the VS Code user-profile level. [@claim:clm_9f62af18ad3c6241793e9bc91980badc26a08408c2569ca3e7d20990df0bcc6b]
- Flowbaby reportedly governs memory usage and evaluation limits for these agents, suggesting an evaluation mechanism exists in the memory layer, though no benchmark results appear in the evidence. [@claim:clm_a02e28628bcd81723183da7836797d2924630366d60299a1cd32a9ad291dd481]
- Requirements are VS Code with GitHub Copilot; for memory, the Flowbaby extension plus Python 3.10+. The README states these agents require Flowbaby to function correctly. [@claim:clm_aa4dba30575a6c1bb0b0b7b2e501bd57143ab28e568cae9e4f32242143ca8125]
- Agents are invoked in VS Code Copilot Chat by selecting them from the agents dropdown (not with the @ symbol), or optionally via GitHub Copilot CLI with commands like copilot --agent planner. [@claim:clm_baeefc3cbcbc2ad83071b9f0d2480ce8957ee388e2d4ca2c0cbb8b7208df2804]
- A documented upstream Copilot CLI bug means user-level agents in ~/.copilot/agents/ are not loaded; the recommended workaround is per-repository .github/agents/ placement. [@claim:clm_cae3cfe55c559b186903c08b6189c994d9735e8c2dce2e5d4d17e3109b192fb2]
- Flowbaby provides workspace-scoped long-term memory in a local knowledge graph with hybrid graph-vector search; the README states agents fall back to stateless behavior without it. [@claim:clm_d80b7a6681aa592db734a8270c04c10e9c38de0218351736265dd54ad01d815e]
- Agents hand off via a structured template (source agent, artifact path, status, key context, recommended action), and Planner, Implementer, QA, Analyst, and Security document invoking each other as scoped subagents. [@claim:clm_e18849a789eb2578ecce0e8b4b3f79970a93aedf86f24f3afaca745cf57e63c5]
- A typical pipeline runs Roadmap → Planner → Analyst/Architect/Security/Critic → Implementer → Code Reviewer → QA → UAT → DevOps, with documented patterns including an investigation branch and a security gate. [@claim:clm_f535595cd8fc0e62b71d6a72a3d7aff31963dd92152389a291227802bd52296f]
<!-- rcw:end owner=source:src_899d0b0aedac560ba5cec6025bf1724c block=evidence -->

## Researcher notes

