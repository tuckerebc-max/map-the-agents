# AX (`ax-agent-executor`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: google
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI; install=curl -fsSL https://github.com/google/ax/releases/latest/download/install.sh | sh (one-line CLI installer); or from a checkout: make install
- Model providers: Runs any containerized agent workload — a Claude Code runner ships in-repo (cmd/runners/claude-code-runner, examples/claude-code) and any custom image or command works; agents bring their own providers. A Model resource also configures providers/credentials for platform components
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [google/ax](../../repos/google/ax.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A Kubernetes-shaped declarative runtime for agent workloads: tasks, workspaces (pre-wired Git repos, MCP servers, skills), models, and egress gateways are YAML manifests applied with a kubectl-like CLI, each sandboxed and suspend/resume-able on Agent Substrate actors. It targets fleets of millions of agent tasks per cluster with checkpointing and ssh-into-sandbox.

(captured site page body (agents/ax-agent-executor.md), not a verified repo-code finding)
AX came out of the observation that agents are a new workload class — stateful, loop-running, money-burning, and badly served by either stateless services or batch jobs — and answers it the way Kubernetes answered containers. Four primitives (Task, Workspace, Model, Gateway) are declared in ax.io/v1alpha1 YAML and applied with a deliberately kubectl-shaped CLI; a task lands in a gVisor-sandboxed actor on Agent Substrate with CPU/memory limits, a pre-cloned workspace with MCP servers and skills materialized, credentials injected from Kubernetes secrets, and egress restricted to gateway allowlists. Tasks suspend to checkpoint and resume where they left off, \`ax ssh\` opens a shell inside the running sandbox, and the whole thing promotes unchanged from a local Kind cluster to GKE. Platform teams running fleets of coding-agent workloads (the shipped runner is Claude Code) are the audience; the maintainers describe it as job orchestration, not an agent framework.
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/ax-agent-executor.md)
