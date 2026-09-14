# traycerai/traycer

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b12949767727 @ 6d5e53e24e3c3dec

## Summary (orientation draft, not independently verified)

Traycer is described as an AI orchestration app that runs multiple agents in parallel while sharing memory across all models and providers. The product supports agent-to-agent communication, letting users create automated loops where agents debate architecture or peer-review each other's code.

## Source coverage

Source coverage (partial): 3 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The context window is shared across providers, so users can switch models within the same agent without losing context. -- evidence: [README.md#L22-L22](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L22-L22), [README.md#L28-L32](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L28-L32)
  - [observation/documented] Agent-to-agent abilities such as reading a transcript or delivering a message are narrower and depend on the user, Host, and runtime, per a capability matrix. -- evidence: [README.md#L28-L32](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L28-L32)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use Bun 1.3.12 workspaces with Nx, run build/compile/lint/format via bun scripts, and commits require DCO sign-off; tests run in CI, not pre-commit hooks. -- evidence: [AGENTS.md#L42-L46](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L42-L46), [AGENTS.md#L3-L3](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L3-L3), [AGENTS.md#L26-L33](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L26-L33)
  - [observation/documented] Repository development practice: commits must not manually run compile/build/lint/format beforehand because pre-commit runs affected workspace checks, and make dev-desktop targets the production cloud with no local backends. -- evidence: [AGENTS.md#L42-L46](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L42-L46), [AGENTS.md#L39-L40](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L39-L40)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] An agent is a durable session inside a Task that the user interacts with through a Chat or Terminal interface, powered by an underlying coding-agent provider. -- evidence: [README.md#L49-L49](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L49-L49)
  - [observation/documented] Desktop builds are distributed for macOS (arm64 and x64 .dmg), Linux (AppImage, .deb, .rpm), and Windows x64 .exe via GitHub Releases. -- evidence: [README.md#L36-L43](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L36-L43)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Traycer is described as an AI orchestration app that runs multiple agents in parallel while sharing memory across all models and providers. -- evidence: [README.md#L20-L20](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L20-L20)
  - [observation/documented] The product supports agent-to-agent communication, letting users create automated loops where agents debate architecture or peer-review each other's code. -- evidence: [README.md#L28-L32](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L28-L32)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Supported coding agents listed as fully supported are Claude Code, Codex, Cursor, and OpenCode, plus Traycer's own native inference subscription. -- evidence: [README.md#L51-L57](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L51-L57)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](traycer.detail.md)

Metadata and full claim list: [full detail](traycer.detail.md)
Human notes ([notes](traycer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
