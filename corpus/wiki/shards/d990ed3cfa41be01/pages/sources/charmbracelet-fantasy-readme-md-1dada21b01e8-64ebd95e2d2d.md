---
access: public
aliases: []
claim_ids:
- clm_1ddcc2f3ba435779332b7fc26cfe40eb7fc9c299f1650767e9a508b214ff629f
- clm_264f186b7d3181da23bee4b706e4acaf3ce0087d544c74a78089e42b21d13f0d
- clm_29831ec274fcf5937cae4b3b81c1c5fcdab06c0e5dd9191045fdfcb3dc124e2f
- clm_508610f86caa71d8a60c0007f703645378f9a5f78c5389e42bc0fc152b606f99
- clm_5b62beeddb41f0cceebcf6b71ebd7ff84918cc5f5101daf82cc12153526f4c07
- clm_7f1c67ae36e7a9343a45f00c40ceede4f15996adf247c77133a51d4f1beb6e93
- clm_bd944c45bd695753a1a2348fdd9ad8d9a9dbb3c45171cf89d457a37e536eadbe
- clm_faefd5fdf77346e204c2b2d6ae2944222a61de8860daf1eed8b67f20029a7618
maturity: draft
page_id: pg_4ab4c8994e985932928d64ebd95e2d2d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_661f9c47939a5bed97e9115ebb1a2e5c
title: charmbracelet/fantasy/README.md @ 1dada21b01e8
updated_at: '2026-09-14T03:06:09Z'
---

# charmbracelet/fantasy/README.md @ 1dada21b01e8

<!-- rcw:begin owner=source:src_661f9c47939a5bed97e9115ebb1a2e5c block=evidence -->
- The library is imported as charm.land/fantasy, with provider packages such as charm.land/fantasy/providers/openrouter. [@claim:clm_1ddcc2f3ba435779332b7fc26cfe40eb7fc9c299f1650767e9a508b214ff629f]
- Agents are created with fantasy.NewAgent, accepting a model plus options such as WithSystemPrompt and WithTools, and run via agent.Generate with an AgentCall containing a prompt. [@claim:clm_264f186b7d3181da23bee4b706e4acaf3ce0087d544c74a78089e42b21d13f0d]
- The README states Fantasy does not yet support image models, audio models, or PDF uploads, and is a work in progress. [@claim:clm_29831ec274fcf5937cae4b3b81c1c5fcdab06c0e5dd9191045fdfcb3dc124e2f]
- Custom tools are defined with fantasy.NewAgentTool, taking a name, description, and a function implementing the tool behavior. [@claim:clm_508610f86caa71d8a60c0007f703645378f9a5f78c5389e42bc0fc152b606f99]
- Fantasy supports many providers via dedicated packages (e.g. Azure, Bedrock, OpenRouter) and a generic openaicompat layer for OpenAI-compatible providers. [@claim:clm_5b62beeddb41f0cceebcf6b71ebd7ff84918cc5f5101daf82cc12153526f4c07]
- Fantasy is a Go library for building AI agents, offering multi-provider and multi-model support behind a single API. [@claim:clm_7f1c67ae36e7a9343a45f00c40ceede4f15996adf247c77133a51d4f1beb6e93]
- Fantasy was built to power Crush, Charm's coding agent. [@claim:clm_bd944c45bd695753a1a2348fdd9ad8d9a9dbb3c45171cf89d457a37e536eadbe]
- Providers are instantiated via constructors like openrouter.New with an API-key option, and language models are obtained by calling provider.LanguageModel with a context and model name. [@claim:clm_faefd5fdf77346e204c2b2d6ae2944222a61de8860daf1eed8b67f20029a7618]
<!-- rcw:end owner=source:src_661f9c47939a5bed97e9115ebb1a2e5c block=evidence -->

## Researcher notes

