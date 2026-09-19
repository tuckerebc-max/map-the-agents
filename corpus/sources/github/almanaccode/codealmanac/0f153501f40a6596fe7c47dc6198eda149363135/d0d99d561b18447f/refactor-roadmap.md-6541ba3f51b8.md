# Refactor Roadmap

Date: 2026-06-08

This roadmap assumes source changes happen in later work. No source code was
modified during this audit.

## Slice 0: Set Product Contracts Before Code

Goal: remove ambiguity before moving files.

Decisions:

- Is local GitHub ingest `gh`-based, Composio-based, or are these two explicitly
  separate products?
- Is scheduled Garden installed by default or opt-in?
- Are deprecated aliases temporary or permanent compatibility?
- Is `almanac serve` a current-wiki viewer or a global local Almanac console?

Outputs:

- Update active repo instructions and wiki pages after decisions.
- Write tests around chosen public behavior before deleting alternatives.

Why first:

Several smells are product conflicts, not TypeScript problems. Refactoring them
without a product decision would just move the ambiguity.

## Slice 1: Lazy CLI Registration And SQLite-Free Cleanup

Goal: delete or sharply shrink `src/cli/sqlite-free.ts`.

Implementation direction:

- Make registration files safe to import without loading SQLite-heavy modules.
- Lazy-import command implementations inside Commander action handlers.
- Keep the early ABI guard and setup/update/doctor recovery behavior.
- Preserve setup shortcut behavior only if Commander itself cannot own it.

Likely files:

- `src/cli.ts`
- `src/cli/register-*.ts`
- `src/cli/sqlite-free.ts`
- `bin/codealmanac.ts`
- setup, automation, doctor, update tests

Tests:

- ABI guard behavior for broken `better-sqlite3`.
- Setup/update/doctor/uninstall commands still run in recovery mode.
- Help output and deprecated groups stay stable where intentionally retained.

Success condition:

There is one command parser for public flags, or a very small documented
recovery parser for the minimum repair surface.

## Slice 2: Typed Lifecycle Start APIs

Goal: stop routing durable lifecycle facts through CLI output.

Implementation direction:

- Add `src/capture/start.ts` with `startCaptureRun()`.
- Add `src/ingest/start.ts` if ingest-specific operation setup remains thick.
- Make `runCaptureCommand()` and `runIngestCommand()` render typed results.
- Make `capture sweep` consume typed capture-start results directly.
- Move GitHub PR report-output policy out of `src/cli/commands/operations.ts`.
- Replace message-substring operation error classification with typed errors.

Likely files:

- `src/cli/commands/operations.ts`
- `src/cli/commands/capture-sweep.ts`
- `src/capture/sweep.ts`
- `src/capture/start.ts`
- `src/ingest/start.ts`
- `src/operations/*`

Tests:

- `capture sweep` records run ids without parsing stdout.
- JSON and text CLI output can change without breaking sweep ledger behavior.
- Ingest output behavior remains stable.
- Error rendering covers typed missing-wiki and source setup failures.

Success condition:

CLI command rendering is no longer an internal API.

## Slice 3: Unified Capture Discovery

Goal: make manual capture and scheduled sweep use the same session candidate
model.

Implementation direction:

- Reuse `src/capture/discovery/*` for manual capture.
- Remove Claude-only directory/content fallback from `src/capture/input.ts` or
  replace it with shared candidate discovery.
- Implement manual selection policy over `SessionCandidate`.
- Either support `capture --app codex` or remove the flag until supported.
- Keep quiet-window and ledger policy in sweep.

Tests:

- Manual capture can select Claude and Codex candidates when requested.
- Explicit transcript file capture still works.
- Sweep behavior stays unchanged for quiet-window eligibility.
- Large transcript discovery uses bounded reads.

Success condition:

"Transcript discovery" has one code path and two selection policies.

## Slice 4: Provider Identity And Runtime Contract Cleanup

Goal: remove duplicated provider facts and stale runtime fields.

Implementation direction:

- Add a small shared `ProviderId` identity catalog.
- Rename readiness provider interfaces/types to avoid looking like runtime
  providers.
- Use one provider-id guard in config, process spec validation, and records.
- Remove `AgentRunSpec.connectors` unless a chosen product path requires it.
- Keep `networkAccess` or a neutral runtime requirement for sandbox behavior.
- Remove nested `display.raw` from persisted harness tool events.
- Normalize Codex thread/turn ids as explicit fields if viewer/jobs need them.
- Delete doctor's injected provider-status branch and use readiness providers.
- Decide and remove or quarantine legacy Codex exec exports/tests.

Tests:

- Provider default model and display name are consistent in setup, agents,
  operations, and records.
- Doctor injected status follows the same readiness catalog.
- Run logs do not persist raw provider protocol payloads by default.
- Codex app-server network access still works for source ingest.

Success condition:

There is one provider identity vocabulary and no stale Composio-shaped runtime
field in provider-neutral specs.

## Slice 5: Query Read Models And Viewer Split

Goal: make CLI and viewer read from shared wiki query projections.

Implementation direction:

- Add `src/wiki/query/pages.ts`.
- Add `src/wiki/query/topics.ts`.
- Move page summary, topic detail, topic list/count, and path mention
  projections out of CLI/viewer modules.
- Split `src/viewer/api.ts` into wiki, jobs, review, and connections modules.
- Decide whether `serve` is global local console or current-wiki viewer and
  update help/docs accordingly.

Tests:

- CLI `search`, `show`, `topics`, and viewer API agree on archive filters,
  topic counts, file mention semantics, and page summaries.
- Global viewer behavior is covered if retained.
- Binding help/docs reflect exposed scope.

Success condition:

Viewer and CLI can differ in presentation, not in duplicated graph semantics.

## Slice 6: Health And Source Maintenance Split

Goal: keep diagnosis, source checks, and deterministic repairs separate.

Implementation direction:

- Move source/citation checks into `src/wiki/sources/health.ts`.
- Move legacy source-frontmatter repair into `src/wiki/sources/maintenance.ts`.
- Keep `src/wiki/health/index.ts` as report composition.
- Reuse shared frontmatter parsing for empty-page body checks.
- Keep `health --fix` narrow and explicit.

Tests:

- Existing health categories stay stable.
- `health --fix` only rewrites safe legacy source frontmatter.
- Empty page detection uses the same frontmatter semantics as the indexer.

Success condition:

Health is not the place where arbitrary wiki repair logic accumulates.

## Slice 7: Source Access Product Cleanup

Goal: resolve the local `gh` versus Composio split.

If local `gh` wins:

- Remove or park `connect github` / `source github` if they are not current
  product.
- Remove connector runtime tests and config fields that no production path uses.
- Keep source-ref parsing and `ingest github:pr:N` as a simple local tool path.

If Composio wins:

- Move GitHub source resolution to connector account selection.
- Pass connector requirements through a connector/source boundary, not directly
  through harness provider-neutral specs.
- Replace `gh` prompt guidance and tests.

Tests:

- One happy path and one missing-auth path for the chosen source model.
- No stale docs/wiki claim the opposite source model.

Success condition:

There is one obvious answer to "how does local GitHub ingest read PR material?"

## Slice 8: Documentation And Wiki Cleanup

Goal: align repo instructions with source truth after the code moves.

Targets:

- `MANUAL.md`
- `AGENTS.md` / imported instructions if needed
- active `.almanac/pages/*` architecture pages
- command help text
- stale plans only when directly harmful

Updates:

- Narrow the no-AI/page-write invariant.
- Document provider runtime/readiness split with current names.
- Document viewer product scope.
- Remove stale `bootstrap` language.
- Record any intentional permanent compatibility aliases.

Success condition:

Future agents do not rebuild deleted architecture from stale docs.

