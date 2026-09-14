# humanlayer/humanlayer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 99abe673498c @ 847cd17b149ba4c3

## Summary (orientation draft, not independently verified)

The snapshot is mostly development and documentation guidance: the README marks the code as deprecated, DEVELOPMENT.md describes parallel nightly/dev daemon environments, and docs knowledge files cover release, docs, and channel-design practices. Little evidence describes shipped runtime behavior directly. Evidence coverage: 159 of 172 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 3 facet(s); 10 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Internal docs knowledge describes contact channels (Slack, email, web embeds, SMS/WhatsApp in beta) as composable, with web embeds requiring a backend proxy so HumanLayer API keys are never exposed to the frontend. -- evidence: [docs/docs.knowledge.md#L160-L175](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L160-L175), [docs/docs.knowledge.md#L186-L194](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L186-L194)
  - [observation/documented] Docs knowledge describes a three-level contact-channel configuration hierarchy (operation, SDK, project) where operation-level settings override SDK-level, which override project defaults. -- evidence: [docs/docs.knowledge.md#L222-L227](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L222-L227)
- workflows (10 claim(s)):
  - [observation/documented] Repository development practice: the README states the code in this repo is largely deprecated and points readers to a rebuilt HumanLayer at humanlayer.com. -- evidence: [README.md#L3-L3](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/README.md#L3-L3)
  - [observation/documented] Repository development practice: DEVELOPMENT.md describes parallel 'nightly' (stable) and 'dev' (testing) environments so daemon or WUI changes can be tested without restarting the daemon and breaking active Claude sessions. -- evidence: [DEVELOPMENT.md#L23-L26](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L23-L26), [DEVELOPMENT.md#L7-L7](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L7-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] The humanlayer.md SDK documentation notes the HumanLayer SDKs were removed in pull request #646 and are being superseded by CodeLayer. -- evidence: [humanlayer.md#L3-L3](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L3-L3), [humanlayer.md#L5-L5](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L5-L5)
- relevance: unknown (no source-linked claim submitted for this facet)

(8 additional claim(s) omitted for length; see [full detail](humanlayer.detail.md) for every claim.)

Metadata and full claim list: [full detail](humanlayer.detail.md)
Human notes ([notes](humanlayer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
