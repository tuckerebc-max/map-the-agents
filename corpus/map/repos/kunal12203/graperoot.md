# kunal12203/graperoot

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e21c5b9cd3e3 @ 657d207f0df5b456

## Summary (orientation draft, not independently verified)

GrapeRoot is described as an open-source launcher that sits between the user and an AI coding assistant, building a semantic graph of files, symbols, imports, and call chains to pre-load relevant code into each prompt. The product exposes launcher commands: `dgc` for Claude Code, `dg` for Codex CLI, `dgo` for OpenCode, and `graperoot . --<tool>` flags for Cursor, Gemini CLI, Copilot, OpenClaw, Kilocode, MiMo Code, Antigravity, Kiro CLI, and Command Code. Evidence coverage: 181 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] GrapeRoot is described as an open-source launcher that sits between the user and an AI coding assistant, building a semantic graph of files, symbols, imports, and call chains to pre-load relevant code into each prompt. -- evidence: [README.md#L36-L36](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L36-L36)
- components (1 claim(s)):
  - [observation/documented] Project data lives in `<project>/.dual-graph/` (info_graph.json for the semantic graph, chat_action_graph.json for session memory, context-store.json for persistent decisions/tasks/facts), with a global install at `~/.dual-graph/`. -- evidence: [README.md#L287-L291](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L287-L291), [README.md#L279-L283](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L279-L283), [README.md#L285-L285](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L285-L285), [README.md#L277-L277](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L277-L277)
- design-choices (1 claim(s)):
  - [observation/documented] All processing is stated to be local with no code leaving the machine, and telemetry is limited to anonymous crash reports (error type, failed step, OS/Python version, product version), explicitly excluding code, file paths, project names, prompts, and personal data. -- evidence: [README.md#L338-L338](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L338-L338), [README.md#L334-L336](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L334-L336), [README.md#L332-L332](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L332-L332), [README.md#L271-L271](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L271-L271)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's contributing section invites PRs for bug fixes, new AI assistant support, install improvements, and docs for the open-source launcher scripts. -- evidence: [README.md#L368-L368](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L368-L368)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes launcher commands: `dgc` for Claude Code, `dg` for Codex CLI, `dgo` for OpenCode, and `graperoot . --<tool>` flags for Cursor, Gemini CLI, Copilot, OpenClaw, Kilocode, MiMo Code, Antigravity, Kiro CLI, and Command Code. -- evidence: [README.md#L127-L140](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L127-L140), [README.md#L240-L251](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L240-L251), [README.md#L179-L183](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L179-L183), [README.md#L187-L191](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L187-L191), [README.md#L232-L236](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L232-L236)
  - [observation/documented] The `graperoot` CLI supports an interactive picker, `--version`, `--update`, `--no-auto-update`, `--auto-update`, and `--no-telemetry`/`--telemetry` flags per the README usage sections. -- evidence: [README.md#L321-L324](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L321-L324), [README.md#L223-L228](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L223-L228), [README.md#L311-L314](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L311-L314), [README.md#L316-L319](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L316-L319), [README.md#L340-L344](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L340-L344)
- memory-state (1 claim(s)):
  - [observation/documented] The README describes session memory: files that were read, edited, or queried are weighted higher in future turns, so context compounds across a session. -- evidence: [README.md#L52-L52](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L52-L52), [README.md#L266-L269](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L266-L269)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](graperoot.detail.md)

Metadata and full claim list: [full detail](graperoot.detail.md)
Human notes ([notes](graperoot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
