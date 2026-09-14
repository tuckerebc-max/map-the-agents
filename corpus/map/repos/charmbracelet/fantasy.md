# charmbracelet/fantasy

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1dada21b01e8 @ 24e830b636a75709

## Summary (orientation draft, not independently verified)

Fantasy is a Go library for building AI agents, offering multi-provider and multi-model support behind a single API. Providers are instantiated via constructors like openrouter.New with an API-key option, and language models are obtained by calling provider.LanguageModel with a context and model name.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Fantasy is a Go library for building AI agents, offering multi-provider and multi-model support behind a single API. -- evidence: [README.md#L10-L10](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L10-L10)
- components (1 claim(s)):
  - [observation/documented] Custom tools are defined with fantasy.NewAgentTool, taking a name, description, and a function implementing the tool behavior. -- evidence: [README.md#L37-L42](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L37-L42)
- design-choices (1 claim(s)):
  - [observation/documented] Fantasy supports many providers via dedicated packages (e.g. Azure, Bedrock, OpenRouter) and a generic openaicompat layer for OpenAI-compatible providers. -- evidence: [README.md#L65-L65](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L65-L65)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors build with go build ./..., test via task test or go test with a 30m timeout, and lint/format using golangci-lint and gofumpt. -- evidence: [AGENTS.md#L5-L10](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L5-L10)
  - [observation/documented] Repository development practice: provider integration tests use VCR cassettes in testdata, with API keys supplied via FANTASY_<PROVIDER>_API_KEY env vars loaded from .env, and the recorder injected as an http.Client transport. -- evidence: [AGENTS.md#L28-L29](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L28-L29), [AGENTS.md#L20-L24](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L20-L24)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Providers are instantiated via constructors like openrouter.New with an API-key option, and language models are obtained by calling provider.LanguageModel with a context and model name. -- evidence: [README.md#L21-L26](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L21-L26), [README.md#L30-L35](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L30-L35)
  - [observation/documented] Agents are created with fantasy.NewAgent, accepting a model plus options such as WithSystemPrompt and WithTools, and run via agent.Generate with an AgentCall containing a prompt. -- evidence: [README.md#L51-L59](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L51-L59), [README.md#L44-L49](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L44-L49)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The library is imported as charm.land/fantasy, with provider packages such as charm.land/fantasy/providers/openrouter. -- evidence: [README.md#L17-L19](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L17-L19)
- limitations (1 claim(s)):
  - [observation/documented] The README states Fantasy does not yet support image models, audio models, or PDF uploads, and is a work in progress. -- evidence: [README.md#L69-L69](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L69-L69), [README.md#L71-L73](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L71-L73)
- relevance (1 claim(s)):
  - [observation/documented] Fantasy was built to power Crush, Charm's coding agent. -- evidence: [README.md#L69-L69](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L69-L69)

(1 additional claim(s) omitted for length; see [full detail](fantasy.detail.md) for every claim.)

Metadata and full claim list: [full detail](fantasy.detail.md)
Human notes ([notes](fantasy.notes.md), never overwritten by build)

[Back to map index](../../index.md)
