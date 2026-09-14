---
access: public
aliases: []
claim_ids:
- clm_9a757b784a84dcdfff4e56183675f68c000e0a5b36213e9d52dddffca382274e
- clm_aa3b4fd9f19108b582b7f041236dc89a95a650caf6b583c79538087d91dd087b
maturity: draft
page_id: pg_3f32b53756cb5e98b7619ee846122c0b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_126d55f145de56659161973a30d5d20a
title: huggingface/tau/AGENTS.md @ a8f18e7bc645
updated_at: '2026-09-14T02:04:24Z'
---

# huggingface/tau/AGENTS.md @ a8f18e7bc645

<!-- rcw:begin owner=source:src_126d55f145de56659161973a30d5d20a block=evidence -->
- Repository development practice: contributors run checks via uv (uv run pytest, ruff check, ruff format --check, mypy), keep commits atomic, and add tests for behavior changes before expanding features. [@claim:clm_9a757b784a84dcdfff4e56183675f68c000e0a5b36213e9d52dddffca382274e]
- Tau is split into three layers: tau_ai (provider/model streaming), tau_agent (portable harness with loop, tools, events, sessions), and tau_coding (CLI, TUI, skills, on-disk sessions). [@claim:clm_aa3b4fd9f19108b582b7f041236dc89a95a650caf6b583c79538087d91dd087b]
<!-- rcw:end owner=source:src_126d55f145de56659161973a30d5d20a block=evidence -->

## Researcher notes

