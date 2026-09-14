# walkingdevflag/mle-star-open -- full detail

[Back to orientation](mle-star-open.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/walkingdevflag/mle-star-open/30887a7364ed5e8b8c399d65b44bb2821238e885/22a7f399ba6120ea.json](../../../wiki/dossiers/walkingdevflag/mle-star-open/30887a7364ed5e8b8c399d65b44bb2821238e885/22a7f399ba6120ea.json)

## specifications (1 claim(s))

- [observation/documented] The project is an unofficial, Google-free, local-friendly reimplementation of the MLE-STAR multi-agent ML engineering pipeline, not affiliated with the original authors or Google. -- evidence: [README.md#L179-L179](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L179-L179), [README.md#L4-L6](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L4-L6) (`clm_74f95a639b029e8b5c29b01d1cd889d94285bcfbdfe8d3d675a335500ede939d`)

## components (1 claim(s))

- [observation/documented] The pipeline consists of multi-agent stages: initialization, refinement, ensembling, and submission. -- evidence: [README.md#L12-L18](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L12-L18) (`clm_4fc845e6030a03d192de38b58b9878d78f828092eb7b21175727f12d06c191c2`)

## design-choices (2 claim(s))

- [observation/documented] Tasks are defined by a directory containing task_description.txt (task_name, target, id_column, metric) plus train.csv and optionally test.csv; train must include the target column while test omits it. -- evidence: [README.md#L92-L92](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L92-L92), [README.md#L75-L81](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L75-L81), [README.md#L85-L90](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L85-L90) (`clm_8727393d4ce027f35102adbc50af4de5ec7b9b2983eb9916f7203fd3b4dc7ffd`)
- [observation/documented] Runs write artifacts under machine_learning_engineering/workspace/<task>/<run_id>/ with init, refine, ensemble, output/predictions.csv, and logs subdirectories. -- evidence: [README.md#L118-L125](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L118-L125) (`clm_7a10eef9af38838a265240b782ce0194d5779699fef989869f1eaf03201184ec`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: tests are run with pytest, and scenario and pipeline tests live under eval/ and tests/; test dependencies are pytest and pytest-asyncio. -- evidence: [requirements.txt#L23-L24](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L23-L24), [README.md#L142-L144](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L142-L144), [README.md#L146-L146](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L146-L146) (`clm_4a4527ef1a42a0e40635c1b30a572aa8d6ecbe7da1206af43ca5561b5cdebf90`)
- [observation/documented] Repository development practice: setup instructions call for Python 3.12+, Git, optionally Poetry, a conda environment, and pip install -r requirements.txt. -- evidence: [README.md#L35-L37](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L35-L37), [README.md#L54-L55](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L54-L55), [README.md#L47-L48](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L47-L48) (`clm_757fa069b8368224ea22f904a11a136ea78470fd134d00252021e994a599b124`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is operated via CLI scripts: run_pipeline.py for the full pipeline, run_task.py for a minimal run with fewer LLM calls, and make_submission.py for Kaggle-style submission formatting. -- evidence: [README.md#L112-L114](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L112-L114), [README.md#L100-L102](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L100-L102), [README.md#L106-L108](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L106-L108) (`clm_be49af2bdd3118f233fa1f54b70849ae1125938e796351de5973d2122314a749`)
- [observation/documented] Configuration is via a .env file (e.g., OPENROUTER_API_KEY, ROOT_AGENT_MODEL); environment variables override defaults defined in shared_libraries/config.py DefaultConfig. -- evidence: [README.md#L67-L67](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L67-L67), [README.md#L59-L61](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L59-L61), [README.md#L131-L131](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L131-L131) (`clm_275f08c27c3de840c267ed8d8eaf09da32ac66c9a3b53aee1237ae74eac9ebe6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include openai, httpx, python-dotenv, pydantic, and duckduckgo-search, plus an ML stack of numpy, pandas, scikit-learn, and torch. -- evidence: [requirements.txt#L17-L17](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L17-L17), [requirements.txt#L6-L10](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L6-L10), [requirements.txt#L13-L15](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/requirements.txt#L13-L15) (`clm_bc30b34ad08f800838f29aa44cf6cf36007fff27d49b27cb948e6aebaa4cc195`)

## limitations (2 claim(s))

- [observation/documented] The project is not sized for official MLE-Bench specs (36 vCPUs / 440GB RAM / A10 24GB) and targets local experimentation; OpenRouter free tier is roughly 50 requests/day. -- evidence: [README.md#L154-L157](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L154-L157) (`clm_5fb75fb9a994e0aa4e0ec38f161fc2fc7eb4a913127dc082c548a734a7ae67a4`)
- [observation/documented] The Ollama local-model adapter is deferred pending provider and evaluation stabilization; the archive cites an evolving provider interface, in-flight tool layer, and a not-yet-merged prompt/artifact cache as reasons. -- evidence: [ARCHIVE.md#L10-L15](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/ARCHIVE.md#L10-L15), [README.md#L154-L157](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L154-L157), [ARCHIVE.md#L6-L6](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/ARCHIVE.md#L6-L6) (`clm_3e658270a67699b9174eaea1240f32a5d9226e1b04944a03765685fa936c7277`)

## relevance (1 claim(s))

- [observation/documented] The project reimplements the approach of the MLE-STAR paper (arXiv:2506.15692), which it cites as the original work. -- evidence: [README.md#L172-L173](https://github.com/WalkingDevFlag/MLE-STAR-Open/blob/30887a7364ed5e8b8c399d65b44bb2821238e885/README.md#L172-L173) (`clm_ee7a8de3104129f25ed9bedfd228d0c2d6351cb3469c5e7ad58a05fdac0e4ab5`)

