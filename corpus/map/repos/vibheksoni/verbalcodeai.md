# vibheksoni/verbalcodeai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b65654df0be4 @ 868b8614361a0d87

## Summary (orientation draft, not independently verified)

Selected evidence records: VerbalCodeAI is a terminal-based AI code companion offering code analysis, natural-language code search, chat, and agent mode, using embeddings and LLM integration. The app runs via `python app.py` with a main menu offering Chat with AI, Agent Mode, Reindex Project, Project Info, Settings, and Exit.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] VerbalCodeAI is a terminal-based AI code companion offering code analysis, natural-language code search, chat, and agent mode, using embeddings and LLM integration. -- evidence: [README.md#L68-L76](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L68-L76), [README.md#L15-L15](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L15-L15)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Performance can be tuned via PERFORMANCE_MODE (LOW/MEDIUM/MAX), MAX_THREADS, embedding cache size, similarity threshold, and per-provider API delay settings. -- evidence: [README.md#L491-L491](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L491-L491), [README.md#L484-L484](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L484-L484), [README.md#L486-L486](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L486-L486), [README.md#L482-L482](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L482-L482), [README.md#L582-L584](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L582-L584), [README.md#L480-L480](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L480-L480)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions follow a fork, feature-branch, commit, push, and pull-request workflow, and PRs are welcomed. -- evidence: [README.md#L656-L656](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L656-L656), [README.md#L658-L662](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L658-L662)
  - [observation/documented] Repository development practice: setup is via platform scripts (setup_windows.bat, setup_linux.sh) or manual venv creation plus pip install -r requirements.txt and a .env file. -- evidence: [README.md#L129-L132](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L129-L132), [README.md#L110-L114](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L110-L114), [README.md#L134-L134](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L134-L134), [README.md#L120-L123](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L120-L123), [README.md#L97-L100](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L97-L100)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The app runs via `python app.py` with a main menu offering Chat with AI, Agent Mode, Reindex Project, Project Info, Settings, and Exit. -- evidence: [README.md#L142-L144](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L142-L144), [README.md#L152-L157](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L152-L157)
  - [observation/documented] A built-in HTTP API server is started with `python app.py --serve [PORT]` (default 8000) and exposes health, initialize, ask, index/start, and index/status endpoints. -- evidence: [README.md#L181-L183](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L181-L183), [README.md#L185-L185](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L185-L185), [README.md#L189-L193](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L189-L193)
- memory-state (1 claim(s)):
  - [observation/documented] The AI has a memory system for project information, controlled by MEMORY_ENABLED with a configurable MAX_MEMORY_ITEMS cap (default 10). -- evidence: [README.md#L509-L509](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L509-L509), [README.md#L68-L76](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L68-L76), [README.md#L511-L511](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L511-L511)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Agent Mode provides search, file, code-analysis, git, memory, system-command, and web tools, including embed_search, run_command, git_history, and google_search. -- evidence: [README.md#L163-L171](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L163-L171)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Supported LLM providers are Ollama (default, local), Google AI, OpenAI, Anthropic, Groq, and OpenRouter, each configured via .env provider and API-key variables. -- evidence: [README.md#L421-L424](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L421-L424), [README.md#L533-L538](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L533-L538), [README.md#L435-L438](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/README.md#L435-L438)
  - [observation/documented] requirements.txt pins libraries including anthropic, openai, ollama, google-generativeai, groq, mcp, tree-sitter, textual, scikit-learn, and pytest. -- evidence: [requirements.txt#L1-L92](https://github.com/vibheksoni/VerbalCodeAi/blob/b65654df0be4168bf429e87eda0d4282c6f6c14c/requirements.txt#L1-L92)
- limitations (1 claim(s)):
More evidence: [full detail](verbalcodeai.detail.md)

Metadata and full claim list: [full detail](verbalcodeai.detail.md)
Human notes ([notes](verbalcodeai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
