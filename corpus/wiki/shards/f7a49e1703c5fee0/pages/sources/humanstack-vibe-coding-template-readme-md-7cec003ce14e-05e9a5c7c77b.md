---
access: public
aliases: []
claim_ids:
- clm_25ae4abfc6c9793739a041f533e38bbe5dbea58ddd02c9a078d24bfaf67e6bbe
- clm_26899ffffbf601995b0801b92d4d3240569253ceb5d717a2c01bf2f188ace99e
- clm_287aee8924c465f7f7b7f7bef87e62f69e59866dfebe153659e629292ecbfa43
- clm_4947b76bfe1e4c6475b49cd09b21b62f6e86f1e6415a272e6eb1f47de2c79b14
- clm_55039d88b7f6199ff53bd05094fc6da687beed15f61b036c7a0cfc91111a2a96
- clm_882e0ef5c44847fbbfcf2ee55d63250d4cfa5668906cdf26953d0e697807fcb1
- clm_8a2202f3089e9aa0c7d5bd0c536377bdb4631a1a215bd56952a5dd52d13a8cc1
- clm_e214456fd9a250d4bc11bc5352c910f5687496e0ecce1393e8b65f4a81418228
- clm_ea0dbbe6943764224bbd0c0a94e65958c9e38ac07ac843724a62cbae00bf8f7b
- clm_f6e674f5040deb64a79525f1a7570968541277baa9ab46141462f23aebf9951c
maturity: draft
page_id: pg_8b68929361a15f4fb01e05e9a5c7c77b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5bfb50cfdf6c5f2e8fe0ec5af803394c
title: humanstack/vibe-coding-template/README.md @ 7cec003ce14e
updated_at: '2026-09-14T03:57:10Z'
---

# humanstack/vibe-coding-template/README.md @ 7cec003ce14e

<!-- rcw:begin owner=source:src_5bfb50cfdf6c5f2e8fe0ec5af803394c block=evidence -->
- The backend includes an abstracted LLM service supporting OpenAI and Claude, a vector embeddings service, and Qdrant integration with document storage and semantic search. [@claim:clm_25ae4abfc6c9793739a041f533e38bbe5dbea58ddd02c9a078d24bfaf67e6bbe]
- The vector database layer falls back automatically to a local in-memory database when Qdrant is unavailable. [@claim:clm_26899ffffbf601995b0801b92d4d3240569253ceb5d717a2c01bf2f188ace99e]
- The frontend is a Next.js application using Tailwind CSS with a Supabase client and complete auth flows including login, signup, and password reset. [@claim:clm_287aee8924c465f7f7b7f7bef87e62f69e59866dfebe153659e629292ecbfa43]
- Prerequisites include Docker and Docker Compose, Make, Node.js 18+, Python 3.10+, and the Supabase CLI for migrations. [@claim:clm_4947b76bfe1e4c6475b49cd09b21b62f6e86f1e6415a272e6eb1f47de2c79b14]
- The template ships a Python FastAPI backend with Supabase integration for auth, database, realtime, storage, and migrations, plus LLM and vector-database services. [@claim:clm_55039d88b7f6199ff53bd05094fc6da687beed15f61b036c7a0cfc91111a2a96]
- Environment configuration requires Supabase URL and service key, OpenAI and/or Anthropic API keys for LLM features, and optionally Qdrant credentials. [@claim:clm_882e0ef5c44847fbbfcf2ee55d63250d4cfa5668906cdf26953d0e697807fcb1]
- Running the dev environment exposes the frontend at localhost:3000, the backend API at localhost:8000, and API docs at localhost:8000/docs. [@claim:clm_8a2202f3089e9aa0c7d5bd0c536377bdb4631a1a215bd56952a5dd52d13a8cc1]
- Repository development practice: setup is via ./first-time.sh (tool checks, API key prompts, .env generation) or manually by copying .env.example files, then make dev. [@claim:clm_e214456fd9a250d4bc11bc5352c910f5687496e0ecce1393e8b65f4a81418228]
- A Makefile provides commands such as make dev, prod variants, clean, and database migration commands like db-migration-new, db-apply, db-list, db-status, and db-push. [@claim:clm_ea0dbbe6943764224bbd0c0a94e65958c9e38ac07ac843724a62cbae00bf8f7b]
- Repository development practice: the repo includes Cursor rules under .cursor/rules/ that apply automatically based on edited files, with templates like @api-endpoint-template and @react-component-template. [@claim:clm_f6e674f5040deb64a79525f1a7570968541277baa9ab46141462f23aebf9951c]
<!-- rcw:end owner=source:src_5bfb50cfdf6c5f2e8fe0ec5af803394c block=evidence -->

## Researcher notes

