# d-kimuson/claude-code-viewer

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9367cf006be9 @ d2e4b2b80b9562f7

## Summary (orientation draft, not independently verified)

Claude Code Viewer is a self-hosted web client that reads Claude Code JSONL session logs from ~/.claude/projects, offers real-time viewing, Git operations, an integrated terminal, and Agent-SDK chat features gated by authentication mode. Contributor rules in AGENTS.md/CLAUDE.md are development practice, not product behavior. Evidence coverage: 157 of 162 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The product includes an integrated terminal emulator in a bottom panel, letting users launch Claude Code from the browser without leaving it. -- evidence: [README.md#L31-L31](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L31-L31)
  - [observation/documented] It is a PWA supporting Add to Home Screen on mobile with an optimized UI and push notifications when sessions complete. -- evidence: [README.md#L95-L95](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L95-L95)
- design-choices (2 claim(s)):
  - [observation/documented] The app reads Claude Code conversation logs from ~/.claude/projects/<project>/<session-id>.jsonl JSONL files and automatically discovers new projects and sessions. -- evidence: [README.md#L236-L238](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L236-L238)
  - [observation/documented] Conversation data is preserved through strict Zod schema validation, with a progressive-disclosure UI that reveals details on demand. -- evidence: [README.md#L284-L289](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L284-L289), [README.md#L37-L37](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L37-L37)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must avoid 'as' casting, raw fetch, dev servers, and node built-ins; use Effect-TS and Hono RPC + TanStack Query, follow TDD, and run pnpm gatecheck check and lingui-check before committing. -- evidence: [AGENTS.md#L18-L21](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L18-L21), [AGENTS.md#L11-L14](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L11-L14), [AGENTS.md#L77-L80](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L77-L80), [AGENTS.md#L69-L69](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L69-L69)
  - [observation/documented] Repository development practice: commit messages follow Conventional Commits, appear in release notes, and 'fix' is reserved for user-facing bugs while internal fixes use 'chore'. -- evidence: [AGENTS.md#L25-L25](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L25-L25), [AGENTS.md#L38-L38](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L38-L38), [AGENTS.md#L31-L36](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L31-L36)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI accepts options including --port (default 3000), --hostname, --verbose, --password, --executable, --claude-dir, --api-only, and --base-path. -- evidence: [README.md#L71-L80](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L71-L80)
  - [observation/documented] When a password is configured, /api routes require authentication via a ccv-session cookie from /api/auth/login or an Authorization: Bearer header; without a password, API auth is disabled. -- evidence: [README.md#L153-L153](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L153-L153), [README.md#L150-L151](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L150-L151), [README.md#L148-L148](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L148-L148)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Due to Anthropic ToS ambiguity for subscription accounts, chat sending, session resuming, permission approval, and AskUserQuestion are opt-in; read-oriented features work independently of the Agent SDK. -- evidence: [README.md#L15-L20](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L15-L20)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](claude-code-viewer.detail.md)

Metadata and full claim list: [full detail](claude-code-viewer.detail.md)
Human notes ([notes](claude-code-viewer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
