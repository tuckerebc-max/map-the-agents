---
access: public
aliases: []
claim_ids:
- clm_195c79988df5c73ee518bbb2fa0dc62a136a817846d08eb70933c659cb3f609d
- clm_25361fec5631fe529025b1f554ecee245f266b11a53756eac5aff8fdbf3d0c63
- clm_432c46a1516460a0a88f397f8d18bfe7da13b338d494b2ddfece6f03403fe7a3
- clm_c23581621ffc9beba7d5a02ab9bb11a29725159cadee817a948735d204eb9ed4
maturity: draft
page_id: pg_5d5dd0a11b965180bdd8ac7df5535c71
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_600d8a8dc7a1555d95256bd17bf81dab
title: semanser/codel/DEVELOPMENT.md @ fe1e846c9e04
updated_at: '2026-09-14T02:38:52Z'
---

# semanser/codel/DEVELOPMENT.md @ fe1e846c9e04

<!-- rcw:begin owner=source:src_600d8a8dc7a1555d95256bd17bf81dab block=evidence -->
- Repository development practice: contributors need golang, nodejs, docker, and postgresql; they copy .env.example files for backend and frontend, run 'go run .' in backend, and use 'yarn' then 'yarn dev' in frontend. [@claim:clm_195c79988df5c73ee518bbb2fa0dc62a136a817846d08eb70933c659cb3f609d]
- The backend appears to be written in Go, since the OpenAI model list is referenced via the go-openai Go package and development requires golang. [@claim:clm_25361fec5631fe529025b1f554ecee245f266b11a53756eac5aff8fdbf3d0c63]
- Repository development practice: the frontend expects VITE_API_URL without a URL scheme (e.g. localhost:8080, not http://localhost:8080), and backend optionally takes PORT (default 8080) and DATABASE_URL. [@claim:clm_432c46a1516460a0a88f397f8d18bfe7da13b338d494b2ddfece6f03403fe7a3]
- The backend exposes a GraphQL playground, indicated by the successful-start message pointing to http://localhost:<port>/playground. [@claim:clm_c23581621ffc9beba7d5a02ab9bb11a29725159cadee817a948735d204eb9ed4]
<!-- rcw:end owner=source:src_600d8a8dc7a1555d95256bd17bf81dab block=evidence -->

## Researcher notes

