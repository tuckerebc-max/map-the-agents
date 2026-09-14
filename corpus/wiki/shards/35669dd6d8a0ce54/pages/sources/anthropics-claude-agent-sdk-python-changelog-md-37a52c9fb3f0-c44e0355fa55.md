---
access: public
aliases: []
claim_ids:
- clm_788eb7b986d8c40f01fa504ef2b120ed6c3b5bb547bfadaf59d6498ebb5b82c3
- clm_8188a3ef0ab129c393bbac20970dd3f193c656324f7d7d574215ea880cc7f638
- clm_8266ae1f684292ad3cce1db4ae92229c94bc77ea7e69ad874828fdb79b1758de
- clm_e56cc68f5d84e3920961f0d755857c8febc6dfa94c61099c7a4d39a45c711e23
maturity: draft
page_id: pg_e596e0bedee15d3ba2e4c44e0355fa55
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b58652636e515ed68e0e8f86e3a654b8
title: anthropics/claude-agent-sdk-python/CHANGELOG.md @ 37a52c9fb3f0
updated_at: '2026-09-14T01:33:27Z'
---

# anthropics/claude-agent-sdk-python/CHANGELOG.md @ 37a52c9fb3f0

<!-- rcw:begin owner=source:src_b58652636e515ed68e0e8f86e3a654b8 block=evidence -->
- Skill names in ClaudeAgentOptions.skills are validated at connect time; wildcard entries like "plugin:*" or "*" must be replaced with skills="all" or a Skill(...) rule in allowed_tools. [@claim:clm_788eb7b986d8c40f01fa504ef2b120ed6c3b5bb547bfadaf59d6498ebb5b82c3]
- On Windows, the SDK refuses to spawn .bat/.cmd CLI scripts and rejects cmd.exe metacharacters in resume/session_id values to prevent command injection. [@claim:clm_8188a3ef0ab129c393bbac20970dd3f193c656324f7d7d574215ea880cc7f638]
- The changelog documents security hardening such as validating skill names to prevent --allowedTools injection and passing --resume/--session-id as single =-joined argv tokens. [@claim:clm_8266ae1f684292ad3cce1db4ae92229c94bc77ea7e69ad874828fdb79b1758de]
- The mcp dependency was widened to mcp>=1.23.0,<3.0.0, supporting mcp 2.x for in-process servers served over mcp's in-memory transport. [@claim:clm_e56cc68f5d84e3920961f0d755857c8febc6dfa94c61099c7a4d39a45c711e23]
<!-- rcw:end owner=source:src_b58652636e515ed68e0e8f86e3a654b8 block=evidence -->

## Researcher notes

