# Architecture

## Modules

| Module | Responsibility |
|---|---|
| `map_agents/core.py` | Corpus layout, atomic JSON/bytes writes, the writer lock, `catalog/repos.json` and `catalog/observations.jsonl` load/save. |
| `map_agents/intake.py` | Extracts and normalizes public GitHub repository links from arbitrary text/Markdown/JSON; rejects private hosts, secret shapes and oversized input before any write. This is the only place free-text ever touches the catalog. |
| `map_agents/collect.py` | Network-bounded, budgeted collection: the `alltheagents.org` backing catalog feed and immutable per-repository source snapshots (README/docs by default, plus caller-supplied explicit paths), verified against Git blob SHAs. |
| `map_agents/wiki.py` | The only bridge to the vendored kernel. `prepare` builds a bounded packet from the active snapshot via the real `rcw` subprocess; `apply` validates a dossier proposal against that packet and applies it through the kernel; `audit` reconciles kernel records. No hand-written wiki files. |
| `map_agents/maps.py` | Renders `map/` (index, per-repo pages, classes/components/patterns/gaps/freshness indexes, paginated) and `AGENTS_CORPUS.md` from the catalog and sealed dossiers; also the bounded Markdown-only `query`. |
| `map_agents/workers.py` | `maintain` (bounded, resumable, model-free: catalog + fair snapshot queue + `needs_distillation`) and `run_worker` (one repository's packet → optional trusted-command distillation → validated apply → build), both governed by a single `Limits` object and a cooperative deadline. |
| `map_agents/automation.py` | The two hosted receivers: `receive_event` (one GitHub `repository_dispatch` event JSON file) and `receive_inbox` (file-based leads under `inbox/<lane>/<project>/<origin>.*`). Both funnel into the ordinary `intake.ingest`; neither ever runs anything from the payload. |
| `map_agents/__main__.py` | The CLI: `init intake receive inbox status catalog snapshot prepare apply audit build query maintain worker`. Every command emits one JSON object; nonzero exit codes are `WorkbenchError.code` or a small set of documented exceptions. |

## Data flow

```
free text / dispatch event / inbox file
        │  (intake.extract_links + normalize; automation strips everything else)
        ▼
catalog/repos.json, catalog/observations.jsonl        <- accumulated, idempotent, never overwritten
        │  (collect.catalog: alltheagents.org backing feed, adds "classes")
        │  (collect.snapshot: bounded README/docs/explicit-path fetch, Git-blob verified)
        ▼
sources/github/<owner>/<repo>/<commit>/<snapshot_id>/  <- immutable once written
        │  (wiki.prepare: rcw kernel builds a packet of slices from the active snapshot)
        ▼
packets/<operation_id>.json  (+ a sealed hash record)
        │  (a small agent or an explicitly configured trusted command writes a proposal
        │   citing only this packet's slice_ids; wiki.validate_proposal checks it strictly)
        ▼
wiki.apply → the real rcw kernel → wiki/  (canonical; never hand-edited)
        │  (maps.build)
        ▼
map/  (index, per-repo pages, classes/components/patterns/gaps/freshness, AGENTS_CORPUS.md pointer)
```

`workers.maintain` drives the top half of this pipeline on a fair, resumable cursor with no model
involved. `workers.run_worker` drives one repository through the bottom half; with no `argv` it
returns a manual envelope (packet + exact proposal instructions) instead of calling anything.

## Roots and ownership

`sources/` (immutable snapshots) and `wiki/` (kernel-owned) are disjoint. `state/` holds the fair
cursor, maintenance/worker receipts, and in-flight job records — committing it in the maintenance
workflow is what lets a fresh scheduled run resume fairly instead of restarting the rotation.
`packets/`, `proposals/`, and `inbox/private/` are git-ignored everywhere in the tree (`**/packets/`
etc. in `.gitignore`); only normalized links and sealed dossier claims ever leave those directories.

## Boundaries this design keeps

- No execution of anything found in source text, a proposal, or a dispatch payload; commands run
  by `worker -- <exe> <args>` are fixed at invocation time, `shell=False`, and never touch source
  text.
- Every claim in the wiki cites real evidence (`slice_ids` into a specific packet); schema validity
  is a shape check, not a correctness or human-approval claim.
- A shrinking budget or a repository whose selected paths no longer fit raises `BudgetGap` and keeps
  the prior valid snapshot pointer rather than silently degrading coverage.
- `maintain`'s per-repository failures are recorded in `failures[]` and the run still exits 0 (a
  receipt, not a crash); `worker`'s failures raise, because a caller waiting on one repository's
  distillation needs to know it did not happen.
