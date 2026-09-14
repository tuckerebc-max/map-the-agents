# peterfei/ifai -- full detail

[Back to orientation](ifai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/peterfei/ifai/752aa91e923741f0818685620bd97bd72d4e48bf/38e3e9c4e59fc7e8.json](../../../wiki/dossiers/peterfei/ifai/752aa91e923741f0818685620bd97bd72d4e48bf/38e3e9c4e59fc7e8.json)

## specifications (1 claim(s))

- [observation/documented] IfAI is described as an AI-native code editor and agent orchestration assistant built on Tauri 2.0 and React 19, with 9+ collaborating agents driven by DAG workflows. -- evidence: [README_EN.md#L3-L6](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L3-L6), [README.md#L3-L6](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L3-L6) (`clm_d693faf2ff416dd616d41c4949ba06581566dd1ddf6d70f1487a18682759e198`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run the app in dev mode with npm run tauri dev after npm install, and build releases with npm run build:community followed by npm run tauri:community; the HTTP API is enabled in dev via ENABLE_HTTP_API=true. -- evidence: [README_EN.md#L101-L104](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L101-L104), [docs/AI-CHAT-API.md#L57-L58](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L57-L58), [README_EN.md#L93-L98](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L93-L98), [README.md#L103-L106](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L103-L106), [README.md#L95-L100](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L95-L100) (`clm_7bc32c3ea497a44151884b763603da68add2fab948f35b4dbc94fe3d72b5f92c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] An HTTP API exposes POST /api/ai/chat/stream returning SSE (text/event-stream) streaming chat responses, with request fields messages, provider_config (name, api_key, base_url), model, and optional enable_tools. -- evidence: [docs/AI-CHAT-API.md#L67-L78](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L67-L78), [docs/AI-CHAT-API.md#L23-L23](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L23-L23), [docs/AI-CHAT-API.md#L86-L86](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L86-L86), [docs/AI-CHAT-API.md#L115-L120](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L115-L120), [docs/AI-CHAT-API.md#L92-L92](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L92-L92), [docs/AI-CHAT-API.md#L102-L108](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L102-L108) (`clm_215aab98eec72b526ae5b3d3fec391b2c022b4c8c4bde322e7d57325191385d9`)
- [observation/documented] SSE events include content_delta, done (with finish_reason), and error types carrying error codes such as AI_SERVICE_ERROR, NETWORK_ERROR, TIMEOUT, and API_ERROR; HTTP 503 and 500 are documented error statuses. -- evidence: [docs/AI-CHAT-API.md#L174-L185](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L174-L185), [docs/AI-CHAT-API.md#L326-L329](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L326-L329), [docs/AI-CHAT-API.md#L150-L158](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L150-L158), [docs/AI-CHAT-API.md#L162-L170](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L162-L170), [docs/AI-CHAT-API.md#L345-L350](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L345-L350) (`clm_fa81b1ede2c86d5d68ad9635b7a313416e1653a7819c0c4b1f5863607e1c967a`)

## memory-state (2 claim(s))

- [observation/documented] A persistent two-layer memory system stores hot memory (injected into the system prompt) and cold memory (session archives) as zero-dependency Markdown, with a MemorySave tool and LLM-driven extraction. -- evidence: [README.md#L209-L211](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L209-L211) (`clm_8967e1204f383037286df25211beeb11f2f5cce069dffc472f939ce746f411bf`)
- [observation/documented] Chat threads persist messages to IndexedDB and are restored after restart; a dual-queue MessageQueue serializes within a thread while allowing concurrency across threads. -- evidence: [README.md#L176-L179](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L176-L179), [README.md#L163-L169](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L163-L169) (`clm_cf598c92f2c6e59129f8d9707d0a109ce08ea9d10b248e96573bab5812b7ee31`)

## orchestration (3 claim(s))

- [observation/documented] The product ships specialized agents (Explore, Review, Refactor, Test, Doc, Plan, ReAct, Git Commit, Debug) coordinated via a YAML-declarative DAG workflow engine with topological-sort scheduling supporting sequential and parallel execution. -- evidence: [README.md#L36-L44](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L36-L44), [README_EN.md#L34-L42](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L34-L42) (`clm_6fcc1a17f0d893a7adc297e90edd9a53fd882125e245324e9ee24985374c1984`)
- [observation/documented] Agents can invoke other agents up to a maximum depth of 5 levels, and a collaboration framework provides parallel invocation, knowledge sharing, and result aggregation primitives. -- evidence: [README.md#L181-L184](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L181-L184), [README.md#L36-L44](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L36-L44), [README_EN.md#L34-L42](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L34-L42) (`clm_a66a8e4710f7ca2f98115b6a508fa56d58fbef580047cfbec12bd82755e530d7`)
- [observation/documented] A declarative intent-routing system uses O(1) lookup-table routing to match natural-language task descriptions to the appropriate agent or workflow. -- evidence: [README.md#L36-L44](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L36-L44), [README.md#L197-L198](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L197-L198), [README_EN.md#L34-L42](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L34-L42) (`clm_d7bd0f904c57fea557f3d37d67186429cc8f88562256396ca8f1cbf7d0625d28`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents have shell-level control and can execute commands such as npm, git, and cargo to install dependencies and self-heal environments; the changelog notes a 100% trust model with tool-call limits raised from 100 to 1000. -- evidence: [README_EN.md#L23-L27](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L23-L27), [README.md#L25-L29](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L25-L29), [README.md#L202-L205](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L202-L205), [README_EN.md#L34-L42](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L34-L42) (`clm_59b10a8fbcc65b3713908afe4bd164bd7d639be89e36cc4f17cf14a45cb4118a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The architecture diagram shows a React 19 interaction layer over a Rust/Tauri 2.0 core, with AI services for DeepSeek, Kimi, and Qwen models, a RAG/vector engine, and system services for Shell, PTY, and Git; building requires Node.js >= 18 and Rust >= 1.80. -- evidence: [README_EN.md#L110-L117](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L110-L117), [README.md#L92-L92](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L92-L92), [README_EN.md#L90-L90](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README_EN.md#L90-L90), [README.md#L112-L119](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/README.md#L112-L119) (`clm_6148060d7efe4394c094d1e0b2792d441807e4caeb4c103a275c4729f4b7cda1`)

## limitations (1 claim(s))

- [observation/documented] Per the API documentation, tool calling via the enable_tools flag is marked as not yet implemented (待实现). -- evidence: [docs/AI-CHAT-API.md#L27-L31](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L27-L31), [docs/AI-CHAT-API.md#L373-L373](https://github.com/peterfei/ifai/blob/752aa91e923741f0818685620bd97bd72d4e48bf/docs/AI-CHAT-API.md#L373-L373) (`clm_b83b71f2247b6834b40c77f28f857db21754a836804a8a860702421f6d421df9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

