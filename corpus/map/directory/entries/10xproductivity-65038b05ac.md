# 10xProductivity (`10xproductivity`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ZhixiangLuo
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=git clone; create python venv (python3 -m venv .venv); pip install -e .\[dev\]; instruct coding agent to read setup.md
- Model providers: agent-agnostic (Cursor, Claude Code, Codex, Copilot via --engine flag)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [zhixiangluo/10xproductivity](../../repos/zhixiangluo/10xproductivity.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first personal AI assistant that turns existing coding agents (Cursor, Claude Code, Codex, Copilot) into a work assistant operating within corporate constraints — no new infrastructure, no IT approval, no Slack apps or webhooks. Uses your existing authenticated sessions and permissions. Features a coaching loop where human-AI interaction creates reusable skills, triggers, and workflows over time. Ships 25+ pre-built tool-connection ...

(captured site page body (agents/10xproductivity.md), not a verified repo-code finding)
Inside most companies, employees cannot install Slack apps, webhooks, or automation platforms without IT approval, yet their coding agent already has authenticated browser sessions and broad tool access. 10xProductivity exploits that: a local-first Python framework invokes the agent you already use (Cursor, Claude Code, Codex, Copilot) through an --engine flag and drives it with recipes, triggers, and workflows for enterprise search, stand-up prep, or Slack polling. A hooks directory keeps credentials and browser state out of the repo tree, and new workflows are built in supervised coaching sessions before being trusted to run autonomously. It targets employees who want personal automation without IT involvement.
Sources: [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/10xproductivity.md)
