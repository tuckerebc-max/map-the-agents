---
access: public
aliases: []
claim_ids:
- clm_35d45516006b4b57f93bee8454fe1ceb94d9509b35cb552a83295a9e984e8676
- clm_5f51c880e86028c70ab1910e4e2f97963585cad0bfc4a5b351e12f44ab303fd0
- clm_a370a49cb525c91b4b180a5e73aaefa7c1c9d4a682dff74cb60829bec65d3954
maturity: draft
page_id: pg_89fd54cfc3cd54f4849258f16472a55c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8588319bbd6257edb80b893e50baab48
title: electric-sql/electric/AGENTS_MOBILE_CI_RELEASE_PLAN.md @ bb397424db0e
updated_at: '2026-09-14T03:49:21Z'
---

# electric-sql/electric/AGENTS_MOBILE_CI_RELEASE_PLAN.md @ bb397424db0e

<!-- rcw:begin owner=source:src_8588319bbd6257edb80b893e50baab48 block=evidence -->
- Repository development practice: authenticated EAS builds will not run on untrusted fork PRs because GitHub does not expose secrets to them; forks get local checks while EAS builds run for same-repo or trusted labeled PRs. [@claim:clm_35d45516006b4b57f93bee8454fe1ceb94d9509b35cb552a83295a9e984e8676]
- The mobile plan records that react, react-dom, react-native-webview, and TypeScript versions were aligned across the mobile/server-ui/runtime graph so expo-doctor passes 18/18 checks. [@claim:clm_5f51c880e86028c70ab1910e4e2f97963585cad0bfc4a5b351e12f44ab303fd0]
- The mobile package @electric-ax/agents-mobile is described as an existing Expo SDK 54 app using Expo Router, React Native, and Expo DOM Components to embed agents-server-ui surfaces. [@claim:clm_a370a49cb525c91b4b180a5e73aaefa7c1c9d4a682dff74cb60829bec65d3954]
<!-- rcw:end owner=source:src_8588319bbd6257edb80b893e50baab48 block=evidence -->

## Researcher notes

