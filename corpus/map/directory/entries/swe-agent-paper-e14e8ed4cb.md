# SWE-agent Paper (`swe-agent-paper`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: unknown
- License: arXiv paper (code MIT at swe-agent.com)
- Language: Python
- Interface: unknown
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Introduces Agent-Computer Interface (ACI) tailored to LM agents for software engineering; achieved SOTA on SWE-bench (12.5% pass@1) and HumanEvalFix (87.7% pass@1); demonstrates that ACI design significantly affects agent behavior and performance.

(captured site page body (agents/swe-agent-paper.md), not a verified repo-code finding)
The SWE-agent paper (Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press; Princeton) argued that language models acting on code repositories are a new class of computer user and therefore need purpose-built interfaces, analogous to how IDEs serve human developers. It formalized the Agent-Computer Interface concept: compact file viewers, search tools with bounded output, and guarded edit commands that constrain the agent away from error-prone interaction patterns. The resulting system set state-of-the-art results at publication — 12.5% pass@1 on SWE-bench and 87.7% on HumanEvalFix — and the paper demonstrated that interface design choices materially change agent performance independent of the underlying model. The paper seeded the SWE-agent codebase, the SWE-bench ecosystem, and the ACI design vocabulary that subsequent open-source harnesses still build on.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swe-agent-paper.md)
