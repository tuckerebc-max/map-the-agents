---
access: public
aliases: []
claim_ids:
- clm_356267357153856747deabec21b33d446e4636bb3a78fa0af38b48c3fd84d879
- clm_44d7ace5bf347adac4a794687072ae1f962ffb53c3de4f6aac4a83171baa1e85
- clm_4e52f806e8f3f8447e18ba1b06f266b5c7d30f926a9952858b57486b32268a2f
- clm_57cae18fe09ba3e0f77ec588f7577f77af4ea4b206b96001c45aaa921978c88e
- clm_63e4d8753bed330a8626d0f876b840cac58bac1fbd4bb652c7ff9cbb837e3cfd
- clm_90afabb4a6dc2077803923501739316bc6804e2f95d174ef8d3b35c3055d4eca
- clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c
- clm_e53466553ef54788b7351d019629dcd53f2bea8f75853039285b988307b624e9
maturity: draft
page_id: pg_b8d002230f1959b0a491abd640fad888
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bb9a7dbe414d55da8c79f80fa35692da
title: soldatov-ss/django-completion/docs/api.md @ 924dfae6094c
updated_at: '2026-09-14T04:22:22Z'
---

# soldatov-ss/django-completion/docs/api.md @ 924dfae6094c

<!-- rcw:begin owner=source:src_bb9a7dbe414d55da8c79f80fa35692da block=evidence -->
- Documented compatibility: Python 3.10+, Django 4.2+, bash and zsh shells, Linux and macOS expected; Windows is not officially supported though WSL with bash/zsh may work. [@claim:clm_356267357153856747deabec21b33d446e4636bb3a78fa0af38b48c3fd84d879]
- The package exposes no stable public Python API for applications; it is primarily a Django management-command integration. [@claim:clm_44d7ace5bf347adac4a794687072ae1f962ffb53c3de4f6aac4a83171baa1e85]
- The app registers a single `autocomplete` management command with subcommands install, status, refresh, context, and uninstall, invoked as `python manage.py autocomplete ...`. [@claim:clm_4e52f806e8f3f8447e18ba1b06f266b5c7d30f926a9952858b57486b32268a2f]
- When the app is in INSTALLED_APPS, its AppConfig wraps Django's command execution so a background thread refreshes the cache after manage.py runs, with a 60-second cooldown, a process-local lock, and no blocking of the triggering command. [@claim:clm_57cae18fe09ba3e0f77ec588f7577f77af4ea4b206b96001c45aaa921978c88e]
- State lives in `{project_root}/.django-completion-cache.json` (schema version 2), holding command names, app labels with local/pip origin, per-command options and help, migration names, warnings, and a generated_at timestamp. [@claim:clm_63e4d8753bed330a8626d0f876b840cac58bac1fbd4bb652c7ff9cbb837e3cfd]
- The cache is machine-specific runtime state not meant to be committed, and its format is a documented contract: additive changes do not bump schema_version, breaking changes do, and consumers must ignore unknown fields. [@claim:clm_90afabb4a6dc2077803923501739316bc6804e2f95d174ef8d3b35c3055d4eca]
- Tab completion never imports Django or touches the database; shell scripts only read the local cache and call an internal helper `django_completion._complete`, which is explicitly not stable public API. [@claim:clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c]
- `autocomplete context` prints a compact markdown summary of project-local commands with flags and help plus per-app migration names; `--json` prints the full cache and `--refresh` forces a rebuild first. [@claim:clm_e53466553ef54788b7351d019629dcd53f2bea8f75853039285b988307b624e9]
<!-- rcw:end owner=source:src_bb9a7dbe414d55da8c79f80fa35692da block=evidence -->

## Researcher notes

