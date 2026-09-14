---
access: public
aliases: []
claim_ids:
- clm_1b7041bd0a7940d59fa5b8c68f46361f080cc1fcae8d3355da31370dd482790c
- clm_326784a0ebc5d679e0629acafae72697ef90bb9550e90b5097077a953b1a60b6
- clm_4c2088faaef40bf75f5660a906751e8a79bc67897ed462f4d59e39e80d6e6eca
- clm_56e4693320ae84c265b10c911d1fea45dab3afadae2b1d26c11105af32706c54
- clm_6663fa9faa9f4083a2224ae122fa963c4ea33a58b60b62e6b9bf853e89fa6f29
- clm_8670b85b9a413a33c74df2e862f51a78628b72bc029ed687d2cc897460a34c55
- clm_a18453a4958068b4780700a050a1af38e63b4ab4e3f1cdbf40b878a80e4c67dd
- clm_a2cd2b595a3453f90509e0f6f6ba5cd1afbf788479db5441163416cfebcceba6
- clm_ae6278a5318e315b260f75f7ea905d23224d5f589fbba1672a6266ea5fb3b98c
- clm_d3eb1c49bb8514ef4d0cb75bd387c09b98d48f33fcf2d1d33889fbf2f52d0099
- clm_daca6bebab07369cdef9a988427dacb5a750e719e1e359a584e9afa6f16b087d
- clm_ed2d7b9b91bca1964fdc43af4874d5202563401661bdbbeeedbc9efc632108bc
- clm_f6fa002234ccbc7896e84ed805b9a8df43f39d9e2f9221f311222400b26dcb2a
- clm_f8ea165f584278848f9f35773a54b3472e225ec9744e83e901ba21db0ac05c52
maturity: draft
page_id: pg_4e2e39b67409515a856f8605cb806d84
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eef80e8cb408515aaf6803e560785838
title: rasbt/mini-coding-agent/README.md @ 717cae4ff10d
updated_at: '2026-09-14T02:35:19Z'
---

# rasbt/mini-coding-agent/README.md @ 717cae4ff10d

<!-- rcw:begin owner=source:src_eef80e8cb408515aaf6803e560785838 block=evidence -->
- The README states the agent is intentionally small and optimized for readability, not robustness. [@claim:clm_1b7041bd0a7940d59fa5b8c68f46361f080cc1fcae8d3355da31370dd482790c]
- Context reduction is documented: long outputs are clipped, repeated reads deduplicated, and older transcript entries compressed to keep prompt size under control. [@claim:clm_326784a0ebc5d679e0629acafae72697ef90bb9550e90b5097077a953b1a60b6]
- The agent sends prompts to Ollama's /api/generate endpoint, with the default model qwen3.5:4b and default host http://127.0.0.1:11434. [@claim:clm_4c2088faaef40bf75f5660a906751e8a79bc67897ed462f4d59e39e80d6e6eca]
- The agent expects the model to emit either <tool>...</tool> or <final>...</final>, and notes that different Ollama models follow this format with varying reliability. [@claim:clm_56e4693320ae84c265b10c911d1fea45dab3afadae2b1d26c11105af32706c54]
- The design uses a stable prompt prefix separate from the changing request, transcript, and memory, so repeated model calls can reuse the static parts efficiently. [@claim:clm_6663fa9faa9f4083a2224ae122fa963c4ea33a58b60b62e6b9bf853e89fa6f29]
- The project reportedly has no Python runtime dependency beyond the standard library, so it can be run directly with python mini_coding_agent.py without uv. [@claim:clm_8670b85b9a413a33c74df2e862f51a78628b72bc029ed687d2cc897460a34c55]
- The runtime reportedly keeps both a full durable transcript and a smaller working memory so sessions can be resumed while preserving important state. [@claim:clm_a18453a4958068b4780700a050a1af38e63b4ab4e3f1cdbf40b878a80e4c67dd]
- Risky tools such as shell commands and file writes are gated by approval, with three modes: ask (default and recommended), auto (allows arbitrary command execution and file writes), and never (denies risky actions). [@claim:clm_a2cd2b595a3453f90509e0f6f6ba5cd1afbf788479db5441163416cfebcceba6]
- Running the agent requires Python 3.10+, an installed Ollama, and a locally pulled Ollama model; uv is optional for environment management and the CLI entry point. [@claim:clm_ae6278a5318e315b260f75f7ea905d23224d5f589fbba1672a6266ea5fb3b98c]
- Scoped subtasks can be delegated to helper subagents that inherit enough context to help while operating within limits. [@claim:clm_d3eb1c49bb8514ef4d0cb75bd387c09b98d48f33fcf2d1d33889fbf2f52d0099]
- Sessions are saved under the target workspace root in .mini-coding-agent/sessions/, and can be resumed by id or with --resume latest. [@claim:clm_daca6bebab07369cdef9a988427dacb5a750e719e1e359a584e9afa6f16b087d]
- Inside the REPL, slash commands (/help, /memory, /session, /reset, /exit, /quit) are handled directly by the agent rather than sent to the model as tasks. [@claim:clm_ed2d7b9b91bca1964fdc43af4874d5202563401661bdbbeeedbc9efc632108bc]
- The agent exposes a CLI with flags including --cwd, --model, --host, --ollama-timeout, --resume, --approval, --max-steps, --max-new-tokens, --temperature, and --top-p, with documented defaults such as max-steps 6 and max-new-tokens 512. [@claim:clm_f6fa002234ccbc7896e84ed805b9a8df43f39d9e2f9221f311222400b26dcb2a]
- The agent is described as a minimal local agent loop with workspace snapshot collection, stable prompt plus turn state, structured tools, approval handling for risky tools, transcript/memory persistence, and bounded delegation. [@claim:clm_f8ea165f584278848f9f35773a54b3472e225ec9744e83e901ba21db0ac05c52]
<!-- rcw:end owner=source:src_eef80e8cb408515aaf6803e560785838 block=evidence -->

## Researcher notes

