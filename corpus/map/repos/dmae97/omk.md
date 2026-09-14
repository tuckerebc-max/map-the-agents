# dmae97/omk

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: dmae97/open-multi-agent-kit (github id 1225139405).
Latest snapshot: commit 4e820f879503 @ 5a51db1e1ff93d41

## Summary (orientation draft, not independently verified)

Selected evidence records: The v0.90.9 hardening document is an implementation-ready plan kept as a plan, not evidence that code was applied; the package version was 0.90.8 when written and 0.91.0 in the later snapshot. Per the patch analysis, aborting during sequential or wave tool execution can leave later tool calls in the transcript without matching tool results, since the loop breaks and returns only completed results.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The v0.90.9 hardening document is an implementation-ready plan kept as a plan, not evidence that code was applied; the package version was 0.90.8 when written and 0.91.0 in the later snapshot. -- evidence: [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L14-L14](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L14-L14), [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L3-L8](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L3-L8)
  - [observation/documented] The planned ALG-001 invariant requires every assistant tool call to have exactly one terminal result with a disposition of completed, failed, blocked, aborted, timeout, or skipped, with synthetic results for never-started calls. -- evidence: [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L261-L265](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L261-L265), [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L272-L280](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L272-L280), [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L282-L286](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L282-L286)
- components (1 claim(s)):
  - [observation/documented] ALG-003 is reported complete (15/15) as of 2026-07-23, including a Git workspace fingerprint (head plus dirty-diff digest), post-receipt latest-mutation evidence invalidation, and command-string secret redaction with a secure command hash. -- evidence: [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L16-L24](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L16-L24), [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L39-L40](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L39-L40)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the 2026-07-23 snapshot's verification evidence is limited to focused tests (112/112) and 'npm run check' exit 0; it explicitly does not claim full builds, ./test.sh, ./omk-test.sh, npm pack, or platform smoke results. -- evidence: [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L16-L24](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L16-L24), [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L44-L45](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L44-L45)
  - [observation/documented] Repository development practice: DESIGN.md governs the README and public brand assets with defined color tokens, typography levels, a 4px spacing unit, preferred asset ratios (2:1 hero, 3:2 feature frames), media budgets, and accessibility rules; packages/coding-agent/DESIGN.md covers the terminal UI. -- evidence: [DESIGN.md#L55-L58](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L55-L58), [DESIGN.md#L40-L42](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L40-L42), [DESIGN.md#L11-L19](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L11-L19), [DESIGN.md#L25-L30](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L25-L30), [DESIGN.md#L36-L36](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L36-L36), [DESIGN.md#L3-L3](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L3-L3), [DESIGN.md#L67-L67](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L67-L67), [DESIGN.md#L48-L51](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/DESIGN.md#L48-L51)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Only the CI callsite is wired to the receipt executor: ci.yml invokes dist/verify-ci.js, which runs release-consistency commands via executeVerifiedLocalBash with executor 'ci-runner'; CLI, interactive, RPC, and AgentSession bash paths remain unconnected. -- evidence: [OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L28-L33](https://github.com/dmae97/omk/blob/4e820f87950392e97129e581aecebb060bf208dd/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md#L28-L33)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (5 claim(s)):
More evidence: [full detail](omk.detail.md)

Metadata and full claim list: [full detail](omk.detail.md)
Human notes ([notes](omk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
