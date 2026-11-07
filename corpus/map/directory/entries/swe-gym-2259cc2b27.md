# SWE-Gym (`swe-gym`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: SWE-Gym
- License: Apache-2.0
- Language: Python
- Interface: install=docker
- Model providers: GPT-4o and Claude 3.5 Sonnet trajectories; fine-tunes OpenHands/Moatless 7B/32B agents
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [swe-gym/swe-gym](../../repos/swe-gym/swe-gym.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First open environment for training and verifying real-world software engineering agents. Contains 2.4K real tasks from 11 Python repositories with pre-built Docker images. Achieved a new open state-of-the-art (32% on SWE-Bench Verified, 26% on SWE-Bench Lite). ICML 2025 accepted. Combines repository context, executable environments, and test verification.

(captured site page body (agents/swe-gym.md), not a verified repo-code finding)
SWE-Gym was built to give agent researchers what SWE-bench gave evaluators: an executable, verifiable training ground. It packages 2,438 real tasks from 11 popular Python repositories, each with repository context, a pre-built Docker environment, and executable tests that decide success, so agents train against ground-truth reward rather than model judgment. The accompanying work showed that fine-tuning a 32B model on fewer than 500 agent-environment trajectories raised SWE-bench Verified by 14 points, and that verifiers trained on the same trajectories enabled best-of-n inference-time scaling to 32% Verified and 26% Lite — the open state of the art at publication (ICML 2025). Reproduction is documented for both the OpenHands and MoatlessTools scaffolds. ML researchers training or verifying SWE agents are the users, and the environment later seeded task-generation efforts like SWE-smith.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/swe-gym.md)
