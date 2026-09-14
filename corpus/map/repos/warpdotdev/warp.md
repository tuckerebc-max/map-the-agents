# warpdotdev/warp

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3959ea72141f @ afc2f384249b5adc

## Summary (orientation draft, not independently verified)

The README calls out open-source dependencies including Tokio, NuShell, Alacritty, Hyper, FontKit, Smol, Fig completion specs, and the warp server framework. The server, Warp Drive backend, hosted authentication, and the Oz agent orchestration layer are not in this repository and remain proprietary. Evidence coverage: 123 of 181 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The client app is licensed AGPL v3 to keep derivatives open, while the warpui_core and warpui UI framework crates are MIT-licensed to maximize reuse. -- evidence: [FAQ.md#L115-L115](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L115-L115), [README.md#L56-L56](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L56-L56), [README.md#L54-L54](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L54-L54), [FAQ.md#L117-L117](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L117-L117)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: contributions start with a GitHub issue; maintainers apply readiness labels (ready-to-spec, ready-to-implement, needs-mocks), and feature work requires a spec PR adding product.md and tech.md under specs/GH<issue-number>/ before code. -- evidence: [FAQ.md#L27-L27](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L27-L27), [README.md#L69-L69](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L69-L69), [FAQ.md#L9-L9](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L9-L9), [FAQ.md#L19-L21](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L19-L21)
  - [observation/documented] Repository development practice: opened PRs are auto-assigned to Oz for an initial review, then a Warp subject-matter expert is requested; contributors can comment /warp-agent-review up to three times per PR for re-review. -- evidence: [FAQ.md#L41-L41](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L41-L41), [FAQ.md#L45-L45](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L45-L45)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Running Warp provides a /feedback command that files an issue with logs and environment details attached automatically. -- evidence: [FAQ.md#L15-L15](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L15-L15)
  - [observation/documented] The team plans to support the Agent Client Protocol (ACP) in Warp so other models or subscriptions could connect directly; this is tracked on their roadmap. -- evidence: [FAQ.md#L69-L69](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L69-L69), [FAQ.md#L67-L67](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L67-L67)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README calls out open-source dependencies including Tokio, NuShell, Alacritty, Hyper, FontKit, Smol, Fig completion specs, and the warp server framework. -- evidence: [README.md#L102-L110](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L102-L110), [README.md#L100-L100](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L100-L100)
- limitations (2 claim(s)):
  - [observation/documented] The server, Warp Drive backend, hosted authentication, and the Oz agent orchestration layer are not in this repository and remain proprietary. -- evidence: [FAQ.md#L93-L93](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L93-L93), [FAQ.md#L99-L99](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L99-L99)
  - [observation/documented] Warp's built-in agent harness runs server-side and is not open in this repository, so Codex or Claude models cannot currently be used with existing subscriptions in Warp. -- evidence: [FAQ.md#L65-L65](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L65-L65)
More evidence: [full detail](warp.detail.md)

Metadata and full claim list: [full detail](warp.detail.md)
Human notes ([notes](warp.notes.md), never overwritten by build)

[Back to map index](../../index.md)
