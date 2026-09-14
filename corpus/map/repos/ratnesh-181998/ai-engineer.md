# ratnesh-181998/ai-engineer

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 098968d1893d @ 184ee677e17f4cc4

## Summary (orientation draft, not independently verified)

The snapshot consists almost entirely of a README that curates educational material on AI engineering topics (RAG, agents, LLMs, fine-tuning, MCP/A2A), with links to PDFs, videos, and papers; no shipped runtime product is evidenced. Evidence coverage: 170 of 284 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications (6 claim(s)):
  - [observation/documented] The README presents an 'AI Periodic Table' taxonomy organizing AI concepts into rows: primitives (prompts, embeddings, LLMs), compositions (function calling, vector DBs, RAG, guardrails), deployment, and emerging elements. -- evidence: [README.md#L169-L172](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L169-L172), [README.md#L163-L167](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L163-L167), [README.md#L153-L155](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L153-L155), [README.md#L150-L150](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L150-L150), [README.md#L157-L161](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L157-L161)
  - [observation/documented] It describes composite 'reactions' such as a RAG chatbot combining prompts, embeddings, vector DB, retrieval, LLM, and guardrails, and an agentic system as agent plus function calling plus frameworks looping until a goal is achieved. -- evidence: [README.md#L175-L176](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L175-L176)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Per the README, A2A-supporting remote agents must publish a JSON Agent Card describing capabilities and authentication, which clients use to discover and select agents. -- evidence: [README.md#L391-L391](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L391-L391), [README.md#L393-L393](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L393-L393)
  - [observation/documented] The README states MCP gives agents access to tools while A2A lets agents connect and collaborate with other agents, and that A2A agents can be modeled as MCP resources via their AgentCard. -- evidence: [README.md#L387-L387](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L387-L387), [README.md#L385-L385](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L385-L385), [README.md#L372-L373](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L372-L373)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [inference/documented] The snapshot appears to contain no executable code or product runtime; the evidence consists of README documentation, images, and linked PDFs, so it functions as a reference collection rather than a runnable agent. -- evidence: [README.md#L2-L2](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L2-L2), [README.md#L21-L21](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L21-L21), [README.md#L89-L89](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L89-L89), [README.md#L560-L560](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L560-L560)
- relevance (3 claim(s)):
  - [observation/documented] The repository is a curated learning resource for AI engineering, covering agentic AI, generative AI, LLMs, and RAG topics as stated in its README heading. -- evidence: [README.md#L21-L21](https://github.com/Ratnesh-181998/AI-Engineer/blob/098968d1893decd220ef68d3311a847d2a3b1e7d/README.md#L21-L21)
More evidence: [full detail](ai-engineer.detail.md)

Metadata and full claim list: [full detail](ai-engineer.detail.md)
Human notes ([notes](ai-engineer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
