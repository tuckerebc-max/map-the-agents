# aws-samples/remote-swe-agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3a34a9b4d0da @ a5513177dfea5d49

## Summary (orientation draft, not independently verified)

README and AmazonQ.md describe a self-hosted, AWS-serverless autonomous software development agent deployable via CDK, with web, Slack, REST API, and GitHub Actions interfaces, and a worker architecture on EC2. Most evidence is documentation; contributor coding conventions appear in AmazonQ.md. Evidence coverage: 154 of 157 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is organized into five main parts: a CDK infrastructure directory, an agent-core shared module, a Slack Bolt app, a worker package containing the AI agent implementation and tool suite, and a Next.js webapp. -- evidence: [AmazonQ.md#L26-L28](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L26-L28), [AmazonQ.md#L9-L11](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L9-L11), [AmazonQ.md#L13-L24](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L13-L24), [AmazonQ.md#L30-L31](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L30-L31)
- design-choices (2 claim(s)):
  - [observation/documented] The system is designed as a single-tenant deployment, one per tenant, relying on a pay-as-you-go model so multiple deployments carry minimal infrastructure overhead. -- evidence: [README.md#L329-L329](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L329-L329), [README.md#L327-L327](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L327-L327)
  - [observation/documented] GitHub integration supports either a personal access token stored in SSM (simpler, single-user) or a GitHub App (recommended for teams), and with the App option only repositories under a single organization installation can be used. -- evidence: [README.md#L208-L209](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L208-L209), [README.md#L153-L154](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L153-L154)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AmazonQ.md prescribes contributor conventions including TypeScript, Prettier formatting, avoiding comments unless necessary, using Next.js server actions with Zod schemas and authActionClient, and building agent-core before other packages. -- evidence: [AmazonQ.md#L179-L184](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L179-L184), [AmazonQ.md#L167-L175](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L167-L175), [AmazonQ.md#L203-L203](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L203-L203)
  - [observation/documented] Repository development practice: the documented development flow is to create a branch, implement and test, run format and type checks, open a PR with an English title and description, and request review once CI passes. -- evidence: [AmazonQ.md#L244-L248](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/AmazonQ.md#L244-L248)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Users can interact with the deployed system through a web dashboard, a Slack bot, RESTful API endpoints, and a GitHub Actions integration that triggers agents from repository events. -- evidence: [README.md#L296-L300](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L296-L300), [README.md#L307-L310](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L307-L310), [README.md#L312-L315](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L312-L315), [README.md#L302-L305](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L302-L305), [README.md#L321-L321](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L321-L321)
  - [observation/documented] The agent acts as an MCP client; integrations are configured by editing packages/worker/mcp.json and redeploying, after which new agents can use MCP servers as tools. -- evidence: [README.md#L377-L377](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L377-L377), [README.md#L363-L363](https://github.com/aws-samples/remote-swe-agents/blob/3a34a9b4d0dab1cb09dc41c292990d7e5ae7259b/README.md#L363-L363)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
More evidence: [full detail](remote-swe-agents.detail.md)

Metadata and full claim list: [full detail](remote-swe-agents.detail.md)
Human notes ([notes](remote-swe-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
