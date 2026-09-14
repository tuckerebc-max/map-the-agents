---
access: public
aliases: []
claim_ids:
- clm_4e162e1f946ed82c8252fd2ae8e299e70fb59cd6b90b047e6b24dd861b961bd0
- clm_57cae18fe09ba3e0f77ec588f7577f77af4ea4b206b96001c45aaa921978c88e
- clm_63e4d8753bed330a8626d0f876b840cac58bac1fbd4bb652c7ff9cbb837e3cfd
- clm_90afabb4a6dc2077803923501739316bc6804e2f95d174ef8d3b35c3055d4eca
- clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c
maturity: draft
page_id: pg_653ddd92cba15912911b6bfd2d931b49
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_539d3c4ead475a54b162944afabb9ec4
title: soldatov-ss/django-completion/docs/how_it_works.md @ 924dfae6094c
updated_at: '2026-09-14T04:22:22Z'
---

# soldatov-ss/django-completion/docs/how_it_works.md @ 924dfae6094c

<!-- rcw:begin owner=source:src_539d3c4ead475a54b162944afabb9ec4 block=evidence -->
- Migration completion is based on migration files on disk rather than database state, respects settings.MIGRATION_MODULES, ignores private, hidden, and non-Python files, and adds `zero` at completion time rather than storing it in the cache. [@claim:clm_4e162e1f946ed82c8252fd2ae8e299e70fb59cd6b90b047e6b24dd861b961bd0]
- When the app is in INSTALLED_APPS, its AppConfig wraps Django's command execution so a background thread refreshes the cache after manage.py runs, with a 60-second cooldown, a process-local lock, and no blocking of the triggering command. [@claim:clm_57cae18fe09ba3e0f77ec588f7577f77af4ea4b206b96001c45aaa921978c88e]
- State lives in `{project_root}/.django-completion-cache.json` (schema version 2), holding command names, app labels with local/pip origin, per-command options and help, migration names, warnings, and a generated_at timestamp. [@claim:clm_63e4d8753bed330a8626d0f876b840cac58bac1fbd4bb652c7ff9cbb837e3cfd]
- The cache is machine-specific runtime state not meant to be committed, and its format is a documented contract: additive changes do not bump schema_version, breaking changes do, and consumers must ignore unknown fields. [@claim:clm_90afabb4a6dc2077803923501739316bc6804e2f95d174ef8d3b35c3055d4eca]
- Tab completion never imports Django or touches the database; shell scripts only read the local cache and call an internal helper `django_completion._complete`, which is explicitly not stable public API. [@claim:clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c]
<!-- rcw:end owner=source:src_539d3c4ead475a54b162944afabb9ec4 block=evidence -->

## Researcher notes

