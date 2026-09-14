# eigent-ai/eigent -- full detail

[Back to orientation](eigent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/eigent-ai/eigent/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/dc36965489dec4b6.json](../../../wiki/dossiers/eigent-ai/eigent/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/dc36965489dec4b6.json)

## specifications (1 claim(s))

- [observation/documented] Eigent is described as an open-source Cowork desktop application for building, managing, and deploying a custom AI workforce that automates complex workflows. -- evidence: [README.md#L31-L31](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L31-L31) (`clm_3ddca9421ca9d823ab50eb698e2b57535c00f670b98948439c2e2107d9734d0b`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The product is stated to be model agnostic, supporting cloud APIs, enterprise gateways, or local inference without vendor lock-in. -- evidence: [README.md#L37-L46](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L37-L46), [README.md#L185-L185](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L185-L185) (`clm_0cd1cfba6dc6c4de7008977af3236f8fe7838de1843c877af098eab435172096`)
- [observation/documented] Local deployment is the recommended mode: a local backend server with full API, local model integration (vLLM, Ollama, LM Studio, etc.), and complete isolation from cloud services with no account required. -- evidence: [README.md#L102-L105](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L102-L105), [README.md#L96-L96](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L96-L96), [README.md#L124-L124](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L124-L124) (`clm_5e89279db8a8c38249c09d3ca72fe98ccb4515a475f9c93f80f6818020a80cff`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: the cloud-connected quick start instructs cloning the repo, running npm install and npm run dev (Node.js 18-22 required), and notes this mode connects to Eigent cloud services and needs account registration. -- evidence: [README.md#L113-L113](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L113-L113), [README.md#L117-L122](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L117-L122), [README.md#L124-L124](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L124-L124) (`clm_b7ec62227388422a78b4c64e18238f81600a2d5a3a5b32f5e91188cc1674ce12`)
- [observation/documented] Repository development practice: after pulling new code, contributors are told to update frontend dependencies with npm install and backend Python dependencies via 'cd backend && uv sync'. -- evidence: [README.md#L132-L132](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L132-L132), [README.md#L135-L137](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L135-L137), [README.md#L128-L128](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L128-L128) (`clm_bc70d67b67758725482d6cbe426c0108e785faa7ddbd66d27c4fd4c94933ef90`)
- [observation/documented] Repository development practice: the design-system document gives UI agents an ordered inspection procedure (design contract, existing surfaces, primitives, tokens, exception registry) and a conflict priority list starting with accessibility and product behavior. -- evidence: [docs/design-system/design.md#L17-L22](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/docs/design-system/design.md#L17-L22), [docs/design-system/design.md#L15-L15](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/docs/design-system/design.md#L15-L15), [docs/design-system/design.md#L24-L24](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/docs/design-system/design.md#L24-L24), [docs/design-system/design.md#L26-L30](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/docs/design-system/design.md#L26-L30) (`clm_5aee51c23e087c19e755fb0cf712d9c62b4097db0bfcaba615d2471f422507f0`)
- [observation/documented] Repository development practice: generated files under src/style/generated must never be hand-edited; token changes require regenerating via 'npm run generate:design-tokens'. -- evidence: [docs/design-system/design.md#L67-L69](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/docs/design-system/design.md#L67-L69), [docs/design-system/design.md#L64-L65](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/docs/design-system/design.md#L64-L65) (`clm_c3906a011990989509534874d44115491132eda1c25faaef6b404c97fe1895fa`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The README lists built-in browser and terminal toolkits, MCP integration, and skill integration as product capabilities. -- evidence: [README.md#L37-L46](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L37-L46) (`clm_558e64a638d1e4bf58cc9ddc47b2c286bfdd8a1534d496465c6eda0c5fe73a5d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The product advertises a multi-agent workforce that divides work among specialized agents, collaborates in parallel, and executes multi-step workflows, alongside a single-agent mode for focused tasks. -- evidence: [README.md#L33-L33](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L33-L33), [README.md#L173-L173](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L173-L173), [README.md#L37-L46](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L37-L46), [README.md#L169-L169](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L169-L169) (`clm_108e42a45a15a216322d2142ab3cc82dabcd518cb3d0f2ac330d8a3a39d141fe`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The backend stack is documented as FastAPI with uv as package manager, Uvicorn as async server, OAuth 2.0 and Passlib for authentication, and CAMEL as the multi-agent framework. -- evidence: [README.md#L255-L259](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L255-L259) (`clm_36f76731b7f637e0c9704612d5725b8cec9547cd996805606e70da93e9fda16e`)
- [observation/documented] The frontend is documented as React with Electron for the desktop app, TypeScript, Tailwind CSS, Radix UI, Zustand for state, and React Flow as flow editor. -- evidence: [README.md#L263-L268](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L263-L268) (`clm_fccba73c762e329c65466b47e46329450495d51d8ef2216839039a64e1a37fe7`)

## limitations (1 claim(s))

- [inference/documented] The roadmap table lists items such as prompt caching, context compression, fixed-workflow workforce support, and forbidding repeated page visits as future work, suggesting these capabilities are not yet present. -- evidence: [README.md#L282-L290](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L282-L290) (`clm_0ab86833e6e549ddf792003e7b969a19691d2b71bf393cfa5d2df659608d989a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

