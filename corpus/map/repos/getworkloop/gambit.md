# getworkloop/gambit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: bolt-foundry/gambit (github id 1101529500).
Latest snapshot: commit d413df73f726 @ 8445de880a1b3f7a

## Summary (orientation draft, not independently verified)

The snapshot is documentation-heavy: Gambit is a synthetic scenario and evaluation layer for agent systems with a CLI, simulator Debug UI, and JSR library. Evidence covers its CLI commands, deck file format, sandbox execution defaults, runtime library API, and docs-organization practices.

## Source coverage

Source coverage (partial): 6 of 46 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Agent definitions use a Markdown 'deck' file format with TOML-like frontmatter (label, modelParams, actions); the README notes 'deck' remains the exact implementation term. -- evidence: [README.md#L397-L399](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L397-L399), [README.md#L440-L448](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L440-L448), [README.md#L150-L152](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L150-L152), [README.md#L401-L404](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L401-L404)
  - [observation/documented] Compute agents are TypeScript decks using Zod contextSchema/responseSchema and a run() function, with no model call; child actions are referenced by path in deck frontmatter. -- evidence: [README.md#L417-L420](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L417-L420), [README.md#L440-L448](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L440-L448), [README.md#L422-L430](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L422-L430)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: docs/external is designated external-only, excluding internal debates, open risks, and execution details, while internal doctrine lives elsewhere. -- evidence: [docs/external/ABOUT.md#L12-L13](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/external/ABOUT.md#L12-L13), [docs/README.md#L6-L7](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/README.md#L6-L7), [docs/README.md#L3-L4](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/README.md#L3-L4)
  - [observation/documented] Repository development practice: docs/posts/ is a chronological digest of notable updates, with each post expected to cross-link back to the internal execution notes holding goals, owners, and decision logs. -- evidence: [docs/posts/2026-01-19-introducing-posts.md#L20-L23](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/posts/2026-01-19-introducing-posts.md#L20-L23), [docs/posts/2026-01-19-introducing-posts.md#L7-L10](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/posts/2026-01-19-introducing-posts.md#L7-L10), [docs/posts/2026-01-19-introducing-posts.md#L33-L36](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/docs/posts/2026-01-19-introducing-posts.md#L33-L36)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI offers commands including run (one-shot with --context/--message), repl, chat, scenario, and grade, runnable via npx without installation. -- evidence: [README.md#L210-L212](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L210-L212), [README.md#L162-L164](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L162-L164), [README.md#L204-L206](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L204-L206), [README.md#L171-L173](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L171-L173), [README.md#L177-L179](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L177-L179), [README.md#L150-L152](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L150-L152)
  - [observation/documented] The `--context` flag replaced the older `--init` flag, which remains accepted as a deprecated alias for script compatibility. -- evidence: [README.md#L166-L167](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L166-L167)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions support persisted state and JSONL traces via --state and --trace flags; the Debug UI stores local-first state (sessions, traces, notes) under .gambit/. -- evidence: [README.md#L222-L224](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L222-L224), [README.md#L281-L284](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L281-L284), [README.md#L177-L179](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L177-L179)
- orchestration (1 claim(s)):
  - [observation/documented] Compute decks can call child agent definitions from code via ctx.spawnAndWait({ path, input }) and emit structured trace events with ctx.log(...). -- evidence: [README.md#L321-L324](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L321-L324)
- tools-permissions (2 claim(s)):
  - [observation/documented] CLI commands that execute decks default to worker sandbox execution; --no-worker-sandbox (or --legacy-exec) forces legacy in-process execution, and gambit.toml can set worker_sandbox equivalently. -- evidence: [README.md#L228-L238](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L228-L238), [README.md#L240-L241](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L240-L241)
  - [observation/documented] Runtime tools can be supplied via Markdown/TOML files with [[tools]] entries (name, description, optional inputSchema and action), where action bindings run Gambit agent definitions with tool arguments as context. -- evidence: [README.md#L189-L189](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L189-L189), [README.md#L191-L194](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L191-L194), [README.md#L196-L200](https://github.com/getworkloop/gambit/blob/d413df73f7262f7eb9dee56721249caeb8e759a2/README.md#L196-L200)
- evaluation (1 claim(s)):
More evidence: [full detail](gambit.detail.md)

Metadata and full claim list: [full detail](gambit.detail.md)
Human notes ([notes](gambit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
