# Agents by Hugging Face (`agents-by-hugging-face`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: unknown
- License: Apache-2.0
- Language: Python
- Interface: platforms=IDE, Web; install=pip install transformers (stable); or install from source for the main version
- Model providers: Hugging Face (HfApiEngine / Inference API), Local (TransformersEngine)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Experimental agent API in Hugging Face Transformers offering CodeAgent (one-shot code generation and execution) and ReactAgent (step-by-step ReAct with JSON or Python tool calls); integrates with Gradio, Langchain, Hugging Face Spaces, and HF Hub tools via ToolCollection

(captured site page body (agents/agents-by-hugging-face.md), not a verified repo-code finding)
As LLMs gained tool-use competence, Hugging Face added an agents module to Transformers so models could chain its ecosystem of tools — text downloaders, speech-to-text, image generation, and community tools from the Hub — inside a reasoning loop. ReactAgent follows the think-act-observe pattern with JSON tool calls; CodeAgent instead has the model emit Python code that runs in a restricted interpreter with access limited to the toolbox and safe built-ins, which lets one generation invoke several tools. Custom tools plug in via the agent.tool decorator or load_tool from the Hub. The API was later deprecated and removed from Transformers in favor of the dedicated smolagents library, which carries the same CodeAgent and tool-calling design forward. Its main audience today is people reading older codebases and papers built on the Transformers agents API.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agents-by-hugging-face.md)
