# vibheksoni/verbalcodeai -- full detail

[Back to orientation](verbalcodeai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vibheksoni/verbalcodeai/b65654df0be4168bf429e87eda0d4282c6f6c14c/868b8614361a0d87.json](../../../wiki/dossiers/vibheksoni/verbalcodeai/b65654df0be4168bf429e87eda0d4282c6f6c14c/868b8614361a0d87.json)

## specifications (1 claim(s))

- [observation/documented] VerbalCodeAI is a terminal-based AI code companion offering code analysis, natural-language code search, chat, and agent mode, using embeddings and LLM integration. -- evidence: [README.md#L68-L76](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L68-L76), [README.md#L15-L15](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L15-L15) (`clm_aa509a4cfca10b1f3fcf95ce6848ed728adb6f423f5253e44c47138a4d1e04d0`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Performance can be tuned via PERFORMANCE_MODE (LOW/MEDIUM/MAX), MAX_THREADS, embedding cache size, similarity threshold, and per-provider API delay settings. -- evidence: [README.md#L491-L491](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L491-L491), [README.md#L484-L484](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L484-L484), [README.md#L486-L486](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L486-L486), [README.md#L482-L482](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L482-L482), [README.md#L582-L584](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L582-L584), [README.md#L480-L480](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L480-L480) (`clm_1f6db99ab0c539bd9c610a285ff0ffb8e33c2d6afab573fc26fbcfc78ebeefc7`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions follow a fork, feature-branch, commit, push, and pull-request workflow, and PRs are welcomed. -- evidence: [README.md#L656-L656](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L656-L656), [README.md#L658-L662](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L658-L662) (`clm_525b64bb7f8f6b109fb5cdc115487b7c5199583462720c20e8b6de0fb2e20527`)
- [observation/documented] Repository development practice: setup is via platform scripts (setup_windows.bat, setup_linux.sh) or manual venv creation plus pip install -r requirements.txt and a .env file. -- evidence: [README.md#L129-L132](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L129-L132), [README.md#L110-L114](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L110-L114), [README.md#L134-L134](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L134-L134), [README.md#L120-L123](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L120-L123), [README.md#L97-L100](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L97-L100) (`clm_1f279a9815daec4bf8db82b54d2bb55e59f642c523b71cbb89f13c1e680e98d2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The app runs via `python app.py` with a main menu offering Chat with AI, Agent Mode, Reindex Project, Project Info, Settings, and Exit. -- evidence: [README.md#L142-L144](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L142-L144), [README.md#L152-L157](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L152-L157) (`clm_254a4ec615c5ccbfe8623974811120f33db685fdad36f97628467a52a32d3b75`)
- [observation/documented] A built-in HTTP API server is started with `python app.py --serve [PORT]` (default 8000) and exposes health, initialize, ask, index/start, and index/status endpoints. -- evidence: [README.md#L181-L183](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L181-L183), [README.md#L185-L185](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L185-L185), [README.md#L189-L193](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L189-L193) (`clm_e2f0f67a0911193cdc777d97548a1bcadf45988fc2c5a5641e399ead6b246c0d`)
- [observation/documented] The HTTP server accepts only localhost connections by default; setting HTTP_ALLOW_ALL_ORIGINS=TRUE in .env allows connections from any IP address. -- evidence: [README.md#L214-L214](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L214-L214) (`clm_d5708579cd114a667b9a9a2fd8897a1fc69c319fd263337c0af87d497fa3e89e`)

## memory-state (1 claim(s))

- [observation/documented] The AI has a memory system for project information, controlled by MEMORY_ENABLED with a configurable MAX_MEMORY_ITEMS cap (default 10). -- evidence: [README.md#L509-L509](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L509-L509), [README.md#L68-L76](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L68-L76), [README.md#L511-L511](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L511-L511) (`clm_948d0361ca80b1dbd1a45b782799f68b948900c469871185afec537c35bb0a6d`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Agent Mode provides search, file, code-analysis, git, memory, system-command, and web tools, including embed_search, run_command, git_history, and google_search. -- evidence: [README.md#L163-L171](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L163-L171) (`clm_b006ee4fbdf795a91b4f35fdf2e14c9e6649eb2bf47253d7e90712fcdb2fd680`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Supported LLM providers are Ollama (default, local), Google AI, OpenAI, Anthropic, Groq, and OpenRouter, each configured via .env provider and API-key variables. -- evidence: [README.md#L421-L424](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L421-L424), [README.md#L533-L538](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L533-L538), [README.md#L435-L438](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L435-L438) (`clm_80742661beddb1a77a576c05f7d3386ba8469136d39c519535cd1ebd5ddd749c`)
- [observation/documented] requirements.txt pins libraries including anthropic, openai, ollama, google-generativeai, groq, mcp, tree-sitter, textual, scikit-learn, and pytest. -- evidence: [requirements.txt#L1-L92](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/requirements.txt#L1-L92) (`clm_0cd938e1b765564a0c984afa3f9dbb85b2e29e9e8298367a86171386d4601ca6`)

## limitations (1 claim(s))

- [observation/documented] Anthropic and Groq do not provide embedding capabilities, so a different provider must be used for embeddings when those providers are selected. -- evidence: [README.md#L569-L569](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L569-L569), [README.md#L578-L578](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L578-L578) (`clm_4c52c6a4997e97a6951af68698879785680eb833d78a081e1d997ea4273bcd57`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

