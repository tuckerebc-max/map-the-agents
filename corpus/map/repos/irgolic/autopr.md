# irgolic/autopr

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a95671a20d8d @ 29ca6eca824e6f47

## Summary (orientation draft, not independently verified)

Selected evidence records: AutoPR is a GitHub Action that automatically writes pull requests in response to issues, per its usage guide. When an issue gets a label containing 'AutoPR', the bot plans a fix, writes code, pushes a branch, and opens a pull request.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AutoPR is a GitHub Action that automatically writes pull requests in response to issues, per its usage guide. -- evidence: [USAGE.md#L4-L4](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L4-L4)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Triggered runs create a branch named autopr/issue-# and open a PR to the base branch; an existing branch is overwritten by default behavior described in the usage steps. -- evidence: [USAGE.md#L27-L31](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L27-L31)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors extend AutoPR by subclassing Action (with an id and run method) or Agent (with handle_event), and actions share state via a ContextDict passed between actions. -- evidence: [CONTRIBUTING.md#L57-L57](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L57-L57), [CONTRIBUTING.md#L18-L18](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L18-L18), [CONTRIBUTING.md#L51-L51](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L51-L51), [CONTRIBUTING.md#L26-L29](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L26-L29)
  - [observation/documented] Repository development practice: each rail run makes two LLM calls — a natural-language chat message, then a guardrails call serializing the response to typed JSON. -- evidence: [CONTRIBUTING.md#L117-L119](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L117-L119)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The action is invoked as docker://ghcr.io/irgolic/autopr:latest and configured through workflow 'with:' parameters such as github_token and model. -- evidence: [USAGE.md#L59-L68](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L59-L68), [USAGE.md#L46-L53](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L46-L53)
  - [observation/documented] Documented inputs include github_token (required), base_branch (default main), model (default gpt-4), context_limit (8192), min/max_tokens, num_reasks, temperature, agent_id (default plan_and_code), and overwrite_existing. -- evidence: [USAGE.md#L78-L90](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L78-L90)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] When an issue gets a label containing 'AutoPR', the bot plans a fix, writes code, pushes a branch, and opens a pull request. -- evidence: [README.md#L39-L42](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L39-L42), [README.md#L37-L37](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L37-L37)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] AutoPR is built with Guardrails, described as prompting LLMs to generate structured data with JSON Schemas and re-asking when output does not adhere. -- evidence: [README.md#L17-L18](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L17-L18), [README.md#L29-L31](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L29-L31)
  - [observation/documented] The action requires an OpenAI API key with ChatGPT access, supplied via the OPENAI_API_KEY secret. -- evidence: [USAGE.md#L10-L11](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L10-L11), [USAGE.md#L17-L21](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L17-L21)
- limitations (3 claim(s)):
  - [observation/documented] The README lists known defects: incorrectly referencing code in other files, duplicating lines, calling nonexistent functions, and only working on GitHub. -- evidence: [README.md#L61-L64](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L61-L64)
More evidence: [full detail](autopr.detail.md)

Metadata and full claim list: [full detail](autopr.detail.md)
Human notes ([notes](autopr.notes.md), never overwritten by build)

[Back to map index](../../index.md)
