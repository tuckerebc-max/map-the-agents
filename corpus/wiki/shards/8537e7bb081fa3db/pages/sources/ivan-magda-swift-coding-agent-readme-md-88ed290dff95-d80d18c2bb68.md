---
access: public
aliases: []
claim_ids:
- clm_0559886f40371a94cc44038d98afcf1d5526e595ac5604ee00dd42030966ae81
- clm_573f0405798151bd993c21f5aa24d5deb4759da65039fad1081e0ec518841e03
- clm_7447858dcbdcaaab82e209d5632265ba932ebf12cde85ecddd1a98d0ed5276e5
- clm_77541a28832fe82155a6c0d3835a0406919afbc5387de7db5e727a5039f04db3
- clm_b345c5f2e5bf97a35f9c545bfff0620a6c7a5adeeecd3abe1a672b519bb6b281
- clm_b7841256fffa30db1bd6bcb091df7255cd1d760c01aeba69c1c2f0ca2f83c4f7
- clm_fcfa9bdf7269b6fa9e851458f14f25b152fa49487509ccfce62586eeaf5e7e2d
maturity: draft
page_id: pg_a8f58d1422e7588dae5fd80d18c2bb68
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c09e10ca46a8511fb4e20457226b4654
title: ivan-magda/swift-coding-agent/README.md @ 88ed290dff95
updated_at: '2026-09-14T02:06:02Z'
---

# ivan-magda/swift-coding-agent/README.md @ 88ed290dff95

<!-- rcw:begin owner=source:src_c09e10ca46a8511fb4e20457226b4654 block=evidence -->
- The README states the project is explicitly not a full Claude Code clone, a general-purpose multi-agent framework, or production-ready IDE tooling; the gaps are deliberate. [@claim:clm_0559886f40371a94cc44038d98afcf1d5526e595ac5604ee00dd42030966ae81]
- The loop body is invariant across stages; each stage only adds tool handler entries and injection points before the API call, with tools varying while the loop stays identical. [@claim:clm_573f0405798151bd993c21f5aa24d5deb4759da65039fad1081e0ec518841e03]
- The package depends on AsyncHTTPClient (from 1.32.0, SwiftNIO-based) rather than URLSession for cross-platform macOS/Linux HTTP and streaming SSE, built with Swift 6.2 strict concurrency. [@claim:clm_7447858dcbdcaaab82e209d5632265ba932ebf12cde85ecddd1a98d0ed5276e5]
- The agent runs a fixed while-true loop: append the user query, call the Anthropic API, and if the stop reason is tool use, execute tools and append results as a user message; otherwise return the text content. [@claim:clm_77541a28832fe82155a6c0d3835a0406919afbc5387de7db5e727a5039f04db3]
- It is a two-target Swift Package Manager project: a Core library holding the API client, shell executor, agent loop, and tools, plus a thin CLI entry point. [@claim:clm_b345c5f2e5bf97a35f9c545bfff0620a6c7a5adeeecd3abe1a672b519bb6b281]
- The project's thesis is that coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers, deliberately rebuilding Claude Code's restrained design in Swift. [@claim:clm_b7841256fffa30db1bd6bcb091df7255cd1d760c01aeba69c1c2f0ca2f83c4f7]
- The agent communicates with POST https://api.anthropic.com/v1/messages over raw HTTP built on AsyncHTTPClient, and the CLI executable is named `agent`. [@claim:clm_fcfa9bdf7269b6fa9e851458f14f25b152fa49487509ccfce62586eeaf5e7e2d]
<!-- rcw:end owner=source:src_c09e10ca46a8511fb4e20457226b4654 block=evidence -->

## Researcher notes

