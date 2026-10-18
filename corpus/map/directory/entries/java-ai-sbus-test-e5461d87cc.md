# Java-Ai-Sbus-Test (`java-ai-sbus-test`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: abhikt48
- License: unknown
- Language: Java
- Interface: install=Download applicationinsights-agent-3.5.2.jar, run with -javaagent VM argument
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [abhikt48/java-ai-sbus-test](../../repos/abhikt48/java-ai-sbus-test.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A minimal test case for integrating Azure Application Insights codeless agent with Azure ServiceBus dependency tracking, using the Java agent for telemetry.

(captured site page body (agents/java-ai-sbus-test.md), not a verified repo-code finding)
The repository exists to confirm that the applicationinsights-agent-3.5.2.jar captures Azure Service Bus dependency telemetry correctly. The README walks through dropping the agent JAR into an agent/ folder, pointing applicationinsights.json at an App Insights connection string, and launching the sample with -javaagent to watch the dependency tree appear in the portal. There is no AI coding functionality, no LLM, and no tool loop; the name simply collides with agent-harness terminology. It is retained in the census as a categorization error rather than a harness.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/java-ai-sbus-test.md)
