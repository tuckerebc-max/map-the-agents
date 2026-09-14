# kyaukyuai/gpt-all-star

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cc9336f763bf @ 10848232eeca5153

## Summary (orientation draft, not independently verified)

Selected evidence records: The project is described as an AI-powered code generation tool for building web applications from scratch through collaboration among autonomous AI agents, framed as a research project. The concept is team-based agent collaboration: a leader is chosen for each step, the leader creates an action plan, and team members work together to complete each task.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is described as an AI-powered code generation tool for building web applications from scratch through collaboration among autonomous AI agents, framed as a research project. -- evidence: [README.md#L6-L10](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L6-L10)
- components (1 claim(s)):
  - [observation/documented] Agent team members are configurable by editing the gpt_all_star/agents.yml file, indicating agents are defined in a YAML configuration file. -- evidence: [README.md#L152-L152](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L152-L152)
- design-choices (1 claim(s)):
  - [observation/documented] The concept is team-based agent collaboration: a leader is chosen for each step, the leader creates an action plan, and team members work together to complete each task. -- evidence: [README.md#L29-L33](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L29-L33)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: developers are strongly recommended to run the app with Docker, using make build and make up, then open a web terminal on port 7681 and install dependencies with poetry. -- evidence: [README.md#L108-L111](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L108-L111), [README.md#L119-L121](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L119-L121), [README.md#L62-L62](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L62-L62), [README.md#L115-L115](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L115-L115)
  - [observation/documented] Repository development practice: contributors fork the repository, create a feature branch, and send a pull request; setup uses poetry lock/install, poetry shell, and pre-commit install. -- evidence: [README.md#L179-L183](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L179-L183), [README.md#L200-L202](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L200-L202), [README.md#L194-L196](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L194-L196), [README.md#L187-L190](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L187-L190)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI offers options including --step with values such as specification, system_design, ui_design, development, entrypoint, healing, plus project_name, japanese_mode, review_mode, debug_mode, and plan_and_solve flags. -- evidence: [README.md#L134-L148](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L134-L148)
  - [observation/documented] Users run the tool via the gpt-all-star command after exporting OPENAI_API_MODEL (e.g. gpt-4o) and OPENAI_API_KEY environment variables. -- evidence: [README.md#L56-L58](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L56-L58), [README.md#L49-L52](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L49-L52)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The tool is distributed on PyPI as gpt-all-star and installed with pip; the project is MIT licensed. -- evidence: [README.md#L43-L45](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L43-L45), [README.md#L4-L4](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L4-L4)
  - [observation/documented] Configuration supports three LLM endpoints selected via an ENDPOINT variable: OpenAI, Azure OpenAI, and Anthropic, each with its own key/model environment variables. -- evidence: [README.md#L78-L78](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L78-L78), [README.md#L81-L82](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L81-L82), [README.md#L92-L93](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L92-L93), [README.md#L85-L89](https://github.com/kyaukyuai/gpt-all-star/blob/cc9336f763bfc4d1fc2f4d5c75e640f22d7d9ebc/README.md#L85-L89)
- limitations (1 claim(s)):
More evidence: [full detail](gpt-all-star.detail.md)

Metadata and full claim list: [full detail](gpt-all-star.detail.md)
Human notes ([notes](gpt-all-star.notes.md), never overwritten by build)

[Back to map index](../../index.md)
