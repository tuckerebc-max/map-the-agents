# FinRobot (`finrobot`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: AI4Finance-Foundation
- License: Apache-2.0
- Language: Python
- Interface: install=pip
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ai4finance-foundation/finrobot](../../repos/ai4finance-foundation/finrobot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI agent platform for financial applications (not a coding agent). Automates equity research, investment analysis, and valuation. Strict separation of deterministic financial computation (pure-Python operators) from LLM-based narration -- all financial numbers are code-calculated, not LLM-generated, with full provenance tracking. Multi-agent architecture: 1 Lead Agent, 5 role-based sub-agents (Data, Analysis, Modeling, Synthesis, Report), and 3 debate agents (Bull, Bear, ...

(captured site page body (agents/finrobot.md), not a verified repo-code finding)
FinRobot, from the AI4Finance Foundation, applies multi-agent LLM architecture to investment research: a lead orchestrator coordinates role-based pipeline agents through equity research, valuation (DCF, comps, LBO), and risk assessment, with debate agents arguing against drafts before reports finalize. Its design principle separates deterministic computation from narrative generation — Python operators compute every number, and LLMs only shape the reasoning and prose around them, which addresses the reliability problem of LLM-generated financial figures. The project ships as a Python package plus a Tauri/React desktop frontend and is documented in an ICAIF 2024 paper. Its users are quantitative researchers, financial analysts, and academics experimenting with agentic workflows for investment analysis.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/finrobot.md)
