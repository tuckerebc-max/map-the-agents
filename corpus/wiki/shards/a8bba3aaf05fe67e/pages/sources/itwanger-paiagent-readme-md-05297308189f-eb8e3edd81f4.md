---
access: public
aliases: []
claim_ids:
- clm_01c4e6cc9fe45823c5361871ab44bbda7451d7fc05385905f10d18ef9b8de011
- clm_124f58b9298e116bf52f4c56f450a552940ee33044f2c438bb830e5cd3844883
- clm_142811aee456cf96f2ae7fa8efa4d708335919e58d4cacb1ae5ef1e4dce12ee5
- clm_1be3b820a09531870cebec0e8a1f807e5063f3a39bf6e99c77903cbd4ab3707b
- clm_613a0b83641226c40c2b0cee0df3d6bd452940be70876b164c488f3b759194c7
- clm_679d10083e10d2f5373e6fac0bdb5506a1a8e2fec25e0110fa8eb9ce42665f0d
- clm_8cd259420cd05c3c7349dc5750fd443ce6196b3209caa5c83a356d1eceb1bf45
- clm_a1518d9a35028ff4a78be4b02705342e6c1850265963f4bccc1c4b6f6587dba5
- clm_a5905276d3a216799da43f19296d6b8f8c36ef356891028f82fe4f629563f68b
- clm_b0a523d224d1f0301fe4f80e762249ae4fd312b0ead739e6a0823bc6c4748a1e
- clm_c132afbeb971f30e146e33c250bd15d87d4f1d1e0f5f1d3e1ceea70647bf8375
- clm_c863f303e5d4d2d57a04fb9adb17edb365fed95e27d80bc35f68889d1b6d9c49
- clm_cd97a1aa2883a7532e06187383b2d8db710f512d49746ef76167b3731311ffed
- clm_e8bd493fd8e6471cf257a5e41bcb6a5116aad2fbcf177fa4174aaa8f039b869b
maturity: draft
page_id: pg_3daf304736e356c08b6beb8e3edd81f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_158fd7f916aa5fc499884841151bb015
title: itwanger/PaiAgent/README.md @ 05297308189f
updated_at: '2026-09-14T03:59:38Z'
---

# itwanger/PaiAgent/README.md @ 05297308189f

<!-- rcw:begin owner=source:src_158fd7f916aa5fc499884841151bb015 block=evidence -->
- Skills load progressively in three levels (summary, full SKILL.md, reference docs) to save tokens, and are exposed to LLMs as Spring AI FunctionCallbacks (LoadSkillDetailFunction/LoadSkillReferenceFunction). [@claim:clm_01c4e6cc9fe45823c5361871ab44bbda7451d7fc05385905f10d18ef9b8de011]
- An EngineSelector routes execution by the workflow's engineType field: 'dag' to the DAG engine, 'langgraph' to LangGraph4j, with null defaulting to DAG for backward compatibility. [@claim:clm_124f58b9298e116bf52f4c56f450a552940ee33044f2c438bb830e5cd3844883]
- Repository development practice: contributors should fork, create a feature branch, commit, push, and open a PR; backend code follows the Alibaba Java manual, frontend follows Airbnb React style, and commits use Conventional Commits. [@claim:clm_142811aee456cf96f2ae7fa8efa4d708335919e58d4cacb1ae5ef1e4dce12ee5]
- Skills are defined declaratively via SKILL.md with YAML frontmatter (name, description) plus markdown rules, each skill being a directory with an optional reference subdirectory. [@claim:clm_1be3b820a09531870cebec0e8a1f807e5063f3a39bf6e99c77903cbd4ab3707b]
- The documented stack includes Java 21+, Spring Boot 3.4.1, Spring AI 1.0.0-M5, Spring AI Alibaba 1.0.0-M6.1, LangGraph4j, React 18, TypeScript 5, MyBatis-Plus 3.5.5, and MySQL 8.0+. [@claim:clm_613a0b83641226c40c2b0cee0df3d6bd452940be70876b164c488f3b759194c7]
- PaiAgent is described as an enterprise AI workflow visual orchestration platform with a drag-and-drop interface for building and running AI workflows without coding. [@claim:clm_679d10083e10d2f5373e6fac0bdb5506a1a8e2fec25e0110fa8eb9ce42665f0d]
- Repository development practice: setup requires Java 21+, Node.js 18+, MySQL 8.0+, and Maven 3.8+; the backend runs via ./mvnw spring-boot:run on port 8084 and the frontend via npm install/npm run dev on port 5173. [@claim:clm_8cd259420cd05c3c7349dc5750fd443ce6196b3209caa5c83a356d1eceb1bf45]
- The README states that changing the password after first login is a feature yet to be implemented, and the default admin/admin123 account is for development only. [@claim:clm_a1518d9a35028ff4a78be4b02705342e6c1850265963f4bccc1c4b6f6587dba5]
- The frontend is a ReactFlow-based flow editor supporting node dragging, edge wiring, and parameter editing, with a node panel, canvas, and configuration panel. [@claim:clm_a5905276d3a216799da43f19296d6b8f8c36ef356891028f82fe4f629563f68b]
- MinIO is listed as an optional object storage dependency; the Agent Plan plan proposes transferring generated images and videos to MinIO to avoid reliance on vendor temporary URLs. [@claim:clm_b0a523d224d1f0301fe4f80e762249ae4fd312b0ead739e6a0823bc6c4748a1e]
- The Skills system exposes REST endpoints: GET /api/skills for summaries, GET /api/skills/{name} for details, and GET /api/skills/{name}/references/{ref} for reference documents. [@claim:clm_c132afbeb971f30e146e33c250bd15d87d4f1d1e0f5f1d3e1ceea70647bf8375]
- LLM nodes are invoked through a ChatClientFactory that creates clients at runtime from node configuration (apiUrl, apiKey, model, temperature), supporting OpenAI-compatible providers including DeepSeek, Zhipu, and AIPing, plus Qwen via DashScope. [@claim:clm_c863f303e5d4d2d57a04fb9adb17edb365fed95e27d80bc35f68889d1b6d9c49]
- In the LangGraph4j engine, NodeAdapter adapts existing NodeExecutors into AsyncNodeActions, StateManager manages inputData/nodeOutputs/globalContext, and ExecutionEvent callbacks report node start/success/error. [@claim:clm_cd97a1aa2883a7532e06187383b2d8db710f512d49746ef76167b3731311ffed]
- The DAG engine uses Kahn's algorithm for topological ordering and DFS-based cycle detection, executes nodes in topological order, and passes upstream outputs to downstream nodes. [@claim:clm_e8bd493fd8e6471cf257a5e41bcb6a5116aad2fbcf177fa4174aaa8f039b869b]
<!-- rcw:end owner=source:src_158fd7f916aa5fc499884841151bb015 block=evidence -->

## Researcher notes

