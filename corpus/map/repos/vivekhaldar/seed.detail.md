# vivekhaldar/seed -- full detail

[Back to orientation](seed.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vivekhaldar/seed/cd79a60acafe425f8bd31078996d5818bb151ad6/1c4ee6f29e9155bf.json](../../../wiki/dossiers/vivekhaldar/seed/cd79a60acafe425f8bd31078996d5818bb151ad6/1c4ee6f29e9155bf.json)

## specifications (1 claim(s))

- [observation/documented] The README describes seed.py as calling a language model with a single exec tool that runs shell commands, loading its system prompt from self/SELF.md, with the agent able to edit self/ to retain tools, notes, and behavior between sessions. -- evidence: [README.md#L5-L7](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L5-L7) (`clm_1c21cb6e16de6c98bffd03a5bacee83ebb995cd1367701fc65ecb8807dbbf5c3`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The design doc states the seed prompt and the agent's self-description were collapsed into the same mutable file: the loop's only hardcoded context decision is reading self/SELF.md, re-read every turn so self-edits take effect immediately. -- evidence: [docs/DESIGN.md#L116-L125](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L116-L125) (`clm_20cf0afd1bfc4fbfa799056a44053e60c1ad0c62da330a877eb445ace790d2ed`)
- [observation/documented] The license text labels itself Sovereign Source License v0.3 and describes an Apache 2.0 extension with optional development-data services. It says basic use under Apache 2.0 terms involves no data collection. -- evidence: [SovereignLicense.md#L135-L135](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/SovereignLicense.md#L135-L135), [SovereignLicense.md#L11-L11](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/SovereignLicense.md#L11-L11), [README.md#L99-L101](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L99-L101) (`clm_52f744dcb896bdb82625534c942f6a7320cc5677be56c04fbb8d0b68b5776252`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (1 claim(s))

- [observation/documented] Documentation states each session is fresh and its conversation is discarded on exit, so nothing survives except what the agent wrote into self/; a separate verbatim transcript is recorded per session as a flight recorder that is never loaded at boot. -- evidence: [README.md#L42-L45](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L42-L45), [docs/DESIGN.md#L127-L132](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L127-L132) (`clm_caa1e9c43fbcf3d467be6d59e5648a07cfc0d73779707ab8f83efa73f16a1425`)

## orchestration (1 claim(s))

- [observation/documented] Documentation states planting creates a fresh, private git repo at the target directory (or nests git under self/ inside an existing repo) and never overwrites an existing seed.py or run_seed.sh, so a grown loop cannot be clobbered by a later plant. -- evidence: [docs/DESIGN.md#L151-L158](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L151-L158), [docs/DESIGN.md#L160-L173](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L160-L173), [README.md#L27-L32](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L27-L32) (`clm_7579999285389999537281730cc0a3fe6ef67362161033c0032b571d2eb7cb78`)

## tools-permissions (2 claim(s))

- [observation/documented] The design doc states the one irreducible primitive is exec: the seed ships exactly one tool that runs a bash command and returns its output, with every other capability expressed through it rather than compressed further. -- evidence: [docs/DESIGN.md#L101-L107](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L101-L107) (`clm_b0cd2e8c122e601bf592a9351e866f9f379e5e2c585889bc9ed34600889af803`)
- [observation/documented] Setup is documented as detecting an existing provider credential or asking interactively, verifying it with one minimal model request unless --no-verify is passed, and storing a pasted key only in llm's user-level key store, never writing it into run_seed.sh, seed.py, or git. -- evidence: [README.md#L79-L83](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L79-L83), [README.md#L52-L55](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L52-L55), [README.md#L20-L25](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L20-L25) (`clm_c51554f832154dc9ec002117528db5497c86f528de2a0c23195766dc20bd08b1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Documentation states models and keys are handled by Simon Willison's llm library, chosen over LiteLLM, PydanticAI, and a raw OpenAI SDK/OpenRouter combination for its multi-provider plugin model, per-conversation session state, and plain-function tool calling. -- evidence: [README.md#L52-L55](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/README.md#L52-L55), [docs/DESIGN.md#L175-L194](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L175-L194) (`clm_4ac7621e362e7ff4a6a5eaa471539192141fd7f2d8c224814b79729ccfbf7448`)

## limitations (1 claim(s))

- [observation/documented] The risk register documents ungated exec as a consciously accepted risk: the agent runs arbitrary bash as the invoking user with no sandbox or approval gate, though every command and its output is printed to the terminal. -- evidence: [docs/DESIGN.md#L198-L209](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L198-L209) (`clm_7ccdf33d506a3508ca4925ede4604280a7f8cae461bb8f01c7a5879cbcb880ab`)

## relevance (1 claim(s))

- [observation/documented] The design document frames its distinct claim as germinating a personal agent from an auditable seed in dialogue, with conversation as selection pressure rather than a benchmark-driven optimization loop. -- evidence: [docs/DESIGN.md#L92-L97](https://github.com/vivekhaldar/seed/blob/cd79a60acafe425f8bd31078996d5818bb151ad6/docs/DESIGN.md#L92-L97) (`clm_7470a553d2958b5c1989a003d9ebff2ee12c2ab84ae770dc2593dbcacde1fcf5`)

