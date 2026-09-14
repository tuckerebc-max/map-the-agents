# polymathwizard/bhil-ai-first-development-toolkit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 161f8e5311bd @ dffb30bc95fe376f

## Summary (orientation draft, not independently verified)

The repository is a documented AI-first development methodology toolkit: an artifact chain (PRD→SPEC→ADR→TASK→CODE→REVIEW→DEPLOY) with YAML traceability IDs, copy-and-fill templates including three AI-native ADR types, a two-week sprint workflow with a test-first gate and promptfoo evaluation, and optional RuFlo orchestration with RuVector persistent memory. It is MIT-licensed per the README. Evidence coverage: 169 of 253 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 27 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] The toolkit prescribes a traceable artifact chain — PRD (what), SPEC (how), ADR (why), TASK (steps) — flowing through code, review, deploy, and closed by a sprint retrospective. -- evidence: [README.md#L17-L21](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L17-L21), [01-methodology-overview.md#L60-L62](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/01-methodology-overview.md#L60-L62)
  - [observation/documented] Every artifact carries a traceability ID in YAML frontmatter with defined formats such as PRD-NNN, SPEC-NNN, ADR-NNN, TASK-NNN, S-NN, and PV-NNN. -- evidence: [README.md#L114-L114](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L114-L114), [README.md#L116-L123](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L116-L123)
- components (1 claim(s)):
  - [observation/documented] The repository ships copy-and-fill templates including PRD, SPEC, TASK, sprint plan, and four ADR variants: core MADR-style, model-selection, prompt-strategy, and agent-orchestration. -- evidence: [README.md#L29-L82](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L29-L82)
- design-choices (1 claim(s)):
  - [observation/documented] Beyond standard ADRs, the toolkit defines three AI-native ADR categories — model selection, prompt strategy, and agent orchestration — each with its own template. -- evidence: [README.md#L139-L139](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L139-L139), [README.md#L135-L135](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L135-L135), [README.md#L141-L141](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L141-L141), [README.md#L137-L137](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L137-L137)
- workflows (3 claim(s)):
  - [observation/documented] A sprint is defined as a two-week cycle with four phases: specification (days 1-2), planning (days 3-5), implementation (week 2 days 1-3), and integration/evaluation/deploy/retro (days 4-5). -- evidence: [03-sprint-workflow.md#L13-L18](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L13-L18), [03-sprint-workflow.md#L9-L9](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L9-L9)
  - [observation/documented] The methodology mandates a test-first gate for AI-generated code: write tests, confirm they fail and commit that state, then implement without modifying test files. -- evidence: [03-sprint-workflow.md#L148-L150](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L148-L150), [03-sprint-workflow.md#L146-L146](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L146-L146)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Skills in .claude/skills/ are exposed as available slash-commands in Claude Code, and path-scoped rules in .claude/rules/ load when relevant files are opened. -- evidence: [00-getting-started.md#L62-L65](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/00-getting-started.md#L62-L65)
- memory-state (1 claim(s)):
  - [observation/documented] The methodology assigns RuVector the role of maintaining persistent memory across sessions so agent context does not start cold; RuFlo optionally orchestrates agents across the artifact chain. -- evidence: [00-getting-started.md#L9-L9](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/00-getting-started.md#L9-L9), [README.md#L23-L23](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L23-L23)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](bhil-ai-first-development-toolkit.detail.md)

Metadata and full claim list: [full detail](bhil-ai-first-development-toolkit.detail.md)
Human notes ([notes](bhil-ai-first-development-toolkit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
