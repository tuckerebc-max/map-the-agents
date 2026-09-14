# huggingface/tau -- full detail

[Back to orientation](tau.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/huggingface/tau/a8f18e7bc645d09d47d40b21bc602df97f2579fd/e787110266cc3f66.json](../../../wiki/dossiers/huggingface/tau/a8f18e7bc645d09d47d40b21bc602df97f2579fd/e787110266cc3f66.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Tau is split into three layers: tau_ai (provider/model streaming), tau_agent (portable harness with loop, tools, events, sessions), and tau_coding (CLI, TUI, skills, on-disk sessions). -- evidence: [README.md#L42-L46](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L42-L46), [AGENTS.md#L25-L29](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/AGENTS.md#L25-L29) (`clm_aa3b4fd9f19108b582b7f041236dc89a95a650caf6b583c79538087d91dd087b`)

## design-choices (2 claim(s))

- [observation/documented] The architecture treats a typed event stream as the contract: providers, renderers, the TUI, and custom frontends all consume events rather than the core rendering UI itself. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L221-L222](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L221-L222) (`clm_280c2f040f0ee6f2d40b40bf6d9ce8aa3b1d84ac647f86d484746f6f252d2979`)
- [observation/documented] The core harness is kept portable: it does not depend on Textual, Rich, local config paths, slash commands, or rendering, and frontends consume its events. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L56-L57](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L56-L57) (`clm_0f0a9928b3e19fd1936beda40d41c88c7b149d8e3b9754aa512824323c9abab8`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run checks via uv (uv run pytest, ruff check, ruff format --check, mypy), keep commits atomic, and add tests for behavior changes before expanding features. -- evidence: [AGENTS.md#L47-L53](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/AGENTS.md#L47-L53), [README.md#L228-L234](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L228-L234), [CONTRIBUTING.md#L62-L67](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L62-L67), [CONTRIBUTING.md#L104-L108](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L104-L108) (`clm_9a757b784a84dcdfff4e56183675f68c000e0a5b36213e9d52dddffca382274e`)
- [observation/documented] Repository development practice: releases to PyPI are intentional — a version bump in pyproject.toml merged via PR triggers publishing, not every merge to main. -- evidence: [CONTRIBUTING.md#L127-L128](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L127-L128), [CONTRIBUTING.md#L130-L135](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L130-L135) (`clm_45931093f9995d612aa9104263d0b6c278ee78307ac2de6816e732e0d9423b9d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] As a library, users construct AgentHarness with AgentHarnessConfig (provider, model, system prompt, tools) and consume an async event stream from harness.prompt(). -- evidence: [README.md#L205-L206](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L205-L206), [README.md#L208-L215](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L208-L215), [README.md#L217-L219](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L217-L219) (`clm_696d0e6ad8f0dd95868a1886fae0ed485045fbccf828d2c0be3b2409a994932d`)
- [observation/documented] The CLI supports interactive TUI and one-shot print mode (tau -p), a --cwd option, and slash commands such as /login and /model for provider and model selection. -- evidence: [README.md#L148-L151](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L148-L151), [README.md#L159-L164](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L159-L164), [README.md#L176-L185](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L176-L185) (`clm_4df0be67604bbd93bc1658803effa2f7b1004ca6b04385ff68b274d54a163845`)
- [observation/documented] The provider catalog is data-driven: built-in entries live in src/tau_coding/data/catalog.toml, and users can add providers via ~/.tau/catalog.toml with the same schema without code changes. -- evidence: [CONTRIBUTING.md#L98-L100](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/CONTRIBUTING.md#L98-L100), [README.md#L170-L172](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L170-L172) (`clm_9b9a2699ae592f444491e392bde5ceeb84da11f359b97d8be61d597c7d16f8b2`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are stored as durable, append-only JSONL files under ~/.tau/sessions/ with resume and branching, and active context can be compacted without rewriting the record. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L176-L185](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L176-L185) (`clm_cdd69d98a912368b2c20dd1931b66e1b208fc595168487658a01a74bb0998268`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Tau ships built-in coding tools named read, write, edit, and bash, described as typed functions with a schema and an async executor returning structured results. -- evidence: [README.md#L191-L201](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L191-L201), [README.md#L176-L185](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L176-L185) (`clm_2fd0fa34aadb23b9ebda646f7a49d6187091ade346cdc05b356314774319c849`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Tau requires Python 3.12 or newer, is published on PyPI as tau-ai installing a tau command, and recommends uv-based installers. -- evidence: [README.md#L61-L63](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L61-L63) (`clm_0c5e75359429f33dfc114e623936588e3310213fc37008fb1a09e43251c5d3a0`)
- [observation/documented] Built-in provider support includes OpenAI, Anthropic, OpenAI Codex subscription auth, OpenRouter, Hugging Face, and custom OpenAI-compatible endpoints including local models. -- evidence: [README.md#L166-L168](https://github.com/huggingface/tau/blob/a8f18e7bc645d09d47d40b21bc602df97f2579fd/README.md#L166-L168) (`clm_a6916eb3825acb9608d42a0658c9c3a83790426304a83b5596a5ed446ddcd6ba`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

