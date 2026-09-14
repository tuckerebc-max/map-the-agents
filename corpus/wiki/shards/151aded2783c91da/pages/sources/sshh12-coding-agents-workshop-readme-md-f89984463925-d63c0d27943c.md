---
access: public
aliases: []
claim_ids:
- clm_3a24e41a7d22f938e9f6c03f12b614ffa949c21a9361700581b4d36491b987f4
- clm_5ef416f9bdc401ddc5ba859c7f47ee6d7d7d99082298a01c4e888538486afd9c
- clm_8d83db98e981ef410254cf054fe37dc2a4adca5f490039653990502492b38c52
- clm_94460afd88b8f4f316442c0f7d36b23b813f91c5f6773bc5b6b7344bedb4a992
- clm_a8bc5c77fb4e9d3940afea22a711164bc501cf58717718024c74492d9431a2fa
- clm_ad1679e983fdb1a5a493e1cd8dff7ff3a2541745e9eabd6e24f884c89c477ac6
- clm_b463dc02256f210d6b0606a3e50b26cf28c29b4248d99efccf6bf1b9073d89d2
- clm_f140188f5cf95de41cb45561b91f44fb1c4064f1cbb8d5f3d14792087e00cf04
- clm_f1e6200057e23bdc213d39db615f9405cf033585b27aa6fda56f2e0ba09f1f5c
maturity: draft
page_id: pg_99edd23e24095ec4a441d63c0d27943c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3370d5924d6d5c39a588dccc7c3337f9
title: sshh12/coding-agents-workshop/README.md @ f89984463925
updated_at: '2026-09-14T04:23:31Z'
---

# sshh12/coding-agents-workshop/README.md @ f89984463925

<!-- rcw:begin owner=source:src_3370d5924d6d5c39a588dccc7c3337f9 block=evidence -->
- Both A/ and B/ implement the same ML Experiment Tracker with experiment tracking, run logging with metrics, run comparison charts, and a dashboard. [@claim:clm_3a24e41a7d22f938e9f6c03f12b614ffa949c21a9361700581b4d36491b987f4]
- The repo contains README.md, scorecard.md, race.md, slides.html with embedded speaker notes, and demo directories A/ (deliberate anti-patterns) and B/ (agent-optimized). [@claim:clm_5ef416f9bdc401ddc5ba859c7f47ee6d7d7d99082298a01c4e888538486afd9c]
- The repo holds materials for the 'Optimizing Codebases for Agents' workshop: a demo app in before/after versions, an AI-readiness scorecard, and agent race narrator notes. [@claim:clm_8d83db98e981ef410254cf054fe37dc2a4adca5f490039653990502492b38c52]
- The scorecard audits a codebase 0-3 across three dimensions (rules file/agent config, file organization, test & verification) for a max score of 9, and can be run by Claude Code via a provided prompt. [@claim:clm_94460afd88b8f4f316442c0f7d36b23b813f91c5f6773bc5b6b7344bedb4a992]
- The repository is MIT licensed. [@claim:clm_a8bc5c77fb4e9d3940afea22a711164bc501cf58717718024c74492d9431a2fa]
- Prerequisites include a laptop with a dev environment, an authenticated AI coding tool (Claude Code, Gemini CLI, Codex CLI, or Cursor), Python 3.10+, and a repo to audit. [@claim:clm_ad1679e983fdb1a5a493e1cd8dff7ff3a2541745e9eabd6e24f884c89c477ac6]
- The README documents running tests with pytest from the B/ directory. [@claim:clm_b463dc02256f210d6b0606a3e50b26cf28c29b4248d99efccf6bf1b9073d89d2]
- The two demo versions differ in code organization, not functionality: Version A is a realistic mess while Version B is optimized for coding agents. [@claim:clm_f140188f5cf95de41cb45561b91f44fb1c4064f1cbb8d5f3d14792087e00cf04]
- Version A runs via 'pip install -r requirements.txt' then 'python app.py' in A/; Version B uses 'pip install -r requirements.txt' then 'python manage.py run' in B/. [@claim:clm_f1e6200057e23bdc213d39db615f9405cf033585b27aa6fda56f2e0ba09f1f5c]
<!-- rcw:end owner=source:src_3370d5924d6d5c39a588dccc7c3337f9 block=evidence -->

## Researcher notes

