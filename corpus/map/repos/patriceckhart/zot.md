# patriceckhart/zot

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f60e492e5518 @ 17a5430f57315354

## Summary (orientation draft, not independently verified)

README evidence describes zot, a Go-based coding agent harness distributed as a static binary with many built-in providers, built-in tools, multiple run modes, session management, swarm subagents, and a jail sandbox guardrail. No contributor-workflow or evaluation evidence appears in the provided slices. Evidence coverage: 101 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] zot is a coding agent harness written in Go and distributed as a single static binary. -- evidence: [README.md#L18-L18](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L18-L18), [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29)
- design-choices (3 claim(s)):
  - [observation/documented] Extensions run in any language via subprocess plus JSON-RPC, none installed by default, opted into with `zot ext install` or `zot --ext`; themes are user and extension JSON files. -- evidence: [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29)
  - [observation/documented] API keys can be fetched from a password manager via an api_key_command executed directly without a shell; output is cached in memory only, never written to disk, and capped at 64 KiB. -- evidence: [README.md#L106-L106](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L106-L106), [README.md#L108-L108](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L108-L108), [README.md#L92-L92](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L92-L92)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] Standing instructions come from AGENTS.md files (global plus root-to-cwd chain, deeper files overriding), while reusable instructions use SKILL.md files; SYSTEM.md replaces the built-in identity and --system-prompt wins per invocation. -- evidence: [README.md#L167-L167](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L167-L167), [README.md#L171-L172](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L171-L172), [README.md#L151-L151](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L151-L151), [README.md#L184-L190](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L184-L190), [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29)
  - [observation/documented] zot does not read CLAUDE.md; the only Claude-compatible input is skills under .claude/skills/, and migrating users are told to move content into AGENTS.md. -- evidence: [README.md#L192-L192](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L192-L192)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports interactive TUI, print, stream, piped-input, and JSON modes, plus an `zot rpc` long-lived subprocess speaking newline-delimited JSON for embedding in other applications. -- evidence: [README.md#L296-L297](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L296-L297), [README.md#L200-L212](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L200-L212), [README.md#L272-L277](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L272-L277)
  - [observation/documented] A Go SDK is offered via the packages/agent/sdk import, where a Runtime per project exposes Prompt(ctx, text, images) returning a channel of events; both embedding paths share one event schema. -- evidence: [README.md#L296-L297](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L296-L297), [README.md#L299-L299](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L299-L299)
- memory-state (3 claim(s)):
  - [observation/documented] All data lives under $ZOT_HOME, including config.json, auth.json (mode 0600), per-cwd JSONL session transcripts, a 6h-TTL models cache, skills, themes, extensions, and logs. -- evidence: [README.md#L84-L88](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L84-L88), [README.md#L137-L149](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L137-L149)
  - [observation/documented] Sessions are JSONL transcripts resumable via --continue, --resume, --session, or /sessions; empty sessions are deleted on close, and `zot sessions prune` can remove sessions for vanished directories or by age. -- evidence: [README.md#L465-L465](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L465-L465), [README.md#L467-L467](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L467-L467), [README.md#L463-L463](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L463-L463)
- orchestration (2 claim(s)):
More evidence: [full detail](zot.detail.md)

Metadata and full claim list: [full detail](zot.detail.md)
Human notes ([notes](zot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
