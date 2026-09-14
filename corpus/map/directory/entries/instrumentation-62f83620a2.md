# instrumentation (`instrumentation`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: brutusin
- License: Apache-2.0
- Language: Java
- Interface: install=Maven dependency (org.brutusin:instrumentation) from Maven Central, or build fat-jar with Premain-Class and launch via -javaagent JVM flag
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [brutusin/instrumentation](../../repos/brutusin/instrumentation.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An extensible Java agent framework that instruments JVM bytecode at class-loading time, injecting code into methods to notify custom listeners about method start, finish, and error events. README explicitly states it is superseded by https://github.com/ShiftLeftSecurity/bctrace. NOTE: This is a JVM bytecode instrumentation framework, NOT an AI coding agent harness.

(captured site page body (agents/instrumentation.md), not a verified repo-code finding)
brutusin/instrumentation is a Java agent in the JVM sense: loaded via -javaagent with a Premain-Class, it rewrites bytecode at class-loading time using ASM so that registered Interceptors hear about method entry, exit, and thrown errors. The design is deliberately minimal — a JRE 1.5+ dependency and one Maven artifact, org.brutusin:instrumentation, with logging-instrumentation as the worked example. Its README now redirects users to ShiftLeftSecurity/bctrace, a more mature continuation by the same lineage, and the project has been inactive since 2020. It contains no AI, no LLM calls, and no coding-agent features.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/instrumentation.md)
