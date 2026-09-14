# `ade-cli` v2 — proposal

> Draft for review 2026-07-13 · Owner @mingrui · Against aide main @ 2026-07-10
> Source of the original: `docs/cli-v2-proposal.md` in aide.
>
> **Revised 2026-07-21 — the job-item store.** Doc ids are removed; the store,
> history, and every document command re-key on **job item ids**. The affected
> body sections are rewritten in place; superseded earlier decisions are marked
> where they stood. See the revision summary below for the deltas and their
> rationale.

A ground-up design of the CLI against the current ADE v2 contract. We optimize for the clearest possible story about what ADE is, not for backward compatibility with earlier iterations.

## Revision summary (2026-07-21): from doc ids to job items

The v2 store keyed everything on a content-derived **doc id** — bytes were
identity, a path only provenance, params a cache key inside one doc folder,
"last parse wins". Living with it showed the seams: the same document parsed
with different params fought over one folder; extractions went stale on every
re-parse; and the store answered "what documents exist" when users and agents
actually ask "what runs did I do". This revision re-keys the store on the
**invocation**:

- **Doc ids are gone.** The primary key is the **job item id** — a combined
  hash of *verb + source path hash + document content hash + params hash*
  (URL sources: *verb + url hash + params hash* — the CLI never sees the
  bytes; the verb prefix keeps parse and extract ids from ever colliding;
  exact formula under Identifiers). Identity is now *where the document lives ×
  what its bytes are × how it was processed*.

- **Flat store.** `~/.ade/jobs/<job-item-id>/`, one folder per job item, parse
  and extract alike. No more `docs/<doc-id>/` with params fighting inside.

- **`docs` → `history`.** `history list` shows job item ids, kind, state,
  **params**, and source; `history clear` deletes items. `docs show` is
  dropped — the viewer and `--json` list output cover inspection.

- **`extract` takes a job item id, not a doc id** — or a document path. Given a
  path, it **reuses the latest completed parse** for that path+content (and
  logs the reuse); if none exists it **runs a standalone parse job first**,
  then the extract referencing it — so the next `extract -d` of the same file
  reuses it. This deliberately supersedes v2's "no hidden auto-parse" rule —
  see the extract section for the new billing posture.

- **Parse is dedup-with-notice.** Same path + content + params ⇒ served from
  disk with an explicit "already parsed — pass `--force` to re-parse" notice;
  only `--force` re-bills.

- **`view`, `crop`, and `find` take job item ids.** `view` grows a **history
  sidebar** backed by a store-level `history.js`, re-scanned and rewritten on
  every `view` run (so manually deleted items disappear); missing viewers
  build in a background process with per-item *building…* status visible in
  the sidebar.

- **Variants replace staleness.** Params live inside identity, so parsing the
  same document with different params creates a *sibling* job item — variants
  coexist; "last parse wins" is gone. The stale-extraction machinery survives
  only for `--force` re-parse in place (which does replace artifacts under an
  unchanged id).

Known consequence, accepted deliberately: **moving or copying a file changes
its identity** (new path hash ⇒ new job item ⇒ a re-parse bills). v2 deduped
by bytes across paths; the job-item model trades that for a history that
matches how runs actually happened. The dedup-with-notice gate means the cost
is always visible before it recurs.

## The ADE v2 contract we build against

The contract facts the design leans on:

- **Two document APIs, both async job contracts.** `POST /v2/parse` and `POST /v2/extract`, each with a `/jobs` surface (create → 202 + job id, poll, per-caller job list). Canonical paths are bare `/v2/*` on every host.

- **Execution tiers.** Async `service_tier`: `priority` (full price, fast lane — same lane as sync) or `standard` (0.5× for parse, slower lane). Async caps: 6 000 pages / 1 GiB PDFs. No job cancel exists; submitted work always completes and bills.

- **Parse returns markdown plus one structure tree with grounding inline** *(re-verified 2026-07-21)*: the full document as `markdown`, and a `structure` tree (`document → page → element → table_cell`) where **every node carries its grounding inline** — `{page, range, box}`, with `range` a `[start, end)` code-point slice of the markdown and `box` **normalized `{xmin, ymin, xmax, ymax}` fractions of page size in `[0, 1]`** (multiply by any raster's dimensions for pixels). Leaf elements additionally carry `atomic_grounding` — finer segments (visual lines today), each a full `{page, range, box}`. There is no separate grounding tree and no pixel/dpi coordinate space. Metadata carries `job_id`, resolved `version`, `failed_pages`, `credit_usage` + itemized breakdown.

- **The complete customer `options` object for parse** *(re-verified 2026-07-21; sent as a JSON-serialized string in the form data)*:
  - `pages` — JSON array of **1-indexed** integers (not a range-string grammar); values < 1 are 422; omitted ⇒ all pages. Filtered-out pages don't appear in `structure`, but `metadata.page_count` still counts them and billing excludes them.
  - `atomic_grounding` — bool, default `true`; `false` omits the `atomic_grounding` field from every node.
  - `inline_markdown` — bool, default `false`; `true` adds each node's own `markdown` slice inline (root, pages, elements, cells).
  - `blocks.<type>.markdown` — bool, default `true`, per element type (`text`, `table`, `figure`, `marginalia`, `attestation`, `logo`, `scan_code`, `card`); `false` suppresses that type's markdown (range collapses to zero-length).
  - `blocks.table.format` — `"html"` (default) or `"markdown"`.
  - `password` — accepted in shape, **always 422** (`encrypted_pdf_unsupported`).
  - **Unknown keys at any nesting level are 422** (`extra="forbid"`, error names the key, envelope `{code: "validation_error", message}`). The legacy `dpi`, `grounding`, and `blocks.<type>.caption` options are **retired** and rejected this way.

- **Extract takes markdown + a JSON schema** and returns the extraction plus per-field `{value, spans}` metadata — spans are offsets into the input markdown; `null` spans mark synthesised values. Parse markdown ends with a `<!-- doc_id=… -->` trailer extract reads and echoes.

- **Model registries** are enforced at submit: parse `dpt-3-pro` family (`dpt-3-pro-latest` default alias), extract `extract-latest`.

## Design principles

1. **The store is the source of truth for work done.** `~/.ade` is the CLI's real API. Only `parse` and `extract` create billable work, and both persist everything they produce as a job item; every other document command is a read model over the store. (`org` reads account state from the server and never touches job items.)

2. **Commands are guarantees, not actions.** `parse` means "ensure this exact run exists", not "fire a request". Idempotent, resumable, interrupt-safe.

3. **Judgment stays in the calling agent.** The CLI does deterministic, mechanical work: parse, persist, project, search, render, total. Ranking, selection, and synthesis do not live here.

4. **One transport, one schema.** v2 endpoints only, async jobs only, grounding-tree projection only.

5. **Two audiences, explicit artifacts.** Agents get JSON + `elements.json`; humans get one explorable HTML artifact per job item, a history sidebar to move between them, and a receipt.

## Command surface (revised 2026-07-21)

```
# credentials & CLI lifecycle
ade auth                     save/inspect credentials (login/status/logout)
ade version                  print version
ade help [COMMAND]           whole-surface reference in one call (agent bootstrap)
ade update                   check for and install a newer CLI release

# network verbs — the ADE job contracts
ade parse -d FILE|--document-url URL
        [--tier priority|standard]   default: priority (full price, fast lane)
        [--wait SECONDS]             default: 600; 0 = submit & return
        [--pages SPEC]               convenience: page spec ("1-5,8") → the
                                     1-indexed pages array
        [--options JSON]             full v2 ParseOptions pass-through
                                     (atomic_grounding, inline_markdown,
                                     blocks.<type>.markdown, blocks.table.format);
                                     unknown keys are rejected by the server (422)
        [--model VERSION]            default: dpt-3-pro-latest
        [--force]                    re-parse the same job item in place (re-bills)

ade extract JOB_ID|-d FILE|--markdown FILE|--markdown-url URL
        --schema FILE|JSON
                                 input is exactly ONE of:
        JOB_ID                       a parse job item id (or unambiguous
                                     prefix); the extract job item records a
                                     reference to it (parse/ref.json)
        -d FILE|--document FILE      extract by document path: reuse the latest
                                     completed parse job of this path+content
                                     (logged, referenced), else run a
                                     standalone parse job first, then extract
        --markdown FILE|--markdown-url URL
                                     escape hatch: extract from markdown
                                     that did not come from parse
        [--tier priority|standard]   same tier posture as parse
        [--wait SECONDS]             same wait semantics as parse
        [--model VERSION]            default: extract-latest
        [--strict]                   v2 ExtractOptions pass-through
        [--force]

# local read models
ade history list             job items: id, kind, state, params, source
ade history clear JOB_ID|--all
                                 delete stored job items

ade find --job JOB_ID QUERY  search a parse job item's elements
        [--regex] [--type T] [--page N] [--element-id ID]...

ade view JOB_ID              build the job item's self-contained HTML viewer
        [--element-id ID]            emit deep link (view.html#element=ID)
        [--open]                     open in browser
                                 every run re-scans the store, rewrites
                                 history.js, and backgrounds missing builds

ade crop JOB_ID --element-id ID
        [-o PATH] [--dpi N] [--open]
                                 render one element's region as PNG

# org management entrance
ade org usage                org-level credits/plan   (needs an ADE usage API)
ade org jobs                 server-side job index for this API key (backed today)
ade org limits               rate-limit config/budget (needs an ADE limits API)
```

Eleven commands in four bands: credentials & CLI lifecycle (`auth`, `version`, `help`, `update`), the two network verbs (`parse`, `extract`), local read models (`history`, `find`, `view`, `crop`), and the org management entrance (`org`).

## `help` and `update` — CLI lifecycle

- **`help`** prints the complete command reference — every command, flag, exit state, and the store layout — in one call (`--json` for a machine-readable schema). Per-command `--help` exists as usual; the point of `help` is the **agent bootstrap**: one invocation teaches an unfamiliar agent the whole surface without N round trips. SKILL.md's "first move: discover the CLI" becomes exactly one command.

- **`update`** checks the release channel for a newer CLI and self-updates on confirmation. A demo CLI drifts against a moving backend unless staying current is one command; `update` plus registry-aware error messages ("unknown model — run `ade update`?") keeps installed copies honest. Mechanism (uv/pipx/pip) is a tracked detail.

## `parse` — the ensure-parsed guarantee

A state machine over the store, keyed by the **job item id** (source path ×
content × params — see Identifiers):

```
absent    → submit async job (multipart → POST /v2/parse/jobs),
            write claim ticket BEFORE first poll, poll with backoff,
            finalize artifacts, exit ready
pending   → resume polling the recorded job — never resubmits, never re-bills
complete  → serve summary from disk, zero API calls, with an explicit
            already-parsed notice (--force overrides)
failed    → report reason once, mark ticket; the NEXT run resubmits fresh
expired   → poll 404s (server retention passed) → treat as absent, resubmit
```

Decided semantics:

- **Blocking by default.** Submit + poll inside one command; artifacts on disk when it exits ready. `--wait 0` returns right after submit (claim ticket saved).

- **Async-only transport, `priority` tier default.** Replacing the sync route must not change latency class or price (sync was lane-2 at 1.0×; async `priority` is the same lane at the same price). `--tier standard` is the deliberate half-price knob for batch work. We always send `service_tier`; never the deprecated `priority` field spelling.

- **Interrupts are free.** Ctrl-C stops the *waiting*, never the work — there is no server cancel, and interrupted jobs still bill. The claim ticket makes re-running the same command the recovery gesture; on interrupt the CLI prints `job <id> continues server-side; re-run this command to collect`.

- **Wait expiry is a normal outcome, not an error.** Exit carries a machine-readable `{status: "pending", job_id, job_item_id}` payload and a distinct non-zero exit state ("artifacts not ready ≠ failure"); the recovery gesture is again the same command.

- **Dedup-with-notice** *(revised 2026-07-21)*. Same source path + same bytes
  + same params ⇒ the run already exists; the CLI serves the stored summary
  free and says so explicitly:
  `already parsed — job item <id> (completed <ts>); pass --force to re-parse.`
  Only `--force` triggers a new server job, which **replaces this job item's
  artifacts in place** (same id, new server `job_id`) and marks the extract
  job items referencing it stale.

- **Params are part of identity, not a cache key** *(revised 2026-07-21)*.
  Different `--pages/--options/--model/--tier` on the same file ⇒ a **different
  job item id** ⇒ a sibling folder. Variants coexist in history; nothing is
  silently replaced. v2's "one live parse per doc — last parse wins" is
  retired along with the doc folder it governed.

- **No user-facing `--timeout`.** Transport guards are internal. `--wait` clocks the poll phase only; the upload always runs to completion (a wait deadline must not abort a 90 %-done 1 GiB upload — no job exists until submit returns).

- Summary surfaces the new metadata: `job_id` (billing correlation), resolved `version`, `failed_pages` / partial results, `credit_usage` + breakdown, tier — plus the job item id and store path, and runnable `next:` hints (`view <job-item-id>`, `extract <job-item-id> --schema …`).

## `extract` — schema extraction on the same guarantee machinery

`POST /v2/extract` is a job contract like parse (async `/jobs` create + poll + list, same envelope), so `extract` inherits the entire `parse` lifecycle for free: ensure-semantics, claim tickets, blocking with `--wait`, ctrl-C = stop waiting not working, pending as a non-error, `--tier` posture. What differs is the input/output shape and where the results live *(input model revised 2026-07-21)*:

- **Input: a parse job item id, a document path, or bring-your-own markdown.**
  Exactly one of — and in every case the result is a **top-level extract job
  item under `jobs/`**; extractions never nest inside parse folders
  *(clarified 2026-07-21)*:

  1. **`extract JOB_ID --schema …`** — the primary agent path. `JOB_ID` names
     a completed parse job item; the CLI sends its `parse.md` as the markdown
     (the `<!-- doc_id=… -->` trailer gives the server-side link between the
     two calls for free). The extract job item **references** the parse via
     `parse/ref.json` — parse artifacts are never copied (decision 8: one
     copy of ground truth; `history clear` of the parse cascades, so refs
     never dangle).

  2. **`extract -d FILE --schema …`** — the human path. The CLI hashes the
     file and looks for the **latest completed parse job** of that
     path + content (any params; newest `completed_at` wins). If one matches,
     it is **reused** and the reuse is logged in the summary
     (`reused parse job item <id> (model …, completed <ts>)`) — no parse is
     billed; the extract item references it like case 1. If none exists, the
     CLI **runs a standalone parse job first** (default parse params) — a
     normal top-level parse item, exactly as if the user had run `parse -d` —
     then the extract job referencing it: two billable jobs, both itemised in
     the summary. *(Revised 2026-07-21, superseding the embedded-parse
     shape: decision 10.)* There is no private/embedded parse anymore — every
     parse the CLI ever runs is a reusable job item, so back-to-back
     `extract -d` runs on a never-parsed document bill the parse exactly
     once. *This supersedes v2's "no hidden auto-parse" decision:* the path
     form is explicitly a convenience verb, and the summary's credit
     breakdown keeps the bill legible; the parse-reuse rule keeps repeat
     invocations one-bill.

  3. **`--markdown FILE` / `--markdown-url URL`** — the bring-your-own-markdown
     escape hatch (any parser's output works, per the contract). The input
     markdown is **copied into the extract job item** as `markdown.md`
     (decision 9: spans index exactly those bytes; for `--markdown-url` the
     CLI materializes the response's echoed markdown — it never had a local
     file). No `parse/` at all: evidence degrades to spans-only (there is no
     grounding to join against) and `view` renders the markdown pane alone.
     The "sources referenced, never copied" rule stays scoped to page-image
     documents.

- **Identity.** The extract job item id follows the same formula as parse,
  with one addition *(build finding, 2026-07-21)*: a parse-backed extraction
  includes the **referenced parse job item id** in its params hash, so
  extractions of two parse variants never collide (see Identifiers).
  Same parse, same schema, same params ⇒ dedup-with-notice, exactly like
  parse; `--force` re-extracts in place.

- **Staleness** now has one cause: a `--force` re-parse replacing a parse
  item's artifacts under an unchanged id. Referencing extract items record the
  server `job_id` of the parse generation they ran against; on mismatch they
  are stale — kept, badged, re-extracted on next use, never silently served.
  Parse variants (different params) are *siblings*, not replacements, so they
  never stale anything.

- **Output.** `extraction` (the JSON matching the schema) plus `extraction_metadata` — the same shape with per-field `{value, spans}`, where `spans` are `[start, end)` offsets into the markdown and `null` marks values the model synthesised rather than quoted. Persisted verbatim.

- **Field→box evidence is a local join.** Extraction spans and `elements.json` spans index the *same* markdown string, so the CLI projects field-level visual evidence offline: field → spans → overlapping elements → boxes/pages, stored as `evidence.json`. This is exactly the span→box resolution `/v2/workflow`'s ground step performs server-side — we get it from artifacts we already store, per job item, per field, with no extra API call. Synthesised fields (null spans) are reported as *ungroundable* — surfaced, never silently dropped.

- **Rate-limit posture note.** The async extract route is worker-paced (never 429s at submit) — one more reason async-only transport is the right default for both verbs.

`/v2/workflow` (server-side parse → extract → ground pipeline) stays **out of scope**: the CLI decomposes the same story into `parse` + `extract` + the local join, and keeps every intermediate artifact inspectable in the store — which is the demo's point.

## `history` — the read model over the store *(replaces `docs`, 2026-07-21)*

`history list` is the one flat answer to "what runs exist here":

- **One row per job item** — id, kind (`parse` | `extract`), state
  (`parsed | extracted | pending | failed | unreadable | markdown`),
  **params** (compact: model, pages, tier for parse; schema field list +
  model for extract), and source. Extract items that reference a parse item
  render as indented child rows beneath it (linkage from `parse/ref.json`);
  markdown items render flat. `--json`
  emits the full records (params verbatim, timestamps, parent linkage,
  artifact index) — everything `docs show` used to answer.

- **`history clear JOB_ID|--all`** deletes job item directories under the
  store lock. Clearing a parse item **cascades with notice** to the extract
  items referencing it (`cleared <id> + N dependent extracts`) — the store
  never holds dangling refs (decision 11). Manual folder deletion is also
  tolerated: the store is re-scanned by every `view`/`history` run, so
  removed items vanish from listings and orphaned referencing extracts
  degrade to an explicit parse-missing state.

- **`docs show` is dropped.** Its two audiences are better served elsewhere:
  humans get `view` (receipt header, artifacts, extraction layers), agents
  get `history list --json` plus direct artifact reads from the printed
  store path.

- Zero API calls, like every read model; states derive from tickets and
  artifacts on disk.

## `view` — one explorable artifact per job item, with history navigation

Builds `~/.ade/jobs/<job-item-id>/view.html`, fully self-contained for its
own document data (page images base64-embedded, element data inlined, vanilla
JS, no CDN, works from `file://`) — plus, new in this revision, a **history
sidebar** shared across all viewers.

**Architecture: one generic template, per-item snapshots, built lazily.** The viewer is a single HTML/JS template maintained in the CLI package — written once, instantiated per job item by stamping in that item's data. `parse`/`extract` never build HTML (most runs are never viewed); `view` builds on demand and records the artifact fingerprints it was built from, rebuilding only when the store changed. The document payload is a **snapshot by design**: `file://` sandboxing blocks runtime `fetch()` of local data, and a snapshot keeps the artifact shareable and evidentially stable. Refresh = run `view` again.

**What a viewer shows** depends on the item's kind *(amended 2026-07-21,
implementation review)*:

- a **parse job item** renders its **parse only** — a document can carry
  many extractions and the viewer can't guess which one the user means, so
  extraction layers live in the extract items' own viewers (side benefit:
  parse artifacts stop rebuilding when extractions come and go);
- a **referencing extract item** mints its **own light `view.html`** — URL
  identity per job item — carrying its parse pane's data inline but **no
  page imagery**: images ride in at runtime from the referenced parse
  item's **`pages.js` sidecar** (a JSONP include, the same `file://` trick
  as history.js), rendered once per parse item at default params. One copy
  of a document's imagery however many extractions cite it; a light
  artifact that travels without the store degrades to explicit
  imagery-unavailable placeholders naming the cause and the recovery
  (re-run `view`, or share the parse item's view.html for an image-bearing
  copy). *(Supersedes the earlier resolve-to-parent rule.)*
- a **markdown-only item** renders the markdown pane alone, in its own
  (full) `view.html`;
- extract-kind viewers open on the **Extract tab** — that's what the run
  is; an explicit deep link still wins.

**The history sidebar** *(new, 2026-07-21)*:

- Every `view` run **re-scans `~/.ade/jobs/`** (so manually deleted folders
  drop out) and rewrites **`~/.ade/history.js`** — a JSONP-style read model
  (`window.__ADE_HISTORY__ = {generated_at, items: […]}`; a plain `<script>`
  include works from `file://` where `fetch()` does not). Each item carries
  id, kind, state, source name, compact params, parent linkage, viewer
  status (`built | building | none`), and a store-relative `href` to its
  `view.html`. Because `history.js` *executes* as script, its payload is
  emitted only by a strict JSON serializer with `</` escaped (the same
  discipline as the viewer's inline data block — never string
  concatenation), and the sidebar renders every field as text nodes, never
  `innerHTML`: store-controlled strings (source paths, schema names, field
  values) must have no path to becoming markup or code.

- Each built `view.html` includes `history.js` by relative path and renders
  the sidebar from it: all job items, current one highlighted, click to
  navigate to a sibling viewer.

- **Background builds with visible status.** After serving the requested
  item, `view` spawns a detached background builder that walks the store and
  builds every missing/stale viewer, flipping each item's `history.js`
  status `none → building → built` as it goes (per-item claim under the item
  lock; a claim whose process died is reclaimed). Sidebar entries that are
  `building` render a *building…* badge instead of a link; the sidebar
  re-polls `history.js` every few seconds (re-injected `<script>` tag —
  allowed from `file://`) so links go live without a manual rebuild.
  `--no-sidebar-sync` (tracked detail) opts out of the background pass.

**Source access is fail-safe, never duplicated.** Page images are rendered from the source document at build time via the recorded source path — the store never copies the source (review decision: reference, don't duplicate). If the source has been moved or deleted, or the item was parsed from a URL, `view` still builds: the markdown pane, element data, and extraction overlays all come from stored artifacts; the page pane degrades to an explicit "source unavailable" notice with boxes listed textually. Rendering weakens gracefully; the build never fails for a missing source.

- **Two synced panes.** Left: rendered pages with box overlays, color-coded by element type, toggles for type filter / line-level `parts` / table-cell boxes. Right: markdown mapped by span. Hover or click either side highlights the counterpart (`id ↔ span ↔ box` comes straight from the grounding tree).

- **Deep links are the agent contract.** `view.html#element=<id>` scrolls to and flashes the cited element in both panes; `#extract=<id>&field=<name>` selects an extraction layer and field. Agent answers cite element ids and end with one link per job item instead of a pile of PNG paths.

- **Header receipt.** Model snapshot, page count, failed-page badges, server `job_id`, credits + breakdown, params.

- **Size posture.** Embed pages at modest dpi (~120) with a page cap; `--pages`/`--dpi` override. A shareable artifact that survives being attached to Slack beats a lean one that breaks when sidecar files don't travel. (The sidebar degrades when `view.html` travels without the store — `history.js` missing ⇒ sidebar hidden, document panes untouched.)

- **Extraction overlay.** Stored extractions render as selectable layers on the same panes: a side rail lists each extraction (schema name/fingerprint); selecting one highlights its fields' boxes (from `evidence.json`), synthesised (ungroundable) fields visibly badged, stale extractions (post-`--force` parse) badged as such.

## `crop` — one element's region as PNG *(takes a job item id)*

`ade crop JOB_ID --element-id ID [-o PATH] [--dpi N]` renders a single
element crop through the raster pipeline — for multimodal agents that need to
*look at* evidence mid-reasoning. `JOB_ID` is a parse job item (or an extract
item with a contained/referenced parse); element ids come from `find` or
extraction evidence. Same fail-safe rule as the viewer's page pane, but
stricter: a crop with no source is an error — never a stale image. Crops are
derived artifacts, stored under the job item's `crops/` unless `-o` says
otherwise.

## `find` — element search for agents

**Decided: keep.** Pure local filtering over a parse job item's `elements.json` — no network, no ranking. Its role is **id discovery**: it closes the loop between `parse` (which manufactures element ids) and `view`/`crop`/citations (which consume them).

- **Filters, all exact:** positional substring query (case-insensitive), `--regex`, `--type` (element type — `table_cell` matches make "cite the precise cell" mechanical), `--page`, `--element-id` (resolve known ids), `--limit`. `--job` is repeatable for multi-item QA; matches always carry their `job_item_id`.

- **Output is the citation currency**, one record per match: `{job_item_id, element_id, type, page, box, text}` — directly consumable by `view --element-id`, `crop`, deep links, and answer citations. Results in document order (page, then reading order), never ranked.

- **Why a verb instead of jq:** grep returns lines, `find` returns records — the agent never re-joins matched text back to ids/boxes, and never loads `elements.json` into its context window. It is also the only search SKILL.md can rely on in every agent environment (no jq, no bash, Windows). Anything resembling relevance ranking is out of scope by principle #3: selection is the agent's job.

## `org` — the management entrance

The terminal-side entrance for managing the ADE SaaS account, not a local ledger (per review: tracking only what this machine spent is pointless — accounts are shared across people, machines, and CI). `usage` is the flagship view; the group is shaped to grow:

| Subcommand | What it shows | Backend today |
|---|---|---|
| `org usage` | org credits over a period, by model / tier / day; plan quota + remaining | **missing** — no customer usage/quota API exists in the gateway (verified); this section doubles as the requirements sketch for the product ask |
| `org jobs` | the server-side async job index for this API key: pending / processing / completed / failed, cross-machine | **exists** — `GET /v2/parse/jobs` + `GET /v2/extract/jobs` (per-caller, ownership-gated) |
| `org limits` | rate-limit configuration and current budget (hourly async page bucket, per-minute sync) | **missing** — limits live in gateway config; no read API |
| `org keys` (candidate) | API key inventory/rotation | **missing** — likely stays console-only; listed to scope the entrance, not to promise it |

Posture:

- **Ship `org jobs` first** — it's backed today and gives the claim-ticket model its account-wide counterpart: local tickets say what *this machine* awaits; `org jobs` says what *the key* has in flight anywhere.

- **`org usage` ships when the backend endpoint lands.** The demo repo files the API ask with a concrete requirements sketch (period filter, group-by model/tier, plan quota + remaining) — a documented gap with a waiting consumer is deliberate product feedback.

- **No local-ledger fallback.** Per-run receipts already live where they belong: the `parse`/`extract` summaries and the `view` header.

## Storage layout *(revised 2026-07-21)*

Three storage principles govern everything below:

1. **Indexed by invocation.** Every parse or extract run lives under its
   **job item id** — source path hash × content hash × params hash. The same
   run (same file at the same path, same bytes, same params) always resolves
   to the same folder and is served from it; any of the three changing means
   a *different* job item, side by side with the old one. Job items are
   immutable except under `--force`, which re-runs *in place*.

2. **Staleness follows dependency edges — and only `--force` creates them.**
   An extraction nested under a parse item records the server `job_id` of the
   parse generation it ran against; a `--force` re-parse mints a new
   generation and marks it stale — kept, badged, re-extracted on next use.
   Parse variants are siblings, never replacements, so nothing else stales.
   A `--markdown` extraction has no parse edge and can never go stale — and,
   symmetrically, can never have box evidence.

3. **Raw is truth, derived is disposable.** Raw API responses are stored
   verbatim and never edited; every index (`elements.json`, `evidence.json`,
   `history.js`, `view.html`) is recomputable from them.

The store is **fully flat** *(clarified 2026-07-21)*: every run — parse or
extract, however invoked — is one top-level folder under `jobs/`. An extract
item's relationship to its parse is expressed *inside* the extract folder, in
exactly one of two shapes — parse-backed (a reference, never a copy) or
markdown-only *(the embedded-parse third shape was dropped 2026-07-21;
decision 10)*:

```
~/.ade/
  config.json                      endpoint only (default is never pinned)
  credentials.json                 active credential (mode 0600; written by
                                   `auth login` — never read from config.json)
  history.js                       sidebar read model over jobs/ (JSONP:
                                   window.__ADE_HISTORY__ = {…}); rewritten by
                                   every `view`/`history` run from a fresh scan

  jobs/                            FLAT: one folder per job item, siblings all
    │                              — never nested under each other
    │
    ├─ <parse-job-item-id>/        ── kind: parse ──────────────────────────
    │    meta.json                 kind, provenance (source path/URL), params,
    │                              state, timestamps, artifact index
    │    job.json                  claim ticket: server job_id, tier,
    │                              submitted_at, state, generation
    │    parse.json                raw v2 ParseResponse (ground truth)
    │    parse.md                  markdown (keeps the doc_id trailer that
    │                              extract reads)
    │    elements.json             flat projection of the structure tree
    │                              (grounding inline), stamped with its
    │                              generation's server job_id
    │    view.html                 built lazily by `view` (source never copied
    │                              here — page renders resolve the recorded
    │                              source path)
    │    crops/                    PNG crops (derived, recomputable)
    │
    ├─ <extract-job-item-id>/      ── kind: extract, parse-backed
    │    meta.json  job.json          (`extract JOB_ID`, or `extract -d` —
    │    extract.json                 which reuses the latest parse of that
    │    evidence.json                path+content or runs a standalone parse
    │    parse/                       job first; either way it references) ──
    │      ref.json                {job_item_id, parse server job_id,
    │                              direct?} → the referenced parse job
    │                              above; artifacts are never copied.
    │                              direct: true records that this extract
    │                              invocation created the parse (provenance,
    │                              not ownership — the parse is a normal
    │                              standalone item). This item's own
    │                              view.html is a LIGHT artifact reusing the
    │                              parse item's pages.js imagery sidecar
    │                              (see the view section;
    │                              evidence.json is the local span→box join:
    │                              per field {value, spans, element_ids,
    │                              pages, boxes | ungroundable})
    │
    └─ <extract-job-item-id>/      ── kind: extract, `--markdown FILE` /
         meta.json  job.json          `--markdown-url URL` ──────────────────
         markdown.md               the input markdown, copied in — spans
                                   index exactly these bytes (for URLs, the
                                   response's echoed markdown materialized)
         extract.json
         evidence.json             spans-only (no grounding to join against)
         view.html                 markdown pane alone; no parse/ at all
```

### Identifiers *(revised 2026-07-21)*

The **job item id** is the CLI's local primary key — one id per invocation
identity:

```
# local sources (a file path; markdown bytes for --markdown FILE)
source_hash   = sha256(resolved absolute path)
content_hash  = sha256(document bytes)          # markdown bytes for --markdown items
job_item_id   = sha256(verb + ":" + source_hash + ":" + content_hash
                       + ":" + params_hash)[:16]

# URL sources (--document-url, --markdown-url) — the CLI never sees the
# bytes before submit, so there is no content component (clarified 2026-07-21):
url_hash      = sha256(URL string)
job_item_id   = sha256(verb + ":" + url_hash + ":" + params_hash)[:16]

params_hash   = sha256(canonical JSON params)   # parse: {model, options, tier}
                                                # extract: {schema, model, options,
                                                #   + parse_job_item_id when the
                                                #     extraction references a parse}
```

**Extract identity includes the referenced parse item id** *(build finding,
2026-07-21)*: a parse-backed extraction reuses the parse item's identity
components verbatim and adds the parse job item id to its params hash.
Without it, extractions of two parse *variants* of the same document share
source × content × extract-params and collide on one id — silently re-running
each other in place, violating "variants coexist; nothing is silently
replaced". Every parse-backed extraction carries the linkage — `extract -d`
with no reusable parse runs a standalone parse job first and references it,
so there is no unlinked parse-backed form. Only `--markdown` /
`--markdown-url` items (no parse) hash without linkage:
`extract : source : content : extract-params` (or the URL shape) alone —
safe because their content hash *is* the markdown the spans index. Consequence: the same
`extract -d` command re-run after a newer parse variant became "latest" mints
a sibling extraction (different parse ⇒ different markdown ⇒ different run)
rather than deduping against the old one.

Consequence for URL items: identity is the URL × params, so a re-run dedups
against the stored item even if the remote content has changed since — the
CLI cannot detect remote drift; `--force` is the refresh gesture.

The verb prefix keeps parse and extract ids from ever colliding; truncated
SHA-256 keeps prefixes typeable while collisions stay out of practical reach.
The same two shapes cover all extract input forms — parse-backed and
markdown items derive their ids the same way (`--markdown FILE` uses the
local-source shape with the markdown bytes as content; `--markdown-url` uses
the URL shape).

Two *server* identifiers are recorded but never keyed on: `metadata.job_id`
(server-minted per request; billing correlation and the staleness edge, in
`job.json`/`meta.json`) and the `doc_id` in the parse-markdown trailer
(server-side document identity; echoed by extract as `metadata.doc_id`).

### Job item id resolution *(replaces REF resolution, 2026-07-21)*

Commands that read the store (`view`, `crop`, `find`, `history clear`,
`extract JOB_ID`) take a **job item id or an unambiguous prefix** (floored at
8 characters in printed hints). Nothing else: with params inside identity, a
path or source name may legitimately match several sibling items, so path
lookup is no longer a resolution rule — the remediation for "I have a path,
not an id" is `ade history list` (filterable, params visible) or the
convenience verbs that accept paths outright (`parse -d`, `extract -d`).
Unknown or ambiguous ids error with candidates listed.

Consequence, by design: **identity is the invocation** — editing a file, moving
it, or changing params each mint a new job item; the old item and its evidence
stay intact, still true of the run they were computed from.

### Idempotency, by layer *(revised 2026-07-21)*

Storage identity is idempotent by *source × content × params* (same triple ⇒
same directory, always). The `parse` and `extract` guarantees are idempotent
over the same key: an exact match is served from disk with the
already-done notice; any component differing ⇒ a new job item beside the old;
`--force` alone re-runs an existing id in place.

### File taxonomy

- **Raw API responses** (`parse.json`, `extract.json`) — verbatim ground truth, never edited. Everything else can be rebuilt from these (plus the source).

- **Derived indexes** (`elements.json`, `evidence.json`, `view.html`, `history.js`) — recomputable projections, kept because agents and the viewer read them repeatedly. `elements.json` is the flat projection of the response's structure tree (grounding is inline on every node): one record per element — so consumers grep one array instead of walking trees. "Element" is the v2 API's own vocabulary — the CLI's nouns match the API's. `history.js` is the store-level projection the sidebar reads; it is regenerated from a directory scan, so it heals after manual deletions.

- **Bookkeeping** (`meta.json`, `job.json`) — CLI state: provenance, params, claim tickets, viewer-build status.

## Non-goals

- **Legacy/pre-v2 parse endpoints, dual schemas, sync transport.** The CLI speaks the v2 job contracts only. *Gate before launch:* run `eval/` against `dpt-3-pro-20260710` to validate dense-table coverage, so dropping the legacy fallback is a conscious call.

- **`/v2/workflow` and `/v2/ground`** *(the latter added 2026-07-21)*. Both decomposed CLI-side into `parse` + `extract` + the local span→box join, keeping every intermediate inspectable and costing zero extra API calls (see `extract` and the re-verified addendum).

- **Source duplication.** The store holds references and derived artifacts, never document copies (see Decisions).

- **Semantic ranking** in `find` — out by principle #3. *(The v2 "variant
  archiving" non-goal is retired as of 2026-07-21: params-in-identity makes
  parse variants first-class siblings; comparison/eval tooling over them
  still lives in `eval/`, not here.)*

- **Cross-path dedup.** The job-item model deliberately does not dedupe the
  same bytes parsed from two paths; the dedup-with-notice gate keeps the
  repeat cost visible instead.

## Decisions from review (2026-07-13)

**1 · Sources are referenced, never copied.** `view` and `crop` resolve the recorded source path at render time; if the source is gone (or the item came from a URL), rendering degrades fail-safe — stored artifacts (markdown, elements, extractions) always render; page images show "source unavailable". The build never fails on a missing source.

**2 · `find` stays** — the deterministic id-discovery verb (see section).

**3 · `usage` is org-level, under the `org` management entrance.** The local-only ledger is dropped as pointless; `org jobs` ships first (backed today), `org usage` when the backend usage API lands (product ask filed with requirements).

## Decisions from revision review (2026-07-21)

**4 · `history clear` stays** alongside `history list` — a safe, locked
deletion path; manual folder deletion is tolerated because every scan-backed
read model (listings, `history.js`) regenerates.

**5 · `find` moves to job ids** (`--job`), consistent with `view`/`crop`/
`extract`.

**6 · Sidebar builds run in the background with visible status.** `view`
never blocks on sibling builds; `history.js` carries per-item
`built | building | none` status, the sidebar badges *building…* and
re-polls, and links go live as the background builder finishes each item.

**7 · The proposal is revised in place** (this document); superseded v2
decisions are marked where they stood rather than erased.

**8 · The store is fully flat, and extract items *reference* their parse**
*(clarified 2026-07-21)*. Extractions never nest inside parse folders — every
job item is a top-level sibling under `jobs/`. Every parse-backed extract
item holds `parse/ref.json` (job item id + parse server job_id), never a
copy: one copy of ground truth, no N× duplication of large parse artifacts
across a document's many extractions, and staleness stays a job_id
comparison.

**9 · `--markdown` input is copied into the extract item** (`markdown.md`).
The markdown *is* the extraction's input contract — spans index exactly those
bytes — and for `--markdown-url` the CLI never had a local file. The
"sources referenced, never copied" rule stays scoped to page-image documents.

**10 · A fresh `extract -d` runs a standalone parse job, then references it**
*(revised later on 2026-07-21, superseding this decision's first form)*. The
embedded-parse shape is dropped: when no reusable parse exists, the CLI runs
a normal top-level parse job (default params) and the extract references it —
identical to `parse -d` then `extract JOB_ID`. Every parse the CLI ever runs
is therefore reusable, the reuse pool is simply "all parse job items", and
repeated `extract -d` on a never-parsed document bills the parse exactly
once. *(First form — embedded parses, invisible to reuse, re-billing on
repeat — was accepted earlier the same day and retired by this revision;
its double-bill consequence is gone.)*

**11 · `history clear` of a parse item cascades with notice** to the extract
items referencing it — the store never holds dangling refs. Orphans from
*manual* deletion degrade to an explicit parse-missing state on the next scan.

**12 · Extract identity includes the referenced parse item id** *(build
finding from #58's review)*. The Identifiers formula alone let extractions of
two parse variants collide on one id and silently re-run each other in place.
Every parse-backed extraction adds the parse job item id to its params hash
(with decision 10's revision, all parse-backed extractions reference);
`--markdown` items carry no linkage.

## Tracked implementation details

Deliberately undecided until build time; each is locally reversible.

- pending exit code value
- poll cadence (start ~1 s, ×1.5, cap 10 s)
- internal transport guard values
- KNOWN_ENDPOINTS trim
- progress display on TTY
- claim-ticket schema
- ~~`--pages` spec grammar and its merge/conflict rule against a `pages` key
  inside `--options` JSON~~ *(decided at build, 2026-07-21: `--pages` takes
  1-indexed values and low-to-high ranges, e.g. `1,3-5`, and merges into the
  `--options` object as its `pages` array — the same array given either way
  is the same invocation, hence the same job item; giving pages in both
  flags is a usage error, never a precedence — silent precedence could bill
  a page set the user didn't intend)*
- view page cap + render-dpi defaults (CLI-side rasterization — unrelated to
  the retired API `dpi` option)
- PNG crop padding
- SKILL.md exit-code table
- span-overlap rules (partial/multi-element spans)
- `--schema` file-vs-inline detection
- extract version registry check
- `view --serve` live-reload dev mode
- view rebuild fingerprint scheme
- `help --json` schema shape
- update mechanism (uv/pipx/pip)
- org group naming (org vs account)
- org usage API requirements sketch
- *(2026-07-21)* canonical-JSON params serialization (key order, defaults
  inlined vs omitted — a default that changes must not change identities)
- *(2026-07-21)* `history.js` schema + sidebar re-poll cadence & cache-busting
- *(2026-07-21)* background-builder claim/heartbeat scheme and
  `--no-sidebar-sync` spelling
- *(2026-07-21)* `parse/ref.json` exact schema (carries {job_item_id, parse
  server job_id}; field spellings at build time) — the scan itself is
  decided: standalone parse items only, newest `completed_at` wins
- *(2026-07-21)* store migration: v2 `docs/<doc-id>/` layouts are not
  migrated (demo posture — `history list` simply won't see them; document
  `rm -rf ~/.ade/docs` in the changelog) — **confirmed**: no production
  deployments exist, so no migration tooling ships

## Rollout

1. This proposal reviewed/merged.

2. Build order *(revised 2026-07-21)*: job-item store + identity + scan
   (`history list`/`clear`, `history.js` writer) → `parse` on the new
   identity (dedup-with-notice, variants) → `extract` (job-id input, path
   reuse/auto-parse, the three flat folder shapes) → `find`/`crop` on job
   ids → `view` (kind-aware payloads, sidebar, background builder) →
   `help`/`update` → `org` (`jobs` now; `usage`/`limits` when backend APIs
   land).

3. **SKILL.md and CONTEXT.md rewrites ship in the same change as the
   surface** — the skill is the deployed agent contract; the loop becomes
   "run `parse`; it's free if already done" + job-item vocabulary +
   pending/resume + deep-link citations. CONTEXT.md's Doc id / REF / Live
   parse / Stale entries are rewritten to the job-item language.

4. Eval gate before launch: dense-table coverage on `dpt-3-pro-20260710` (see Non-goals).

5. File the `org usage` / `org limits` backend API asks with the ADE team, referencing this doc's requirements sketch.

6. File the CLI OAuth platform asks: a Logto native-app registration (loopback redirect) and an `/api/authz` access-token-acceptance decision (see Build decisions → Auth).

## Contract verification addendum (2026-07-14)

Verified against aide main on 2026-07-14 (gateway `services/gateway`, contracts `packages/aide_temporal/customer_surface.py`). The reviewed body above is left as reviewed; these findings refine it and govern where they differ:

1. **Parse async submit can 429.** Parse (and workflow) page-meter at submit against the hourly async bucket (`job_surface/router.py` preflight metering); only *extract* async is worker-paced and never 429s at submit. The body's rate-limit note is extract-specific, not general. CLI posture (decided): on submit 429, honor Retry-After and retry within the `--wait` budget; if the budget expires before a job exists, exit with a distinct machine-readable rate-limited state (no claim ticket — nothing was submitted).

2. **Auth is Bearer-only on the customer host.** Clients always send `Authorization: Bearer <token>` to `api.ade.landing.ai` (Logto PAT terminated at the Traefik edge in production; native gateway API key on internal environments). The tracked "endpoint-driven auth-scheme default" is dropped: `config.json` holds `{endpoint, api_key}` only, with `ADE_ENDPOINT` / `ADE_API_KEY` env overrides.

3. **ZDR is not a client concern.** Zero-data-retention is an account-level flag injected by the edge as a request header and enforced server-side; it is rejected as server-only if sent in the body. The tracked "ZDR flag exposure" item is dropped — the CLI sends nothing.

4. **Extract `standard` tier is also 0.5×** (set in `operations/v2_extract.py`, separate from parse's contract-level multiplier). Tier posture is symmetric across both verbs.

5. **Confirmed as written:** no job-cancel endpoint exists; job results stay pollable for 7 days (Temporal namespace retention), then poll 404s (the `expired` state); no customer usage/quota API exists; `POST /v1/files` stages bytes and returns a `file_ref` usable as `markdown_ref`; model registries at submit are parse `dpt-3-pro-20260710 | dpt-3-pro-20260515 | dpt-3-pro-latest | dpt-3-pro` and extract `extract-20260710 | extract-20260630 | extract-latest | extract`; canonical host is `api.ade.landing.ai` (`api.va.landing.ai` is VTRA's, and `/v2/ade/*` spellings are a retired alias — canonical paths are bare `/v2/*`).

### Re-verified 2026-07-21 (parse options & response shape)

The parse wire contract moved under the CLI in mid-July; the contract section
above is rewritten to match. Deltas against what the 2026-07-14 addendum and
the repo's `openapi.json` describe:

1. **`dpi` is retired** (rejected 422 since 2026-07-16), along with the
   legacy `grounding` option and `blocks.<type>.caption`. There is no pixel
   coordinate space to configure anymore.
2. **Boxes are normalized** `{xmin, ymin, xmax, ymax}` fractions of page size
   in `[0, 1]` (8-decimal rounding, clamped) — multiply by any raster's
   dimensions for pixels (landed server-side 2026-07-13).
3. **Grounding is inline on the structure tree** — every node carries
   `{page, range, box}` (`range` = `[start, end)` code-point slice,
   `metadata.range_units = "unicode_codepoints"`); leaf elements add
   `atomic_grounding` segments. No separate grounding tree.
4. **`pages` is a 1-indexed JSON integer array** (values < 1 are 422;
   out-of-range positives are silently ignored), and **`inline_markdown`**
   was added (both 2026-07-14).
5. **Options are `extra="forbid"` at every nesting level**, and validation
   errors use the unified `{code: "validation_error", message}` envelope
   (2026-07-16) — the error names the offending `options.<key>`.
6. The full customer options surface is exactly: `pages`,
   `atomic_grounding`, `inline_markdown`, `blocks.<type>.markdown` (8 types),
   `blocks.table.format` (`"html"` | `"markdown"`), `password` (always 422).
   Everything internal (`zero_data_retention`, limits, queues, billing
   fields) lives on the request wrapper as server-only and is rejected as
   customer input.

The repo's `openapi.json` is refreshed (2026-07-21) from a pre-release ADE
deployment's `/openapi.json` — the spec this CLI develops against;
production (`api.ade.landing.ai`) lags it.

7. **New in that spec: a `/v2/ground` contract** (sync + `/jobs`), taking
   an extract call's `extraction_metadata` plus the parse's `structure` tree
   and returning, per extracted field, the overlapping blocks with ids, pages,
   and boxes — the server-side twin of the CLI's local evidence join. The
   local-join decision **stands**: it costs zero API calls, works offline
   from artifacts the store already holds, and keeps every intermediate
   inspectable. `/v2/ground` joins `/v2/workflow` in the out-of-scope list as
   deliberate decomposition, not an oversight.

## Build decisions (grilling session, 2026-07-14)

Decisions made on top of the reviewed proposal:

- **Stack:** Python 3.12+, uv-managed; typer for the command tree; httpx transport; pypdfium2 for page rendering. Command name is `ade` (the package keeps the `ade-cli` name), as written throughout this doc.
- **Auth (revised 2026-07-14, supersedes the addendum item 2 config shape):** the CLI supports **two methods** — API key, and an **OAuth browser login** (authorization-code + PKCE with a `127.0.0.1` loopback callback against Logto). `auth` becomes a gh-style group: `auth login` (browser flow by default; `--api-key [KEY]` stores a key instead), `auth status`, `auth logout`. OAuth ends with **access + refresh tokens**, auto-refreshed; both credential shapes live in `~/.ade/credentials.json` (mode 0600, separate from `config.json`). Precedence: `ADE_API_KEY` env always wins; otherwise the most recent `auth login` sets the active method. Headless environments use the API key path in v1 (`auth login` fails with remediation when no browser is available); device-code flow is tracked as the future headless OAuth answer.
  **Platform dependencies (asks to file, like the org-usage precedent):** (1) register a Logto **native app** with a loopback redirect URI for the CLI; (2) confirm whether the edge's `/api/authz` (vision-agent) accepts Logto **OIDC access tokens** as Bearer or only `pat_...` PATs — if PAT-only, either extend authz or pivot the flow's end-credential to a minted PAT. Nothing CLI-usable exists today: the gateway's `/auth/*` is internal-only cookie SSO, and `/user/key` mints keys production ignores.
- **Scope:** full command surface in the proposal's build order; `org usage` / `org limits` ship as explicit "backend missing — ask filed" stubs; SKILL.md ships with the surface; the `eval/` dense-table gate is a separate effort.
- **Extract input staging:** inline `markdown` for small inputs; above a size threshold (build-time value) transparently upload via `POST /v1/files` and send `markdown_ref`.
- **Output convention:** human-readable on TTY by default; every command supports `--json` emitting one stable JSON object/array on stdout (errors/pending payloads included). SKILL.md tells agents to pass `--json`.
- **Concurrency:** the claim ticket is created atomically (O_EXCL) *before submit* (tightened from "before first poll"); exactly one process submits, others join as pollers of the recorded job. A submitless ticket (crash between claim and submit) is detected by the absence of a `job_id` and reclaimed.
- **429 posture:** see addendum item 1.
- **Testing:** offline-first (fake httpx transport + fixtures covering 202 → pending → completed/failed/404, 429, 206 partials); one env-gated live smoke test (real key) covering parse→extract→view.
