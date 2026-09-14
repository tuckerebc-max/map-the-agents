# strands-agents/harness-sdk

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: strands-agents/sdk-python (github id 983715534).
Latest snapshot: commit 08ed4cfd3eb4 @ 2ada8cfbc7de393b

## Summary (orientation draft, not independently verified)

Selected evidence records: Strands Agents is an open-source SDK for building and running AI agents in Python and TypeScript, positioned as a replacement for a hand-rolled agent loop that runs in the user's process with no hosted control plane. The monorepo contains strands-py (Python SDK), strands-ts (TypeScript SDK), site (Astro/Starlight documentation site), and team (governance and cross-SDK process docs including designs/ proposals).

## Source coverage

Source coverage (partial): 8 of 260 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 9 documented, 4 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Strands Agents is an open-source SDK for building and running AI agents in Python and TypeScript, positioned as a replacement for a hand-rolled agent loop that runs in the user's process with no hosted control plane. -- evidence: [README.md#L35-L35](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L35-L35)
- components (2 claim(s)):
  - [observation/documented] The monorepo contains strands-py (Python SDK), strands-ts (TypeScript SDK), site (Astro/Starlight documentation site), and team (governance and cross-SDK process docs including designs/ proposals). -- evidence: [README.md#L37-L37](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L37-L37), [README.md#L39-L44](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L39-L44)
  - [observation/code-inspected] The Python SDK includes an AgentDelegation plugin (auto-registered on every agent) that enforces delegation semantics for tools configured with delegate=True, acting as a no-op when no delegation tools fire. -- evidence: [strands-py/src/strands/agent/_agent_delegation.py#L76-L77](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L76-L77), [strands-py/src/strands/agent/_agent_delegation.py#L1-L1](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L1-L1), [strands-py/src/strands/agent/_agent_delegation.py#L73-L74](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L73-L74), [strands-py/src/strands/agent/_agent_delegation.py#L83-L89](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L83-L89)
- design-choices (4 claim(s)):
  - [observation/documented] The SDK advertises built-in lifecycle controls (turn limits, token budgets, cancellation, stop reasons), tools, structured output, MCP, multi-agent patterns, memory, sessions, model portability, streaming, guardrails, tracing, and evals. -- evidence: [README.md#L35-L35](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L35-L35)
  - [observation/code-inspected] Delegation enforces a single-call constraint (a delegation tool must be the only tool called in a turn, otherwise the call is cancelled or an error result is returned), and the agent loop exits via end_turn after a successful delegation whose content becomes the final assistant message. -- evidence: [strands-py/src/strands/agent/_agent_delegation.py#L5-L9](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L5-L9), [strands-py/src/strands/agent/_agent_delegation.py#L217-L217](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L217-L217), [strands-py/src/strands/agent/_agent_delegation.py#L245-L263](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L245-L263), [strands-py/src/strands/agent/_agent_delegation.py#L133-L139](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L133-L139)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: Python SDK tests and formatting run via hatch test and hatch fmt in strands-py; the TypeScript SDK uses npm ci, npm run build, and npm test; the docs site runs with npm install and npm run dev in site/; git operations are done from the repo root. -- evidence: [README.md#L112-L112](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L112-L112), [README.md#L129-L134](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L129-L134), [README.md#L114-L120](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L114-L120), [README.md#L122-L127](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L122-L127)
  - [observation/documented] Repository development practice: contributions are guided by CONTRIBUTING.md covering bug reports, development setup, pull requests, code of conduct, and security issue reporting; doc PRs are welcome alongside code changes. -- evidence: [README.md#L108-L108](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L108-L108), [README.md#L138-L143](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L138-L143)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
More evidence: [full detail](harness-sdk.detail.md)

Metadata and full claim list: [full detail](harness-sdk.detail.md)
Human notes ([notes](harness-sdk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
