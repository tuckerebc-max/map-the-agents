# ohad6k/viberaven

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f64e97730fd5 @ c3cd057bf9b81d82

## Summary (orientation draft, not independently verified)

Evidence is README/CHANGELOG/AGENTS.md only: VibeRaven is an MIT-licensed local CLI/Studio cockpit (viberaven@1.4.2) that scans AI-built apps offline, issues ship verdicts, and connects coding agents via skills, plugin manifests, and MCP. No source code is included in the snapshot, so claims are documentation-based.

## Source coverage

Source coverage (partial): 3 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Provider detection covers Supabase, Vercel, GitHub, Stripe, Sentry, Resend, Clerk, Auth.js, PostHog, and Upstash, rendered as trading-card style cards in the Studio. -- evidence: [README.md#L45-L45](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L45-L45), [README.md#L47-L49](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L47-L49)
  - [observation/documented] The public repo is described as the agent discovery/installation surface, while product source development happens in a private repository; current release is viberaven@1.4.2 (AGENTS.md references 1.4.3). -- evidence: [README.md#L196-L196](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L196-L196), [README.md#L200-L200](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L200-L200), [AGENTS.md#L3-L3](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/AGENTS.md#L3-L3)
- design-choices (2 claim(s)):
  - [observation/documented] The tool is local-first: CLI and Studio run on the user's machine with no login, API key, telemetry, or scan quota, and all context is written to .viberaven/ as markdown and JSON readable by git and any agent. -- evidence: [README.md#L173-L176](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L173-L176), [README.md#L106-L106](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L106-L106), [README.md#L51-L51](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L51-L51), [README.md#L67-L67](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L67-L67)
  - [observation/documented] Fix recipes are described as guarded and non-destructive: cleanup is plan-only and nothing is pushed or deployed automatically. -- evidence: [README.md#L173-L176](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L173-L176)
- workflows (4 claim(s)):
  - [observation/documented] `viberaven init --agents all` writes bounded VIBERAVEN:START/END rule blocks into AGENTS.md, CLAUDE.md, GEMINI.md, Cursor rules, copilot instructions, and .viberaven context files, with a --dry-run preview. -- evidence: [README.md#L125-L128](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L125-L128), [README.md#L112-L115](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L112-L115), [README.md#L123-L123](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L123-L123), [README.md#L119-L121](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L119-L121)
  - [observation/documented] The installed agent rules teach a loop: run check, read .viberaven/, fix one gap, then re-check until gate.status equals "clear". -- evidence: [README.md#L130-L130](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L130-L130)
- skills-patterns (2 claim(s)):
  - [observation/documented] A six-skill skills.sh pack routes agents: viberaven (router), architecture-context, architecture-plan, what-broke, production-context, and go-live, installable via `skills add ohad6k/VibeRaven --skill viberaven`. -- evidence: [README.md#L145-L147](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L145-L147), [README.md#L136-L143](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L136-L143), [README.md#L134-L134](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L134-L134)
  - [observation/documented] The repo doubles as an agent plugin (plugin.yaml, .claude-plugin/, .codex-plugin/, gemini-extension.json) exposing the six skills plus /viberaven-work, /viberaven-help, /viberaven-production-context, and /viberaven-launch commands. -- evidence: [README.md#L151-L151](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L151-L151)
- interfaces (4 claim(s)):
  - [observation/documented] The product is invoked via npx as `viberaven` (Studio), `viberaven check` (terminal verdict), `viberaven fix`, `viberaven init --agents`, `viberaven doctor --agents`, and `viberaven audit --vercel-supabase`, with a `--strict` gate and `--mcp` mode. -- evidence: [README.md#L83-L85](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L83-L85), [README.md#L157-L159](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L157-L159), [README.md#L112-L115](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L112-L115), [README.md#L100-L104](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L100-L104), [README.md#L31-L33](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L31-L33), [README.md#L165-L167](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L165-L167), [README.md#L119-L121](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L119-L121)
  - [observation/documented] `viberaven check` prints one line per finding with file:line evidence in artifacts and exits with code 1 when blockers exist. -- evidence: [README.md#L98-L98](https://github.com/ohad6k/VibeRaven/blob/f64e97730fd59b3d42c7f26fd769a5e85cee87c8/README.md#L98-L98)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](viberaven.detail.md)

Metadata and full claim list: [full detail](viberaven.detail.md)
Human notes ([notes](viberaven.notes.md), never overwritten by build)

[Back to map index](../../index.md)
