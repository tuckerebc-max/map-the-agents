# rawwerks/recursive-coding-agents -- full detail

[Back to orientation](recursive-coding-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rawwerks/recursive-coding-agents/0c71127a731c33b1e2db458280aac1c4cdc254fe/84739f8a75fa1e91.json](../../../wiki/dossiers/rawwerks/recursive-coding-agents/0c71127a731c33b1e2db458280aac1c4cdc254fe/84739f8a75fa1e91.json)

## specifications (2 claim(s))

- [observation/documented] The repo defines Recursive Language Models (RLMs) as systems that keep context as symbolic state, inspect and slice it with code, call models or agents over slices, and aggregate results verifiably. -- evidence: [README.md#L9-L9](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L9-L9) (`clm_8d390bb8f8460d636fcdc11861db6754deaa2fc587ce513a57953e3e087f7529`)
- [observation/documented] A one-line RLM definition states the task context moves into a persistent executable environment, the root model works through handles, and final answers return through the outer model-call interface. -- evidence: [README.md#L40-L40](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L40-L40) (`clm_96d149639f2c716d58f9ad730264ea548c90312f03a5e88148c4a9873d7e3dfd`)

## components (2 claim(s))

- [observation/documented] The repository contains four main parts: a SvelteKit web deck, an rlm-rubric directory, Claude Code workflow examples, and OpenProse program examples. -- evidence: [README.md#L26-L32](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L26-L32) (`clm_818a0386e1685d777421725e5856dc32aae5fc72915f90643751edc4bb8a9634`)
- [observation/documented] The rubric directory includes an RLM definition, a seven-gate rubric, and a judging methodology document for evidence-based system judgment. -- evidence: [README.md#L15-L22](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L15-L22), [README.md#L26-L32](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L26-L32) (`clm_5e0b569c37b01eaf2352f7477fcb236d8549bf8f1e98dfa99d6f5e8d204ec123`)

## design-choices (2 claim(s))

- [observation/documented] Example folders are verdict-shaped: files under rlm/ are passing or intended-passing examples, while not-rlm/ holds nearby negative controls. -- evidence: [README.md#L34-L34](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L34-L34) (`clm_a0fd590c6161d104aba847c616fe6c38c5e4f983986fb8d75de79c7c904a366a`)
- [observation/documented] Judging is by run shape rather than product label: a full RLM requires externalized context behind handles, model-chosen decomposition, programmatic calls over slices, and symbolic aggregation. -- evidence: [README.md#L36-L36](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L36-L36) (`clm_bd9f11e1326185da122390fd41494ec98e5fb591598035e49fcac6aad8ee44a3`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors run bun-based checks from web/ including svelte-check, design, social-metadata, and theme tests, plus a production build. -- evidence: [DEVELOPING.md#L21-L27](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L21-L27) (`clm_b933783ad3c597cb134ee41a179cfa720cc3690c750888bfab7e21fb8c8e416c`)
- [observation/documented] Repository development practice: pre-commit hooks run gitleaks on staged changes, and pre-push hooks only remind maintainers that deploys are explicit; hooks are activated via core.hooksPath. -- evidence: [DEVELOPING.md#L38-L38](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L38-L38), [DEVELOPING.md#L40-L42](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L40-L42), [DEVELOPING.md#L44-L46](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L44-L46) (`clm_540ff36e8eb299c92a09c4cedce5d63d92111d817d2a752fb66ba5951c3cbefd`)
- [observation/documented] Repository development practice: production deploys go through a checked scripts/deploy-web.sh wrapper or wrangler, require maintainer Cloudflare authentication, and tokens must never be passed on command lines. -- evidence: [DEVELOPING.md#L64-L67](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L64-L67), [DEVELOPING.md#L69-L71](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L69-L71), [DEVELOPING.md#L54-L60](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L54-L60) (`clm_458ab9d8876580755cdb588d524874b34cde4d4ed3ab7ad9e47808a620c1d784`)
- [observation/documented] Repository development practice: slide content is authored as mdsvex files in web/src/slides/ with ordering controlled by order.ts, and slides support metadata props like label, variant, alt, align, and background. -- evidence: [DEVELOPING.md#L14-L15](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L14-L15), [DEVELOPING.md#L92-L98](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L92-L98), [DEVELOPING.md#L77-L83](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L77-L83) (`clm_39b5fcfaada4b64bf4ec4387e637a506b658bf8c101eb77f0ce2a024f6c9c6b8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The live presentation is a website at https://recursivecodingagents.com, described as the public deck for the AI Engineer World's Fair 2026 talk. -- evidence: [README.md#L3-L3](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L3-L3), [README.md#L5-L5](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L5-L5) (`clm_f63be282c293b048dd3cf6658694a13c3baffccb798897157a3630994c5563ab`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The web project appears to depend on SvelteKit with mdsvex slides and the @sveltejs/adapter-cloudflare adapter, built with the bun toolchain. -- evidence: [DEVELOPING.md#L50-L52](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L50-L52), [DEVELOPING.md#L75-L75](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L75-L75), [DEVELOPING.md#L8-L12](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L8-L12) (`clm_e0c8641dd010089b5af8923fe8461fa10212ace4fa4856fd322141dc66a96399`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

