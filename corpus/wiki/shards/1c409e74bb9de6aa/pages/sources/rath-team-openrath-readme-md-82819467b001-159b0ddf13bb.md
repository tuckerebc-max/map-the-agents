---
access: public
aliases: []
claim_ids:
- clm_08718dcc1fef5a641dca9dda41c0404fbe8391f1f35a2f5867e70d534f375033
- clm_112583f5488ba75ac71dfdff75a6004fbb69b0176ae060e156d58c592f860d16
- clm_1852125020a00c78d41062e27ac626a7968f037f65ea2b915751bc1190436146
- clm_2a950178b278ee9d18014302a270ca3c6d4b51880d7d4a6088e9066b3efd07f7
- clm_3026dac26635880504341eefcd0002bf4313ac5a9108b68e5c4a278a5c5dc412
- clm_31844418c3a3884a082d24b4c0f1d764099194d7490a33c3b4e96ca73ef41422
- clm_3e95c12ebf221e044c86c9e88c869045b330a658c505877b799cb53e830883f1
- clm_49417797f1e066ab07af0988d4b1eae418d4468cad7a05388f58a570e0a198b4
- clm_4c98292f853f8b96fc40a1eab42ed11bdd2a74a143a3e6475b35b8c1c0bb50be
- clm_a7ce7641325d7e898a88e7ce3727c8d0058aead33d66d77ac684ce34d486ef6a
- clm_aa38937715b490a22fcdeaf2587b1bd5715f19976b50cb48cf360a275894066c
- clm_bc51bb8c513d4cb9cf1120639ce7323b7cf3d265a68b8d419d4de3e721849bf6
- clm_d01fec61cdeb3004392391a2f7f7613a4271fecb15a19289a9f7d4b885aeabcc
- clm_e6db68cdcf5b34a58d1f53f3a04071a9c48a45f1162deccfc420c66a24a997b0
maturity: draft
page_id: pg_2808587dd0d4532db7b6159b0ddf13bb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4347e70250ca59d3a74f138eeee67b26
title: Rath-Team/OpenRath/README.md @ 82819467b001
updated_at: '2026-09-14T02:35:21Z'
---

# Rath-Team/OpenRath/README.md @ 82819467b001

<!-- rcw:begin owner=source:src_4347e70250ca59d3a74f138eeee67b26 block=evidence -->
- OpenRath exposes core runtime objects: Session (conversation state and inter-agent lineage), Sandbox (tool execution placement), Memory, Tool, Agent, Workflow, and Selector. [@claim:clm_08718dcc1fef5a641dca9dda41c0404fbe8391f1f35a2f5867e70d534f375033]
- OpenRath is Session-first rather than agent-loop-first, so multi-agent, multi-branch, durable-memory, sandboxed, and lineage-traced workloads share one flowing value. [@claim:clm_112583f5488ba75ac71dfdff75a6004fbb69b0176ae060e156d58c592f860d16]
- flow.Workflow subclasses implement forward(session) -> Session, enabling nesting of agents, forks, compression, tools, and child workflows without a new state format per layer. [@claim:clm_1852125020a00c78d41062e27ac626a7968f037f65ea2b915751bc1190436146]
- The production data plane uses PostgreSQL as source of truth, Redis for signaling acceleration, and S3-compatible artifact storage; the server/postgres extra installs via pip with openrath-migrate for schema migration. [@claim:clm_2a950178b278ee9d18014302a270ca3c6d4b51880d7d4a6088e9066b3efd07f7]
- The Agent Server HTTP surface is explicitly labeled Beta, and v1 JSONL imports are historical records rather than resumable active Runs. [@claim:clm_3026dac26635880504341eefcd0002bf4313ac5a9108b68e5c4a278a5c5dc412]
- The base install ships a zero-dependency local memory backend storing data under .openrath/memory/ with lexical BM25 recall, optional embeddings, and OpenViking as an optional external backend. [@claim:clm_31844418c3a3884a082d24b4c0f1d764099194d7490a33c3b4e96ca73ef41422]
- v2.0.0 adds a durable production layer: @step/@router boundaries compile to immutable plans; Runs, Events, and Checkpoints survive process and worker restarts, with leases, fencing, retries, and resumable queues. [@claim:clm_3e95c12ebf221e044c86c9e88c869045b330a658c505877b799cb53e830883f1]
- flow.Selector is an LLM-backed router over self-describing workflows that returns the next workflow or a no-op EmptyWorkflow, keeping if/while control flow in plain Python. [@claim:clm_49417797f1e066ab07af0988d4b1eae418d4468cad7a05388f58a570e0a198b4]
- FlowToolCall is the model-visible tool abstraction combining name, description, JSON schema, and a Python call over a Session; BackendTool* is the lower-level payload consumed by sandbox backends. [@claim:clm_4c98292f853f8b96fc40a1eab42ed11bdd2a74a143a3e6475b35b8c1c0bb50be]
- The framework maps PyTorch concepts to agent concepts: Session as Tensor, Sandbox/Backend as Device, Memory as Parameter, Tool as Function, Agent as nn.Linear, Workflow as nn.Module, Selector as control flow. [@claim:clm_a7ce7641325d7e898a88e7ce3727c8d0058aead33d66d77ac684ce34d486ef6a]
- The local sandbox backend is always available and runs file, command, and code tools against the host workspace; an optional opensandbox backend connects the same tool layer to a containerized runtime, and sessions retain sandbox ownership across tool calls. [@claim:clm_aa38937715b490a22fcdeaf2587b1bd5715f19976b50cb48cf360a275894066c]
- Agent Server tokens carry explicit action grants, object access is tenant/project scoped, runtime identities need no DDL privileges, and an Effect Ledger stops ambiguous non-idempotent effects in NEEDS_REVIEW rather than replaying them. [@claim:clm_bc51bb8c513d4cb9cf1120639ce7323b7cf3d265a68b8d419d4de3e721849bf6]
- Session supports fork(), detach(), merge(...), JSONL serialization, sandbox binding via session.to("local", spec="./"), plus from_user_message and from_agent_prompt constructors. [@claim:clm_d01fec61cdeb3004392391a2f7f7613a4271fecb15a19289a9f7d4b885aeabcc]
- Agent memory APIs include memory= binding at construction, remember_memory, recall_memory, commit_memory, and commit_on_forward=True for automatic commits. [@claim:clm_e6db68cdcf5b34a58d1f53f3a04071a9c48a45f1162deccfc420c66a24a997b0]
<!-- rcw:end owner=source:src_4347e70250ca59d3a74f138eeee67b26 block=evidence -->

## Researcher notes

