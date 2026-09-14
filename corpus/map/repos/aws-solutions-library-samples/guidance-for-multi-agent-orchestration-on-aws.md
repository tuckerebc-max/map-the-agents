# aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 092b5d81c5dc @ 80f619fc8f826a70

## Summary (orientation draft, not independently verified)

The repository documents a multi-agent Amazon Bedrock customer-support demo: a React frontend served via CloudFront/WAF/Cognito, an AppSync GraphQL WebSocket streaming layer, a Lambda resolver invoking a Bedrock Supervisor Agent that routes to four specialized sub-agents using Athena SQL action groups and knowledge bases. Evidence is documentation-only; no evaluation or benchmark material appears.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The system uses five agents: a Supervisor Agent plus Order Management, Product Recommendation, Troubleshooting, and Personalization agents. -- evidence: [README.md#L47-L51](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L47-L51)
  - [observation/documented] The runtime chatbot is a React website using a WebSocket API and Lambda functions that call the Amazon Bedrock Converse API and action groups for text-to-SQL against Athena. -- evidence: [README.md#L55-L55](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L55-L55)
- design-choices (2 claim(s)):
  - [observation/documented] Bedrock agent IDs are managed via environment variables dynamically exported from the CDK stack at build time, avoiding hardcoded IDs in source or config files. -- evidence: [README.md#L210-L210](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L210-L210), [README.md#L213-L217](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L213-L217)
  - [observation/documented] The frontend is served from a private S3 bucket via CloudFront with Origin Access Control, protected by a CloudFront-scoped WAF using AWS managed rule sets, with Cognito handling authentication. -- evidence: [README.md#L62-L62](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L62-L62), [README.demo.md#L17-L19](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.demo.md#L17-L19)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves cloning the repo, running npm i, bootstrapping CDK, editing config/project-config.json with the account number, and deploying via the starter-kit CLI options. -- evidence: [README.md#L252-L252](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L252-L252), [README.md#L192-L194](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L192-L194), [README.md#L185-L188](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L185-L188), [README.md#L225-L225](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L225-L225), [README.md#L198-L200](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L198-L200), [README.md#L254-L254](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L254-L254)
  - [observation/documented] Repository development practice: before running the app, the Athena query result location must be manually set to an S3 prefix in the Athena console; the README notes this will be automated in a future revision. -- evidence: [README.md#L265-L269](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L265-L269), [README.md#L257-L258](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L257-L258)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Frontend-backend communication uses AWS AppSync GraphQL subscriptions; chat is sent via a sendChat mutation and responses arrive as onUpdateChat subscription messages with assistant text and trace data. -- evidence: [README-Amplify-WebSocket-Workflow.md#L20-L20](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L20-L20), [README-Amplify-WebSocket-Workflow.md#L78-L90](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L78-L90), [README-Amplify-WebSocket-Workflow.md#L96-L103](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L96-L103)
  - [observation/documented] The GraphQL schema defines Chat and Session models with owner-based auth rules, plus a custom sendChat mutation restricted to Cognito user pools. -- evidence: [README-Amplify-WebSocket-Workflow.md#L198-L202](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L198-L202), [README-Amplify-WebSocket-Workflow.md#L188-L196](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L188-L196), [README-Amplify-WebSocket-Workflow.md#L204-L208](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L204-L208)
- memory-state (1 claim(s)):
  - [observation/documented] Session data is stored in Amazon DynamoDB, and the Personalization Agent maintains a persistent customer profile recalling prior interactions across support sessions. -- evidence: [README.md#L98-L99](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L98-L99), [README.md#L64-L64](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L64-L64)
- orchestration (1 claim(s)):
More evidence: [full detail](guidance-for-multi-agent-orchestration-on-aws.detail.md)

Metadata and full claim list: [full detail](guidance-for-multi-agent-orchestration-on-aws.detail.md)
Human notes ([notes](guidance-for-multi-agent-orchestration-on-aws.notes.md), never overwritten by build)

[Back to map index](../../index.md)
