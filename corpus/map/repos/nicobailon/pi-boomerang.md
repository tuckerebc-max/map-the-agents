# nicobailon/pi-boomerang

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1a5985b2d92c @ f61ed095535cf80d

## Summary (orientation draft, not independently verified)

pi-boomerang is a pi coding agent extension that runs tasks autonomously and replaces raw turn history with an expanded handoff summary to save tokens. Evidence covers its commands, chaining/rethrow modes, templates, agent-callable tool, and documented limitations.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] After completion, raw turn history is replaced in future context by an expanded handoff summary containing outcome, changed files, relevant reads, validation commands, failures, and config metadata. -- evidence: [CHANGELOG.md#L62-L63](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/CHANGELOG.md#L62-L63), [README.md#L71-L71](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L71-L71), [README.md#L13-L13](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L13-L13)
  - [observation/documented] The session tree preserves full history for `/tree` navigation, so only future context is collapsed while the underlying history remains accessible. -- evidence: [README.md#L39-L39](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L39-L39), [README.md#L41-L41](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L41-L41)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The extension exposes a `/boomerang <task>` command that executes a task autonomously and summarizes context afterward, plus `/boomerang-cancel` to abort without summarizing. -- evidence: [README.md#L68-L69](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L68-L69), [README.md#L211-L226](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L211-L226), [README.md#L9-L11](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L9-L11), [README.md#L13-L13](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L13-L13)
  - [observation/documented] Chained templates can be run in sequence (e.g. `/boomerang /scout -> /planner -> /impl`) with per-step inline args, global fallback args after `--`, and a single summary return at the end. -- evidence: [README.md#L81-L81](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L81-L81), [README.md#L75-L75](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L75-L75), [README.md#L83-L85](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L83-L85), [README.md#L77-L79](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L77-L79), [README.md#L61-L61](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L61-L61)
- memory-state (1 claim(s)):
  - [observation/documented] Tool state and guidance persist to `~/.pi/agent/boomerang.json` across restarts, while anchor state is in-memory only and clears on session start or switch. -- evidence: [README.md#L205-L205](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L205-L205), [README.md#L244-L247](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L244-L247)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] An optional agent-callable `boomerang` tool supports task mode (queued autonomous execution) and anchor mode (toggle a summary point); it is disabled by default and enabled via `/boomerang tool on`. -- evidence: [README.md#L188-L188](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L188-L188), [README.md#L190-L190](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L190-L190), [README.md#L192-L192](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L192-L192), [README.md#L180-L180](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L180-L180), [README.md#L178-L178](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L178-L178), [README.md#L194-L196](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L194-L196)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] Documented limitations: summaries are heuristic and may miss semantic details, the agent may still ask questions, anchor state is in-memory only, and tool-initiated summaries may lag in the UI until `/reload`. -- evidence: [README.md#L207-L207](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L207-L207), [README.md#L244-L247](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L244-L247)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](pi-boomerang.detail.md) for every claim.)

Metadata and full claim list: [full detail](pi-boomerang.detail.md)
Human notes ([notes](pi-boomerang.notes.md), never overwritten by build)

[Back to map index](../../index.md)
