---
access: public
aliases: []
claim_ids:
- clm_275f08c27c3de840c267ed8d8eaf09da32ac66c9a3b53aee1237ae74eac9ebe6
- clm_3e658270a67699b9174eaea1240f32a5d9226e1b04944a03765685fa936c7277
- clm_4a4527ef1a42a0e40635c1b30a572aa8d6ecbe7da1206af43ca5561b5cdebf90
- clm_4fc845e6030a03d192de38b58b9878d78f828092eb7b21175727f12d06c191c2
- clm_5fb75fb9a994e0aa4e0ec38f161fc2fc7eb4a913127dc082c548a734a7ae67a4
- clm_74f95a639b029e8b5c29b01d1cd889d94285bcfbdfe8d3d675a335500ede939d
- clm_757fa069b8368224ea22f904a11a136ea78470fd134d00252021e994a599b124
- clm_7a10eef9af38838a265240b782ce0194d5779699fef989869f1eaf03201184ec
- clm_8727393d4ce027f35102adbc50af4de5ec7b9b2983eb9916f7203fd3b4dc7ffd
- clm_be49af2bdd3118f233fa1f54b70849ae1125938e796351de5973d2122314a749
- clm_ee7a8de3104129f25ed9bedfd228d0c2d6351cb3469c5e7ad58a05fdac0e4ab5
maturity: draft
page_id: pg_68e3d9b13da25f0fb07b8e0367613839
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_be4d03b54a3b56a8b56ee4bde407bec4
title: WalkingDevFlag/MLE-STAR-Open/README.md @ 30887a7364ed
updated_at: '2026-09-14T03:22:56Z'
---

# WalkingDevFlag/MLE-STAR-Open/README.md @ 30887a7364ed

<!-- rcw:begin owner=source:src_be4d03b54a3b56a8b56ee4bde407bec4 block=evidence -->
- Configuration is via a .env file (e.g., OPENROUTER_API_KEY, ROOT_AGENT_MODEL); environment variables override defaults defined in shared_libraries/config.py DefaultConfig. [@claim:clm_275f08c27c3de840c267ed8d8eaf09da32ac66c9a3b53aee1237ae74eac9ebe6]
- The Ollama local-model adapter is deferred pending provider and evaluation stabilization; the archive cites an evolving provider interface, in-flight tool layer, and a not-yet-merged prompt/artifact cache as reasons. [@claim:clm_3e658270a67699b9174eaea1240f32a5d9226e1b04944a03765685fa936c7277]
- Repository development practice: tests are run with pytest, and scenario and pipeline tests live under eval/ and tests/; test dependencies are pytest and pytest-asyncio. [@claim:clm_4a4527ef1a42a0e40635c1b30a572aa8d6ecbe7da1206af43ca5561b5cdebf90]
- The pipeline consists of multi-agent stages: initialization, refinement, ensembling, and submission. [@claim:clm_4fc845e6030a03d192de38b58b9878d78f828092eb7b21175727f12d06c191c2]
- The project is not sized for official MLE-Bench specs (36 vCPUs / 440GB RAM / A10 24GB) and targets local experimentation; OpenRouter free tier is roughly 50 requests/day. [@claim:clm_5fb75fb9a994e0aa4e0ec38f161fc2fc7eb4a913127dc082c548a734a7ae67a4]
- The project is an unofficial, Google-free, local-friendly reimplementation of the MLE-STAR multi-agent ML engineering pipeline, not affiliated with the original authors or Google. [@claim:clm_74f95a639b029e8b5c29b01d1cd889d94285bcfbdfe8d3d675a335500ede939d]
- Repository development practice: setup instructions call for Python 3.12+, Git, optionally Poetry, a conda environment, and pip install -r requirements.txt. [@claim:clm_757fa069b8368224ea22f904a11a136ea78470fd134d00252021e994a599b124]
- Runs write artifacts under machine_learning_engineering/workspace/<task>/<run_id>/ with init, refine, ensemble, output/predictions.csv, and logs subdirectories. [@claim:clm_7a10eef9af38838a265240b782ce0194d5779699fef989869f1eaf03201184ec]
- Tasks are defined by a directory containing task_description.txt (task_name, target, id_column, metric) plus train.csv and optionally test.csv; train must include the target column while test omits it. [@claim:clm_8727393d4ce027f35102adbc50af4de5ec7b9b2983eb9916f7203fd3b4dc7ffd]
- The product is operated via CLI scripts: run_pipeline.py for the full pipeline, run_task.py for a minimal run with fewer LLM calls, and make_submission.py for Kaggle-style submission formatting. [@claim:clm_be49af2bdd3118f233fa1f54b70849ae1125938e796351de5973d2122314a749]
- The project reimplements the approach of the MLE-STAR paper (arXiv:2506.15692), which it cites as the original work. [@claim:clm_ee7a8de3104129f25ed9bedfd228d0c2d6351cb3469c5e7ad58a05fdac0e4ab5]
<!-- rcw:end owner=source:src_be4d03b54a3b56a8b56ee4bde407bec4 block=evidence -->

## Researcher notes

