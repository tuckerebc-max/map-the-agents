---
access: public
aliases: []
claim_ids:
- clm_0a0964473c8029930c56cab3cf8d8f7b28aecff9901d61a45cdf1e743fcc1f06
- clm_0bf04f289b51c69cc642d32f20cd6c4d86b624a11d5b3b6b703b3e603d5b59f1
- clm_52a63a5bb611f6efa5da25183f53b9f82961beea8fb3f4ec728ce341f9d28174
- clm_708fdfd35af2be8823a0e18a2ab3e29a4369fc70a30341a35f437165b959857b
- clm_7bc19d50be447dcbfa54b8ddebc365320b5f4934f5083d4b0c4f9d2447f7aee9
- clm_a61d2ead309ce6c68c7ac0f0068086f825f48df1ac2a9bac2672ffca33373592
- clm_b79217b3d1b1768243712e81157a9a0ca75f2729cbb77e0e861834e3bc1c7d5c
- clm_bdbbbe8ee4b35a8e3672751a527d69a008ced067b8bec7bf946c2bc25f55a0f0
- clm_f364afc2bd420723a1c888fbc71bca542d1d96c458e873acf57a2d8fa7e0ddcb
- clm_f97403cc6d672a1b514a35357b067a8462650096440921437d47b2855ce28b00
maturity: draft
page_id: pg_fbba01aac77e5d9faa398e134e3d22f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ba901ff773915a95b36925118964c48d
title: OpenAutoCoder/live-swe-agent/README.md @ 8d7dd8634580
updated_at: '2026-09-14T02:25:55Z'
---

# OpenAutoCoder/live-swe-agent/README.md @ 8d7dd8634580

<!-- rcw:begin owner=source:src_ba901ff773915a95b36925118964c48d block=evidence -->
- Live-SWE-agent is built on top of the mini-swe-agent framework with very minimal modifications. [@claim:clm_0a0964473c8029930c56cab3cf8d8f7b28aecff9901d61a45cdf1e743fcc1f06]
- The README's setup guide link for installing mini-swe-agent appears empty, so installation instructions may be incomplete in this snapshot. [@claim:clm_0bf04f289b51c69cc642d32f20cd6c4d86b624a11d5b3b6b703b3e603d5b59f1]
- The project maintains a leaderboard where models are evaluated with Live-SWE-agent to enable apples-to-apples comparison of model capabilities. [@claim:clm_52a63a5bb611f6efa5da25183f53b9f82961beea8fb3f4ec728ce341f9d28174]
- The project positions itself as an open scaffold for fair benchmarking of LLMs on software engineering tasks, contrasting with proprietary scaffolds. [@claim:clm_708fdfd35af2be8823a0e18a2ab3e29a4369fc70a30341a35f437165b959857b]
- The agent is run via the mini CLI with a custom config file, e.g. `mini --config config/livesweagent.yaml`, with additional details in the config folder. [@claim:clm_7bc19d50be447dcbfa54b8ddebc365320b5f4934f5083d4b0c4f9d2447f7aee9]
- The agent is described as a live, runtime self-evolving software engineering agent that expands and revises its own capabilities while working on a real-world issue. [@claim:clm_a61d2ead309ce6c68c7ac0f0068086f825f48df1ac2a9bac2672ffca33373592]
- The README reports a 45.8% solve rate on SWE-Bench Pro, described as a state-of-the-art result as of Nov 17, 2025. [@claim:clm_b79217b3d1b1768243712e81157a9a0ca75f2729cbb77e0e861834e3bc1c7d5c]
- Complete trajectories, patches, and results for SWE-bench Verified and SWE-Bench Pro runs are published as release artifacts and Hugging Face datasets. [@claim:clm_bdbbbe8ee4b35a8e3672751a527d69a008ced067b8bec7bf946c2bc25f55a0f0]
- Gemini 3 Pro with Live-SWE-agent reportedly scored 77.4% on SWE-bench Verified, outperforming other available models per the README news section. [@claim:clm_f364afc2bd420723a1c888fbc71bca542d1d96c458e873acf57a2d8fa7e0ddcb]
- The README reports Claude Opus 4.5 with Live-SWE-agent scoring 79.2% on SWE-bench Verified, claimed to lead open-source scaffolds. [@claim:clm_f97403cc6d672a1b514a35357b067a8462650096440921437d47b2855ce28b00]
<!-- rcw:end owner=source:src_ba901ff773915a95b36925118964c48d block=evidence -->

## Researcher notes

