---
access: public
aliases: []
claim_ids:
- clm_25810b429e727ab22fff0acff556f07cf65533ef5dbb93c768010d7f178fd5c2
- clm_45445fbdf514406b74e3437b967142d27a0b8de6e334151a763a369fbc6f7f1e
maturity: draft
page_id: pg_d5987279080c509db2db111c0840c4b2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b314598f5fd255fb835b9e176f8bd01e
title: coze-dev/coze-studio/CLAUDE.md @ fefb05ff27be
updated_at: '2026-09-14T03:42:58Z'
---

# coze-dev/coze-studio/CLAUDE.md @ fefb05ff27be

<!-- rcw:begin owner=source:src_b314598f5fd255fb835b9e176f8bd01e block=evidence -->
- Repository development practice: contributors use a Rush.js monorepo with 135+ frontend packages, run tests via rush test / go test, and follow coverage targets by package level (80% for level 1). [@claim:clm_25810b429e727ab22fff0acff556f07cf65533ef5dbb93c768010d7f178fd5c2]
- Repository development practice: model configuration requires copying a template in backend/conf/model/ and setting id, API key, and model; supported providers include OpenAI, Volcengine Ark, Claude, Gemini, Qwen, DeepSeek, and Ollama. [@claim:clm_45445fbdf514406b74e3437b967142d27a0b8de6e334151a763a369fbc6f7f1e]
<!-- rcw:end owner=source:src_b314598f5fd255fb835b9e176f8bd01e block=evidence -->

## Researcher notes

