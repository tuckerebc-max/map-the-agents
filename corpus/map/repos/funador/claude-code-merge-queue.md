# funador/claude-code-merge-queue

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f77757479cab @ 52448af2613d1623

## Summary (orientation draft, not independently verified)

A local, zero-cost merge queue npm package (TypeScript, Node >=18, zero runtime deps) that serializes landings from parallel Claude Code agents via numbered worktree lanes, a FIFO push queue, and a pre-push check gate. Evidence is README-only; behavior claims are documented, not code-inspected.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Configuration lives in a single .mjs file with fields for branchPrefix, worktreeSuffix, portBase, integration/production branches, protectedBranches, regenerableFiles, symlinks, buildOutputDirs, checkCommand, and checksRequired. -- evidence: [README.md#L47-L61](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L47-L61), [README.md#L43-L45](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L43-L45)
  - [observation/documented] Malformed configuration fails loudly at command load time, listing every problem (empty branch names, negative port, identical integration and production branches) rather than failing later. -- evidence: [README.md#L63-L66](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L63-L66)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes commands including hook worktree-create, build-lock, land, sync, promote, preview, port, and prune, each documented with its purpose. -- evidence: [README.md#L81-L90](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L81-L90)
  - [observation/documented] An init command writes a config file, CLAUDE.md instructions, a .claude/settings.json hook wiring, Husky pre-push hook if present, and package.json scripts like land, sync, promote, preview. -- evidence: [README.md#L23-L26](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L23-L26), [README.md#L101-L113](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L101-L113)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The land command rebases and pushes a lane onto the integration branch through a FIFO queue so two lanes are never mid-push simultaneously; agents can run it themselves. -- evidence: [README.md#L81-L90](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L81-L90)
  - [observation/documented] A WorktreeCreate hook plugs the tool's numbered lanes into Claude Code's native worktree creation, and build-lock serializes builds machine-wide across lanes. -- evidence: [README.md#L81-L90](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L81-L90)
- tools-permissions (2 claim(s)):
  - [observation/documented] A pre-push hook rejects direct git pushes to the integration branch and runs checkCommand before allowing a landing; with no checkCommand configured, every push fails by default. -- evidence: [README.md#L92-L97](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L92-L97)
  - [observation/documented] Blocked pushes can be bypassed via a single environment variable (CLAUDE_CODE_MERGE_QUEUE_EMERGENCY_PUSH=1), which the README notes is a convention, not a guarantee against an adversarial agent. -- evidence: [README.md#L125-L126](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L125-L126), [README.md#L117-L119](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L117-L119), [README.md#L121-L123](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L121-L123)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] README badges indicate TypeScript 5.x, Node >=18, MIT license, and zero runtime dependencies; the package is published on npm as claude-code-merge-queue. -- evidence: [README.md#L5-L13](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L5-L13)
- limitations (3 claim(s)):
More evidence: [full detail](claude-code-merge-queue.detail.md)

Metadata and full claim list: [full detail](claude-code-merge-queue.detail.md)
Human notes ([notes](claude-code-merge-queue.notes.md), never overwritten by build)

[Back to map index](../../index.md)
