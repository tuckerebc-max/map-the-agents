# Nl2Iac (`nl2iac`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ramonbgc
- License: unknown
- Language: Python (Streamlit)
- Interface: install=git clone; pip install -r requirements.txt; configure .streamlit/secrets.toml with GCP/OpenAI credentials
- Model providers: Google (Gemini 1.5 Flash), OpenAI (GPT-4o)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [ramonbgc/nl2iac](../../repos/ramonbgc/nl2iac.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): NOTE: Not a coding agent harness. Domain-specific agent that translates natural language to Infrastructure as Code (IaC) deployments with multi-LLM provider support. Early stage (9 commits, 1 star).

(captured site page body (agents/nl2iac.md), not a verified repo-code finding)
nl2iac is a personal experiment converting natural-language requests into Terraform configuration and driving GCP deployments from a Streamlit interface. A configuration toggle switches between Google Gemini and OpenAI models, with optional LangSmith tracing. The pipeline is intentionally narrow: NL input in, Terraform out, applied against a configured GCP project and region. The repository shows nine commits, no releases, and no license file, marking it as a single-author experiment rather than a maintained tool. It demonstrates the NL-to-IaC pattern at toy scale rather than production use.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nl2iac.md)
