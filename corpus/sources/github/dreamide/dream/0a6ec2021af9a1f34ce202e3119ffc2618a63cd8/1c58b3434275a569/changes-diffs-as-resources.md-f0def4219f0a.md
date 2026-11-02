# Changes-tab diffs as project resources

From the October 16 architecture review (candidate 5).

## CDR-01: A file's diff is a project resource; the Changes tab's view is one reducer

Status: implemented

Problem and trigger: `GitChangesImpl` (`git-panel/changes.tsx`, 891
lines) built its own diff cache inside React:

- 11 refs, 9 per-project state maps (one instance only ever shows one
  project), and a serial load queue with a priority flag nobody set;
- stale results dropped by comparing refresh keys, and four effects that
  only copied state into refs.

All of that repeats what the project resource cache already does: version
on the git refresh key, share reads under way, invalidate as a group.

The optimistic revert was spread across three handlers and a pruning
effect. A single-file revert that **failed** left the file hidden until it
stopped being changed, which for a failed revert could be indefinitely.
None of this could be tested without rendering.

The write chip read the same diffs through its own `apiClient.gitDiff`
call, sharing nothing.

Scope:

- `lib/project-resource-cache.ts`: a resource spec can set
  `maxConcurrentLoads`. Loads of that kind beyond it wait their turn,
  first come first served, so asking for many does not start a git process
  for each at once. This replaces the tab's serial queue.
- `project-resources.ts`: a `gitDiff` kind (git group, at most 4 at once)
  and `gitDiffResourceKey(projectPath, change)`, keyed on the file's path,
  status and previous path as the git status reported them.
- New `changes/changes-view.ts`: a pure reducer for what the tab shows
  beyond the status:
  - expanded rows, and diffs rendered past the size guard;
  - files being reverted, and files hidden by a revert.

  A reverted file hides at once and shows again if the revert fails. If it
  succeeds, the first status read after it decides whether the file shows.
  A fresh status also forgets expanded and forced rows that are no longer
  changed.
- `git-panel/changes.tsx`: each expanded row reads its own diff through
  `useProjectResource`, only while the tab shows a status of the current
  version (as before). It keeps one reducer and the view-mode state. One
  instance per project (keyed), so no per-project maps.
- The write chip reads its diff through the same resource.
- `changes/expansion-state.ts` and its test are deleted (replaced by the
  reducer).

Excluded:

- The worktree dialog's compare diff, which is a different route
  (`gitWorktreeCompareDiff`).
- The write chip still fetches a diff whenever it has no inline one, even
  collapsed (a separate, speculative candidate). It is now bounded by the
  concurrency limit and shared with the tab.

Completion criteria:

- The tab holds no diff cache, queue or refresh-key comparison of its own.
- Diffs are read at most 4 at a time; a failed read frees its place.
  Covered by cache tests.
- A diff is read once per refresh and again after a bump. Its request
  carries the status's path, status and previous path (null when none).
  Covered by a resource test.
- Revert: hidden at once, shown again on failure, decided by the first
  status after success; status pruning of expanded and forced rows;
  toggling; no-op actions keep state. Covered by reducer tests.

Validation (2026-10-16):

- `pnpm lint`, `pnpm check:scratch` and `tsc --noEmit` pass.
- `pnpm test`: 153 files, 1056 passed, 4 skipped. New tests:
  - two limiter tests in `project-resource-cache.test.ts`;
  - one `gitDiff` test in `project-resources.test.ts`;
  - eight reducer tests in `changes/changes-view.test.ts`.

  The two old expansion-state tests are replaced by the reducer's toggle
  test.
- `git-panel/changes.tsx` went from 891 to 448 lines.
- Not inspected in the running app (the user's live session). Worth a
  check by hand:
  - expand all with many changed files;
  - revert one file, then revert all;
  - refresh while a diff shows.

Behaviour changes, all deliberate:

- A single-file revert that fails shows the file again at once. Before,
  it stayed hidden while the file remained changed.
- Up to 4 diffs load in parallel. Before, the tab loaded one at a time
  (its priority flag was never used).
- Collapsing and expanding a row within one refresh shows the cached diff
  without a read, as before; across a refresh it reads again when shown.
- The write chip's diff is shared with the tab and cached per refresh.
  Before, every chip read it anew.

Recovery: docs/architecture/tasks/changes-diffs-as-resources.md#CDR-01.
