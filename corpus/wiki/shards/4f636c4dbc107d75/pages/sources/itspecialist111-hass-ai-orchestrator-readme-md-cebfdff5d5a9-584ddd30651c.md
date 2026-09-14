---
access: public
aliases: []
claim_ids:
- clm_0fa9f1430e09c6fc6c71d0aa5379f8e28fe43f2f228f0b590968314e21b46ad4
- clm_1e09edac28b58b0df9287b60556f77c8d46883f3a126f372c6c25594d5d91787
- clm_27d9c2c451a972d50b987a52f1e0da2e170156d3fd45c1d690f64a9db70c3968
- clm_34f4137819cbb8a2c79ad38dd70609b68b04f9936f57b6813505270292874663
- clm_65c20e33ae4e9101b734854317d0465319f5101e5e244fd491513841b91074e3
- clm_6a7e09926eb22ee4b2f4afcb3808cc944e09cfe16a445b2029e6524ab1f66c2e
- clm_717fa1a3c10724d2ffd01ff15e34fb091620d3b72593a0d46542991a76ebd191
- clm_821177d2c56d976216e3361eeca529c3e1448d2fa33e5e531434c41a3170c35f
- clm_87d5076d3fe22b44736628b26adffc86a6799593962c6cc01d105c173b16b89c
- clm_8dc33c7f846956ad271682f75c9b7ad4f98c04448d339832a90de75e8d54517c
- clm_93d4790eced057dd32f7cf316a67a3c2cc204e655c258bf66e9c51f7509ba469
- clm_aef6b72ae13d6f0fd00a4d38430644a4aee5ebf2afcefcf22ffbddcf9bb99818
- clm_bf31b0a769bb898e96612356e0d9b3b121b5bee046063be2a4419b1a20f24786
- clm_bf746c72db4edddc90be666da354c5c470a0e82c46c42262ca4bf9b351f66d49
- clm_d5fbdda19865bdcaec9a7bda0c6f573cf8ae3a5d3e5bf1f096e9f77dd0c9eb80
- clm_d648f28e357e637424816064ce4bcf132eb99a43bd2a8194db1eceb4aee0121e
- clm_fb717924f68045f46fd8bfd046c8989f6edab43bd04a26d38338fdbf3923ab6d
maturity: draft
page_id: pg_c624cdd3fb7d5d0bbf50584ddd30651c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bef6479ee6b75cc9a868d26dc302639f
title: ITSpecialist111/HASS-AI-Orchestrator/README.md @ cebfdff5d5a9
updated_at: '2026-09-14T03:59:20Z'
---

# ITSpecialist111/HASS-AI-Orchestrator/README.md @ cebfdff5d5a9

<!-- rcw:begin owner=source:src_bef6479ee6b75cc9a868d26dc302639f block=evidence -->
- The kernel enforces hard budgets on reasoning iterations, tool calls, wall-clock time, context and result size; rejected calls still receive protocol-valid errors, and batches run concurrently only when entirely read-only. [@claim:clm_0fa9f1430e09c6fc6c71d0aa5379f8e28fe43f2f228f0b590968314e21b46ad4]
- An optional Streamable HTTP MCP client adds external tools, resources, and prompts with discovery, per-call timeouts, and namespacing; remote MCP annotations are kept as metadata but never automatically downgrade local safety policy. [@claim:clm_1e09edac28b58b0df9287b60556f77c8d46883f3a126f372c6c25594d5d91787]
- Three reasoning profiles (Rapid, Balanced, Deep) vary thinking, iteration, tool-call, and time ceilings while keeping identical schema validation, allowlists, approval requirements, and checkpointed replay. [@claim:clm_27d9c2c451a972d50b987a52f1e0da2e170156d3fd45c1d690f64a9db70c3968]
- A React dashboard provides Home, Ask & Run, Action center, Automation, Advanced insights, Dashboard Studio, and Quick Ask surfaces; generated dashboard HTML runs in an opaque sandbox under a restrictive CSP with no same-origin API access. [@claim:clm_34f4137819cbb8a2c79ad38dd70609b68b04f9936f57b6813505270292874663]
- Version 0.13 records whether Home Assistant accepted a service call but does not re-observe affected entities to verify physical outcomes; post-action verification is named as the next milestone, and Assist/voice integration is not yet included. [@claim:clm_65c20e33ae4e9101b734854317d0465319f5101e5e244fd491513841b91074e3]
- Plan execution uses an atomic claim so only one executor runs a plan, checkpoints after each step, stops on failure marking remaining steps skipped, and returns idempotent responses for already-completed plans. [@claim:clm_6a7e09926eb22ee4b2f4afcb3808cc944e09cfe16a445b2029e6524ab1f66c2e]
- Active model conversations do not resume across process restarts (persisted plans are durable), and an interrupted executing plan is intentionally never auto-replayed because a command may already have reached a device. [@claim:clm_717fa1a3c10724d2ffd01ff15e34fb091620d3b72593a0d46542991a76ebd191]
- The project is versioned v0.13.6 and is distributed as a Home Assistant add-on, with a badge claiming 286 backend tests passing. [@claim:clm_821177d2c56d976216e3361eeca529c3e1448d2fa33e5e531434c41a3170c35f]
- The design principle is that the model proposes while application code validates: the runtime, not the model, decides which tools exist, which domains/services are allowed, what needs approval, and what is audited. [@claim:clm_87d5076d3fe22b44736628b26adffc86a6799593962c6cc01d105c173b16b89c]
- Tool requests are validated against JSON Schema and local policy covering entity domains, service allowlists, blocked domains, and temperature bounds; dangerous domains like shell_command, hassio, script, automation, and rest_command are blocked by default. [@claim:clm_8dc33c7f846956ad271682f75c9b7ad4f98c04448d339832a90de75e8d54517c]
- The product ships dry-run by default with direct execution disabled; first-run config sets dry_run_mode true, reasoning_allow_direct_execute false, and legacy autonomous loops disabled. [@claim:clm_93d4790eced057dd32f7cf316a67a3c2cc204e655c258bf66e9c51f7509ba469]
- The kernel is provider-neutral, supporting local Ollama (default gemma4:e4b) plus OpenAI, Anthropic, GitHub Models, and Microsoft Foundry; requirements include Home Assistant OS/Supervised and an Ollama server or cloud credentials. [@claim:clm_aef6b72ae13d6f0fd00a4d38430644a4aee5ebf2afcefcf22ffbddcf9bb99818]
- Repository development practice: contributors run backend tests via pytest in a Python 3.11/3.12 venv, build the dashboard with npm ci/audit/build on Node 22, and can use a Dockerfile.test image for a lockfile-only reproducible test run. [@claim:clm_bf31b0a769bb898e96612356e0d9b3b121b5bee046063be2a4419b1a20f24786]
- The generic ha_call_service path is not exposed to the reasoning model; mutations go through a guarded local call_ha_service route so direct WebSocket access cannot bypass policy, and approval status is application context that model arguments cannot forge. [@claim:clm_bf746c72db4edddc90be666da354c5c470a0e82c46c42262ca4bf9b351f66d49]
- In plan and auto modes, state-changing calls are intercepted and simulated results are returned to the model; the exact tool name and arguments are recorded as a reviewable plan, later replayed in order without new model decisions. [@claim:clm_d5fbdda19865bdcaec9a7bda0c6f573cf8ae3a5d3e5bf1f096e9f77dd0c9eb80]
- Optional RAG and episodic memory use ChromaDB with local Ollama embeddings to store entity capabilities, manuals, past goals and outcomes, and user feedback; recalled episodes are reweighted by feedback without changing execution policy. [@claim:clm_d648f28e357e637424816064ce4bcf132eb99a43bd2a8194db1eceb4aee0121e]
- An eval scenario file defines representative home-agent goals (security approval, blocked domains, climate conflict, duplicates, ambiguity, etc.) scored by deterministic assertions on mutations, approvals, budgets, and forbidden tools rather than an LLM judge. [@claim:clm_fb717924f68045f46fd8bfd046c8989f6edab43bd04a26d38338fdbf3923ab6d]
<!-- rcw:end owner=source:src_bef6479ee6b75cc9a868d26dc302639f block=evidence -->

## Researcher notes

