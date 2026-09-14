# the-pr-agent/pr-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: codium-ai/pr-agent (github id 662766482).
Latest snapshot: commit d24b6f36e787 @ 80d4ad7ef368be71

## Summary (orientation draft, not independently verified)

Evidence covers PR-Agent, an open-source AI code review agent (community-maintained legacy Qodo project) with comment/CLI/GitHub Action interfaces, multiple git providers and LLM backends, an agent-skills injection feature, and documented limitations. Development-practice guidance appears only in the contributing section.

## Source coverage

Source coverage (partial): 6 of 53 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Each core tool (/review, /improve, /ask) is described as using a single LLM call, taking roughly 30 seconds at low cost. -- evidence: [README.md#L114-L114](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L114-L114)
  - [observation/documented] A PR compression strategy converts code diffs into manageable LLM prompts, and the README claims it handles both small and large PRs. -- evidence: [README.md#L116-L116](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L116-L116), [docs/docs/index.md#L85-L85](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/index.md#L85-L85)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: for local verification, run 'PYTHONPATH=. uv run pytest' from the repo root, which discovers the unit-test suite under tests/unittest; e2e tests under tests/e2e_tests need provider credentials and are invoked explicitly. -- evidence: [README.md#L210-L210](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L210-L210)
- skills-patterns (2 claim(s)):
  - [observation/documented] Agent Skills use a SKILL.md format: a directory with a markdown file whose YAML frontmatter carries name and description, followed by a markdown body of review guidance. -- evidence: [docs/docs/core-abilities/agent_skills.md#L9-L13](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L9-L13), [docs/docs/core-abilities/agent_skills.md#L7-L7](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L7-L7)
  - [observation/documented] When enabled, PR-Agent discovers SKILL.md files under configured paths and injects each skill's name, description, and body into the /review, /improve, /describe, and top-level /ask prompts alongside extra_instructions. -- evidence: [docs/docs/core-abilities/agent_skills.md#L22-L22](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L22-L22)
- interfaces (5 claim(s)):
  - [observation/documented] PR-Agent tools can be invoked by commenting commands like /describe, /review, /improve, and /ask on a pull request, or locally via a CLI such as 'pr-agent --pr_url <PR_URL> review'. -- evidence: [README.md#L176-L176](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L176-L176), [README.md#L180-L183](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L180-L183), [README.md#L186-L187](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L186-L187)
  - [observation/documented] The product can run as a GitHub Action triggered on pull_request opened/synchronize events, configured via a workflow file that supplies OPENAI_KEY and GITHUB_TOKEN secrets. -- evidence: [README.md#L72-L86](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L72-L86)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] skills.paths is host-level only: it cannot be set from a repository's .pr_agent.toml, and repo-supplied values are ignored with a warning, to prevent malicious repos from pointing the scan at sensitive host files. -- evidence: [docs/docs/core-abilities/agent_skills.md#L44-L44](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L44-L44), [docs/docs/core-abilities/agent_skills.md#L41-L42](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L41-L42)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](pr-agent.detail.md)

Metadata and full claim list: [full detail](pr-agent.detail.md)
Human notes ([notes](pr-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
