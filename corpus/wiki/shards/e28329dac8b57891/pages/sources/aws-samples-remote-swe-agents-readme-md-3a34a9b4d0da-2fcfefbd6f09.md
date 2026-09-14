---
access: public
aliases: []
claim_ids:
- clm_0d11f6f74da7bbbb3995bc56eb90c6fd330d5f0e18fcbca9d4e6b3083d48f098
- clm_0e1c3fd2490d7b7f9b21159e405c2b0b861730f73d4b947691a9c09483e7954c
- clm_1187204a34b2752d027d42963473c6aad209cd06f58e637817e6bd13ae48cb2d
- clm_1b1c8cf5102e89e305faebae96ead27abcf0c9b42dc579aa890159cf5be85c1a
- clm_41240c5e4120c4c4e8c5078975b471e78af5d15ebf26684fabd62c7012d1cff9
- clm_5dfc841670e55ddaea8032482e841f71b1ffd9decfb4ea06fdfd1fc576feef3f
- clm_7d2d0760ad6e7d0b6301cb3a6433c73114196785334155cc0e2ca987ac87bcf9
- clm_9d3cb2c3b9a0aba78b66e321ba26a93bbd4b4ea2274dbbd31dc98179c7c3114a
- clm_a1abfdd25798982ab7a7f23dae9e1f4cf2a7244df937ddb2e885023e1676fdac
- clm_b4d655ac512d332f1d365933375bdb1439a9e3d25ee1baf5ee628523d42c18f5
- clm_c5717364b48e2045cecc46b1d3487ed184b7bd097f5b53dea33c5569e1cd71c7
maturity: draft
page_id: pg_bc2be25e8b585f84bb512fcfefbd6f09
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_13e91e8555f05c699f77d1e8ce2b7c6b
title: aws-samples/remote-swe-agents/README.md @ 3a34a9b4d0da
updated_at: '2026-09-14T01:36:38Z'
---

# aws-samples/remote-swe-agents/README.md @ 3a34a9b4d0da

<!-- rcw:begin owner=source:src_13e91e8555f05c699f77d1e8ce2b7c6b block=evidence -->
- Users can interact with the deployed system through a web dashboard, a Slack bot, RESTful API endpoints, and a GitHub Actions integration that triggers agents from repository events. [@claim:clm_0d11f6f74da7bbbb3995bc56eb90c6fd330d5f0e18fcbca9d4e6b3083d48f098]
- When using the GitHub App option, the system is limited to repositories under a single organization (app installation), per the README note. [@claim:clm_0e1c3fd2490d7b7f9b21159e405c2b0b861730f73d4b947691a9c09483e7954c]
- Slack messages reach an API Gateway webhook feeding a Lambda, which publishes to AppSync Events and stores history in DynamoDB; a Worker Manager provisions an EC2 instance plus EBS volume per new thread, and workers subscribe back to AppSync for messages. [@claim:clm_1187204a34b2752d027d42963473c6aad209cd06f58e637817e6bd13ae48cb2d]
- The agent acts as an MCP client; integrations are configured by editing packages/worker/mcp.json and redeploying, after which new agents can use MCP servers as tools. [@claim:clm_1b1c8cf5102e89e305faebae96ead27abcf0c9b42dc579aa890159cf5be85c1a]
- Deployment prerequisites are Node.js 22+, npm 9+, AWS CLI, an IAM profile with appropriate permissions, and Docker. [@claim:clm_41240c5e4120c4c4e8c5078975b471e78af5d15ebf26684fabd62c7012d1cff9]
- Access controls differ by channel: Slack access can be restricted via SLACK_ADMIN_USER_ID_LIST, Cognito self-sign-up is disabled by default with equal permissions for account holders, REST API access requires knowing an API key, and any repository collaborator can invoke the GitHub Action. [@claim:clm_5dfc841670e55ddaea8032482e841f71b1ffd9decfb4ea06fdfd1fc576feef3f]
- The agent runs on AWS Bedrock models; the cost table assumes Claude Sonnet 3.7 usage, and a web UI setting selects the default foundation model for new sessions. [@claim:clm_7d2d0760ad6e7d0b6301cb3a6433c73114196785334155cc0e2ca987ac87bcf9]
- Worker instances receive minimal IAM policies by default (logging, self-termination, S3 read), and extra permissions can be attached via the WORKER_ADDITIONAL_POLICIES environment variable. [@claim:clm_9d3cb2c3b9a0aba78b66e321ba26a93bbd4b4ea2274dbbd31dc98179c7c3114a]
- GitHub integration supports either a personal access token stored in SSM (simpler, single-user) or a GitHub App (recommended for teams), and with the App option only repositories under a single organization installation can be used. [@claim:clm_a1abfdd25798982ab7a7f23dae9e1f4cf2a7244df937ddb2e885023e1676fdac]
- The README showcases example agent sessions and a search link to public pull requests authored by the agent, suggesting demonstration-based evidence of capability rather than a formal benchmark harness. [@claim:clm_b4d655ac512d332f1d365933375bdb1439a9e3d25ee1baf5ee628523d42c18f5]
- The system is designed as a single-tenant deployment, one per tenant, relying on a pay-as-you-go model so multiple deployments carry minimal infrastructure overhead. [@claim:clm_c5717364b48e2045cecc46b1d3487ed184b7bd097f5b53dea33c5569e1cd71c7]
<!-- rcw:end owner=source:src_13e91e8555f05c699f77d1e8ce2b7c6b block=evidence -->

## Researcher notes

