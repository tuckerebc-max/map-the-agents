# guidance-for-multi-agent-orchestration-on-aws (`guidance-for-multi-agent-orchestration-on-aws`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: aws-solutions-library-samples
- License: Apache-2.0
- Language: TypeScript
- Interface: install=git clone, npm i, cdk bootstrap, authenticate to ECR, configure project-config.json, npm run develop
- Model providers: Amazon Bedrock (Anthropic Claude, Amazon Nova, Cohere)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws](../../repos/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Reference implementation for multi-agent collaboration on Amazon Bedrock using a Supervisor Agent as central orchestrator routing queries to specialized sub-agents (Order Management, Product Recommendation, Troubleshooting, Personalization), each with its own knowledge base and action groups (text-2-SQL via Athena, vector search on S3).

(captured site page body (agents/guidance-for-multi-agent-orchestration-on-aws.md), not a verified repo-code finding)
This repository is an AWS Solutions Library guidance deployment demonstrating Amazon Bedrock's multi-agent collaboration feature in a customer-support scenario. A supervisor agent coordinates five specialized sub-agents — order management via text-to-SQL over Athena, product recommendation, troubleshooting through a knowledge base, and personalization — behind a React web app served from S3/CloudFront with Cognito authentication and a WebSocket API on API Gateway. The CDK project provisions the full stack and documents the cost profile, roughly $606–761 per month at 100,000 requests driven mostly by Bedrock Knowledge Bases. Its purpose is architectural demonstration for teams building Bedrock-based agent systems in retail support contexts, not software development, and it remains available as a maintained sample.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/guidance-for-multi-agent-orchestration-on-aws.md)
