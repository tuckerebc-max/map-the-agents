# tuo-lei/vibe-replay -- full detail

[Back to orientation](vibe-replay.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tuo-lei/vibe-replay/1f8645e807753620004f9ae75f595f0d06f8d4ba/76aec0fa0043c673.json](../../../wiki/dossiers/tuo-lei/vibe-replay/1f8645e807753620004f9ae75f595f0d06f8d4ba/76aec0fa0043c673.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Generated replays are self-contained HTML files that make no automatic external requests; remote HTTP(S) images load only after an explicit per-image click, and data URLs render immediately. -- evidence: [README.md#L179-L190](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L179-L190), [AGENTS.md#L58-L94](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L58-L94), [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271) (`clm_b140e9b755925363aefbba99dd95546395b462c30d0f4f5373e7c89bb72ea838`)
- [observation/documented] The tool is local-first: it reads session files and generates local HTML without an account, and data leaves the machine only on explicit Gist/cloud publish or login, when aggregated (non-conversation) insights sync daily. -- evidence: [README.md#L179-L190](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L179-L190), [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271) (`clm_b69b00d3dab62412ca4e1edc7ab43220c15ec2fe25d3bbe5423dce60c630426e`)
- [observation/documented] Secret redaction is built in: API keys, tokens, PEM keys, and sensitive paths are detected and redacted before replay generation. -- evidence: [README.md#L179-L190](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L179-L190), [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271) (`clm_db54421ba4b204701dc539f7fad789fdd4583af7e309a27168086c1cf05d2a8d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: AGENTS.md is the single source of truth for coding agents (CLAUDE.md is an @AGENTS.md shim), with pnpm-only tooling, oxlint/oxfmt via lefthook pre-commit, `pnpm verify` as the pre-PR gate, and a guard test enforcing the agent-instruction wiring and a 32 KiB AGENTS.md size limit. -- evidence: [AGENTS.md#L191-L194](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L191-L194), [AGENTS.md#L185-L187](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L185-L187), [AGENTS.md#L3-L6](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L3-L6), [AGENTS.md#L98-L110](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L98-L110), [AGENTS.md#L176-L183](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L176-L183), [AGENTS.md#L16-L30](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/AGENTS.md#L16-L30) (`clm_f6920e88e359fe8570f0f995113b7a5b07dc46e41557bf58e6bc802487af3101`)

## skills-patterns (1 claim(s))

- [observation/documented] A portable replay skill ships at skills/replay/SKILL.md for the Agent Skills standard, installable via `npx skills add tuo-lei/vibe-replay --skill replay -g` or by manually downloading the file into ~/.claude/skills/replay. -- evidence: [README.md#L145-L145](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L145-L145), [README.md#L157-L161](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L157-L161), [README.md#L147-L149](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L147-L149) (`clm_cdfd3d88ed9d6a38d0ba0ab9541fb8dad15ac24c557b5a94cf1559d017cce07e`)

## interfaces (2 claim(s))

- [observation/documented] The product is invoked via an npx CLI (e.g. `npx vibe-replay`, `-d` for dashboard, `-p grok-bot`) that auto-discovers sessions and emits a single self-contained HTML replay file. -- evidence: [README.md#L227-L227](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L227-L227), [README.md#L17-L19](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L17-L19), [README.md#L209-L211](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L209-L211), [README.md#L34-L34](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L34-L34) (`clm_725c6e2c3ce09f0d7c33efd010f893bfe328b2c5312dd2bf6e5113acfa999bc2`)
- [observation/documented] Ask Replay exposes bounded read-only server tools such as search_sessions, get_session_summary, get_session_content, get_scene, get_session_annotations, get_session_overlays, and get_insights with time ranges like 7d/30d/90d/all. -- evidence: [docs/ai-chat-feature-parity.md#L10-L27](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/docs/ai-chat-feature-parity.md#L10-L27) (`clm_f24a361e3953ef8183d1714ac85a48a3dcc82d45033041cce148e0c60a4d081d`)

## memory-state (2 claim(s))

- [observation/documented] Remote SSH sources are configured in ~/.vibe-replay/config.json with id, label, sshHost, and provider list; the tool reuses existing OpenSSH keys, aliases, and ProxyJump settings and stores no credentials itself. -- evidence: [README.md#L42-L43](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L42-L43), [README.md#L58-L60](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L58-L60), [README.md#L45-L56](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L45-L56), [README.md#L62-L62](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L62-L62) (`clm_392d2a8c9cd576cdbee8b1aa7e2cc36e0db240cd44856d7dc37de487e51ece44`)
- [observation/documented] AI provider credentials and OAuth refresh tokens are stored in ~/.vibe-replay/ai-auth.json with restricted permissions, with the path overridable via VIBE_REPLAY_AI_AUTH; credentials stay out of replay files and cloud uploads. -- evidence: [README.md#L257-L271](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L257-L271) (`clm_f5c7c9e929bd6337be9e877c74d160c1da8310121d2d9dc3d5fbedaf61e276f0`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Ask Replay is documented as a read-only assistant: it can inspect data and navigate the editor but never edits files, publishes, or mutates state; requested mutations are returned to the user as handoff data for review. -- evidence: [README.md#L229-L245](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L229-L245), [docs/ai-chat-feature-parity.md#L3-L6](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/docs/ai-chat-feature-parity.md#L3-L6), [README.md#L106-L111](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L106-L111), [docs/ai-chat-feature-parity.md#L37-L51](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/docs/ai-chat-feature-parity.md#L37-L51) (`clm_d29a9a19c3f403e6dbdb850a7db353ec9e33bf75158d4c4daffbe28386069613`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] SSH remote indexing of Grok Bot transcripts is not included yet, per the provider documentation. -- evidence: [README.md#L215-L215](https://github.com/tuo-lei/vibe-replay/blob/1f8645e807753620004f9ae75f595f0d06f8d4ba/README.md#L215-L215) (`clm_af1f320f794a3bda267039348f24480a43397405f16dbf6ee97a90c2258e50a6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

