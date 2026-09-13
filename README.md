# Map the Agents

A small, private, GitHub-first workbench that keeps compact, source-linked maps of public agent
repositories, so Navy Yard and Tech Triangle design work can check "has anyone already looked at
this" before re-researching it. It records observations and evidence — it never adopts, installs,
or executes anything it observes. A repository landing in the map is an **evaluation candidate**,
not an adoption decision.

## What is here

| Path | What it is |
|---|---|
| `map_agents/` | The package: intake, collection, the model-free maintainer, the model worker, wiki integration, map rendering, and the GitHub receivers. |
| `skills/map-the-agents/SKILL.md` | The repo-owned, lookup-first skill for design tasks. Start here for day-to-day use. |
| `vendor/research-corpus-wiki/` | Unmodified, pinned dependency that owns every canonical wiki write. See `vendor-pin.json`. |
| `.github/workflows/` | Read-only CI and the scheduled/dispatchable maintenance job. |
| `docs/` | Architecture and operations detail. |
| `scripts/demo_synthetic.py` | Offline, two-class, fully fabricated end-to-end demonstration (no real research data). |
| `scripts/verify_vendor.py` | Verifies every vendored file against its recorded Git blob and SHA-256. |
| `corpus/` (generated, not in this checkout yet) | Catalog, immutable source snapshots, the wiki, and rendered maps. Created by `init`/any write command. |

## Quickstart

```
uv run --python 3.12 --extra dev python -m pytest tests -q
uv run --python 3.12 python scripts/verify_vendor.py
uv run --python 3.12 python -m map_agents --root corpus status
```

Then read `skills/map-the-agents/SKILL.md` for the real lookup/intake/worker command recipes, and
`docs/architecture.md` / `docs/operations.md` for how the pieces fit together and how automation
runs. `AGENTS_CORPUS.md` at the repository root points into the generated map once `corpus/`
exists.

## Current state (2026-09-13)

- **Workbench build complete, full corpus population pending.** This checkout ships the pipeline,
  tests, automation, docs and skill; it does not yet contain a populated `corpus/`. A real seed of
  researched repositories is added separately after independent review.
- **No live model configured.** `maintain` (metadata-only) works today; `worker` requires either a
  small agent reading its packet or an explicitly configured trusted command — no provider SDK or
  API key is wired up, so `needs_distillation` repositories stay pending until one is.
- **Live WhatsApp is not connected.** The only supported inbound research paths are: the local CLI
  (`intake`), file-based leads under `inbox/public/` and `inbox/private/` (`inbox` command), and the
  GitHub `repository_dispatch` `research-completed` receiver (`receive` command). Anything else is
  not wired up, regardless of what a caller's text claims.
- **This repository is not yet created on GitHub.** See `docs/observatory-manifest.json` for the
  planned registration under the Stargazer Observatory once independent review and publication are
  complete.
