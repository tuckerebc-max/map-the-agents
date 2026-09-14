# rylaa/fable5-opus5-orchestrator

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d258385088a6 @ b517b7606d696080

## Summary (orientation draft, not independently verified)

A Claude Code plugin ('Fable Orchestrator') that forces upfront clarification via four hooks, a `## Clarified` record, and a checkbox ledger in ./.workflow/LEDGER.md, with env-var configuration, teammate reaping, and metrics logging. All prior product claims were verified against cited README slices; the MIT license line is not asserted here.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Four hooks enforce the workflow: a PreToolUse clarify gate, a PreToolUse spawn gate, a task-list gate on the third ledgerless tracker task, and a Stop gate when a turn ends with open ledger items. -- evidence: [README.md#L28-L33](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L28-L33)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: tests run with `python3 -m pytest tests/ -q`; the hook tests execute the stdin/stdout JSON filters end to end as subprocesses, plus a second layer pinning the core text and the skill. -- evidence: [README.md#L79-L81](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L79-L81), [README.md#L83-L83](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L83-L83)
- skills-patterns (1 claim(s)):
  - [observation/documented] The clarify protocol in skills/clarify/SKILL.md scans seven axes (scope edge, acceptance, constraints, decision ownership, priority conflicts, existing-code contact, failure behavior) and always asks whether work lands on the current branch or a new one. -- evidence: [README.md#L39-L39](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L39-L39)
- interfaces (1 claim(s)):
  - [observation/documented] The product is a Claude Code plugin installed via the marketplace commands `/plugin marketplace add Rylaa/fable5-opus5-orchestrator` and `/plugin install orchestrator@fable-orchestrator`. -- evidence: [README.md#L9-L12](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L9-L12)
- memory-state (2 claim(s)):
  - [observation/documented] Requirements are recorded as checkbox lines in `./.workflow/LEDGER.md` with open, done, and deferred-with-approval states; phases cite item numbers and discoveries are appended. -- evidence: [README.md#L52-L57](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L52-L57), [README.md#L59-L59](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L59-L59), [README.md#L18-L22](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L18-L22)
  - [observation/documented] The hook validates the `## Clarified` record by four rules: every question has an `->` answer, no `Assumption:` line, at least one answered question, and a `Branch:` line; only plain bullets count, not fenced templates or HTML comments. -- evidence: [README.md#L48-L48](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L48-L48)
- orchestration (2 claim(s)):
  - [observation/documented] Sessions run as: chair reads the repo, asks all questions in rounds before planning, writes a ledger, then works directly or through workers; workers cannot ask the user anything. -- evidence: [README.md#L18-L22](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L18-L22)
  - [observation/documented] Finished teammates are reaped automatically at session end and on a rate-limited idle sweep (default 1-hour idle threshold); metrics go to ~/.claude/fable-orch/metrics.jsonl, summarized by `python3 scripts/stats.py`. -- evidence: [README.md#L65-L73](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L65-L73), [README.md#L75-L75](https://github.com/Rylaa/fable5-opus5-orchestrator/blob/d258385088a618260f8cc6fcf9486d388edacdfb/README.md#L75-L75)
- tools-permissions (1 claim(s)):
More evidence: [full detail](fable5-opus5-orchestrator.detail.md)

Metadata and full claim list: [full detail](fable5-opus5-orchestrator.detail.md)
Human notes ([notes](fable5-opus5-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
