# browser-operator-core (`browser-operator-core`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: BrowserOperator
- License: BSD-3-Clause
- Language: C++, JavaScript, TypeScript
- Interface: platforms=Web; install=Download binaries from GitHub Releases (macOS 10.15+, Windows 10 64-bit+)
- Model providers: OpenRouter, OpenAI, Groq, LiteLLM (Ollama)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [browseroperator/browser-operator-core](../../repos/browseroperator/browser-operator-core.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source, privacy-focused AI browser running locally on a Chromium fork with a multi-agent platform for autonomous web automation. All processing happens locally; supports complete offline operation via Ollama. Compatible with 100+ AI models. Open-source alternative to ChatGPT Atlas, Perplexity Comet, Dia, and Microsoft Copilot Edge Browser.

(captured site page body (agents/browser-operator-core.md), not a verified repo-code finding)
browser-operator-core is an open-source AI browser built as a fork of Chromium (28,000+ commits on its main branch), embedding a multi-agent automation platform directly into the browser rather than bolting it on through an extension or Playwright layer. Agents coordinate to complete research, shopping, and business-automation tasks — literature reviews, price tracking, lead generation, compliance audits — using computer-use-style interaction with pages. Model backends are pluggable across OpenRouter, OpenAI, Groq, and LiteLLM-proxied Ollama, so the whole stack can run offline with local models; MCP support allows connecting external tool servers. The project positions itself as an open alternative to ChatGPT Atlas, Perplexity Comet, Dia, and Microsoft's Copilot-bundled Edge, with privacy as the selling point: all inference and automation run locally under BSD-3-Clause licensing. It suits users and teams who need autonomous web work without sending browsing data to a cloud provider.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/browser-operator-core.md)
