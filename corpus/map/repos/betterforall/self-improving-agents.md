# betterforall/self-improving-agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5f7823732d87 @ 2ffba66f8aa5de4e

## Summary (orientation draft, not independently verified)

The repository documents a four-level progression of self-improving code agents (simple benchmark loop, structured reviewer feedback, self-rewriting meta-agent, adversarial arena), with shared task definitions, checkpointing, and reported experiment results on three tasks using Gemini 2.5 Flash. Evidence coverage: 145 of 183 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project defines four levels of self-improving code agents, each adding one key idea, from a simple improvement loop to an adversarial arena with self-modifying agents. -- evidence: [README.md#L3-L4](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L3-L4)
- components (5 claim(s)):
  - [observation/documented] Level 1 (autoresearch/) is a single-agent loop: the LLM proposes code, it is written to a file, benchmarked, kept if better, and repeated; bad proposals revert immediately. -- evidence: [README.md#L138-L141](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L138-L141), [README.md#L134-L136](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L134-L136), [README.md#L132-L132](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L132-L132)
  - [observation/documented] Level 2 (feedback-loop/) adds a reviewer agent that returns structured feedback (issue type, severity, fix suggestion, confidence, detected pattern) explaining why a solution failed. -- evidence: [README.md#L151-L159](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L151-L159), [README.md#L147-L147](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L147-L147)
- design-choices (3 claim(s)):
  - [observation/documented] Level 2 uses asymmetric information: the worker gets a small prompt with just the code, while the reviewer sees full history and prior feedback to spot cross-iteration patterns. -- evidence: [README.md#L165-L165](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L165-L165), [README.md#L161-L163](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L161-L163)
  - [observation/documented] In Arena Loop, code agents are described as mini-HyperAgents that can mutate their own propose() function, so the code-generating code itself evolves. -- evidence: [README.md#L227-L228](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L227-L228)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Each level is run via a run.py entry point (e.g. python autoresearch/run.py) with a --task flag selecting tasks such as snake, support, or email_validation. -- evidence: [README.md#L83-L86](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L83-L86), [README.md#L89-L91](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L89-L91)
  - [observation/documented] run_all.py runs experiments across all levels and generates comparison analysis, supporting --levels/--tasks filters and a --fresh flag to ignore previous results; analyze_results.py performs cross-level comparison after experiments are done. -- evidence: [README.md#L100-L101](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L100-L101), [README.md#L104-L105](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L104-L105), [README.md#L97-L97](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L97-L97)
- memory-state (1 claim(s)):
  - [observation/documented] All levels share tasks/checkpoint.py for resumable checkpointing using sequence-numbered JSON files with atomic writes (write to .tmp then os.replace), keeping only the last three checkpoints. -- evidence: [README.md#L332-L336](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L332-L336)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (3 claim(s)):
  - [observation/documented] Experiments used Gemini 2.5 Flash across five levels and three tasks (email_validation, snake, support) in 15 total experiments, with per-level metrics, costs, and token counts reported. -- evidence: [experiment-results.md#L14-L30](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L14-L30), [experiment-results.md#L7-L10](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L7-L10)
More evidence: [full detail](self-improving-agents.detail.md)

Metadata and full claim list: [full detail](self-improving-agents.detail.md)
Human notes ([notes](self-improving-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
