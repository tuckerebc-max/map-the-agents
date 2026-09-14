---
access: public
aliases: []
claim_ids:
- clm_05c3823377d183a77c704d3c247a32cb57cca1262f5ff7ca7c0c7e181c95261e
- clm_0e9b5754e76d7cd505e34f455794b1cc88a10f00ff9cb3e9b1e862c181fa263f
- clm_1d3a4b64f90b85a9a4bc4e3900aae8c865176dfef1947ee754749160244d23a5
- clm_6a13e834ba965d6387609918821a8da9eb651bb27f74492ccb32ecd76ce247ec
- clm_886a8211b7a533146c206af3c9510d614e8f8d73179a58f690d7bdbade760d8d
maturity: draft
page_id: pg_cb9f87ed6fed566ca953fdf89d408060
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_346f41afea9758489f6c402b4a103405
title: oracle-devrel/oracle-ai-developer-hub/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md
  @ 3317c535db76
updated_at: '2026-09-14T04:15:22Z'
---

# oracle-devrel/oracle-ai-developer-hub/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md @ 3317c535db76

<!-- rcw:begin owner=source:src_346f41afea9758489f6c402b4a103405 block=evidence -->
- The OAMP retrofit pass records the package version as oracleagentmemory==26.4.0, and a pre-flight step confirms 26.4.0 or newer is installed. [@claim:clm_05c3823377d183a77c704d3c247a32cb57cca1262f5ff7ca7c0c7e181c95261e]
- Documented OAMP quirks include context_card.formatted_content being a byte-for-byte alias of content, batch-written messages sharing one timestamp, and RECORD_CHUNKS holding roughly 1.3 rows per message. [@claim:clm_0e9b5754e76d7cd505e34f455794b1cc88a10f00ff9cb3e9b1e862c181fa263f]
- A decision tree in oamp.md maps memory shapes to tools: OAMP for conversational per-user durable memory, OracleVS for fixed RAG corpora, OracleChatHistory for simple chat logs, and SQL tables for counters and audit trails. [@claim:clm_1d3a4b64f90b85a9a4bc4e3900aae8c865176dfef1947ee754749160244d23a5]
- A shared oamp_helpers module exposes make_oamp_client, make_oamp_thread, and add_turn convenience functions, with auto-extraction enabled only when OCI_GENAI_API_KEY is set, otherwise degrading to manual-add mode. [@claim:clm_6a13e834ba965d6387609918821a8da9eb651bb27f74492ccb32ecd76ce247ec]
- A documented OAMP issue (V4-OAMP-1): batched add_messages calls count as one event, so memory-extraction frequency triggers never fire; the fix is per-turn writes via an add_turn helper. [@claim:clm_886a8211b7a533146c206af3c9510d614e8f8d73179a58f690d7bdbade760d8d]
<!-- rcw:end owner=source:src_346f41afea9758489f6c402b4a103405 block=evidence -->

## Researcher notes

