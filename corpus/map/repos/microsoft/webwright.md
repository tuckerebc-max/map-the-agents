# microsoft/webwright

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bc26750af3ad @ 884112d832b1b36a

## Summary (orientation draft, not independently verified)

Webwright is a Microsoft research repository providing a minimal terminal-based coding-agent harness (~1.5k LoC) that turns LLM coding models into browser agents via Playwright, with pluggable OpenAI/Anthropic/OpenRouter backends, a Skill Factory for reusable code skills, plugin integrations for Claude Code/Codex/OpenClaw/Hermes, and reported benchmark results on Online-Mind2Web and Odysseys. Evidence coverage: 147 of 186 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The repository layout includes src/webwright with a CLI entrypoint (run/cli.py), a core agent loop (agents/default.py), a Playwright browser workspace (environments/), tools (image_qa, self_reflection), model backends, and stacked YAML configs (base.yaml, model_openai.yaml, model_claude.yaml). -- evidence: [README.md#L106-L124](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L106-L124)
  - [observation/documented] A small Flask app under assets/task_showcase/ renders repeatable-run results (task.json plus report.json per task folder) as a dashboard, served locally on port 5005 and configurable to point at a run's generated tasks directory. -- evidence: [README.md#L162-L165](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L162-L165), [README.md#L130-L136](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L130-L136), [README.md#L138-L141](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L138-L141)
- design-choices (3 claim(s)):
  - [observation/documented] Webwright gives the LLM a terminal from which it launches browser sessions to complete web tasks, capturing screenshots and page state only when needed, and each task's browsing history is captured as a single re-runnable Python script. -- evidence: [README.md#L19-L19](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L19-L19)
  - [observation/documented] The architecture deliberately separates the agent from the browser: the browser is treated as a disposable environment the agent spawns and discards, while the persistent state is the code, screenshots, and logs in the local workspace. -- evidence: [README.md#L72-L78](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L72-L78), [README.md#L39-L39](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L39-L39)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: prerequisites are Python 3.10+, Chromium installed via Playwright, and an API key for the chosen backend; installation is `pip install -e .` followed by `playwright install chromium`, and the image_qa/self_reflection tools reuse the configured backend model so no extra key is needed. -- evidence: [README.md#L212-L215](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L212-L215), [README.md#L205-L208](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L205-L208), [README.md#L199-L201](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L199-L201)
  - [observation/documented] Repository development practice: the project adopts the Microsoft Open Source Code of Conduct, with questions directed to opencode@microsoft.com. -- evidence: [CODE_OF_CONDUCT.md#L3-L3](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/CODE_OF_CONDUCT.md#L3-L3), [CODE_OF_CONDUCT.md#L7-L10](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/CODE_OF_CONDUCT.md#L7-L10)
- skills-patterns (3 claim(s)):
  - [observation/documented] The Skill Factory distills each solved task's script into reusable, verified, parameterized code skills that run standalone without a model (~40 s, zero tokens); a recommend/route step checks the library out of the agent loop, either running a matching skill directly or injecting it as a prompt hint. -- evidence: [README.md#L177-L183](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L177-L183), [README.md#L189-L191](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L189-L191), [README.md#L171-L175](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L171-L175)
More evidence: [full detail](webwright.detail.md)

Metadata and full claim list: [full detail](webwright.detail.md)
Human notes ([notes](webwright.notes.md), never overwritten by build)

[Back to map index](../../index.md)
