# groupzer0/vs-code-agents -- full detail

[Back to orientation](vs-code-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/groupzer0/vs-code-agents/c28eb5fe2cd87a362cc6fafefe3926712b0be482/eb89d19d5a12c1be.json](../../../wiki/dossiers/groupzer0/vs-code-agents/c28eb5fe2cd87a362cc6fafefe3926712b0be482/eb89d19d5a12c1be.json)

## specifications (2 claim(s))

- [observation/documented] The repo defines 13 specialized agents, each owning one workflow part: Roadmap, Planner, Analyst, Architect, Critic, Security, Implementer, Code Reviewer, QA, UAT, DevOps, Retrospective, and ProcessImprovement. -- evidence: [README.md#L177-L200](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L177-L200), [README.md#L25-L39](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L25-L39) (`clm_706d9884ee617657335128d85a1f4bcc79d5a616e3d2e18d1f685c75f9bec8b3`)
- [observation/documented] Agents carry explicit constraints, e.g. Planner plans without writing code, Implementer follows plans without redesigning, and Security produces findings without implementing remediations. -- evidence: [AGENTS-DEEP-DIVE.md#L35-L47](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L35-L47), [README.md#L41-L41](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L41-L41) (`clm_7d0a4d51754cffb43ef8242451bbea844e0f8ee13d0c0263675dd5b84fe91387`)

## components (2 claim(s))

- [observation/documented] Agent definitions are Markdown files (e.g. planner.agent.md, security.agent.md) under vs-code-agents/, intended to be copied into a project's .github/agents/ directory or installed at the VS Code user-profile level. -- evidence: [README.md#L177-L200](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L177-L200), [README.md#L55-L63](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L55-L63), [README.md#L65-L65](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L65-L65) (`clm_9f62af18ad3c6241793e9bc91980badc26a08408c2569ca3e7d20990df0bcc6b`)
- [observation/documented] A skills system provides modular, on-demand instruction sets including memory-contract, analysis-methodology, security-patterns, testing-patterns, release-procedures, and cross-repo-contract, placed in .claude/skills/ (stable) or .github/skills/ (Insiders). -- evidence: [README.md#L263-L263](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L263-L263), [README.md#L265-L277](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L265-L277), [README.md#L279-L281](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L279-L281) (`clm_2cd3fbab82a7579f5103bae6e4881f480d4b0f6d2efb95a5fab97862a78a895b`)

## design-choices (2 claim(s))

- [observation/documented] The workflow is document-driven: agents write Markdown artifacts into agent-output/ subfolders (planning, analysis, security, qa, etc.) with sequential NNN naming, status fields, and closure into closed/ subfolders. -- evidence: [AGENTS-DEEP-DIVE.md#L230-L240](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L230-L240), [AGENTS-DEEP-DIVE.md#L53-L64](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L53-L64), [README.md#L148-L148](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L148-L148), [AGENTS-DEEP-DIVE.md#L184-L186](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L184-L186) (`clm_9e4410ad90882b3d6192781296375d23fbf410dc5b0200c8dbaa57a4f53ac63c`)
- [observation/documented] Quality gates are built in: Critic reviews plans, Code Reviewer gates code before QA and can reject, Security audits at any phase, and DevOps releases only with explicit user approval. -- evidence: [README.md#L151-L151](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L151-L151), [AGENTS-DEEP-DIVE.md#L35-L47](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L35-L47), [AGENTS-DEEP-DIVE.md#L157-L160](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L157-L160) (`clm_3dcf52e09a293b8a48971a00354ec04249984a3828ce5ba846db54352935535e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcome, and the repo runs an automatic markdownlint-cli2 check in GitHub Actions on pushes and PRs touching .md files. -- evidence: [README.md#L325-L325](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L325-L325), [README.md#L332-L332](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L332-L332) (`clm_5f93700e454a8c7c3057b9ade14a0d7a2d64465d9cee84ea03c38bff10212241`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Agents are invoked in VS Code Copilot Chat by selecting them from the agents dropdown (not with the @ symbol), or optionally via GitHub Copilot CLI with commands like copilot --agent planner. -- evidence: [README.md#L77-L77](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L77-L77), [README.md#L83-L84](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L83-L84), [README.md#L104-L106](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L104-L106) (`clm_baeefc3cbcbc2ad83071b9f0d2480ce8957ee388e2d4ca2c0cbb8b7208df2804`)
- [observation/documented] Flowbaby exposes agent tools #flowbabyStoreSummary and #flowbabyRetrieveMemory, used with structured JSON payloads carrying query, decisions, rationale, and artifact metadata. -- evidence: [AGENTS-DEEP-DIVE.md#L376-L379](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L376-L379), [AGENTS-DEEP-DIVE.md#L406-L421](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L406-L421), [AGENTS-DEEP-DIVE.md#L308-L312](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L308-L312) (`clm_2ce1f21009b619978b1eddf0fb0832d36923ccddc3b7966336c69d5a5ae89177`)

## memory-state (2 claim(s))

- [observation/documented] All agents load a memory-contract skill governing Flowbaby usage: retrieve before decisions, store at value boundaries (including every 5 turns), use specific hypothesis-driven queries, and acknowledge retrieved memory. -- evidence: [AGENTS-DEEP-DIVE.md#L391-L395](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L391-L395), [AGENTS-DEEP-DIVE.md#L358-L358](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L358-L358), [AGENTS-DEEP-DIVE.md#L365-L368](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L365-L368) (`clm_678bd2ab1b9bc91e0548d625a3db570020da99d2200002d7c1043bbf8ffb8f00`)
- [observation/documented] Flowbaby provides workspace-scoped long-term memory in a local knowledge graph with hybrid graph-vector search; the README states agents fall back to stateless behavior without it. -- evidence: [AGENTS-DEEP-DIVE.md#L306-L306](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L306-L306), [README.md#L90-L90](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L90-L90), [AGENTS-DEEP-DIVE.md#L308-L312](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L308-L312) (`clm_d80b7a6681aa592db734a8270c04c10e9c38de0218351736265dd54ad01d815e`)

## orchestration (2 claim(s))

- [observation/documented] A typical pipeline runs Roadmap → Planner → Analyst/Architect/Security/Critic → Implementer → Code Reviewer → QA → UAT → DevOps, with documented patterns including an investigation branch and a security gate. -- evidence: [AGENTS-DEEP-DIVE.md#L79-L90](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L79-L90), [AGENTS-DEEP-DIVE.md#L129-L134](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L129-L134), [README.md#L124-L126](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L124-L126), [AGENTS-DEEP-DIVE.md#L148-L153](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L148-L153) (`clm_f535595cd8fc0e62b71d6a72a3d7aff31963dd92152389a291227802bd52296f`)
- [observation/documented] Agents hand off via a structured template (source agent, artifact path, status, key context, recommended action), and Planner, Implementer, QA, Analyst, and Security document invoking each other as scoped subagents. -- evidence: [AGENTS-DEEP-DIVE.md#L289-L295](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L289-L295), [README.md#L318-L321](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L318-L321), [AGENTS-DEEP-DIVE.md#L297-L298](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L297-L298) (`clm_e18849a789eb2578ecce0e8b4b3f79970a93aedf86f24f3afaca745cf57e63c5`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] Flowbaby reportedly governs memory usage and evaluation limits for these agents, suggesting an evaluation mechanism exists in the memory layer, though no benchmark results appear in the evidence. -- evidence: [README.md#L98-L98](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L98-L98) (`clm_a02e28628bcd81723183da7836797d2924630366d60299a1cd32a9ad291dd481`)

## dependencies (1 claim(s))

- [observation/documented] Requirements are VS Code with GitHub Copilot; for memory, the Flowbaby extension plus Python 3.10+. The README states these agents require Flowbaby to function correctly. -- evidence: [README.md#L88-L88](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L88-L88), [README.md#L338-L339](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L338-L339) (`clm_aa4dba30575a6c1bb0b0b7b2e501bd57143ab28e568cae9e4f32242143ca8125`)

## limitations (1 claim(s))

- [observation/documented] A documented upstream Copilot CLI bug means user-level agents in ~/.copilot/agents/ are not loaded; the recommended workaround is per-repository .github/agents/ placement. -- evidence: [README.md#L108-L108](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L108-L108) (`clm_cae3cfe55c559b186903c08b6189c994d9735e8c2dce2e5d4d17e3109b192fb2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

