---
access: public
aliases: []
claim_ids:
- clm_0d67e716fde8c277f703c18068b426a5beea4b7e80e95030f1e679a8f42e7fa3
- clm_3fa7fe2bc667035fce1f33e22972e1cde467fae7e1c04f3d11ee34b8e1772cec
- clm_8a61315b01ddc5298e4b601e8ab6042b77b3a7780f7011adb8aaab3775921913
- clm_a16d06e3346b1fec9bd79f9a09dad95bf041044219cd5358567091d54cf10adf
- clm_a8eef703a36a5bbaffa6690914f0844482e9e81e09f9bbf6ca329e377edae4cf
- clm_af120992b96e69e10cb8562b03d9ccfb2d8c48f61dccea6c6def3e9ded1ab4d4
- clm_bc9bc372df5b644b1a5e2000ecdf50c40aa50ff2d10d21aec70e87fc3c37f4d8
- clm_c60e4526a9c72ce521f467097df97c2cc51edb3606afb95c91f01975c7dd0428
- clm_d70e50f0438c6198cce0898e29e13a356539b7faf98ff4a2c8410095e8f4eb9e
- clm_dd7ef5b37d6ae51caed3095a6949899a0517d7d127502e5eebef58a2276624c7
maturity: draft
page_id: pg_29b099380ec6596281789b2fd1118bbf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e0a28758f1a5dc18523aafbcfcd4303
title: divar-ir/ai-doc-gen/README.md @ bd3aba71a0c5
updated_at: '2026-09-14T03:48:05Z'
---

# divar-ir/ai-doc-gen/README.md @ bd3aba71a0c5

<!-- rcw:begin owner=source:src_7e0a28758f1a5dc18523aafbcfcd4303 block=evidence -->
- The stack is Python 3.13 with pydantic-ai for agent orchestration, OpenAI-compatible APIs for LLM access, GitPython and python-gitlab for Git/GitLab operations, and logfire/OpenTelemetry plus optional Langfuse for observability. [@claim:clm_0d67e716fde8c277f703c18068b426a5beea4b7e80e95030f1e679a8f42e7fa3]
- Installation is documented via uv (recommended) or pip, and a Dockerfile plus a Helm chart under k8s/helm support containerized and Kubernetes CronJob deployments. [@claim:clm_3fa7fe2bc667035fce1f33e22972e1cde467fae7e1c04f3d11ee34b8e1772cec]
- Analyzer agents run in parallel through a configurable worker pool controlled by ANALYZER_MAX_WORKERS, where 0 means auto-detecting the CPU count; a --max-workers flag can cap concurrency. [@claim:clm_8a61315b01ddc5298e4b601e8ab6042b77b3a7780f7011adb8aaab3775921913]
- The tool appears most relevant to teams using GitLab and AI coding assistants (Claude Code, Cursor) who want automated, recurring documentation updates via merge requests. [@claim:clm_a16d06e3346b1fec9bd79f9a09dad95bf041044219cd5358567091d54cf10adf]
- The tool analyzes repositories with five specialized analysis agents (code structure, dependencies, data flow, request flow, APIs) and generates a README plus AI assistant configuration files such as CLAUDE.md, AGENTS.md, and Cursor rules. [@claim:clm_a8eef703a36a5bbaffa6690914f0844482e9e81e09f9bbf6ca329e377edae4cf]
- The repository ships as an installable Claude Code plugin providing three skills: analyze-codebase, generate-readme, and generate-ai-rules, installable via the plugin marketplace commands. [@claim:clm_af120992b96e69e10cb8562b03d9ccfb2d8c48f61dccea6c6def3e9ded1ab4d4]
- Agents access the codebase through registered tools: FileReadTool for ranged file reading and ListFilesTool for filtered recursive listing, both registered with every agent. [@claim:clm_bc9bc372df5b644b1a5e2000ecdf50c40aa50ff2d10d21aec70e87fc3c37f4d8]
- Configuration is layered with precedence from Pydantic defaults, then a .ai/config.yaml (or .yml) file in the target repository, then CLI flags. [@claim:clm_c60e4526a9c72ce521f467097df97c2cc51edb3606afb95c91f01975c7dd0428]
- The CLI exposes analyze, generate readme, and generate ai-rules commands taking a --repo-path argument, plus a cronjob analyze command; an ai-doc-gen console script exposes the same CLI. [@claim:clm_d70e50f0438c6198cce0898e29e13a356539b7faf98ff4a2c8410095e8f4eb9e]
- The architecture is layered: an argparse CLI entry point, command-specific handlers implementing an AbstractHandler interface, pydantic-ai agents with YAML/Jinja2 prompts, and a tool layer with file-reading and file-listing tools registered with every agent. [@claim:clm_dd7ef5b37d6ae51caed3095a6949899a0517d7d127502e5eebef58a2276624c7]
<!-- rcw:end owner=source:src_7e0a28758f1a5dc18523aafbcfcd4303 block=evidence -->

## Researcher notes

