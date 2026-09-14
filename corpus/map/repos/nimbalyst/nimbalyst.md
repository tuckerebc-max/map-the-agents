# nimbalyst/nimbalyst

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d6e1d008d9ee @ 777ff5f0ac48054d

## Summary (orientation draft, not independently verified)

Nimbalyst is described as an open-source, MIT-licensed visual workspace for building with coding agents such as Codex, Claude Code, and OpenCode, shipped as a desktop app for macOS, Windows, and Linux with an iOS companion app. The repository is a TypeScript/Electron npm-workspaces monorepo with packages for the Electron desktop app, a native SwiftUI iOS app, cross-platform runtime services (AI, sync, Lexical editor), a collab-protocol wire-format package, an extension SDK, and built-in extensions.

## Source coverage

Source coverage (partial): 3 of 89 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Nimbalyst is described as an open-source, MIT-licensed visual workspace for building with coding agents such as Codex, Claude Code, and OpenCode, shipped as a desktop app for macOS, Windows, and Linux with an iOS companion app. -- evidence: [README.md#L163-L165](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L163-L165), [README.md#L3-L3](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The repository is a TypeScript/Electron npm-workspaces monorepo with packages for the Electron desktop app, a native SwiftUI iOS app, cross-platform runtime services (AI, sync, Lexical editor), a collab-protocol wire-format package, an extension SDK, and built-in extensions. -- evidence: [CLAUDE.md#L123-L132](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L123-L132), [README.md#L144-L149](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L144-L149), [README.md#L129-L129](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L129-L129)
- design-choices (2 claim(s)):
  - [observation/documented] Content and status are stored as plain markdown files and workflows as slash commands inside the user's git repo, with no proprietary store, and parallel agent sessions are each isolated in their own git worktree. -- evidence: [README.md#L21-L31](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L21-L31)
  - [observation/documented] The app sends anonymous usage analytics to PostHog, states it collects no PII, file contents/paths, API keys, or document/session/chat content, uses a random anonymous install ID, and offers an opt-out in Settings. -- evidence: [README.md#L118-L121](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L118-L121), [README.md#L116-L116](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L116-L116), [README.md#L123-L123](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L123-L123)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md instructs AI contributors that any runtime-behavior change ships with a unit test and that the pre-push gate (npm run typecheck && npm run test:prepush) must be run locally, with failures recorded to .vitest/last-run.log readable via npm run test:last. -- evidence: [CLAUDE.md#L25-L25](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L25-L25), [CLAUDE.md#L27-L27](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L27-L27)
  - [observation/documented] Repository development practice: parallel work slices must declare disjoint file sets (including CHANGELOG.md and package.json), slices never run the full gate themselves, and CHANGELOG entries are written only when a commit is requested, one bullet per feature with no internal scaffolding. -- evidence: [CLAUDE.md#L13-L13](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L13-L13), [CLAUDE.md#L9-L9](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L9-L9), [CLAUDE.md#L21-L21](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L21-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Every editor, built-in or custom, goes through the same EditorHost contract, making pluggable editors for arbitrary file types first-class; existing extensions include an Astro website editor, visual git log, mindmap, slides, and a 3D object editor. -- evidence: [README.md#L75-L77](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L75-L77), [README.md#L21-L31](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L21-L31)
More evidence: [full detail](nimbalyst.detail.md)

Metadata and full claim list: [full detail](nimbalyst.detail.md)
Human notes ([notes](nimbalyst.notes.md), never overwritten by build)

[Back to map index](../../index.md)
