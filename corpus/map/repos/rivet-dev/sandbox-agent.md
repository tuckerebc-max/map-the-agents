# rivet-dev/sandbox-agent

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bbc195cc3fb5 @ 56989d83a6914f57

## Summary (orientation draft, not independently verified)

Sandbox Agent is a Rust server that runs inside sandboxes and exposes a universal HTTP/SSE API for controlling coding agents (Claude Code, Codex, OpenCode, Cursor, Amp, Pi), with a TypeScript SDK, CLI, and Inspector UI. Evidence is mostly README product documentation plus contributor instructions in CLAUDE.md.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project comprises a Rust daemon ('sandbox-agent server') exposing HTTP+SSE, a TypeScript SDK with embedded and server modes, a built-in Inspector UI, and a CLI mirroring the HTTP endpoints. -- evidence: [README.md#L53-L58](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L53-L58)
- design-choices (1 claim(s)):
  - [observation/documented] The server is implemented as a single static Rust binary, chosen for fast startup and predictable memory usage so it can run in sandboxes or CI without a Node.js runtime. -- evidence: [README.md#L33-L38](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L33-L38), [README.md#L254-L255](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L254-L255)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md instructs contributors to keep CLI subcommands and HTTP endpoints in sync, update docs/cli.mdx on CLI changes, and regenerate docs/openapi.json when HTTP contracts change. -- evidence: [CLAUDE.md#L31-L38](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/CLAUDE.md#L31-L38)
  - [observation/documented] Repository development practice: contributors must keep three files in sync (common-software docs, a Dockerfile, and a Rust test file) and can verify with 'cargo test -p sandbox-agent --test common_software'. -- evidence: [CLAUDE.md#L47-L52](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/CLAUDE.md#L47-L52)
- skills-patterns (1 claim(s)):
  - [observation/documented] A skill for the product can be installed via 'npx skills add rivet-dev/skills -s sandbox-agent' or the bunx equivalent. -- evidence: [README.md#L72-L74](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L72-L74), [README.md#L68-L70](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L68-L70)
- interfaces (5 claim(s)):
  - [observation/documented] The product exposes a single HTTP API with SSE streaming that normalizes different coding agents' proprietary APIs, so integrations can swap agents via configuration rather than code changes. -- evidence: [README.md#L27-L27](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L27-L27), [README.md#L25-L25](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L25-L25)
  - [observation/documented] The TypeScript SDK supports embedded mode via SandboxAgent.start() and remote server mode via SandboxAgent.connect() with a baseUrl and token, and offers methods like listAgents, createSession, postMessage, and streamEvents. -- evidence: [README.md#L107-L111](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L107-L111), [README.md#L115-L116](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L115-L116), [README.md#L118-L121](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L118-L121), [README.md#L123-L123](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L123-L123), [README.md#L99-L100](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L99-L100), [README.md#L125-L128](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L125-L128)
- memory-state (1 claim(s)):
  - [observation/documented] The SDK does not persist session data itself; events stream in a universal JSON schema that consumers are expected to store externally, e.g. in Postgres, ClickHouse, or Rivet. -- evidence: [README.md#L29-L29](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L29-L29), [README.md#L230-L231](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L230-L231)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](sandbox-agent.detail.md)

Metadata and full claim list: [full detail](sandbox-agent.detail.md)
Human notes ([notes](sandbox-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
