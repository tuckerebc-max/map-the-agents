# openautocoder/live-swe-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8d7dd8634580 @ f59c96dca85cc602

## Summary (orientation draft, not independently verified)

The snapshot is README-only evidence for Live-SWE-agent, a self-evolving software engineering agent built on mini-swe-agent and configured via a custom YAML config. Reported results include 79.2% on SWE-bench Verified (Claude Opus 4.5) and 45.8% on SWE-Bench Pro, with run artifacts published.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Complete trajectories, patches, and results for SWE-bench Verified and SWE-Bench Pro runs are published as release artifacts and Hugging Face datasets. -- evidence: [README.md#L71-L73](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L71-L73), [README.md#L75-L75](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L75-L75)
- design-choices (1 claim(s)):
  - [observation/documented] The agent is described as a live, runtime self-evolving software engineering agent that expands and revises its own capabilities while working on a real-world issue. -- evidence: [README.md#L24-L25](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L24-L25)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The agent is run via the mini CLI with a custom config file, e.g. `mini --config config/livesweagent.yaml`, with additional details in the config folder. -- evidence: [README.md#L63-L65](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L63-L65), [README.md#L67-L67](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L67-L67)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (4 claim(s)):
  - [observation/documented] The README reports Claude Opus 4.5 with Live-SWE-agent scoring 79.2% on SWE-bench Verified, claimed to lead open-source scaffolds. -- evidence: [README.md#L29-L32](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L29-L32)
  - [observation/documented] The README reports a 45.8% solve rate on SWE-Bench Pro, described as a state-of-the-art result as of Nov 17, 2025. -- evidence: [README.md#L29-L32](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L29-L32)
- dependencies (1 claim(s)):
  - [observation/documented] Live-SWE-agent is built on top of the mini-swe-agent framework with very minimal modifications. -- evidence: [README.md#L59-L59](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L59-L59)
- limitations (1 claim(s)):
  - [inference/documented] The README's setup guide link for installing mini-swe-agent appears empty, so installation instructions may be incomplete in this snapshot. -- evidence: [README.md#L61-L61](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L61-L61)
- relevance (1 claim(s)):
  - [observation/documented] The project positions itself as an open scaffold for fair benchmarking of LLMs on software engineering tasks, contrasting with proprietary scaffolds. -- evidence: [README.md#L36-L36](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L36-L36), [README.md#L38-L38](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L38-L38)

(2 additional claim(s) omitted for length; see [full detail](live-swe-agent.detail.md) for every claim.)

Metadata and full claim list: [full detail](live-swe-agent.detail.md)
Human notes ([notes](live-swe-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
