# kristoferlund/duet-gpt -- full detail

[Back to orientation](duet-gpt.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kristoferlund/duet-gpt/6e28904075b593b03ca8a31924ae8acd5f7cea32/539778bb614080db.json](../../../wiki/dossiers/kristoferlund/duet-gpt/6e28904075b593b03ca8a31924ae8acd5f7cea32/539778bb614080db.json)

## specifications (1 claim(s))

- [observation/documented] DuetGPT is an experimental AI-powered CLI tool and semi-autonomous agent that helps developers with coding and file system tasks. -- evidence: [README.md#L5-L5](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L5-L5) (`clm_376099eb2fa171100dac3317388f18fab5152e87e26810640d556d1922020fd6`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [inference/documented] The approval step before command execution appears to be the product's core safety mechanism, since the README describes automatic execution only after developer approval. -- evidence: [README.md#L5-L5](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L5-L5) (`clm_7ba89c6aa92eb70aae21bb18e99cff662b735a79e569a55605d289b638b9dfae`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Example tasks include refactoring code, writing bash scripts, searching files for text, and drafting PR descriptions from commit messages; it is also described as a general bash helper. -- evidence: [README.md#L16-L19](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L16-L19), [README.md#L7-L7](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L7-L7) (`clm_6b33ceec78816b1cfa5d71d9c8ce81748b124806bb367d73cd2cfb76e85e1021`)

## interfaces (3 claim(s))

- [observation/documented] The developer describes a task; the AI issues commands or follow-up questions, and after developer approval DuetGPT automatically executes the commands. -- evidence: [README.md#L5-L5](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L5-L5) (`clm_e600e51cf5eff6e022fe34badd64dbec88875b281c301479f40b88920882e042`)
- [observation/documented] Installed globally via npm as duet-gpt and started with the duet-gpt command; on first run it prompts for an OpenAI API key. -- evidence: [README.md#L45-L45](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L45-L45), [README.md#L31-L31](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L31-L31), [README.md#L39-L39](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L39-L39), [README.md#L41-L43](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L41-L43), [README.md#L33-L35](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L33-L35) (`clm_d1a68de2df1a07a21139e916e87ef6ebf5ff8c4101bddf20cd02a5e7cf8461a8`)
- [observation/documented] A configuration screen added before app start allows the user to change settings such as the API key. -- evidence: [CHANGELOG.md#L12-L12](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/CHANGELOG.md#L12-L12) (`clm_7ed283e6241a2bd913bdffd340c66f1e72be3e69a6646d3d79eb7331b745f33b`)

## memory-state (1 claim(s))

- [observation/documented] A changelog entry indicates AI assistant responses are added to memory, and the sample interaction shows 'LLM and memory started' at launch. -- evidence: [README.md#L94-L158](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L94-L158), [CHANGELOG.md#L18-L26](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/CHANGELOG.md#L18-L26) (`clm_57b809944a359776734d03d2bbbb759fc21d290e7a2e7b28ba5bbd6c329c68e4`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project no longer uses langchain, relying instead on OpenAI function calling, which the author says improved reliability and performance. -- evidence: [CHANGELOG.md#L32-L34](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/CHANGELOG.md#L32-L34), [README.md#L3-L3](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L3-L3) (`clm_d88f3a9f14892bc2275e3735c81cd9a84822a72a430a22d173b36d7402513227`)
- [observation/documented] Works with OpenAI models gpt-3.5-turbo-0613 (noted as not producing great code) and gpt-4-0613. -- evidence: [README.md#L11-L12](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L11-L12), [README.md#L9-L9](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L9-L9) (`clm_df7a80fa8f76bee3f90dde48a76a7570bf3ca2b7e8736c617b2851f454236131`)

## limitations (1 claim(s))

- [observation/documented] Known issue: when proposing changes to large files the AI may return incomplete results due to the limited gpt-4 context window; it works best with small files. -- evidence: [README.md#L164-L164](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L164-L164) (`clm_fa0114844b315731b5b1bd9e994af92220b4e63e7a89de114c4f74af8bdd97b9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

