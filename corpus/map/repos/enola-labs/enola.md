# enola-labs/enola

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f34e1998d5c4 @ 832a935ff1466519

## Summary (orientation draft, not independently verified)

Enola is a local, deterministic architectural regression-testing CLI/MCP tool that parses source into a code graph, pins baselines, and grades structural deltas of a change with configurable failure policies. Evidence is README-only documentation of the product's commands, explainers, agent integration, and documented limitations. Evidence coverage: 133 of 367 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 44 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Enola maps a repository's structure before a change and compares it afterward, reporting only what that specific change introduced rather than pre-existing issues. -- evidence: [README.md#L10-L10](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L10-L10)
- components (2 claim(s)):
  - [observation/documented] Enola runs nineteen checks it calls explainers (e.g. layers, cycles, intent, god-class, hotspots, unused-routes, coverage) on every run; a policy flag decides which findings may set the exit code. -- evidence: [README.md#L243-L243](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L243-L243), [README.md#L247-L260](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L247-L260)
  - [observation/documented] A read-only local dashboard visualizes snapshots with findings, architectural changes, lifetime usage and diagnostics tabs, and shows the generation command when no snapshot exists. -- evidence: [README.md#L151-L151](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L151-L151), [README.md#L145-L145](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L145-L145)
- design-choices (4 claim(s)):
  - [observation/documented] The tool computes its graph from parsed source with graph algorithms, using no language model, embeddings, upload, account, or license check. -- evidence: [README.md#L12-L14](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L12-L14), [README.md#L375-L375](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L375-L375)
  - [observation/documented] By default no policy is set: all findings are reported, the run exits 0, and the output explicitly states that nothing was enforced. -- evidence: [README.md#L245-L245](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L245-L245), [README.md#L204-L205](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L204-L205)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI includes commands such as enola --explain, baseline pin, check, doctor, dashboard, coverage, install --hooks, uninstall and upgrade, with flags like --fail-on, --min-confidence, --target and --max-spillover. -- evidence: [README.md#L22-L24](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L22-L24), [README.md#L405-L407](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L405-L407), [README.md#L147-L149](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L147-L149), [README.md#L157-L158](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L157-L158), [README.md#L277-L284](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L277-L284), [README.md#L135-L137](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L135-L137), [README.md#L99-L101](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L99-L101), [README.md#L160-L162](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L160-L162)
  - [observation/documented] Enola exposes itself to coding agents as an MCP server launched via the command 'enola', with per-client setup for Claude Code, Copilot, Cursor, opencode and Codex. -- evidence: [README.md#L107-L114](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L107-L114), [README.md#L119-L127](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L119-L127)
- memory-state (1 claim(s)):
  - [observation/documented] Snapshots carry a receipt with enola's version, git ref, dirty-tree status, extractors used, and a sha256-based snapshot ID; baselines pinned by a different version or ignore rules are deemed incomparable until re-pinned. -- evidence: [README.md#L141-L143](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L141-L143), [README.md#L377-L377](https://github.com/enola-labs/enola/blob/f34e1998d5c41eeeb14e95f6c3584b8fee0746c6/README.md#L377-L377)
- orchestration (1 claim(s)):
More evidence: [full detail](enola.detail.md)

Metadata and full claim list: [full detail](enola.detail.md)
Human notes ([notes](enola.notes.md), never overwritten by build)

[Back to map index](../../index.md)
