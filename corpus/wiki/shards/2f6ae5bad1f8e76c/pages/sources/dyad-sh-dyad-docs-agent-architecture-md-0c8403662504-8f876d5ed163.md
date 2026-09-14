---
access: public
aliases: []
claim_ids:
- clm_276f6a53f22536c65aa73f2270fdabd2966b5b977fa02760bb63035850c9bbeb
- clm_5d803da96a1b00b2cc5d01f83b6d3de993dcd7a20a2b91c6d1d3877eda713fea
- clm_6c09f7f3268f9571d5ef067bd4b16aa0b7d99a7dda9b97b0f7b95ea7a8bde254
maturity: draft
page_id: pg_48440b6d68555693a2418f876d5ed163
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_253310f6882c56479f769950b6b562c6
title: dyad-sh/dyad/docs/agent_architecture.md @ 0c8403662504
updated_at: '2026-09-14T01:47:29Z'
---

# dyad-sh/dyad/docs/agent_architecture.md @ 0c8403662504

<!-- rcw:begin owner=source:src_253310f6882c56479f769950b6b562c6 block=evidence -->
- Repository development practice: contributors add tools in the local_agent/tools directory, register them in tool_definitions.ts, render their XML tag in DyadMarkdownParser.tsx, and can add E2E tests modeled on e2e-tests/local_agent*.spec.ts with tool-call fixtures. [@claim:clm_276f6a53f22536c65aa73f2270fdabd2966b5b977fa02760bb63035850c9bbeb]
- The local agent's core loop lives in src/pro/main/ipc/handlers/local_agent/local_agent_handler.ts, calling the LLM until it stops making tool calls or hits a per-turn maximum step count; tool_definitions.ts lists the agent's tools. [@claim:clm_5d803da96a1b00b2cc5d01f83b6d3de993dcd7a20a2b91c6d1d3877eda713fea]
- Dyad historically simulated tool calling with custom XML-like tags instead of models' formal tool calling, citing the ability to batch many calls and evidence that JSON code output hurts quality; a newer agent architecture moves toward standard tool calling. [@claim:clm_6c09f7f3268f9571d5ef067bd4b16aa0b7d99a7dda9b97b0f7b95ea7a8bde254]
<!-- rcw:end owner=source:src_253310f6882c56479f769950b6b562c6 block=evidence -->

## Researcher notes

