# andrewyng/context-hub

Status: distilled - Freshness: stale
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 67dcbeb2eb42 @ 65cc044e4f4063f8

## Summary (orientation draft, not independently verified)

Context Hub is an MIT-licensed npm CLI (@aisuite/chub) that gives coding agents curated, versioned markdown API docs with search/fetch, local annotations, and up/down feedback; evidence is mostly README plus contributor docs, with no code slices.

## Source coverage

Source coverage (partial): 3 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product is an npm-distributed CLI requiring Node.js >= 18, installed globally as @aisuite/chub. -- evidence: [README.md#L5-L7](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L5-L7), [README.md#L11-L15](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L11-L15)
- design-choices (2 claim(s)):
  - [observation/documented] Annotations are local notes persisted across sessions and re-injected on future fetches only with --with-annotations, which is off by default, with contents treated as untrusted input. -- evidence: [README.md#L91-L91](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L91-L91), [README.md#L68-L68](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L68-L68)
  - [observation/documented] Feedback is up/down ratings sent to doc authors so content improves for everyone, separate from local annotations. -- evidence: [README.md#L38-L38](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L38-L38), [README.md#L70-L70](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L70-L70)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors fork from main, add/update tests, run 'cd cli && npm test', validate with 'chub build content/ --validate-only', then submit a pull request. -- evidence: [CONTRIBUTING.md#L40-L45](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L40-L45)
  - [observation/documented] Repository development practice: tests run via npm test, test:watch, and test:coverage inside the cli directory, using Vitest unit tests plus e2e/integration tests. -- evidence: [CONTRIBUTING.md#L29-L34](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L29-L34), [CONTRIBUTING.md#L56-L73](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L56-L73)
- skills-patterns (1 claim(s)):
  - [observation/documented] Agents can use Chub via a SKILL.md agent skill; for Claude Code the README suggests placing it in ~/.claude/skills/get-api-docs. -- evidence: [README.md#L19-L19](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L19-L19)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands including chub search [query], chub get <id> [--lang py|js], chub annotate (note, --clear, --list), and chub feedback <id> <up|down>. -- evidence: [README.md#L53-L60](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L53-L60)
  - [observation/documented] Fetches support language variants via --lang (e.g. py or js) for the same doc ID such as openai/chat. -- evidence: [README.md#L44-L47](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L44-L47)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project is MIT licensed and content is plain markdown with YAML frontmatter maintained in the repo. -- evidence: [README.md#L101-L101](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L101-L101), [README.md#L95-L95](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L95-L95)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](context-hub.detail.md) for every claim.)

Metadata and full claim list: [full detail](context-hub.detail.md)
Human notes ([notes](context-hub.notes.md), never overwritten by build)

[Back to map index](../../index.md)
