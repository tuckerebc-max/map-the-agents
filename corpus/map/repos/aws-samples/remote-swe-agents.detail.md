# aws-samples/remote-swe-agents -- full detail

[Back to orientation](remote-swe-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aws-samples/remote-swe-agents/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/a5513177dfea5d49.json](../../../wiki/dossiers/aws-samples/remote-swe-agents/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/a5513177dfea5d49.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is organized into five main parts: a CDK infrastructure directory, an agent-core shared module, a Slack Bolt app, a worker package containing the AI agent implementation and tool suite, and a Next.js webapp. -- evidence: [AmazonQ.md#L26-L28](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L26-L28), [AmazonQ.md#L9-L11](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L9-L11), [AmazonQ.md#L13-L24](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L13-L24), [AmazonQ.md#L30-L31](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L30-L31) (`clm_dd4be6fd6c0a5cb88bf97a6edd6cfdbd3588505cc70fef926ad6bb25e23c801d`)

## design-choices (2 claim(s))

- [observation/documented] The system is designed as a single-tenant deployment, one per tenant, relying on a pay-as-you-go model so multiple deployments carry minimal infrastructure overhead. -- evidence: [README.md#L329-L329](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L329-L329), [README.md#L327-L327](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L327-L327) (`clm_c5717364b48e2045cecc46b1d3487ed184b7bd097f5b53dea33c5569e1cd71c7`)
- [observation/documented] GitHub integration supports either a personal access token stored in SSM (simpler, single-user) or a GitHub App (recommended for teams), and with the App option only repositories under a single organization installation can be used. -- evidence: [README.md#L208-L209](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L208-L209), [README.md#L153-L154](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L153-L154) (`clm_a1abfdd25798982ab7a7f23dae9e1f4cf2a7244df937ddb2e885023e1676fdac`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AmazonQ.md prescribes contributor conventions including TypeScript, Prettier formatting, avoiding comments unless necessary, using Next.js server actions with Zod schemas and authActionClient, and building agent-core before other packages. -- evidence: [AmazonQ.md#L179-L184](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L179-L184), [AmazonQ.md#L167-L175](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L167-L175), [AmazonQ.md#L203-L203](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L203-L203) (`clm_05169d21606bea3932ce1d8b11cf57e2da45a796dad3b0d84848d6ef8768b0fb`)
- [observation/documented] Repository development practice: the documented development flow is to create a branch, implement and test, run format and type checks, open a PR with an English title and description, and request review once CI passes. -- evidence: [AmazonQ.md#L244-L248](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L244-L248) (`clm_059a883de673835b4c954621f5e5b33618215d2cfcb75ee46ef518fe64ab7c1e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Users can interact with the deployed system through a web dashboard, a Slack bot, RESTful API endpoints, and a GitHub Actions integration that triggers agents from repository events. -- evidence: [README.md#L296-L300](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L296-L300), [README.md#L307-L310](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L307-L310), [README.md#L312-L315](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L312-L315), [README.md#L302-L305](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L302-L305), [README.md#L321-L321](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L321-L321) (`clm_0d11f6f74da7bbbb3995bc56eb90c6fd330d5f0e18fcbca9d4e6b3083d48f098`)
- [observation/documented] The agent acts as an MCP client; integrations are configured by editing packages/worker/mcp.json and redeploying, after which new agents can use MCP servers as tools. -- evidence: [README.md#L377-L377](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L377-L377), [README.md#L363-L363](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L363-L363) (`clm_1b1c8cf5102e89e305faebae96ead27abcf0c9b42dc579aa890159cf5be85c1a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Slack messages reach an API Gateway webhook feeding a Lambda, which publishes to AppSync Events and stores history in DynamoDB; a Worker Manager provisions an EC2 instance plus EBS volume per new thread, and workers subscribe back to AppSync for messages. -- evidence: [README.md#L391-L394](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L391-L394), [README.md#L383-L385](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L383-L385), [README.md#L396-L399](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L396-L399), [README.md#L387-L389](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L387-L389) (`clm_1187204a34b2752d027d42963473c6aad209cd06f58e637817e6bd13ae48cb2d`)

## tools-permissions (2 claim(s))

- [observation/documented] Worker instances receive minimal IAM policies by default (logging, self-termination, S3 read), and extra permissions can be attached via the WORKER_ADDITIONAL_POLICIES environment variable. -- evidence: [README.md#L413-L416](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L413-L416), [README.md#L97-L97](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L97-L97), [README.md#L99-L101](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L99-L101) (`clm_9d3cb2c3b9a0aba78b66e321ba26a93bbd4b4ea2274dbbd31dc98179c7c3114a`)
- [observation/documented] Access controls differ by channel: Slack access can be restricted via SLACK_ADMIN_USER_ID_LIST, Cognito self-sign-up is disabled by default with equal permissions for account holders, REST API access requires knowing an API key, and any repository collaborator can invoke the GitHub Action. -- evidence: [README.md#L333-L336](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L333-L336) (`clm_5dfc841670e55ddaea8032482e841f71b1ffd9decfb4ea06fdfd1fc576feef3f`)

## evaluation (1 claim(s))

- [inference/documented] The README showcases example agent sessions and a search link to public pull requests authored by the agent, suggesting demonstration-based evidence of capability rather than a formal benchmark harness. -- evidence: [README.md#L39-L39](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L39-L39), [README.md#L32-L35](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L32-L35), [README.md#L30-L30](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L30-L30) (`clm_b4d655ac512d332f1d365933375bdb1439a9e3d25ee1baf5ee628523d42c18f5`)

## dependencies (2 claim(s))

- [observation/documented] Deployment prerequisites are Node.js 22+, npm 9+, AWS CLI, an IAM profile with appropriate permissions, and Docker. -- evidence: [README.md#L47-L51](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L47-L51) (`clm_41240c5e4120c4c4e8c5078975b471e78af5d15ebf26684fabd62c7012d1cff9`)
- [observation/documented] The agent runs on AWS Bedrock models; the cost table assumes Claude Sonnet 3.7 usage, and a web UI setting selects the default foundation model for new sessions. -- evidence: [README.md#L355-L355](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L355-L355), [README.md#L438-L453](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L438-L453) (`clm_7d2d0760ad6e7d0b6301cb3a6433c73114196785334155cc0e2ca987ac87bcf9`)

## limitations (1 claim(s))

- [observation/documented] When using the GitHub App option, the system is limited to repositories under a single organization (app installation), per the README note. -- evidence: [README.md#L208-L209](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L208-L209) (`clm_0e1c3fd2490d7b7f9b21159e405c2b0b861730f73d4b947691a9c09483e7954c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

