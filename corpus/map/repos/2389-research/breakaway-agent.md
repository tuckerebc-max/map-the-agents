# 2389-research/breakaway-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit a426c399d50f @ fa31829804eca3a3

## Summary (orientation draft, not independently verified)

break-away is a small, hackable Bun/TypeScript code agent with a policy-blind loop, five tools, subagent spawning, and no permission guardrails; the snapshot also includes an implementation plan for making the compiled binary first-class. Evidence coverage: 151 of 387 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The core agent loop is described as policy-blind: all behavior is injected through a Policy object, and the run() loop in src/agent.ts is roughly 165 lines. -- evidence: [README.md#L72-L72](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L72-L72)
  - [observation/documented] The agent supports self-modification: editing tools.ts, policy.ts, or system.txt then SIGHUP or /reload hot-reloads via cache-busted dynamic import, while SIGUSR2 or /restart exits with code 42 so a wrapper relaunches it (up to 20 times). -- evidence: [README.md#L80-L80](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L80-L80), [README.md#L82-L87](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L82-L87), [README.md#L78-L78](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L78-L78)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the implementation plan mandates TDD (write failing test, verify failure, implement, verify pass), conventional commits with a Claude-Session trailer, bun test staying green (80+ tests), no mocks of own code, stdout purity, and .env never committed or printed. -- evidence: [docs/superpowers/plans/2026-08-30-first-class-binary.md#L15-L22](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L15-L22), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L37-L37](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L37-L37), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L56-L56](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L56-L56), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L73-L73](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L73-L73)
  - [observation/documented] Repository development practice: the plan document instructs agentic workers to use superpowers:subagent-driven-development or superpowers:executing-plans to implement tasks with checkbox tracking. -- evidence: [docs/superpowers/plans/2026-08-30-first-class-binary.md#L3-L3](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L3-L3)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The model drives five tools: read_file with paged line-window reads, write_file, atomic single-occurrence edit_file, bash with process-group timeout kill and 8000-char output cap, and spawn_agent. -- evidence: [README.md#L55-L60](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L55-L60)
  - [observation/documented] CLI flags include --cwd, --model, --system, --serious (long-horizon profile with retries, error nudging, and a completion audit), --max-turns, --quiet, --debug, and --help. -- evidence: [README.md#L29-L42](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L29-L42)
- memory-state (1 claim(s)):
  - [observation/documented] Each run writes a JSONL transcript to .transcripts/ (or $BREAK_AWAY_TRANSCRIPT_DIR), one file per run. -- evidence: [README.md#L49-L49](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L49-L49)
- orchestration (2 claim(s)):
  - [observation/documented] spawn_agent launches child agents whose stdout/stderr go to spawn-<ts> files; nesting depth is tracked via BREAK_AWAY_DEPTH and capped by BREAK_AWAY_MAX_DEPTH (default 3), returning an error at the cap. -- evidence: [README.md#L99-L99](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L99-L99), [README.md#L97-L97](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L97-L97)
  - [observation/documented] An agents.jsonl registry records spawn, start, and done events across parent and child agents, and done records carry status (ok/error) and stop_reason. -- evidence: [README.md#L110-L110](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L110-L110), [README.md#L101-L101](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L101-L101)
- tools-permissions (1 claim(s)):
More evidence: [full detail](breakaway-agent.detail.md)

Metadata and full claim list: [full detail](breakaway-agent.detail.md)
Human notes ([notes](breakaway-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
