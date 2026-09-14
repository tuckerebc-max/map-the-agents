# charmbracelet/fantasy -- full detail

[Back to orientation](fantasy.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/charmbracelet/fantasy/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/24e830b636a75709.json](../../../wiki/dossiers/charmbracelet/fantasy/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/24e830b636a75709.json)

## specifications (1 claim(s))

- [observation/documented] Fantasy is a Go library for building AI agents, offering multi-provider and multi-model support behind a single API. -- evidence: [README.md#L10-L10](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L10-L10) (`clm_7f1c67ae36e7a9343a45f00c40ceede4f15996adf247c77133a51d4f1beb6e93`)

## components (1 claim(s))

- [observation/documented] Custom tools are defined with fantasy.NewAgentTool, taking a name, description, and a function implementing the tool behavior. -- evidence: [README.md#L37-L42](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L37-L42) (`clm_508610f86caa71d8a60c0007f703645378f9a5f78c5389e42bc0fc152b606f99`)

## design-choices (1 claim(s))

- [observation/documented] Fantasy supports many providers via dedicated packages (e.g. Azure, Bedrock, OpenRouter) and a generic openaicompat layer for OpenAI-compatible providers. -- evidence: [README.md#L65-L65](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L65-L65) (`clm_5b62beeddb41f0cceebcf6b71ebd7ff84918cc5f5101daf82cc12153526f4c07`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors build with go build ./..., test via task test or go test with a 30m timeout, and lint/format using golangci-lint and gofumpt. -- evidence: [AGENTS.md#L5-L10](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L5-L10) (`clm_ca0202b988c8d7907b8680595a89a1420534460b8d6bd605e8ccf58feb8bc9f1`)
- [observation/documented] Repository development practice: provider integration tests use VCR cassettes in testdata, with API keys supplied via FANTASY_<PROVIDER>_API_KEY env vars loaded from .env, and the recorder injected as an http.Client transport. -- evidence: [AGENTS.md#L28-L29](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L28-L29), [AGENTS.md#L20-L24](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L20-L24) (`clm_c210ef6ff92d634ad5e213f0898363670b8f34945e7c5920323c7154ea61b5ab`)
- [observation/documented] Repository development practice: style notes prefer cmp.Or for defaults, use json/description/enum struct tags for schema generation, and use charm.land/x/vcr rather than go-vcr for HTTP test recording. -- evidence: [AGENTS.md#L14-L16](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/AGENTS.md#L14-L16) (`clm_8374dcf6a5449d05bc5027669e5d3eef0dd0489cc761195d0962650a7f29ee71`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Providers are instantiated via constructors like openrouter.New with an API-key option, and language models are obtained by calling provider.LanguageModel with a context and model name. -- evidence: [README.md#L21-L26](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L21-L26), [README.md#L30-L35](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L30-L35) (`clm_faefd5fdf77346e204c2b2d6ae2944222a61de8860daf1eed8b67f20029a7618`)
- [observation/documented] Agents are created with fantasy.NewAgent, accepting a model plus options such as WithSystemPrompt and WithTools, and run via agent.Generate with an AgentCall containing a prompt. -- evidence: [README.md#L51-L59](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L51-L59), [README.md#L44-L49](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L44-L49) (`clm_264f186b7d3181da23bee4b706e4acaf3ce0087d544c74a78089e42b21d13f0d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The library is imported as charm.land/fantasy, with provider packages such as charm.land/fantasy/providers/openrouter. -- evidence: [README.md#L17-L19](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L17-L19) (`clm_1ddcc2f3ba435779332b7fc26cfe40eb7fc9c299f1650767e9a508b214ff629f`)

## limitations (1 claim(s))

- [observation/documented] The README states Fantasy does not yet support image models, audio models, or PDF uploads, and is a work in progress. -- evidence: [README.md#L69-L69](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L69-L69), [README.md#L71-L73](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L71-L73) (`clm_29831ec274fcf5937cae4b3b81c1c5fcdab06c0e5dd9191045fdfcb3dc124e2f`)

## relevance (1 claim(s))

- [observation/documented] Fantasy was built to power Crush, Charm's coding agent. -- evidence: [README.md#L69-L69](https://github.com/charmbracelet/fantasy/blob/1dada21b01e8fd8db05e8a784f52e2536fe20aaf/README.md#L69-L69) (`clm_bd944c45bd695753a1a2348fdd9ad8d9a9dbb3c45171cf89d457a37e536eadbe`)

