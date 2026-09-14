# onecli/onecli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3e595ef04d1a @ 675314da46d13fff

## Summary (orientation draft, not independently verified)

OneCLI is an open-source, self-hostable platform for running one sandboxed AI agent per team member, with a Rust gateway that injects credentials, a Next.js dashboard, API control plane, runner, Slack channel adapter, and SSH access. Evidence is mostly README and docs (documentation-based), plus contributor setup and licensing terms. Evidence coverage: 118 of 147 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The platform comprises a Next.js web dashboard, an API server control plane owning the database and work queue, a Rust gateway, a runner, a sandbox supervisor, an SSH terminator, and a Slack channel adapter. -- evidence: [README.md#L91-L98](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L91-L98)
- design-choices (2 claim(s)):
  - [observation/documented] Agents run in isolated sandboxes whose only network egress is the gateway, so they can reach only granted resources; the runner is outbound-only with no inbound ports, enabling NAT'd hosts without ingress or tunnels. -- evidence: [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79), [README.md#L81-L81](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L81-L81)
  - [observation/documented] Licensing is Apache-2.0 except for `ee/` directories under the OneCLI Enterprise License, which is free for development, testing and evaluation but requires a subscription for production use. -- evidence: [README.md#L121-L127](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L121-L127)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local setup is `mise install`, `pnpm install`, `pnpm dev`, which generates .env secrets, starts PostgreSQL, applies migrations, and runs web, api, gateway and runner; `pnpm check` is the pre-push and CI gate and `pnpm test` runs test suites. -- evidence: [docs/development.md#L17-L21](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L17-L21), [docs/development.md#L34-L47](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L34-L47), [README.md#L102-L107](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L102-L107)
  - [observation/documented] Repository development practice: contributions require reading the Contributing Guide and Code of Conduct and are accepted under a Contributor License Agreement with ChartDB, Inc., signable via the CLA Assistant flow on a pull request. -- evidence: [README.md#L113-L113](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L113-L113), [CLA.md#L3-L5](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/CLA.md#L3-L5), [CLA.md#L84-L88](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/CLA.md#L84-L88)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Each agent can have its own Slack app answering in channels and DMs under its own name; a DM shares the same conversation as the web dashboard, and gateway approvals appear as Slack cards with Approve/Deny buttons. -- evidence: [docs/channels-slack.md#L15-L20](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/channels-slack.md#L15-L20), [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79)
- memory-state (1 claim(s)):
  - [observation/documented] Agent memory is kept by the platform so it persists, and users can read and edit it at any time from the dashboard. -- evidence: [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79)
- orchestration (1 claim(s)):
More evidence: [full detail](onecli.detail.md)

Metadata and full claim list: [full detail](onecli.detail.md)
Human notes ([notes](onecli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
