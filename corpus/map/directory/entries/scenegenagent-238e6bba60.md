# SceneGenAgent (`scenegenagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: THUDM
- License: Apache-2.0
- Language: Python (generates C# code)
- Interface: install=git clone https://github.com/THUDM/SceneGenAgent.git; cd SceneGenAgent; pip install -r requirements.txt
- Model providers: GPT-4o, Llama3.1-70B (fine-tuned via SceneInstruct); API-based and offline models
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [thudm/scenegenagent](../../repos/thudm/scenegenagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM agent that generates industrial scenes through executable C# code with precise quantitative control (measurements/positioning), structured/calculable format, layout verification, and iterative refinement; ships SceneInstruct, a dataset for fine-tuning open-source LLMs that lifts Llama3.1-70B to approach GPT-4o performance; achieves up to 81.0% success rate on real-world industrial tasks. ACL 2025 Main paper.

(captured site page body (agents/scenegenagent.md), not a verified repo-code finding)
Industrial scene design — factory floors, equipment layouts — demands numeric precision that free-form LLM output cannot guarantee, so the THUDM agent generates executable C# code whose structure makes every measurement and position explicit and checkable. The loop proposes a layout, verifies it against quantitative constraints, and refines until the scene satisfies the requirements, with results published at ACL 2025 Main. The repository includes the agent framework, the SceneInstruct fine-tuning dataset, and training and inference guides, deployable as a Gradio app against API models or local checkpoints. It is research code — nine commits, no releases — aimed at researchers in layout generation and industrial digital twins rather than production users. The technique generalizes: any domain needing quantitative, verifiable spatial output can adopt the code-as-specification pattern.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/scenegenagent.md)
