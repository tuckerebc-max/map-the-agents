# rasbt/mini-coding-agent -- full detail

[Back to orientation](mini-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rasbt/mini-coding-agent/717cae4ff10d01773bd12951f62a575825053414/c0f5070d67f9fc18.json](../../../wiki/dossiers/rasbt/mini-coding-agent/717cae4ff10d01773bd12951f62a575825053414/c0f5070d67f9fc18.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The agent is described as a minimal local agent loop with workspace snapshot collection, stable prompt plus turn state, structured tools, approval handling for risky tools, transcript/memory persistence, and bounded delegation. -- evidence: [README.md#L9-L9](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L9-L9), [README.md#L11-L16](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L11-L16) (`clm_f8ea165f584278848f9f35773a54b3472e225ec9744e83e901ba21db0ac05c52`)

## design-choices (3 claim(s))

- [observation/documented] The agent expects the model to emit either <tool>...</tool> or <final>...</final>, and notes that different Ollama models follow this format with varying reliability. -- evidence: [README.md#L249-L252](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L249-L252) (`clm_56e4693320ae84c265b10c911d1fea45dab3afadae2b1d26c11105af32706c54`)
- [observation/documented] The design uses a stable prompt prefix separate from the changing request, transcript, and memory, so repeated model calls can reuse the static parts efficiently. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49) (`clm_6663fa9faa9f4083a2224ae122fa963c4ea33a58b60b62e6b9bf853e89fa6f29`)
- [observation/documented] Context reduction is documented: long outputs are clipped, repeated reads deduplicated, and older transcript entries compressed to keep prompt size under control. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49) (`clm_326784a0ebc5d679e0629acafae72697ef90bb9550e90b5097077a953b1a60b6`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The agent exposes a CLI with flags including --cwd, --model, --host, --ollama-timeout, --resume, --approval, --max-steps, --max-new-tokens, --temperature, and --top-p, with documented defaults such as max-steps 6 and max-new-tokens 512. -- evidence: [README.md#L220-L239](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L220-L239) (`clm_f6fa002234ccbc7896e84ed805b9a8df43f39d9e2f9221f311222400b26dcb2a`)
- [observation/documented] Inside the REPL, slash commands (/help, /memory, /session, /reset, /exit, /quit) are handled directly by the agent rather than sent to the model as tasks. -- evidence: [README.md#L189-L200](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L189-L200), [README.md#L186-L187](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L186-L187) (`clm_ed2d7b9b91bca1964fdc43af4874d5202563401661bdbbeeedbc9efc632108bc`)
- [observation/documented] The agent sends prompts to Ollama's /api/generate endpoint, with the default model qwen3.5:4b and default host http://127.0.0.1:11434. -- evidence: [README.md#L220-L239](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L220-L239), [README.md#L95-L95](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L95-L95) (`clm_4c2088faaef40bf75f5660a906751e8a79bc67897ed462f4d59e39e80d6e6eca`)

## memory-state (2 claim(s))

- [observation/documented] Sessions are saved under the target workspace root in .mini-coding-agent/sessions/, and can be resumed by id or with --resume latest. -- evidence: [README.md#L165-L167](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L165-L167), [README.md#L178-L180](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L178-L180), [README.md#L163-L163](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L163-L163), [README.md#L169-L169](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L169-L169) (`clm_daca6bebab07369cdef9a988427dacb5a750e719e1e359a584e9afa6f16b087d`)
- [observation/documented] The runtime reportedly keeps both a full durable transcript and a smaller working memory so sessions can be resumed while preserving important state. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49) (`clm_a18453a4958068b4780700a050a1af38e63b4ab4e3f1cdbf40b878a80e4c67dd`)

## orchestration (1 claim(s))

- [observation/documented] Scoped subtasks can be delegated to helper subagents that inherit enough context to help while operating within limits. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49) (`clm_d3eb1c49bb8514ef4d0cb75bd387c09b98d48f33fcf2d1d33889fbf2f52d0099`)

## tools-permissions (1 claim(s))

- [observation/documented] Risky tools such as shell commands and file writes are gated by approval, with three modes: ask (default and recommended), auto (allows arbitrary command execution and file writes), and never (denies risky actions). -- evidence: [README.md#L143-L143](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L143-L143), [README.md#L145-L150](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L145-L150) (`clm_a2cd2b595a3453f90509e0f6f6ba5cd1afbf788479db5441163416cfebcceba6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project reportedly has no Python runtime dependency beyond the standard library, so it can be run directly with python mini_coding_agent.py without uv. -- evidence: [README.md#L64-L64](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L64-L64) (`clm_8670b85b9a413a33c74df2e862f51a78628b72bc029ed687d2cc897460a34c55`)
- [observation/documented] Running the agent requires Python 3.10+, an installed Ollama, and a locally pulled Ollama model; uv is optional for environment management and the CLI entry point. -- evidence: [README.md#L62-L62](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L62-L62), [README.md#L56-L58](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L56-L58) (`clm_ae6278a5318e315b260f75f7ea905d23224d5f589fbba1672a6266ea5fb3b98c`)

## limitations (1 claim(s))

- [observation/documented] The README states the agent is intentionally small and optimized for readability, not robustness. -- evidence: [README.md#L249-L252](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L249-L252) (`clm_1b7041bd0a7940d59fa5b8c68f46361f080cc1fcae8d3355da31370dd482790c`)

## relevance (1 claim(s))

- [observation/documented] EXAMPLE.md provides a hands-on walkthrough of using the agent with Ollama on a small Python project: implementing, editing, and testing a binary_search.py file via the REPL. -- evidence: [EXAMPLE.md#L8-L14](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/EXAMPLE.md#L8-L14), [EXAMPLE.md#L4-L4](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/EXAMPLE.md#L4-L4) (`clm_2a2f9d6bc7693821ac9e930ab64b3181a79d457dd459f6def35c2cfb8b41774f`)

