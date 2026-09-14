# danish296/codevibes

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 37b9e91bf153 @ 7ec2bc852091d048

## Summary (orientation draft, not independently verified)

CodeVibes is a documented AI code-review tool that scans GitHub repositories via DeepSeek, using a React/Express stack with a three-tier priority scan and a 0-100 Vibe Score. Evidence is README-only; one prior claim overstated the required/optional classification of environment variables and has been revised.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CodeVibes is described as an AI code-analysis tool that scans GitHub repositories to identify security vulnerabilities, bugs and performance issues, and code-quality improvements, producing a quantifiable Vibe Score. -- evidence: [README.md#L7-L7](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] The backend is documented to include a deepseekService for AI prompts and streaming, a githubService for repo fetching, SQLite database setup, and Winston logging. -- evidence: [README.md#L259-L291](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L259-L291)
- design-choices (2 claim(s)):
  - [observation/documented] Analysis uses a three-tier priority system: P1 security files (e.g. .env, auth, config) first, then P2 core logic (controllers, services, models), then P3 quality files (tests, utils, other files). -- evidence: [README.md#L139-L144](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L139-L144), [README.md#L123-L130](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L123-L130), [README.md#L121-L121](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L121-L121), [README.md#L132-L137](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L132-L137)
  - [observation/documented] Backend configuration is documented via a .env file listing PORT, DEEPSEEK_API_KEY, GITHUB_TOKEN, DB_PATH, DEEPSEEK_MODEL (deepseek-chat or deepseek-reasoner), and ALLOWED_ORIGINS. -- evidence: [README.md#L245-L246](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L245-L246), [README.md#L241-L241](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L241-L241), [README.md#L249-L253](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L249-L253)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions follow a fork-and-branch flow — fork, create a feature branch, commit, push, and open a Pull Request; contributions are welcome. -- evidence: [README.md#L398-L402](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L398-L402), [README.md#L396-L396](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L396-L396)
  - [observation/documented] Repository development practice: local setup involves cloning, running npm install in both root and codevibes-backend, copying .env.example to .env, and starting backend and frontend dev servers in separate terminals. -- evidence: [README.md#L236-L237](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L236-L237), [README.md#L228-L228](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L228-L228), [README.md#L224-L225](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L224-L225), [README.md#L220-L221](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L220-L221), [README.md#L233-L233](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L233-L233)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Documented REST endpoints include POST /api/analyze, GET /api/analyze/stream (SSE), GET/POST /api/history, DELETE /api/history/:id, GET /api/github/repos, and POST /api/github/validate. -- evidence: [README.md#L314-L317](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L314-L317), [README.md#L306-L310](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L306-L310), [README.md#L299-L302](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L299-L302)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The documented workflow: user submits a repo URL, backend fetches the GitHub file tree, categorizes files by priority, streams file contents to DeepSeek, and pushes issues to the frontend in real time via SSE before computing a final report. -- evidence: [README.md#L112-L115](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L112-L115), [README.md#L98-L99](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L98-L99), [README.md#L101-L101](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L101-L101), [README.md#L95-L96](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L95-L96), [README.md#L103-L110](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L103-L110)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](codevibes.detail.md)

Metadata and full claim list: [full detail](codevibes.detail.md)
Human notes ([notes](codevibes.notes.md), never overwritten by build)

[Back to map index](../../index.md)
