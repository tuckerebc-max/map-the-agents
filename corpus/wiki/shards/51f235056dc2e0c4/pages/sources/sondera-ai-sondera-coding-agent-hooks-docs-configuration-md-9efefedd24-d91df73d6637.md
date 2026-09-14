---
access: public
aliases: []
claim_ids:
- clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26
- clm_282c65fb898dbc36c04ca741468f17d4fe306b35cfe25c16f96733339b435d11
- clm_3a741e09d77fec14ba60d2e5a9ae0b274fa33b27303aa30df5d27b2d97db7b71
- clm_62c117de4ded26410eb724f0fcc8271166c43e9219430589de5e69647fb51b55
maturity: draft
page_id: pg_13e9e3f513c45edfae7ad91df73d6637
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d86caacffeb959b98224e809250edad0
title: sondera-ai/sondera-coding-agent-hooks/docs/configuration.md @ 9efefedd249e
updated_at: '2026-09-14T04:22:24Z'
---

# sondera-ai/sondera-coding-agent-hooks/docs/configuration.md @ 9efefedd249e

<!-- rcw:begin owner=source:src_d86caacffeb959b98224e809250edad0 block=evidence -->
- Trajectories persist in a Turso (SQLite) store defaulting to ~/.sondera/trajectories/trajectories.db, overridable via --db; the console reads agents and trajectories from the same store. [@claim:clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26]
- Enabling the LLM classifiers adds latency to every decision they touch, and with guardrails enabled event content is sent to the configured provider. [@claim:clm_282c65fb898dbc36c04ca741468f17d4fe306b35cfe25c16f96733339b435d11]
- The optional LLM classifiers fail open when disabled, erroring, or slower than the adjudication budget — to compliant with no violations and to Public — so Cedar and the deterministic policies still decide. [@claim:clm_3a741e09d77fec14ba60d2e5a9ae0b274fa33b27303aa30df5d27b2d97db7b71]
- The signature engine and Cedar policies run with no external dependencies or API keys; the optional LLM classifiers support Ollama (the default when enabled), OpenAI-compatible servers, Anthropic, Gemini, and Vertex AI via Application Default Credentials. [@claim:clm_62c117de4ded26410eb724f0fcc8271166c43e9219430589de5e69647fb51b55]
<!-- rcw:end owner=source:src_d86caacffeb959b98224e809250edad0 block=evidence -->

## Researcher notes

