---
access: public
aliases: []
claim_ids:
- clm_16b2ac86a400ecfc2abd2ad751c23e0c6067d6307ea85e230d1e6aabf09b0b65
- clm_1830d8daed69ad935906c2dacc7147ecb9e35d3b5cadcfb9dd848ea54631162e
- clm_217402aa2d8e51ffed9849a6e4850a2b576d04d99095f4151368e72d585d7c62
- clm_2df600ab73b950089bd3a58b6414ce963c27ec834ef17a37d1c0fb87152bba84
- clm_92210d92405ff1624b4d399a4ae581d9850e4833f2728906b5e8edc5996c5bfd
- clm_ba62e3b07c1ec94ee50962ce29afc060a248fc218d3e5e906c14fe9f0f9bfb4d
- clm_f3ce657bedc76bb15260ef489db1ebaadb3ba3d47c9ab3158fe92d81ebe2f2b8
maturity: draft
page_id: pg_0aa8bd3607ac5592b470cfd7ede36049
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b18f70ac04925770a5005d2421bf5366
title: herdrdev/herdr/README.md @ aa961df943b8
updated_at: '2026-09-14T03:08:56Z'
---

# herdrdev/herdr/README.md @ aa961df943b8

<!-- rcw:begin owner=source:src_b18f70ac04925770a5005d2421bf5366 block=evidence -->
- Agents can drive Herdr through a CLI and socket API to spawn panes, prompt each other, and wait until another agent is blocked. [@claim:clm_16b2ac86a400ecfc2abd2ad751c23e0c6067d6307ea85e230d1e6aabf09b0b65]
- The TUI supports tmux-style prefix keys plus mouse click, drag, and split interactions. [@claim:clm_1830d8daed69ad935906c2dacc7147ecb9e35d3b5cadcfb9dd848ea54631162e]
- After a server or machine restart, Herdr restores layout and can resume supported agent sessions, but the original processes do not survive. [@claim:clm_217402aa2d8e51ffed9849a6e4850a2b576d04d99095f4151368e72d585d7c62]
- Herdr is described as a single Rust binary with no Electron dependency, running inside the user's existing terminal. [@claim:clm_2df600ab73b950089bd3a58b6414ce963c27ec834ef17a37d1c0fb87152bba84]
- Each pane is marked working, blocked, or idle, and Herdr signals when an agent stops and needs input. [@claim:clm_92210d92405ff1624b4d399a4ae581d9850e4833f2728906b5e8edc5996c5bfd]
- The product keeps terminals running in a background server so work continues after the client closes or SSH drops, and restores saved layout after server or machine restart. [@claim:clm_ba62e3b07c1ec94ee50962ce29afc060a248fc218d3e5e906c14fe9f0f9bfb4d]
- Herdr runs agents like Claude Code, Codex, Cursor, OpenCode, and Grok in their own terminals without wrapping or replacing them. [@claim:clm_f3ce657bedc76bb15260ef489db1ebaadb3ba3d47c9ab3158fe92d81ebe2f2b8]
<!-- rcw:end owner=source:src_b18f70ac04925770a5005d2421bf5366 block=evidence -->

## Researcher notes

