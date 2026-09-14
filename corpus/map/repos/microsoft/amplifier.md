# microsoft/amplifier

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 28588b93886d @ 4ae0b5b7a1d69299

## Summary (orientation draft, not independently verified)

Selected evidence records: Amplifier is a command-line AI assistant with a modular, extensible architecture; the CLI is described as just one reference interface for the underlying modular platform. Chat mode persists context across messages and offers slash commands (/help, /tools, /agents, /status, /config) plus /think and /do to toggle plan mode; single-shot use is via 'amplifier run'.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Bundles are composable configuration packages defining tools, providers, agents, and behaviors; the default 'foundation' bundle includes filesystem, bash, web, search, and task-delegation tools plus 14 specialized agents. -- evidence: [README.md#L258-L258](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L258-L258), [README.md#L242-L242](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L242-L242), [README.md#L260-L262](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L260-L262)
  - [observation/documented] The architecture distinguishes a provider module (a vendor-protocol adapter) from configured provider instances, so one module can back multiple instances with unique IDs, accounts, models, and priorities. -- evidence: [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L62-L64](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L62-L64), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L72-L76](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L72-L76), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L68-L70](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L68-L70)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Amplifier is a command-line AI assistant with a modular, extensible architecture; the CLI is described as just one reference interface for the underlying modular platform. -- evidence: [README.md#L15-L15](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L15-L15), [README.md#L17-L17](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L17-L17)
  - [observation/documented] Chat mode persists context across messages and offers slash commands (/help, /tools, /agents, /status, /config) plus /think and /do to toggle plan mode; single-shot use is via 'amplifier run'. -- evidence: [README.md#L221-L225](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L221-L225), [README.md#L231-L231](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L231-L231)
- memory-state (1 claim(s)):
  - [observation/documented] Every interaction is automatically saved and sessions are project-scoped; users can list sessions for the current project or across all projects with 'amplifier session list' and its --all-projects flag. -- evidence: [README.md#L291-L291](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L291-L291), [README.md#L316-L316](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L316-L316), [README.md#L301-L301](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L301-L301), [README.md#L304-L304](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L304-L304)
- orchestration (2 claim(s)):
  - [observation/documented] Delegated child sessions resolve their provider by spawn-time precedence: caller provider_preferences, then agent overlay preferences (possibly written from model_role by a routing hook), then parent mount-plan defaults. -- evidence: [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L109-L110](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L109-L110), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L112-L116](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L112-L116)
  - [observation/documented] Routing matrices map semantic model roles to ordered provider/model candidates, but routing applies only when the composed bundle mounts a routing strategy such as the routing-matrix hook. -- evidence: [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L91-L94](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L91-L94), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L96-L100](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L96-L100)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](amplifier.detail.md)

Metadata and full claim list: [full detail](amplifier.detail.md)
Human notes ([notes](amplifier.notes.md), never overwritten by build)

[Back to map index](../../index.md)
