---
access: public
aliases: []
claim_ids:
- clm_50c0ee0bbe48c244d12500bef316e64c8af9e08294af86c2221cad6b6bad446c
maturity: draft
page_id: pg_b0f72494a29e5f6cbcf8aa41d1d15c23
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5042c1b39a10567681570fd1c89eb99e
title: VibePod/vibepod-cli/AGENTS.md @ ef6519007b1d
updated_at: '2026-09-14T03:21:45Z'
---

# VibePod/vibepod-cli/AGENTS.md @ ef6519007b1d

<!-- rcw:begin owner=source:src_5042c1b39a10567681570fd1c89eb99e block=evidence -->
- Repository development practice: the test runner is pytest (`python -m pytest`); CI also validates default images with `scripts/check_default_images.py`, and `ruff check`, `ruff format --check`, and `mypy` are pre-commit gated. Tests should run with a throwaway `VP_CONFIG_DIR` when a host global config exists. [@claim:clm_50c0ee0bbe48c244d12500bef316e64c8af9e08294af86c2221cad6b6bad446c]
<!-- rcw:end owner=source:src_5042c1b39a10567681570fd1c89eb99e block=evidence -->

## Researcher notes

