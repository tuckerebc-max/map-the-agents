# golutra/golutra -- full detail

[Back to orientation](golutra.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/golutra/golutra/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/fd003868b702a204.json](../../../wiki/dossiers/golutra/golutra/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/fd003868b702a204.json)

## specifications (1 claim(s))

- [observation/documented] golutra is described as a multi-agent workspace that turns existing CLI tools into a unified AI collaboration hub, emphasizing parallel execution, orchestration, and real-time result tracking. -- evidence: [README.md#L69-L69](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L69-L69) (`clm_af32b348b5ad9f7cf35e3443251466b0aa4c381dc2e93fddef8bf4b62016df53`)

## components (1 claim(s))

- [observation/documented] The app is built with Vue 3 and Rust as a Tauri desktop application targeting Windows, macOS, and Linux. -- evidence: [README.md#L71-L71](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L71-L71), [README.md#L207-L207](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L207-L207) (`clm_2ba93a3f097803dfe4f2057e66d5ab2567a146eae7e2dc5ce55bc69185c83369`)

## design-choices (1 claim(s))

- [observation/documented] The product supports custom workflows with one-click template import/export, aimed at long-running automation across varied scenarios such as novel writing and video production. -- evidence: [README.md#L73-L73](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L73-L73), [README.md#L209-L209](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L209-L209), [README.md#L91-L96](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L91-L96) (`clm_501497353dc2fc7e02a667e906f4d781e8b5ab5b836f904efd0f6c89ed2c0543`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must fork, create a feature branch, open a PR with a template disclosing identity, third-party sources, AI assistance, and co-authors, and sign the ICLA via a bot-managed CLA check. -- evidence: [CONTRIBUTING.md#L21-L21](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/CONTRIBUTING.md#L21-L21), [CONTRIBUTING.md#L53-L59](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/CONTRIBUTING.md#L53-L59), [CONTRIBUTING.md#L13-L19](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/CONTRIBUTING.md#L13-L19) (`clm_fd9873b6a2fc473dc7f0500500e19e2ef4b381c661443d7cb4e12124ba568670`)
- [observation/documented] Repository development practice: organizational contributions additionally require a CCLA or equivalent written authorization from an authorized signer, with the authorization number registered in corporate-authorizations.json and cited in the PR. -- evidence: [CONTRIBUTING.md#L53-L59](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/CONTRIBUTING.md#L53-L59), [CONTRIBUTING.md#L23-L24](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/CONTRIBUTING.md#L23-L24), [CLA.md#L5-L7](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/CLA.md#L5-L7) (`clm_5520e7cf4664fe490f8fbf413b110c6800dbc186a494db4386388c40e6d1efc9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product supports a compatibility layer for multiple CLI agents, listing Claude Code, Gemini CLI, Codex CLI, OpenCode, Qwen Code, OpenClaw, and 'Any CLI'. -- evidence: [README.md#L29-L48](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L29-L48), [README.md#L108-L114](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L108-L114), [README.md#L244-L250](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L244-L250) (`clm_87b7e72a5730c92b327a22725230477c8da40cd8a76a7ad79352426f8a77e7a5`)
- [observation/documented] Users can click agent avatars to inspect logs, inject prompts directly into terminal streams, and monitor execution while agents run in the background. -- evidence: [README.md#L71-L71](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L71-L71), [README.md#L137-L138](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L137-L138), [README.md#L207-L207](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L207-L207) (`clm_4a8e2c89256370914e6ba21bd5ac87d0cfb4849b924a1c909d2567e219599ed7`)
- [observation/documented] A companion project, golutra-mcp, provides a way to connect external tools and agents through golutra-cli for MCP-based workflow integration. -- evidence: [README.md#L221-L221](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L221-L221), [README.md#L85-L85](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L85-L85) (`clm_853e41970a48b1abc2e321bfcb9a25750a264aab1cde00336ff483cec533e4ba`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is distributed under Business Source License 1.1, with commercial use of golutra as a tool allowed and user-produced outputs belonging to users. -- evidence: [README.md#L14-L18](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L14-L18), [README.md#L322-L324](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L322-L324), [README.md#L187-L189](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L187-L189) (`clm_2309b0ca8846d5d0ed21469d0219af3a227f69bcb45441899e186f8ebb83503d`)

## limitations (1 claim(s))

- [observation/documented] The README states the project is at an early stage, with a CEO Agent layer, agent self-evolution, cross-device migration, and mobile remote control listed as future capabilities rather than current ones. -- evidence: [README.md#L166-L166](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L166-L166), [README.md#L306-L306](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L306-L306), [README.md#L308-L313](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L308-L313), [README.md#L168-L168](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L168-L168), [README.md#L302-L302](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L302-L302), [README.md#L172-L177](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md#L172-L177) (`clm_4952aae15cc7ebb7e8e739db852811674685bf112259bbd11e1b672592cb4a87`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

