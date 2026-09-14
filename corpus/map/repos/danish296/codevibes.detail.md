# danish296/codevibes -- full detail

[Back to orientation](codevibes.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/danish296/codevibes/37b9e91bf153f48cc27562f49cc975f9138ea313/7ec2bc852091d048.json](../../../wiki/dossiers/danish296/codevibes/37b9e91bf153f48cc27562f49cc975f9138ea313/7ec2bc852091d048.json)

## specifications (1 claim(s))

- [observation/documented] CodeVibes is described as an AI code-analysis tool that scans GitHub repositories to identify security vulnerabilities, bugs and performance issues, and code-quality improvements, producing a quantifiable Vibe Score. -- evidence: [README.md#L7-L7](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L7-L7) (`clm_8d271d090582ac2472bc8f628e6885da303353c3a64a3885f0942be99010b34e`)

## components (1 claim(s))

- [observation/documented] The backend is documented to include a deepseekService for AI prompts and streaming, a githubService for repo fetching, SQLite database setup, and Winston logging. -- evidence: [README.md#L259-L291](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L259-L291) (`clm_9df7ef55036efed9003eb43519aee984bd495b90250c00770c57995238027f74`)

## design-choices (2 claim(s))

- [observation/documented] Analysis uses a three-tier priority system: P1 security files (e.g. .env, auth, config) first, then P2 core logic (controllers, services, models), then P3 quality files (tests, utils, other files). -- evidence: [README.md#L139-L144](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L139-L144), [README.md#L123-L130](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L123-L130), [README.md#L121-L121](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L121-L121), [README.md#L132-L137](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L132-L137) (`clm_73d477074afcf70f55ad1f6ee6c95790d4bd188acba5fe29b121b324a4e5af38`)
- [observation/documented] Backend configuration is documented via a .env file listing PORT, DEEPSEEK_API_KEY, GITHUB_TOKEN, DB_PATH, DEEPSEEK_MODEL (deepseek-chat or deepseek-reasoner), and ALLOWED_ORIGINS. -- evidence: [README.md#L245-L246](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L245-L246), [README.md#L241-L241](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L241-L241), [README.md#L249-L253](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L249-L253) (`clm_0c6c30e55692970883ce1578d29e6c9acfef828b6e66566a0073cae02f34a814`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions follow a fork-and-branch flow — fork, create a feature branch, commit, push, and open a Pull Request; contributions are welcome. -- evidence: [README.md#L398-L402](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L398-L402), [README.md#L396-L396](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L396-L396) (`clm_5b4f072f7b56aa75b414e51acd3d7d10d7f1aa0b2c04b121f2b3ac34dad98797`)
- [observation/documented] Repository development practice: local setup involves cloning, running npm install in both root and codevibes-backend, copying .env.example to .env, and starting backend and frontend dev servers in separate terminals. -- evidence: [README.md#L236-L237](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L236-L237), [README.md#L228-L228](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L228-L228), [README.md#L224-L225](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L224-L225), [README.md#L220-L221](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L220-L221), [README.md#L233-L233](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L233-L233) (`clm_85c16c7d1b1e98971b1c0c6b365ac722200ba130fc0c35900bf4721551c34c29`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Documented REST endpoints include POST /api/analyze, GET /api/analyze/stream (SSE), GET/POST /api/history, DELETE /api/history/:id, GET /api/github/repos, and POST /api/github/validate. -- evidence: [README.md#L314-L317](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L314-L317), [README.md#L306-L310](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L306-L310), [README.md#L299-L302](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L299-L302) (`clm_53b268649b44ec1f4ef6d672edfb929a06d99355c3ab4053e4f7a00d0fe4c0b1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The documented workflow: user submits a repo URL, backend fetches the GitHub file tree, categorizes files by priority, streams file contents to DeepSeek, and pushes issues to the frontend in real time via SSE before computing a final report. -- evidence: [README.md#L112-L115](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L112-L115), [README.md#L98-L99](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L98-L99), [README.md#L101-L101](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L101-L101), [README.md#L95-L96](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L95-L96), [README.md#L103-L110](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L103-L110) (`clm_4f0a751aee74d088efc2d28e6bff1b5d774e5442ea033d19493dc409c309d7b1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The product computes a 0-100 Vibe Score from issue severity weights (CRITICAL 25, HIGH 15, MEDIUM 5, LOW 1) subtracted from 100, with labeled ranges from Excellent (90-100) to Critical (0-49). -- evidence: [README.md#L323-L330](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L323-L330), [README.md#L335-L337](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L335-L337), [README.md#L332-L333](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L332-L333), [README.md#L339-L344](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L339-L344) (`clm_7293d550ae309b7eacce94f276e682d04f467bb62f63adae1396f915165aada5`)

## dependencies (2 claim(s))

- [observation/documented] The documented stack includes React 18 + Vite, TailwindCSS, Zustand, Node.js + Express, Better-SQLite3, tsx, the DeepSeek API, and Octokit as the GitHub API client. -- evidence: [README.md#L195-L205](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L195-L205) (`clm_b4a7fd179699d353bc6c1f1bda31beaa04026bc1078795cd6630b7021fe189ab`)
- [observation/documented] Running the tool requires Node.js v18+ and a DeepSeek API key; a GitHub token is optional and only needed for private repositories. -- evidence: [README.md#L212-L214](https://github.com/danish296/codevibes/blob/37b9e91bf153f48cc27562f49cc975f9138ea313/README.md#L212-L214) (`clm_1d0115cde8a8d9dc09b9a278e865f8d756221a896c54850efc5691f7e383774c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

