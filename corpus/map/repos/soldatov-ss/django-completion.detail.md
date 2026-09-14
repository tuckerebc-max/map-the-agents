# soldatov-ss/django-completion -- full detail

[Back to orientation](django-completion.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/soldatov-ss/django-completion/924dfae6094cf7b8a3e696dc9666de904742c8b1/115737500698c399.json](../../../wiki/dossiers/soldatov-ss/django-completion/924dfae6094cf7b8a3e696dc9666de904742c8b1/115737500698c399.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Tab completion never imports Django or touches the database; shell scripts only read the local cache and call an internal helper `django_completion._complete`, which is explicitly not stable public API. -- evidence: [docs/how_it_works.md#L89-L92](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L89-L92), [docs/api.md#L133-L133](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L133-L133), [docs/how_it_works.md#L11-L11](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L11-L11), [README.md#L161-L170](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L161-L170) (`clm_91468b875cced83092dcf43d2a6669eb4f7d223af90c8a5d1881be43cd9b2d6c`)
- [observation/documented] Migration completion is based on migration files on disk rather than database state, respects settings.MIGRATION_MODULES, ignores private, hidden, and non-Python files, and adds `zero` at completion time rather than storing it in the cache. -- evidence: [docs/how_it_works.md#L40-L40](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L40-L40), [docs/how_it_works.md#L32-L32](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L32-L32), [docs/how_it_works.md#L34-L34](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L34-L34), [docs/how_it_works.md#L36-L38](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L36-L38) (`clm_4e162e1f946ed82c8252fd2ae8e299e70fb59cd6b90b047e6b24dd861b961bd0`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run `uv sync`, `uv run pytest -q`, `uv run ruff check .`, and `uv run ty check` after cloning the repo. -- evidence: [README.md#L202-L209](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L202-L209) (`clm_96edf60266c3351b14e406db12d31fda29dda07a1ceda46ec8d6d4c81f2d88d6`)
- [observation/documented] Repository development practice: the README ships an AGENTS.md/CLAUDE.md snippet instructing agents to read the cache file instead of running `manage.py help` or grepping management/commands, and to run `autocomplete context` on first visit. -- evidence: [README.md#L84-L90](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L84-L90), [README.md#L73-L73](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L73-L73), [README.md#L78-L82](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L78-L82) (`clm_a4ed95e77fa10fcd44ae6b2a42ef32957e639ecbfbe4efba804541b6692c2095`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The app registers a single `autocomplete` management command with subcommands install, status, refresh, context, and uninstall, invoked as `python manage.py autocomplete ...`. -- evidence: [docs/api.md#L16-L16](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L16-L16), [README.md#L131-L137](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L131-L137), [README.md#L35-L37](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L35-L37) (`clm_4e52f806e8f3f8447e18ba1b06f266b5c7d30f926a9952858b57486b32268a2f`)
- [observation/documented] `autocomplete context` prints a compact markdown summary of project-local commands with flags and help plus per-app migration names; `--json` prints the full cache and `--refresh` forces a rebuild first. -- evidence: [docs/api.md#L65-L65](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L65-L65), [README.md#L54-L54](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L54-L54) (`clm_e53466553ef54788b7351d019629dcd53f2bea8f75853039285b988307b624e9`)
- [observation/documented] The package exposes no stable public Python API for applications; it is primarily a Django management-command integration. -- evidence: [docs/api.md#L3-L3](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L3-L3) (`clm_44d7ace5bf347adac4a794687072ae1f962ffb53c3de4f6aac4a83171baa1e85`)

## memory-state (2 claim(s))

- [observation/documented] State lives in `{project_root}/.django-completion-cache.json` (schema version 2), holding command names, app labels with local/pip origin, per-command options and help, migration names, warnings, and a generated_at timestamp. -- evidence: [docs/how_it_works.md#L19-L26](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L19-L26), [docs/api.md#L85-L85](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L85-L85), [docs/api.md#L83-L83](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L83-L83), [docs/api.md#L87-L118](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L87-L118) (`clm_63e4d8753bed330a8626d0f876b840cac58bac1fbd4bb652c7ff9cbb837e3cfd`)
- [observation/documented] The cache is machine-specific runtime state not meant to be committed, and its format is a documented contract: additive changes do not bump schema_version, breaking changes do, and consumers must ignore unknown fields. -- evidence: [docs/api.md#L129-L129](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L129-L129), [docs/how_it_works.md#L28-L28](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L28-L28) (`clm_90afabb4a6dc2077803923501739316bc6804e2f95d174ef8d3b35c3055d4eca`)

## orchestration (1 claim(s))

- [observation/documented] When the app is in INSTALLED_APPS, its AppConfig wraps Django's command execution so a background thread refreshes the cache after manage.py runs, with a 60-second cooldown, a process-local lock, and no blocking of the triggering command. -- evidence: [docs/api.md#L73-L73](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L73-L73), [docs/how_it_works.md#L50-L50](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L50-L50), [docs/how_it_works.md#L46-L48](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L46-L48), [docs/how_it_works.md#L56-L56](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L56-L56) (`clm_57cae18fe09ba3e0f77ec588f7577f77af4ea4b206b96001c45aaa921978c88e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Documented compatibility: Python 3.10+, Django 4.2+, bash and zsh shells, Linux and macOS expected; Windows is not officially supported though WSL with bash/zsh may work. -- evidence: [docs/api.md#L137-L145](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L137-L145), [README.md#L149-L157](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L149-L157) (`clm_356267357153856747deabec21b33d446e4636bb3a78fa0af38b48c3fd84d879`)

## limitations (1 claim(s))

- [observation/documented] Stated limitations include bash/zsh only (fish planned), no django-admin support, no global options before the command, no custom alias support, and no database-aware applied/unapplied migration filtering. -- evidence: [README.md#L183-L188](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L183-L188) (`clm_70aff5eb5918dd18f410efe9b79d0294a72452dbf16116dc87aad119b2babaef`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

