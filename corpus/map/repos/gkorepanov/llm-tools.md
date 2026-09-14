# gkorepanov/llm-tools

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 49867219956a @ 2eddf75b8b535de6

## Summary (orientation draft, not independently verified)

The snapshot is a small shared Python package for Voicebot's streamed LLM calls, documented mainly in a README describing LiteLLM-based streaming, retries, fallbacks, token accounting, and translation helpers.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 3 facet(s); 10 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The package is described as a small shared library for Voicebot's streamed LLM calls. -- evidence: [README.md#L3-L3](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L3-L3)
  - [observation/documented] It provides LiteLLM-based async chat streaming with bounded initial-request and mid-stream retries. -- evidence: [README.md#L7-L13](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L7-L13)
- design-choices (1 claim(s)):
  - [observation/documented] Production model chains live in the bot's private configuration and are constructed by bot/parsing/generator.py, currently using Google Gemini as primary with OpenAI GPT-5.4 mini as fallback. -- evidence: [README.md#L15-L17](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L15-L17)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Model chains are built on LiteLLM, and the README states the package no longer uses LangChain. -- evidence: [README.md#L7-L13](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L7-L13), [README.md#L19-L19](https://github.com/gkorepanov/llm-tools/blob/49867219956ad3cba942d3b4c78be79ffd1dffbf/README.md#L19-L19)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](llm-tools.detail.md) for every claim.)

Metadata and full claim list: [full detail](llm-tools.detail.md)
Human notes ([notes](llm-tools.notes.md), never overwritten by build)

[Back to map index](../../index.md)
