# wienerdog-ai/wienerdog

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 91668da62822 @ 10c545f38401b46b

## Summary (orientation draft, not independently verified)

Wienerdog is a file-based memory/routine installer for Claude Code and Codex CLI: a thin Node CLI compiles a canonical core at ~/.wienerdog/ into per-harness adapters, with a PARA markdown vault, nightly transcript-driven 'dreaming' with tiered gates, OS-native scheduling, and a governed Google Workspace CLI. Evidence is largely documentation (ARCHITECTURE.md, README) plus a FIX-PLAN describing pending gate fixes. Evidence coverage: 92 of 151 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 948 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The architecture describes the product as a compiler plus prompts, not an application: a thin CLI, short-lived hook scripts, and scheduled jobs whose brain is claude -p or codex exec, targeting under ~4k LOC of plain Node 18+ with no build step. -- evidence: [docs/ARCHITECTURE.md#L5-L5](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The system map shows a canonical core at ~/.wienerdog/ (config.yaml, skills, prompts, bin, state, secrets, logs, install manifest) plus Claude and Codex adapters that sync compiles into ~/.claude/ and ~/.codex/. -- evidence: [docs/ARCHITECTURE.md#L9-L56](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L9-L56)
- design-choices (1 claim(s)):
  - [observation/documented] Wienerdog never owns the user's CLAUDE.md/AGENTS.md; it manages only a sentinel-delimited block, sync overwrites edits inside sentinels while leaving outside edits untouched, and uninstall removes exactly that region. -- evidence: [docs/ARCHITECTURE.md#L92-L92](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L92-L92)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the repo dogfoods its own product — its memory vault lives in memory/, its development conventions are its own CLAUDE.md, and most code is written by mid-tier AI models following its spec system in docs/specs/. -- evidence: [README.md#L86-L86](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/README.md#L86-L86)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The wienerdog CLI exposes subcommands install, sync, doctor, dream, schedule, run-job, gws, and uninstall per the architecture system map. -- evidence: [docs/ARCHITECTURE.md#L9-L56](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L9-L56)
- memory-state (2 claim(s)):
  - [observation/documented] The memory vault defaults to ~/wienerdog/ with PARA-style folders (00-Inbox through 07-Daily, reports, .git); machine state such as watermarks, queue, and score cache lives in ~/.wienerdog/state/, never in the vault. -- evidence: [docs/ARCHITECTURE.md#L102-L115](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L102-L115), [docs/ARCHITECTURE.md#L154-L154](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L154-L154)
  - [observation/documented] Vault notes carry mandatory frontmatter provenance fields on every auto-write, including id, type, origin, source_sessions, confidence, recurrence, and a derived_from_untrusted flag. -- evidence: [docs/ARCHITECTURE.md#L117-L117](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L117-L117), [docs/ARCHITECTURE.md#L119-L133](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L119-L133)
- orchestration (2 claim(s)):
More evidence: [full detail](wienerdog.detail.md)

Metadata and full claim list: [full detail](wienerdog.detail.md)
Human notes ([notes](wienerdog.notes.md), never overwritten by build)

[Back to map index](../../index.md)
