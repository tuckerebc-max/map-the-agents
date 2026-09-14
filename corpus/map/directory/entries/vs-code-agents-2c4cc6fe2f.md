# vs-code-agents (`vs-code-agents`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: groupzer0
- License: MIT
- Language: Markdown, Python
- Interface: platforms=IDE; install=git clone https://github.com/groupzer0/agents.git; copy .agent.md files into .github/agents/ or user-level VS Code profile; install Flowbaby extension from VS Code Marketplace
- Model providers: GitHub Copilot (via VS Code)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [groupzer0/vs-code-agents](../../repos/groupzer0/vs-code-agents.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Multi-agent workflow system for GitHub Copilot in VS Code bringing structure, quality gates, and long-term memory to AI-assisted development. Specialized agents (Planner, Implementer, Security, QA, etc.) each own a specific part of the dev workflow with clear constraints and document-driven output; designed for persistent, workspace-scoped memory via Flowbaby.

(captured site page body (agents/vs-code-agents.md), not a verified repo-code finding)
vs-code-agents exists because unstructured Copilot sessions forget context, skip quality gates, and lose decision history. It defines 13 custom agents (planner, analyst, architect, security, critic, implementer, code-reviewer, QA, UAT, devops, roadmap, retrospective, process-improvement) as Markdown files installed into a project's .github/agents/ directory, each with hard constraints: the Planner cannot write code and the Implementer cannot redesign. Agents hand off through structured Markdown documents stored in an agent-output/ audit trail, and the Security agent follows a five-phase framework covering STRIDE threat modeling, OWASP Top 10, CVE scanning, and ASVS compliance. Cross-session memory requires the companion Flowbaby VS Code extension backed by Python 3.10+. It targets teams standardizing Copilot-assisted development with review gates.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vs-code-agents.md)
