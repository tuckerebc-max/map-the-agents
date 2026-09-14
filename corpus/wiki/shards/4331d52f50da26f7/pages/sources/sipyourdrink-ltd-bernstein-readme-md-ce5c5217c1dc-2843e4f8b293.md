---
access: public
aliases: []
claim_ids:
- clm_13ac6865f2dc9682ee16f009703530addada0796f1539cf0d1828b475a359a66
- clm_24b48cfaf202ca21249154cfe5d376d482f770b9e5743a3908602581d21a96f9
- clm_86720398fff7f344e1d1b38cfcd51aed69ca2788453df3828eba6e18d87da653
- clm_9a4dd64a7a3eecb1a0aed8ed6d90bf6af73529b3ec4bb9f4f62d3ec8b92780cb
- clm_aacb4e5277f4c603c2fb561322cfad94c777f5c72965b6ee1da0bcf98c4c310d
- clm_bfc7ebce5ce6e4415806c3018a6a5963ee577342abc517038d699d809e1e5a1e
- clm_ec6127f7c96f95933f033be31f1faa794485ef1a6cda73a9abe39dbfc7e10088
maturity: draft
page_id: pg_7f2dedbe1e155662bce42843e4f8b293
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d129993ae9a751d88bad1c6df6a96bb0
title: sipyourdrink-ltd/bernstein/README.md @ ce5c5217c1dc
updated_at: '2026-09-14T04:21:54Z'
---

# sipyourdrink-ltd/bernstein/README.md @ ce5c5217c1dc

<!-- rcw:begin owner=source:src_d129993ae9a751d88bad1c6df6a96bb0 block=evidence -->
- The project targets Python 3.12+ per its README badge, is published on PyPI and GHCR, and is licensed Apache-2.0. [@claim:clm_13ac6865f2dc9682ee16f009703530addada0796f1539cf0d1828b475a359a66]
- Runs are declared in YAML manifests defining phases, roles, node dependencies, conditional edges, and retry policies; workflow resume validates the manifest digest at start and refuses a changed spec. [@claim:clm_24b48cfaf202ca21249154cfe5d376d482f770b9e5743a3908602581d21a96f9]
- The orchestrator is deterministic Python with no model in the coordination loop; only one planning LLM call happens up front, and the same plan replays to a byte-identical task graph. [@claim:clm_86720398fff7f344e1d1b38cfcd51aed69ca2788453df3828eba6e18d87da653]
- Volunteer compute tasks are constrained by a volunteer.json manifest declaring sandbox backend, network allowlist, and wall-clock/memory ceilings; a donor's own limits can only narrow, never widen, the declared containment. [@claim:clm_9a4dd64a7a3eecb1a0aed8ed6d90bf6af73529b3ec4bb9f4f62d3ec8b92780cb]
- The project is beta, solo-maintained, and under active development; minor versions may change interfaces, and users are advised to pin versions. The volunteer one-command runner and the hosted api.bernstein.run service are not yet available. [@claim:clm_aacb4e5277f4c603c2fb561322cfad94c777f5c72965b6ee1da0bcf98c4c310d]
- The CLI surface includes bernstein init, -g, live, run plan.yaml, stop, workflow run/resume, replay/lineage/audit verification commands, and bernstein verify receipt for offline receipt checking. [@claim:clm_bfc7ebce5ce6e4415806c3018a6a5963ee577342abc517038d699d809e1e5a1e]
- bernstein bench run <suite> --reliability k (also spelled bernstein eval) runs each task k times under fixed coordination and reports a pass^k floor alongside pass@1, sealing the result in a signed receipt that can be re-verified offline. [@claim:clm_ec6127f7c96f95933f033be31f1faa794485ef1a6cda73a9abe39dbfc7e10088]
<!-- rcw:end owner=source:src_d129993ae9a751d88bad1c6df6a96bb0 block=evidence -->

## Researcher notes

