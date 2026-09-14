---
access: public
aliases: []
claim_ids:
- clm_03829bc430697e0d5f36a18217880cc4563cfef75e50068e789653eaa3e1d8ed
- clm_1b59d6e4bd9603dba68e8bbbb6dc79b31a21f21a7358b5af34374351160ef510
- clm_1b65dde6f0c2c6e84dca08d7db333007d5e55cbd7922643f8d0004341ed4e84d
- clm_215efc569222f7db7773e6680b47fd2344eb32c11153f927502c9b9f4a5e521f
- clm_28e4ed529cdc705f5922d8ebb729937d071527ad9ab6c344d64692b7fbaecd1d
- clm_4bbde4198df54eeecaa506b36eb12fe55067cf54dd1d2ec341ff6a0719d6a4c6
- clm_7b8245e480822bc4ae9d4fc652bc2b841086b273f3d90b7e1fa5f30f647941fa
- clm_7cdd5a4850da1a3efc4f8bf070c33f1e887112232f85e0b308bdc4dd8bea61b0
- clm_85544aa3b9a575fa8c1e6060fdb73ac5af9e8c68ea8057afb51f8af5c28ee06e
maturity: draft
page_id: pg_55ad447229f951f1b6d0bee5f4f6fd1e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0531576aacba5fecab820aa20f4f8408
title: julien-c/synthtraces/README.md @ e5f8ec99d814
updated_at: '2026-09-14T04:01:21Z'
---

# julien-c/synthtraces/README.md @ e5f8ec99d814

<!-- rcw:begin owner=source:src_0531576aacba5fecab820aa20f4f8408 block=evidence -->
- The project is described as a minimal codebase that generates synthetic coding agent session traces using the Pi coding-agent package. [@claim:clm_03829bc430697e0d5f36a18217880cc4563cfef75e50068e789653eaa3e1d8ed]
- The README's final statistics section is a TODO, to be populated after generation with success rate, turn counts, and token counts. [@claim:clm_1b59d6e4bd9603dba68e8bbbb6dc79b31a21f21a7358b5af34374351160ef510]
- Local user models are GGUF quantizations (Q8_0) such as Qwen3.6-27B, Qwen3.6-35B-A3B-MTP, and gemma-4-26B-A4B-it, run via llama.cpp. [@claim:clm_1b65dde6f0c2c6e84dca08d7db333007d5e55cbd7922643f8d0004341ed4e84d]
- Each generated session pairs two models: a remotely hosted open model acting as the coding agent and a local llama.cpp model playing the user, within one of the project codebases. [@claim:clm_215efc569222f7db7773e6680b47fd2344eb32c11153f927502c9b9f4a5e521f]
- The generation matrix comprises 20 agent models, 3 local user models, 20 codebases, and 20 starting questions, totaling 24,000 sessions. [@claim:clm_28e4ed529cdc705f5922d8ebb729937d071527ad9ab6c344d64692b7fbaecd1d]
- The coding agent is equipped with the default Pi tools: read, write, edit, and bash. [@claim:clm_4bbde4198df54eeecaa506b36eb12fe55067cf54dd1d2ec341ff6a0719d6a4c6]
- The user model opens with one of the starting questions and drives the conversation with the agent over up to N turns, while the agent reads, edits, and runs against a locally cloned codebase. [@claim:clm_7b8245e480822bc4ae9d4fc652bc2b841086b273f3d90b7e1fa5f30f647941fa]
- The project is MIT-licensed, English-language, and links to a GitHub code repository and a Hugging Face dataset, both named julien-c/synthtraces. [@claim:clm_7cdd5a4850da1a3efc4f8bf070c33f1e887112232f85e0b308bdc4dd8bea61b0]
- The full exchange is recorded as a trace, and the dataset is the cartesian product of agent model, user model, codebase, and starting question. [@claim:clm_85544aa3b9a575fa8c1e6060fdb73ac5af9e8c68ea8057afb51f8af5c28ee06e]
<!-- rcw:end owner=source:src_0531576aacba5fecab820aa20f4f8408 block=evidence -->

## Researcher notes

