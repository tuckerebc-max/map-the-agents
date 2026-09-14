# pingdotgg/t3code

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 66e39ca2aabd @ 9b65991334d57d26

## Summary (orientation draft, not independently verified)

Selected evidence records: T3 Code lets users control coding agents remotely through an iOS app, Android app, web app, and an Electron-based desktop app. The product works with existing subscriptions to Claude Code, Codex, Cursor, Grok Build, OpenCode, and Google Antigravity, controlling those agents when set up on the user's computer.

## Source coverage

Source coverage (partial): 4 of 4 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The project charges nothing for the product and states it aims to be performant, remote-ready, and open enough that users can fork and build their own editor. -- evidence: [README.md#L11-L11](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L11-L11), [README.md#L9-L9](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L9-L9)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md forbids killing processes by name/path matching, forbids starting servers against or writing to the live ~/.t3/userdata database, and forbids setting VITE_HTTP_URL/VITE_WS_URL in dev because Vite proxies /api, /ws, /oauth, and /.well-known. -- evidence: [AGENTS.md#L61-L63](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/AGENTS.md#L61-L63)
  - [observation/documented] Repository development practice: agents must never open a PR unless the developer explicitly asks; PRs use conventional-commit titles, one concern per PR, before/after images for UI changes, and evidence uploaded to GitHub rather than committed. -- evidence: [AGENTS.md#L115-L121](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/AGENTS.md#L115-L121)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] T3 Code lets users control coding agents remotely through an iOS app, Android app, web app, and an Electron-based desktop app. -- evidence: [README.md#L3-L3](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L3-L3)
  - [observation/documented] Running `npx t3@latest` launches the T3 Code backend on the local machine plus a local web app for controlling agents; a `--help` flag exposes the full CLI reference. -- evidence: [README.md#L35-L35](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L35-L35), [README.md#L33-L33](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L33-L33), [README.md#L29-L31](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L29-L31)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The product works with existing subscriptions to Claude Code, Codex, Cursor, Grok Build, OpenCode, and Google Antigravity, controlling those agents when set up on the user's computer. -- evidence: [README.md#L5-L5](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L5-L5)
  - [observation/documented] At least one provider must be installed and authenticated before use; each provider names a CLI and login command, while Antigravity is enabled in Settings with Google sign-in and needs no CLI. -- evidence: [README.md#L15-L23](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L15-L23)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](t3code.detail.md)

Metadata and full claim list: [full detail](t3code.detail.md)
Human notes ([notes](t3code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
