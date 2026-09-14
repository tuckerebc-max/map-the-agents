---
access: public
aliases: []
claim_ids:
- clm_28ab3c3b9ed2b584111e11bf16067878253ec91a71376953c2b1f665435124f1
- clm_42dfca3119df3e3a7650a56d8d88b7857d6bb675ea435fcafae1f16b1cf797b7
- clm_431feadeb20e4f2b25dce59860e57404d1451dc2bd6695ab70ca0aa28d5a070c
- clm_5986ecd89c16493d8bc68bb0c106e42de1443bb90f505dfc01611c80dacc020c
- clm_61f99d2df2455d24385ff0fbbeeaa1665bbf1e6b721be2ffb5e7bb5dd9e7fe30
- clm_91cad1974df75f0a8c4de6e2c6b9eb2ef8f2be234e48399a93e83c36fac7d400
- clm_d558f25f2d8e013a943d6284825366c7a68e4814f60db513a61a9c8c29e6816b
- clm_d8558b387ac5122e79bd85a00f5cede471de6fa7ae87854d432322dda0f1da74
- clm_ed6f090d67ca6416f7b2c85b208d34f5e45f7a752e7c4733383a34600b6be7e8
maturity: draft
page_id: pg_edf4dff7dc9a5f76a62ccc290df5750f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e776f7df96ca5c0cbd883c327e3affee
title: aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/README.md @
  b48bcb476d08
updated_at: '2026-09-14T03:05:41Z'
---

# aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/README.md @ b48bcb476d08

<!-- rcw:begin owner=source:src_e776f7df96ca5c0cbd883c327e3affee block=evidence -->
- The platform supports extensible tools including command execution, web search, image generation, and external service integration, configurable per agent. [@claim:clm_28ab3c3b9ed2b584111e11bf16067878253ec91a71376953c2b1f665435124f1]
- The default model is Claude Opus 4.8; Claude Fable 5 is selectable but requires the account's Bedrock data retention mode set to provider_data_share in the invocation region. [@claim:clm_42dfca3119df3e3a7650a56d8d88b7857d6bb675ea435fcafae1f16b1cf797b7]
- The agent runs as a Docker container on AgentCore Runtime using the Strands Agents SDK (TypeScript), implemented as an Express server on port 8080. [@claim:clm_431feadeb20e4f2b25dce59860e57404d1451dc2bd6695ab70ca0aa28d5a070c]
- The stack includes a React SPA frontend on CloudFront+S3, Cognito JWT auth, an Express.js API on Lambda/API Gateway, DynamoDB+S3 storage, AppSync Events WebSocket, and EventBridge scheduling. [@claim:clm_5986ecd89c16493d8bc68bb0c106e42de1443bb90f505dfc01611c80dacc020c]
- Real-time streaming is achieved via AppSync Events (WebSocket), and a session-stream-handler Lambda relays DynamoDB Streams to AppSync. [@claim:clm_61f99d2df2455d24385ff0fbbeeaa1665bbf1e6b721be2ffb5e7bb5dd9e7fe30]
- User requests flow from the React frontend through Cognito authentication to AgentCore Runtime, which orchestrates agent execution with tool integration via AgentCore Gateway. [@claim:clm_91cad1974df75f0a8c4de6e2c6b9eb2ef8f2be234e48399a93e83c36fac7d400]
- Agents use AgentCore Memory with both short-term memory (session history) for conversational context and long-term persistent memory enabled. [@claim:clm_d558f25f2d8e013a943d6284825366c7a68e4814f60db513a61a9c8c29e6816b]
- The product is a multi-agent platform for creating, customizing, and sharing AI agents across an organization, built on Amazon Bedrock AgentCore. [@claim:clm_d8558b387ac5122e79bd85a00f5cede471de6fa7ae87854d432322dda0f1da74]
- The application is explicitly not designed for production use; it is a proof-of-concept not intended to support more than a few hundred users. [@claim:clm_ed6f090d67ca6416f7b2c85b208d34f5e45f7a752e7c4733383a34600b6be7e8]
<!-- rcw:end owner=source:src_e776f7df96ca5c0cbd883c327e3affee block=evidence -->

## Researcher notes

