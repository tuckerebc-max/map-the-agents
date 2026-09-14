# aws-samples/sample-multi-agent-orchestration-chat-on-agentcore

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b48bcb476d08 @ c3c4e8e8d4cbc12e

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is a multi-agent platform for creating, customizing, and sharing AI agents across an organization, built on Amazon Bedrock AgentCore. The stack includes a React SPA frontend on CloudFront+S3, Cognito JWT auth, an Express.js API on Lambda/API Gateway, DynamoDB+S3 storage, AppSync Events WebSocket, and EventBridge scheduling.

## Source coverage

Source coverage (partial): 3 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is a multi-agent platform for creating, customizing, and sharing AI agents across an organization, built on Amazon Bedrock AgentCore. -- evidence: [README.md#L5-L5](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L5-L5), [README.md#L9-L9](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L9-L9)
- components (2 claim(s)):
  - [observation/documented] The stack includes a React SPA frontend on CloudFront+S3, Cognito JWT auth, an Express.js API on Lambda/API Gateway, DynamoDB+S3 storage, AppSync Events WebSocket, and EventBridge scheduling. -- evidence: [README.md#L62-L70](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L62-L70)
  - [observation/documented] The agent runs as a Docker container on AgentCore Runtime using the Strands Agents SDK (TypeScript), implemented as an Express server on port 8080. -- evidence: [AGENTS.md#L18-L26](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L18-L26), [AGENTS.md#L54-L61](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L54-L61), [README.md#L72-L72](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L72-L72)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the repo is an npm-workspaces monorepo of 8 packages using Node.js 22, TypeScript ~5.7, jest/vitest tests, eslint+prettier, and a solution-style tsc build that must run before cdk synth/deploy. -- evidence: [AGENTS.md#L16-L16](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L16-L16), [AGENTS.md#L18-L26](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L18-L26), [AGENTS.md#L39-L44](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L39-L44), [AGENTS.md#L48-L50](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L48-L50)
  - [observation/documented] Repository development practice: CI runs secret scanning via detect-secrets through ASH, with test files excluded by globs in .ash/ash.yaml and documented pragma/ignore_paths handling for false positives. -- evidence: [AGENTS.md#L54-L61](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L54-L61)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Real-time streaming is achieved via AppSync Events (WebSocket), and a session-stream-handler Lambda relays DynamoDB Streams to AppSync. -- evidence: [README.md#L62-L70](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L62-L70), [AGENTS.md#L54-L61](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/AGENTS.md#L54-L61), [README.md#L72-L72](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L72-L72)
- memory-state (1 claim(s)):
  - [observation/documented] Agents use AgentCore Memory with both short-term memory (session history) for conversational context and long-term persistent memory enabled. -- evidence: [README.md#L72-L72](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L72-L72)
- orchestration (1 claim(s)):
  - [observation/documented] User requests flow from the React frontend through Cognito authentication to AgentCore Runtime, which orchestrates agent execution with tool integration via AgentCore Gateway. -- evidence: [README.md#L50-L50](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L50-L50)
- tools-permissions (1 claim(s)):
  - [observation/documented] The platform supports extensible tools including command execution, web search, image generation, and external service integration, configurable per agent. -- evidence: [README.md#L13-L36](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L13-L36), [README.md#L40-L46](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L40-L46)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The default model is Claude Opus 4.8; Claude Fable 5 is selectable but requires the account's Bedrock data retention mode set to provider_data_share in the invocation region. -- evidence: [README.md#L138-L138](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L138-L138), [README.md#L158-L158](https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/blob/b48bcb476d08383f9d9b65a5df046555d7ba0fbb/README.md#L158-L158)
More evidence: [full detail](sample-multi-agent-orchestration-chat-on-agentcore.detail.md)

Metadata and full claim list: [full detail](sample-multi-agent-orchestration-chat-on-agentcore.detail.md)
Human notes ([notes](sample-multi-agent-orchestration-chat-on-agentcore.notes.md), never overwritten by build)

[Back to map index](../../index.md)
