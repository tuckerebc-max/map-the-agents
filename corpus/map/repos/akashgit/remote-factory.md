# akashgit/remote-factory

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4262d361ebbf @ cd2e332d94e06242

## Summary (orientation draft, not independently verified)

re:factory is a Python 3.11+ CLI-driven multi-agent factory built on Claude Code, organized as four layers (CLI, workflow graph engine, CEO orchestrator, specialist agents) with an eval system, MAP-Elites outer loop, and ACE playbook self-improvement. Evidence coverage: 158 of 321 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 49 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The system is described as four layers: a Python CLI, a workflow graph engine of Pydantic DAGs with typed nodes (AgentNode, FnNode, GateNode, ForkNode, JoinNode), a CEO orchestrator agent, and specialist Claude Code subprocess agents. -- evidence: [README.md#L272-L272](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L272-L272), [README.md#L244-L266](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L244-L266), [README.md#L274-L274](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L274-L274), [README.md#L270-L270](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L270-L270)
  - [observation/documented] Specialist agents include Researcher, Strategist, Builder, Reviewer, Evaluator, Archivist, Refiner, and Failure Analyst, each invoked as `factory agent <role> --task "..."` with a narrow responsibility. -- evidence: [docs/architecture.md#L29-L39](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/architecture.md#L29-L39)
- design-choices (3 claim(s)):
  - [observation/documented] Design-v2 replaces hardcoded researchers and a single strategist with three Director agents that dynamically size N (3-7) research directions, M (2-5) strategy perspectives, and K (2-5) QA testers, following parallel generation, synthesis, then gating. -- evidence: [README.md#L108-L114](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L108-L114), [README.md#L100-L100](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L100-L100)
  - [observation/documented] ACE self-improvement derives playbook bullets from real experiment outcomes, tracks helpful/harmful counters per bullet, prunes negative-net-score rules, caps playbook size, and injects evolved playbooks into agent prompts at spawn time. -- evidence: [docs/ace.md#L98-L102](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L98-L102), [docs/ace.md#L17-L21](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L17-L21), [docs/ace.md#L25-L29](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L25-L29), [docs/ace.md#L33-L33](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L33-L33), [docs/ace.md#L57-L60](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L57-L60)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors install dev deps with `uv sync --all-groups`, run `pytest -v`, lint with `ruff check .`, and type-check with `mypy factory/`; a contributing guide covers dev setup, code style, testing, and PR workflow. -- evidence: [README.md#L470-L475](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L470-L475), [README.md#L465-L466](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L465-L466)
  - [observation/documented] Repository development practice: after editing a workflow graph in `factory/workflow/definitions.py`, contributors re-export skills via `factory workflow export-skills` and test with `pytest tests/test_workflow.py -v`. -- evidence: [README.md#L151-L153](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L151-L153)
- skills-patterns (1 claim(s)):
  - [observation/documented] Workflow graphs are exported to SKILL.md prose playbooks through a verified pipeline (templatize, review agent, guard, split) producing SKILL.md plus SKILL.annotations.yaml, with a CI regression test guarding drift between definitions and exported skills. -- evidence: [README.md#L383-L383](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L383-L383), [README.md#L385-L390](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L385-L390), [README.md#L402-L402](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L402-L402), [README.md#L392-L394](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L392-L394)
- interfaces (4 claim(s)):
  - [observation/documented] The primary CLI is `factory ceo <path> --mode <mode>` with modes including design, design-v2, create, meta, and outer-loop (run headless), plus `--focus` to target a backlog item, GitHub issue, or topic. -- evidence: [README.md#L102-L106](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L102-L106), [README.md#L68-L71](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L68-L71), [README.md#L219-L220](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L219-L220), [README.md#L284-L286](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L284-L286), [README.md#L165-L172](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L165-L172), [README.md#L20-L20](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L20-L20)
More evidence: [full detail](remote-factory.detail.md)

Metadata and full claim list: [full detail](remote-factory.detail.md)
Human notes ([notes](remote-factory.notes.md), never overwritten by build)

[Back to map index](../../index.md)
