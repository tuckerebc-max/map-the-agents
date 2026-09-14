# vasihemanth/tokentelemetry

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0d691ae343ed @ 584cdc952070dd60

## Summary (orientation draft, not independently verified)

TokenTelemetry is a free, open-source, 100% local observability dashboard tracking token usage, LLM costs, tool calls, session traces, and reasoning steps across AI coding agents, with no signup or cloud. The project structure includes a Python FastAPI backend that reads agent logs and serves a REST API, a Next.js 16 React frontend dashboard, a cross-platform bin/cli.js launcher, and install.sh/install.ps1 installers. Evidence coverage: 148 of 202 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 30 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] TokenTelemetry is a free, open-source, 100% local observability dashboard tracking token usage, LLM costs, tool calls, session traces, and reasoning steps across AI coding agents, with no signup or cloud. -- evidence: [README.md#L5-L5](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L5-L5), [README.md#L15-L15](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L15-L15)
- components (1 claim(s)):
  - [observation/documented] The project structure includes a Python FastAPI backend that reads agent logs and serves a REST API, a Next.js 16 React frontend dashboard, a cross-platform bin/cli.js launcher, and install.sh/install.ps1 installers. -- evidence: [README.md#L335-L342](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L335-L342)
- design-choices (2 claim(s)):
  - [observation/documented] Budgets are observational by design: TokenTelemetry tracks spend against user-set limits and alerts at 80% and 100% thresholds but never blocks an agent. -- evidence: [README.md#L173-L173](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L173-L173), [README.md#L111-L123](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L111-L123)
  - [observation/documented] Plan-limit readings come from the provider's own login data on the machine rather than being estimated from history, and the UI distinguishes provider plan ceilings from user-defined project budgets. -- evidence: [README.md#L181-L181](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L181-L181), [README.md#L179-L179](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L179-L179), [README.md#L183-L183](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L183-L183)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions follow a branch-and-PR flow (feat/ branches, conventional commit messages), and ADR-0001 requires an architecture decision record in docs/adr/ committed in the same PR as the code it describes. -- evidence: [README.md#L436-L436](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L436-L436), [README.md#L442-L444](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L442-L444), [docs/adr/0001-record-architecture-decisions.md#L38-L44](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0001-record-architecture-decisions.md#L38-L44), [docs/adr/0001-record-architecture-decisions.md#L19-L23](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0001-record-architecture-decisions.md#L19-L23)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Remote access is opt-in: --host 0.0.0.0 exposes the backend, a random auth token is auto-generated and printed once unless --auth-token or --insecure-no-auth is passed, and loopback clients never need the token. -- evidence: [README.md#L297-L301](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L297-L301), [README.md#L285-L285](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L285-L285)
  - [observation/documented] The Hermes dashboard plugin embeds TokenTelemetry as a tab inside Hermes's own web dashboard (port 9119 to 3000), is pure-frontend with no extra backend, and deep-links to Analytics, Projects, and All Agents pages. -- evidence: [README.md#L89-L89](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L89-L89), [README.md#L105-L105](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L105-L105)
- memory-state (2 claim(s)):
  - [observation/documented] State lives in ~/.tokentelemetry/ as hand-editable JSON files (aliases, hidden projects, preferences, billing, power, VERSION), with no database; a data directory can be relocated via --data-dir or TOKENTELEMETRY_DATA_DIR. -- evidence: [README.md#L218-L226](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L218-L226), [README.md#L243-L245](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L243-L245), [README.md#L235-L239](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L235-L239), [README.md#L216-L216](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L216-L216), [README.md#L228-L228](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L228-L228)
More evidence: [full detail](tokentelemetry.detail.md)

Metadata and full claim list: [full detail](tokentelemetry.detail.md)
Human notes ([notes](tokentelemetry.notes.md), never overwritten by build)

[Back to map index](../../index.md)
