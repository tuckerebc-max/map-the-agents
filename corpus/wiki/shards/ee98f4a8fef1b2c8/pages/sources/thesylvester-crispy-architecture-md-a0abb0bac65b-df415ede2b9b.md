---
access: public
aliases: []
claim_ids:
- clm_1fe536f25a0b7092a6525ac18efa25a95d3e4d94476ba8d06bf0059dc35a3656
- clm_469016ba51996fb2c16681be17455b1021d7294a7af2cb5bcee7da2cf0f3d981
- clm_5369ae7e775d7b7c0fa58e4d30e417480f256a0f42cbce32193a58ebf821e162
- clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497
- clm_78a23726e10d5758a231084fe7e0a58db96d0a0bd355375d3be4185f3ab9152b
- clm_8189e45d703dd865bbfce150d0a7e69c39a93e21427942b050bf84c69e1fbf8e
- clm_ac4a116f5472617a4e75f926cc71976339a62cb1945c37c1d8be3d922c5ad074
- clm_e2417184d61fc7c3e5646734dd3dac3b63c3739dd6de99fd231ffbd82090fd47
- clm_ea0709eb341359ebc0cabb856a5ecc98e85f082d2fb3f84f18a4333a37956516
maturity: draft
page_id: pg_1f80083e481c5e24a658df415ede2b9b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fb5fb91a836858208bb82157d67e036a
title: TheSylvester/crispy/architecture.md @ a0abb0bac65b
updated_at: '2026-09-14T03:18:51Z'
---

# TheSylvester/crispy/architecture.md @ a0abb0bac65b

<!-- rcw:begin owner=source:src_fb5fb91a836858208bb82157d67e036a block=evidence -->
- Core includes vendor-agnostic transcript types, per-vendor adapters, a session-channel pub/sub multiplexer, session-manager orchestration, and an activity-index that owns all ~/.crispy/ disk I/O. [@claim:clm_1fe536f25a0b7092a6525ac18efa25a95d3e4d94476ba8d06bf0059dc35a3656]
- The webview talks to the host over a JSON-RPC protocol via a SessionService interface with dual transports: VS Code postMessage and WebSocket. [@claim:clm_469016ba51996fb2c16681be17455b1021d7294a7af2cb5bcee7da2cf0f3d981]
- An approval system routes three approval types: standard tool-use option buttons, multi-question AskUser forms, and plan-review (ExitPlan) approvals resolved via transport.resolveApproval. [@claim:clm_5369ae7e775d7b7c0fa58e4d30e417480f256a0f42cbce32193a58ebf821e162]
- Per the architecture doc, only the Claude adapter is wired up today, and the roadmap lists Gemini CLI and OpenCode support as coming soon. [@claim:clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497]
- The standalone dev/standalone server listens on HTTP + WebSocket at port 3456 and serves the static webview bundle, auto-registering the Claude adapter at startup. [@claim:clm_78a23726e10d5758a231084fe7e0a58db96d0a0bd355375d3be4185f3ab9152b]
- Core is written in a functional style: free functions with module-level state rather than classes, and the webview derives all state client-side from channel events with no direct file I/O. [@claim:clm_8189e45d703dd865bbfce150d0a7e69c39a93e21427942b050bf84c69e1fbf8e]
- The webview uses React 19 with esbuild and vanilla CSS using VS Code theme variables, with a two-column layout of sidebar plus transcript viewer. [@claim:clm_ac4a116f5472617a4e75f926cc71976339a62cb1945c37c1d8be3d922c5ad074]
- SessionService method groups cover session lifecycle (list/load/create/fork/close), agent control (send, interrupt, setModel, setPermissions), approvals, subscriptions, and file operations. [@claim:clm_e2417184d61fc7c3e5646734dd3dac3b63c3739dd6de99fd231ffbd82090fd47]
- The codebase is organized into three layers: core (src/core/) owning state and logic, host (src/host/) as a thin RPC router, and webview (src/webview/) for UI. [@claim:clm_ea0709eb341359ebc0cabb856a5ecc98e85f082d2fb3f84f18a4333a37956516]
<!-- rcw:end owner=source:src_fb5fb91a836858208bb82157d67e036a block=evidence -->

## Researcher notes

