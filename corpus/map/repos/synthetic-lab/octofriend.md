# synthetic-lab/octofriend

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6b2159fc9829 @ 00d502e0d3cc130a

## Summary (orientation draft, not independently verified)

Octo (octofriend) is a terminal coding assistant that works with OpenAI-compatible, Anthropic, and local LLM APIs, with Docker sandboxing, MCP/LSP integration, Agent Skills, session persistence, and a zero-telemetry stance. Evidence is documentation-based (README/CHANGELOG); no source code slices are present, so all claims are documented rather than code-inspected. Evidence coverage: 180 of 221 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Octo optionally uses two custom open-sourced Hugging Face models (diff-apply and fix-json) to automatically handle tool-call and code-edit failures from the main coding LLM. -- evidence: [README.md#L22-L31](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L22-L31)
  - [observation/documented] Octo auto-detects installed language servers (e.g. typescript-language-server, gopls, rust-analyzer) and exposes IDE-grade navigation tools with no configuration; custom LSP entries override built-ins, and LSP can be disabled entirely or per-server. -- evidence: [README.md#L321-L323](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L321-L323), [README.md#L316-L317](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L316-L317), [README.md#L292-L296](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L292-L296), [README.md#L298-L300](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L298-L300), [README.md#L325-L329](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L325-L329), [README.md#L286-L290](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L286-L290)
- design-choices (2 claim(s)):
  - [observation/documented] Octo claims zero telemetry and works with any OpenAI-compatible API, Anthropic, or locally run LLMs. -- evidence: [README.md#L1-L2](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L1-L2), [README.md#L33-L36](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L33-L36), [README.md#L22-L31](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L22-L31)
  - [observation/documented] Instruction files are discovered as OCTO.md, CLAUDE.md, or AGENTS.md; the first found wins, and rules from the current directory up through the home directory are merged, with a global file also possible in ~/.config/octofriend/OCTO.md. -- evidence: [README.md#L175-L177](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L175-L177), [README.md#L185-L186](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L185-L186), [README.md#L179-L183](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L179-L183), [README.md#L169-L169](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L169-L169), [README.md#L171-L173](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L171-L173)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the repo ships a CONTRIBUTING.md describing contribution guidelines, and canary.sh/canary.fish scripts that contributors source to build and run 'main' as 'canary-octo'. -- evidence: [README.md#L409-L410](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L409-L410), [CHANGELOG.md#L89-L89](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L89-L89), [CHANGELOG.md#L85-L87](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L85-L87)
- skills-patterns (1 claim(s)):
  - [observation/documented] Octo supports the Agent Skills spec (tagged Markdown with optional scripts), auto-detecting skills in ~/.config/agents/skills and per-repo .agents/skills, with extra paths configurable in the json5 config. -- evidence: [README.md#L242-L248](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L242-L248), [README.md#L239-L240](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L239-L240), [CHANGELOG.md#L135-L136](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L135-L136), [README.md#L233-L237](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L233-L237), [README.md#L190-L196](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L190-L196), [README.md#L231-L231](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L231-L231)
- interfaces (4 claim(s)):
  - [observation/documented] Octo is installed globally via npm as 'octofriend' and launched with either the 'octofriend' command or the short 'octo' alias. -- evidence: [README.md#L6-L8](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L6-L8), [README.md#L15-L16](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L15-L16), [CHANGELOG.md#L418-L418](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L418-L418), [README.md#L12-L13](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L12-L13)
  - [observation/documented] Sessions can be resumed with 'octo --resume <session-id>', listed via 'octo session list', or switched in-app through a Ctrl+p 'Load previous session' menu; Docker sessions can be resumed with new docker run args. -- evidence: [README.md#L76-L78](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L76-L78), [README.md#L91-L95](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L91-L95), [README.md#L80-L82](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L80-L82), [README.md#L101-L103](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L101-L103), [README.md#L87-L89](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L87-L89)
- memory-state (1 claim(s)):
  - [observation/documented] Conversations are automatically saved per-directory, and Octo replaced rolling history windows with autocompaction for long-context tasks to improve prompt cache hit rates. -- evidence: [README.md#L76-L78](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L76-L78), [CHANGELOG.md#L23-L25](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L23-L25), [CHANGELOG.md#L150-L152](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L150-L152)
- orchestration (2 claim(s)):
More evidence: [full detail](octofriend.detail.md)

Metadata and full claim list: [full detail](octofriend.detail.md)
Human notes ([notes](octofriend.notes.md), never overwritten by build)

[Back to map index](../../index.md)
