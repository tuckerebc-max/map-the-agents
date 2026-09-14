# packtpublishing/30-agents-every-ai-engineer-must-build

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bb19628dd41f @ 4c1521f067d685d0

## Summary (orientation draft, not independently verified)

Selected evidence records: The repository accompanies a Packt book presenting 30 agent architectures, with chapter tables covering foundational, retrieval, tool-orchestration, data-analysis, and domain-specific agent systems. Each chapter ships five pre-executed notebook variants differing by LLM provider, all with identical cell structure and saved outputs so they can be browsed on GitHub without running code.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The repository accompanies a Packt book presenting 30 agent architectures, with chapter tables covering foundational, retrieval, tool-orchestration, data-analysis, and domain-specific agent systems. -- evidence: [README.md#L98-L103](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L98-L103), [README.md#L131-L137](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L131-L137), [README.md#L109-L114](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L109-L114), [README.md#L20-L20](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L20-L20), [README.md#L120-L125](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L120-L125)
  - [observation/documented] Each chapter follows a six-part structure: conceptual foundation, implementation guide, case studies, design patterns and variations, integration considerations, and common pitfalls. -- evidence: [README.md#L141-L141](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L141-L141), [README.md#L143-L148](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L143-L148)
- components (1 claim(s)):
  - [observation/documented] Each chapter ships five pre-executed notebook variants differing by LLM provider, all with identical cell structure and saved outputs so they can be browsed on GitHub without running code. -- evidence: [README.md#L73-L73](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L73-L73), [README.md#L83-L83](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L83-L83), [README.md#L75-L81](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L75-L81)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Documented usage: clone the repo, enter a chapter directory, install base and provider requirements, optionally copy .env.template to .env for an API key, then open the chapter notebook with jupyter notebook. -- evidence: [README.md#L40-L40](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L40-L40), [README.md#L36-L37](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L36-L37), [README.md#L52-L52](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L52-L52), [README.md#L43-L43](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L43-L43), [README.md#L56-L57](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L56-L57)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A no-key simulation mode runs every chapter on a built-in MockLLM with chapter-derived mock responses, requiring no API key; the README states it runs entirely on MockLLM with no dependencies. -- evidence: [README.md#L61-L69](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L61-L69), [README.md#L85-L88](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L85-L88), [README.md#L75-L81](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/README.md#L75-L81)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] A book-wide comparison scored four providers 0-10 per chapter across eight dimensions (including factual accuracy, source grounding, and Bloom's level), based on 68 notebook executions with live API keys in April 2026. -- evidence: [LLM_COMPARISON_SUMMARY.md#L274-L274](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/LLM_COMPARISON_SUMMARY.md#L274-L274), [LLM_COMPARISON_SUMMARY.md#L300-L303](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/LLM_COMPARISON_SUMMARY.md#L300-L303), [LLM_COMPARISON_SUMMARY.md#L276-L285](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/LLM_COMPARISON_SUMMARY.md#L276-L285)
  - [observation/documented] The comparison concludes no single provider wins overall: GPT-4o and local DeepSeek each won 3 chapters, Claude Sonnet 4 and Gemini Flash 2.5 one each, with 8 chapters tied as deterministic and 1 with no winner. -- evidence: [LLM_COMPARISON_SUMMARY.md#L15-L30](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/blob/bb19628dd41f440b8d32c48d97ed41a6b4e01209/LLM_COMPARISON_SUMMARY.md#L15-L30)
- dependencies (1 claim(s)):
More evidence: [full detail](30-agents-every-ai-engineer-must-build.detail.md)

Metadata and full claim list: [full detail](30-agents-every-ai-engineer-must-build.detail.md)
Human notes ([notes](30-agents-every-ai-engineer-must-build.notes.md), never overwritten by build)

[Back to map index](../../index.md)
