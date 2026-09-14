---
access: public
aliases: []
claim_ids:
- clm_0b02da203fcd2e0a243c4e30deaa795e79d4d8b59f5dfcea7e8a999bc22b8eff
- clm_1c11ef75f4016822545696a3233d63e6a0b281534636937351726d5b84750c16
- clm_7c84f0ded688464371f8545f706e76d5503c3655bd69ce36499ab24ddd991517
- clm_9858867453dde331039c980dac0b872b0f3117f15797ef68e9e470c2b7aa5d34
- clm_9af5d3b81bedbed1dc88fb2cd0215eeb02332706642b51ed199c353349e289e9
maturity: draft
page_id: pg_b6b7c5a87b925dd6a44410d6be2e9eea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_292ff47284ce520ca32a4df43a0fc231
title: earendil-works/pi/tui-plan.md @ 71dca871bc80
updated_at: '2026-09-14T01:47:27Z'
---

# earendil-works/pi/tui-plan.md @ 71dca871bc80

<!-- rcw:begin owner=source:src_292ff47284ce520ca32a4df43a0fc231 block=evidence -->
- Constrained layout is exposed via a ViewportTUI capability interface with setLayoutRoot; TuiAltScreen implements it while TuiMainScreen does not, and a type guard checks the capability rather than using instanceof. [@claim:clm_0b02da203fcd2e0a243c4e30deaa795e79d4d8b59f5dfcea7e8a999bc22b8eff]
- The TUI plan introduces a constrained alternate-screen layout so the coding-agent transcript scrolls while pending messages, status, editor, and footer stay fixed at the bottom; main-screen mode keeps terminal-owned scrolling. [@claim:clm_1c11ef75f4016822545696a3233d63e6a0b281534636937351726d5b84750c16]
- Wheel events are hit-tested against the committed frame and routed from the deepest box upward, with overscroll chaining or containment, falling back to the primary scroll view; keyboard scrolling actions remain always available. [@claim:clm_7c84f0ded688464371f8545f706e76d5503c3655bd69ce36499ab24ddd991517]
- The planned public layout primitives are VStack, HStack, and ScrollView, with stack entries configured via basis, grow, shrink, minSize, maxSize, and a viewport-dependent visible predicate. [@claim:clm_9858867453dde331039c980dac0b872b0f3117f15797ef68e9e470c2b7aa5d34]
- The internal layout tree is rebuilt per requested render as a transient frame snapshot, while the public component tree stays long-lived and stateful; leaf render caches in Markdown, Text, Image, and Box are reused. [@claim:clm_9af5d3b81bedbed1dc88fb2cd0215eeb02332706642b51ed199c353349e289e9]
<!-- rcw:end owner=source:src_292ff47284ce520ca32a4df43a0fc231 block=evidence -->

## Researcher notes

