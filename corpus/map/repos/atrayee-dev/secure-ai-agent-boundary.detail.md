# atrayee-dev/secure-ai-agent-boundary -- full detail

[Back to orientation](secure-ai-agent-boundary.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/atrayee-dev/secure-ai-agent-boundary/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/b16dae5a835c4628.json](../../../wiki/dossiers/atrayee-dev/secure-ai-agent-boundary/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/b16dae5a835c4628.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The core mechanism is a data-boundary contract: a YAML/JSON configuration stored with the source that defines scope, redaction rules, visibility level, and output filters for model sessions. -- evidence: [README.md#L44-L44](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L44-L44), [README.md#L46-L49](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L46-L49) (`clm_3d7a05b84c717a4173ee472f4097b1d885163265179f1c4dad51c5e080c4342b`)

## design-choices (3 claim(s))

- [observation/documented] CodeBoundary is described as a zero-trust compartment model in which each third-party model runs in an ephemeral container with strictly bounded data exposure, rather than sharing context across a common environment. -- evidence: [README.md#L10-L10](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L10-L10) (`clm_34b9b311a6ef775190fb0be996c219f21bf56cc61a471842843eda038f403b0d`)
- [observation/documented] The boundary engine is language-aware, claiming syntax-tree understanding for 12+ languages including Python, TypeScript, Rust, Go, Java, C#, C++, Ruby, PHP, Swift, Kotlin, and Shell. -- evidence: [README.md#L55-L55](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L55-L55) (`clm_dc203cdfaec97747e1029fdc095126ff4ece85270009e76edba74d593ad69251`)
- [observation/documented] The architecture uses a 'diplomat's pouch' metaphor: the engineer declares contract contents, the model receives only declared data, and output stays sealed until the engineer unseals it; extra context requests are logged as boundary violation attempts. -- evidence: [README.md#L86-L86](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L86-L86), [README.md#L82-L82](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L82-L82), [README.md#L84-L84](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L84-L84) (`clm_cdf9165a326ce97d1c3437735199293e95d8b49efe3a9c77eaa75d1a79d9acd4`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The primary entry point is a .codeboundary.yml file at the repository root, defining a default contract, an allowed-models list with names and fingerprints, and an audit log destination such as a local .cb-audit/ directory. -- evidence: [README.md#L94-L94](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L94-L94), [README.md#L96-L98](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L96-L98) (`clm_9cd113858aebf4b2f6ac0392362c0c8383ae29dba1ad398344a60334768cacde`)
- [observation/documented] The tool is described as editor-agnostic, integrating with any tool that can run a CLI command before and after an edit or any IDE extension supporting LSP-like hook callbacks. -- evidence: [README.md#L102-L102](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L102-L102) (`clm_064297d1f673aee996b989a02163d9e296554c50057dc4d65890217de91c79d3`)

## memory-state (1 claim(s))

- [observation/documented] Each model invocation runs in an isolated context bubble that starts clean, and model output goes to a staging area rather than the working tree until an engineer explicitly approves it. -- evidence: [README.md#L34-L34](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L34-L34), [README.md#L36-L38](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L36-L38), [README.md#L67-L76](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L67-L76) (`clm_d41f32b73134ab69bde4227b6b64838d1a633ac7b5b7be78c9ced7693ae07189`)

## orchestration (1 claim(s))

- [observation/documented] Hybrid sessions route low-sensitivity tasks to a fast local model and high-complexity tasks to a frontier API under one contract, with context stripped and rehydrated between models. -- evidence: [README.md#L61-L61](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L61-L61), [README.md#L59-L59](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L59-L59) (`clm_ac1b5cda3007c5e6fee52cd8c10e1b8db36c243f8bbdd1acc3a774b012105c76`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The framework is positioned as a decoupled configuration layer requiring no daemon, kernel patching, or heavyweight control plane, overlaying an existing Git workflow. -- evidence: [README.md#L92-L92](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L92-L92) (`clm_277a71ec135d91e705431fac4a18cd068217db1fd5990249f7852b76325ac122`)

## limitations (1 claim(s))

- [observation/documented] The README explicitly disclaims that the software is a security enhancement, not a guarantee: it cannot prevent all leakage such as side-channel attacks or undocumented model behaviors, and authors disclaim liability for data exfiltration. -- evidence: [README.md#L120-L120](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L120-L120), [README.md#L122-L122](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L122-L122) (`clm_7ddbe2efa17f631cbc88fe30dcda9258170a684ac38587de544c4886cef2840d`)

## relevance (1 claim(s))

- [observation/documented] The project targets organizations integrating frontier AI or local LLMs into engineering workflows that must avoid leaking proprietary code or secrets to model endpoints. -- evidence: [README.md#L10-L10](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L10-L10), [README.md#L12-L12](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L12-L12) (`clm_001604271bdae2a9af449ffe9b1217b0ec65c65f9ebbbc3dc9c934533268fff1`)

