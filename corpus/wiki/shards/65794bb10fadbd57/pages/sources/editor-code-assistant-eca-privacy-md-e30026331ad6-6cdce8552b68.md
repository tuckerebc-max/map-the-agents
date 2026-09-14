---
access: public
aliases: []
claim_ids:
- clm_410b6a3eb93f3428668a9f23bf20cd1f32dd150b1e63ab94d2bb4fd93c567ecd
- clm_49283325dde0ef9b2855f4e8d28c1ee9f2e4f8de53273c89474436b3984c4dca
- clm_bcffd2f1369425f3d43da287d372c0c299c641b3f439ce02cf5f2a0415e23d13
maturity: draft
page_id: pg_6787b940d35a551cae9f6cdce8552b68
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_584caea6a24d5407bb692358b5e4745f
title: editor-code-assistant/eca/PRIVACY.md @ e30026331ad6
updated_at: '2026-09-14T01:47:30Z'
---

# editor-code-assistant/eca/PRIVACY.md @ e30026331ad6

<!-- rcw:begin owner=source:src_584caea6a24d5407bb692358b5e4745f block=evidence -->
- Per its privacy policy, ECA runs entirely locally with no hosted service, no accounts, no analytics or tracking, and ships with no MCP servers enabled by default. [@claim:clm_410b6a3eb93f3428668a9f23bf20cd1f32dd150b1e63ab94d2bb4fd93c567ecd]
- Documented providers include Anthropic, OpenAI, GitHub Copilot, Google Gemini, Azure OpenAI, DeepSeek, OpenRouter, xAI, and locally running Ollama, plus custom providers. [@claim:clm_49283325dde0ef9b2855f4e8d28c1ee9f2e4f8de53273c89474436b3984c4dca]
- Locally, ECA stores config in ~/.config/eca/config.json, auth tokens in ~/.cache/eca/db.transit.json, and per-workspace conversation history plus truncated tool outputs auto-deleted after 7 days, respecting XDG paths. [@claim:clm_bcffd2f1369425f3d43da287d372c0c299c641b3f439ce02cf5f2a0415e23d13]
<!-- rcw:end owner=source:src_584caea6a24d5407bb692358b5e4745f block=evidence -->

## Researcher notes

