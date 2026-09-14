# ochyai/vibe-local

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5ea328e201c1 @ e19e0d0faae6df51

## Summary (orientation draft, not independently verified)

vibe-local is a free, offline AI coding environment for Mac combining Ollama local LLMs with the OpenCode TUI (plus an optional built-in Python engine), aimed at non-profit education use. Evidence covers its architecture, CLI/TUI interfaces, permission model, RAG/session state, dependencies, and documented safety limitations. Evidence coverage: 180 of 193 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The v2 launcher detects RAM, selects a model, creates num_ctx-baked Ollama aliases (vibe-coder/vibe-fast) via ollama create, and generates OpenCode config without modifying the user's own OpenCode settings. -- evidence: [README.md#L421-L433](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L421-L433), [README.md#L545-L549](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L545-L549)
  - [observation/documented] An optional built-in Python engine, vibe-coder.py, is dependency-free (stdlib only), talks directly to Ollama's /api/chat with a tool-execution loop, and can run standalone via python3. -- evidence: [RELEASE_NOTES.md#L62-L69](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L62-L69), [README.md#L441-L443](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L441-L443), [README.md#L454-L455](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L454-L455)
- design-choices (2 claim(s)):
  - [observation/documented] v2 dropped the custom Anthropic-to-Ollama conversion proxy because Ollama natively implements the Anthropic Messages API (v0.14+); the old proxy and MLX server were archived under legacy/. -- evidence: [README.md#L435-L437](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L435-L437), [README.md#L44-L49](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L44-L49)
  - [observation/documented] The TUI uses a VT100 DECSTBM scroll region so AI output scrolls above a fixed three-row footer, with a store-only update pattern, non-blocking resize locking, and single-syscall atomic writes. -- evidence: [RELEASE_NOTES.md#L22-L26](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L22-L26), [RELEASE_NOTES.md#L9-L9](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L9-L9), [RELEASE_NOTES.md#L96-L99](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L96-L99)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: release notes report 780 unit tests plus 7 PTY integration tests (787 total) for vibe-coder.py, stated to pass on macOS, Linux, and Windows WSL. -- evidence: [RELEASE_NOTES.md#L62-L69](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L62-L69), [RELEASE_NOTES.md#L102-L105](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L102-L105)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Inside the TUI, /theme switches themes, Tab toggles Plan/Build mode, and /models (or --no-router) pins a specific model instead of the default vibe-auto routing. -- evidence: [README.md#L375-L375](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L375-L375), [README.md#L276-L276](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L276-L276), [README.md#L112-L112](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L112-L112), [README.md#L114-L116](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L114-L116)
- memory-state (2 claim(s)):
  - [observation/documented] vibe-coder.py supports local RAG using sqlite3 and Ollama embeddings to inject relevant codebase context into the system prompt, with the index stored in .vibe/rag/ and tunable top-k and embedding model. -- evidence: [README.md#L445-L452](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L445-L452)
  - [observation/documented] Sessions are persisted as JSONL with resume support via --resume and --session-id, plus context compaction, per the implementation status table. -- evidence: [ROADMAP.md#L17-L45](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/ROADMAP.md#L17-L45)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
More evidence: [full detail](vibe-local.detail.md)

Metadata and full claim list: [full detail](vibe-local.detail.md)
Human notes ([notes](vibe-local.notes.md), never overwritten by build)

[Back to map index](../../index.md)
