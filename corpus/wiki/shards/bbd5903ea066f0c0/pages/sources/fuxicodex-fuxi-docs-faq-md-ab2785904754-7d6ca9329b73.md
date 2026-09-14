---
access: public
aliases: []
claim_ids:
- clm_639ee5fabe7c55abd2aa268bd6483507d749312f36ab51860a108e802933efe4
- clm_6920e1412e414365b7e7e3f04f6a409ff062ee2b2d8713a9ea02e329e5c722c7
- clm_69f246579dd0af64583445181b87e87579175c693e7815b8d8477d26624cf843
- clm_d0e8c9ab428966612f3c83877527df401f3cedcfe59eb36b03befe04d55e2c91
maturity: draft
page_id: pg_74c878be1b7b50c1af1b7d6ca9329b73
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2f8a8a655d6b5dcabc93da7deb2a0832
title: fuxicodex/Fuxi/docs/faq.md @ ab2785904754
updated_at: '2026-09-14T02:01:12Z'
---

# fuxicodex/Fuxi/docs/faq.md @ ab2785904754

<!-- rcw:begin owner=source:src_2f8a8a655d6b5dcabc93da7deb2a0832 block=evidence -->
- The agent is described as running a Think → Act → Verify loop: it reasons about a task, acts with built-in tools, inspects results, and iterates until the work is verified. [@claim:clm_639ee5fabe7c55abd2aa268bd6483507d749312f36ab51860a108e802933efe4]
- Sessions are described as durable: transcripts persist to disk, checkpoints allow resume, rollback, or fork, long conversations auto-compact, and an idle 'dreaming' pass consolidates memory across sessions. [@claim:clm_6920e1412e414365b7e7e3f04f6a409ff062ee2b2d8713a9ea02e329e5c722c7]
- Shell commands reportedly pass an AST safety classifier and rule set before execution, with fine-grained permissions and audit logging; permission modes are default, plan, and bypassPermissions, plus a classifier-gated --auto mode with a circuit breaker. [@claim:clm_69f246579dd0af64583445181b87e87579175c693e7815b8d8477d26624cf843]
- The agent is documented as provider-agnostic: it accepts any OpenAI-compatible endpoint, Gemini, Bedrock/Vertex keys, or FuXi OAuth login, and acts as an MCP client. [@claim:clm_d0e8c9ab428966612f3c83877527df401f3cedcfe59eb36b03befe04d55e2c91]
<!-- rcw:end owner=source:src_2f8a8a655d6b5dcabc93da7deb2a0832 block=evidence -->

## Researcher notes

