---
access: public
aliases: []
claim_ids:
- clm_1d012dce7b71e72a2c9c3ff297644a7e25997f523bf240cb9ea98a87be49d04a
- clm_1fe536f25a0b7092a6525ac18efa25a95d3e4d94476ba8d06bf0059dc35a3656
- clm_58f902c50383e01b70d304d2debc92a9d4c1fcd864db92fd72948cbf7b2c7102
- clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497
- clm_8189e45d703dd865bbfce150d0a7e69c39a93e21427942b050bf84c69e1fbf8e
- clm_ceb8d78a9aba6ec7a67288a296fdf3b06ffcc5e0e4b6112f339c0b1668c1efa5
- clm_ea0709eb341359ebc0cabb856a5ecc98e85f082d2fb3f84f18a4333a37956516
maturity: draft
page_id: pg_6665be40fa365d8181612ae80cba9d80
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0ab040f7cdde53dd9fbe67ca547755e6
title: TheSylvester/crispy/CLAUDE.md @ a0abb0bac65b
updated_at: '2026-09-14T03:18:51Z'
---

# TheSylvester/crispy/CLAUDE.md @ a0abb0bac65b

<!-- rcw:begin owner=source:src_0ab040f7cdde53dd9fbe67ca547755e6 block=evidence -->
- Repository development practice: contributors run npm run typecheck, npm test (e2e pipeline test), npm run test:unit (vitest), and npm run dev for a dev server at localhost:3456, with visual checks via a browser-qa sub-agent. [@claim:clm_1d012dce7b71e72a2c9c3ff297644a7e25997f523bf240cb9ea98a87be49d04a]
- Core includes vendor-agnostic transcript types, per-vendor adapters, a session-channel pub/sub multiplexer, session-manager orchestration, and an activity-index that owns all ~/.crispy/ disk I/O. [@claim:clm_1fe536f25a0b7092a6525ac18efa25a95d3e4d94476ba8d06bf0059dc35a3656]
- Repository development practice: user-facing skills belong in src/plugin/skills/ while dev-only tools go in .claude/skills/, and uncommitted .ai-reference/ specs must be read before changing transcript.ts or UI behavior. [@claim:clm_58f902c50383e01b70d304d2debc92a9d4c1fcd864db92fd72948cbf7b2c7102]
- Per the architecture doc, only the Claude adapter is wired up today, and the roadmap lists Gemini CLI and OpenCode support as coming soon. [@claim:clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497]
- Core is written in a functional style: free functions with module-level state rather than classes, and the webview derives all state client-side from channel events with no direct file I/O. [@claim:clm_8189e45d703dd865bbfce150d0a7e69c39a93e21427942b050bf84c69e1fbf8e]
- Repository development practice: CLAUDE.md forbids business logic in the host, vendor fields in transcript.ts, edits to generated Codex protocol files, and writes to ~/.crispy/ outside activity-index.ts. [@claim:clm_ceb8d78a9aba6ec7a67288a296fdf3b06ffcc5e0e4b6112f339c0b1668c1efa5]
- The codebase is organized into three layers: core (src/core/) owning state and logic, host (src/host/) as a thin RPC router, and webview (src/webview/) for UI. [@claim:clm_ea0709eb341359ebc0cabb856a5ecc98e85f082d2fb3f84f18a4333a37956516]
<!-- rcw:end owner=source:src_0ab040f7cdde53dd9fbe67ca547755e6 block=evidence -->

## Researcher notes

