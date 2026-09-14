# deepagent-ltd/deepagent-code -- full detail

[Back to orientation](deepagent-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/deepagent-ltd/deepagent-code/57be03002bc4f97476aceeb8b2666860edbc2633/0b8d0383da0604bb.json](../../../wiki/dossiers/deepagent-ltd/deepagent-code/57be03002bc4f97476aceeb8b2666860edbc2633/0b8d0383da0604bb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Three collaboration modes are offered: Auto (end-to-end execution), Loop (editable `goal+plan.md` advanced through plan, execute, verify, iterate ticks), and Design (faithful execution of a user-written plan); autonomy and permission levels are independent of mode. -- evidence: [README.md#L38-L42](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L38-L42), [README.md#L44-L44](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L44-L44) (`clm_ead25eab29b929c50ad91e7a5f2755df919d8dabba2ead37f599a5f7f32eb0a9`)
- [observation/documented] Context assembly uses a durable Context Epoch: stable system instructions stay byte-stable for prompt caching while volatile state is appended in a dedicated tail block, and context changes are admitted only at safe provider-turn boundaries. -- evidence: [CONTEXT.md#L39-L40](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/CONTEXT.md#L39-L40), [README.md#L79-L79](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L79-L79), [README.md#L81-L81](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L81-L81) (`clm_7d43ca997771a9a73ee3c124ea1adc7cbe2163bb18489bbc320cbff4a5d384b4`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product ships as a desktop app and a terminal CLI; the CLI supports `deepagent auth login`, `deepagent auth list`, and `deepagent-code run "<task>"`. -- evidence: [README.md#L107-L108](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L107-L108), [README.md#L161-L161](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L161-L161), [README.md#L164-L165](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L164-L165), [README.md#L202-L204](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L202-L204), [README.md#L143-L143](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L143-L143) (`clm_54771ee885d68ccc5c4750792639e52ed121b90a3747c4cefdade68ee4b46554`)
- [observation/documented] Providers are configured in `~/.deepagent/code/config.jsonc`; a custom OpenAI-compatible endpoint can set `discovery: true` for runtime model refresh or list models explicitly under `models`. -- evidence: [README.md#L169-L171](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L169-L171), [README.md#L173-L188](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L173-L188) (`clm_b526bd398a1ba102298cf99934337f3e19584661910112bc7809b387e1303448`)

## memory-state (2 claim(s))

- [observation/documented] Persistent state lives in typed documents (knowledge, strategy, methodology, skill, memory, design, worklog, diagnosis, eval) linked via supports/blocks/conflicts/validates into a traversable graph, with scope layers from session-private to sealed audit-only material. -- evidence: [README.md#L218-L218](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L218-L218), [README.md#L220-L220](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L220-L220) (`clm_28e6d3a3240321e8276a3f13a1f7554d883fa3ece3870444b9e4f00ede23033f`)
- [observation/documented] Learning follows a governed lifecycle: evidence creates a candidate, isolated review or human decision changes its status, and regression/ablation gates publish a reproducible knowledge snapshot; rejection reasons persist so discarded patterns are not silently relearned. -- evidence: [README.md#L66-L66](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L66-L66) (`clm_ccccd1d6a08d85c7d54bac050862c7777dc5632dd5833efc4b91ae7ac3c3a7f0`)

## orchestration (2 claim(s))

- [observation/documented] Write-capable subagents get dedicated worktrees and return compact summaries; a Reviewer session checks each exact worker SHA, the coordinator performs serial `--no-ff` merges, and generation fencing prevents stale workers from settling or overwriting newer work. -- evidence: [README.md#L97-L97](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L97-L97), [README.md#L95-L95](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L95-L95) (`clm_8816eb9058ae23b4ed3f99e85eb7a97a840410ca9c21a66301dc83963196c4aa`)
- [observation/documented] For high-risk decisions an Expert Panel reviews a frozen question through correctness, security, performance, architecture, and reproducibility lenses, debating anonymously up to three rounds before a deterministic arbiter that preserves minority opinions and fails closed to human review. -- evidence: [README.md#L99-L99](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L99-L99) (`clm_02bfd67211e541db19d07f1dea0d607b7eb65749e2da63599f7027bba43f32c8`)

## tools-permissions (1 claim(s))

- [observation/documented] The preset MCP catalog derives risk tiers from the catalog template rather than user config, and servers default to not-connected with write and external-fetch operations behind approval gates. -- evidence: [README.md#L226-L226](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L226-L226) (`clm_23081dd23f39173f016b8f9cf5aba564230e7a1160bbb8ba433677875c1df6ef`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project builds with Bun 1.3.14 and is provider-agnostic, supporting 75+ providers via the AI SDK and models.dev plus any OpenAI- or Anthropic-compatible endpoint. -- evidence: [README.md#L137-L139](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L137-L139), [README.md#L232-L232](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L232-L232) (`clm_6673651db53f53de51238100a758a96a3f38c7e41a8c8393ddbbb68db52363a0`)

## limitations (1 claim(s))

- [observation/documented] The `deepagent-code` npm package is not yet publicly published; installation is via the desktop app or a curl install script. -- evidence: [README.md#L107-L108](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L107-L108), [README.md#L112-L113](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L112-L113) (`clm_b6a1fe8e96f4337e9ffba6228b83f5e6bd7ee541dc29d05ef11e2270d79f2487`)

## relevance (1 claim(s))

- [observation/documented] The project is licensed AGPL-3.0-or-later and is derived from opencode under the MIT License with NOTICE attribution; an enterprise edition exists in a separate repository. -- evidence: [README.md#L278-L278](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L278-L278), [README.md#L11-L15](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L11-L15), [README.md#L276-L276](https://github.com/deepagent-ltd/deepagent-code/blob/57be03002bc4f97476aceeb8b2666860edbc2633/README.md#L276-L276) (`clm_6f658f2e0cb6000519a44b1de0a87934e4d06e6efca5fbb06f28fa916f986ba4`)

