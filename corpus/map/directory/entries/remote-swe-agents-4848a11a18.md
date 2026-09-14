# remote-swe-agents (`remote-swe-agents`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aws-samples
- License: MIT-0
- Language: TypeScript
- Interface: platforms=Autonomous, Web; install=git clone + cd cdk + npm ci + npx cdk bootstrap + npx cdk deploy --all; or one-click AWS Sample deployment
- Model providers: AWS Bedrock
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [aws-samples/remote-swe-agents](../../repos/aws-samples/remote-swe-agents.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted, fully open-source autonomous SWE agent on AWS serverless infrastructure — offers a Devin/OpenAI Codex/Google Jules-like experience with no upfront or fixed costs (~$0 when idle). Features web UI, Slack bot, REST API, GitHub Actions integration, per-session isolated EC2 worker VMs, MCP client support, and pay-as-you-go pricing.

(captured site page body (agents/remote-swe-agents.md), not a verified repo-code finding)
The project exists for teams that want the cloud-agent workflow — delegate a task, get a pull request — without sending code to a hosted service or paying for idle capacity. Messages arrive through Slack or a REST API, flow via AppSync Events into DynamoDB, and a Worker Manager boots an isolated EC2 instance per session that clones the target repository, works with Bedrock models, and pushes branches or pull requests. MCP servers configured through mcp.json extend the agent's tools, and a Next.js dashboard adds session monitoring, cost analytics, and API-key management. Security is treated as a first-class concern: single-tenant deployments, least-privilege IAM with optional egress filtering, and Cognito-gated access. It fits AWS-centric teams and OSS maintainers who need cheap, isolated background agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/remote-swe-agents.md)
