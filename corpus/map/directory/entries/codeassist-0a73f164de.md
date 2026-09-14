# codeassist (`codeassist`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: gensyn-ai
- License: MIT
- Language: Python
- Interface: install=docker
- Model providers: None (trains a local model from user interaction)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [gensyn-ai/codeassist](../../repos/gensyn-ai/codeassist.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Completely private, local AI coding assistant by Gensyn that writes directly in your editor and learns from every keystroke. Continuous learning from interaction (every keystroke, edit, deletion, or untouched output is a training signal). Apprentice model — behaves like a collaborator learning your craft. Trains a personal local model checkpoint per episode and optionally uploads to HuggingFace. NOTE: Project appears ...

(captured site page body (agents/codeassist.md), not a verified repo-code finding)
CodeAssist was Gensyn's demonstration of decentralized training applied to coding assistance: a local assistant that writes directly into the editor relative to the cursor and adapts to the user's style through reinforcement signals from every keystroke, acceptance, and deletion. Each interaction episode trains a personal model checkpoint on the local machine, optionally uploaded to Hugging Face, with no code leaving the machine. Operationally it functioned as Gensyn's Testnet participation app, where users solved practice problems and earned on-chain participation credit, tying model improvement to network participation. Gensyn has stopped tracking new CodeAssist participation as the network shifts to Mainnet, and the repository — 27 commits, no releases — is no longer under development.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codeassist.md)
