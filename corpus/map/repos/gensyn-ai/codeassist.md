# gensyn-ai/codeassist

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3bf99c623173 @ 0a81e310c0a13d4f

## Summary (orientation draft, not independently verified)

README-only snapshot of Gensyn's CodeAssist, a local AI coding assistant that learns from user keystrokes and trains a personal model via Docker-based episodes. Evidence covers product behavior, setup dependencies, training workflow, and contributor linting practices.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CodeAssist is described as a fully private, local AI coding assistant by Gensyn that helps users practice programming problems and train a personal assistant. -- evidence: [README.md#L6-L6](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L6-L6)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The assistant writes directly in the user's editor; every keystroke, edit, or deletion acts as a learning signal so it adapts to the user's habits over time. -- evidence: [README.md#L69-L69](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L69-L69), [README.md#L8-L8](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L8-L8)
- workflows (3 claim(s)):
  - [observation/documented] Training is triggered by pressing Ctrl+C in the terminal; the system compares user edits to assistant actions, computes rewards and penalties, updates a local checkpoint, and stores weights under persistent-data/trainer/models. -- evidence: [README.md#L83-L88](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L83-L88), [README.md#L79-L79](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L79-L79)
  - [observation/documented] Episodes need not solve the problem successfully; users can stop recording by leaving the web UI and starting training with ctrl+c, and the trained model uploads to Hugging Face if a valid token exists. -- evidence: [README.md#L81-L81](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L81-L81), [README.md#L83-L88](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L83-L88)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product runs a web UI on localhost:3000 with email one-time-passcode or Google login, and credentials are stored in persistent-data/auth/userKeyMap.json. -- evidence: [README.md#L63-L63](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L63-L63), [README.md#L65-L65](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L65-L65)
  - [observation/documented] Users select Easy, Medium, or Hard problems from a sidebar, and the assistant can be paused via Shift+Space or a Pause button, with a 'No-Op' signaling the user's turn. -- evidence: [README.md#L73-L75](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L73-L75), [README.md#L67-L67](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L67-L67)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The main script is run with 'uv run run.py', which handles the environment and launches the assistant; a --port argument can override the default port 3000. -- evidence: [README.md#L51-L51](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L51-L51), [README.md#L53-L55](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L53-L55), [README.md#L122-L125](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L122-L125), [README.md#L117-L120](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L117-L120)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [inference/documented] The product's improvement loop is user-driven: README guidance suggests improvement becomes clearer after roughly 4-5 training episodes, implying no automated benchmark harness is documented. -- evidence: [README.md#L94-L98](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L94-L98)
- dependencies (1 claim(s)):
  - [observation/documented] Running CodeAssist requires Docker, Python no older than 3.10, and UV for dependency management, plus a HuggingFace token with Write access. -- evidence: [README.md#L26-L26](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L26-L26), [README.md#L59-L59](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L59-L59), [README.md#L18-L18](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L18-L18), [README.md#L22-L22](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L22-L22)
- limitations (2 claim(s)):
More evidence: [full detail](codeassist.detail.md)

Metadata and full claim list: [full detail](codeassist.detail.md)
Human notes ([notes](codeassist.notes.md), never overwritten by build)

[Back to map index](../../index.md)
