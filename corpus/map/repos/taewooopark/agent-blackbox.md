# taewooopark/agent-blackbox

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bc0d72aeb7bd @ 04a1eb49ea1e68ba

## Summary (orientation draft, not independently verified)

Selected evidence records: Agent-Blackbox is described as a local-first flight recorder and context-efficiency profiler for coding agents, rebuilding each run as a live, replayable operational graph from observed events rather than the agent's own summary. The daemon exposes an HTTP/WebSocket API including POST /events, GET /graph?seq, GET /snapshot, GET /audit, GET /efficiency, POST /suggest, GET/POST /optimize[/apply|/revert], GET /handoff, and WS /stream for live snapshots.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Agent-Blackbox is described as a local-first flight recorder and context-efficiency profiler for coding agents, rebuilding each run as a live, replayable operational graph from observed events rather than the agent's own summary. -- evidence: [README.md#L31-L31](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L31-L31)
- components (1 claim(s)):
  - [observation/documented] The repository is organized into packages/core (canonical TraceEvents, graph, redaction, replay, audit, handoff, efficiency engine), host adapters for claude-code, codex, and opencode, apps/daemon, and apps/dashboard. -- evidence: [README.md#L404-L415](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L404-L415), [README.md#L365-L370](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L365-L370)
- design-choices (2 claim(s)):
  - [observation/documented] The stated philosophy is to derive truth from observed events rather than the agent's self-report, with every node being an event the agent actually emitted (read, edit, command with exit code, delegation). -- evidence: [README.md#L378-L381](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L378-L381), [README.md#L376-L376](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L376-L376)
  - [observation/documented] The tool is local-first with no API key: traces stay on the machine, raw prompts, secrets, and file contents are redacted by default, and even model-based suggestions receive only a redacted digest (metric statuses, counts, file basenames, command verbs). -- evidence: [README.md#L378-L381](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L378-L381), [README.md#L241-L241](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L241-L241)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: to build from source, clone the repo, run npm install and npm run build:cli, then run node packages/cli/dist/cli.js; development checks use npm run check (typecheck + tests) and npm run build. -- evidence: [README.md#L101-L105](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L101-L105), [README.md#L421-L425](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L421-L425)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The daemon exposes an HTTP/WebSocket API including POST /events, GET /graph?seq, GET /snapshot, GET /audit, GET /efficiency, POST /suggest, GET/POST /optimize[/apply|/revert], GET /handoff, and WS /stream for live snapshots. -- evidence: [README.md#L387-L398](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L387-L398)
- memory-state (1 claim(s)):
  - [observation/documented] Per-project state lives under <project>/.agent-blackbox/ (optimization.json, efficiency-profile.json, optional rules.json), with cross-run baselines stored as baselines.json next to the daemon's event store. -- evidence: [README.md#L417-L417](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L417-L417)
- orchestration (1 claim(s)):
  - [observation/documented] The session map renders subagent genealogy: real delegations (task tool, child sessions, workflow fan-out) fork into their own lanes attributed to the subagent, with lanes named by role distilled from the spawn type or task prompt. -- evidence: [README.md#L165-L177](https://github.com/TaewoooPark/Agent-Blackbox/blob/bc0d72aeb7bd207b48099ba07f813be37c0e449c/README.md#L165-L177)
- tools-permissions (1 claim(s)):
More evidence: [full detail](agent-blackbox.detail.md)

Metadata and full claim list: [full detail](agent-blackbox.detail.md)
Human notes ([notes](agent-blackbox.notes.md), never overwritten by build)

[Back to map index](../../index.md)
