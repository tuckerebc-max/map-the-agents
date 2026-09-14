---
access: public
aliases: []
claim_ids:
- clm_011e4b3447c3906f226d37a71154bf42c183830d82e79666c22c749f05db86a1
- clm_0bfb7b9fa279a5d645b2481181c9e23318a782c21f652b2ead36e10e4a984d7f
- clm_4f491900a0c01084876d568fa99068540f4811b9919243833ec551eb93f734bf
- clm_7287e8f4c5c582953f8355f27164dfd12e9feaf1736efc793c0bc3548e555829
- clm_83743b3490a9421e8f382650944a4e1b91b495bebb0f366768beb69120f12831
- clm_8511e23e6a01331aed3af1c66b2bb4ab9a306e4e7f7c1505baac6397f6b37b4c
- clm_8b3c5e8ce29873fcb1847644611009c0104af4633e5cee8fd52bc93a68c86cc0
- clm_d009005c4f2750eff47d27b58bb84141913fda465a84e6fc2e853059f4a0f418
- clm_f26a783b75d186b1cc6cbde785c1c7acf10460c68c1ef2e7c546c4dfba651c89
- clm_f6b8fda0168e8f29e41afefd86ec7b4f64112e182212ee066711a59b69a2ff56
maturity: draft
page_id: pg_251117fdf0095bb9a1fbbb698a285886
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_45f3744283755ba6a6684e820468cd68
title: aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/README.md
  @ 092b5d81c5dc
updated_at: '2026-09-14T03:37:27Z'
---

# aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/README.md @ 092b5d81c5dc

<!-- rcw:begin owner=source:src_45f3744283755ba6a6684e820468cd68 block=evidence -->
- The application requires several Bedrock models to be enabled, including Cohere Embed English V3, Nova Pro/Lite/Micro, Claude Sonnet 3.5 (V1 and V2), Claude 3 Haiku, and Haiku 3.5. [@claim:clm_011e4b3447c3906f226d37a71154bf42c183830d82e79666c22c749f05db86a1]
- The frontend is served from a private S3 bucket via CloudFront with Origin Access Control, protected by a CloudFront-scoped WAF using AWS managed rule sets, with Cognito handling authentication. [@claim:clm_0bfb7b9fa279a5d645b2481181c9e23318a782c21f652b2ead36e10e4a984d7f]
- Session data is stored in Amazon DynamoDB, and the Personalization Agent maintains a persistent customer profile recalling prior interactions across support sessions. [@claim:clm_4f491900a0c01084876d568fa99068540f4811b9919243833ec551eb93f734bf]
- Sub-agents access data through Bedrock Action Groups: Order Management and Personalization execute SQL against Athena tables, while the Troubleshooting Agent relies only on its knowledge base without Action Groups. [@claim:clm_7287e8f4c5c582953f8355f27164dfd12e9feaf1736efc793c0bc3548e555829]
- Repository development practice: setup involves cloning the repo, running npm i, bootstrapping CDK, editing config/project-config.json with the account number, and deploying via the starter-kit CLI options. [@claim:clm_83743b3490a9421e8f382650944a4e1b91b495bebb0f366768beb69120f12831]
- Bedrock agent IDs are managed via environment variables dynamically exported from the CDK stack at build time, avoiding hardcoded IDs in source or config files. [@claim:clm_8511e23e6a01331aed3af1c66b2bb4ab9a306e4e7f7c1505baac6397f6b37b4c]
- Repository development practice: before running the app, the Athena query result location must be manually set to an S3 prefix in the Athena console; the README notes this will be automated in a future revision. [@claim:clm_8b3c5e8ce29873fcb1847644611009c0104af4633e5cee8fd52bc93a68c86cc0]
- The Bedrock Supervisor Agent analyzes user queries for intent, routes them to suitable sub-agents, and maintains conversation context as the central orchestrator. [@claim:clm_d009005c4f2750eff47d27b58bb84141913fda465a84e6fc2e853059f4a0f418]
- The system uses five agents: a Supervisor Agent plus Order Management, Product Recommendation, Troubleshooting, and Personalization agents. [@claim:clm_f26a783b75d186b1cc6cbde785c1c7acf10460c68c1ef2e7c546c4dfba651c89]
- The runtime chatbot is a React website using a WebSocket API and Lambda functions that call the Amazon Bedrock Converse API and action groups for text-to-SQL against Athena. [@claim:clm_f6b8fda0168e8f29e41afefd86ec7b4f64112e182212ee066711a59b69a2ff56]
<!-- rcw:end owner=source:src_45f3744283755ba6a6684e820468cd68 block=evidence -->

## Researcher notes

