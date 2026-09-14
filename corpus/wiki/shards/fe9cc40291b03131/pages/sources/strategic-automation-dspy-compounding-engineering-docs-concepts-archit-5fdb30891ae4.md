---
access: public
aliases: []
claim_ids:
- clm_519257e91ad178073e35be7c1f61147855fd64c14a0807f1df44f1037a86e518
- clm_53ac4d4066fcc6c4e0a74f202afc9190610b6685358358742d7ec7395768d386
- clm_a1fd99747b9dc8f7c8c2a6bef42a8fcab4b9077de626776b492f6d8b9fb6b9de
- clm_a4de5b450f2907fd55cee35dea117bd8351a943693a1b6ed772b3b22c912fbd3
- clm_b3589ade229303d9d7034ba686bdb8cfa53d3dd97fd8a2eca8de042357c89a46
- clm_d8f3fe892b2a15961648c6a102734991a85ea0dc06ae0dadef85a09bcba711f4
- clm_f286d75ec5e663819d15c0c6b19c35a71ad7ec3a4902f32a305dc039d06e8b42
maturity: draft
page_id: pg_92ae95e7a31b57c7a7e05fdb30891ae4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_232492dfccbf54a9be6fd1d1efc029ed
title: Strategic-Automation/dspy-compounding-engineering/docs/concepts/architecture.md
  @ 918f63caff79
updated_at: '2026-09-14T03:15:54Z'
---

# Strategic-Automation/dspy-compounding-engineering/docs/concepts/architecture.md @ 918f63caff79

<!-- rcw:begin owner=source:src_232492dfccbf54a9be6fd1d1efc029ed block=evidence -->
- Work execution can run in isolated git worktrees for safe parallel execution, with automatic worktree cleanup after completion. [@claim:clm_519257e91ad178073e35be7c1f61147855fd64c14a0807f1df44f1037a86e518]
- Workflows orchestrate multi-step processes: the review pipeline parallelizes agents and writes pending todo files, triage interactively converts them to ready, and unified work executes them via ReAct loops, marking them complete. [@claim:clm_53ac4d4066fcc6c4e0a74f202afc9190610b6685358358742d7ec7395768d386]
- The system is layered: a CLI layer (cli.py), orchestration layer (workflows/), DSPy agents layer (agents/), knowledge layer, and infrastructure/utils layer. [@claim:clm_a1fd99747b9dc8f7c8c2a6bef42a8fcab4b9077de626776b492f6d8b9fb6b9de]
- The product exposes a Typer-based CLI ('compounding') with commands including review, triage, work, plan, and codify, mapping user intents to workflows. [@claim:clm_a4de5b450f2907fd55cee35dea117bd8351a943693a1b6ed772b3b22c912fbd3]
- Learnings are persisted as structured JSON in a .knowledge/ directory, with keyword/tag-based retrieval and automatic injection of relevant past learnings into agent calls via a KBPredict wrapper. [@claim:clm_b3589ade229303d9d7034ba686bdb8cfa53d3dd97fd8a2eca8de042357c89a46]
- Parallelism uses ThreadPoolExecutor for multi-agent and multi-todo execution, with --workers to set worker count and --sequential for serial mode. [@claim:clm_d8f3fe892b2a15961648c6a102734991a85ea0dc06ae0dadef85a09bcba711f4]
- Review agents include specialized roles such as Security Sentinel (vulnerabilities), Performance Oracle (bottlenecks), Architecture Strategist, and Data Integrity Guardian, with 10+ agents run in parallel. [@claim:clm_f286d75ec5e663819d15c0c6b19c35a71ad7ec3a4902f32a305dc039d06e8b42]
<!-- rcw:end owner=source:src_232492dfccbf54a9be6fd1d1efc029ed block=evidence -->

## Researcher notes

