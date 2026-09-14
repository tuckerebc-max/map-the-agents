# itwanger/paiagent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 05297308189f @ 136f02042d8f4a25

## Summary (orientation draft, not independently verified)

PaiAgent is documented as an enterprise AI workflow visual orchestration platform built on Spring Boot 3.4.1/Java 21 and React 18, with a dual DAG/LangGraph4j engine, a Skills system, and a plan document proposing Agent Plan integration (web search, memory, multimodal, RAG nodes). Evidence is documentation-based; setup, test, and contribution instructions are development practice, not runtime behavior. Evidence coverage: 184 of 360 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The Agent Plan integration plan specifies new node types: web_search/web_fetch, memory_write/memory_retrieve, image_generate/video_generate/vision_analyze, and knowledge_upsert/knowledge_retrieve, also registrable as ReAct Agent tools. -- evidence: [docs/agent-plan-harness-integration-plan.md#L22-L29](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L22-L29)
  - [observation/documented] The plan adds a volcengine_agent_plan provider with global config fields for embedding, image, video, and TTS models plus webSearchEnabled and memoryEnabled toggles, normalizing provider aliases like 'ark' and '火山方舟'. -- evidence: [docs/agent-plan-harness-integration-plan.md#L22-L29](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L22-L29), [docs/agent-plan-harness-integration-plan.md#L37-L43](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L37-L43), [docs/agent-plan-harness-integration-plan.md#L47-L47](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/agent-plan-harness-integration-plan.md#L47-L47)
- components (1 claim(s)):
  - [observation/documented] PaiAgent is described as an enterprise AI workflow visual orchestration platform with a drag-and-drop interface for building and running AI workflows without coding. -- evidence: [README.md#L26-L26](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L26-L26), [README.md#L5-L5](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L5-L5), [README.md#L7-L7](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L7-L7)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors should fork, create a feature branch, commit, push, and open a PR; backend code follows the Alibaba Java manual, frontend follows Airbnb React style, and commits use Conventional Commits. -- evidence: [README.md#L786-L788](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L786-L788), [README.md#L778-L782](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L778-L782)
  - [observation/documented] Repository development practice: setup requires Java 21+, Node.js 18+, MySQL 8.0+, and Maven 3.8+; the backend runs via ./mvnw spring-boot:run on port 8084 and the frontend via npm install/npm run dev on port 5173. -- evidence: [README.md#L462-L462](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L462-L462), [README.md#L380-L385](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L380-L385), [README.md#L486-L489](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L486-L489), [README.md#L481-L484](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L481-L484), [README.md#L452-L455](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L452-L455)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are defined declaratively via SKILL.md with YAML frontmatter (name, description) plus markdown rules, each skill being a directory with an optional reference subdirectory. -- evidence: [README.md#L669-L669](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L669-L669), [README.md#L682-L686](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L682-L686), [README.md#L671-L678](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L671-L678), [README.md#L106-L111](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L106-L111)
  - [observation/documented] Skills load progressively in three levels (summary, full SKILL.md, reference docs) to save tokens, and are exposed to LLMs as Spring AI FunctionCallbacks (LoadSkillDetailFunction/LoadSkillReferenceFunction). -- evidence: [README.md#L106-L111](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L106-L111), [README.md#L696-L699](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L696-L699)
- interfaces (3 claim(s)):
  - [observation/documented] The Skills system exposes REST endpoints: GET /api/skills for summaries, GET /api/skills/{name} for details, and GET /api/skills/{name}/references/{ref} for reference documents. -- evidence: [README.md#L703-L707](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L703-L707)
  - [observation/documented] The frontend is a ReactFlow-based flow editor supporting node dragging, edge wiring, and parameter editing, with a node panel, canvas, and configuration panel. -- evidence: [docs/FINAL_SUMMARY.md#L62-L65](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/FINAL_SUMMARY.md#L62-L65), [docs/FINAL_SUMMARY.md#L75-L77](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/FINAL_SUMMARY.md#L75-L77), [docs/FINAL_SUMMARY.md#L67-L73](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/docs/FINAL_SUMMARY.md#L67-L73), [README.md#L75-L75](https://github.com/itwanger/PaiAgent/blob/05297308189fa5054f1f5ac1af6346a48eea5aad/README.md#L75-L75)
- memory-state (1 claim(s)):
More evidence: [full detail](paiagent.detail.md)

Metadata and full claim list: [full detail](paiagent.detail.md)
Human notes ([notes](paiagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
