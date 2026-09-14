# legioncodeinc/honeycomb

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c1cb6bf5674c @ c3ac5449590e9e74

## Summary (orientation draft, not independently verified)

README and BUILD.md describe Honeycomb, a local-daemon shared-memory system for AI coding agents built on Activeloop Deeplake, with a CLI, MCP server, SDK, and dashboard; contributor docs cover build tiers, CLA, and release automation. Evidence coverage: 135 of 181 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Honeycomb provides shared, persistent memory for AI coding agents: what one harness learns is recallable by others across sessions, tools, devices, and teammates. -- evidence: [README.md#L12-L15](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L12-L15), [README.md#L56-L56](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L56-L56)
- components (1 claim(s)):
  - [observation/documented] The product is a long-lived local daemon plus thin clients (hooks, CLI, MCP, SDK); the daemon is the sole process talking to storage, reached over loopback HTTP on 127.0.0.1:3850. -- evidence: [README.md#L212-L223](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L212-L223), [README.md#L210-L210](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L210-L210)
- design-choices (2 claim(s)):
  - [observation/documented] At session start a bounded index of roughly 300-800 tokens of relevant keys is pushed once, with deeper detail pulled on demand rather than injected per turn. -- evidence: [README.md#L91-L97](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L91-L97)
  - [observation/documented] The daemon binds loopback only (single machine); cross-device and cross-user sharing happen through Deeplake's org/workspace scope rather than a remote daemon bind. -- evidence: [README.md#L290-L293](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L290-L293)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: npm run ci is the quality gate every change must pass, combining typecheck, duplication detection (jscpd), vitest tests, and a SQL-safety audit. -- evidence: [README.md#L307-L307](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L307-L307), [README.md#L301-L305](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L301-L305)
  - [observation/documented] Repository development practice: the codebase is a single-package TypeScript monorepo with tiered import direction (tier N may import only from lower tiers), DeepLake access confined to src/daemon, and esbuild bundling per target entry root. -- evidence: [BUILD.md#L21-L27](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L21-L27), [BUILD.md#L29-L32](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L29-L32), [BUILD.md#L17-L19](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L17-L19), [BUILD.md#L3-L6](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L3-L6)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A unified honeycomb CLI exposes verbs such as setup, status, login, start/stop, remember, recall, sessions, and uninstall; baseline operational verbs accept --json with exit codes 2/1/0 for malformed usage, runtime failure, and success. -- evidence: [README.md#L157-L181](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L157-L181), [README.md#L155-L155](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L155-L155), [README.md#L185-L187](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L185-L187)
  - [observation/documented] Besides the CLI, Honeycomb is reachable via the Hive portal dashboard at 127.0.0.1:3853, a bundled MCP server exposing read/resolve and search/mine tools, and a TypeScript SDK with /react, /vercel, and /openai subpath entries. -- evidence: [README.md#L274-L276](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L274-L276), [README.md#L146-L146](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L146-L146)
- memory-state (1 claim(s)):
  - [observation/documented] Memories exist at three tiers: a one-line key, a distilled summary carrying the semantic embedding, and the full raw session dialogue; resolution is a deterministic pointer walk across three Deeplake tables. -- evidence: [README.md#L235-L239](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L235-L239), [README.md#L91-L97](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L91-L97), [README.md#L241-L241](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L241-L241)
More evidence: [full detail](honeycomb.detail.md)

Metadata and full claim list: [full detail](honeycomb.detail.md)
Human notes ([notes](honeycomb.notes.md), never overwritten by build)

[Back to map index](../../index.md)
