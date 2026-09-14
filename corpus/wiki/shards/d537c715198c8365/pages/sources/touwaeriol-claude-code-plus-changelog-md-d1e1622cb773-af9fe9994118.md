---
access: public
aliases: []
claim_ids:
- clm_7a0f8de7aa9c6f961325e310fd5977e2052c9b5363c3f4adf1b99d56aee2510f
- clm_7a8b51e8999587c202c2231420971e5f1099d98e098a4265986fbfe2bc871502
- clm_8bef16158fa27fe6fae1d8d332697dd2e19f549bbae0db3e5ba43f768f42733c
- clm_953af7d2190798029e07225a1c336389a9d8b953449a8688d3941f6f09fcc24e
- clm_bb863e917286dc6399fdc3a820cac94f124ba96595c1466a9f31aaca752b1154
- clm_f2ef34ecd3c61427733d85f237a0a463a44bc88a3a4d19f5b65614dcf557b2ae
maturity: draft
page_id: pg_6b5bf2d24424516c978caf9fe9994118
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d9aec184bc715c7188fc3fce993b6ab9
title: touwaeriol/claude-code-plus/CHANGELOG.md @ d1e1622cb773
updated_at: '2026-09-14T03:19:53Z'
---

# touwaeriol/claude-code-plus/CHANGELOG.md @ d1e1622cb773

<!-- rcw:begin owner=source:src_d9aec184bc715c7188fc3fce993b6ab9 block=evidence -->
- A model selector lets users switch between Claude models (Opus 4.5, Sonnet 4.5, Haiku 4.5), including a /model slash command and default model in settings. [@claim:clm_7a0f8de7aa9c6f961325e310fd5977e2052c9b5363c3f4adf1b99d56aee2510f]
- Repository development practice: the README welcomes contributions via pull requests, and the changelog records CI verification-matrix and caching build practices. [@claim:clm_7a8b51e8999587c202c2231420971e5f1099d98e098a4265986fbfe2bc871502]
- The architecture appears to use RSocket over WebSocket for streaming chat and plain HTTP for non-streaming IDE actions, per the changelog's RSocket migration notes and AGENTS.md protocol descriptions. [@claim:clm_8bef16158fa27fe6fae1d8d332697dd2e19f549bbae0db3e5ba43f768f42733c]
- The plugin supports MCP (Model Context Protocol) servers to extend Claude's capabilities, with status monitoring, reconnect, and enable/disable controls. [@claim:clm_953af7d2190798029e07225a1c336389a9d8b953449a8688d3941f6f09fcc24e]
- File write operations go through a secure authorization dialog, and the plugin added a dynamic MCP tool allowlist for flexible tool permissions. [@claim:clm_bb863e917286dc6399fdc3a820cac94f124ba96595c1466a9f31aaca752b1154]
- Sessions support reconnection: the plugin resumes a session using a stored conversation ID and auto-reconnects when the frontend becomes visible again. [@claim:clm_f2ef34ecd3c61427733d85f237a0a463a44bc88a3a4d19f5b65614dcf557b2ae]
<!-- rcw:end owner=source:src_d9aec184bc715c7188fc3fce993b6ab9 block=evidence -->

## Researcher notes

