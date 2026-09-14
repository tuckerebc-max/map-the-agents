# itwanger/paiagent -- full detail

[Back to orientation](paiagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/itwanger/paiagent/05297308189fa5054f1f5ac1af6346a48eea5aad/136f02042d8f4a25.json](../../../wiki/dossiers/itwanger/paiagent/05297308189fa5054f1f5ac1af6346a48eea5aad/136f02042d8f4a25.json)

## specifications (2 claim(s))

- [observation/documented] The Agent Plan integration plan specifies new node types: web_search/web_fetch, memory_write/memory_retrieve, image_generate/video_generate/vision_analyze, and knowledge_upsert/knowledge_retrieve, also registrable as ReAct Agent tools. -- evidence: [docs/agent-plan-harness-integration-plan.md#L22-L29](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L22-L29) (`clm_ece923b61180a4ba6cddd106e87561664de24b4fde9a97fa055feb261cae51cf`)
- [observation/documented] The plan adds a volcengine_agent_plan provider with global config fields for embedding, image, video, and TTS models plus webSearchEnabled and memoryEnabled toggles, normalizing provider aliases like 'ark' and '火山方舟'. -- evidence: [docs/agent-plan-harness-integration-plan.md#L22-L29](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L22-L29), [docs/agent-plan-harness-integration-plan.md#L37-L43](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L37-L43), [docs/agent-plan-harness-integration-plan.md#L47-L47](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L47-L47) (`clm_d2632504b040d72f23f04e041f855f5477bf8eed918ad7e89a6e6547a53325dd`)

## components (1 claim(s))

- [observation/documented] PaiAgent is described as an enterprise AI workflow visual orchestration platform with a drag-and-drop interface for building and running AI workflows without coding. -- evidence: [README.md#L26-L26](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L26-L26), [README.md#L5-L5](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L5-L5), [README.md#L7-L7](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L7-L7) (`clm_679d10083e10d2f5373e6fac0bdb5506a1a8e2fec25e0110fa8eb9ce42665f0d`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors should fork, create a feature branch, commit, push, and open a PR; backend code follows the Alibaba Java manual, frontend follows Airbnb React style, and commits use Conventional Commits. -- evidence: [README.md#L786-L788](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L786-L788), [README.md#L778-L782](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L778-L782) (`clm_142811aee456cf96f2ae7fa8efa4d708335919e58d4cacb1ae5ef1e4dce12ee5`)
- [observation/documented] Repository development practice: setup requires Java 21+, Node.js 18+, MySQL 8.0+, and Maven 3.8+; the backend runs via ./mvnw spring-boot:run on port 8084 and the frontend via npm install/npm run dev on port 5173. -- evidence: [README.md#L462-L462](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L462-L462), [README.md#L380-L385](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L380-L385), [README.md#L486-L489](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L486-L489), [README.md#L481-L484](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L481-L484), [README.md#L452-L455](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L452-L455) (`clm_8cd259420cd05c3c7349dc5750fd443ce6196b3209caa5c83a356d1eceb1bf45`)
- [observation/documented] Repository development practice: the integration plan's test plan calls for backend unit tests (./mvnw test), frontend npm run build verification, and mock-based integration acceptance of a web content production workflow. -- evidence: [docs/agent-plan-harness-integration-plan.md#L174-L180](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L174-L180), [docs/agent-plan-harness-integration-plan.md#L191-L193](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L191-L193), [docs/agent-plan-harness-integration-plan.md#L184-L187](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L184-L187) (`clm_5855780a08a556bc688828aede3928d6f15a08f883136c5a65ae70a930b743c7`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are defined declaratively via SKILL.md with YAML frontmatter (name, description) plus markdown rules, each skill being a directory with an optional reference subdirectory. -- evidence: [README.md#L669-L669](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L669-L669), [README.md#L682-L686](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L682-L686), [README.md#L671-L678](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L671-L678), [README.md#L106-L111](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L106-L111) (`clm_1be3b820a09531870cebec0e8a1f807e5063f3a39bf6e99c77903cbd4ab3707b`)
- [observation/documented] Skills load progressively in three levels (summary, full SKILL.md, reference docs) to save tokens, and are exposed to LLMs as Spring AI FunctionCallbacks (LoadSkillDetailFunction/LoadSkillReferenceFunction). -- evidence: [README.md#L106-L111](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L106-L111), [README.md#L696-L699](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L696-L699) (`clm_01c4e6cc9fe45823c5361871ab44bbda7451d7fc05385905f10d18ef9b8de011`)

## interfaces (3 claim(s))

- [observation/documented] The Skills system exposes REST endpoints: GET /api/skills for summaries, GET /api/skills/{name} for details, and GET /api/skills/{name}/references/{ref} for reference documents. -- evidence: [README.md#L703-L707](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L703-L707) (`clm_c132afbeb971f30e146e33c250bd15d87d4f1d1e0f5f1d3e1ceea70647bf8375`)
- [observation/documented] The frontend is a ReactFlow-based flow editor supporting node dragging, edge wiring, and parameter editing, with a node panel, canvas, and configuration panel. -- evidence: [docs/FINAL_SUMMARY.md#L62-L65](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/FINAL_SUMMARY.md#L62-L65), [docs/FINAL_SUMMARY.md#L75-L77](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/FINAL_SUMMARY.md#L75-L77), [docs/FINAL_SUMMARY.md#L67-L73](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/FINAL_SUMMARY.md#L67-L73), [README.md#L75-L75](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L75-L75) (`clm_a5905276d3a216799da43f19296d6b8f8c36ef356891028f82fe4f629563f68b`)
- [observation/documented] LLM nodes are invoked through a ChatClientFactory that creates clients at runtime from node configuration (apiUrl, apiKey, model, temperature), supporting OpenAI-compatible providers including DeepSeek, Zhipu, and AIPing, plus Qwen via DashScope. -- evidence: [README.md#L759-L764](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L759-L764), [README.md#L81-L85](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L81-L85), [README.md#L638-L641](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L638-L641) (`clm_c863f303e5d4d2d57a04fb9adb17edb365fed95e27d80bc35f68889d1b6d9c49`)

## memory-state (1 claim(s))

- [observation/documented] A plan document proposes memory nodes (memory_write/memory_retrieve) backed by local agent_memory tables and Doubao-embedding-vision embeddings, with workflow/user/global scopes and explicit (not automatic) memory writes. -- evidence: [docs/agent-plan-harness-integration-plan.md#L197-L201](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L197-L201), [docs/agent-plan-harness-integration-plan.md#L86-L87](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L86-L87), [docs/agent-plan-harness-integration-plan.md#L105-L107](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L105-L107), [docs/agent-plan-harness-integration-plan.md#L101-L101](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L101-L101), [docs/agent-plan-harness-integration-plan.md#L82-L82](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L82-L82) (`clm_696ec7009591b47894ea23641fa212728108c394d8591a951cd5577bb9b4d94f`)

## orchestration (3 claim(s))

- [observation/documented] The DAG engine uses Kahn's algorithm for topological ordering and DFS-based cycle detection, executes nodes in topological order, and passes upstream outputs to downstream nodes. -- evidence: [README.md#L623-L629](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L623-L629), [README.md#L93-L96](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L93-L96) (`clm_e8bd493fd8e6471cf257a5e41bcb6a5116aad2fbcf177fa4174aaa8f039b869b`)
- [observation/documented] An EngineSelector routes execution by the workflow's engineType field: 'dag' to the DAG engine, 'langgraph' to LangGraph4j, with null defaulting to DAG for backward compatibility. -- evidence: [README.md#L647-L647](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L647-L647), [README.md#L99-L103](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L99-L103), [README.md#L649-L655](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L649-L655) (`clm_124f58b9298e116bf52f4c56f450a552940ee33044f2c438bb830e5cd3844883`)
- [observation/documented] In the LangGraph4j engine, NodeAdapter adapts existing NodeExecutors into AsyncNodeActions, StateManager manages inputData/nodeOutputs/globalContext, and ExecutionEvent callbacks report node start/success/error. -- evidence: [README.md#L657-L663](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L657-L663), [README.md#L99-L103](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L99-L103) (`clm_cd97a1aa2883a7532e06187383b2d8db710f512d49746ef76167b3731311ffed`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The documented stack includes Java 21+, Spring Boot 3.4.1, Spring AI 1.0.0-M5, Spring AI Alibaba 1.0.0-M6.1, LangGraph4j, React 18, TypeScript 5, MyBatis-Plus 3.5.5, and MySQL 8.0+. -- evidence: [README.md#L9-L16](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L9-L16), [README.md#L165-L280](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L165-L280) (`clm_613a0b83641226c40c2b0cee0df3d6bd452940be70876b164c488f3b759194c7`)
- [observation/documented] MinIO is listed as an optional object storage dependency; the Agent Plan plan proposes transferring generated images and videos to MinIO to avoid reliance on vendor temporary URLs. -- evidence: [docs/agent-plan-harness-integration-plan.md#L197-L201](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L197-L201), [README.md#L165-L280](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L165-L280), [docs/agent-plan-harness-integration-plan.md#L133-L133](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L133-L133) (`clm_b0a523d224d1f0301fe4f80e762249ae4fd312b0ead739e6a0823bc6c4748a1e`)

## limitations (1 claim(s))

- [observation/documented] The README states that changing the password after first login is a feature yet to be implemented, and the default admin/admin123 account is for development only. -- evidence: [README.md#L500-L504](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L500-L504) (`clm_a1518d9a35028ff4a78be4b02705342e6c1850265963f4bccc1c4b6f6587dba5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

