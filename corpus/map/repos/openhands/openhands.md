# openhands/openhands

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 28464621d879 @ f5c20f1428089f35

## Summary (orientation draft, not independently verified)

Evidence shows Agent Canvas is a self-hosted developer control center for coding agents and automations, in beta, installable via npm, Docker, or source, powered by the OpenHands Agent Server REST API and optionally paired with an Automation Server. No code or evaluation harness is shown in the provided slices.

## Source coverage

Source coverage (partial): 3 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Agent Canvas is described as a self-hosted developer control center for coding agents and automations, currently in beta status. -- evidence: [README.md#L3-L31](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L3-L31), [README.md#L33-L33](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L33-L33)
- components (1 claim(s)):
  - [observation/documented] Agent Canvas is powered by the OpenHands Agent Server, a REST API for running multiple agents on one machine; the frontend can connect to and switch between multiple Agent Servers. -- evidence: [README.md#L126-L126](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L126-L126)
- design-choices (1 claim(s)):
  - [observation/documented] The project is split across repositories: this repo owns the frontend, backend selection, and local-stack orchestration, while the SDK owns the Agent Server API and the automation repo owns scheduling and dispatching. -- evidence: [README.md#L150-L150](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L150-L150), [README.md#L143-L148](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L143-L148)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to AGENTS.md for contributor-specific repository boundaries and a required custom code-review guide. -- evidence: [README.md#L150-L150](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L150-L150)
  - [observation/documented] Repository development practice: the changelog follows Keep a Changelog format and the project adheres to Semantic Versioning; npm publishing is automated via a GitHub Actions workflow with OIDC trusted publishing. -- evidence: [CHANGELOG.md#L5-L6](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/CHANGELOG.md#L5-L6), [CHANGELOG.md#L14-L26](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/CHANGELOG.md#L14-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] It can run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. -- evidence: [README.md#L3-L31](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L3-L31)
  - [observation/documented] The agent-canvas CLI starts the full local stack by default and supports --frontend-only and --backend-only flags to run pieces separately. -- evidence: [README.md#L75-L75](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L75-L75), [README.md#L77-L80](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L77-L80)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] An Automation Server can be paired with the Agent Server to run agents on a schedule or in response to events, dispatching conversations to the Agent Server/SDK. -- evidence: [README.md#L150-L150](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L150-L150), [README.md#L135-L135](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L135-L135)
- tools-permissions (1 claim(s)):
  - [observation/documented] Running without a sandbox executes the agent-server directly on the host, where the agent has full filesystem access; the Docker option restricts agent access to projects under PROJECTS_PATH. -- evidence: [README.md#L65-L66](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L65-L66), [README.md#L104-L104](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L104-L104)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](openhands.detail.md)

Metadata and full claim list: [full detail](openhands.detail.md)
Human notes ([notes](openhands.notes.md), never overwritten by build)

[Back to map index](../../index.md)
