---
access: public
aliases: []
claim_ids:
- clm_0d97a3f036e85b5246bf559cb00efabd330d74375f7b294d7d77a2af2e601030
- clm_c00023d751c7808ad2a8828b7712b7ae498a1f0ef28dae622d6a9fecbbcb21da
- clm_fddc79e3507044a1182c9e093186a43a59186cc79f8ece553c42bc7f8f03b83c
maturity: draft
page_id: pg_c491a54c23b551cbb9d9ce5c9bcb2022
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7777df607ea65d5789c4cc37024ef061
title: neovateai/neovate-code/docs/designs/2025-01-26-global-terminal-focus-event-handler.md
  @ 0a24b363ecbe
updated_at: '2026-09-14T02:22:03Z'
---

# neovateai/neovate-code/docs/designs/2025-01-26-global-terminal-focus-event-handler.md @ 0a24b363ecbe

<!-- rcw:begin owner=source:src_7777df607ea65d5789c4cc37024ef061 block=evidence -->
- The chosen fix is a global always-active useInput hook in ChatInput.tsx to intercept focus events, with a simplified skip-handler kept in TextInput as a safety net. [@claim:clm_0d97a3f036e85b5246bf559cb00efabd330d74375f7b294d7d77a2af2e601030]
- A design doc dated 2025-01-26 addresses terminal focus escape sequences ([I]/[O]) appearing as literal text in the chat input when modals are shown, because Ink strips the escape prefix. [@claim:clm_c00023d751c7808ad2a8828b7712b7ae498a1f0ef28dae622d6a9fecbbcb21da]
- The focus handler updates window focus state via useAppStore.getState().setWindowFocused, setting true for '[I' (focus gained) and false for '[O' (focus lost). [@claim:clm_fddc79e3507044a1182c9e093186a43a59186cc79f8ece553c42bc7f8f03b83c]
<!-- rcw:end owner=source:src_7777df607ea65d5789c4cc37024ef061 block=evidence -->

## Researcher notes

