# codeshell-vscode (`codeshell-vscode`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: WisdomShell
- License: Apache-2.0
- Language: TypeScript
- Interface: install=vscode
- Model providers: CodeShell
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [wisdomshell/codeshell-vscode](../../repos/wisdomshell/codeshell-vscode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Intelligent coding assistant for VSCode built on the CodeShell LLM; supports code completion, code explanation/optimization/cleanup, comment/unit test generation, performance/security checks, and multi-turn chat with session history

(captured site page body (agents/codeshell-vscode.md), not a verified repo-code finding)
codeshell-vscode is the VS Code client for WisdomShell's CodeShell model family, built for developers who want a coding assistant fully inside their own infrastructure. The extension provides auto-triggered inline completion (configurable delay, Tab to accept), right-click code actions that explain, optimize, or clean up code, generate comments and unit tests, and check performance and security issues, plus multi-turn chat with session history and code-block insertion. It requires a self-hosted CodeShell backend: either llama.cpp serving the 4-bit quantized chat GGUF on CPU, or Text Generation Inference running CodeShell-7B or CodeShell-7B-Chat on GPU. Development stopped in mid-2024; the repository has 55 commits, no releases, and 23 open issues without responses, and documentation is primarily in Chinese.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/codeshell-vscode.md)
