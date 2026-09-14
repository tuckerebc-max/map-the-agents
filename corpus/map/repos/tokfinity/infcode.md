# tokfinity/infcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1dfd4c14a835 @ cb2e48a1909ab624

## Summary (orientation draft, not independently verified)

InfCode is described as an adversarial multi-agent code agent system that uses LLMs to automatically analyze and fix repository issues, developed by Tokfinity's Code Research team and Beihang University. The system uses a dual-agent adversarial refinement framework that iteratively improves both test patches and code patches, aiming to produce fixes verified under strengthened test suites.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] InfCode is described as an adversarial multi-agent code agent system that uses LLMs to automatically analyze and fix repository issues, developed by Tokfinity's Code Research team and Beihang University. -- evidence: [README.md#L6-L6](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L6-L6)
- components (3 claim(s)):
  - [observation/documented] The Patch Generator registers multiple generator groups, each in a separate container generating and repairing candidate patches in parallel, running up to 5 attempts and gathering all produced patches. -- evidence: [README.md#L22-L22](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L22-L22)
  - [observation/documented] Inside the Generator, a Test Patch Generator strengthens tests to expose faults while a Code Patch Generator refines patches to satisfy the enhanced tests, in an adversarial loop. -- evidence: [README.md#L24-L24](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L24-L24)
- design-choices (1 claim(s)):
  - [observation/documented] The system uses a dual-agent adversarial refinement framework that iteratively improves both test patches and code patches, aiming to produce fixes verified under strengthened test suites. -- evidence: [README.md#L8-L8](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L8-L8)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup instructions direct users to create a .env file with API keys (e.g. OPENROUTER_API_KEY), install pip dependencies from requirements.txt, and ensure Docker is installed and running. -- evidence: [README.md#L72-L72](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L72-L72), [README.md#L80-L83](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L80-L83), [README.md#L132-L135](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L132-L135), [README.md#L76-L77](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L76-L77)
  - [observation/documented] Repository development practice: configuration lives in config/config.yaml with sections for providers, runner (concurrency, iterations), builder (Docker image build), and log settings. -- evidence: [README.md#L123-L127](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L123-L127)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Result Submitter tool runs git diff inside the container to obtain and return the generated patch content after the LLM finishes patch generation and testing. -- evidence: [README.md#L62-L64](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L62-L64)
  - [observation/documented] A batch CLI (_batch_run.py) accepts flags for config file, run name, issue list, concurrency (default 20), output directory cleaning, and output directory. -- evidence: [README.md#L90-L92](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L90-L92), [README.md#L96-L102](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L96-L102)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] InfCode adopts a generate-select architecture: Patch Generation produces candidate patches and Patch Selection picks the optimal one. -- evidence: [README.md#L20-L20](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L20-L20)
- tools-permissions (1 claim(s)):
More evidence: [full detail](infcode.detail.md)

Metadata and full claim list: [full detail](infcode.detail.md)
Human notes ([notes](infcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
