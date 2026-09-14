# aws-samples/sample-multi-agent-orchestration-chat-on-agentcore -- full detail

[Back to orientation](sample-multi-agent-orchestration-chat-on-agentcore.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/c3c4e8e8d4cbc12e.json](../../../wiki/dossiers/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/c3c4e8e8d4cbc12e.json)

## specifications (1 claim(s))

- [observation/documented] The product is a multi-agent platform for creating, customizing, and sharing AI agents across an organization, built on Amazon Bedrock AgentCore. -- evidence: [README.md#L5-L5](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L5-L5), [README.md#L9-L9](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L9-L9) (`clm_d8558b387ac5122e79bd85a00f5cede471de6fa7ae87854d432322dda0f1da74`)

## components (2 claim(s))

- [observation/documented] The stack includes a React SPA frontend on CloudFront+S3, Cognito JWT auth, an Express.js API on Lambda/API Gateway, DynamoDB+S3 storage, AppSync Events WebSocket, and EventBridge scheduling. -- evidence: [README.md#L62-L70](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L62-L70) (`clm_5986ecd89c16493d8bc68bb0c106e42de1443bb90f505dfc01611c80dacc020c`)
- [observation/documented] The agent runs as a Docker container on AgentCore Runtime using the Strands Agents SDK (TypeScript), implemented as an Express server on port 8080. -- evidence: [AGENTS.md#L18-L26](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L18-L26), [AGENTS.md#L54-L61](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L54-L61), [README.md#L72-L72](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L72-L72) (`clm_431feadeb20e4f2b25dce59860e57404d1451dc2bd6695ab70ca0aa28d5a070c`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the repo is an npm-workspaces monorepo of 8 packages using Node.js 22, TypeScript ~5.7, jest/vitest tests, eslint+prettier, and a solution-style tsc build that must run before cdk synth/deploy. -- evidence: [AGENTS.md#L16-L16](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L16-L16), [AGENTS.md#L18-L26](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L18-L26), [AGENTS.md#L39-L44](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L39-L44), [AGENTS.md#L48-L50](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L48-L50) (`clm_10436225c91522b6d72002002493ca0b7f21522a857462ad0d3393858840b1af`)
- [observation/documented] Repository development practice: CI runs secret scanning via detect-secrets through ASH, with test files excluded by globs in .ash/ash.yaml and documented pragma/ignore_paths handling for false positives. -- evidence: [AGENTS.md#L54-L61](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L54-L61) (`clm_ff261e7a169eac0533978874ee0637e9d83797ec57b9a6b4343afaa2282743c8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Real-time streaming is achieved via AppSync Events (WebSocket), and a session-stream-handler Lambda relays DynamoDB Streams to AppSync. -- evidence: [README.md#L62-L70](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L62-L70), [AGENTS.md#L54-L61](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L54-L61), [README.md#L72-L72](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L72-L72) (`clm_61f99d2df2455d24385ff0fbbeeaa1665bbf1e6b721be2ffb5e7bb5dd9e7fe30`)

## memory-state (1 claim(s))

- [observation/documented] Agents use AgentCore Memory with both short-term memory (session history) for conversational context and long-term persistent memory enabled. -- evidence: [README.md#L72-L72](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L72-L72) (`clm_d558f25f2d8e013a943d6284825366c7a68e4814f60db513a61a9c8c29e6816b`)

## orchestration (1 claim(s))

- [observation/documented] User requests flow from the React frontend through Cognito authentication to AgentCore Runtime, which orchestrates agent execution with tool integration via AgentCore Gateway. -- evidence: [README.md#L50-L50](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L50-L50) (`clm_91cad1974df75f0a8c4de6e2c6b9eb2ef8f2be234e48399a93e83c36fac7d400`)

## tools-permissions (1 claim(s))

- [observation/documented] The platform supports extensible tools including command execution, web search, image generation, and external service integration, configurable per agent. -- evidence: [README.md#L13-L36](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L13-L36), [README.md#L40-L46](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L40-L46) (`clm_28ab3c3b9ed2b584111e11bf16067878253ec91a71376953c2b1f665435124f1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The default model is Claude Opus 4.8; Claude Fable 5 is selectable but requires the account's Bedrock data retention mode set to provider_data_share in the invocation region. -- evidence: [README.md#L138-L138](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L138-L138), [README.md#L158-L158](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L158-L158) (`clm_42dfca3119df3e3a7650a56d8d88b7857d6bb675ea435fcafae1f16b1cf797b7`)

## limitations (1 claim(s))

- [observation/documented] The application is explicitly not designed for production use; it is a proof-of-concept not intended to support more than a few hundred users. -- evidence: [README.md#L293-L293](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L293-L293), [README.md#L298-L298](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L298-L298) (`clm_ed6f090d67ca6416f7b2c85b208d34f5e45f7a752e7c4733383a34600b6be7e8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

