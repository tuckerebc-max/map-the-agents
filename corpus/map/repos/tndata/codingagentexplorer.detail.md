# tndata/codingagentexplorer -- full detail

[Back to orientation](codingagentexplorer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tndata/codingagentexplorer/e70b2cc5213e063f15d404e482920a49d9edd7df/b9b610683b980106.json](../../../wiki/dossiers/tndata/codingagentexplorer/e70b2cc5213e063f15d404e482920a49d9edd7df/b9b610683b980106.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] HookAgent is a companion CLI used as a Claude Code hook command: it reads a JSON payload from stdin, collects Claude environment variables, POSTs to the dashboard's /api/hook-event endpoint, and relays exitCode/stdout/stderr back. -- evidence: [README.md#L210-L214](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L210-L214), [README.md#L200-L200](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L200-L200) (`clm_15f3990fb8a930384735f5d4d8363949fc738965e66188bcdcd3a1139c862b60`)
- [observation/documented] HookAgent exits silently with code 0 when the dashboard is not running, so it never blocks Claude Code. -- evidence: [README.md#L262-L262](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L262-L262), [README.md#L210-L214](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L210-L214) (`clm_5a4ce8633bf5bfc9a61c36f2a8c0f2c83863e985fe33fd316642463746a6db43`)
- [observation/documented] The MCP Observer acts as a transparent proxy on port 9999 between Claude Code and any HTTP-based MCP server, with the destination URL configured at runtime via a dashboard page. -- evidence: [README.md#L151-L151](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L151-L151), [CLAUDE.md#L48-L48](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/CLAUDE.md#L48-L48), [README.md#L126-L126](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L126-L126) (`clm_2f36d62d4ed3c19aed46cee8d8374062e6431f183eff730991124ce7a7601a91`)

## design-choices (1 claim(s))

- [observation/documented] The architecture uses ASP.NET Core with YARP reverse proxy, SignalR for real-time dashboard updates, a vanilla HTML/JS/CSS frontend with no build step, and a single NuGet dependency (Yarp.ReverseProxy). -- evidence: [README.md#L298-L301](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L298-L301) (`clm_e657275eb07badb388230cec2064cbfadacf50c477151585e467255fc5ce2fe6`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: build and run with 'dotnet build' then 'dotnet run --project CodingAgentExplorer'; publish via publish.bat (Windows) or bash publish.sh (macOS/Linux) into a gitignored Published/ directory. -- evidence: [README.md#L67-L70](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L67-L70), [README.md#L176-L179](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L176-L179), [README.md#L174-L174](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L174-L174), [README.md#L186-L189](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L186-L189) (`clm_112fc3d9ce852c49e1cc2794e4a6a31e0acf5162e45d91509c84e9cd1da42a9f`)
- [observation/documented] Repository development practice: CLAUDE.md imposes a writing style rule for documentation, forbidding em dashes and dashes as sentence separators in README.md and other docs. -- evidence: [CLAUDE.md#L82-L83](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/CLAUDE.md#L82-L83) (`clm_579dec6d2009efef92f3f6c1c09f2945cb56f07b4d608ffca444720fcf2b26cb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The dashboard exposes three views: HTTP Inspector (table of proxied requests with headers, bodies, SSE events, timing), Conversation View (chat-style timeline), and MCP Observer. -- evidence: [README.md#L18-L18](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L18-L18), [README.md#L120-L122](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L120-L122) (`clm_5808aef265d2b075d3a69bf5e5b24db221ad5aa012b83866a7126bebdaed059c`)
- [observation/documented] The tool runs four localhost endpoints: reverse proxy on 8888, MCP proxy on 9999, and dashboard on 5000 (HTTP) and 5001 (HTTPS, auto-launching a browser on Windows). -- evidence: [README.md#L116-L116](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L116-L116), [README.md#L72-L76](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L72-L76) (`clm_cf1f1562b7de53c4cb5ff4fd1726fb60b48f2149d8f9948c543f8f7ebabd49d0`)
- [observation/documented] Claude Code is pointed at the proxy by setting the ANTHROPIC_BASE_URL environment variable to http://localhost:8888; helper scripts enable and disable it per terminal session only. -- evidence: [README.md#L80-L80](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L80-L80), [README.md#L110-L110](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L110-L110), [README.md#L104-L104](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L104-L104) (`clm_08f07587ff2efaa6205faf4a6eb56e79017965b9a2dd3eb6164a92327780b769`)

## memory-state (1 claim(s))

- [observation/documented] Captured data is held in memory only: a circular buffer capped at 1000 requests for API traffic, plus in-memory stores for hook events and MCP requests (max 500), with no persistence. -- evidence: [CLAUDE.md#L60-L73](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/CLAUDE.md#L60-L73), [README.md#L331-L333](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L331-L333) (`clm_791dfcc0cf71e770528e6616582349dae29b4438246c69c6b41b500426f7eafb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] API keys in x-api-key and Authorization headers are automatically redacted from stored request data, and the proxy listens only on localhost. -- evidence: [README.md#L331-L333](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L331-L333) (`clm_c74b8dd5f97bbf4ea2462ba86411efe02d2fabf596d7639f2bb9c77acdc2faf6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project requires the .NET 10 SDK (or later) to build, and published outputs require the .NET 10 runtime on the target machine. -- evidence: [README.md#L50-L50](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L50-L50), [README.md#L196-L196](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L196-L196) (`clm_e7b85008fafe429202bf14cddc449be828a58f162b7b499b869efe51d6bf4b21`)

## limitations (1 claim(s))

- [observation/documented] The tool currently supports Claude Code with the Anthropic API only; support for additional coding agents may be added in the future. -- evidence: [README.md#L359-L359](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L359-L359) (`clm_84c037f3ba48863afadefb13f7bf72a3210b2c482ccac708b0dc52ce06328fd5`)

## relevance (1 claim(s))

- [observation/documented] The project was built as a teaching tool for AI-agent workshops, helping developers understand what happens under the hood when AI coding agents work. -- evidence: [README.md#L353-L353](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L353-L353) (`clm_ae14e7c49873ebf6842aeae4f02799a9b5d72bb8cde7216292918866b2f1d38e`)

