# multi-agent-ai-sdr-flink-orchestrator (`multi-agent-ai-sdr-flink-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: thefalc
- License: MIT
- Language: Python (agents) and JavaScript/TypeScript (NextJS web app)
- Interface: install=git clone; web app via npm install && npm run dev; agents app via Python venv, pip install -r requirements.txt, uvicorn app.main:app --reload. Requires Confluent Cloud, Azure OpenAI API key, MongoDB
- Model providers: OpenAI, Azure OpenAI
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [thefalc/multi-agent-ai-sdr-flink-orchestrator](../../repos/thefalc/multi-agent-ai-sdr-flink-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Demo app for event-driven multi-agent Sales Development Representative (SDR) workflow. Uses Apache Flink SQL with external LLM model inference as the orchestrator (rather than a traditional agent framework). 5 agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, Send Email. Event-driven architecture using Confluent Cloud/Kafka. Examples for both Autogen and LangGraph. Only 9 commits, low activity. NOTE: This is a ...

(captured site page body (agents/multi-agent-ai-sdr-flink-orchestrator.md), not a verified repo-code finding)
The repository demonstrates an architectural idea rather than a product: using Apache Flink SQL, running on Confluent Cloud, as the orchestrator of a multi-agent sales workflow instead of a conventional agent framework. Five agents — lead ingestion, lead scoring, active outreach, nurture campaigns, and email sending — process leads as events on Kafka topics, with a machine-learning router model deciding which agent handles each message; Next.js handles lead capture and MongoDB stores state, while Python agent services expose the LLM logic. Parallel implementations under autogen-example and langgraph-example show the same workflow in two agent frameworks. As a sales automation demo it has nothing to do with coding agents — no code is generated or modified — and its nine commits and lack of releases mark it as a personal demo accompanying the author's write-ups. Its value is as a reference for event-driven multi-agent orchestration rather than as an installable harness.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/multi-agent-ai-sdr-flink-orchestrator.md)
