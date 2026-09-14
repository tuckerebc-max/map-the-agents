---
access: public
aliases: []
claim_ids:
- clm_77577541eb5f0a9cf8f26cd1045adc0f58820ca1e859602ff4fd80aa62e3e850
- clm_91adb5957045edfa9c0a803ea604a92b2781e5daa6253043c28bbd8308a069cf
- clm_d08bdecd2526bf4bc9cbb1979230fbfe17fe4acc12d084749e0ab4a720805cbe
- clm_f3e99aceead92ea62c85b9b92b107f1687276f0df0cfc613194cf8d828d758dc
- clm_f7fa31157bbb834300751eae16d569f871be4a41a8c9efdaab2544df9d084e21
maturity: draft
page_id: pg_eea934ccf6375f6aa0a61869fd4d0bc9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f8b182f778f856e686c542292a54d9bb
title: blaine/fantastty/docs/plans/2026-03-07-tmux-attach-design.md @ 60d248d0d20a
updated_at: '2026-09-14T03:38:52Z'
---

# blaine/fantastty/docs/plans/2026-03-07-tmux-attach-design.md @ 60d248d0d20a

<!-- rcw:begin owner=source:src_f8b182f778f856e686c542292a54d9bb block=evidence -->
- The attach design uses inert do-nothing PTYs per pane (discarding input) so real I/O flows through the tmux control connection, with input intercepted at SurfaceView level. [@claim:clm_77577541eb5f0a9cf8f26cd1045adc0f58820ca1e859602ff4fd80aa62e3e850]
- A dated design document proposes tmux control-mode (-CC) attach so tmux windows render as native tabs and panes as Ghostty splits; it appears to be a plan, not necessarily shipped behavior. [@claim:clm_91adb5957045edfa9c0a803ea604a92b2781e5daa6253043c28bbd8308a069cf]
- The attach design specifies a TmuxControlClient Swift actor per attached session, with all I/O and event handling actor-isolated, plus pure parser structs for protocol and layout. [@claim:clm_d08bdecd2526bf4bc9cbb1979230fbfe17fe4acc12d084749e0ab4a720805cbe]
- The attach design requires tmux control mode from tmux 1.8+ and tmux 3.3+ for shell-integration passthrough, with a version check and warning on connect. [@claim:clm_f3e99aceead92ea62c85b9b92b107f1687276f0df0cfc613194cf8d828d758dc]
- The attach design lists non-goals: no tmux status-bar or border rendering, no Mosh support (standard SSH only), and no auto-reconnect on SSH drop (manual reconnect). [@claim:clm_f7fa31157bbb834300751eae16d569f871be4a41a8c9efdaab2544df9d084e21]
<!-- rcw:end owner=source:src_f8b182f778f856e686c542292a54d9bb block=evidence -->

## Researcher notes

