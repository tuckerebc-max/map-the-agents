# Ownership boundaries

This repository is a fork of [`agegr/pi-web`](https://github.com/agegr/pi-web) that
packages it, together with the [`earendil-works/pi`](https://github.com/earendil-works/pi)
SDK, into a signed desktop app. Three layers, three integration mechanisms:

| Layer | Source | How it arrives | Who owns the files |
|---|---|---|---|
| Agent runtime | `@earendil-works/pi-*` | npm dependency, exact version | upstream |
| Web UI | `agegr/pi-web` | `git merge` of an upstream release tag | upstream |
| Desktop shell | this repo | authored here | fork |

The whole maintenance cost of this project is concentrated in one place: **files the
fork edits that upstream also owns.** Everything in this document exists to keep that
set small and visible.

## The machine-readable boundary

[`scripts/fork-ownership.json`](../scripts/fork-ownership.json) is the single source of
truth. It is consumed by:

- `.github/workflows/component-updates.yml` — decides whether a nightly sync may push
  to `main` unattended or must open a PR for review.
- `scripts/fork-ownership.test.mjs` — fails if the manifest drifts from the tree.

Update the manifest in the same commit that changes the boundary. Do not maintain a
second copy of this list anywhere.

## Cosmetic drift vs structural drift

Not all divergence costs the same, and line count is a bad proxy for risk.

pi-web styles its components with inline `style={{ … }}` objects, which a stylesheet
cannot override. So restyling a shared component *necessarily* edits the upstream file:
you delete the inline style and add a `className`. That produces a large diff — and it
is fine. If upstream later edits the same line, git reports a textual conflict, the sync
job fails, and a human looks at it. Loud failure is the safe failure.

What is dangerous is **structural** drift: rewritten JSX trees, new components spliced
into upstream files, and logic moved across file boundaries. Those merge *cleanly* while
being wrong.

`npm run drift` measures the split and flags any file whose recorded risk no longer
matches:

```
components/ModelsConfig.tsx     146 total    134 cosmetic     12 structural   low
components/AppShell.tsx         558 total    129 cosmetic    429 structural   high
```

Both files have big diffs. Only one of them is a problem. `ModelsConfig.tsx` is the
reference for how a restyled shared component should look.

Risk thresholds live in the manifest's `riskModel` and are applied to structural drift
only: `>= 250` high, `>= 30` medium, below that low.

### Where the structural drift actually is

Across the whole fork: **969 cosmetic lines, 1379 structural**. But the structural half
is highly concentrated — three files carry 80% of it:

| File | structural | what it is |
|---|---|---|
| `components/SessionSidebar.tsx` | 430 | sidebar redesign; ~500 lines moved out to `ProjectPicker.tsx` / `path-ui.tsx` |
| `components/AppShell.tsx` | 376 | top-bar redesign (was 429 before the desktop chrome moved out) |
| `components/FileViewer.tsx` | 305 | toolbar, status states, file icons, live-sync indicator |
| `components/TabBar.tsx` | 66 | accessibility: tab roles, roving focus, arrow-key navigation |
| `components/FileExplorer.tsx` | 61 | selection highlighting; git status colours on CSS variables |
| `hooks/useTheme.ts` | 57 | follows the OS colour scheme until the user chooses |
| `components/ChatWindow.tsx` | 35 | branding copy, empty state |

Every other shared component is cosmetic-only.

Note what the `AppShell.tsx` number says. Moving the desktop chrome into
`components/desktop/` removed only 53 of its 429 structural lines: the rest is the
fork's own top-bar design — the toolbar consolidated into a more-menu, upstream's
inline-styled buttons rebuilt — and it applies to the web build too. **That drift is the
product, not a defect.** It cannot be cleaned up without deleting the differentiated
interaction design, so `AppShell.tsx` stays a permanent review point rather than
something to fix. The same will be true of any file where the fork's design genuinely
diverges from upstream's.

## The failure mode this guards against

`git merge` conflicts are the *safe* outcome — the sync workflow runs under
`set -euo pipefail`, so a conflict fails the job and nothing ships.

The dangerous outcome is a **silent semantic conflict**: upstream edits a region the
fork also changed, git merges it cleanly because the edits do not textually overlap,
and the result is two implementations of the same behaviour. Tests, `tsc --noEmit`
and `eslint` all pass, and the previous pipeline pushed that straight to `main` and
cut a signed release with no human in the loop.

The worst instance today is `components/SessionSidebar.tsx`: roughly 500 lines were
moved out into `components/ProjectPicker.tsx` and `components/path-ui.tsx`, neither of
which exists upstream. Git does not track cross-file moves, so an upstream change to
the project-picker block merges back into `SessionSidebar.tsx` cleanly and resurrects
a second copy of code that now lives in `ProjectPicker.tsx`.

Concrete measurement: upstream's `v0.8.0 → v0.8.1` patch release touched **7 files
that this fork has also modified**, including all three of the highest-risk ones.
Expect roughly a third of the files in any upstream release to land on fork-modified
files. That rate is stable, not temporary — see the dispositions below.

### Sentinels

`components/fork-extractions.test.mjs` turns that silent failure into a loud one. It
covers both directions a clean-but-wrong merge can go:

- **Resurrection** — code the fork moved elsewhere reappears at its origin, e.g.
  `displayCwd` getting redefined inside `SessionSidebar.tsx` while `path-ui.tsx` also
  exports it. Importing a moved symbol is fine; redefining it is the signal.
- **Erosion** — a fork change is dropped and the file quietly reverts toward upstream,
  e.g. `AppShell.tsx` losing `data-tauri-drag-region`, or `app/layout.tsx` losing its
  `native-theme.css` import (which would revert the entire restyle).

The assertions are validated by mutation: each failure mode was injected and confirmed
to fail the test. When one fires after a merge, re-apply the fork change — do not delete
the assertion. Add a new entry whenever code is moved out of, or added to, a shared file.

## Rules for changing a shared file

In order of preference:

1. **Style only?** Put the CSS in `app/native-theme.css` and, in the upstream component,
   replace the inline `style={{ … }}` with a `className` — nothing else. Deleting the
   inline style is unavoidable (a stylesheet cannot override it) and is not a boundary
   violation; leaving the JSX shape untouched is the part that matters.
   `app/globals.css` stays byte-identical to upstream — never edit it.
   `native-theme.css` is imported after it in `app/layout.tsx` so equal-specificity
   rules win.
2. **Generally useful?** Send it upstream to `agegr/pi-web` as a PR. Once merged, the
   structural divergence disappears entirely. This is the only real fix, and it is the
   right home for things like the `ProjectPicker` extraction, the `FileViewer` toolbar,
   and `hooks/useTheme.ts` following `prefers-color-scheme`.
3. **Genuinely desktop-only?** Put it in `components/desktop/` and reach it from the
   upstream file with a single import and a mount point. Components there render to
   nothing in a browser build, so the host does not even need an `isTauriDesktop()`
   branch around them — `<WindowControls />` is the reference. Never restructure
   upstream JSX to accommodate desktop code.

What to avoid: rewriting upstream JSX for visual reasons, and moving upstream code
across file boundaries.

## Fork-owned files

Safe to edit freely; upstream never touches them. Full list in the manifest's
`forkOwnedPaths`. Broadly: `src-tauri/`, `desktop/`, `scripts/`, `.github/workflows/`,
`app/native-theme.css`, `app/api/updates/`, `lib/branding.ts`, `lib/app-updates.ts`,
`lib/desktop-updater.ts`, `lib/desktop-window.ts`, and the desktop-only components
(`ProjectPicker`, `UpdateReminder`, `AppSettings`, `path-ui`).

## Deliberate decisions that look like mistakes

- **`package.json` is still named `@agegr/pi-web`.** This is intentional. Upstream
  edits its own name and version on every release; renaming the fork would produce a
  conflict in `package.json` on every single sync. The user-facing brand comes from
  `lib/branding.ts` and `src-tauri/tauri.conf.json` instead. (JSON has no comments,
  which is why this note lives here.)
- **`next.config.ts` keeps its hand-written `serverExternalPackages` list.** It is
  tempting to derive it from `package.json`, but this file is upstream-owned and
  upstream updates that list itself when it adds a pi package. Auto-deriving it here
  would manufacture a conflict on every release. The fork-owned copies of that list are
  derived instead — `scripts/pi-packages.mjs` reads `package.json` and feeds both
  `scripts/prepare-desktop.mjs` and the sync workflow, so adding a pi package cannot
  leave one of them behind.
- **`AGENTS.md` is an upstream file.** It does not mention Tauri and should not. Put
  desktop maintenance notes in `docs/` and, at most, leave a one-line pointer there.
- **Local builds do not register the updater.** `src-tauri` reads the public key via
  `option_env!`, so a build without `PI_AGENT_DESKTOP_UPDATER_PUBLIC_KEY` simply has no
  updater. Keep it that way — it prevents a local debug build from accepting update
  payloads.

## What the nightly sync does

`.github/workflows/component-updates.yml`, at 02:17 daily:

1. Resolves the latest `pi` and `pi-web` releases; stops if neither moved.
2. Skips if a review PR for this upstream tag is already open.
3. **Classifies the incoming upstream changeset against the manifest, before merging** —
   after the merge commit exists, the incoming changeset can no longer be recovered
   with a plain diff.
4. Merges the upstream tag and updates the pi dependencies.
5. Gates on `npm test` (including `components/*.test.mjs`), `tsc --noEmit`, `npm run lint`,
   and a real standalone Next build.
6. **No overlap** → pushes to `main` and dispatches the signed release.
   **Overlap at blocked risk** → pushes `sync/pi-web-<tag>` and opens a PR with the
   boundary report. Merging that PR is what triggers the release.
7. On failure, files or comments on a `component-sync-failure` issue.

A merge conflict fails step 4 and nothing ships — that is the design.

## What is settled, and what is not

Every entry in the manifest carries a `disposition`, and the reasoning is in
`decisionLog`. Two values:

- **`reduce`** — drift that can go away without losing anything: desktop-only code that
  belongs in `components/desktop/`, or fork additions sitting in an upstream file that
  can move to a fork-owned one. Act on these.
- **`accepted`** — reviewed and kept.

As of 2026-07-26 everything remaining is `accepted`. Two rounds of `reduce` work are
done: the desktop window chrome left `AppShell.tsx`, and the update types left
`lib/api-types.ts` (which is now byte-identical to upstream and off the list entirely).

What is left splits in two, and neither half is a backlog item:

- **The fork's interaction design** — `AppShell.tsx` (376), `SessionSidebar.tsx` (430),
  `ChatWindow.tsx` (35). This is the product. It cannot be cleaned up without deleting it.
- **Generic improvements with zero desktop coupling** — `FileViewer.tsx` (305),
  `TabBar.tsx` (66), `FileExplorer.tsx` (61), `hooks/useTheme.ts` (57). Accessibility,
  selection highlighting, OS theme following, a file toolbar. None of it touches Tauri,
  so `components/desktop/` is not a home for it; the only ways out are upstreaming it or
  deleting a working feature. Upstreaming was declined, so these are kept.

The consequence is that most upstream releases will open a review PR rather than
publishing unattended. That is the running cost of maintaining a UI fork, priced
honestly. The guardrails make it a review, not a silent failure — which was the goal.

Narrow `blockOnRisk` only if the drift itself goes away. Never to quiet the gate.

## When you add new drift

Adding to a shared file is fine — just make the decision explicit:

1. Run `npm run drift`. If the structural number moved, update the manifest.
2. Give the entry a `disposition`. `reduce` means you intend to remove it; if you cannot
   say how, it is `accepted` and you are choosing to pay for it.
3. If you moved code out of a shared file, add a sentinel in
   `components/fork-extractions.test.mjs` — that is the failure mode nothing else catches.
4. Append a dated line to `decisionLog` so the next person does not re-litigate it.

## Commands

```
npm test        # the same gate CI runs: lib + scripts + components tests
npm run drift   # cosmetic vs structural drift, flags stale manifest risk levels
npm run lint    # eslint + branding check
```
