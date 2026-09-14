# codehamr/codehamr

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8ad8eae6cc57 @ 3adff9ea9eb023a4

## Summary (orientation draft, not independently verified)

The snapshot is README-only documentation for codehamr, a minimal terminal coding agent for local LLMs and OpenAI-compatible endpoints, describing a single tool-calling loop, four tools, YAML model profiles, and several documented limitations. No code or contributor-workflow slices are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] codehamr is described as a minimal coding agent for the terminal, built for local LLMs and also able to run against OpenAI-compatible endpoints. -- evidence: [README.md#L3-L4](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L3-L4)
- components (1 claim(s)):
  - [observation/documented] The agent works with four tools — bash, read_file, write_file, and edit_file — investigating the project directly rather than guessing. -- evidence: [README.md#L18-L23](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L18-L23)
- design-choices (2 claim(s)):
  - [observation/documented] The design deliberately favors simplicity: three slash commands, one embedded system prompt, and no router, sub-agents, skill system, or MCP. -- evidence: [README.md#L15-L16](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L15-L16)
  - [observation/documented] Self-verification (running tests, compiling, loading the page) is instilled by the system prompt as a habit rather than a blocking gate; when a check cannot run, the agent reports 'unverified:' instead of pretending success. -- evidence: [README.md#L95-L95](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L95-L95), [README.md#L18-L23](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L18-L23)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The /models command lists configured model profiles, and /models <name> switches the active profile. -- evidence: [README.md#L81-L81](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L81-L81)
  - [observation/documented] On first run codehamr seeds .codehamr/config.yaml with a local profile (Ollama, vLLM, LM-Studio) and a hamrpass profile; the system prompt is embedded in the binary, not stored on disk. -- evidence: [README.md#L49-L52](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L49-L52)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The agent runs a single plain loop: it calls tools until the work is done, then replies, rather than using a more elaborate orchestration scheme. -- evidence: [README.md#L18-L23](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L18-L23)
- tools-permissions (1 claim(s)):
  - [observation/documented] The README warns that the agent runs model-generated shell commands with full filesystem access and recommends running it inside sandboxes such as devcontainers or isolated VMs. -- evidence: [README.md#L43-L43](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L43-L43)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Configuration supports OpenAI-compatible endpoints; the example config defines local, openai, and hamrpass profiles with llm and url fields, and the local and openai profiles also carry key and context_size fields. -- evidence: [README.md#L54-L55](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L54-L55), [README.md#L63-L79](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L63-L79)
More evidence: [full detail](codehamr.detail.md)

Metadata and full claim list: [full detail](codehamr.detail.md)
Human notes ([notes](codehamr.notes.md), never overwritten by build)

[Back to map index](../../index.md)
