# trafficguard/typedai -- full detail

[Back to orientation](typedai.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/trafficguard/typedai/34139aec65bb70f7062cf7f92667c11ffde4fcb1/05c891535de024b4.json](../../../wiki/dossiers/trafficguard/typedai/34139aec65bb70f7062cf7f92667c11ffde4fcb1/05c891535de024b4.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The platform ships software-developer agents including a Code Editing Agent with a compile/lint/test/fix loop, a ticket-to-PR Software Engineer Agent, and a Code Review agent that posts comments on GitLab merge requests. -- evidence: [README.md#L67-L83](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L67-L83) (`clm_c29bf7be5151f0a56bb06cec4a346be8af8ee37c52493505bab0f8d228727d1e`)
- [observation/documented] TypedAI includes two autonomous agent types, XML and CodeGen, which apply reasoning to break a user request into a plan executed via available function calls. -- evidence: [docs/docs/agent-concepts.md#L15-L16](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L15-L16) (`clm_766a90d31c7c12b46c3081a71ad7831352cb5f6c10049cf9e9da8ee46705e65d`)

## design-choices (3 claim(s))

- [observation/documented] LLM function-calling schemas are auto-generated from a `@func` decorator on class methods, avoiding duplicate schema definitions via zod or JSON. -- evidence: [README.md#L215-L216](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L215-L216) (`clm_0491418b123b418f81c8ce4393fe799a31e29bc83a275a6a0e65c38a0ecb4749`)
- [observation/documented] Agent state, current user, tool configuration, and default LLMs are looked up through Node's AsyncLocalStorage, requiring agent code to run within an AsyncLocalStorage context. -- evidence: [docs/docs/agent-concepts.md#L29-L30](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L29-L30), [docs/docs/agent-concepts.md#L32-L34](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L32-L34) (`clm_3eb6d4ca2a8badd2957a211516b4279498f93740e4854e1d062cd6c256a282c6`)
- [observation/documented] Each agent is configured with three LLMs for easy, medium, and hard tasks, making it simple to swap in different models at a given capability level. -- evidence: [docs/docs/agent-concepts.md#L67-L67](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L67-L67) (`clm_05c519830705cc1537f1c7ef1328998a617ceca753bdafdff6ee153c1d73e80c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors set up the project with `./bin/setup` and run it locally with `./bin/serve`. -- evidence: [docs/README.md#L5-L5](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/README.md#L5-L5), [docs/README.md#L9-L9](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/README.md#L9-L9) (`clm_6da9f1e360428a77c4a1d5387cd55ac2a07caafb91a9ddcb0be5d510e852a138`)
- [observation/documented] Repository development practice: with `DATABASE_TYPE=postgres` set, a Postgres Docker container auto-starts during app-context initialization, skipping when the host is remote, inside Docker, or in CI. -- evidence: [docs/AUTO_START_POSTGRES.md#L9-L9](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/AUTO_START_POSTGRES.md#L9-L9), [docs/AUTO_START_POSTGRES.md#L13-L23](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/AUTO_START_POSTGRES.md#L13-L23), [docs/AUTO_START_POSTGRES.md#L68-L75](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/AUTO_START_POSTGRES.md#L68-L75) (`clm_72b574060ff1a72f14216f97d0ee5272b79fb795f5150991d32d8891a227163a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] TypedAI offers both CLI and Web UI interfaces, and the `ai` wrapper script runs locally while `aid` runs in Docker for isolation; both expose CLI agents including a codeAgent for autonomous code editing. -- evidence: [README.md#L50-L50](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L50-L50), [README.md#L25-L37](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L25-L37) (`clm_4a9ac38de623b2c358f4a047beb48bcc4adf64ca173efa0729db226f8ad7e950`)
- [observation/documented] The CLI supports commands such as `ai query`, `ai code`, and `ai research` for automation and development workflows. -- evidence: [README.md#L45-L48](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L45-L48) (`clm_b00a9ed204502c57d080f8da548ec66dbef7a9ea20e7597077d9b2eb1bc80248`)
- [observation/documented] Code review guidelines are defined as XML files in `resources/codeReview` against a schema there, and reviews can be filtered by file extension or required diff text to reduce LLM cost. -- evidence: [docs/CODE_REVIEW.md#L10-L10](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/CODE_REVIEW.md#L10-L10), [docs/CODE_REVIEW.md#L12-L14](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/CODE_REVIEW.md#L12-L14) (`clm_11b1fa1c83c321dd2e4487cd378a1267c521d992e516cb86e1dd706742a83516`)
- [observation/documented] Enabling the GitLab code-review feature requires configuring webhooks at project or group level pointing to `<your-typedai-domain>/gitlab/v1/webhook`. -- evidence: [docs/CODE_REVIEW.md#L74-L75](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/CODE_REVIEW.md#L74-L75), [docs/CODE_REVIEW.md#L72-L72](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/CODE_REVIEW.md#L72-L72), [docs/CODE_REVIEW.md#L77-L78](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/CODE_REVIEW.md#L77-L78) (`clm_18a3e13280227d4af4f160adbdae8cd9460e49d6142f997d710ba609328b8127`)

## memory-state (2 claim(s))

- [observation/documented] Workflows run with a persisted agent context whose state is saved as 'completed' or 'error', so agent actions can be reviewed and resumed in the UI. -- evidence: [docs/docs/agent-concepts.md#L36-L65](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L36-L65) (`clm_762b2dc5bb00d8cb6235e4464529486c76f8f8eb703b56ce2fe3d147ece003e7`)
- [observation/documented] The Postgres schema auto-created at startup includes tables for users, chats, agent contexts and iterations, LLM call logs, prompt revisions, function cache, and code review configs. -- evidence: [docs/POSTGRES_SETUP.md#L117-L117](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/POSTGRES_SETUP.md#L117-L117), [docs/POSTGRES_SETUP.md#L121-L133](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/POSTGRES_SETUP.md#L121-L133) (`clm_77fdf0304facd5cef4595e2462448118cb2795583bfd538c3d46b35276f440f9`)

## orchestration (1 claim(s))

- [observation/documented] The project distinguishes workflow agents, whose control flow is defined in code with LLM results driving conditionals, from autonomous agents where the LLM directs its own process and tool usage. -- evidence: [docs/docs/agent-concepts.md#L24-L25](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L24-L25), [docs/docs/agent-concepts.md#L7-L11](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L7-L11) (`clm_7af6d6a0c7b90cf27841ff612ab7cd533dbcf9333b9ff0eb2aae92d9437168dc`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents use callable tool integrations such as Filesystem, Jira, Slack, Perplexity, Google Cloud, GitLab, and GitHub, with configurable human-in-the-loop settings for budget control and agent-initiated questions. -- evidence: [README.md#L25-L37](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L25-L37), [README.md#L56-L61](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L56-L61) (`clm_bed482c862198f71bab09e481d08ba1b207503be2c338c0037c32ae864023b76`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The platform supports many LLM services including OpenAI, Anthropic (native and Vertex), Gemini, Groq, Fireworks, Together.ai, DeepSeek, Ollama, Cerebras, SambaNova, OpenRouter, and X.ai. -- evidence: [README.md#L25-L37](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L25-L37) (`clm_29b18f76093eeee0104cbc9dab8aefc4a3382ec4e2ea4ceb8c7a5b29b7c5844a`)
- [observation/documented] The project does not use LangChain, and its README claims the platform's scope covers functionality found in LangChain and LangSmith. -- evidence: [README.md#L143-L143](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L143-L143), [README.md#L141-L141](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L141-L141) (`clm_ed7ad4b921c877b74bfb7d6687d3fcb1f73067161cbb60c17d25b6dff93eb37d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] TypedAI is a full-featured platform for developing and running agents, LLM-based workflows, and chatbots, described as the TypeScript-first AI platform for developers. -- evidence: [README.md#L19-L19](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L19-L19), [README.md#L1-L8](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L1-L8) (`clm_5bb70e06102c29ffb76581ec165402521c06b1e784abb115fdddbc899900cf85`)

