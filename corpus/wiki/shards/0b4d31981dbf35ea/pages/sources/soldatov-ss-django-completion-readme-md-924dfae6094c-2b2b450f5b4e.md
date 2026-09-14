---
access: public
aliases: []
claim_ids:
- clm_356267357153856747deabec21b33d446e4636bb3a78fa0af38b48c3fd84d879
- clm_4e52f806e8f3f8447e18ba1b06f266b5c7d30f926a9952858b57486b32268a2f
- clm_70aff5eb5918dd18f410efe9b79d0294a72452dbf16116dc87aad119b2babaef
- clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c
- clm_96edf60266c3351b14e406db12d31fda29dda07a1ceda46ec8d6d4c81f2d88d6
- clm_a4ed95e77fa10fcd44ae6b2a42ef32957e639ecbfbe4efba804541b6692c2095
- clm_e53466553ef54788b7351d019629dcd53f2bea8f75853039285b988307b624e9
maturity: draft
page_id: pg_9175c13ca7a657c5afdc2b2b450f5b4e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_60e787158c22502284f05fbef25f958a
title: soldatov-ss/django-completion/README.md @ 924dfae6094c
updated_at: '2026-09-14T04:22:22Z'
---

# soldatov-ss/django-completion/README.md @ 924dfae6094c

<!-- rcw:begin owner=source:src_60e787158c22502284f05fbef25f958a block=evidence -->
- Documented compatibility: Python 3.10+, Django 4.2+, bash and zsh shells, Linux and macOS expected; Windows is not officially supported though WSL with bash/zsh may work. [@claim:clm_356267357153856747deabec21b33d446e4636bb3a78fa0af38b48c3fd84d879]
- The app registers a single `autocomplete` management command with subcommands install, status, refresh, context, and uninstall, invoked as `python manage.py autocomplete ...`. [@claim:clm_4e52f806e8f3f8447e18ba1b06f266b5c7d30f926a9952858b57486b32268a2f]
- Stated limitations include bash/zsh only (fish planned), no django-admin support, no global options before the command, no custom alias support, and no database-aware applied/unapplied migration filtering. [@claim:clm_70aff5eb5918dd18f410efe9b79d0294a72452dbf16116dc87aad119b2babaef]
- Tab completion never imports Django or touches the database; shell scripts only read the local cache and call an internal helper `django_completion._complete`, which is explicitly not stable public API. [@claim:clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c]
- Repository development practice: contributors run `uv sync`, `uv run pytest -q`, `uv run ruff check .`, and `uv run ty check` after cloning the repo. [@claim:clm_96edf60266c3351b14e406db12d31fda29dda07a1ceda46ec8d6d4c81f2d88d6]
- Repository development practice: the README ships an AGENTS.md/CLAUDE.md snippet instructing agents to read the cache file instead of running `manage.py help` or grepping management/commands, and to run `autocomplete context` on first visit. [@claim:clm_a4ed95e77fa10fcd44ae6b2a42ef32957e639ecbfbe4efba804541b6692c2095]
- `autocomplete context` prints a compact markdown summary of project-local commands with flags and help plus per-app migration names; `--json` prints the full cache and `--refresh` forces a rebuild first. [@claim:clm_e53466553ef54788b7351d019629dcd53f2bea8f75853039285b988307b624e9]
<!-- rcw:end owner=source:src_60e787158c22502284f05fbef25f958a block=evidence -->

## Researcher notes

