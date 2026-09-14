---
access: public
aliases: []
claim_ids:
- clm_6f1a3903af13faf53d0ee0aacc49fd405506897471a85c165496422c082af0aa
- clm_8a920caed05636898c6195b2cd4c34d6a221c07314b7da9740885be904f8350c
- clm_dbb3b4a94ff7321d3e0373b92966d5495d7ff303e99f7bc3d503d5c446e30109
- clm_f2c947a9f19b1d784c2b0d0e6cd2b452be5122ca16e1475def0aba4e9f4ff19c
maturity: draft
page_id: pg_c731f1f52f9d5e53963d958f8816c231
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_deff165050d350c0a855278608f03642
title: sumitsingh4411/repo-agent/docs/PLUGINS.md @ 703c1afdf6f3
updated_at: '2026-09-14T03:15:53Z'
---

# sumitsingh4411/repo-agent/docs/PLUGINS.md @ 703c1afdf6f3

<!-- rcw:begin owner=source:src_deff165050d350c0a855278608f03642 block=evidence -->
- Per the docs, remote MCP support covers Streamable HTTP with no-auth or bearer token only; legacy SSE-only servers and servers requiring OAuth login are not supported in this build. [@claim:clm_6f1a3903af13faf53d0ee0aacc49fd405506897471a85c165496422c082af0aa]
- Plugins are MCP servers addable from a built-in catalog of ~20 servers, from npm/GitHub packages (run via npx), custom stdio commands, or remote URLs over Streamable HTTP with optional bearer tokens. [@claim:clm_8a920caed05636898c6195b2cd4c34d6a221c07314b7da9740885be904f8350c]
- Plugin tools run without a confirmation prompt by default (repoAgent.plugins.autoRun = true); turning it off yields a Run/Reject prompt per external tool call. File edits are blocked from absolute paths and '..' traversal per the README. [@claim:clm_dbb3b4a94ff7321d3e0373b92966d5495d7ff303e99f7bc3d503d5c446e30109]
- API keys and plugin tokens are stored in VS Code SecretStorage rather than settings or repo files; the CLI keeps its own key store (~/.repo-agent.json, chmod 600, opt-in) since it cannot read VS Code SecretStorage. [@claim:clm_f2c947a9f19b1d784c2b0d0e6cd2b452be5122ca16e1475def0aba4e9f4ff19c]
<!-- rcw:end owner=source:src_deff165050d350c0a855278608f03642 block=evidence -->

## Researcher notes

