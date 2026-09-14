# abcwyc/pi-agent-desktop

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 378db4dc27e4 @ 54f269a83aa71cea

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is a local AI agent desktop application for macOS and Windows that packages the pi agent's capabilities into a standalone installable app. The app bundles three components: the desktop shell authored in this fork, the pi agent runtime as an npm dependency, and the pi-web UI merged from an upstream release tag.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is a local AI agent desktop application for macOS and Windows that packages the pi agent's capabilities into a standalone installable app. -- evidence: [README.md#L5-L5](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] The app bundles three components: the desktop shell authored in this fork, the pi agent runtime as an npm dependency, and the pi-web UI merged from an upstream release tag. -- evidence: [docs/ownership-boundaries.md#L7-L11](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/ownership-boundaries.md#L7-L11)
  - [observation/documented] The desktop package bundles a Next.js standalone server, a Node.js runtime, and the current Pi SDK, so the local server starts with the app without separate installation. -- evidence: [README.md#L38-L38](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L38-L38)
- design-choices (2 claim(s)):
  - [observation/documented] Updates are whole-app only: the upgrade button installs one complete signed build containing all three components and restarts; it never patches individual JavaScript packages or downloads unsigned files. -- evidence: [README.md#L72-L76](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L72-L76), [README.md#L80-L80](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L80-L80)
  - [observation/documented] The web UI uses a small internal i18n layer with English and Simplified Chinese packages, browser-inferred initial locale, and persistence in localStorage under pi-locale. -- evidence: [docs/i18n.md#L3-L6](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/i18n.md#L3-L6), [docs/i18n.md#L12-L13](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/i18n.md#L12-L13), [docs/i18n.md#L15-L17](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/i18n.md#L15-L17)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm test, tsc --noEmit, npm run lint, cargo fmt/clippy checks, and npm run release:verify; they should avoid next build during normal development. -- evidence: [README.md#L130-L130](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L130-L130), [README.md#L142-L143](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L142-L143), [README.md#L116-L116](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L116-L116), [README.md#L136-L136](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L136-L136), [README.md#L133-L133](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L133-L133), [README.md#L146-L147](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L146-L147)
  - [observation/documented] Repository development practice: a nightly component-updates workflow syncs upstream pi and pi-web releases, intersecting changes with fork-ownership.json and running the full gate before pushing to main or opening a PR. -- evidence: [docs/ownership-boundaries.md#L19-L20](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/ownership-boundaries.md#L19-L20), [README.md#L172-L175](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L172-L175), [docs/ownership-boundaries.md#L22-L24](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/ownership-boundaries.md#L22-L24)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Features include browsing and resuming past Pi sessions, real-time chat with visible thinking/tool calls/cost, branching or forking conversations, and Git worktree switching from the sidebar. -- evidence: [README.md#L9-L17](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L9-L17)
  - [observation/documented] The app can preview source code, diffs, Markdown, images, audio, PDF, and DOCX files, and offers dark mode, automatic session naming, and a completion sound. -- evidence: [README.md#L9-L17](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L9-L17)
- memory-state (1 claim(s)):
More evidence: [full detail](pi-agent-desktop.detail.md)

Metadata and full claim list: [full detail](pi-agent-desktop.detail.md)
Human notes ([notes](pi-agent-desktop.notes.md), never overwritten by build)

[Back to map index](../../index.md)
