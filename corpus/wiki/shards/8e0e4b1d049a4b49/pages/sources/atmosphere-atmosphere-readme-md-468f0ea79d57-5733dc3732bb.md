---
access: public
aliases: []
claim_ids:
- clm_1d8a5d6574f48abd25d811da533c4341eefd473c537d96def482da856dd7a66b
- clm_1e5262574ae80babe3f511539e5876c8a6270d2afb102599dd2f1d5ac4318e3f
- clm_59e1042ef9426e125d9916612293db078e2cb6e1258ba03a124b50767486c5c8
- clm_6bcef9d731bbe2026b8a197c2d7cfb552b7356f3a7787bafcc153e10c2271495
- clm_866dbf102562ab740b8c8ed962d16fcd651a2a2ca03d871ac77d80fc8d80b761
- clm_9495451c2824285e4cdf93b4cf5acbadfd3df68688b1febe8f9c0a066640d41b
- clm_ba10976b125261eb4662d9e32927cc3641c68a9993b7d1677164a87c7d833aa6
- clm_dcbd1dfe153dd5b16dd19e6fa54acf0eaac04d057dd760a6929b6e103c28a90a
- clm_f8ae665ea548119f524007c1f61b5ff38a134d5f727d987a48c53adb0c5521b8
- clm_fb6713b36ffa426fdcdb8eda2035d0323e5d3e8314d5858e62985d1fde7743fb
maturity: draft
page_id: pg_752af07972f3529ab5e05733dc3732bb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_53f2e9b934f0535a927d22c15844d65b
title: Atmosphere/atmosphere/README.md @ 468f0ea79d57
updated_at: '2026-09-14T01:35:28Z'
---

# Atmosphere/atmosphere/README.md @ 468f0ea79d57

<!-- rcw:begin owner=source:src_53f2e9b934f0535a927d22c15844d65b block=evidence -->
- Requirements are Java 21+, Spring Boot 4.1.0 or 3.5 via the -Pspring-boot3 profile, and Quarkus 3.36.3+; artifacts are published to Maven Central and atmosphere.js to npm. [@claim:clm_1d8a5d6574f48abd25d811da533c4341eefd473c537d96def482da856dd7a66b]
- Multi-agent orchestration uses @Coordinator and AgentFleet with handoffs, conditional routing, an event-sourced coordination journal, and durable hibernating Workflow<S> over a CheckpointStore (optionally Temporal-backed). [@claim:clm_1e5262574ae80babe3f511539e5876c8a6270d2afb102599dd2f1d5ac4318e3f]
- The CLI can import agent skill files, e.g. atmosphere import of an Anthropic SKILL.md URL, and a companion atmosphere-skills repository offers curated skill files. [@claim:clm_59e1042ef9426e125d9916612293db078e2cb6e1258ba03a124b50767486c5c8]
- Runtime adapter capabilities are pinned by AbstractAgentRuntimeContractTest.expectedCapabilities(), so a runtime cannot drift from its declared feature set without breaking tests. [@claim:clm_6bcef9d731bbe2026b8a197c2d7cfb552b7356f3a7787bafcc153e10c2271495]
- Governance controls include GovernancePolicy/PolicyRing with allow/deny lists and rate limits, @AgentScope purpose enforcement, tool approval policies, and a plan-and-verify verifier module. [@claim:clm_866dbf102562ab740b8c8ed962d16fcd651a2a2ca03d871ac77d80fc8d80b761]
- The atmosphere-ai module ships an AgentRuntime SPI with a built-in OpenAI-compatible adapter; eleven more adapters live in separate modules, two of which (Anthropic, Cohere) are native HTTP+SSE clients. [@claim:clm_9495451c2824285e4cdf93b4cf5acbadfd3df68688b1febe8f9c0a066640d41b]
- Classpath modules register endpoints: browser endpoint at /atmosphere/agent/my-agent, MCP at .../mcp, A2A at .../a2a, AG-UI at .../agui, plus an admin dashboard and console UI. [@claim:clm_ba10976b125261eb4662d9e32927cc3641c68a9993b7d1677164a87c7d833aa6]
- Governance policy can be declared in YAML (deny-list phrases, cost ceilings) or via annotations such as @AgentScope with purpose, forbiddenTopics, and breach behavior. [@claim:clm_dcbd1dfe153dd5b16dd19e6fa54acf0eaac04d057dd760a6929b6e103c28a90a]
- Memory is provided as AiConversationMemory per-conversation history and LongTermMemory per-user facts, in-memory or durable via SQLite/Redis modules, with a SemanticRecallInterceptor for vector recall. [@claim:clm_f8ae665ea548119f524007c1f61b5ff38a134d5f727d987a48c53adb0c5521b8]
- A single @Agent annotation declares an agent, with @Prompt for streaming messages, @Command for slash commands (including confirmation prompts), and @AiTool for tool methods. [@claim:clm_fb6713b36ffa426fdcdb8eda2035d0323e5d3e8314d5858e62985d1fde7743fb]
<!-- rcw:end owner=source:src_53f2e9b934f0535a927d22c15844d65b block=evidence -->

## Researcher notes

