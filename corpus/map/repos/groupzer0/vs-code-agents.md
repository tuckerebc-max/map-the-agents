# groupzer0/vs-code-agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c28eb5fe2cd8 @ eb89d19d5a12c1be

## Summary (orientation draft, not independently verified)

The repository ships a set of Markdown-defined GitHub Copilot custom agents (Flowbaby Agent Team) forming a document-driven multi-agent development workflow, with optional Flowbaby-based persistent memory. Evidence is documentation-only (README and deep-dive guide); no runtime code is shown. Evidence coverage: 156 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The repo defines 13 specialized agents, each owning one workflow part: Roadmap, Planner, Analyst, Architect, Critic, Security, Implementer, Code Reviewer, QA, UAT, DevOps, Retrospective, and ProcessImprovement. -- evidence: [README.md#L177-L200](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L177-L200), [README.md#L25-L39](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L25-L39)
  - [observation/documented] Agents carry explicit constraints, e.g. Planner plans without writing code, Implementer follows plans without redesigning, and Security produces findings without implementing remediations. -- evidence: [AGENTS-DEEP-DIVE.md#L35-L47](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L35-L47), [README.md#L41-L41](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L41-L41)
- components (2 claim(s)):
  - [observation/documented] Agent definitions are Markdown files (e.g. planner.agent.md, security.agent.md) under vs-code-agents/, intended to be copied into a project's .github/agents/ directory or installed at the VS Code user-profile level. -- evidence: [README.md#L177-L200](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L177-L200), [README.md#L55-L63](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L55-L63), [README.md#L65-L65](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L65-L65)
  - [observation/documented] A skills system provides modular, on-demand instruction sets including memory-contract, analysis-methodology, security-patterns, testing-patterns, release-procedures, and cross-repo-contract, placed in .claude/skills/ (stable) or .github/skills/ (Insiders). -- evidence: [README.md#L263-L263](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L263-L263), [README.md#L265-L277](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L265-L277), [README.md#L279-L281](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L279-L281)
- design-choices (2 claim(s)):
  - [observation/documented] The workflow is document-driven: agents write Markdown artifacts into agent-output/ subfolders (planning, analysis, security, qa, etc.) with sequential NNN naming, status fields, and closure into closed/ subfolders. -- evidence: [AGENTS-DEEP-DIVE.md#L230-L240](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L230-L240), [AGENTS-DEEP-DIVE.md#L53-L64](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L53-L64), [README.md#L148-L148](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L148-L148), [AGENTS-DEEP-DIVE.md#L184-L186](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L184-L186)
  - [observation/documented] Quality gates are built in: Critic reviews plans, Code Reviewer gates code before QA and can reject, Security audits at any phase, and DevOps releases only with explicit user approval. -- evidence: [README.md#L151-L151](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L151-L151), [AGENTS-DEEP-DIVE.md#L35-L47](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L35-L47), [AGENTS-DEEP-DIVE.md#L157-L160](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L157-L160)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcome, and the repo runs an automatic markdownlint-cli2 check in GitHub Actions on pushes and PRs touching .md files. -- evidence: [README.md#L325-L325](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L325-L325), [README.md#L332-L332](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L332-L332)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Agents are invoked in VS Code Copilot Chat by selecting them from the agents dropdown (not with the @ symbol), or optionally via GitHub Copilot CLI with commands like copilot --agent planner. -- evidence: [README.md#L77-L77](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L77-L77), [README.md#L83-L84](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L83-L84), [README.md#L104-L106](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/README.md#L104-L106)
  - [observation/documented] Flowbaby exposes agent tools #flowbabyStoreSummary and #flowbabyRetrieveMemory, used with structured JSON payloads carrying query, decisions, rationale, and artifact metadata. -- evidence: [AGENTS-DEEP-DIVE.md#L376-L379](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L376-L379), [AGENTS-DEEP-DIVE.md#L406-L421](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L406-L421), [AGENTS-DEEP-DIVE.md#L308-L312](https://github.com/groupzer0/vs-code-agents/blob/c28eb5fe2cd87a362cc6fafefe3926712b0be482/AGENTS-DEEP-DIVE.md#L308-L312)
- memory-state (2 claim(s)):
More evidence: [full detail](vs-code-agents.detail.md)

Metadata and full claim list: [full detail](vs-code-agents.detail.md)
Human notes ([notes](vs-code-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
