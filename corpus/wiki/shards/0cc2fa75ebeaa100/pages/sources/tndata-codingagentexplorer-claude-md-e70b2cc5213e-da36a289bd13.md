---
access: public
aliases: []
claim_ids:
- clm_2f36d62d4ed3c19aed46cee8d8374062e6431f183eff730991124ce7a7601a91
- clm_579dec6d2009efef92f3f6c1c09f2945cb56f07b4d608ffca444720fcf2b26cb
- clm_791dfcc0cf71e770528e6616582349dae29b4438246c69c6b41b500426f7eafb
maturity: draft
page_id: pg_2375c98520bf525f9460da36a289bd13
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9930a9445ce75614bbe568d29e0e9012
title: tndata/CodingAgentExplorer/CLAUDE.md @ e70b2cc5213e
updated_at: '2026-09-14T04:26:42Z'
---

# tndata/CodingAgentExplorer/CLAUDE.md @ e70b2cc5213e

<!-- rcw:begin owner=source:src_9930a9445ce75614bbe568d29e0e9012 block=evidence -->
- The MCP Observer acts as a transparent proxy on port 9999 between Claude Code and any HTTP-based MCP server, with the destination URL configured at runtime via a dashboard page. [@claim:clm_2f36d62d4ed3c19aed46cee8d8374062e6431f183eff730991124ce7a7601a91]
- Repository development practice: CLAUDE.md imposes a writing style rule for documentation, forbidding em dashes and dashes as sentence separators in README.md and other docs. [@claim:clm_579dec6d2009efef92f3f6c1c09f2945cb56f07b4d608ffca444720fcf2b26cb]
- Captured data is held in memory only: a circular buffer capped at 1000 requests for API traffic, plus in-memory stores for hook events and MCP requests (max 500), with no persistence. [@claim:clm_791dfcc0cf71e770528e6616582349dae29b4438246c69c6b41b500426f7eafb]
<!-- rcw:end owner=source:src_9930a9445ce75614bbe568d29e0e9012 block=evidence -->

## Researcher notes

