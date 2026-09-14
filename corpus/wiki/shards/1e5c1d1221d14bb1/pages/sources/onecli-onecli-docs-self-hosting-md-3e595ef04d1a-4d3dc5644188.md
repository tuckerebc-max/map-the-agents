---
access: public
aliases: []
claim_ids:
- clm_98b16239a052c95aeebc96a92a50232eaf733deb37c40bc0272cf6d3e17ebae9
maturity: draft
page_id: pg_c46be0c574325b84a4cf4d3dc5644188
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_655f57cebedd53cc980f44d4c8749d1d
title: onecli/onecli/docs/self-hosting.md @ 3e595ef04d1a
updated_at: '2026-09-14T02:25:50Z'
---

# onecli/onecli/docs/self-hosting.md @ 3e595ef04d1a

<!-- rcw:begin owner=source:src_655f57cebedd53cc980f44d4c8749d1d block=evidence -->
- Self-hosted upgrades must not use a bare `docker compose pull && up -d`, because the agent sandbox image is set via RUNNER_AGENT_IMAGE on the runner service and would silently stay stale while other services update. [@claim:clm_98b16239a052c95aeebc96a92a50232eaf733deb37c40bc0272cf6d3e17ebae9]
<!-- rcw:end owner=source:src_655f57cebedd53cc980f44d4c8749d1d block=evidence -->

## Researcher notes

