# kristoferlund/duet-gpt

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6e28904075b5 @ 539778bb614080db

## Summary (orientation draft, not independently verified)

DuetGPT is an experimental AI-powered CLI agent that helps developers with coding and file-system tasks by proposing commands for approval and then executing them, using OpenAI function calling instead of langchain. Evidence covers its interface, supported models, memory behavior, and known limitations; contributor-instruction claims are omitted per correction scope.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] DuetGPT is an experimental AI-powered CLI tool and semi-autonomous agent that helps developers with coding and file system tasks. -- evidence: [README.md#L5-L5](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [inference/documented] The approval step before command execution appears to be the product's core safety mechanism, since the README describes automatic execution only after developer approval. -- evidence: [README.md#L5-L5](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L5-L5)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Example tasks include refactoring code, writing bash scripts, searching files for text, and drafting PR descriptions from commit messages; it is also described as a general bash helper. -- evidence: [README.md#L16-L19](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L16-L19), [README.md#L7-L7](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L7-L7)
- interfaces (3 claim(s)):
  - [observation/documented] The developer describes a task; the AI issues commands or follow-up questions, and after developer approval DuetGPT automatically executes the commands. -- evidence: [README.md#L5-L5](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L5-L5)
  - [observation/documented] Installed globally via npm as duet-gpt and started with the duet-gpt command; on first run it prompts for an OpenAI API key. -- evidence: [README.md#L45-L45](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L45-L45), [README.md#L31-L31](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L31-L31), [README.md#L39-L39](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L39-L39), [README.md#L41-L43](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L41-L43), [README.md#L33-L35](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L33-L35)
- memory-state (1 claim(s)):
  - [observation/documented] A changelog entry indicates AI assistant responses are added to memory, and the sample interaction shows 'LLM and memory started' at launch. -- evidence: [README.md#L94-L158](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L94-L158), [CHANGELOG.md#L18-L26](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/CHANGELOG.md#L18-L26)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project no longer uses langchain, relying instead on OpenAI function calling, which the author says improved reliability and performance. -- evidence: [CHANGELOG.md#L32-L34](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/CHANGELOG.md#L32-L34), [README.md#L3-L3](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L3-L3)
  - [observation/documented] Works with OpenAI models gpt-3.5-turbo-0613 (noted as not producing great code) and gpt-4-0613. -- evidence: [README.md#L11-L12](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L11-L12), [README.md#L9-L9](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L9-L9)
- limitations (1 claim(s)):
  - [observation/documented] Known issue: when proposing changes to large files the AI may return incomplete results due to the limited gpt-4 context window; it works best with small files. -- evidence: [README.md#L164-L164](https://github.com/kristoferlund/duet-gpt/blob/6e28904075b593b03ca8a31924ae8acd5f7cea32/README.md#L164-L164)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](duet-gpt.detail.md) for every claim.)

Metadata and full claim list: [full detail](duet-gpt.detail.md)
Human notes ([notes](duet-gpt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
