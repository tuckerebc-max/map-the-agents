# Ai-Agent-Security (`ai-agent-security`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: SecurityLab-UCD
- License: unknown
- Language: Python
- Interface: install=source ./env.sh && pip install -r requirements.txt && cd HE_data && python HE_data.py && cd ../
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [securitylab-ucd/ai-agent-security](../../repos/securitylab-ucd/ai-agent-security.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Research demo implementing homomorphic encryption as a defense for AI agents, presented at RAIE'25 (ICSE 2025 workshop). Includes SSN agent and HE agent demos showing encryption-based protection of sensitive data. Paper-accompanying research artifact with only 23 commits.

(captured site page body (agents/ai-agent-security.md), not a verified repo-code finding)
Agents that handle sensitive data leak it through prompts and context, and this repository explores one defensive idea: run the agent's reasoning over homomorphically encrypted values so the LLM never sees plaintext. The HE agent demo performs sum or product tasks on encrypted data through OpenAI models, with documented limits (results above 400 fail with the default encryptor) and a known indexing bug; a second demo shows encrypted protection of SSN data. The code accompanies 'Security of AI Agents' (arXiv:2406.08689) presented at the RAIE workshop at ICSE 2025 by UC Davis Security Lab researchers, with sandbox evaluation code maintained in a separate AgentBench fork. Its audience is security researchers evaluating encryption-based agent defenses, not developers choosing a coding tool.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/ai-agent-security.md)
