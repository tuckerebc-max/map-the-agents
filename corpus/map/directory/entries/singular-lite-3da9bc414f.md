# Singular (`singular-lite`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: alex-reysa
- License: GPL-3.0
- Language: Shell
- Interface: platforms=Autonomous, CLI; install=./install.sh installs to ~/.singular with a per-repo version pin; requires bash \>= 4, python3, git
- Model providers: delegates to the installed runner CLIs (claude, codex)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [alex-reysa/singular-lite](../../repos/alex-reysa/singular-lite.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A three-tier local orchestration engine — L0 origin scheduler running reconcile cycles (import, recover, integrate, dispatch, snapshot), L1 area planners, and L2 worker agents each in an isolated git worktree — with durable per-task leases, gate commands whose results feed an auditor model, and a decider mapping failures to retry, amend-scope, escalate, or park.

(captured site page body (agents/singular-lite.md), not a verified repo-code finding)
Singular (repo singular-lite) is a bash-and-python orchestration engine for running many autonomous coding agents against one repository. Its three-tier scheduling model puts an L0 origin scheduler through a reconcile cycle — import, recover, integrate, dispatch, snapshot — with L1 area planners decomposing work and L2 worker agents each executing one task in an isolated git worktree on a per-task branch, using whatever runner CLI is on PATH such as claude or codex. Coordination is durable rather than ad hoc: per-task leases prevent collision, state packets track owned files and changes, gate commands like npm test feed results to an auditor model, and a decider maps failures to retry, amend-scope, escalate, or park. Workers dispatch detached by default with a reaper attributing completions and crashes on later cycles, and the autonomy loop supports human approval gates and context continuity through capsules, findings ledgers, and session affinity. It targets macOS and Linux operators running long-lived agent fleets in a single repo.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/singular-lite.md)
