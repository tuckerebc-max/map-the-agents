# atrayee-dev/secure-ai-agent-boundary

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4c23100eddad @ b16dae5a835c4628

## Summary (orientation draft, not independently verified)

The snapshot contains only README.md content describing CodeBoundary, a zero-trust data-boundary layer for AI-assisted coding, including its contract system, compartmentalized sessions, hybrid model routing, and disclaimers. No code, tests, or contributor instructions are present in the evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The core mechanism is a data-boundary contract: a YAML/JSON configuration stored with the source that defines scope, redaction rules, visibility level, and output filters for model sessions. -- evidence: [README.md#L44-L44](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L44-L44), [README.md#L46-L49](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L46-L49)
- design-choices (3 claim(s)):
  - [observation/documented] CodeBoundary is described as a zero-trust compartment model in which each third-party model runs in an ephemeral container with strictly bounded data exposure, rather than sharing context across a common environment. -- evidence: [README.md#L10-L10](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L10-L10)
  - [observation/documented] The boundary engine is language-aware, claiming syntax-tree understanding for 12+ languages including Python, TypeScript, Rust, Go, Java, C#, C++, Ruby, PHP, Swift, Kotlin, and Shell. -- evidence: [README.md#L55-L55](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L55-L55)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The primary entry point is a .codeboundary.yml file at the repository root, defining a default contract, an allowed-models list with names and fingerprints, and an audit log destination such as a local .cb-audit/ directory. -- evidence: [README.md#L94-L94](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L94-L94), [README.md#L96-L98](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L96-L98)
  - [observation/documented] The tool is described as editor-agnostic, integrating with any tool that can run a CLI command before and after an edit or any IDE extension supporting LSP-like hook callbacks. -- evidence: [README.md#L102-L102](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L102-L102)
- memory-state (1 claim(s)):
  - [observation/documented] Each model invocation runs in an isolated context bubble that starts clean, and model output goes to a staging area rather than the working tree until an engineer explicitly approves it. -- evidence: [README.md#L34-L34](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L34-L34), [README.md#L36-L38](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L36-L38), [README.md#L67-L76](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L67-L76)
- orchestration (1 claim(s)):
  - [observation/documented] Hybrid sessions route low-sensitivity tasks to a fast local model and high-complexity tasks to a frontier API under one contract, with context stripped and rehydrated between models. -- evidence: [README.md#L61-L61](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L61-L61), [README.md#L59-L59](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L59-L59)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The framework is positioned as a decoupled configuration layer requiring no daemon, kernel patching, or heavyweight control plane, overlaying an existing Git workflow. -- evidence: [README.md#L92-L92](https://github.com/Atrayee-dev/secure-ai-agent-boundary/blob/4c23100eddad59df384b6c0cf8d35bbbb7a6d52e/README.md#L92-L92)
- limitations (1 claim(s)):
More evidence: [full detail](secure-ai-agent-boundary.detail.md)

Metadata and full claim list: [full detail](secure-ai-agent-boundary.detail.md)
Human notes ([notes](secure-ai-agent-boundary.notes.md), never overwritten by build)

[Back to map index](../../index.md)
