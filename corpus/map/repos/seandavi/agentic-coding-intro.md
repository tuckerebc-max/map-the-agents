# seandavi/agentic-coding-intro

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f3a290d2df43 @ 88727176f78e91bf

## Summary (orientation draft, not independently verified)

The repository is a single-document educational handout (README.md) introducing agentic coding tools, primarily Google Antigravity, to developers already comfortable with R or Python. It covers concepts (tokens, context windows, model-vs-agent), practical habits (Markdown instruction files, context management), and a hello-world exercise. Evidence coverage: 141 of 211 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (5 claim(s)):
  - [observation/documented] The document's stated tool is Google Antigravity, described as Google's agentic development platform where an agent can plan, edit files, run commands, and drive a browser; the official download link is provided. -- evidence: [README.md#L5-L5](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L5-L5)
  - [observation/documented] The handout teaches a conceptual distinction between the LLM (reasoning engine) and the agentic framework layer, which supplies the plan/act/observe/revise loop, tool routing, session memory, and permission guardrails. -- evidence: [README.md#L217-L217](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L217-L217), [README.md#L251-L255](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L251-L255), [README.md#L215-L215](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L215-L215)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The title deliberately strikes through 'Gemini CLI' to illustrate that specific tools change within months, so the handout emphasizes slowly-changing concepts like agents, context, tokens, and file-based habits. -- evidence: [README.md#L7-L7](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L7-L7)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The handout recommends keeping broadly applicable facts in one stable instruction file while moving task-specific procedures into skills or separate documents that load on demand, to conserve context budget. -- evidence: [README.md#L394-L394](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L394-L394), [README.md#L384-L385](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L384-L385), [README.md#L391-L392](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L391-L392)
- interfaces (1 claim(s)):
  - [observation/documented] The handout describes MCP (Model Context Protocol) as an open standard for connecting AI applications to external tools and data, letting agents reach beyond the local filesystem to services like GitHub or databases. -- evidence: [README.md#L312-L312](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L312-L312), [README.md#L321-L321](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L321-L321), [README.md#L317-L317](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L317-L317)
- memory-state (1 claim(s)):
  - [observation/documented] The document advocates Markdown files as project memory and decision records, noting Antigravity's Artifacts and Knowledge Base and its reported automatic pickup of AGENTS.md, GEMINI.md, and CLAUDE.md instruction files. -- evidence: [README.md#L331-L331](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L331-L331), [README.md#L335-L335](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L335-L335)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Antigravity is a downloadable desktop application for macOS, Windows, and Linux requiring sign-in with a Google account; it is model-flexible, with Gemini 3 Pro, Claude Sonnet 4.5, and open models mentioned as options. -- evidence: [README.md#L418-L418](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L418-L418), [README.md#L413-L416](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L413-L416), [README.md#L406-L406](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L406-L406)
- limitations (1 claim(s)):
More evidence: [full detail](agentic-coding-intro.detail.md)

Metadata and full claim list: [full detail](agentic-coding-intro.detail.md)
Human notes ([notes](agentic-coding-intro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
