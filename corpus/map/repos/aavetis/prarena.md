# aavetis/prarena

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ce67a5baafeb @ a90e89d66917f8f9

## Summary (orientation draft, not independently verified)

The project benchmarks AI coding agents by measuring each agent's ability to produce mergeable pull requests, comparing ready-PR merge success rates across agents. Metrics distinguish all PRs (including drafts), ready (non-draft) PRs, and merged PRs, with headline statistics computed on ready PRs only for fair cross-agent comparison.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Agent identification uses GitHub search qualifiers on branch prefix (head:copilot/, head:codex/, head:cursor/) or bot author (devin-ai-integration[bot], codegen-sh[bot], google-labs-jules[bot]). -- evidence: [README.md#L35-L36](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L35-L36), [README.md#L39-L40](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L39-L40), [README.md#L23-L24](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L23-L24), [README.md#L43-L44](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L43-L44), [README.md#L31-L32](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L31-L32), [README.md#L27-L28](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L27-L28)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md provides a mandatory step-by-step checklist for onboarding a new agent, described as the single source of truth after earlier omissions caused Jules-related regressions. -- evidence: [AGENTS.md#L5-L5](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/AGENTS.md#L5-L5), [AGENTS.md#L54-L54](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/AGENTS.md#L54-L54)
  - [observation/documented] Repository development practice: onboarding requires collecting four GitHub search queries per agent (total, merged, ready, draft), verifying each manually in a browser before codifying it. -- evidence: [AGENTS.md#L8-L18](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/AGENTS.md#L8-L18)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The project publishes an interactive dashboard at prarena.ai presenting the PR statistics. -- evidence: [README.md#L3-L3](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L3-L3)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (3 claim(s)):
  - [observation/documented] The project benchmarks AI coding agents by measuring each agent's ability to produce mergeable pull requests, comparing ready-PR merge success rates across agents. -- evidence: [README.md#L15-L15](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L15-L15)
  - [observation/documented] Metrics distinguish all PRs (including drafts), ready (non-draft) PRs, and merged PRs, with headline statistics computed on ready PRs only for fair cross-agent comparison. -- evidence: [README.md#L9-L11](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L9-L11), [README.md#L15-L15](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/README.md#L15-L15)
- dependencies (1 claim(s)):
  - [observation/documented] The Python pipeline depends on matplotlib, pandas, requests, numpy, and jinja2 per requirements.txt. -- evidence: [requirements.txt#L1-L5](https://github.com/aavetis/PRarena/blob/ce67a5baafeb98bf0af6ff882aa6f53997fb399a/requirements.txt#L1-L5)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](prarena.detail.md) for every claim.)

Metadata and full claim list: [full detail](prarena.detail.md)
Human notes ([notes](prarena.notes.md), never overwritten by build)

[Back to map index](../../index.md)
