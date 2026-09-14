# gitlab-copilot-coding-agent (`gitlab-copilot-coding-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: satomic
- License: No license file in the repository
- Language: Python
- Interface: platforms=CLI; install=Import repo to GitLab via Git URL, configure CI/CD variables, deploy webhook service via Docker (satomic/gitlab-copilot-coding-agent-hook:latest) or from source (python3 main.py)
- Model providers: GitHub Copilot
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [satomic/gitlab-copilot-coding-agent](../../repos/satomic/gitlab-copilot-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Bridges GitHub Copilot CLI with GitLab CI/CD for fully autonomous coding workflows. Issue assignment triggers automated implementation with MR creation, MR comments trigger code updates, and MR reviewer assignment triggers intelligent comprehensive code review — all without leaving GitLab. Flask webhook service captures GitLab events.

(captured site page body (agents/gitlab-copilot-coding-agent.md), not a verified repo-code finding)
GitHub's coding agent lives in GitHub's ecosystem, and this project grafts it onto GitLab. A Flask webhook service captures GitLab events — issue assignment, MR comments, reviewer assignment — and triggers CI pipelines in an orchestrator repo, where the Copilot CLI (running in a dedicated Docker image) plans, implements, pushes commits, and opens merge requests, or produces severity-categorized review reports. Setup requires a Copilot subscription with a fine-grained PAT, a dedicated bot GitLab user, and Docker or Kubernetes runners, with CI variables holding the credentials. It is a single-contributor Python project (58 commits, 41 stars) with multilingual docs and video walkthroughs, useful to GitLab shops that want Copilot's agent without leaving their platform.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gitlab-copilot-coding-agent.md)
