# ikamensh/kodo -- full detail

[Back to orientation](kodo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ikamensh/kodo/51aebbfe5a309715543259edbe207ae151cc33ad/f4e77a0c0e2eb4e7.json](../../../wiki/dossiers/ikamensh/kodo/51aebbfe5a309715543259edbe207ae151cc33ad/f4e77a0c0e2eb4e7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The default team comprises an orchestrator plus architect, worker_smart, worker_fast, tester, and tester_browser agents, each with a distinct role such as code survey, implementation, testing, or browser-based UI testing. -- evidence: [README.md#L272-L280](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L272-L280) (`clm_623b7dbe686e15f9dacd4f08353698857d9c55f67d533f1d1a90efd470a9956c`)

## design-choices (4 claim(s))

- [observation/documented] An API model is recommended as orchestrator over CLI coding tools because CLI agents tend to write code, micromanage, or go off-script, while a plain API model stays in a coordinator role that delegates. -- evidence: [README.md#L143-L143](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L143-L143) (`clm_41f22382a9a0abed077c9c38b70d07c54f6bc7dd173ccd3eea04958a9013a724`)
- [observation/documented] Custom teams are defined via team.json with lookup order project-level .kodo/team.json then user-level ~/.kodo/teams/{name}.json; agent fields include backend, model, description, system_prompt, max_turns (default 15), timeout_s, chrome, and fallback_model. -- evidence: [README.md#L354-L354](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L354-L354), [README.md#L313-L315](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L313-L315), [README.md#L319-L350](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L319-L350), [README.md#L311-L311](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L311-L311) (`clm_3b2b5779f156ba13fabcabf542fc58bc8858d72c0a110e9eb05e516447c56dcd`)
- [observation/documented] Cost tracking separates an API bucket of real pay-per-token spend (e.g. ~$0.13/run for a Gemini Flash orchestrator) from a Virtual bucket showing what subscription-covered worker usage would have cost, which is not actually charged. -- evidence: [README.md#L360-L363](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L360-L363), [README.md#L365-L365](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L365-L365) (`clm_da0fb545623e3264343a07cf90865aea83a308201e8369d02bc1b919c9d84a8f`)
- [observation/documented] Four effort levels (low, standard, high, max) scale both orchestrator behavior and verification strictness, from basic test-passing checks up to skeptical rejection of technically correct but mediocre work. -- evidence: [README.md#L286-L291](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L286-L291) (`clm_0fecf4359da23e32d684e4a579cc57934aef67c3cd9f8f0ceb129133c28ab3e7`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md documents mocked end-to-end smoke scripts (e.g. scripts/smoke_test_cli.py, run_cli_mocked.py, smoke_test_resume.py) verifying CLI, resume, improve, and interactive flows without API keys, with the full suite run via `uv run pytest tests/` (464 passed, 1 xfailed). -- evidence: [AGENTS.md#L7-L14](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/AGENTS.md#L7-L14), [AGENTS.md#L33-L33](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/AGENTS.md#L33-L33) (`clm_df8a77f656638d0e8c4c86211efa84ff30eeac5391cc6c06472d2fd3587c2cfb`)
- [observation/documented] Repository development practice: CLAUDE.md requires autospec=True on all unittest.mock.patch calls (enforced by tests/test_autospec_enforcement.py), spec=RealClass or create_autospec for bare mocks, and a `# noqa: autospec` escape hatch. -- evidence: [CLAUDE.md#L54-L56](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/CLAUDE.md#L54-L56) (`clm_464912d44bf7b9c721b93021d9c35ca3414f9ad0617ec5c2507a9af4dc405b0c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Configuration flags include --team (full default, quick, test), --exchanges, --cycles, --orchestrator (api default, or claude-code/gemini-cli/codex/cursor), --orchestrator-model, --effort, --skip-intake, --auto-refine, --json, and --no-auto-commit. -- evidence: [README.md#L217-L221](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L217-L221), [README.md#L203-L208](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L203-L208), [README.md#L210-L215](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L210-L215) (`clm_2c596ed9227d9f5f5c530f96af05829cf110889f277b6360f26c2d60f7777ec9`)

## memory-state (2 claim(s))

- [observation/documented] Runs are stored under ~/.kodo/runs/ and can be resumed by ID or as the latest incomplete run; test-mode coverage tracking persists in .kodo/test-coverage.md so repeated runs skip previously tested features. -- evidence: [README.md#L235-L235](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L235-L235), [README.md#L170-L172](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L170-L172), [README.md#L371-L371](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L371-L371) (`clm_2f529893cb7f1f3f2aee96aedf55c04757de922a1d87e633f63feb1f0d15bfdb`)
- [observation/documented] A session is a stateful conversation with a backend that tracks token usage and supports reset; an agent combines a prompt, session, and turn budget, invoked as agent.run(task, project_dir). -- evidence: [README.md#L300-L307](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L300-L307) (`clm_5b9b953b9bd2c7cfa9e70e584fb4a80b7c78136bb943a641d66181de05fb3f49`)

## orchestration (2 claim(s))

- [observation/documented] An orchestrator LLM delegates to a team of agents via tool calls; two implementations are described: ClaudeCodeOrchestrator (running on Claude Code with agents as MCP tools) and ApiOrchestrator on the Anthropic or Gemini API. -- evidence: [README.md#L300-L307](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L300-L307) (`clm_0aeddd577efa6b777ee8fe7a5ce929cadb80943e8aaba05124e061d84b71abc8`)
- [observation/documented] Work is structured hierarchically: a cycle is one unit of orchestrated work, a run spans multiple cycles with summaries bridging context, and stages are independently verifiable plan pieces that run sequentially or in parallel git worktrees. -- evidence: [README.md#L300-L307](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L300-L307) (`clm_5ef96e5a3b53d406b86cec58595d15fa1ed35fa9663172307e5e075fb1733d63`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents run with full permissions in bypassPermissions mode; they primarily work in the project directory but can access any file on the system, so users are advised to have a git commit or backup before launching. -- evidence: [README.md#L224-L224](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L224-L224) (`clm_208b61ed0cfb30564a8848adcf0a809b6a51df3395da1f07df1d1157d4abc78b`)

## evaluation (1 claim(s))

- [observation/documented] A published 100-task head-to-head benchmark using the same underlying model (Cursor composer-1.5) reports that adding Kodo's orchestration layer solves 24% more real-world GitHub issues, with methodology and interactive results available online. -- evidence: [README.md#L25-L25](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L25-L25) (`clm_767ffd831c3bf3500fbbbb734af9e9237b98bddcf7c9dcca446fe9507e042743`)

## dependencies (2 claim(s))

- [observation/documented] Kodo targets Python 3.13+, is installed with uv (uv tool install kodo-agent), and requires at least one agent backend, with Claude Code plus one fast backend (Cursor, Codex, or Gemini CLI) recommended. -- evidence: [README.md#L124-L124](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L124-L124), [README.md#L98-L98](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L98-L98), [README.md#L110-L113](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L110-L113), [README.md#L135-L135](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L135-L135), [README.md#L1-L15](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L1-L15) (`clm_0b89e239530f1af647e39fffff8a078322a46d63f022e131daf82699b93ffb2c`)
- [observation/documented] The API orchestrator expects a GOOGLE_API_KEY (Gemini, described as recommended) or ANTHROPIC_API_KEY (Claude alternative) set in .env or the environment. -- evidence: [README.md#L137-L141](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L137-L141) (`clm_69b007aad2bebb7a2f8eba8fe1737089ff6c55df340bd9a60a66e38efe552678`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

