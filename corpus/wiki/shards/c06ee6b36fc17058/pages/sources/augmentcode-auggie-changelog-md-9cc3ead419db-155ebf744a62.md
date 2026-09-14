---
access: public
aliases: []
claim_ids:
- clm_02e32fea2e996a32228eb0bf65db22e99f799edd501d165da965f8fabce5198b
- clm_2f372183f531ae80ac14210c4882198c2e0686f17edf150642195ab6378eb226
- clm_58d20415375e64cb610aa1b53b4e56e4c228313ae5bec0d479504f87b0ce759e
- clm_94ca75d86417463177ef4a34c85bc07c8d0c0b3a0ea56249c1944e73ac6fbd68
- clm_bb6aa4baa53ac2950e632601244021ec28b30ae1d2cb06680ff81f5887ab8632
- clm_c891153b0c25cb92a2f474de5614be017e0705a0ac305c7b3205ebf296df91f8
- clm_cc0c65842f21631d8f769f8ca75851e105ce80d00e54ab0f31089ad845f60876
- clm_d71617e3f795f34ccb86dd6208675be90f559a79dc77ad5160b3a265a8bb893c
maturity: draft
page_id: pg_936c1448f54059d9b72e155ebf744a62
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_061f71807ff350e389b7aa8ca1683a76
title: augmentcode/auggie/CHANGELOG.md @ 9cc3ead419db
updated_at: '2026-09-14T01:35:48Z'
---

# augmentcode/auggie/CHANGELOG.md @ 9cc3ead419db

<!-- rcw:begin owner=source:src_061f71807ff350e389b7aa8ca1683a76 block=evidence -->
- Agent progress is saved incrementally after each LLM exchange to prevent loss on crashes, and queued messages persist in the session file across CLI restarts. [@claim:clm_02e32fea2e996a32228eb0bf65db22e99f799edd501d165da965f8fabce5198b]
- Saving files to sensitive paths requires approval, and denying a tool permission request provides clearer feedback, indicating a runtime permission model over tool use. [@claim:clm_2f372183f531ae80ac14210c4882198c2e0686f17edf150642195ab6378eb226]
- Plan mode saves plans to ~/.augment/plans/ and enforces strict read-only access; tool permissions default to denylist mode to prevent accidental lockout from all tools. [@claim:clm_58d20415375e64cb610aa1b53b4e56e4c228313ae5bec0d479504f87b0ce759e]
- The CLI loads specialized domain knowledge from SKILL.md files following the agentskills.io specification, and a /skills command shows loaded skills with approximate token usage. [@claim:clm_94ca75d86417463177ef4a34c85bc07c8d0c0b3a0ea56249c1944e73ac6fbd68]
- The agent supports built-in sub-agents including explore, auggie-guide, and a general-purpose sub-agent, and the agent loop executes independent tools in parallel. [@claim:clm_bb6aa4baa53ac2950e632601244021ec28b30ae1d2cb06680ff81f5887ab8632]
- Cloud subcommands include auggie cloud project, tunnel open/close/list, analytics, trigger enable/disable, and vfs get-url for compact durable VFS file links. [@claim:clm_c891153b0c25cb92a2f474de5614be017e0705a0ac305c7b3205ebf296df91f8]
- The CLI offers an MCP mode with --mcp-auto-workspace for on-the-fly workspace indexing, and an --acp flag for Agent Communication Protocol support. [@claim:clm_cc0c65842f21631d8f769f8ca75851e105ce80d00e54ab0f31089ad845f60876]
- A daemon component validates the host's Git version at startup, can be configured with a custom worktree directory, and can auto-discover git workspaces under a non-git container. [@claim:clm_d71617e3f795f34ccb86dd6208675be90f559a79dc77ad5160b3a265a8bb893c]
<!-- rcw:end owner=source:src_061f71807ff350e389b7aa8ca1683a76 block=evidence -->

## Researcher notes

