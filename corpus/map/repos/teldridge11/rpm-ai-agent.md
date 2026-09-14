# teldridge11/rpm-ai-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b58d9dee3649 @ 012875b7bce6006d

## Summary (orientation draft, not independently verified)

A Python agent that solves Raven's Progressive Matrices using a three-layer reasoning approach, with documented accuracy results and simple CLI usage via Test.py.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 7 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

7 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository includes a set of RPM problems the agent can be tested against, plus an image illustrating the layered architecture. -- evidence: [README.md#L11-L11](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L11-L11), [README.md#L30-L30](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L30-L30)
- design-choices (2 claim(s)):
  - [observation/documented] The agent mimics human reasoning with a three-layer approach: layer one finds obvious patterns, layer two filters candidate answers violating patterns, and layer three scores remaining answers by attribute similarity. -- evidence: [README.md#L9-L9](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L9-L9)
  - [observation/documented] Each of the three layers contributes capabilities the others cannot, and combined they reportedly solve problems with high accuracy. -- evidence: [README.md#L9-L9](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L9-L9)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The agent is run from the Agent directory with `python Test.py`, and results are written to ProblemResults.csv. -- evidence: [README.md#L30-L30](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L30-L30)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Reported accuracy: 11/12 (91.7%) on basic 2x2 problems, 2/8 (25%) on challenge problems, and 17/20 (85%) on previously unseen problems. -- evidence: [README.md#L14-L14](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L14-L14), [README.md#L16-L20](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L16-L20)
- dependencies (1 claim(s)):
  - [observation/documented] Running the agent requires Python and the Pillow image processing library installed locally. -- evidence: [README.md#L24-L24](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L24-L24)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The project targets Raven's Progressive Matrices, a visual-reasoning intelligence test with 2x2 or 3x3 matrices and six or eight answer choices per problem. -- evidence: [README.md#L4-L4](https://github.com/teldridge11/RPM-AI-Agent/blob/b58d9dee36491d3aa7f338955ca2db1c121c1f6a/README.md#L4-L4)

Every claim for this repository is shown above and in [full detail](rpm-ai-agent.detail.md).

Metadata and full claim list: [full detail](rpm-ai-agent.detail.md)
Human notes ([notes](rpm-ai-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
