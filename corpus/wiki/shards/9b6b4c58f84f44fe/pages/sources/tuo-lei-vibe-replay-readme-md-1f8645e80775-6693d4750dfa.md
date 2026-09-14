---
access: public
aliases: []
claim_ids:
- clm_392d2a8c9cd576cdbee8b1aa7e2cc36e0db240cd44856d7dc37de487e51ece44
- clm_725c6e2c3ce09f0d7c33efd010f893bfe328b2c5312dd2bf6e5113acfa999bc2
- clm_af1f320f794a3bda267039348f24480a43397405f16dbf6ee97a90c2258e50a6
- clm_b140e9b755925363aefbba99dd95546395b462c30d0f4f5373e7c89bb72ea838
- clm_b69b00d3dab62412ca4e1edc7ab43220c15ec2fe25d3bbe5423dce60c630426e
- clm_cdfd3d88ed9d6a38d0ba0ab9541fb8dad15ac24c557b5a94cf1559d017cce07e
- clm_d29a9a19c3f403e6dbdb850a7db353ec9e33bf75158d4c4daffbe28386069613
- clm_db54421ba4b204701dc539f7fad789fdd4583af7e309a27168086c1cf05d2a8d
- clm_f5c7c9e929bd6337be9e877c74d160c1da8310121d2d9dc3d5fbedaf61e276f0
maturity: draft
page_id: pg_7380213da6645058b08b6693d4750dfa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4d26b8aaa2aa5c5ba7ca96d97f05ee05
title: tuo-lei/vibe-replay/README.md @ 1f8645e80775
updated_at: '2026-09-14T04:27:41Z'
---

# tuo-lei/vibe-replay/README.md @ 1f8645e80775

<!-- rcw:begin owner=source:src_4d26b8aaa2aa5c5ba7ca96d97f05ee05 block=evidence -->
- Remote SSH sources are configured in ~/.vibe-replay/config.json with id, label, sshHost, and provider list; the tool reuses existing OpenSSH keys, aliases, and ProxyJump settings and stores no credentials itself. [@claim:clm_392d2a8c9cd576cdbee8b1aa7e2cc36e0db240cd44856d7dc37de487e51ece44]
- The product is invoked via an npx CLI (e.g. `npx vibe-replay`, `-d` for dashboard, `-p grok-bot`) that auto-discovers sessions and emits a single self-contained HTML replay file. [@claim:clm_725c6e2c3ce09f0d7c33efd010f893bfe328b2c5312dd2bf6e5113acfa999bc2]
- SSH remote indexing of Grok Bot transcripts is not included yet, per the provider documentation. [@claim:clm_af1f320f794a3bda267039348f24480a43397405f16dbf6ee97a90c2258e50a6]
- Generated replays are self-contained HTML files that make no automatic external requests; remote HTTP(S) images load only after an explicit per-image click, and data URLs render immediately. [@claim:clm_b140e9b755925363aefbba99dd95546395b462c30d0f4f5373e7c89bb72ea838]
- The tool is local-first: it reads session files and generates local HTML without an account, and data leaves the machine only on explicit Gist/cloud publish or login, when aggregated (non-conversation) insights sync daily. [@claim:clm_b69b00d3dab62412ca4e1edc7ab43220c15ec2fe25d3bbe5423dce60c630426e]
- A portable replay skill ships at skills/replay/SKILL.md for the Agent Skills standard, installable via `npx skills add tuo-lei/vibe-replay --skill replay -g` or by manually downloading the file into ~/.claude/skills/replay. [@claim:clm_cdfd3d88ed9d6a38d0ba0ab9541fb8dad15ac24c557b5a94cf1559d017cce07e]
- Ask Replay is documented as a read-only assistant: it can inspect data and navigate the editor but never edits files, publishes, or mutates state; requested mutations are returned to the user as handoff data for review. [@claim:clm_d29a9a19c3f403e6dbdb850a7db353ec9e33bf75158d4c4daffbe28386069613]
- Secret redaction is built in: API keys, tokens, PEM keys, and sensitive paths are detected and redacted before replay generation. [@claim:clm_db54421ba4b204701dc539f7fad789fdd4583af7e309a27168086c1cf05d2a8d]
- AI provider credentials and OAuth refresh tokens are stored in ~/.vibe-replay/ai-auth.json with restricted permissions, with the path overridable via VIBE_REPLAY_AI_AUTH; credentials stay out of replay files and cloud uploads. [@claim:clm_f5c7c9e929bd6337be9e877c74d160c1da8310121d2d9dc3d5fbedaf61e276f0]
<!-- rcw:end owner=source:src_4d26b8aaa2aa5c5ba7ca96d97f05ee05 block=evidence -->

## Researcher notes

