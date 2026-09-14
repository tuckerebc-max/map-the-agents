# aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws -- full detail

[Back to orientation](guidance-for-multi-agent-orchestration-on-aws.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/058f08e4/32cd7998/092b5d81c5dc9e39162d9a554bdf1642b4036202/80f619fc8f826a70.json](../../../wiki/dossiers/058f08e4/32cd7998/092b5d81c5dc9e39162d9a554bdf1642b4036202/80f619fc8f826a70.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The system uses five agents: a Supervisor Agent plus Order Management, Product Recommendation, Troubleshooting, and Personalization agents. -- evidence: [README.md#L47-L51](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L47-L51) (`clm_f26a783b75d186b1cc6cbde785c1c7acf10460c68c1ef2e7c546c4dfba651c89`)
- [observation/documented] The runtime chatbot is a React website using a WebSocket API and Lambda functions that call the Amazon Bedrock Converse API and action groups for text-to-SQL against Athena. -- evidence: [README.md#L55-L55](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L55-L55) (`clm_f6b8fda0168e8f29e41afefd86ec7b4f64112e182212ee066711a59b69a2ff56`)

## design-choices (2 claim(s))

- [observation/documented] Bedrock agent IDs are managed via environment variables dynamically exported from the CDK stack at build time, avoiding hardcoded IDs in source or config files. -- evidence: [README.md#L210-L210](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L210-L210), [README.md#L213-L217](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L213-L217) (`clm_8511e23e6a01331aed3af1c66b2bb4ab9a306e4e7f7c1505baac6397f6b37b4c`)
- [observation/documented] The frontend is served from a private S3 bucket via CloudFront with Origin Access Control, protected by a CloudFront-scoped WAF using AWS managed rule sets, with Cognito handling authentication. -- evidence: [README.md#L62-L62](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L62-L62), [README.demo.md#L17-L19](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.demo.md#L17-L19) (`clm_0bfb7b9fa279a5d645b2481181c9e23318a782c21f652b2ead36e10e4a984d7f`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup involves cloning the repo, running npm i, bootstrapping CDK, editing config/project-config.json with the account number, and deploying via the starter-kit CLI options. -- evidence: [README.md#L252-L252](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L252-L252), [README.md#L192-L194](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L192-L194), [README.md#L185-L188](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L185-L188), [README.md#L225-L225](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L225-L225), [README.md#L198-L200](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L198-L200), [README.md#L254-L254](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L254-L254) (`clm_83743b3490a9421e8f382650944a4e1b91b495bebb0f366768beb69120f12831`)
- [observation/documented] Repository development practice: before running the app, the Athena query result location must be manually set to an S3 prefix in the Athena console; the README notes this will be automated in a future revision. -- evidence: [README.md#L265-L269](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L265-L269), [README.md#L257-L258](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L257-L258) (`clm_8b3c5e8ce29873fcb1847644611009c0104af4633e5cee8fd52bc93a68c86cc0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Frontend-backend communication uses AWS AppSync GraphQL subscriptions; chat is sent via a sendChat mutation and responses arrive as onUpdateChat subscription messages with assistant text and trace data. -- evidence: [README-Amplify-WebSocket-Workflow.md#L20-L20](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L20-L20), [README-Amplify-WebSocket-Workflow.md#L78-L90](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L78-L90), [README-Amplify-WebSocket-Workflow.md#L96-L103](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L96-L103) (`clm_f5a1d32eae9a403a5524b02fee998ded80d910cb262dc89ce7aefec68a927ce2`)
- [observation/documented] The GraphQL schema defines Chat and Session models with owner-based auth rules, plus a custom sendChat mutation restricted to Cognito user pools. -- evidence: [README-Amplify-WebSocket-Workflow.md#L198-L202](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L198-L202), [README-Amplify-WebSocket-Workflow.md#L188-L196](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L188-L196), [README-Amplify-WebSocket-Workflow.md#L204-L208](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README-Amplify-WebSocket-Workflow.md#L204-L208) (`clm_3b005c62cdff2c918ddb4511f25ce9ebd1038d455eb7d1debd2b97ee0a29a45f`)

## memory-state (1 claim(s))

- [observation/documented] Session data is stored in Amazon DynamoDB, and the Personalization Agent maintains a persistent customer profile recalling prior interactions across support sessions. -- evidence: [README.md#L98-L99](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L98-L99), [README.md#L64-L64](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L64-L64) (`clm_4f491900a0c01084876d568fa99068540f4811b9919243833ec551eb93f734bf`)

## orchestration (1 claim(s))

- [observation/documented] The Bedrock Supervisor Agent analyzes user queries for intent, routes them to suitable sub-agents, and maintains conversation context as the central orchestrator. -- evidence: [README.md#L68-L68](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L68-L68) (`clm_d009005c4f2750eff47d27b58bb84141913fda465a84e6fc2e853059f4a0f418`)

## tools-permissions (1 claim(s))

- [observation/documented] Sub-agents access data through Bedrock Action Groups: Order Management and Personalization execute SQL against Athena tables, while the Troubleshooting Agent relies only on its knowledge base without Action Groups. -- evidence: [README.md#L74-L74](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L74-L74), [README.md#L76-L76](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L76-L76), [README.md#L70-L70](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L70-L70) (`clm_7287e8f4c5c582953f8355f27164dfd12e9feaf1736efc793c0bc3548e555829`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The application requires several Bedrock models to be enabled, including Cohere Embed English V3, Nova Pro/Lite/Micro, Claude Sonnet 3.5 (V1 and V2), Claude 3 Haiku, and Haiku 3.5. -- evidence: [README.md#L145-L153](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/blob/092b5d81c5dc9e39162d9a554bdf1642b4036202/README.md#L145-L153) (`clm_011e4b3447c3906f226d37a71154bf42c183830d82e79666c22c749f05db86a1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

