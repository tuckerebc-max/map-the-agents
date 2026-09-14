# obra/smallest-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d42ba035040c @ be9c585e53a4e1f2

## Summary (orientation draft, not independently verified)

The minified agent source src/smallest-agent.js is stated to be 493 bytes, with a separately commented, more readable variant of the same code. The README warns the agent has unrestricted bash access and can do anything, including destructive actions.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 5 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

5 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The minified agent source src/smallest-agent.js is stated to be 493 bytes, with a separately commented, more readable variant of the same code. -- evidence: [README.md#L11-L11](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L11-L11), [README.md#L13-L13](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L13-L13)
- design-choices (1 claim(s)):
  - [observation/documented] The project originated as an experiment in how small a functional coding agent could be; an earlier draft was then set to golf itself down over about 20 minutes. -- evidence: [README.md#L1-L1](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L1-L1), [README.md#L7-L7](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L7-L7), [README.md#L5-L5](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L5-L5), [README.md#L9-L9](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L9-L9)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the final minification step is done with terser -c -m --module on the commented source, per the README. -- evidence: [README.md#L15-L15](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L15-L15)
  - [observation/documented] Repository development practice: npm test runs a repeatable smoke test against the live API covering 'hi', uuidgen, and a failing shell command. -- evidence: [README.md#L17-L17](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L17-L17)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The README warns the agent has unrestricted bash access and can do anything, including destructive actions. -- evidence: [README.md#L19-L21](https://github.com/obra/smallest-agent/blob/d42ba035040c64aa59ba235d8cf8da8cf0129944/README.md#L19-L21)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](smallest-agent.detail.md).

Metadata and full claim list: [full detail](smallest-agent.detail.md)
Human notes ([notes](smallest-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
