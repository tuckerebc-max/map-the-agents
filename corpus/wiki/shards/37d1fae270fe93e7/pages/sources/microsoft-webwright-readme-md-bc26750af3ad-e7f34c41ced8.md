---
access: public
aliases: []
claim_ids:
- clm_02aeb5f27778da8a4a549f5dcc554cac21ec63dd2afddf18b9c27144abeb4d87
- clm_02c4c311755cd286e9cb97e595327b51b1a1bc967b193c950f9ceb99862a1d25
- clm_0a2afd9e25f4df890442fbb2a935d4b6590b78bc05d643cb5615b9be7813f1b1
- clm_12391bc41c0da741c8087a82e2d4856a91b349fbed42b59e1bbb89822029a871
- clm_21e67efe5d4d6fe8784c89b46b0b035f1fbca26d35022154606927dcea8877fa
- clm_2b97a3d0d45b9a3ea0f1e1e9a3cb83f053a01015491ff17648d691995e94567b
- clm_2c4826f8b3bec51a6a4d036eda2d81569ddda8b391a046c473dbf67e6abceda2
- clm_3cf84102354995f2eb11d3ec01cc30f3b1719db5e1ab264b9ce2159ae8ecce03
- clm_48072d58fd737cb1717a44c97737307f0fb3620f8db48868e1513b062cee9686
- clm_6de17261b6a12a818ffa1d760865cdde4698407a4db76594551f87f2b9e416ed
- clm_8dd3c0c153b990970356944572c932b6f82a273fd00144154a88223d31093031
- clm_9dc1dcb3412fdef7d25d992e5bc6dbf91fe32fe33aa6b12e411a8e7d25c3326b
- clm_bb970ac09565e8ac5732562533f0a47501ee010c0cc8718e876c32a6f3662f2f
- clm_cab6f4036d20b0f73c54d37cf8b70e096f2104c3b6ad70cb5182f4a27bc0930d
- clm_e723bcec7374a13e3f6f0708c950928feaa43d32b83dc7547e95814ca02209ef
maturity: draft
page_id: pg_8ba6777875bc55a780c5e7f34c41ced8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_21b70ef63cd25f278edb3c8aaa7227d4
title: microsoft/Webwright/README.md @ bc26750af3ad
updated_at: '2026-09-14T02:18:47Z'
---

# microsoft/Webwright/README.md @ bc26750af3ad

<!-- rcw:begin owner=source:src_21b70ef63cd25f278edb3c8aaa7227d4 block=evidence -->
- The repository layout includes src/webwright with a CLI entrypoint (run/cli.py), a core agent loop (agents/default.py), a Playwright browser workspace (environments/), tools (image_qa, self_reflection), model backends, and stacked YAML configs (base.yaml, model_openai.yaml, model_claude.yaml). [@claim:clm_02aeb5f27778da8a4a549f5dcc554cac21ec63dd2afddf18b9c27144abeb4d87]
- The CLI is invoked as `python -m webwright.run.cli` with stackable config flags (-c), a task instruction (-t), a start URL (--start-url), a task ID (--task-id), and an output directory (-o). [@claim:clm_02c4c311755cd286e9cb97e595327b51b1a1bc967b193c950f9ceb99862a1d25]
- Webwright ships plugin manifests for Claude Code and OpenAI Codex plus a shared skills/webwright/ folder usable by OpenClaw and Hermes; Claude Code offers /webwright:run (one-shot script) and /webwright:craft (parameterized argparse CLI tool) slash commands. [@claim:clm_0a2afd9e25f4df890442fbb2a935d4b6590b78bc05d643cb5615b9be7813f1b1]
- On WebArena (10 retrieve-type templates, 3 self-hosted sites, gpt-5.4), skill reuse lifts held-out accuracy from 55% to 70% (+15 pp) while reducing steps. [@claim:clm_12391bc41c0da741c8087a82e2d4856a91b349fbed42b59e1bbb89822029a871]
- Runtime dependencies are stated as just httpx, pydantic, playwright, and typer, with model backends for OpenAI, Anthropic, and OpenRouter each around 150-200 lines. [@claim:clm_21e67efe5d4d6fe8784c89b46b0b035f1fbca26d35022154606927dcea8877fa]
- The Skill Factory distills each solved task's script into reusable, verified, parameterized code skills that run standalone without a model (~40 s, zero tokens); a recommend/route step checks the library out of the agent loop, either running a matching skill directly or injecting it as a prompt hint. [@claim:clm_2b97a3d0d45b9a3ea0f1e1e9a3cb83f053a01015491ff17648d691995e94567b]
- A plain base.yaml run writes trajectory.json and debug artifacts, while adding the task_showcase.yaml config additionally generates a report.json with structured output for the Flask dashboard. [@claim:clm_2c4826f8b3bec51a6a4d036eda2d81569ddda8b391a046c473dbf67e6abceda2]
- A small Flask app under assets/task_showcase/ renders repeatable-run results (task.json plus report.json per task folder) as a dashboard, served locally on port 5005 and configurable to point at a run's generated tasks directory. [@claim:clm_3cf84102354995f2eb11d3ec01cc30f3b1719db5e1ab264b9ce2159ae8ecce03]
- Reported benchmark results: 86.7% on Online-Mind2Web (300 tasks) with GPT-5.4 and 84.7% with Claude Opus 4.7; 60.1% on Odysseys (200 long-horizon tasks) with GPT-5.4, +15.6 points over prior SOTA, using a 100-step budget. [@claim:clm_48072d58fd737cb1717a44c97737307f0fb3620f8db48868e1513b062cee9686]
- In plugin mode, the host agent drives the Webwright loop natively with no extra LLM API key beyond the host subscription, and hosts that natively read PNG screenshots can skip the image_qa/self_reflection tools. [@claim:clm_6de17261b6a12a818ffa1d760865cdde4698407a4db76594551f87f2b9e416ed]
- The project advertises a minimal footprint with no multi-agent system, graph engine, plugin layer, or hidden orchestration; the core agent loop is a single ~450-line file, the Playwright environment ~570 lines, and the CLI ~150 lines. [@claim:clm_8dd3c0c153b990970356944572c932b6f82a273fd00144154a88223d31093031]
- Repository development practice: prerequisites are Python 3.10+, Chromium installed via Playwright, and an API key for the chosen backend; installation is `pip install -e .` followed by `playwright install chromium`, and the image_qa/self_reflection tools reuse the configured backend model so no extra key is needed. [@claim:clm_9dc1dcb3412fdef7d25d992e5bc6dbf91fe32fe33aa6b12e411a8e7d25c3326b]
- The architecture deliberately separates the agent from the browser: the browser is treated as a disposable environment the agent spawns and discards, while the persistent state is the code, screenshots, and logs in the local workspace. [@claim:clm_bb970ac09565e8ac5732562533f0a47501ee010c0cc8718e876c32a6f3662f2f]
- A trajectory comparison viewer under assets/compare_trajectory/ (served via python3 -m http.server) accepts Webwright raw_responses.jsonl plus trajectory.json and can also display Codex and GitHub Copilot traces for token-usage comparison. [@claim:clm_cab6f4036d20b0f73c54d37cf8b70e096f2104c3b6ad70cb5182f4a27bc0930d]
- Webwright gives the LLM a terminal from which it launches browser sessions to complete web tasks, capturing screenshots and page state only when needed, and each task's browsing history is captured as a single re-runnable Python script. [@claim:clm_e723bcec7374a13e3f6f0708c950928feaa43d32b83dc7547e95814ca02209ef]
<!-- rcw:end owner=source:src_21b70ef63cd25f278edb3c8aaa7227d4 block=evidence -->

## Researcher notes

