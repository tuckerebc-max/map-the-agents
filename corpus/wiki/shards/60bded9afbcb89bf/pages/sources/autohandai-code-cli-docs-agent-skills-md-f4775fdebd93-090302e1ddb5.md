---
access: public
aliases: []
claim_ids:
- clm_04c47572c18fd0d86abcaa123f311b92e1c62c0ec1997f9dd8c144a8fff1abb0
- clm_0fe27beccf53825a779c8fe54ab85a48e0fbe14a5beab2eae40fbce7e008d9a9
- clm_6026759256d34afe67334115c65547ad00ed4365841d993485992fde236b68f4
- clm_6d7ed083768bb9f67c429da0c57011804668192a6954874c040aa51f48683123
- clm_7976533c20c6ab2bd70007c6148e0b32abdf754f3fd6c0a5b900f6f324b33559
- clm_96322a6ba78b65463d9e38171f3bf42b9501c816ac86f0a30e983412f045db00
- clm_c7d75e94edbeda87c007a68415cb256ae8d1493b7c07015a787e9a062e517227
- clm_d8fd1ecb52e61e022bfee0494a507fe87a913345c2cd9848b872ae7f44b1a96f
maturity: draft
page_id: pg_a41082accdd55c8da57e090302e1ddb5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_84e7823f7b4e56148c658cb71b054c55
title: autohandai/code-cli/docs/agent-skills.md @ f4775fdebd93
updated_at: '2026-09-14T01:35:30Z'
---

# autohandai/code-cli/docs/agent-skills.md @ f4775fdebd93

<!-- rcw:begin owner=source:src_84e7823f7b4e56148c658cb71b054c55 block=evidence -->
- Skills are discovered from many locations with later sources taking precedence, including built-in dist skills, Codex, Claude, shared agent directories, Autohand user/project dirs, and extension contributions. [@claim:clm_04c47572c18fd0d86abcaa123f311b92e1c62c0ec1997f9dd8c144a8fff1abb0]
- Skills are SKILL.md packages with YAML frontmatter (name, description, optional allowed-tools, license, compatibility, metadata) plus markdown instructions injected into agent context when activated. [@claim:clm_0fe27beccf53825a779c8fe54ab85a48e0fbe14a5beab2eae40fbce7e008d9a9]
- Delegated workers read up to five recent project lessons (each truncated to 1,000 chars) from the workspace's .autohand/memory; bare mode disables this, and agent.autoMemory:false disables automatic lesson saving. [@claim:clm_6026759256d34afe67334115c65547ad00ed4365841d993485992fde236b68f4]
- Skills declare a space-delimited allowed-tools list restricting which tools they may use, and the agent prompts before risky operations unless a different permission mode is chosen. [@claim:clm_6d7ed083768bb9f67c429da0c57011804668192a6954874c040aa51f48683123]
- Memory tools include save_memory, recall_memory (ranked by content, tags, recency), inspect_memory, and delete_memory which retains a canonical deletion event. [@claim:clm_7976533c20c6ab2bd70007c6148e0b32abdf754f3fd6c0a5b900f6f324b33559]
- Skills found in Codex or Claude locations are auto-copied to the corresponding Autohand locations, and existing Autohand skills are never overwritten. [@claim:clm_96322a6ba78b65463d9e38171f3bf42b9501c816ac86f0a30e983412f045db00]
- Slash commands include /skills (list, use, deactivate, info, new) and /deep-research with a /deep-search alias for research runs. [@claim:clm_c7d75e94edbeda87c007a68415cb256ae8d1493b7c07015a787e9a062e517227]
- The bundled deep-research skill runs multi-task research with persisted status (task progress, tool, evidence/failure counts, tokens), and a run is marked complete only after tasks finish, the report passes a source audit, and project checks pass. [@claim:clm_d8fd1ecb52e61e022bfee0494a507fe87a913345c2cd9848b872ae7f44b1a96f]
<!-- rcw:end owner=source:src_84e7823f7b4e56148c658cb71b054c55 block=evidence -->

## Researcher notes

