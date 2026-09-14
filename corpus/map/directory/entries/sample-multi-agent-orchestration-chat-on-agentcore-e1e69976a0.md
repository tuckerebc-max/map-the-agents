# sample-multi-agent-orchestration-chat-on-agentcore (`sample-multi-agent-orchestration-chat-on-agentcore`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: aws-samples
- License: MIT-0
- Language: TypeScript
- Interface: install=npm ci; npx -w packages/cdk cdk bootstrap; npm run deploy; requires Node.js 22.12.0+ and AWS CLI
- Model providers: Amazon Bedrock (Anthropic Claude)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [aws-samples/sample-multi-agent-orchestration-chat-on-agentcore](../../repos/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent orchestration chat platform built on Amazon Bedrock AgentCore; enables teams to create, customize, and share AI agents across an organization; includes preset agents (Software Developer, Data Analyst, Physicist); supports event-driven automation, extensible tools, JWT/Cognito auth, persistent memory; proof-of-concept (PoC)

(captured site page body (agents/sample-multi-agent-orchestration-chat-on-agentcore.md), not a verified repo-code finding)
The sample demonstrates how an organization stands up a shared agent workspace on AWS: teams create custom agents, discover and reuse colleagues' agents, and trigger any of them from schedules or GitHub webhooks. Preset agents such as Software Developer and Data Analyst ship with tool access to command execution, web search, and GitHub, and agents persist context through AgentCore's short- and long-term memory. Everything deploys from one repository via CDK — React on CloudFront, Express on Lambda, DynamoDB and S3 storage, AppSync WebSockets for streaming — with Cognito JWTs for access control. The repository is explicit that this is a proof of value for a few hundred users, not production software, and may change without backward compatibility. AWS customers evaluating internal agent platforms are the intended audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sample-multi-agent-orchestration-chat-on-agentcore.md)
