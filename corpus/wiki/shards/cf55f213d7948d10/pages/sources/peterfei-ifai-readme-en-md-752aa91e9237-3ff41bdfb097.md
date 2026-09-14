---
access: public
aliases: []
claim_ids:
- clm_59b10a8fbcc65b3713908afe4bd164bd7d639be89e36cc4f17cf14a45cb4118a
- clm_6148060d7efe4394c094d1e0b2792d441807e4caeb4c103a275c4729f4b7cda1
- clm_6fcc1a17f0d893a7adc297e90edd9a53fd882125e245324e9ee24985374c1984
- clm_7bc32c3ea497a44151884b763603da68add2fab948f35b4dbc94fe3d72b5f92c
- clm_a66a8e4710f7ca2f98115b6a508fa56d58fbef580047cfbec12bd82755e530d7
- clm_d693faf2ff416dd616d41c4949ba06581566dd1ddf6d70f1487a18682759e198
- clm_d7bd0f904c57fea557f3d37d67186429cc8f88562256396ca8f1cbf7d0625d28
maturity: draft
page_id: pg_93a6a1cf5f8e5afc90433ff41bdfb097
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c3be4a8e3ee1562c80a855d9082a5558
title: peterfei/ifai/README_EN.md @ 752aa91e9237
updated_at: '2026-09-14T02:30:22Z'
---

# peterfei/ifai/README_EN.md @ 752aa91e9237

<!-- rcw:begin owner=source:src_c3be4a8e3ee1562c80a855d9082a5558 block=evidence -->
- Agents have shell-level control and can execute commands such as npm, git, and cargo to install dependencies and self-heal environments; the changelog notes a 100% trust model with tool-call limits raised from 100 to 1000. [@claim:clm_59b10a8fbcc65b3713908afe4bd164bd7d639be89e36cc4f17cf14a45cb4118a]
- The architecture diagram shows a React 19 interaction layer over a Rust/Tauri 2.0 core, with AI services for DeepSeek, Kimi, and Qwen models, a RAG/vector engine, and system services for Shell, PTY, and Git; building requires Node.js >= 18 and Rust >= 1.80. [@claim:clm_6148060d7efe4394c094d1e0b2792d441807e4caeb4c103a275c4729f4b7cda1]
- The product ships specialized agents (Explore, Review, Refactor, Test, Doc, Plan, ReAct, Git Commit, Debug) coordinated via a YAML-declarative DAG workflow engine with topological-sort scheduling supporting sequential and parallel execution. [@claim:clm_6fcc1a17f0d893a7adc297e90edd9a53fd882125e245324e9ee24985374c1984]
- Repository development practice: contributors run the app in dev mode with npm run tauri dev after npm install, and build releases with npm run build:community followed by npm run tauri:community; the HTTP API is enabled in dev via ENABLE_HTTP_API=true. [@claim:clm_7bc32c3ea497a44151884b763603da68add2fab948f35b4dbc94fe3d72b5f92c]
- Agents can invoke other agents up to a maximum depth of 5 levels, and a collaboration framework provides parallel invocation, knowledge sharing, and result aggregation primitives. [@claim:clm_a66a8e4710f7ca2f98115b6a508fa56d58fbef580047cfbec12bd82755e530d7]
- IfAI is described as an AI-native code editor and agent orchestration assistant built on Tauri 2.0 and React 19, with 9+ collaborating agents driven by DAG workflows. [@claim:clm_d693faf2ff416dd616d41c4949ba06581566dd1ddf6d70f1487a18682759e198]
- A declarative intent-routing system uses O(1) lookup-table routing to match natural-language task descriptions to the appropriate agent or workflow. [@claim:clm_d7bd0f904c57fea557f3d37d67186429cc8f88562256396ca8f1cbf7d0625d28]
<!-- rcw:end owner=source:src_c3be4a8e3ee1562c80a855d9082a5558 block=evidence -->

## Researcher notes

