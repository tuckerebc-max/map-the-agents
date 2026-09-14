# tndata/codingagentexplorer

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e70b2cc5213e @ b9b610683b980106

## Summary (orientation draft, not independently verified)

The dashboard exposes three views: HTTP Inspector (table of proxied requests with headers, bodies, SSE events, timing), Conversation View (chat-style timeline), and MCP Observer. The tool runs four localhost endpoints: reverse proxy on 8888, MCP proxy on 9999, and dashboard on 5000 (HTTP) and 5001 (HTTPS, auto-launching a browser on Windows).

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] HookAgent is a companion CLI used as a Claude Code hook command: it reads a JSON payload from stdin, collects Claude environment variables, POSTs to the dashboard's /api/hook-event endpoint, and relays exitCode/stdout/stderr back. -- evidence: [README.md#L210-L214](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L210-L214), [README.md#L200-L200](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L200-L200)
  - [observation/documented] HookAgent exits silently with code 0 when the dashboard is not running, so it never blocks Claude Code. -- evidence: [README.md#L262-L262](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L262-L262), [README.md#L210-L214](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L210-L214)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture uses ASP.NET Core with YARP reverse proxy, SignalR for real-time dashboard updates, a vanilla HTML/JS/CSS frontend with no build step, and a single NuGet dependency (Yarp.ReverseProxy). -- evidence: [README.md#L298-L301](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L298-L301)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: build and run with 'dotnet build' then 'dotnet run --project CodingAgentExplorer'; publish via publish.bat (Windows) or bash publish.sh (macOS/Linux) into a gitignored Published/ directory. -- evidence: [README.md#L67-L70](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L67-L70), [README.md#L176-L179](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L176-L179), [README.md#L174-L174](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L174-L174), [README.md#L186-L189](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L186-L189)
  - [observation/documented] Repository development practice: CLAUDE.md imposes a writing style rule for documentation, forbidding em dashes and dashes as sentence separators in README.md and other docs. -- evidence: [CLAUDE.md#L82-L83](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/CLAUDE.md#L82-L83)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The dashboard exposes three views: HTTP Inspector (table of proxied requests with headers, bodies, SSE events, timing), Conversation View (chat-style timeline), and MCP Observer. -- evidence: [README.md#L18-L18](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L18-L18), [README.md#L120-L122](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L120-L122)
  - [observation/documented] The tool runs four localhost endpoints: reverse proxy on 8888, MCP proxy on 9999, and dashboard on 5000 (HTTP) and 5001 (HTTPS, auto-launching a browser on Windows). -- evidence: [README.md#L116-L116](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L116-L116), [README.md#L72-L76](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L72-L76)
- memory-state (1 claim(s)):
  - [observation/documented] Captured data is held in memory only: a circular buffer capped at 1000 requests for API traffic, plus in-memory stores for hook events and MCP requests (max 500), with no persistence. -- evidence: [CLAUDE.md#L60-L73](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/CLAUDE.md#L60-L73), [README.md#L331-L333](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L331-L333)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] API keys in x-api-key and Authorization headers are automatically redacted from stored request data, and the proxy listens only on localhost. -- evidence: [README.md#L331-L333](https://github.com/tndata/CodingAgentExplorer/blob/e70b2cc5213e063f15d404e482920a49d9edd7df/README.md#L331-L333)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](codingagentexplorer.detail.md)

Metadata and full claim list: [full detail](codingagentexplorer.detail.md)
Human notes ([notes](codingagentexplorer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
