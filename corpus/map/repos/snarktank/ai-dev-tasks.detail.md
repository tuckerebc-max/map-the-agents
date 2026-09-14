# snarktank/ai-dev-tasks -- full detail

[Back to orientation](ai-dev-tasks.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/snarktank/ai-dev-tasks/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/26353fabe4d41e58.json](../../../wiki/dossiers/snarktank/ai-dev-tasks/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/26353fabe4d41e58.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Both prompt files state the PRD and task list are written for a junior developer, requiring explicit, unambiguous, jargon-light requirements. -- evidence: [generate-tasks.md#L70-L70](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L70-L70), [create-prd.md#L69-L69](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L69-L69) (`clm_fec857fa2fe3686db02e816b9b2188d35ef0759dd6560087c3c11bd461b03c72`)

## workflows (3 claim(s))

- [observation/documented] The documented workflow is: create a PRD, generate a task list from it, then have the AI work through tasks one sub-task at a time with user review between steps. -- evidence: [README.md#L61-L61](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L61-L61), [README.md#L69-L69](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L69-L69), [README.md#L11-L13](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L11-L13) (`clm_fbac4dd83753b082bb38e98f59cc8d408edecc9a813f6b1ca7f0e108dde41e14`)
- [observation/documented] Repository development practice: contributions are accepted via opening an issue to discuss changes and submitting pull requests with enhancements. -- evidence: [README.md#L125-L126](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L125-L126) (`clm_048909d45a336701a530f38fa46767f25751406f1b5767a38d96d86691b74991`)
- [observation/documented] Repository development practice: the task-list template tells the implementing agent to run tests with 'npx jest [optional/path/to/test/file]' and to place unit tests alongside the code they test. -- evidence: [generate-tasks.md#L40-L41](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L40-L41) (`clm_17690a95fffef2e79e76785fe8b7a1b3341ee555ab5d7c1aaf19e5a37d083569`)

## skills-patterns (7 claim(s))

- [observation/documented] The repo ships markdown prompt files meant to be referenced inside AI coding assistants (e.g., via @create-prd.md) to steer their behavior, rather than executable code. -- evidence: [README.md#L3-L3](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L3-L3), [README.md#L30-L34](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L30-L34), [README.md#L27-L28](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L27-L28), [README.md#L89-L90](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L89-L90) (`clm_25f4552f1804c7d2644932169ef5508f9097e361158facc21dc4f565b64912e0`)
- [observation/documented] create-prd.md instructs the AI to ask 3-5 essential clarifying questions, formatted as numbered questions with lettered options so the user can reply with selections like '1A, 2C'. -- evidence: [create-prd.md#L9-L12](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L9-L12), [create-prd.md#L27-L29](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L27-L29) (`clm_03315831ce8d85b66a7ce91860f51ca65238f483897eddc1132d3fbbe8f3826c`)
- [observation/documented] create-prd.md specifies a nine-section PRD structure including goals, user stories, numbered functional requirements, non-goals, success metrics, and open questions. -- evidence: [create-prd.md#L57-L65](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L57-L65) (`clm_6144c4e96a13391bb2a1500cba81e8d302051de8a83c5fdae9165384108ca0b3`)
- [observation/documented] create-prd.md directs the AI to save the PRD as prd-[feature-name].md in a /tasks directory and explicitly forbids starting implementation of the PRD. -- evidence: [create-prd.md#L73-L75](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L73-L75), [create-prd.md#L79-L81](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L79-L81) (`clm_463809ad835485bf19437cede305b2f7531299ad51c5f82d417cfae5882435f6`)
- [observation/documented] generate-tasks.md requires task 0.0 'Create feature branch' as the first task unless the user opts out, and pauses for user confirmation ('Go') before generating sub-tasks. -- evidence: [generate-tasks.md#L66-L66](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L66-L66), [generate-tasks.md#L15-L22](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L15-L22) (`clm_a13a359c65cb376c6f4464dccdb58d9930fdd392f9fd750a2ee6449684e1c3a7`)
- [observation/documented] generate-tasks.md instructs the AI to check off each sub-task in the markdown file by changing '- [ ]' to '- [x]' after completion, updating after each sub-task. -- evidence: [generate-tasks.md#L50-L50](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L50-L50), [generate-tasks.md#L45-L45](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L45-L45) (`clm_f0eca526e442a736ecf168125128b199ced8378c3060110191eb3334e24a9607`)
- [observation/documented] The generated task list must include a 'Relevant Files' section listing files to create or modify, with corresponding test files where applicable. -- evidence: [generate-tasks.md#L15-L22](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L15-L22), [generate-tasks.md#L31-L36](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L31-L36) (`clm_0259ac4a8b17321494274b872e31b2065bbb1ff3ebaa421d756cdd4e38bcf0fe`)

## interfaces (1 claim(s))

- [observation/documented] The intended interface is file-tagging in an AI IDE/CLI: users reference the markdown files and generated PRDs with @-mentions such as @create-prd.md and @MyFeature-PRD.md. -- evidence: [README.md#L46-L49](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L46-L49), [README.md#L30-L34](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L30-L34), [README.md#L115-L117](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L115-L117) (`clm_09a8ac38d927995236894b2d8f06df3266306d8e57b89aaef95bd58b3f935f2c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

