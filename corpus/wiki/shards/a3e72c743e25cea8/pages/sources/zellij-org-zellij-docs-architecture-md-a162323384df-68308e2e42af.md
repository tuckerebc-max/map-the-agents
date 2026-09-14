---
access: public
aliases: []
claim_ids:
- clm_3d957ab74046ff817da29fd77c0116847b59b4c1ad392572c54919bb9498fcd8
- clm_6cf0d0bb45a5cb5e3150f51a8fbeae0a6953a8d49bd105b0f87e7b10f77ee8fb
- clm_ffdf28cf6513737c54693ff22f21b3569d47ca54f886b0c61a79e00a7778740f
maturity: draft
page_id: pg_5a9b5d997dc853eb813568308e2e42af
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_44591e94001953b48eea31d69253713a
title: zellij-org/zellij/docs/ARCHITECTURE.md @ a162323384df
updated_at: '2026-09-14T04:33:58Z'
---

# zellij-org/zellij/docs/ARCHITECTURE.md @ a162323384df

<!-- rcw:begin owner=source:src_44591e94001953b48eea31d69253713a block=evidence -->
- The Screen component manages on-screen panes: coordinating pane resizing, creating new panes, and closing panes while filling their space with others. [@claim:clm_3d957ab74046ff817da29fd77c0116847b59b4c1ad392572c54919bb9498fcd8]
- The PtyBus tracks asynchronous streams reading from pty sockets, parses bytes into ANSI/VT events, and sends them to the Screen for delivery to the relevant TerminalPane. [@claim:clm_6cf0d0bb45a5cb5e3150f51a8fbeae0a6953a8d49bd105b0f87e7b10f77ee8fb]
- TerminalPane connects a pane to a single pty (typically running a shell or program), tracks the Scroll line buffer, and interprets ANSI/VT instructions for styling and cursor positioning. [@claim:clm_ffdf28cf6513737c54693ff22f21b3569d47ca54f886b0c61a79e00a7778740f]
<!-- rcw:end owner=source:src_44591e94001953b48eea31d69253713a block=evidence -->

## Researcher notes

