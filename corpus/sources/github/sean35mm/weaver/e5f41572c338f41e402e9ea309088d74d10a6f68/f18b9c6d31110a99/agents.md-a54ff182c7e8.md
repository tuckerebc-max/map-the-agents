# AGENTS.md — for agents (and humans) working on the Weaver repo

Weaver is a CLI-first, serverless coordination layer that gives multiple coding agents shared
situational awareness in the same repo. This file orients you; the public docs are linked below.

## Project docs

- **[README.md](./README.md)** — what Weaver is, the data model, commands, conflict model.
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** — setup, where things live, the bar for changes.
- **[RELEASING.md](./RELEASING.md)** — how to cut/publish a release. **Always follow this for
  releases.**

## Commands

```bash
node src/cli.ts --help     # or: bun src/cli.ts --help   (runs TS directly, no build needed)
npm test                   # node --test  (must pass)
npm run test:bun           # bun test     (must also pass — CI runs both)
npm run typecheck          # tsc --noEmit
npm run build              # verify generated UI + TypeScript + temporary standalone binary
node scripts/demo.ts       # seed a throwaway store, then `weaver watch` / `dashboard`
```

## Conventions (important)

- **Conventional Commits** (`feat:`/`fix:`/`chore:`/`docs:`/`refactor:`/`test:`) — they drive
  versioning and the changelog via release-please. This is mandatory.
- Tests use `node:test` + `node:assert/strict` and must pass on **both Node and Bun**.
- Relative imports use explicit **`.ts` extensions** (required by Node type-stripping + Bun).
- Keep pure logic **clock-injectable** (pass `now` in); no `Date.now()` inside testable units.
- Keep the core **zero-runtime-dependency** where practical (`picomatch` is the only one).
- Validation is **lenient at the CLI boundary**: never throw a stack trace at an agent, and
  `check` must never crash a tool call.
- The CLI is the **universal engine** — never add a hard dependency on one harness.

## Releasing — short version

Don't hand-create releases. Land `feat:`/`fix:` commits on `main`, then **merge the
"chore: release vX.Y.Z" PR** that release-please opens. That tags the release, builds + attaches
the standalone binaries. Full details and the
pre-flight checklist are in **[RELEASING.md](./RELEASING.md)**.

<!-- weaver:start protocol=4 -->
Run `weaver status` every task. Read-only/plan-only: stop after status unless it/user identifies a
pad; read only—no create/use/claim/done.

Before writes: `weaver task "<goal>"`; use a pad only for a matching active pad, collaborators,
handoff/resumption, conflict/shared decisions, or user request—not complexity/duration; claim every
scope once before editing.

If `claim` exits 1, it WAS recorded: don't rerun. Read intent/reason/activity/pad. Prefer other work; proceed only if harmless,
otherwise coordinate/ask; never silently overwrite. Different-worktree: informational; coordinate integration.

If using a pad: curate Markdown; read its revision and merge stale conflicts.
Archive only when the whole workstream is complete. Trash only empty/duplicate/obsolete pads with
reason+revision and no live attachments; recover mistakes. Keep secrets/PII out. Lasting knowledge:
Repository Facts (`fact`; correct: `--update`; retire: `forget`).

Before commit/push/PR: exactly `weaver preflight --staged`, `weaver preflight --upstream`, or
`weaver preflight --base <ref>`; pause on overlaps. Write sessions finish with `weaver done`.
<!-- weaver:end -->
