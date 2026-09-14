# sre (`sre`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: SmythOS
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=npm
- Model providers: OpenAI, Anthropic, Google AI, AWS Bedrock, Groq, Perplexity
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [smythos/sre](../../repos/smythos/sre.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): OS-level cloud-native runtime and SDK for production AI agents ('The Linux of AI Agents'). Unified Resource Abstraction — same API works across all providers (swap providers without changing code). Built-in Candidate/ACL security system. 40+ production-ready components. Run agents via SDK or load .smyth files from visual builder.

(captured site page body (agents/sre.md), not a verified repo-code finding)
SRE (Smyth Runtime Environment) targets the plumbing layer of agent development: the same TypeScript SDK calls abstract resources — storage (Local, S3, GCS, Azure), LLMs (OpenAI, Anthropic, Google AI, Bedrock, Groq, Perplexity), vector databases (Pinecone, Milvus), cache, and secrets vaults — so infrastructure can be swapped per deployment without touching agent logic. Around the kernel sit 40+ components for generation, search, scraping, API calls, and classification, a Candidate/ACL security model with credential vaults, and the ability to run agents from code or from .smyth files exported by the SmythOS visual builder. It installs via npm as an SDK or CLI and runs local, cloud, or edge. Teams building agents that must survive provider and infrastructure changes are the audience, rather than end-user coding sessions.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sre.md)
