---
access: public
aliases: []
claim_ids:
- clm_610b7a0ed807e18a8ea126fb8583085a5b542e09b41c06192521ee77eebe7767
- clm_714cdd3a88b182689ced3ed7c8102dfeccf237f985ab4eb7db6edc4125dc2da3
- clm_ad90ae8c769ec7ef371aefe1c085123297b9665c82e7c558c6d36143f0943421
- clm_b6dc40e2aa1b2397e4f838a476c907f7887851f5c228552c742d7e38030c53ba
- clm_e1f3dc42594528ec303261e906a0baf377c6928c123868c8fba36b419c4f4f5b
- clm_f24e628244b609e8f03050cdd02509be783eb23a4b6003100befbf9856eb6a8b
maturity: draft
page_id: pg_dd05878f35e2527c926fe14b335e5c7a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_22d12039694751a9b924123441d65177
title: EuniAI/Prometheus/README.md @ acb83608ed7f
updated_at: '2026-09-14T01:48:13Z'
---

# EuniAI/Prometheus/README.md @ acb83608ed7f

<!-- rcw:begin owner=source:src_22d12039694751a9b924123441d65177 block=evidence -->
- The platform exposes an API at localhost:9002 under /v1.2 with interactive docs at /docs, and requires a JWT secret generated via a provided script for authentication. [@claim:clm_610b7a0ed807e18a8ea126fb8583085a5b542e09b41c06192521ee77eebe7767]
- Prerequisites include Docker and Docker Compose, Python 3.11+ for local development, and API keys for OpenAI, Anthropic, or Google Gemini; PostgreSQL and Neo4j are required services. [@claim:clm_714cdd3a88b182689ced3ed7c8102dfeccf237f985ab4eb7db6edc4125dc2da3]
- A hierarchical multi-agent system routes user issues through a classification agent into bug, feature, and question pipelines, each with specialized downstream agents. [@claim:clm_ad90ae8c769ec7ef371aefe1c085123297b9665c82e7c558c6d36143f0943421]
- The README news section claims top-5 and top-1 rankings among GPT-5 agents on the SWE-bench leaderboard for automated software engineering as of 2025-11. [@claim:clm_b6dc40e2aa1b2397e4f838a476c907f7887851f5c228552c742d7e38030c53ba]
- Core components include a Tree-sitter-based AST/semantic knowledge graph in Neo4j, LangGraph state machines with checkpointing, Docker containers for isolated build/test execution, and multi-tier LLM integration (GPT-4, Claude, Gemini). [@claim:clm_e1f3dc42594528ec303261e906a0baf377c6928c123868c8fba36b419c4f4f5b]
- Prometheus is described as a platform using unified knowledge graphs and multi-agent systems to operate on multilingual codebases, built on LangGraph state machines. [@claim:clm_f24e628244b609e8f03050cdd02509be783eb23a4b6003100befbf9856eb6a8b]
<!-- rcw:end owner=source:src_22d12039694751a9b924123441d65177 block=evidence -->

## Researcher notes

