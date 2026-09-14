---
access: public
aliases: []
claim_ids:
- clm_65bb86ae4149ee01a598b845f4810bd16c8906b4a3ff354f060fff5d2bfe939b
- clm_bb92a300bee440aec290092a449a3b1a5f28f2f8b55a49f2ec8126820988591e
- clm_dc4a6bb564069f27c0d5319a2da08da825a1957874b72f846fab1e3a7dac4c62
- clm_e8e585d9f5405bcd4ce7afe08b501f314913f8a68cbb7687cd53fa5ef4e4f0f1
- clm_fcb6c2beae5b10a5987a3aa1cedfc2527b715afdfa144f0b361c969edf116b18
maturity: draft
page_id: pg_b93ea194125f59338d3c87e067df09ea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e611332507650c2979c57a00839aba1
title: proxysoul/Empryo/GETTING_STARTED.md @ f771fc238e64
updated_at: '2026-09-14T02:32:49Z'
---

# proxysoul/Empryo/GETTING_STARTED.md @ f771fc238e64

<!-- rcw:begin owner=source:src_7e611332507650c2979c57a00839aba1 block=evidence -->
- Source/npm installs require Bun (>= 1.0) rather than Node.js; Neovim >= 0.11 is needed for the embedded editor; a Nerd Font is needed for icons. [@claim:clm_65bb86ae4149ee01a598b845f4810bd16c8906b4a3ff354f060fff5d2bfe939b]
- A privacy feature lets users block file patterns (e.g. .env, secrets/**) via /privacy add; the agent then refuses to read, display, or access matching files even through shell commands. [@claim:clm_bb92a300bee440aec290092a449a3b1a5f28f2f8b55a49f2ec8126820988591e]
- The terminal UI embeds a real Neovim instance (Ctrl+E toggles focus), with config modes selectable via /nvim-config (auto, user, default, none). [@claim:clm_dc4a6bb564069f27c0d5319a2da08da825a1957874b72f846fab1e3a7dac4c62]
- A task router assigns models to ten routable roles (e.g. spark for read-only scouting, ember for code edits, verify for review), configurable per tab, per project, or globally, with custom agents definable. [@claim:clm_e8e585d9f5405bcd4ce7afe08b501f314913f8a68cbb7687cd53fa5ef4e4f0f1]
- A SQLite-backed memory system stores decisions, patterns, and preferences across conversations, with write scope configurable to session, project, or global and memories injected into the system prompt. [@claim:clm_fcb6c2beae5b10a5987a3aa1cedfc2527b715afdfa144f0b361c969edf116b18]
<!-- rcw:end owner=source:src_7e611332507650c2979c57a00839aba1 block=evidence -->

## Researcher notes

