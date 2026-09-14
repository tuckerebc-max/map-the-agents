# peterfei/ifai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 752aa91e9237 @ 38e3e9c4e59fc7e8

## Summary (orientation draft, not independently verified)

IfAI is documented as an AI-native code editor and agent orchestration platform built on Tauri 2.0 and React 19, featuring 9+ specialized agents coordinated via YAML-declared DAG workflows, plus an SSE-based HTTP chat API. Evidence is primarily README/API documentation; no source code slices were provided. Evidence coverage: 171 of 243 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 95 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] IfAI is described as an AI-native code editor and agent orchestration assistant built on Tauri 2.0 and React 19, with 9+ collaborating agents driven by DAG workflows. -- evidence: [README_EN.md#L3-L6](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L3-L6), [README.md#L3-L6](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L3-L6)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run the app in dev mode with npm run tauri dev after npm install, and build releases with npm run build:community followed by npm run tauri:community; the HTTP API is enabled in dev via ENABLE_HTTP_API=true. -- evidence: [README_EN.md#L101-L104](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L101-L104), [docs/AI-CHAT-API.md#L57-L58](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L57-L58), [README_EN.md#L93-L98](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L93-L98), [README.md#L103-L106](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L103-L106), [README.md#L95-L100](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L95-L100)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] An HTTP API exposes POST /api/ai/chat/stream returning SSE (text/event-stream) streaming chat responses, with request fields messages, provider_config (name, api_key, base_url), model, and optional enable_tools. -- evidence: [docs/AI-CHAT-API.md#L67-L78](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L67-L78), [docs/AI-CHAT-API.md#L23-L23](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L23-L23), [docs/AI-CHAT-API.md#L86-L86](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L86-L86), [docs/AI-CHAT-API.md#L115-L120](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L115-L120), [docs/AI-CHAT-API.md#L92-L92](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L92-L92), [docs/AI-CHAT-API.md#L102-L108](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L102-L108)
  - [observation/documented] SSE events include content_delta, done (with finish_reason), and error types carrying error codes such as AI_SERVICE_ERROR, NETWORK_ERROR, TIMEOUT, and API_ERROR; HTTP 503 and 500 are documented error statuses. -- evidence: [docs/AI-CHAT-API.md#L174-L185](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L174-L185), [docs/AI-CHAT-API.md#L326-L329](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L326-L329), [docs/AI-CHAT-API.md#L150-L158](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L150-L158), [docs/AI-CHAT-API.md#L162-L170](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L162-L170), [docs/AI-CHAT-API.md#L345-L350](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L345-L350)
- memory-state (2 claim(s)):
  - [observation/documented] A persistent two-layer memory system stores hot memory (injected into the system prompt) and cold memory (session archives) as zero-dependency Markdown, with a MemorySave tool and LLM-driven extraction. -- evidence: [README.md#L209-L211](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L209-L211)
  - [observation/documented] Chat threads persist messages to IndexedDB and are restored after restart; a dual-queue MessageQueue serializes within a thread while allowing concurrency across threads. -- evidence: [README.md#L176-L179](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L176-L179), [README.md#L163-L169](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L163-L169)
- orchestration (3 claim(s)):
  - [observation/documented] The product ships specialized agents (Explore, Review, Refactor, Test, Doc, Plan, ReAct, Git Commit, Debug) coordinated via a YAML-declarative DAG workflow engine with topological-sort scheduling supporting sequential and parallel execution. -- evidence: [README.md#L36-L44](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L36-L44), [README_EN.md#L34-L42](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L34-L42)
  - [observation/documented] Agents can invoke other agents up to a maximum depth of 5 levels, and a collaboration framework provides parallel invocation, knowledge sharing, and result aggregation primitives. -- evidence: [README.md#L181-L184](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L181-L184), [README.md#L36-L44](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L36-L44), [README_EN.md#L34-L42](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L34-L42)
- tools-permissions (1 claim(s)):
More evidence: [full detail](ifai.detail.md)

Metadata and full claim list: [full detail](ifai.detail.md)
Human notes ([notes](ifai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
