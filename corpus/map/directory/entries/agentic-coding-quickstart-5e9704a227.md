# agentic-coding-quickstart (`agentic-coding-quickstart`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: GSA-TTS
- License: CC0-1.0
- Language: Shell
- Interface: install=git clone, then ./acq run opencode \<path\>; requires microsandbox (Homebrew/curl) or Docker
- Model providers: USAi
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [gsa-tts/agentic-coding-quickstart](../../repos/gsa-tts/agentic-coding-quickstart.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Built for U.S. federal teams — integrates with the USAi government AI API, enforces sandbox isolation (microsandbox microVMs or Docker) for safety, handles federal compliance (Zscaler CA, git commit signing), and auto-provisions federal-relevant agent skills via a kits system.

(captured site page body (agents/agentic-coding-quickstart.md), not a verified repo-code finding)
Federal engineering teams cannot use consumer AI coding tools as-is: data must stay inside approved systems, Zscaler intercepts TLS, and commits require signing, so GSA-TTS built this quickstart to make compliant agent setup a one-command operation. Running ./acq opencode launches the opencode agent inside a microsandbox microVM (or Docker) wired to the USAi LLM gateway at api.gsa.usai.gov, with USAi keys and GitHub tokens injected at runtime so secrets never enter the guest VM, and Zscaler certificate handling plus git commit signing configured automatically. It is one of three companion repositories (with Playbook and Patterns) and ships reusable agent skills for federal compliance, code review, and secure development. Its users are US government engineering teams adopting AI coding under federal constraints.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentic-coding-quickstart.md)
