---
access: public
aliases: []
claim_ids:
- clm_0acfa49b0bd88396a9b621ab725f2943a7a55a2d83685f76f7d0c3ffd52204b3
- clm_2f014212af75a9cadb059ebea58098da837e3b697fff680b27c768d436886288
- clm_5d938e80747f10f9652a61c96c58e43f2202b09ef821f23d4e3110cd61509d20
- clm_69ccefc9b543fd9ad05673960e50d3124e920fd39a1306278275642cd46c9991
- clm_d2749f1e3e19ac4df142a4651e444d318f2bb4f3e27339876e84b5c61ed59442
- clm_dc9a3463ac96a3c82fa1e35d26f3a8082d6c96c50f732c7aeeb15d9478b72224
maturity: draft
page_id: pg_27d181253223594a8cdfc911deae00d7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b3efe320bae2544289f1a323ed424221
title: stippi/code-assistant/docs/configuration.md @ ba818a46c472
updated_at: '2026-09-14T02:43:45Z'
---

# stippi/code-assistant/docs/configuration.md @ ba818a46c472

<!-- rcw:begin owner=source:src_b3efe320bae2544289f1a323ed424221 block=evidence -->
- The product includes permission tiers and a command sandbox; --sandbox-mode offers danger-full-access (the default), read-only, and workspace-write, with --sandbox-network allowing outbound network access in workspace-write mode. [@claim:clm_0acfa49b0bd88396a9b621ab725f2943a7a55a2d83685f76f7d0c3ffd52204b3]
- Multiple LLM providers are supported, including Anthropic, OpenAI, Google Vertex AI, Ollama, OpenRouter, SAP AI Core, Groq, Cerebras, and Mistral, configured via providers.json and models.json with example files for each. [@claim:clm_2f014212af75a9cadb059ebea58098da837e3b697fff680b27c768d436886288]
- Sessions are per project with branching and persistent state; each chat session is permanently tied to its initial project/folder and tool syntax, which cannot be changed later. [@claim:clm_5d938e80747f10f9652a61c96c58e43f2202b09ef821f23d4e3110cd61509d20]
- Tool-invocation syntax is adaptive per session: native function calling, XML tags, or triple-caret blocks, selectable via --tool-syntax native|xml|caret. [@claim:clm_69ccefc9b543fd9ad05673960e50d3124e920fd39a1306278275642cd46c9991]
- Format-on-save runs project formatters after the assistant modifies matching files and updates tool parameters to reflect formatted content, keeping the model's view in sync without re-reading files; mappings pair glob patterns with shell commands. [@claim:clm_d2749f1e3e19ac4df142a4651e444d318f2bb4f3e27339876e84b5c61ed59442]
- CLI flags include --list-models/--list-providers, --model, --task, --continue-task, --use-diff-format, --record/--playback session recording, and --verbose logging. [@claim:clm_dc9a3463ac96a3c82fa1e35d26f3a8082d6c96c50f732c7aeeb15d9478b72224]
<!-- rcw:end owner=source:src_b3efe320bae2544289f1a323ed424221 block=evidence -->

## Researcher notes

