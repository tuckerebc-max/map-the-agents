# tractorjuice/arc-kit

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bc6bf533811d @ 4dba9575cce4f2e6

## Summary (orientation draft, not independently verified)

ArcKit is a slash-command architecture toolkit: an adm-preliminary command produces a TOGAF Architecture Vision artefact, an au-federal recipe defines 35 dependency-ordered build targets, and a contributor-published validation scorecard reports 9 evaluation runs of 8 AU compliance commands with a 25/25 pass rate. Evidence coverage: 128 of 266 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 327 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The `au-federal` recipe defines 35 targets including 9 optional ones, 2 post-build hooks (arckit:health, arckit:pages), schema_version 1, and an explicit top-level `flagship: AU_DISP`. -- evidence: [docs/au-federal-validation-scorecard.md#L157-L164](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L157-L164), [docs/au-federal-validation-scorecard.md#L233-L240](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L233-L240)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: regression tests live in `tests/plugin/test_au_federal_recipe.py` (run via pytest with `-k round2` or `-k ai6` filters), and the suite grew from 61 baseline tests to 191 across review rounds. -- evidence: [docs/au-federal-validation-scorecard.md#L349-L349](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L349-L349), [docs/au-federal-validation-scorecard.md#L377-L377](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L377-L377), [docs/au-federal-validation-scorecard.md#L270-L270](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L270-L270)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The `/arckit:adm-preliminary` command takes a project ID or transformation scope and produces an Architecture Vision artefact at `projects/<id>/ARC-<id>-ADMP-v1.0.md`. -- evidence: [docs/guides/adm-preliminary.md#L5-L5](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L5-L5), [docs/guides/adm-preliminary.md#L22-L24](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L22-L24), [docs/guides/adm-preliminary.md#L26-L26](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L26-L26)
  - [observation/documented] The adm-preliminary deliverable includes scope, drivers, constraints, success criteria, a Mermaid context diagram, stakeholder map, ADM phase coverage, and traceability sections. -- evidence: [docs/guides/adm-preliminary.md#L32-L42](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L32-L42)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The build harness schedules recipe targets via topological sort over `targets[].deps` with glob expansion; the au-federal plan computes 9 build waves with maximum parallelism of 11 in wave W2. -- evidence: [docs/au-federal-validation-scorecard.md#L196-L196](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L196-L196), [docs/au-federal-validation-scorecard.md#L183-L194](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L183-L194), [docs/au-federal-validation-scorecard.md#L181-L181](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L181-L181)
  - [observation/documented] Per the arckit-build skill's recipe-loading rules, the harness reads recipes from `.arckit/recipes/` first, so a project-level override takes precedence over plugin defaults. -- evidence: [docs/au-federal-validation-scorecard.md#L209-L209](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L209-L209)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (3 claim(s)):
  - [observation/documented] A validation scorecard reports 9 evaluation runs of the 8 AU commands with a 25/25 scorecard pass rate at Run 3, zero UK framework leakage, and 220 AU framework references in the artefacts. -- evidence: [docs/au-federal-validation-scorecard.md#L88-L88](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L88-L88), [docs/au-federal-validation-scorecard.md#L30-L41](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L30-L41)
  - [observation/documented] Layer A validation tested the 8 community commands against a real Australian SMB engagement (DISP-track, OFFICIAL:Sensitive, pure-SaaS estate), with underlying artefacts available under NDA. -- evidence: [docs/au-federal-validation-scorecard.md#L17-L20](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L17-L20), [docs/au-federal-validation-scorecard.md#L399-L399](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L399-L399)
- dependencies (2 claim(s)):
More evidence: [full detail](arc-kit.detail.md)

Metadata and full claim list: [full detail](arc-kit.detail.md)
Human notes ([notes](arc-kit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
