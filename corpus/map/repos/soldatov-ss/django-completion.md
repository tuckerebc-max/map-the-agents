# soldatov-ss/django-completion

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 924dfae6094c @ 115737500698c399

## Summary (orientation draft, not independently verified)

Selected evidence records: The app registers a single `autocomplete` management command with subcommands install, status, refresh, context, and uninstall, invoked as `python manage.py autocomplete ...`. `autocomplete context` prints a compact markdown summary of project-local commands with flags and help plus per-app migration names; `--json` prints the full cache and `--refresh` forces a rebuild first.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Tab completion never imports Django or touches the database; shell scripts only read the local cache and call an internal helper `django_completion._complete`, which is explicitly not stable public API. -- evidence: [docs/how_it_works.md#L89-L92](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L89-L92), [docs/api.md#L133-L133](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L133-L133), [docs/how_it_works.md#L11-L11](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L11-L11), [README.md#L161-L170](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L161-L170)
  - [observation/documented] Migration completion is based on migration files on disk rather than database state, respects settings.MIGRATION_MODULES, ignores private, hidden, and non-Python files, and adds `zero` at completion time rather than storing it in the cache. -- evidence: [docs/how_it_works.md#L40-L40](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L40-L40), [docs/how_it_works.md#L32-L32](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L32-L32), [docs/how_it_works.md#L34-L34](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L34-L34), [docs/how_it_works.md#L36-L38](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L36-L38)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run `uv sync`, `uv run pytest -q`, `uv run ruff check .`, and `uv run ty check` after cloning the repo. -- evidence: [README.md#L202-L209](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L202-L209)
  - [observation/documented] Repository development practice: the README ships an AGENTS.md/CLAUDE.md snippet instructing agents to read the cache file instead of running `manage.py help` or grepping management/commands, and to run `autocomplete context` on first visit. -- evidence: [README.md#L84-L90](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L84-L90), [README.md#L73-L73](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L73-L73), [README.md#L78-L82](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L78-L82)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The app registers a single `autocomplete` management command with subcommands install, status, refresh, context, and uninstall, invoked as `python manage.py autocomplete ...`. -- evidence: [docs/api.md#L16-L16](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L16-L16), [README.md#L131-L137](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L131-L137), [README.md#L35-L37](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L35-L37)
  - [observation/documented] `autocomplete context` prints a compact markdown summary of project-local commands with flags and help plus per-app migration names; `--json` prints the full cache and `--refresh` forces a rebuild first. -- evidence: [docs/api.md#L65-L65](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L65-L65), [README.md#L54-L54](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/README.md#L54-L54)
- memory-state (2 claim(s)):
  - [observation/documented] State lives in `{project_root}/.django-completion-cache.json` (schema version 2), holding command names, app labels with local/pip origin, per-command options and help, migration names, warnings, and a generated_at timestamp. -- evidence: [docs/how_it_works.md#L19-L26](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L19-L26), [docs/api.md#L85-L85](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L85-L85), [docs/api.md#L83-L83](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L83-L83), [docs/api.md#L87-L118](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L87-L118)
  - [observation/documented] The cache is machine-specific runtime state not meant to be committed, and its format is a documented contract: additive changes do not bump schema_version, breaking changes do, and consumers must ignore unknown fields. -- evidence: [docs/api.md#L129-L129](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/api.md#L129-L129), [docs/how_it_works.md#L28-L28](https://github.com/soldatov-ss/django-completion/blob/924dfae6094cf7b8a3e696dc9666de904742c8b1/docs/how_it_works.md#L28-L28)
- orchestration (1 claim(s)):
More evidence: [full detail](django-completion.detail.md)

Metadata and full claim list: [full detail](django-completion.detail.md)
Human notes ([notes](django-completion.notes.md), never overwritten by build)

[Back to map index](../../index.md)
