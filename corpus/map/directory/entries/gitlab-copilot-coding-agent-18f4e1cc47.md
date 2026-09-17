# gitlab-copilot-coding-agent (`gitlab-copilot-coding-agent`)

[Back to directory index](../index.md)

Directory membership: backing-only.

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

(backing feed `description`, not a verified repo-code finding)
GitHub's coding agent lives in GitHub's ecosystem, and this project grafts it onto GitLab. A Flask webhook service captures GitLab events — issue assignment, MR comments, reviewer assignment — and tri
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
