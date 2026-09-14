# icebaker/nano-bots

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2bbc92857aa4 @ 797c7851bb478ba8

## Summary (orientation draft, not independently verified)

This repository is a collection of Nano Bots 'Cartridges' (YAML bot definitions) browsable at nbots.io, with documentation on using, creating, sharing, and licensing them. Most evidence covers contribution/sharing workflow and licensing guidance; no runtime behavior of an implementation is documented here.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] The repository hosts Nano Bots' Cartridges, which are YAML files that require a separate implementation to run. -- evidence: [README.md#L22-L22](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L22-L22), [README.md#L6-L6](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L6-L6), [README.md#L18-L18](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L18-L18)
  - [observation/documented] Cartridges may include a `miscellaneous.marketplace` section with `tags` (clean-URL style) and `samples` entries specifying interface type and inputs. -- evidence: [README.md#L62-L74](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L62-L74), [README.md#L76-L76](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L76-L76), [README.md#L60-L60](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L60-L60)
- components (1 claim(s)):
  - [observation/documented] Listed implementations include a Ruby CLI, a Clinic live editor, a Nano Bots API with a public endpoint, and Sublime Text and VS Code extensions. -- evidence: [README.md#L24-L29](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L24-L29)
- design-choices (1 claim(s)):
  - [observation/documented] The project recommends authors publish cartridges under permissive licenses (CC0-1.0 preferred, any SPDX-known license allowed) given unresolved questions about prompt licensing. -- evidence: [README.md#L104-L104](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L104-L104), [README.md#L88-L88](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L88-L88), [README.md#L90-L90](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L90-L90)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors share Cartridges via pull request, creating a folder named `@your-nickname` under `/cartridges` with a `profile.yml` describing the author. -- evidence: [README.md#L45-L45](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L45-L45), [README.md#L47-L54](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L47-L54)
  - [observation/documented] Repository development practice: each user folder is tied to the contributor's GitHub username and only accepts pull requests from that user. -- evidence: [README.md#L56-L56](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L56-L56)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Cartridges can be used by downloading the YAML file or copying its contents into a local YAML file, then running it with an implementation. -- evidence: [README.md#L18-L18](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L18-L18)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Running a Cartridge requires an external implementation; the repository itself does not provide one. -- evidence: [README.md#L22-L22](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L22-L22), [README.md#L18-L18](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L18-L18)
- limitations (1 claim(s)):
  - [observation/documented] The licensing section states it is uncertain whether its licensing approach is practical or enforceable, and that it should be seen as a statement of intention, not a guarantee. -- evidence: [README.md#L106-L106](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L106-L106)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](nano-bots.detail.md) for every claim.)

Metadata and full claim list: [full detail](nano-bots.detail.md)
Human notes ([notes](nano-bots.notes.md), never overwritten by build)

[Back to map index](../../index.md)
