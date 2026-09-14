# walkingdevflag/mle-star-open

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 30887a7364ed @ 22a7f399ba6120ea

## Summary (orientation draft, not independently verified)

MLE-STAR-Open is an unofficial, Google-free reimplementation of the MLE-STAR multi-agent ML engineering pipeline using OpenAI-compatible APIs (OpenRouter) and DuckDuckGo search, operated via CLI runner scripts with .env/environment-variable configuration. The Ollama local-model adapter is explicitly deferred, and the project targets local experimentation rather than official MLE-Bench scale.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is an unofficial, Google-free, local-friendly reimplementation of the MLE-STAR multi-agent ML engineering pipeline, not affiliated with the original authors or Google. -- evidence: [README.md#L179-L179](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L179-L179), [README.md#L4-L6](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L4-L6)
- components (1 claim(s)):
  - [observation/documented] The pipeline consists of multi-agent stages: initialization, refinement, ensembling, and submission. -- evidence: [README.md#L12-L18](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L12-L18)
- design-choices (2 claim(s)):
  - [observation/documented] Tasks are defined by a directory containing task_description.txt (task_name, target, id_column, metric) plus train.csv and optionally test.csv; train must include the target column while test omits it. -- evidence: [README.md#L92-L92](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L92-L92), [README.md#L75-L81](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L75-L81), [README.md#L85-L90](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L85-L90)
  - [observation/documented] Runs write artifacts under machine_learning_engineering/workspace/<task>/<run_id>/ with init, refine, ensemble, output/predictions.csv, and logs subdirectories. -- evidence: [README.md#L118-L125](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L118-L125)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: tests are run with pytest, and scenario and pipeline tests live under eval/ and tests/; test dependencies are pytest and pytest-asyncio. -- evidence: [requirements.txt#L23-L24](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L23-L24), [README.md#L142-L144](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L142-L144), [README.md#L146-L146](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L146-L146)
  - [observation/documented] Repository development practice: setup instructions call for Python 3.12+, Git, optionally Poetry, a conda environment, and pip install -r requirements.txt. -- evidence: [README.md#L35-L37](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L35-L37), [README.md#L54-L55](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L54-L55), [README.md#L47-L48](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L47-L48)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is operated via CLI scripts: run_pipeline.py for the full pipeline, run_task.py for a minimal run with fewer LLM calls, and make_submission.py for Kaggle-style submission formatting. -- evidence: [README.md#L112-L114](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L112-L114), [README.md#L100-L102](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L100-L102), [README.md#L106-L108](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L106-L108)
  - [observation/documented] Configuration is via a .env file (e.g., OPENROUTER_API_KEY, ROOT_AGENT_MODEL); environment variables override defaults defined in shared_libraries/config.py DefaultConfig. -- evidence: [README.md#L67-L67](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L67-L67), [README.md#L59-L61](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L59-L61), [README.md#L131-L131](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L131-L131)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Runtime dependencies include openai, httpx, python-dotenv, pydantic, and duckduckgo-search, plus an ML stack of numpy, pandas, scikit-learn, and torch. -- evidence: [requirements.txt#L17-L17](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L17-L17), [requirements.txt#L6-L10](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L6-L10), [requirements.txt#L13-L15](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L13-L15)
- limitations (2 claim(s)):
  - [observation/documented] The project is not sized for official MLE-Bench specs (36 vCPUs / 440GB RAM / A10 24GB) and targets local experimentation; OpenRouter free tier is roughly 50 requests/day. -- evidence: [README.md#L154-L157](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L154-L157)
More evidence: [full detail](mle-star-open.detail.md)

Metadata and full claim list: [full detail](mle-star-open.detail.md)
Human notes ([notes](mle-star-open.notes.md), never overwritten by build)

[Back to map index](../../index.md)
