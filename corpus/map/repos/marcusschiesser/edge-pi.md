# marcusschiesser/edge-pi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c4b694c4abb1 @ ec984f0805a83ae0

## Summary (orientation draft, not independently verified)

Edge-Pi is a Vercel AI SDK-based coding agent SDK plus an `epi` CLI proof-of-concept, with documented architecture spanning model factories, tools, sessions, and compaction. Most other evidence covers contributor workflows (AGENTS.md, CONTRIBUTING.md).

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] Edge-Pi is a lightweight coding agent library built on the Vercel AI SDK, providing primitives for tool support, session management, and context compaction. -- evidence: [README.md#L3-L3](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L3-L3), [README.md#L5-L5](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L5-L5)
  - [observation/documented] The project positions itself as an open replacement for Anthropic's proprietary Claude Agent SDK, working with any LLM provider via the Vercel AI SDK. -- evidence: [README.md#L5-L5](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] The edge-pi core package contains CodingAgent, Tool Factory with tools, SessionManager, Compaction, and a runtime abstraction, per the architecture diagram. -- evidence: [architecture.md#L14-L20](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L14-L20)
  - [observation/documented] The edge-pi-cli package handles CLI args and modes, a model factory, auth storage/OAuth, and settings, skills, prompts, and context. -- evidence: [architecture.md#L7-L12](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L7-L12)
- design-choices (2 claim(s)):
  - [observation/documented] The runtime abstraction connects tools to a local filesystem/shell environment, with optional WebContainer and Vercel Sandbox execution environments. -- evidence: [architecture.md#L30-L35](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L30-L35), [architecture.md#L48-L57](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L48-L57)
  - [observation/documented] The codebase is based on the pi coding agent by Mario Zechner, and the SDK is intentionally minimal with features that don't belong there directed to the CLI. -- evidence: [CONTRIBUTING.md#L38-L38](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L38-L38), [README.md#L9-L9](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L9-L9)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md forbids running `npm run dev`, `npm run build`, or `npm test`, requires `npm run check` after code changes, and forbids committing unless the user asks. -- evidence: [AGENTS.md#L23-L28](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L23-L28)
  - [observation/documented] Repository development practice: first-time contributors must open an issue and receive a maintainer `lgtm` approval before submitting PRs, a gate intended to filter low-quality AI-generated contributions. -- evidence: [CONTRIBUTING.md#L15-L15](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L15-L15), [CONTRIBUTING.md#L23-L23](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L23-L23), [CONTRIBUTING.md#L17-L21](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L17-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI is installed globally via `npm install -g edge-pi-cli` and run with the `epi` command, with `epi --help` for more information. -- evidence: [README.md#L31-L33](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L31-L33), [README.md#L19-L21](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L19-L21), [README.md#L25-L27](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L25-L27)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are persisted as JSONL files, and a changelog entry says SessionManager is integrated with CodingAgent so history is auto-restored and persisted during generate() and stream(). -- evidence: [docs/CHANGELOG.md#L7-L7](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/docs/CHANGELOG.md#L7-L7), [architecture.md#L30-L35](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L30-L35), [architecture.md#L48-L57](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L48-L57)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](edge-pi.detail.md)

Metadata and full claim list: [full detail](edge-pi.detail.md)
Human notes ([notes](edge-pi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
