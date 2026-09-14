# autoresearch-factory/agon -- full detail

[Back to orientation](agon.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/autoresearch-factory/agon/594fa079fd35ad51a0ae062668fd859447f5681b/e0afbc882b3308ac.json](../../../wiki/dossiers/autoresearch-factory/agon/594fa079fd35ad51a0ae062668fd859447f5681b/e0afbc882b3308ac.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Every handoff between agents goes through a file on disk, which the README says makes runs recoverable, auditable, and reusable across projects. -- evidence: [README.md#L11-L11](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L11-L11) (`clm_6bbcfccf943725ed5768b60ec4ad878744343ec367a1269890f2dbb4b622652d`)
- [observation/documented] The pipeline is deliberately minimal and explicit: topic → idea → proposal → experiment. -- evidence: [README.md#L11-L11](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L11-L11) (`clm_7382fc1984d7f6b750735be2f4c418330933e09b9c4818da9beefe665f0694aa`)
- [observation/documented] Optional local configuration lives in .settings.toml, with a .settings.example.toml template for customizing model routing and parallelism. -- evidence: [README.md#L74-L74](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L74-L74) (`clm_93476d5e54ca4db3a2c03e97b3de20d05a4038ff63ae25b25fcfced5431f3c41`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Agon exposes four Claude Code slash commands: /idea-tick, /proposal-tick, /experiment-tick, and /deep-lit-tick, which advance the research pipeline stages. -- evidence: [README.md#L45-L48](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L45-L48) (`clm_2037a2ac15cea07ab11a24c027f964f1507be5fe8d93061fe5a64e4f70c85315`)
- [observation/documented] Commands accept free-form arguments, e.g. /experiment-tick can be told a run is a debugging run and asked to pause for user approval after each agent call. -- evidence: [README.md#L52-L59](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L52-L59) (`clm_fec97295778d9ab6dbc636a12ef3af5c2db8c9b5c8eac8f3f483472fea66d914`)

## memory-state (2 claim(s))

- [observation/documented] The documented setup enables CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS so the main agent can resume background subagents and subagents can message each other, and sets cleanupPeriodDays to 3650 to retain session history. -- evidence: [README.md#L109-L113](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L109-L113) (`clm_085b409c65bc72d04a3bf4523fd417806f0d5aa999d1701f0b237c6b054956c2`)
- [inference/documented] The data workspace layout (topics/, ideas/, workspace/ directories) appears to be where the file-based artifacts of each pipeline stage are stored. -- evidence: [README.md#L67-L72](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L67-L72) (`clm_2a81397c17629b2c2a4e4f7c749ad1c30606a56e61ce8c6f2f45d93d805f6d71`)

## orchestration (1 claim(s))

- [observation/documented] The experiment stage coordinates scientist, coder, auditor, and reviewer roles for a single workspace, with agents planning, implementing, auditing, and reviewing each other in closed loops. -- evidence: [README.md#L45-L48](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L45-L48), [README.md#L11-L11](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L11-L11) (`clm_e7d74802cdc6f33baa2c18e5eb85c867efa0489c746d2b16a8f4d05540b128cd`)

## tools-permissions (1 claim(s))

- [observation/documented] Running Agon requires launching Claude Code with --dangerously-skip-permissions, because unattended subagents write files, launch experiments, and call tools for hours and a permission prompt would stall the run; the README suggests isolating it on its own machine, container, or account. -- evidence: [README.md#L36-L39](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L36-L39), [README.md#L41-L41](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L41-L41) (`clm_0c88b05c0f0a9968f55e450b838c8340e6091848d401a932f4200f947de1b174`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Agon is a Claude Code plugin intended to run from a separate data workspace repository (agon-artifacts), cloned side by side with the plugin directory. -- evidence: [README.md#L63-L63](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L63-L63), [README.md#L19-L19](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L19-L19), [README.md#L21-L24](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L21-L24) (`clm_8ce10a40342d33d1f64fd8762117b8a3bfbe9c2a036c9bc2b68882e7a4b2a51c`)
- [observation/documented] The README documents an optional claude-ds wrapper that runs Claude Code against DeepSeek's Anthropic-compatible API endpoint using DEEPSEEK_API_KEY, with deepseek-v4-pro and deepseek-v4-flash model mappings. -- evidence: [README.md#L85-L103](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L85-L103), [README.md#L78-L78](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L78-L78) (`clm_bd1414a1a5ff11465105437d2c8309260d4ef8a8fc1e856aff583595889f9753`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Agon is presented as an autonomous large-scale omnidisciplinary research system built on Prompt Economy, with an accompanying arXiv paper (2606.24177) reporting deployments across more than ten research domains. -- evidence: [README.md#L13-L13](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L13-L13), [README.md#L121-L131](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L121-L131) (`clm_b496447f0261313a510f71ee64399609b27bbdb370ea357e4a3fdd775eff6d3b`)

