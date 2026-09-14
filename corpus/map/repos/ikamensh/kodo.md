# ikamensh/kodo

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 51aebbfe5a30 @ f4e77a0c0e2eb4e7

## Summary (orientation draft, not independently verified)

Selected evidence records: The default team comprises an orchestrator plus architect, worker_smart, worker_fast, tester, and tester_browser agents, each with a distinct role such as code survey, implementation, testing, or browser-based UI testing. An orchestrator LLM delegates to a team of agents via tool calls; two implementations are described: ClaudeCodeOrchestrator (running on Claude Code with agents as MCP tools) and ApiOrchestrator on the Anthropic or Gemini API.

## Source coverage

Source coverage (partial): 3 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The default team comprises an orchestrator plus architect, worker_smart, worker_fast, tester, and tester_browser agents, each with a distinct role such as code survey, implementation, testing, or browser-based UI testing. -- evidence: [README.md#L272-L280](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L272-L280)
- design-choices (4 claim(s)):
  - [observation/documented] An API model is recommended as orchestrator over CLI coding tools because CLI agents tend to write code, micromanage, or go off-script, while a plain API model stays in a coordinator role that delegates. -- evidence: [README.md#L143-L143](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L143-L143)
  - [observation/documented] Custom teams are defined via team.json with lookup order project-level .kodo/team.json then user-level ~/.kodo/teams/{name}.json; agent fields include backend, model, description, system_prompt, max_turns (default 15), timeout_s, chrome, and fallback_model. -- evidence: [README.md#L354-L354](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L354-L354), [README.md#L313-L315](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L313-L315), [README.md#L319-L350](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L319-L350), [README.md#L311-L311](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L311-L311)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md documents mocked end-to-end smoke scripts (e.g. scripts/smoke_test_cli.py, run_cli_mocked.py, smoke_test_resume.py) verifying CLI, resume, improve, and interactive flows without API keys, with the full suite run via `uv run pytest tests/` (464 passed, 1 xfailed). -- evidence: [AGENTS.md#L7-L14](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/AGENTS.md#L7-L14), [AGENTS.md#L33-L33](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/AGENTS.md#L33-L33)
  - [observation/documented] Repository development practice: CLAUDE.md requires autospec=True on all unittest.mock.patch calls (enforced by tests/test_autospec_enforcement.py), spec=RealClass or create_autospec for bare mocks, and a `# noqa: autospec` escape hatch. -- evidence: [CLAUDE.md#L54-L56](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/CLAUDE.md#L54-L56)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Configuration flags include --team (full default, quick, test), --exchanges, --cycles, --orchestrator (api default, or claude-code/gemini-cli/codex/cursor), --orchestrator-model, --effort, --skip-intake, --auto-refine, --json, and --no-auto-commit. -- evidence: [README.md#L217-L221](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L217-L221), [README.md#L203-L208](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L203-L208), [README.md#L210-L215](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L210-L215)
- memory-state (2 claim(s)):
  - [observation/documented] Runs are stored under ~/.kodo/runs/ and can be resumed by ID or as the latest incomplete run; test-mode coverage tracking persists in .kodo/test-coverage.md so repeated runs skip previously tested features. -- evidence: [README.md#L235-L235](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L235-L235), [README.md#L170-L172](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L170-L172), [README.md#L371-L371](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L371-L371)
  - [observation/documented] A session is a stateful conversation with a backend that tracks token usage and supports reset; an agent combines a prompt, session, and turn budget, invoked as agent.run(task, project_dir). -- evidence: [README.md#L300-L307](https://github.com/ikamensh/kodo/blob/51aebbfe5a309715543259edbe207ae151cc33ad/README.md#L300-L307)
- orchestration (2 claim(s)):
More evidence: [full detail](kodo.detail.md)

Metadata and full claim list: [full detail](kodo.detail.md)
Human notes ([notes](kodo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
