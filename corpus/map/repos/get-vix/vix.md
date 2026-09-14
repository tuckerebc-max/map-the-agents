# get-vix/vix

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8e4262d6d1a8 @ 5bb529b55446d470

## Summary (orientation draft, not independently verified)

Evidence consists of README, DEBUG.md, and PROVIDERS.md for vix, an AI coding agent with a daemon (vixd) and TUI client, provider configuration system, pprof debugging endpoints, and a documented plan-mode benchmark against Claude Code. No contributor/development-practice guidance appears in the slices. Evidence coverage: 158 of 295 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vix is described as a fast, token-efficient AI coding agent whose stem agents maximize prompt-cache reuse across phases and whose Tree-sitter virtual filesystem lets it read and edit minified code, claimed to cut tokens 20-50%. -- evidence: [README.md#L5-L5](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L5-L5), [README.md#L23-L23](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L23-L23)
- components (1 claim(s)):
  - [observation/documented] The product consists of a daemon (vixd) and a client (vix); the daemon is started first, and multiple isolated vix instances can then be run. -- evidence: [README.md#L96-L96](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L96-L96), [README.md#L92-L94](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L92-L94), [README.md#L90-L90](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L90-L90), [README.md#L98-L100](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L98-L100)
- design-choices (2 claim(s)):
  - [observation/documented] The stem-agent design uses a generic system prompt with per-phase instructions delivered as user messages, so the explore-phase history stays cached when the LLM is told to act as a planner. -- evidence: [README.md#L133-L133](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L133-L133), [README.md#L135-L135](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L135-L135), [README.md#L129-L129](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L129-L129)
  - [observation/documented] Rather than limiting exploration, vix strips whitespace characters from file content via a virtual filesystem so the LLM works on minified code, reportedly reducing tokens by 20-50%. -- evidence: [README.md#L143-L143](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L143-L143), [README.md#L145-L145](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L145-L145)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Vix advertises standard agent capabilities including skills, MCP servers, subagents, LSP-backed code intelligence, sandboxed execution, and multiple providers. -- evidence: [README.md#L29-L29](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L29-L29)
- interfaces (6 claim(s)):
  - [observation/documented] Both vixd and vix expose a pprof HTTP server via --pprof-port (default ports 6060 and 6061, overridable by VIX_PPROF_PORT), serving goroutine, heap, allocs, and CPU profiles. -- evidence: [DEBUG.md#L29-L31](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L29-L31), [DEBUG.md#L52-L59](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L52-L59), [DEBUG.md#L6-L9](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L6-L9), [DEBUG.md#L3-L4](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L3-L4), [DEBUG.md#L38-L40](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L38-L40)
  - [observation/documented] Providers are configured via a providers.json overlay in ~/.vix/ or ./.vix/ merged over an embedded base: same-id entries are field-patched, new ids appended, and models/credential_methods arrays replace wholesale. -- evidence: [PROVIDERS.md#L12-L13](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L12-L13), [README.md#L110-L112](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L110-L112), [PROVIDERS.md#L15-L16](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L15-L16), [PROVIDERS.md#L18-L23](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L18-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Users can define multi-phase agent pipelines in JSON with agent, bash, and tool steps, including templating, branching, parallelism, and history forking; custom workflows are configured in settings.json. -- evidence: [README.md#L25-L25](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L25-L25), [README.md#L159-L159](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L159-L159)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](vix.detail.md)

Metadata and full claim list: [full detail](vix.detail.md)
Human notes ([notes](vix.notes.md), never overwritten by build)

[Back to map index](../../index.md)
