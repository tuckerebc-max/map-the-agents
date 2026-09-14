---
access: public
aliases: []
claim_ids:
- clm_38c61cce565629a074ed964da1c14ca3b000211d5a61d1b1ce1384b368e588e4
- clm_3af7ab718bcdc97d5b61b3ee2be67fce744197e4861011292aebe22c1f89bfbf
- clm_6f5411b8c7a55f2cf10ddaf47c3f2a726f7e2e064f1c513f8c7aefbd6ddb9e6a
- clm_7bc1e401d59be4d25fc94a0d810f93d5808a5f468b6e6dcb30c793f993ad1c77
- clm_8207e6c9419d8e63eb62d7cba4b27e1c2c5bb05ab922b6e5341db7eaccd769cb
- clm_8849efd66f1205586c9c2b171e884a4def0e1641644273156c58b9e36c22e55e
maturity: draft
page_id: pg_5021d2ad7cfa5d358dd20fc776b4d4e4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_78784ab34c0f58be8574d58faed5a3e5
title: talmetis-labs/aizen/README.md @ 997bdd3bbba4
updated_at: '2026-09-14T04:25:49Z'
---

# talmetis-labs/aizen/README.md @ 997bdd3bbba4

<!-- rcw:begin owner=source:src_78784ab34c0f58be8574d58faed5a3e5 block=evidence -->
- Aizen is documented as a single static binary (~34 MB, ~10 ms cold start claimed) requiring no Node, Python, Docker, or cloud account, targeting Windows, Linux, and macOS. [@claim:clm_38c61cce565629a074ed964da1c14ca3b000211d5a61d1b1ce1384b368e588e4]
- The agent accepts any OpenAI-style /chat/completions endpoint, including OpenAI, OpenRouter, local llama.cpp/vLLM, or an Anthropic gateway. [@claim:clm_3af7ab718bcdc97d5b61b3ee2be67fce744197e4861011292aebe22c1f89bfbf]
- The sandbox runs commands without inheriting API keys, denies network by default, and enforces filesystem policy via Landlock+seccomp on Linux and Seatbelt on macOS; Windows uses Job-Object containment and reports 'partial'. [@claim:clm_6f5411b8c7a55f2cf10ddaf47c3f2a726f7e2e064f1c513f8c7aefbd6ddb9e6a]
- A 'Pantheon' of seven capability-scoped sub-agents (argus, metis, daedalus, nemesis, themis, clio, mnemosyne) is fanned out via `aizen workflow`, which synthesizes one answer. [@claim:clm_7bc1e401d59be4d25fc94a0d810f93d5808a5f468b6e6dcb30c793f993ad1c77]
- The agent is documented to keep an offline BM25-ranked memory that learns from reuse, plus a persona, a durable 'SOUL' identity, and skills it writes for itself after real work. [@claim:clm_8207e6c9419d8e63eb62d7cba4b27e1c2c5bb05ab922b6e5341db7eaccd769cb]
- Repository development practice: contributors sign a CLA once via a bot-comment flow with the exact sentence 'I have read the CLA Document and I hereby sign the CLA'; the CLA grants the maintainer commercial relicensing rights while the public project stays Apache-2.0. [@claim:clm_8849efd66f1205586c9c2b171e884a4def0e1641644273156c58b9e36c22e55e]
<!-- rcw:end owner=source:src_78784ab34c0f58be8574d58faed5a3e5 block=evidence -->

## Researcher notes

