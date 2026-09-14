# LocoTrainer (`locotrainer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: LocoreMind
- License: MIT
- Language: Python
- Interface: install=pip install locotrainer (or setup scripts / git clone)
- Model providers: OpenAI-compatible (DashScope, OpenRouter, llama.cpp, vLLM)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [locoremind/locotrainer](../../repos/locoremind/locotrainer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 4B-parameter MS-SWIFT domain expert agent distilled from Qwen3-Coder-Next; simulates a Claude Code-style agent environment; trained on 361K samples with 32K context; runs locally via GGUF quantization at zero API cost; auto-clones ms-swift on first run; key insight that absolute paths + tolerant tool argument parsing yields reliable agent behavior.

(captured site page body (agents/locotrainer.md), not a verified repo-code finding)
LocoTrainer addresses a narrow, recurring need: engineers working with the MS-SWIFT training framework need codebase analysis and structured reports, and a frontier-model agent is expensive for that repetitive task. The accompanying model was trained on 361,830 samples (agent trajectories, MS-SWIFT knowledge, and project structure paths) over roughly 25 hours on 8x H100s, and the surrounding framework replicates the Claude Code-style environment the model saw in training, down to absolute paths and system reminders, because that fidelity is what makes small-model tool calling reliable. The agent loop reads, searches, and analyzes the MS-SWIFT repository and emits markdown reports, running locally through GGUF quantization at zero API cost or through OpenAI-compatible providers. ML engineers fine-tuning with MS-SWIFT are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/locotrainer.md)
