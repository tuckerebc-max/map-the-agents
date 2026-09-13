# Architecture

The workbench belongs under Stargazer / Observatory and serves Navy Yard and Tech Triangle.
Its records are observations. Downstream Observatory work can turn them into signals and
evaluation candidates, with relevance judgments kept separate from source facts.

```text
All the Agents backing feed + public research/chat leads
    -> catalog: normalized repository identity, origin/project associations
    -> sources: immutable commit + selection, verified text blobs and omissions
    -> prepare: sealed packet from the actual Research Corpus Wiki kernel
    -> small agent: proposal citing only supplied slice IDs
    -> validate/apply/audit: canonical wiki claims, locators and operation history
    -> map: compact repository pages and navigable cross-repository indexes
```

`maintain` drives collection without a model. `worker` handles one repository through
distillation, or returns a manual envelope when no trusted command is supplied. Neither
stage executes code from an observed repository.

## Data ownership

All paths below are inside `corpus/`.

| Path | Owner and contract |
|---|---|
| `catalog/` | Normalized public leads, retained origin/project associations and source metadata. |
| `sources/` | Immutable snapshots keyed by commit and selection. Omitted files and truncated trees remain explicit. |
| `wiki/` | Canonical kernel records and operations; writes go through prepare/apply. |
| `map/` | Generated orientation and linked detail pages. Human `.notes.md` pages are preserved and excluded from default search. |
| `state/catalog-cursor.json`, `state/maintenance.json`, `state/inbox.json` | Persistent fair rotation and bounded failure history. |
| `packets/`, `proposals/`, `state/packets/`, `state/workers/` | Local-only worker payloads, bindings and recovery pointers; back these up together. |
| `inbox/public/`, `inbox/private/` | Deliberately supplied lead files; the private lane is ignored by Git. |

Metadata maintenance publishes only catalog, snapshots, wiki, generated maps and specific
queue state files. It does not publish local worker recovery state. A fresh Git clone restores
the published map and metadata queue; recovering an unfinished local model job requires its
complete local backup, described in [operations](operations.md).

## Evidence and coverage

Every accepted claim cites real slices and immutable source locations. Claims identify whether
they are observations or inferences and whether their basis is documentation or inspected code.
The summary is draft orientation. Shape and linkage validation do not establish semantic truth.
Unsubmitted facets remain unknown; a lead or README alone is not a completed reverse engineering.

The main index stays within 2,000 words and repository orientation pages within 500 words.
Linked detail and secondary indexes paginate. Default query searches only the current generated
Markdown view; `--include-archive` explicitly includes historical kernel pages. Query reports
stale views and incomplete scans instead of implying complete coverage.
