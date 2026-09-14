# invariantlabs-ai/explorer

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e7b13b3f5fe5 @ 6c3b908ee9d5f97f

## Summary (orientation draft, not independently verified)

The README documents Invariant Explorer as a tool for visualizing and exploring agent traces, launched via the invariant-ai pip package with Docker Compose as a prerequisite, storing data in ./data. Most other README content covers local development and testing workflows.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Invariant Explorer is described as a tool for visualizing and exploring agent traces. -- evidence: [README.md#L5-L5](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: local development setup uses ./run.sh up to launch the stack, with Docker Compose installed beforehand. -- evidence: [README.md#L31-L33](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L31-L33), [README.md#L29-L29](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L29-L29), [README.md#L27-L27](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L27-L27)
  - [observation/documented] Repository development practice: tests run via ./run.sh tests-local after stopping the app with ./run.sh down, and can target a folder, a file, or a single test. -- evidence: [README.md#L79-L81](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L79-L81), [README.md#L50-L50](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L50-L50), [README.md#L67-L69](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L67-L69), [README.md#L58-L61](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L58-L61), [README.md#L52-L54](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L52-L54), [README.md#L73-L75](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L73-L75)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Users install the invariant-ai pip package and launch Explorer with the 'invariant explorer' command, then access the instance at http://localhost. -- evidence: [README.md#L20-L21](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L20-L21), [README.md#L17-L17](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L17-L17), [README.md#L23-L23](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L23-L23)
- memory-state (1 claim(s)):
  - [observation/documented] Explorer stores data in a ./data directory of the current working directory; deleting that directory resets the data. -- evidence: [README.md#L38-L38](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L38-L38), [README.md#L23-L23](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L23-L23)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Docker Compose is listed as a prerequisite for running Explorer. -- evidence: [README.md#L11-L11](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L11-L11)
- limitations (1 claim(s)):
  - [observation/documented] The hosted version of Invariant Explorer was shut down in January 2026, with readers pointed to Snyk's AI Security offering for Invariant Labs' continued AI security work. -- evidence: [README.md#L3-L3](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](explorer.detail.md) for every claim.)

Metadata and full claim list: [full detail](explorer.detail.md)
Human notes ([notes](explorer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
