# tuo-lei/vibe-replay

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1f8645e80775 @ 76aec0fa0043c673

## Summary (orientation draft, not independently verified)

The product is invoked via an npx CLI (e.g. `npx vibe-replay`, `-d` for dashboard, `-p grok-bot`) that auto-discovers sessions and emits a single self-contained HTML replay file. Ask Replay exposes bounded read-only server tools such as search_sessions, get_session_summary, get_session_content, get_scene, get_session_annotations, get_session_overlays, and get_insights with time ranges like 7d/30d/90d/all.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Generated replays are self-contained HTML files that make no automatic external requests; remote HTTP(S) images load only after an explicit per-image click, and data URLs render immediately. -- evidence: [README.md#L179-L190](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L179-L190), [AGENTS.md#L58-L94](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L58-L94), [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271)
  - [observation/documented] The tool is local-first: it reads session files and generates local HTML without an account, and data leaves the machine only on explicit Gist/cloud publish or login, when aggregated (non-conversation) insights sync daily. -- evidence: [README.md#L179-L190](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L179-L190), [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md is the single source of truth for coding agents (CLAUDE.md is an @AGENTS.md shim), with pnpm-only tooling, oxlint/oxfmt via lefthook pre-commit, `pnpm verify` as the pre-PR gate, and a guard test enforcing the agent-instruction wiring and a 32 KiB AGENTS.md size limit. -- evidence: [AGENTS.md#L191-L194](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L191-L194), [AGENTS.md#L185-L187](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L185-L187), [AGENTS.md#L3-L6](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L3-L6), [AGENTS.md#L98-L110](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L98-L110), [AGENTS.md#L176-L183](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L176-L183), [AGENTS.md#L16-L30](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L16-L30)
- skills-patterns (1 claim(s)):
  - [observation/documented] A portable replay skill ships at skills/replay/SKILL.md for the Agent Skills standard, installable via `npx skills add tuo-lei/vibe-replay --skill replay -g` or by manually downloading the file into ~/.claude/skills/replay. -- evidence: [README.md#L145-L145](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L145-L145), [README.md#L157-L161](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L157-L161), [README.md#L147-L149](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L147-L149)
- interfaces (2 claim(s)):
  - [observation/documented] The product is invoked via an npx CLI (e.g. `npx vibe-replay`, `-d` for dashboard, `-p grok-bot`) that auto-discovers sessions and emits a single self-contained HTML replay file. -- evidence: [README.md#L227-L227](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L227-L227), [README.md#L17-L19](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L17-L19), [README.md#L209-L211](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L209-L211), [README.md#L34-L34](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L34-L34)
  - [observation/documented] Ask Replay exposes bounded read-only server tools such as search_sessions, get_session_summary, get_session_content, get_scene, get_session_annotations, get_session_overlays, and get_insights with time ranges like 7d/30d/90d/all. -- evidence: [docs/ai-chat-feature-parity.md#L10-L27](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/docs/ai-chat-feature-parity.md#L10-L27)
- memory-state (2 claim(s)):
  - [observation/documented] Remote SSH sources are configured in ~/.vibe-replay/config.json with id, label, sshHost, and provider list; the tool reuses existing OpenSSH keys, aliases, and ProxyJump settings and stores no credentials itself. -- evidence: [README.md#L42-L43](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L42-L43), [README.md#L58-L60](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L58-L60), [README.md#L45-L56](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L45-L56), [README.md#L62-L62](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L62-L62)
  - [observation/documented] AI provider credentials and OAuth refresh tokens are stored in ~/.vibe-replay/ai-auth.json with restricted permissions, with the path overridable via VIBE_REPLAY_AI_AUTH; credentials stay out of replay files and cloud uploads. -- evidence: [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](vibe-replay.detail.md)

Metadata and full claim list: [full detail](vibe-replay.detail.md)
Human notes ([notes](vibe-replay.notes.md), never overwritten by build)

[Back to map index](../../index.md)
