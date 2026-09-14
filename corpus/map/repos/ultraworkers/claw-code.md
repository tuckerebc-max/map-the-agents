# ultraworkers/claw-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 08106b0c3771 @ 3672b0345a23b5ad

## Summary (orientation draft, not independently verified)

The repository documents Claw Code, a Rust implementation of the `claw` CLI agent harness with a full CLI, a lean `claw-analog` agent, and a separate RAG service; evidence is mostly README/concept/how-to-run documentation describing product surface, permissions, sessions, and setup workflows. Evidence coverage: 137 of 276 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 39 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The Rust workspace contains the main `claw` CLI (rusty-claude-cli), an `api` crate for provider clients and streaming, a `runtime` crate with sessions and permission policy/enforcer, a `tools` crate, `claw-analog`, and `claw-rag-service`. -- evidence: [concept.md#L74-L80](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L74-L80)
  - [observation/documented] claw-rag-service is a separate process that indexes a repository into SQLite chunks plus embeddings and exposes an HTTP API with routes including /, /health, /v1/stats, and /v1/query, plus a minimal web UI. -- evidence: [concept.md#L13-L15](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L13-L15), [concept.md#L74-L80](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L74-L80)
- design-choices (1 claim(s)):
  - [observation/documented] Heavy indexing and embedding storage are deliberately kept out of claw-analog; the agent only calls retrieval over HTTP so the vector store and embedding secrets can be scaled or changed independently. -- evidence: [concept.md#L57-L57](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L57-L57)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README instructs building from source via `cargo build --workspace` in rust/, warns against `cargo install claw-code` (a deprecated stub), and says to run `cargo test --workspace` after verifying the binary. -- evidence: [README.md#L263-L263](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L263-L263), [README.md#L125-L127](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L125-L127), [README.md#L115-L121](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L115-L121), [README.md#L265-L268](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L265-L268)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The main `claw` CLI is described as a full agent with a REPL, OAuth, an extended toolset including bash, MCP and plugins, streaming, and integration with Anthropic, OpenAI-compatible, and xAI providers. -- evidence: [concept.md#L13-L15](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L13-L15)
  - [observation/documented] claw-analog is a lean agent on the same API layer with a narrow filesystem-only toolset (read_file, list_dir, glob_workspace, grep_workspace, git_diff, git_log, optional write_file and retrieve_context) and no arbitrary shell, MCP, or plugins. -- evidence: [concept.md#L13-L15](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L13-L15), [how_to_run.md#L180-L190](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L180-L190), [concept.md#L92-L92](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L92-L92), [concept.md#L90-L90](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L90-L90)
- memory-state (1 claim(s)):
  - [observation/documented] claw-analog supports JSON session files (version 1) holding workspace, model, optional preset, and API-format messages; history is loaded on resume and saved after each tool round, with a --save-session export path and warnings about secrets and token cost. -- evidence: [how_to_run.md#L158-L158](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L158-L158), [how_to_run.md#L160-L160](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L160-L160), [how_to_run.md#L162-L162](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L162-L162)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
More evidence: [full detail](claw-code.detail.md)

Metadata and full claim list: [full detail](claw-code.detail.md)
Human notes ([notes](claw-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
