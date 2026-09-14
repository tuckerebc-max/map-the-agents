---
access: public
aliases: []
claim_ids:
- clm_5b395fa597961f27b06eadc6e031e6477045deede9db7a963cd3117060a1fa10
- clm_c53309a951e85d864899bd535058b520c30b7b6aa1491c6403d71cc886b683f0
- clm_c5e652784b83f814f02a35332d26c154343003f876425e4ed7a181199ee86fe1
maturity: draft
page_id: pg_c9348a93e3765ed5a5f407fa56561125
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_27065fe524f5587d914f308eaea9c292
title: tractorjuice/arc-kit/docs/DEPENDENCY-MATRIX.md @ bc6bf533811d
updated_at: '2026-09-14T04:27:55Z'
---

# tractorjuice/arc-kit/docs/DEPENDENCY-MATRIX.md @ bc6bf533811d

<!-- rcw:begin owner=source:src_27065fe524f5587d914f308eaea9c292 block=evidence -->
- The azure-research, aws-research, and gcp-research commands require external MCP servers (Microsoft Learn, AWS Knowledge, and Google Developer Knowledge with an API key) for authoritative cloud documentation. [@claim:clm_5b395fa597961f27b06eadc6e031e6477045deede9db7a963cd3117060a1fa10]
- The trello backlog-export command requires `TRELLO_API_KEY` and `TRELLO_TOKEN` environment variables, and the tenders command relies on a bundled keyless UK Tenders MCP server with best-effort availability. [@claim:clm_c53309a951e85d864899bd535058b520c30b7b6aa1491c6403d71cc886b683f0]
- ArcKit commands follow a documented dependency matrix with MANDATORY, RECOMMENDED, and OPTIONAL dependency levels; the strategy command uniquely requires both principles and stakeholders as mandatory inputs. [@claim:clm_c5e652784b83f814f02a35332d26c154343003f876425e4ed7a181199ee86fe1]
<!-- rcw:end owner=source:src_27065fe524f5587d914f308eaea9c292 block=evidence -->

## Researcher notes

