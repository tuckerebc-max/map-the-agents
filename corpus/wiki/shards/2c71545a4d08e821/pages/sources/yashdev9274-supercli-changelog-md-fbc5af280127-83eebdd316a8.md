---
access: public
aliases: []
claim_ids:
- clm_01915cabdfbdc69f6b779903d1df0bdbe581303facfc8e995c4968aa10bfe7ae
- clm_f25a73ac69b2902099a814e73b422d937572f3341d3da8ffe3931669cf7af91a
maturity: draft
page_id: pg_703b945e85b05178ad8783eebdd316a8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0f4cd2345f595c8e9473bfda7ec1a09c
title: yashdev9274/supercli/CHANGELOG.md @ fbc5af280127
updated_at: '2026-09-14T03:24:55Z'
---

# yashdev9274/supercli/CHANGELOG.md @ fbc5af280127

<!-- rcw:begin owner=source:src_0f4cd2345f595c8e9473bfda7ec1a09c block=evidence -->
- The CLI's Composio integration uses a fallback chain: server-side session proxy via a bearer-authenticated POST /api/composio endpoint, then local SDK, then user prompt; init and /mcp flows try the server session before prompting for an API key. [@claim:clm_01915cabdfbdc69f6b779903d1df0bdbe581303facfc8e995c4968aa10bfe7ae]
- The CLI added an @-picker with fuzzy file search, scroll-windowed slash commands and model selector, and a code review analysis prompt, per the changelog. [@claim:clm_f25a73ac69b2902099a814e73b422d937572f3341d3da8ffe3931669cf7af91a]
<!-- rcw:end owner=source:src_0f4cd2345f595c8e9473bfda7ec1a09c block=evidence -->

## Researcher notes

