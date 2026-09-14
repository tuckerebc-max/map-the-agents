---
access: public
aliases: []
claim_ids:
- clm_08f07587ff2efaa6205faf4a6eb56e79017965b9a2dd3eb6164a92327780b769
- clm_112fc3d9ce852c49e1cc2794e4a6a31e0acf5162e45d91509c84e9cd1da42a9f
- clm_15f3990fb8a930384735f5d4d8363949fc738965e66188bcdcd3a1139c862b60
- clm_2f36d62d4ed3c19aed46cee8d8374062e6431f183eff730991124ce7a7601a91
- clm_5808aef265d2b075d3a69bf5e5b24db221ad5aa012b83866a7126bebdaed059c
- clm_5a4ce8633bf5bfc9a61c36f2a8c0f2c83863e985fe33fd316642463746a6db43
- clm_791dfcc0cf71e770528e6616582349dae29b4438246c69c6b41b500426f7eafb
- clm_84c037f3ba48863afadefb13f7bf72a3210b2c482ccac708b0dc52ce06328fd5
- clm_ae14e7c49873ebf6842aeae4f02799a9b5d72bb8cde7216292918866b2f1d38e
- clm_c74b8dd5f97bbf4ea2462ba86411efe02d2fabf596d7639f2bb9c77acdc2faf6
- clm_cf1f1562b7de53c4cb5ff4fd1726fb60b48f2149d8f9948c543f8f7ebabd49d0
- clm_e657275eb07badb388230cec2064cbfadacf50c477151585e467255fc5ce2fe6
- clm_e7b85008fafe429202bf14cddc449be828a58f162b7b499b869efe51d6bf4b21
maturity: draft
page_id: pg_6528e2a6326251f6967f52cbbc61efbf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_178c5b380e9453228c8a490ec215927f
title: tndata/CodingAgentExplorer/README.md @ e70b2cc5213e
updated_at: '2026-09-14T04:26:42Z'
---

# tndata/CodingAgentExplorer/README.md @ e70b2cc5213e

<!-- rcw:begin owner=source:src_178c5b380e9453228c8a490ec215927f block=evidence -->
- Claude Code is pointed at the proxy by setting the ANTHROPIC_BASE_URL environment variable to http://localhost:8888; helper scripts enable and disable it per terminal session only. [@claim:clm_08f07587ff2efaa6205faf4a6eb56e79017965b9a2dd3eb6164a92327780b769]
- Repository development practice: build and run with 'dotnet build' then 'dotnet run --project CodingAgentExplorer'; publish via publish.bat (Windows) or bash publish.sh (macOS/Linux) into a gitignored Published/ directory. [@claim:clm_112fc3d9ce852c49e1cc2794e4a6a31e0acf5162e45d91509c84e9cd1da42a9f]
- HookAgent is a companion CLI used as a Claude Code hook command: it reads a JSON payload from stdin, collects Claude environment variables, POSTs to the dashboard's /api/hook-event endpoint, and relays exitCode/stdout/stderr back. [@claim:clm_15f3990fb8a930384735f5d4d8363949fc738965e66188bcdcd3a1139c862b60]
- The MCP Observer acts as a transparent proxy on port 9999 between Claude Code and any HTTP-based MCP server, with the destination URL configured at runtime via a dashboard page. [@claim:clm_2f36d62d4ed3c19aed46cee8d8374062e6431f183eff730991124ce7a7601a91]
- The dashboard exposes three views: HTTP Inspector (table of proxied requests with headers, bodies, SSE events, timing), Conversation View (chat-style timeline), and MCP Observer. [@claim:clm_5808aef265d2b075d3a69bf5e5b24db221ad5aa012b83866a7126bebdaed059c]
- HookAgent exits silently with code 0 when the dashboard is not running, so it never blocks Claude Code. [@claim:clm_5a4ce8633bf5bfc9a61c36f2a8c0f2c83863e985fe33fd316642463746a6db43]
- Captured data is held in memory only: a circular buffer capped at 1000 requests for API traffic, plus in-memory stores for hook events and MCP requests (max 500), with no persistence. [@claim:clm_791dfcc0cf71e770528e6616582349dae29b4438246c69c6b41b500426f7eafb]
- The tool currently supports Claude Code with the Anthropic API only; support for additional coding agents may be added in the future. [@claim:clm_84c037f3ba48863afadefb13f7bf72a3210b2c482ccac708b0dc52ce06328fd5]
- The project was built as a teaching tool for AI-agent workshops, helping developers understand what happens under the hood when AI coding agents work. [@claim:clm_ae14e7c49873ebf6842aeae4f02799a9b5d72bb8cde7216292918866b2f1d38e]
- API keys in x-api-key and Authorization headers are automatically redacted from stored request data, and the proxy listens only on localhost. [@claim:clm_c74b8dd5f97bbf4ea2462ba86411efe02d2fabf596d7639f2bb9c77acdc2faf6]
- The tool runs four localhost endpoints: reverse proxy on 8888, MCP proxy on 9999, and dashboard on 5000 (HTTP) and 5001 (HTTPS, auto-launching a browser on Windows). [@claim:clm_cf1f1562b7de53c4cb5ff4fd1726fb60b48f2149d8f9948c543f8f7ebabd49d0]
- The architecture uses ASP.NET Core with YARP reverse proxy, SignalR for real-time dashboard updates, a vanilla HTML/JS/CSS frontend with no build step, and a single NuGet dependency (Yarp.ReverseProxy). [@claim:clm_e657275eb07badb388230cec2064cbfadacf50c477151585e467255fc5ce2fe6]
- The project requires the .NET 10 SDK (or later) to build, and published outputs require the .NET 10 runtime on the target machine. [@claim:clm_e7b85008fafe429202bf14cddc449be828a58f162b7b499b869efe51d6bf4b21]
<!-- rcw:end owner=source:src_178c5b380e9453228c8a490ec215927f block=evidence -->

## Researcher notes

