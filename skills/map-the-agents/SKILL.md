---
name: map-the-agents
description: Look up prior agent-capability research in the Observatory's map before or during Navy Yard or Tech Triangle design work, and record every public GitHub repository lead you encounter (adopted or not) so the map keeps growing. Not for adopting or executing any discovered code.
---

# Map the Agents

The Observatory keeps small, source-linked maps of public agent repositories: what they claim to
do, which facets are still gaps, and how fresh each snapshot is. It answers "has anyone already
looked at this class of agent?" cheaply, before you re-research it. It never runs, imports, or
recommends installing anything it observes; a repository landing in the map is an **evaluation
candidate**, not an adoption decision.

This skill is repo-owned and not globally installed. Run it from a checkout of this repository. It
does not read this repo's `.coordination/` (coordinator-only working notes) or any run receipts.

## Preflight (once per session)

```
uv run --python 3.12 python -m map_agents --root corpus status
```

If the root is missing, `status` still returns `initialized: false`; running any command
(`intake`, `receive`, `inbox`) creates the layout on first write. Do not hand-create files under
`corpus/`.

## Look something up first

```
uv run --python 3.12 python -m map_agents --root corpus query "planning loop sandbox tool runner" --limit 5
```

Searches generated `map/` Markdown only (specifications, components, design-choices, workflows,
skills-patterns, interfaces, memory-state, orchestration, tools-permissions, dependencies,
evaluation, limitations, relevance and gaps). Add `--include-archive` to also search the wiki
kernel's own historical pages. A result's `freshness` is `pending`, `fresh`, `stale`, or
`refresh-failed`; treat `pending` and `refresh-failed` claims as **unknown**, not confirmed. If
`complete` is `false` in the response, the corpus exceeded the safety scan ceiling; narrow the
query rather than trusting an empty result as full coverage.

To browse without searching, start at `map/index.md` (classes, agents, components, patterns, gaps,
freshness) or a specific repository's page under `map/repos/<owner>/<repo>.md`.

## Record a lead you found

Every public GitHub repository you notice during design work should be recorded, whether or not
you end up using it. `origin` and `project` are plain tags (no URLs, no secrets); duplicates are
free (`ingest` and `receive` are no-ops on an unchanged catalog).

```
# One or more URLs/text, straight from the shell:
uv run --python 3.12 python -m map_agents --root corpus intake --origin "design-session" --project "navy-yard" \
  --text "https://github.com/some-org/some-agent looks relevant to the bosun redesign"

# A file instead of --text:
uv run --python 3.12 python -m map_agents --root corpus intake --origin "design-session" --project "tech-triangle" --file notes.md
```

Only normalized `owner/repo` links and your two tags persist; the source text itself is discarded
after link extraction, and private hosts, tokens, and GitHub-secret shapes are rejected before any
write.

### File-based private leads (chat exports, meeting notes)

Do not paste raw private conversations into `--text`. Instead drop a file at
`inbox/private/<project>/<origin>.md` (or `.txt`/`.json`) — the path itself supplies both tags — and
run:

```
uv run --python 3.12 python -m map_agents --root corpus inbox --lane private
```

`inbox/private/` is git-ignored; only the normalized public links extracted from each file reach
`catalog/`, keyed by the file's sha256 so a repeat run is a no-op. Use `--lane public` for files
that are themselves fine to commit under `inbox/public/`.

### Incoming automated research (GitHub Actions)

A `repository_dispatch` event of type `research-completed` (payload: `{project, origin?, urls?,
text?}`) lands the same way through `receive --event-path $GITHUB_EVENT_PATH`; see
`.github/workflows/maintenance.yml`. There is no live WhatsApp connector — that data path does not
exist yet, only file-based inbox leads and this explicit dispatch receiver.

## Refresh snapshots and flag what needs a closer look (no model required)

```
uv run --python 3.12 python -m map_agents --root corpus maintain --max-repos 2 --max-files 4 \
  --max-bytes 60000 --catalog-entries 10 --max-seconds 60
```

This is metadata-only: it advances the public catalog feed, takes bounded README/docs snapshots of
a fair rotation of repositories, and lists which now `needs_distillation`. It never calls a model.
Bytes are storage/network ceilings, not model tokens — if a snapshot or worker envelope is too
large, narrow the selection (fewer files, an explicit `--path`, or a smaller `--max-bytes`), don't
assume a small agent can read more just because its context window is larger.

## Turn a snapshot into a dossier (small-agent or trusted-command recipe)

Either a small agent reading the packet directly, or an explicitly configured trusted command, can
distill one repository. No provider SDK or paid model is required to exercise the mechanics:

```
# 1) Get the bounded envelope (packet + exact instructions) for one queued repository.
#    max-files/max-bytes below bound the underlying snapshot, which bounds the packet the
#    envelope wraps; there is no separate envelope-bytes flag, so narrow the snapshot instead:
uv run --python 3.12 python -m map_agents --root corpus worker --max-files 4 --max-bytes 60000

# 2) Read corpus/packets/<operation_id>.json yourself, write a proposal JSON that matches
#    packet["proposal_schema"] (facets/kinds/bases/bounds are in the packet), citing only
#    packet slice_ids, then apply it through the real kernel — never hand-edit the wiki:
uv run --python 3.12 python -m map_agents --root corpus prepare owner/repo   # if you need a fresh packet
uv run --python 3.12 python -m map_agents --root corpus apply corpus/packets/OP.json corpus/proposals/OP.json
uv run --python 3.12 python -m map_agents --root corpus build
```

A schema-valid proposal is not proof of a correctness claim — it only means the claim cites real
evidence in the shape the kernel requires. `basis: code-inspected` requires citing an actual
code/config slice, not documentation alone. An explicitly configured trusted command instead of a
manual read can be run with `worker -- <exe> <args...>`; the command line is fixed at invocation
time and nothing from source text or the model's own output is ever appended to it.

`worker` returns `outcome: no-op` when nothing currently needs distillation (for example a fresh
corpus with no snapshot yet); run `maintain` first. For a fully offline, runnable walk through this
whole prepare/proposal/apply/build/query shape on fixture data, run
`python scripts/demo_synthetic.py` from the repository root.

## Boundaries

- This skill never installs, executes, or recommends adopting discovered code; it only records and
  organizes evidence about what a public repository claims and shows.
- Canonical wiki writes go through the vendored kernel's `prepare`/`apply` only (see
  `vendor/research-corpus-wiki/SKILL.md`); never hand-edit `corpus/wiki/`.
- One writer owns a given `corpus/` checkout at a time; do not run `maintain`/`worker`/`inbox`
  concurrently against the same root from two sessions.
- Full corpus population is a separate, larger effort; this skill's job is small, resumable
  contributions to it, not a bulk crawl.
