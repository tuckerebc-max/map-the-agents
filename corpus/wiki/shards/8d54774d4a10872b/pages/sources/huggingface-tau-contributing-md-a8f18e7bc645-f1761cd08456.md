---
access: public
aliases: []
claim_ids:
- clm_45931093f9995d612aa9104263d0b6c278ee78307ac2de6816e732e0d9423b9d
- clm_9a757b784a84dcdfff4e56183675f68c000e0a5b36213e9d52dddffca382274e
- clm_9b9a2699ae592f444491e392bde5ceeb84da11f359b97d8be61d597c7d16f8b2
maturity: draft
page_id: pg_2cc9be0f83825d1598b9f1761cd08456
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_866f4aa79ff25865b46b53e840c6d35a
title: huggingface/tau/CONTRIBUTING.md @ a8f18e7bc645
updated_at: '2026-09-14T02:04:24Z'
---

# huggingface/tau/CONTRIBUTING.md @ a8f18e7bc645

<!-- rcw:begin owner=source:src_866f4aa79ff25865b46b53e840c6d35a block=evidence -->
- Repository development practice: releases to PyPI are intentional — a version bump in pyproject.toml merged via PR triggers publishing, not every merge to main. [@claim:clm_45931093f9995d612aa9104263d0b6c278ee78307ac2de6816e732e0d9423b9d]
- Repository development practice: contributors run checks via uv (uv run pytest, ruff check, ruff format --check, mypy), keep commits atomic, and add tests for behavior changes before expanding features. [@claim:clm_9a757b784a84dcdfff4e56183675f68c000e0a5b36213e9d52dddffca382274e]
- The provider catalog is data-driven: built-in entries live in src/tau_coding/data/catalog.toml, and users can add providers via ~/.tau/catalog.toml with the same schema without code changes. [@claim:clm_9b9a2699ae592f444491e392bde5ceeb84da11f359b97d8be61d597c7d16f8b2]
<!-- rcw:end owner=source:src_866f4aa79ff25865b46b53e840c6d35a block=evidence -->

## Researcher notes

