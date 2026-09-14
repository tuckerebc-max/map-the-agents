---
access: public
aliases: []
claim_ids:
- clm_2d557867a9dab6f3dc5710744b8e538f944f043bb5711093c936fb1dc7bdafce
- clm_b1dc2bcf9fd858e42b55be9d90fd47cf1b25274f91483f3e1855d26587ff0a73
maturity: draft
page_id: pg_270467c8b3945d59920c1ddfe9327596
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ab8d75d27bf6575fb7aa43ae100252ad
title: shinpr/galley/SECURITY.md @ b542bd7adb37
updated_at: '2026-09-14T02:39:53Z'
---

# shinpr/galley/SECURITY.md @ b542bd7adb37

<!-- rcw:begin owner=source:src_ab8d75d27bf6575fb7aa43ae100252ad block=evidence -->
- Task YAML, profiles, and PR rerun comments are treated as privileged inputs that can influence local execution; PR comment requeueing is accepted only from the recorded PR author. [@claim:clm_2d557867a9dab6f3dc5710744b8e538f944f043bb5711093c936fb1dc7bdafce]
- Run evidence is recorded for review but is explicitly not a sandbox boundary; stronger isolation requires isolated worktrees, scoped paths, and local OS or container controls. [@claim:clm_b1dc2bcf9fd858e42b55be9d90fd47cf1b25274f91483f3e1855d26587ff0a73]
<!-- rcw:end owner=source:src_ab8d75d27bf6575fb7aa43ae100252ad block=evidence -->

## Researcher notes

