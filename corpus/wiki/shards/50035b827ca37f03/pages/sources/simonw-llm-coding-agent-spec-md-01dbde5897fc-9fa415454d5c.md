---
access: public
aliases: []
claim_ids:
- clm_00e53cc6633f6bddee4cade1ed3598f8dc6cd73854e7f8671bd2dded45883172
- clm_01e602b4a3b3c60f70407054fd9b8dbfb7f0bc9c6a149bd07577933ebe8e0ac9
- clm_2c1c5848689dbe4f5688bfedf3b1342d78ee8fd27a944634004f90efa1827a65
- clm_32ed866bcd5a9f97c53a291aabbd26ec1f96a6bc3e8608f9f366cd3b7c11ced8
- clm_37698841144f6e248c0570549c1451204410ec42d3e5e15ea26e0dcbea3b680c
- clm_3b973c5f241e60d897fa48bc5fceb0613d81ffe76c19e9fa6ef59c839a042462
- clm_70a40b8d7668a1e5e247e0904d1dbb2ba96dfcd85cde3b714f0ad26761eaff98
- clm_a7de350f2d97856f6fd0b7302d524d57ba3d6ed9b52bfc97373fa184b6958693
- clm_ba6ecd1deaba4c0493baada9920faa08f560a8dba835e9484a48deda377495b2
- clm_d5646bd937c74811f9b3f8697396fc75138c43621b9eb60ac2686a896068a30f
- clm_ead4edc1fbfe73e19563b5d0b12b3892066e45adec7c08ece3fb294e4f3d1ccb
maturity: draft
page_id: pg_17113f8c321858bebe4a9fa415454d5c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4f339094fadb542a85605b599c4b63de
title: simonw/llm-coding-agent/spec.md @ 01dbde5897fc
updated_at: '2026-09-14T02:39:56Z'
---

# simonw/llm-coding-agent/spec.md @ 01dbde5897fc

<!-- rcw:begin owner=source:src_4f339094fadb542a85605b599c4b63de block=evidence -->
- The permission system is implemented as a before_call callback on the chain (raising llm.CancelToolCall on denial), with --allow patterns and --yolo skipping prompts; approvals are session-scoped and not persisted. [@claim:clm_00e53cc6633f6bddee4cade1ed3598f8dc6cd73854e7f8671bd2dded45883172]
- All file access is confined to the session root: paths escaping via '..', absolute paths, or symlinks return an 'Error:' string instead of content, letting the model self-correct. [@claim:clm_01e602b4a3b3c60f70407054fd9b8dbfb7f0bc9c6a149bd07577933ebe8e0ac9]
- edit_file performs exact string replacement requiring old_string to appear exactly once unless replace_all is set, and returns a unified diff so the model can verify its edit. [@claim:clm_2c1c5848689dbe4f5688bfedf3b1342d78ee8fd27a944634004f90efa1827a65]
- Sessions are logged to LLM's SQLite database like `llm chat`, so `llm logs` shows full transcripts including tool calls, and conversations can be resumed via -c or --cid. [@claim:clm_32ed866bcd5a9f97c53a291aabbd26ec1f96a6bc3e8608f9f366cd3b7c11ced8]
- Read-only tools run freely, while writes, edits, and shell commands require approval; 'y' approves once, 'a' approves similar actions for the session, and denial is reported back to the model. [@claim:clm_37698841144f6e248c0570549c1451204410ec42d3e5e15ea26e0dcbea3b680c]
- The `llm code` CLI accepts options including an initial prompt, -m/--model, -s/--system, -d/--directory, --yolo, repeatable --allow glob patterns, --no-tool, -c/--continue, --cid, -o model options, and --chain-limit. [@claim:clm_3b973c5f241e60d897fa48bc5fceb0613d81ffe76c19e9fa6ef59c839a042462]
- The package requires Python 3.10+ and pins llm>=0.32a3, needing pip install --pre until LLM 0.32 is stable; it has no other runtime dependencies beyond what llm brings. [@claim:clm_70a40b8d7668a1e5e247e0904d1dbb2ba96dfcd85cde3b714f0ad26761eaff98]
- The spec lists non-goals for the initial release: no sandboxing or containerization (safety comes from the approval flow), no MCP, sub-agents, git or IDE integration, and no Windows-specific shell handling. [@claim:clm_a7de350f2d97856f6fd0b7302d524d57ba3d6ed9b52bfc97373fa184b6958693]
- The agent loop uses conversation.chain with a chain_limit (default 25) bounding tool-execution rounds per run; hitting the limit sets result.hit_limit and returns control to the user. [@claim:clm_ba6ecd1deaba4c0493baada9920faa08f560a8dba835e9484a48deda377495b2]
- search_files appears to use ripgrep when installed with a pure-Python fallback producing identical output; list_files reportedly respects .gitignore, delegating to git ls-files when available. [@claim:clm_d5646bd937c74811f9b3f8697396fc75138c43621b9eb60ac2686a896068a30f]
- A Python API exposes CodingAgent with model, root, approve, and chain_limit parameters; run() returns final text plus tool call/result pairs, and subsequent run() calls continue the same conversation. [@claim:clm_ead4edc1fbfe73e19563b5d0b12b3892066e45adec7c08ece3fb294e4f3d1ccb]
<!-- rcw:end owner=source:src_4f339094fadb542a85605b599c4b63de block=evidence -->

## Researcher notes

