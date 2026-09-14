# agent-field/swe-af

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 311f376a2f12 @ 3876c9a6cfec396b

## Summary (orientation draft, not independently verified)

README-only evidence for SWE-AF, an autonomous multi-agent software engineering runtime built on AgentField, exposing build and issue-level entry points via CLI/HTTP, with documented control loops, runtime/model configuration, and a self-reported benchmark. Evidence coverage: 136 of 392 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Three runtimes are supported via a flat config map: claude_code (Claude), open_code (OpenCode with OpenRouter/OpenAI/Google/Anthropic IDs), and codex (OpenAI Codex CLI). -- evidence: [README.md#L207-L210](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L207-L210)
  - [observation/documented] With only an OpenRouter or Infron key set and no SWE_DEFAULT_RUNTIME, the system auto-selects the open_code runtime and defaults roles to a deepseek model id. -- evidence: [README.md#L386-L386](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L386-L386), [README.md#L249-L250](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L249-L250)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's Tests badge points to a make check command run via GitHub Actions CI (.github/workflows/ci.yml). -- evidence: [README.md#L9-L16](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L9-L16)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] Builds are triggered through the af CLI (af >= 0.1.87) via `af call swe-planner.build --in ...`, or by POSTing to the AgentField HTTP endpoint /api/v1/execute/async/swe-planner.build. -- evidence: [README.md#L44-L54](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L44-L54), [README.md#L58-L78](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L58-L78), [README.md#L42-L42](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L42-L42)
  - [observation/documented] Input accepts repo_url for remote repos or repo_path for local workspaces, plus a config map with runtime, per-role models, and enable_learning. -- evidence: [README.md#L357-L376](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L357-L376), [README.md#L88-L88](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L88-L88)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
  - [observation/documented] Three nested control loops adapt to difficulty: coder retries on QA/review failure, an issue advisor retries/splits/accepts with debt, and a replanner restructures the remaining DAG on escalated failures. -- evidence: [README.md#L214-L214](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L214-L214), [README.md#L222-L222](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L222-L222), [README.md#L216-L220](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L216-L220)
  - [observation/documented] Issues are dependency-sorted and executed in parallel across isolated git worktrees; a typical run reportedly spins up 400-500+ agent instances, scaling to thousands for larger DAGs. -- evidence: [README.md#L448-L448](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L448-L448), [README.md#L437-L442](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L437-L442)
- tools-permissions (1 claim(s)):
  - [observation/documented] Web search is opt-in for the open runtime: setting OPENCODE_ENABLE_EXA=1 and EXA_API_KEY exposes opencode's websearch/webfetch tools to reasoners, with a restraint guideline appended to the coder's system prompt. -- evidence: [README.md#L424-L427](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L424-L427), [README.md#L431-L431](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L431-L431), [README.md#L429-L429](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L429-L429), [README.md#L422-L422](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L422-L422)
- evaluation (1 claim(s)):
  - [observation/documented] A self-reported benchmark scores SWE-AF 95/100 with haiku (~$20) and MiniMax M2.5 (~$6) versus Claude Code sonnet (73), Codex o3 (62), and Claude Code haiku (59) on a Node.js todo-app prompt, using a five-dimension scoring framework. -- evidence: [README.md#L476-L482](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L476-L482), [README.md#L472-L472](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L472-L472), [README.md#L452-L452](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L452-L452), [README.md#L454-L463](https://github.com/Agent-Field/SWE-AF/blob/311f376a2f12df01134acd80384d599dd8039178/README.md#L454-L463)
More evidence: [full detail](swe-af.detail.md)

Metadata and full claim list: [full detail](swe-af.detail.md)
Human notes ([notes](swe-af.notes.md), never overwritten by build)

[Back to map index](../../index.md)
