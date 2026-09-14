# r1n7aro/locus

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 52e714341f53 @ 4404142f5255491b

## Summary (orientation draft, not independently verified)

Locus for Unity is an open-source AI agent for Unity projects, shipped as a standalone Rust+Tauri+Vue.js desktop application with Roslyn-based analysis, C# hot reload, a knowledge/memory system, and a documented tool-permission model. Evidence covers product capabilities, the permission system, platform/compatibility limits, and contributor build/run workflows.

## Source coverage

Source coverage (partial): 6 of 95 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Locus for Unity is described as an open-source AI Agent for Unity projects, currently in early testing with feedback welcomed via Issues. -- evidence: [README.md#L19-L19](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L19-L19), [README.md#L30-L30](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L30-L30)
  - [observation/documented] Locus currently supports Unity 2021 or later on Windows, and compatibility fixes for older versions may be handled as branch-specific solutions. -- evidence: [README.md#L59-L59](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L59-L59), [README.md#L57-L57](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L57-L57)
- components (2 claim(s)):
  - [observation/documented] The product is a standalone Rust + Tauri + Vue.js application that runs as an independent process rather than inside the Unity Editor or as an MCP server. -- evidence: [README.md#L34-L34](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L34-L34), [README.md#L47-L47](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L47-L47)
  - [observation/documented] Built-in Roslyn semantic analysis runs in Locus's own process, providing go-to-definition, find-references, hover info, and live compiler-grade diagnostics without waiting for Unity to compile. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45)
- design-choices (2 claim(s)):
  - [observation/documented] Locus uses a proprietary intermediate representation so agents can progressively read large scenes and assets, paired with retrieval tools to quickly locate target objects. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45)
  - [observation/documented] C# changes apply via built-in hot reload without recompiling the assembly or domain reload, preserving Play Mode state, and the agent can immediately confirm whether a change landed. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45), [README.md#L21-L28](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L21-L28)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the repo uses bun + Tauri 2 with Windows as the primary platform; `bun tauri dev` starts a Vite dev server and opens the Tauri desktop app. -- evidence: [README.md#L67-L69](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L67-L69), [README.md#L71-L71](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L71-L71), [README.md#L63-L63](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L63-L63)
  - [observation/documented] Repository development practice: `bun run locus:test:app` launches an isolated test instance with separate database, config, logs, workspace, WebView2 profile, and temp directories, printing LOCUS_RUNTIME_JSON at startup. -- evidence: [README.md#L79-L79](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L79-L79), [README.md#L75-L77](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L75-L77)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The /view command lets the agent build Unity editor interfaces with Vue.js, free of IMGUI constraints, with data binding and interpreted C# execution. -- evidence: [README.zh-CN.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.zh-CN.md#L36-L45), [README.md#L21-L28](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L21-L28)
- memory-state (1 claim(s)):
  - [observation/documented] An automated knowledge system summarizes conversation requirements into design documents and preserves project understanding in long-term memory. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45), [README.md#L21-L28](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L21-L28)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (4 claim(s)):
More evidence: [full detail](locus.detail.md)

Metadata and full claim list: [full detail](locus.detail.md)
Human notes ([notes](locus.notes.md), never overwritten by build)

[Back to map index](../../index.md)
