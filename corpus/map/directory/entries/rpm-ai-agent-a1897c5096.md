# Rpm-Ai-Agent (`rpm-ai-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: teldridge11
- License: unknown
- Language: Python
- Interface: install=git clone https://github.com/teldridge11/RPM-AI-Agent.git; run python Test.py from Agent directory
- Model providers: none (three-layer rule-based pattern matcher; no LLM involved)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [teldridge11/rpm-ai-agent](../../repos/teldridge11/rpm-ai-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Three-layered knowledge-based agent mimicking human reasoning for Raven's Progressive Matrices; 91.7% accuracy on basic 2x2 problems, 85% on unseen problem sets. Not LLM-based - custom pattern-matching architecture.

(captured site page body (agents/rpm-ai-agent.md), not a verified repo-code finding)
The repository documents a coursework- or research-scale exploration of whether structured, human-like reasoning stages can match learned models on Raven's Progressive Matrices, a standard test of abstract visual reasoning. Each problem image is decomposed, candidate answers are filtered against the patterns induced from the prompt matrix, and remaining options are ranked by attribute similarity, all with Pillow-based image processing in Python rather than any neural component. Reported accuracy — strong on basic 2x2 items, weak on challenge sets — is included with paper PDFs in the repo. It has no license file, no issues or forks, and twenty-two commits, marking it as an inactive personal artifact. Its relevance to this census is as a namesake only: nothing here touches coding agents.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rpm-ai-agent.md)
