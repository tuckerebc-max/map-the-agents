# devill/refakts -- full detail

[Back to orientation](refakts.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/devill/refakts/2ff430870b0428326a771aeb0e320271c61c3c24/2276e7161e5c276e.json](../../../wiki/dossiers/devill/refakts/2ff430870b0428326a771aeb0e320271c61c3c24/2276e7161e5c276e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] move-file updates import references across the codebase, and find-usages locates symbol usages across files. -- evidence: [README.md#L31-L40](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L31-L40) (`clm_229e6ca4f6bf0ead48ea971b912c24650e8dc180037be8af1d379ddbe3a366b4`)

## design-choices (1 claim(s))

- [observation/documented] The design goal is surgical edits: instead of regenerating whole files, operations change only the targeted code and its references, saving tokens and preserving agent cognitive capacity. -- evidence: [README.md#L20-L24](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L20-L24), [README.md#L11-L16](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L11-L16), [README.md#L26-L26](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L26-L26) (`clm_49a7ab7047c752bac63c825d7803ef6bc010854518a7bcfce9b6b84016f99058`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: the repo is optimized for Claude Code; contributors are told to have Claude set up pre/post commit hooks, pick a 'good first issue', assign it to themselves, and can direct work by issue number. -- evidence: [README.md#L135-L140](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L135-L140) (`clm_6b671edf2be68ad3614e9601412c80870975d15e5bf08ce19fe5ea092aa9cb0f`)
- [observation/documented] Repository development practice: tests are fixture-based under tests/fixtures with .input.ts, .expected.ts, and .expected.txt files per command, and npm run test:coverage checks for uncovered use cases. -- evidence: [README.md#L147-L156](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L147-L156) (`clm_8068648ab0810c879b3438f28542e2ecdcefa7424968b2168637ddbc8365af05`)
- [observation/documented] Repository development practice: post-commit hooks scan for quality issues (oversized functions, unused methods, comments, duplication, large changes) and automatically prompt the AI agent with corrective guidance. -- evidence: [README.md#L114-L123](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L114-L123), [README.md#L108-L112](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L108-L112) (`clm_d9e58cfff72b4e4ead069fbc96b63d0d73132f2665c3c68a931efe744cc64bd4`)
- [observation/documented] Repository development practice: a documented 'Habit Hooks' blueprint uses a baseline JSON file of known violations and an emoji agent prompt marker that agent instructions treat as a highest-priority user prompt. -- evidence: [docs/HABIT_HOOKS_MICROFEATURE.md#L189-L194](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/HABIT_HOOKS_MICROFEATURE.md#L189-L194), [docs/HABIT_HOOKS_MICROFEATURE.md#L186-L186](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/HABIT_HOOKS_MICROFEATURE.md#L186-L186), [docs/HABIT_HOOKS_MICROFEATURE.md#L50-L58](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/HABIT_HOOKS_MICROFEATURE.md#L50-L58) (`clm_e47e5d087d7eef365d660c7854a863dbb703bb90bd066aca40d152bbe3552aa2`)
- [observation/documented] Repository development practice: fixture tests follow a setup-execute-validation-cleanup flow, comparing transformed files, stdout, and stderr against expected outputs, with approval commands like npm run test:fixture:approve. -- evidence: [docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L117-L119](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L117-L119), [docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L121-L124](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L121-L124), [docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L181-L185](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L181-L185), [docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L113-L115](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/docs/FIXTURE_TESTING_STRATEGY_FOR_REFACTORING_TOOLS.md#L113-L115) (`clm_441bb8d3aae0ded0e5e692cea0e755e043df96883f1a68d2f22e70ace77dd602`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] RefakTS is a command-line tool exposing commands including extract-variable, inline-variable, rename, select, sort-methods, find-usages, and move-file. -- evidence: [README.md#L31-L40](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L31-L40), [README.md#L20-L24](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L20-L24) (`clm_ca1c355f024b7f3e90d3806a36c822765b5dbf32cb8c117af4b2ab0957c274ed`)
- [observation/documented] The select command supports regex, range, structural, and boundary modes, e.g. --range with start/end regexes and --boundaries "function". -- evidence: [README.md#L66-L70](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L66-L70) (`clm_8ec2b73f4db1b63018039ccf43c79e1df2d8294dcd9f5eb2c73d82d04aecfe19`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool uses ts-morph for AST manipulation and @phenomnomnominal/tsquery for node selection, and is built with TypeScript. -- evidence: [README.md#L76-L76](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L76-L76), [README.md#L74-L74](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L74-L74) (`clm_7598f12684d23327c3b60a57022f96186e6869909dad63ff3c4a7d9604ebc57e`)
- [observation/documented] The package is installed globally via npm as 'refakts'. -- evidence: [README.md#L44-L46](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L44-L46) (`clm_77150e6643c5ad48dfd7f28de9c8253a05afb12c10d43af4fd51fc5b3b6769d5`)

## limitations (2 claim(s))

- [observation/documented] The project is explicitly labeled a proof of concept demonstrating the core concept with basic refactoring operations, with more commands in development. -- evidence: [README.md#L80-L80](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L80-L80) (`clm_ed1f2771b29ebfa83dc3074d4d40dd5e0040e9839bfeabd2d3bea266bbdb2ca0`)
- [observation/documented] Licensing is PolyForm Noncommercial 1.0.0: free for non-commercial use while businesses require a license, with fees distributed among contributors at project leads' discretion. -- evidence: [README.md#L162-L162](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L162-L162), [LICENSE.md#L56-L56](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/LICENSE.md#L56-L56), [README.md#L129-L131](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L129-L131) (`clm_02bc5fbfa7cb44aebd774540a3a09d3cfc0c43b5c3c0c0e83116eddb303ccf35`)

## relevance (1 claim(s))

- [observation/documented] The project targets AI agents making multi-location code changes (renames, extractions) and is positioned as built by AI agents for AI agents, with a roadmap managed by Claude instances. -- evidence: [README.md#L9-L9](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L9-L9), [README.md#L84-L84](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L84-L84) (`clm_e4ddb0d3756605404e91b2eb8237ffdaf35b0076762831a19d275b1d807f8609`)

