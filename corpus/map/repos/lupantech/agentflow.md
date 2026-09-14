# lupantech/agentflow

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b94006436b87 @ 185232572fb0fc34

## Summary (orientation draft, not independently verified)

The evidence is a README describing AgentFlow, a trainable tool-integrated agentic framework with four coordinated modules optimized via Flow-GRPO, plus setup, inference, training, and benchmark instructions.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] AgentFlow is a modular agentic system with four specialized modules: Planner, Executor, Verifier, and Generator. -- evidence: [README.md#L45-L45](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L45-L45), [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70)
- design-choices (1 claim(s)):
  - [observation/documented] The framework optimizes the planner agent within the system online using Flow-based Group Refined Policy Optimization (Flow-GRPO), rather than training a single LLM to interleave reasoning and tool calls. -- evidence: [README.md#L49-L49](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L49-L49), [README.md#L185-L185](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L185-L185)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors are invited to open issues or submit pull requests, contact maintainers by email, or join the project's Slack community. -- evidence: [README.md#L372-L372](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L372-L372)
  - [observation/documented] Repository development practice: before running, users are recommended to verify API keys and environment using provided tool-test and LLM-engine-test scripts. -- evidence: [README.md#L188-L188](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L188-L188), [README.md#L123-L137](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L123-L137), [README.md#L140-L154](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L140-L154), [README.md#L120-L120](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L120-L120)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Inference can be run via quick_start.py, which reports reasoning steps such as query analysis, action prediction, and command execution before producing an answer. -- evidence: [README.md#L159-L173](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L159-L173)
  - [observation/documented] Each agent module can use a different LLM engine; the planner's engine is set via llm_engine_name in run scripts, while Executor/Verifier/Generator default to Qwen-2.5-7B-Instruct via DashScope and can be changed in code. -- evidence: [README.md#L255-L256](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L255-L256), [README.md#L253-L253](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L253-L253), [README.md#L266-L267](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L266-L267), [README.md#L258-L264](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L258-L264)
- memory-state (1 claim(s)):
  - [observation/documented] The four agent modules coordinate via evolving memory and integrated tools across multiple turns. -- evidence: [README.md#L157-L157](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L157-L157), [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The system integrates multiple tools including base_generator, python_coder, google_search, wikipedia_search, and web_search. -- evidence: [README.md#L123-L137](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L123-L137), [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70)
- evaluation (2 claim(s)):
  - [observation/documented] The README reports that AgentFlow with a Qwen-2.5-7B backbone outperforms top baselines on 10 benchmarks (+14.9% search, +14.0% agentic, +14.5% math, +4.1% science), reportedly surpassing GPT-4o. -- evidence: [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70), [README.md#L283-L287](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L283-L287), [README.md#L289-L289](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L289-L289)
  - [observation/documented] Benchmark runs (e.g., Bamboogle) produce per-task folders with evaluation data, execution logs, generated answers, and final score logs; a trained 7B Flow-GRPO planner is served with vLLM for evaluation. -- evidence: [README.md#L232-L235](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L232-L235), [README.md#L241-L242](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L241-L242), [README.md#L244-L247](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L244-L247)
- dependencies (1 claim(s)):
  - [observation/documented] Setup recommends Python 3.11, installation via setup.sh, and API keys (OpenAI, Google, optionally DashScope or Together) configured in agentflow/.env. -- evidence: [README.md#L96-L98](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L96-L98), [README.md#L105-L110](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L105-L110), [README.md#L93-L93](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L93-L93)
More evidence: [full detail](agentflow.detail.md)

Metadata and full claim list: [full detail](agentflow.detail.md)
Human notes ([notes](agentflow.notes.md), never overwritten by build)

[Back to map index](../../index.md)
