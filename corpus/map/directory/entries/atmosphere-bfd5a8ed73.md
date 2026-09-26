# atmosphere (`atmosphere`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: Atmosphere
- License: Apache-2.0
- Language: Java
- Interface: platforms=Web; install=brew
- Model providers: OpenAI, Google, Anthropic, Cohere, Ollama, DashScope, local, BYOK
- Feature flags (directory-reported):
  - mcp_support: yes (atmosphere-mcp module; MCP 2026-07-28 spec with Tasks, MCP Apps, OAuth resource server; transports over WebSocket/SSE/gRPC) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [atmosphere/atmosphere](../../repos/atmosphere/atmosphere.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=other, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Real-time engine for AI agents on the JVM with deep-agent defaults (memory, plan, virtual filesystem, sub-agent delegation) and governance/compliance (OWASP Agentic Top 10, EU AI Act, HIPAA) built in.

(captured site page body (agents/atmosphere.md), not a verified repo-code finding)
Atmosphere is a real-time event-driven framework for running AI agents on the JVM, rebuilt on the long-standing Atmosphere real-time project. An @Agent annotation with @Prompt, @Command, and @AiTool annotations defines agent behavior, while an AgentRuntime SPI supports 12 runtime adapters (Spring AI, LangChain4j, Google ADK, Koog, Semantic Kernel, AgentScope, Embabel, Anthropic, Cohere, CrewAI, and others) that can be swapped without rewriting agent code. Token streaming flows from providers like OpenAI, Anthropic, Cohere, and Ollama to clients over WebSocket, SSE, gRPC, and WebTransport, with modules auto-registering browser, MCP, A2A, and AG-UI endpoints. Governance sits on the critical path: policy admission, human-in-the-loop approvals, PII redaction, cost ceilings, and compliance mappings for OWASP Agentic Top 10, EU AI Act, and HIPAA. Java teams building governed, production-grade agent services use it via Maven Central or Spring Boot starter.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/atmosphere.md)
