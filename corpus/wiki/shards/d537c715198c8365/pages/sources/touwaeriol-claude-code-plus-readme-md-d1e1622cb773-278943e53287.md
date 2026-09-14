---
access: public
aliases: []
claim_ids:
- clm_7a0f8de7aa9c6f961325e310fd5977e2052c9b5363c3f4adf1b99d56aee2510f
- clm_7a8b51e8999587c202c2231420971e5f1099d98e098a4265986fbfe2bc871502
- clm_953af7d2190798029e07225a1c336389a9d8b953449a8688d3941f6f09fcc24e
- clm_bb863e917286dc6399fdc3a820cac94f124ba96595c1466a9f31aaca752b1154
- clm_c39bcd8acab8b1869e6c7b10c4bc8f883f9dc2cf2ddc54c98e3a7a113223aa79
- clm_d4c6feab9bbac90240a7ceeeb848d8ab280cfe4f4ea47507563e10bc93660a10
maturity: draft
page_id: pg_d5c14f5278f95dc19669278943e53287
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5cb9ae715f94540ab6faede3deee8502
title: touwaeriol/claude-code-plus/README.md @ d1e1622cb773
updated_at: '2026-09-14T03:19:53Z'
---

# touwaeriol/claude-code-plus/README.md @ d1e1622cb773

<!-- rcw:begin owner=source:src_5cb9ae715f94540ab6faede3deee8502 block=evidence -->
- A model selector lets users switch between Claude models (Opus 4.5, Sonnet 4.5, Haiku 4.5), including a /model slash command and default model in settings. [@claim:clm_7a0f8de7aa9c6f961325e310fd5977e2052c9b5363c3f4adf1b99d56aee2510f]
- Repository development practice: the README welcomes contributions via pull requests, and the changelog records CI verification-matrix and caching build practices. [@claim:clm_7a8b51e8999587c202c2231420971e5f1099d98e098a4265986fbfe2bc871502]
- The plugin supports MCP (Model Context Protocol) servers to extend Claude's capabilities, with status monitoring, reconnect, and enable/disable controls. [@claim:clm_953af7d2190798029e07225a1c336389a9d8b953449a8688d3941f6f09fcc24e]
- File write operations go through a secure authorization dialog, and the plugin added a dynamic MCP tool allowlist for flexible tool permissions. [@claim:clm_bb863e917286dc6399fdc3a820cac94f124ba96595c1466a9f31aaca752b1154]
- The plugin requires a JetBrains IDE (builds 242-253) and Node.js v18 or higher with node on PATH, and bundles a Claude CLI so no separate CLI install is needed. [@claim:clm_c39bcd8acab8b1869e6c7b10c4bc8f883f9dc2cf2ddc54c98e3a7a113223aa79]
- The product is an IntelliJ IDEA plugin that integrates Claude AI into the IDE, offering code assistance via natural-language chat. [@claim:clm_d4c6feab9bbac90240a7ceeeb848d8ab280cfe4f4ea47507563e10bc93660a10]
<!-- rcw:end owner=source:src_5cb9ae715f94540ab6faede3deee8502 block=evidence -->

## Researcher notes

