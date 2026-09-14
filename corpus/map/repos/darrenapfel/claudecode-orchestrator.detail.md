# darrenapfel/claudecode-orchestrator -- full detail

[Back to orientation](claudecode-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/darrenapfel/claudecode-orchestrator/a83e990b21391024bdb40d04248be268870c444c/2e6a8c3d43b3f016.json](../../../wiki/dossiers/darrenapfel/claudecode-orchestrator/a83e990b21391024bdb40d04248be268870c444c/2e6a8c3d43b3f016.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The design philosophy is 'quality through truth': every claim requires evidence, failures are documented and fixed rather than hidden, which the docs say saves tokens by catching issues early. -- evidence: [readme.md#L9-L9](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L9-L9), [readme.md#L318-L318](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L318-L318) (`clm_e9fabc5d902b30151e33d340598688f80c93972d18076b92ebd97ed8ba52bce3`)

## workflows (4 claim(s))

- [observation/documented] Work follows a nine-step workflow from discovery and requirements through parallel implementation, integration, validation, fix cycles, milestone completion, and feedback processing. -- evidence: [readme.md#L176-L184](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L176-L184) (`clm_d9790da24976d619614be573fcd4fc13967075ce8a67e02a7045772eee9da5a7`)
- [observation/documented] Milestone completion includes starting the service in the background, smoke-testing endpoints, generating testing guides and a feedback form, and processing user feedback into fix sprints. -- evidence: [readme.md#L107-L110](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L107-L110), [readme.md#L100-L104](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L100-L104), [readme.md#L113-L116](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L113-L116) (`clm_1b32a37841f2bfc5edbf9aa70de1599ef6b3374e5906d6b3329e90fa775736bd`)
- [observation/documented] Validation failures trigger documented fix cycles that repeat until all validators pass; the protocol treats multiple cycles as normal, honest progress. -- evidence: [readme.md#L144-L147](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L144-L147), [readme.md#L213-L213](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L213-L213) (`clm_da456f583572300d30b967c49c2e912606c9f45278901952b625c39378f7b84d`)
- [observation/documented] Repository development practice: contributors modify orchestrator-files/, rebuild with node build-orchestrator.js, test via ./orchestrator.sh local, and submit pull requests. -- evidence: [readme.md#L278-L278](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L278-L278), [readme.md#L271-L271](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L271-L271), [readme.md#L273-L276](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L273-L276) (`clm_47d1aef7cefd4e9706603fcd21591024b8bfc10141fffb6e256a3bcd612a2bde`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Installation is via an orchestrator.sh script with 'global' and 'local' modes, and global installs require explicit 'y' confirmation before overwriting, canceling on any other input. -- evidence: [readme.md#L48-L49](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L48-L49), [readme.md#L38-L38](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L38-L38), [readme.md#L42-L43](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L42-L43), [readme.md#L25-L26](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L25-L26) (`clm_9615230e83f7574c8d3104046ad3f8b80361b412f07f5d7679a6121e0aa563c6`)

## memory-state (2 claim(s))

- [observation/documented] State lives in a .work workspace organized into foundation, milestones (with per-sprint tasks, integration, numbered validation and fix-cycle directories, and completion docs), and discovery folders. -- evidence: [readme.md#L68-L87](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L68-L87), [readme.md#L188-L202](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L188-L202) (`clm_af362b0902bcc9553983d402246be3dac275c3f7462a11418169bb5534d19ea2`)
- [observation/documented] Each task produces an EVIDENCE.md with reproducible proof, complete test outputs, timestamped screenshots, and actual command execution, and validated tasks are committed with per-task file isolation. -- evidence: [readme.md#L92-L95](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L92-L95), [readme.md#L138-L141](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L138-L141), [readme.md#L90-L90](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L90-L90) (`clm_4baebc9aa6ff8d96f282a67b8f93742ba3f7fdddc2f382bf94614d82fd3290d1`)

## orchestration (2 claim(s))

- [observation/documented] The framework orchestrates multiple specialized personas (orchestrator, PM, architect, engineer, UX designer, QA and support roles) working in parallel as a simulated software team. -- evidence: [readme.md#L5-L5](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L5-L5), [readme.md#L164-L168](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L164-L168), [readme.md#L54-L54](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L54-L54), [readme.md#L171-L172](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L171-L172), [readme.md#L157-L161](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L157-L161) (`clm_213f4067ea4bfbba48a888ba5b31965cbe966dfc76f319b834f9c68a6af46a83`)
- [observation/documented] Parallel execution is enforced: independent tasks must be created simultaneously in one message, with visual guides and system-level warnings against sequential execution. -- evidence: [readme.md#L240-L242](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L240-L242), [readme.md#L20-L22](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L20-L22), [readme.md#L56-L63](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L56-L63) (`clm_93d049f13402b55a31e500483d03f3f2a702be0cdffaa173d53f68406b5bea55`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The product's validation harness runs four parallel validators (PM end-to-end, test engineer suites and service startup, performance, security) to check milestone quality. -- evidence: [readme.md#L206-L206](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L206-L206), [readme.md#L208-L211](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L208-L211) (`clm_7fd05814e743d758c61beeb11cccfbe6516a9855740f343db433509c9efc41a9`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [inference/documented] The project is explicitly marked deprecated in favor of a new project (www.limeriq.ai), so the framework appears unmaintained at this commit. -- evidence: [readme.md#L1-L1](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L1-L1) (`clm_630f464f0b624d1108fcf6f0faa481b8c64800fc24a7b7c120e4d088dcb45216`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

