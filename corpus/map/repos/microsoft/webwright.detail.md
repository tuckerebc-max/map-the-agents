# microsoft/webwright -- full detail

[Back to orientation](webwright.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/microsoft/webwright/bc26750af3ad166d982f23d101ef8971a3a2fce5/884112d832b1b36a.json](../../../wiki/dossiers/microsoft/webwright/bc26750af3ad166d982f23d101ef8971a3a2fce5/884112d832b1b36a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The repository layout includes src/webwright with a CLI entrypoint (run/cli.py), a core agent loop (agents/default.py), a Playwright browser workspace (environments/), tools (image_qa, self_reflection), model backends, and stacked YAML configs (base.yaml, model_openai.yaml, model_claude.yaml). -- evidence: [README.md#L106-L124](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L106-L124) (`clm_02aeb5f27778da8a4a549f5dcc554cac21ec63dd2afddf18b9c27144abeb4d87`)
- [observation/documented] A small Flask app under assets/task_showcase/ renders repeatable-run results (task.json plus report.json per task folder) as a dashboard, served locally on port 5005 and configurable to point at a run's generated tasks directory. -- evidence: [README.md#L162-L165](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L162-L165), [README.md#L130-L136](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L130-L136), [README.md#L138-L141](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L138-L141) (`clm_3cf84102354995f2eb11d3ec01cc30f3b1719db5e1ab264b9ce2159ae8ecce03`)
- [observation/documented] A trajectory comparison viewer under assets/compare_trajectory/ (served via python3 -m http.server) accepts Webwright raw_responses.jsonl plus trajectory.json and can also display Codex and GitHub Copilot traces for token-usage comparison. -- evidence: [README.md#L384-L387](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L384-L387), [README.md#L378-L378](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L378-L378), [README.md#L389-L389](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L389-L389) (`clm_cab6f4036d20b0f73c54d37cf8b70e096f2104c3b6ad70cb5182f4a27bc0930d`)

## design-choices (3 claim(s))

- [observation/documented] Webwright gives the LLM a terminal from which it launches browser sessions to complete web tasks, capturing screenshots and page state only when needed, and each task's browsing history is captured as a single re-runnable Python script. -- evidence: [README.md#L19-L19](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L19-L19) (`clm_e723bcec7374a13e3f6f0708c950928feaa43d32b83dc7547e95814ca02209ef`)
- [observation/documented] The architecture deliberately separates the agent from the browser: the browser is treated as a disposable environment the agent spawns and discards, while the persistent state is the code, screenshots, and logs in the local workspace. -- evidence: [README.md#L72-L78](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L72-L78), [README.md#L39-L39](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L39-L39) (`clm_bb970ac09565e8ac5732562533f0a47501ee010c0cc8718e876c32a6f3662f2f`)
- [observation/documented] The project advertises a minimal footprint with no multi-agent system, graph engine, plugin layer, or hidden orchestration; the core agent loop is a single ~450-line file, the Playwright environment ~570 lines, and the CLI ~150 lines. -- evidence: [README.md#L55-L59](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L55-L59), [README.md#L19-L19](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L19-L19) (`clm_8dd3c0c153b990970356944572c932b6f82a273fd00144154a88223d31093031`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: prerequisites are Python 3.10+, Chromium installed via Playwright, and an API key for the chosen backend; installation is `pip install -e .` followed by `playwright install chromium`, and the image_qa/self_reflection tools reuse the configured backend model so no extra key is needed. -- evidence: [README.md#L212-L215](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L212-L215), [README.md#L205-L208](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L205-L208), [README.md#L199-L201](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L199-L201) (`clm_9dc1dcb3412fdef7d25d992e5bc6dbf91fe32fe33aa6b12e411a8e7d25c3326b`)
- [observation/documented] Repository development practice: the project adopts the Microsoft Open Source Code of Conduct, with questions directed to opencode@microsoft.com. -- evidence: [CODE_OF_CONDUCT.md#L3-L3](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/CODE_OF_CONDUCT.md#L3-L3), [CODE_OF_CONDUCT.md#L7-L10](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/CODE_OF_CONDUCT.md#L7-L10) (`clm_ad4c65715f751f92856874e069203d95dfe517dd6a8a5a91f306a087fb81e63f`)

## skills-patterns (3 claim(s))

- [observation/documented] The Skill Factory distills each solved task's script into reusable, verified, parameterized code skills that run standalone without a model (~40 s, zero tokens); a recommend/route step checks the library out of the agent loop, either running a matching skill directly or injecting it as a prompt hint. -- evidence: [README.md#L177-L183](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L177-L183), [README.md#L189-L191](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L189-L191), [README.md#L171-L175](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L171-L175) (`clm_2b97a3d0d45b9a3ea0f1e1e9a3cb83f053a01015491ff17648d691995e94567b`)
- [observation/documented] Skill Factory verification uses two gates: an input gate (gold, self_verify, or none) deciding whether a solve is trustworthy, and an output gate (strict, shape, or off) checking the distilled skill can reproduce recorded answers with no model; skills whose scripts contain every answer field verbatim are dropped as lookup-style solves. -- evidence: [docs/skill_factory/reference.md#L11-L14](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/docs/skill_factory/reference.md#L11-L14), [docs/skill_factory/reference.md#L7-L9](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/docs/skill_factory/reference.md#L7-L9), [docs/skill_factory/reference.md#L27-L32](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/docs/skill_factory/reference.md#L27-L32) (`clm_e05d8da30eca9fa3a657fc33d29278d599a5fa6ed084dcb0dbd0c42b425af67b`)
- [observation/documented] Manual mode (`update`) lets users write templates, declare parameters, and set per-run admit verdicts themselves, supporting benchmarks with known answers, non-exact-match judging, and login-gated sites whose credentials are carried into replay but never stored in the skill. -- evidence: [docs/skill_factory/manual.md#L133-L135](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/docs/skill_factory/manual.md#L133-L135), [docs/skill_factory/manual.md#L7-L15](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/docs/skill_factory/manual.md#L7-L15), [docs/skill_factory/manual.md#L17-L24](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/docs/skill_factory/manual.md#L17-L24) (`clm_a1adf00c7c8e70ef365071052c8be0c7f462dec86b64b0a2551ea549d38cf121`)

## interfaces (3 claim(s))

- [observation/documented] The CLI is invoked as `python -m webwright.run.cli` with stackable config flags (-c), a task instruction (-t), a start URL (--start-url), a task ID (--task-id), and an output directory (-o). -- evidence: [README.md#L217-L224](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L217-L224), [README.md#L146-L152](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L146-L152), [README.md#L228-L234](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L228-L234) (`clm_02c4c311755cd286e9cb97e595327b51b1a1bc967b193c950f9ceb99862a1d25`)
- [observation/documented] A plain base.yaml run writes trajectory.json and debug artifacts, while adding the task_showcase.yaml config additionally generates a report.json with structured output for the Flask dashboard. -- evidence: [README.md#L154-L156](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L154-L156) (`clm_2c4826f8b3bec51a6a4d036eda2d81569ddda8b391a046c473dbf67e6abceda2`)
- [observation/documented] Webwright ships plugin manifests for Claude Code and OpenAI Codex plus a shared skills/webwright/ folder usable by OpenClaw and Hermes; Claude Code offers /webwright:run (one-shot script) and /webwright:craft (parameterized argparse CLI tool) slash commands. -- evidence: [README.md#L282-L283](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L282-L283), [README.md#L240-L240](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L240-L240), [README.md#L348-L348](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L348-L348), [README.md#L359-L359](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L359-L359) (`clm_0a2afd9e25f4df890442fbb2a935d4b6590b78bc05d643cb5615b9be7813f1b1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] In plugin mode, the host agent drives the Webwright loop natively with no extra LLM API key beyond the host subscription, and hosts that natively read PNG screenshots can skip the image_qa/self_reflection tools. -- evidence: [README.md#L240-L240](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L240-L240) (`clm_6de17261b6a12a818ffa1d760865cdde4698407a4db76594551f87f2b9e416ed`)

## evaluation (2 claim(s))

- [observation/documented] Reported benchmark results: 86.7% on Online-Mind2Web (300 tasks) with GPT-5.4 and 84.7% with Claude Opus 4.7; 60.1% on Odysseys (200 long-horizon tasks) with GPT-5.4, +15.6 points over prior SOTA, using a 100-step budget. -- evidence: [README.md#L90-L90](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L90-L90), [README.md#L92-L95](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L92-L95) (`clm_48072d58fd737cb1717a44c97737307f0fb3620f8db48868e1513b062cee9686`)
- [observation/documented] On WebArena (10 retrieve-type templates, 3 self-hosted sites, gpt-5.4), skill reuse lifts held-out accuracy from 55% to 70% (+15 pp) while reducing steps. -- evidence: [README.md#L27-L30](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L27-L30), [README.md#L189-L191](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L189-L191) (`clm_12391bc41c0da741c8087a82e2d4856a91b349fbed42b59e1bbb89822029a871`)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies are stated as just httpx, pydantic, playwright, and typer, with model backends for OpenAI, Anthropic, and OpenRouter each around 150-200 lines. -- evidence: [README.md#L55-L59](https://github.com/microsoft/Webwright/blob/bc26750af3ad166d982f23d101ef8971a3a2fce5/README.md#L55-L59) (`clm_21e67efe5d4d6fe8784c89b46b0b035f1fbca26d35022154606927dcea8877fa`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

