# Contributing to Claudexor (humans and agents)

Claudexor is developed largely by external AI coding agents operating in
sessions with no memory of each other. This contract is what keeps hundreds of
such sessions converging instead of drifting. It is short on purpose: follow it
literally.

## Before you change anything

1. Read [`CLAUDEXOR_BIBLE.md`](CLAUDEXOR_BIBLE.md) in full. It is the product
   constitution. If your change would weaken, bypass, or reinterpret an
   invariant, STOP: that is a concept change and needs the owner's explicit
   approval (see "Changing the Bible" below), not a code workaround.
2. Read the rows of [`docs/FEATURES.md`](docs/FEATURES.md) that touch the
   features you are about to work on (it tracks every feature that is not in a
   `solid` state). Read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the
   current map and [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) for the
   contributor workflow.
3. Work in two phases: first diagnose and write down the plan (what you will
   change, which invariants it touches, what proves it worked), then implement.
   Do not improvise structural decisions mid-edit.

## While you work

- Schema first: data-shape changes start in `packages/schema`, then
  `pnpm schema:gen`, then consumers, then Swift DTOs, then docs.
- Keep surfaces thin (CLI/control-api/MCP/ACP/macOS project engine state; they
  never invent business logic). Adapters translate I/O only.
- No regex governance over model prose for risk/winners/tests-passed/
  permissions. Typed contracts, events, gates, and reviewer evidence only.
- Dead code is deleted, not parked. A schema field ships only WITH a real
  producer and consumer in the same change (`pnpm staged:check` enforces the
  floor; comments do not count as consumers).
- Big files do not get bigger: the complexity ratchet
  (`node scripts/complexity-ratchet.mjs`) fails CI when a tracked file grows
  past its baseline. Split instead of appending; after a shrinking refactor,
  run it with `--update` to tighten the bar.

## Before you commit

Run the Node/schema/documentation gate. The package script is the command
source of truth, so this contributor guide does not duplicate its individual
steps:

```bash
pnpm release:verify:node
```

The same portable gate is available as `pnpm release:verify`. Platform-specific
Swift, native-helper, and packaging checks run in CI. On macOS,
`pnpm release:verify:macos` additionally exercises the local app; contributors
need neither a Mac nor a Cursor installation to open a PR.

Review authority is the cumulative diff on an exact candidate under the
[Release review protocol](docs/CHECKLISTS.md#release-review-protocol-inv-125inv-139):
a complete independent report, dispositions, and confirmation by the responsible
maintainer. No model-brand pair, timing overlap, or review signature is required.
Changes after review need testing and review of the affected delta, not a
ceremonial restart of unchanged evidence. There is no per-commit review hook.

Reviewer findings are hypotheses, not patches to apply on trust. Reproduce an
accepted issue, trace its root and canonical owner, search sibling surfaces,
and fix the class only when multiple surfaces or a broken SSOT boundary prove
it; otherwise make the smallest local correction. Reviewers receive the whole
candidate and evidence so architecture stays visible; do not trade that context
for many tiny batches.

**External contributors:** the CI gate suite above is what your PR must pass.
The maintainer owns release review and confirmation; contributors are not
expected to buy particular subscriptions or fund release review.

Contributions are accepted under the repository's MIT license
(inbound = outbound); by opening a PR you license your change under MIT.
Historical `Dxx` codes in old commit messages are archival ids from the
maintainer's decision registry — current rationale lives in the Bible's
invariants, not behind those codes.

Then self-check, honestly, in the commit body:

- Which Bible invariants does this change touch, and how?
- Did every doc that describes the changed behavior get updated in THIS commit
  (`docs/FEATURES.md` row updated or deleted; ARCHITECTURE/DESIGN_SYSTEM/
  INTEGRATIONS/README where relevant)?
- Do the canary golden stories still describe the truth? (Fix the product,
  never the story — unless the owner approved a concept change.)

## Changing the Bible

`CLAUDEXOR_BIBLE.md` changes are constitutional. A commit that touches it must
carry a `CONCEPT-CHANGE(INV-xxx)` marker in its message, added only when the
owner explicitly approved that invariant change. Invariant numbers are stable:
a retired invariant keeps its number and is marked retired, never deleted or
renumbered. Editing an invariant so its original direction is no longer
recognizable is a delete, not an edit.

History is never rewritten merely to repair an incomplete marker. If an
already immutable marked commit omitted an approved invariant id, a later
descendant may add exactly
`CONCEPT-COVERAGE(<full-40-character-sha>: INV-xxx[, INV-yyy])`. The gate
accepts this only for an ancestor inside the same checked release range; it
supplements coverage but cannot replace the original `CONCEPT-CHANGE` marker.

## Canary golden stories

`packages/canary` holds user-level E2E stories over the built CLI with offline
fake harnesses. Each story is pinned to an invariant tag. They run on every PR
(`pnpm canary`). If your change breaks one, the product regressed — do not
weaken the story.
