# darrenapfel/claudecode-orchestrator

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a83e990b2139 @ 2e6a8c3d43b3f016

## Summary (orientation draft, not independently verified)

Selected evidence records: The framework orchestrates multiple specialized personas (orchestrator, PM, architect, engineer, UX designer, QA and support roles) working in parallel as a simulated software team. Parallel execution is enforced: independent tasks must be created simultaneously in one message, with visual guides and system-level warnings against sequential execution.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The design philosophy is 'quality through truth': every claim requires evidence, failures are documented and fixed rather than hidden, which the docs say saves tokens by catching issues early. -- evidence: [readme.md#L9-L9](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L9-L9), [readme.md#L318-L318](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L318-L318)
- workflows (4 claim(s)):
  - [observation/documented] Work follows a nine-step workflow from discovery and requirements through parallel implementation, integration, validation, fix cycles, milestone completion, and feedback processing. -- evidence: [readme.md#L176-L184](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L176-L184)
  - [observation/documented] Milestone completion includes starting the service in the background, smoke-testing endpoints, generating testing guides and a feedback form, and processing user feedback into fix sprints. -- evidence: [readme.md#L107-L110](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L107-L110), [readme.md#L100-L104](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L100-L104), [readme.md#L113-L116](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L113-L116)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Installation is via an orchestrator.sh script with 'global' and 'local' modes, and global installs require explicit 'y' confirmation before overwriting, canceling on any other input. -- evidence: [readme.md#L48-L49](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L48-L49), [readme.md#L38-L38](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L38-L38), [readme.md#L42-L43](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L42-L43), [readme.md#L25-L26](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L25-L26)
- memory-state (2 claim(s)):
  - [observation/documented] State lives in a .work workspace organized into foundation, milestones (with per-sprint tasks, integration, numbered validation and fix-cycle directories, and completion docs), and discovery folders. -- evidence: [readme.md#L68-L87](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L68-L87), [readme.md#L188-L202](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L188-L202)
  - [observation/documented] Each task produces an EVIDENCE.md with reproducible proof, complete test outputs, timestamped screenshots, and actual command execution, and validated tasks are committed with per-task file isolation. -- evidence: [readme.md#L92-L95](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L92-L95), [readme.md#L138-L141](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L138-L141), [readme.md#L90-L90](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L90-L90)
- orchestration (2 claim(s)):
  - [observation/documented] The framework orchestrates multiple specialized personas (orchestrator, PM, architect, engineer, UX designer, QA and support roles) working in parallel as a simulated software team. -- evidence: [readme.md#L5-L5](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L5-L5), [readme.md#L164-L168](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L164-L168), [readme.md#L54-L54](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L54-L54), [readme.md#L171-L172](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L171-L172), [readme.md#L157-L161](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L157-L161)
  - [observation/documented] Parallel execution is enforced: independent tasks must be created simultaneously in one message, with visual guides and system-level warnings against sequential execution. -- evidence: [readme.md#L240-L242](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L240-L242), [readme.md#L20-L22](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L20-L22), [readme.md#L56-L63](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L56-L63)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The product's validation harness runs four parallel validators (PM end-to-end, test engineer suites and service startup, performance, security) to check milestone quality. -- evidence: [readme.md#L206-L206](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L206-L206), [readme.md#L208-L211](https://github.com/darrenapfel/claudecode-orchestrator/blob/a83e990b21391024bdb40d04248be268870c444c/readme.md#L208-L211)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
More evidence: [full detail](claudecode-orchestrator.detail.md)

Metadata and full claim list: [full detail](claudecode-orchestrator.detail.md)
Human notes ([notes](claudecode-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
