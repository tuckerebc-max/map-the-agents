# irgolic/autopr -- full detail

[Back to orientation](autopr.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/irgolic/autopr/a95671a20d8d3e3265768ffecf750ac07abc17cd/29ca6eca824e6f47.json](../../../wiki/dossiers/irgolic/autopr/a95671a20d8d3e3265768ffecf750ac07abc17cd/29ca6eca824e6f47.json)

## specifications (1 claim(s))

- [observation/documented] AutoPR is a GitHub Action that automatically writes pull requests in response to issues, per its usage guide. -- evidence: [USAGE.md#L4-L4](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L4-L4) (`clm_3dc4bafe7ae41a81772fe7063e68430f8163578031ae6c0113ad264770e6a7a0`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Triggered runs create a branch named autopr/issue-# and open a PR to the base branch; an existing branch is overwritten by default behavior described in the usage steps. -- evidence: [USAGE.md#L27-L31](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L27-L31) (`clm_e22c83a7df8d3c7a5bcc5094a8841d3d99472d82df2767efffb365d120c2d8c7`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors extend AutoPR by subclassing Action (with an id and run method) or Agent (with handle_event), and actions share state via a ContextDict passed between actions. -- evidence: [CONTRIBUTING.md#L57-L57](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L57-L57), [CONTRIBUTING.md#L18-L18](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L18-L18), [CONTRIBUTING.md#L51-L51](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L51-L51), [CONTRIBUTING.md#L26-L29](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L26-L29) (`clm_399d16008598e563f5393cf1f00baae7e37cec11739885977cfcd5d1dd0a184a`)
- [observation/documented] Repository development practice: each rail run makes two LLM calls — a natural-language chat message, then a guardrails call serializing the response to typed JSON. -- evidence: [CONTRIBUTING.md#L117-L119](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L117-L119) (`clm_b653979a20ef02eb3857e1d830d13833759dc79f1f4d1d0fba37233b746f4c0b`)
- [observation/documented] Repository development practice: only the IssueLabeledEvent event type is currently supported, with events defined in autopr/models/events.py. -- evidence: [CONTRIBUTING.md#L102-L103](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/CONTRIBUTING.md#L102-L103) (`clm_778e6a72ac56a618bb891b46e62e44b2cd49daeae71496fa3b050c9f1003a60a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The action is invoked as docker://ghcr.io/irgolic/autopr:latest and configured through workflow 'with:' parameters such as github_token and model. -- evidence: [USAGE.md#L59-L68](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L59-L68), [USAGE.md#L46-L53](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L46-L53) (`clm_8a908aa0db557dcadaacbe630929da67d1b031907ca55d3d8243a7d9fed71b82`)
- [observation/documented] Documented inputs include github_token (required), base_branch (default main), model (default gpt-4), context_limit (8192), min/max_tokens, num_reasks, temperature, agent_id (default plan_and_code), and overwrite_existing. -- evidence: [USAGE.md#L78-L90](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L78-L90) (`clm_7a763f6f905b4edb71d175b28021efd7ec78915dcb8c4aa4593b542ead89a167`)
- [observation/documented] The plan_and_code agent accepts agent_config options: planning_actions, codegen_actions, and max_codegen_iterations (default 5). -- evidence: [USAGE.md#L110-L110](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L110-L110), [USAGE.md#L112-L114](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L112-L114) (`clm_2408e8f33183dcd90e2ff8396d9e8056f0117cf12876ef72c30161a837da3c89`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] When an issue gets a label containing 'AutoPR', the bot plans a fix, writes code, pushes a branch, and opens a pull request. -- evidence: [README.md#L39-L42](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L39-L42), [README.md#L37-L37](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L37-L37) (`clm_af541d84286334777ab40c323ac8dcd3fdf5a51e4daf79d4acab23d8804e7a14`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] AutoPR is built with Guardrails, described as prompting LLMs to generate structured data with JSON Schemas and re-asking when output does not adhere. -- evidence: [README.md#L17-L18](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L17-L18), [README.md#L29-L31](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L29-L31) (`clm_33c5062df646da823faccacd3f49ca95de497afc703a2b5a9f01dc7fb7864602`)
- [observation/documented] The action requires an OpenAI API key with ChatGPT access, supplied via the OPENAI_API_KEY secret. -- evidence: [USAGE.md#L10-L11](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L10-L11), [USAGE.md#L17-L21](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L17-L21) (`clm_4d9e084e52aebd01a63ef21deb59a10ecda8e047199fe5d28a37469d293e15a1`)

## limitations (3 claim(s))

- [observation/documented] The README lists known defects: incorrectly referencing code in other files, duplicating lines, calling nonexistent functions, and only working on GitHub. -- evidence: [README.md#L61-L64](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L61-L64) (`clm_a7c1bd809b6bccca6ee7ae185620ef39702c0e69844ef976f4bfb6b015033652`)
- [observation/documented] The GitHub Action was in development and in alpha release at the time of writing. -- evidence: [README.md#L57-L57](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L57-L57) (`clm_b5c91ddb35409d23a2623207d53087bd6b139df6eb10b35e87e7a366432a8707`)
- [observation/documented] AutoPR is documented as not optimized for gpt-3.5-turbo; users with gpt-4 API access are advised to use that instead. -- evidence: [USAGE.md#L70-L74](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/USAGE.md#L70-L74) (`clm_660a173d9b27c35f74bfa43ba91ce0d633d206d9c26673ab15560e4832570687`)

## relevance (1 claim(s))

- [inference/documented] The README frames the project as a historical demo from early 2023 that worked only about 20% of the time, so it appears to be of archival rather than production value. -- evidence: [README.md#L26-L27](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L26-L27), [README.md#L24-L24](https://github.com/irgolic/AutoPR/blob/a95671a20d8d3e3265768ffecf750ac07abc17cd/README.md#L24-L24) (`clm_5f0f5e7f4c83e17652c1c69ac12a58e307611ac411b2eb02f0d7c7fecc320a3f`)

