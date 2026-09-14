# strands-agents/harness-sdk -- full detail

[Back to orientation](harness-sdk.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/strands-agents/harness-sdk/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/2ada8cfbc7de393b.json](../../../wiki/dossiers/strands-agents/harness-sdk/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/2ada8cfbc7de393b.json)

## specifications (1 claim(s))

- [observation/documented] Strands Agents is an open-source SDK for building and running AI agents in Python and TypeScript, positioned as a replacement for a hand-rolled agent loop that runs in the user's process with no hosted control plane. -- evidence: [README.md#L35-L35](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L35-L35) (`clm_e0599e473447529d8f7f81d8e0075ac5edc80ef89a63fe309fef74685d4b5d1f`)

## components (2 claim(s))

- [observation/documented] The monorepo contains strands-py (Python SDK), strands-ts (TypeScript SDK), site (Astro/Starlight documentation site), and team (governance and cross-SDK process docs including designs/ proposals). -- evidence: [README.md#L37-L37](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L37-L37), [README.md#L39-L44](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L39-L44) (`clm_fa43c72c94be5d058e1fd1403c454b534cd48de3fdb1317a5602006a86dcef5e`)
- [observation/code-inspected] The Python SDK includes an AgentDelegation plugin (auto-registered on every agent) that enforces delegation semantics for tools configured with delegate=True, acting as a no-op when no delegation tools fire. -- evidence: [strands-py/src/strands/agent/_agent_delegation.py#L76-L77](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L76-L77), [strands-py/src/strands/agent/_agent_delegation.py#L1-L1](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L1-L1), [strands-py/src/strands/agent/_agent_delegation.py#L73-L74](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L73-L74), [strands-py/src/strands/agent/_agent_delegation.py#L83-L89](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L83-L89) (`clm_ced4324c96d04c991d28f75a9df6b3e8cc81e9f67d46374b993bf22e9b2ef2d3`)

## design-choices (4 claim(s))

- [observation/documented] The SDK advertises built-in lifecycle controls (turn limits, token budgets, cancellation, stop reasons), tools, structured output, MCP, multi-agent patterns, memory, sessions, model portability, streaming, guardrails, tracing, and evals. -- evidence: [README.md#L35-L35](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L35-L35) (`clm_ae57a5994f8bd2176772555ecdf0981db5d22912e45b959a8abfa1862f9a4947`)
- [observation/code-inspected] Delegation enforces a single-call constraint (a delegation tool must be the only tool called in a turn, otherwise the call is cancelled or an error result is returned), and the agent loop exits via end_turn after a successful delegation whose content becomes the final assistant message. -- evidence: [strands-py/src/strands/agent/_agent_delegation.py#L5-L9](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L5-L9), [strands-py/src/strands/agent/_agent_delegation.py#L217-L217](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L217-L217), [strands-py/src/strands/agent/_agent_delegation.py#L245-L263](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L245-L263), [strands-py/src/strands/agent/_agent_delegation.py#L133-L139](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L133-L139) (`clm_2a06be54291ad8e8f48a45d77c98c1e318aeb3d4daae34bf4cbe4d91e04c33c8`)
- [observation/code-inspected] Delegation is incompatible with stateful models: initialization raises ValueError if a delegate=True tool is registered on a stateful model, and at execution time delegation is skipped and the tool runs normally, because early loop exit would leave unclosed function calls server-side. -- evidence: [strands-py/src/strands/agent/_agent_delegation.py#L235-L243](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L235-L243), [strands-py/src/strands/agent/_agent_delegation.py#L97-L110](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L97-L110) (`clm_76494216b2d9638e21f750b10066da8acd7f6a890011b1feaa16f3cce557a0af`)
- [observation/code-inspected] Delegation end_turn is skipped when the parent agent expects structured output or when the delegation tool result has no meaningful (blank) content. -- evidence: [strands-py/src/strands/agent/_agent_delegation.py#L196-L206](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L196-L206), [strands-py/src/strands/agent/_agent_delegation.py#L208-L215](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L208-L215) (`clm_9580442f7fc4e840858ffa1cd5551b7f22ed7e7273464f6853da9283fae8ad03`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: Python SDK tests and formatting run via hatch test and hatch fmt in strands-py; the TypeScript SDK uses npm ci, npm run build, and npm test; the docs site runs with npm install and npm run dev in site/; git operations are done from the repo root. -- evidence: [README.md#L112-L112](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L112-L112), [README.md#L129-L134](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L129-L134), [README.md#L114-L120](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L114-L120), [README.md#L122-L127](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L122-L127) (`clm_46a8396e4030180a315d9c65774de6117a253a280d6d23af1fbd8521578fbedc`)
- [observation/documented] Repository development practice: contributions are guided by CONTRIBUTING.md covering bug reports, development setup, pull requests, code of conduct, and security issue reporting; doc PRs are welcome alongside code changes. -- evidence: [README.md#L108-L108](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L108-L108), [README.md#L138-L143](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L138-L143) (`clm_7e4f4ea495565e041471b73b7d868344c1a26582855938dd2fa51fd992be0330`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The Python API exposes an Agent class constructed with a tools list and invoked by calling it with a prompt string; the TypeScript API exposes an Agent with an awaitable invoke(prompt) method. -- evidence: [README.md#L69-L71](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L69-L71), [README.md#L87-L88](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L87-L88), [README.md#L73-L75](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L73-L75), [README.md#L90-L93](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L90-L93) (`clm_b075c076ac554db140a78adcf2bd371507ad8240b1d94d004525cb90d964d5d7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The agent loop invokes the model, executes requested tools, feeds results back, and repeats until a final response; tool failures are returned to the model as error results rather than terminating the loop, and conversation history accumulates across iterations with a conversation manager keeping it within the context window. -- evidence: [site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L81-L81](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L81-L81), [site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L87-L87](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L87-L87), [site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L29-L29](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L29-L29), [site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L45-L45](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L45-L45) (`clm_646bd25c7f63e549dce0ac55906b43a46502b798d23189b28a3844207e9c9fd2`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The Python SDK requires Python 3.10+ and is installed via pip as strands-agents (with strands-agents-tools); the TypeScript SDK requires Node.js 22+ and installs as @strands-agents/sdk via npm. -- evidence: [README.md#L65-L67](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L65-L67), [README.md#L63-L63](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L63-L63), [README.md#L83-L85](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L83-L85), [README.md#L81-L81](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L81-L81) (`clm_3a98356aa9a0390d66d4c63dd8d9fa696be1cfbbeef5b30500eb0b712d42d176`)
- [observation/documented] Both SDKs default to the Amazon Bedrock model provider, requiring AWS credentials and model access for Claude Sonnet; other providers such as Anthropic, OpenAI, Gemini, and Ollama are covered in the quickstart. -- evidence: [README.md#L59-L59](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L59-L59) (`clm_4bd8d53a4df2a3ec99c5caa037f41288f05c956b7434d534e7e8e4669fe27945`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

