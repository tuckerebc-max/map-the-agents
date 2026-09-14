# piqoni/vogte

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 37e9ab501aa7 @ 40c3abfc06915167

## Summary (orientation draft, not independently verified)

Vogte is a Go-focused, LLM-powered terminal tool (TUI and CLI) that builds compressed AST-based repository context, applies patches in agent mode, and offers local PR review and context generation. Evidence is README-only, so most claims are documented rather than code-inspected.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vogte is described as an agentic terminal tool aimed at existing Go codebases, helping developers build and maintain Go projects with LLMs. -- evidence: [README.md#L1-L9](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L1-L9), [README.md#L15-L19](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L15-L19)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Because the language is assumed to be Go, the tool parses repositories with Abstract Syntax Trees to extract compressed, relevant context for LLM prompts, aiming for near-zero configuration. -- evidence: [README.md#L15-L19](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L15-L19)
- workflows (1 claim(s)):
  - [observation/documented] Installation is via 'go install github.com/piqoni/vogte@latest'; the TUI exits via Ctrl+C or typing q, quite, or exit. -- evidence: [README.md#L49-L49](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L49-L49), [README.md#L41-L43](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L41-L43)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The tool offers a TUI with ask/agent modes and CLI flags including -review, -generate-context, -agent, -config, -dir, and -model. -- evidence: [README.md#L51-L61](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L51-L61), [README.md#L29-L31](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L29-L31), [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27), [README.md#L63-L69](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L63-L69)
  - [observation/documented] Running 'vogte -generate-context' writes a vogte-context.txt file in the current directory, and -dir lets users analyze a project in another directory. -- evidence: [README.md#L78-L79](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L78-L79), [README.md#L81-L81](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L81-L81), [README.md#L63-L69](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L63-L69), [README.md#L74-L76](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L74-L76)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] It uses a two-step flow: first it extracts structs/interfaces/methods signatures and asks the LLM which files are needed, then supplies those files in full so the LLM can produce a solution. -- evidence: [README.md#L38-L38](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L38-L38)
- tools-permissions (1 claim(s)):
  - [observation/documented] In agent mode (via -agent or the AGENT toggle) the tool edits files without user approval, and users are advised to rely on version control to avoid losing work. -- evidence: [README.md#L71-L71](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L71-L71)
- evaluation (1 claim(s)):
  - [observation/documented] After applying patches, the tool runs a 'Sanity Check' (currently 'go vet ./...') and shows a project-health indicator for instant feedback. -- evidence: [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27)
- dependencies (1 claim(s)):
  - [observation/documented] It works with OpenAI-compatible APIs (tested with GPT-4 and Claude Sonnet), supports AWS Bedrock for Anthropic models, and uses OPENAI_API_KEY or ANTHROPIC_API_KEY environment variables. -- evidence: [README.md#L46-L47](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L46-L47), [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27)
- limitations (2 claim(s)):
  - [observation/documented] Each message is treated as a new, unrelated chat, and there is no agentic retry loop on failure, at least for now. -- evidence: [README.md#L34-L35](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L34-L35)
More evidence: [full detail](vogte.detail.md)

Metadata and full claim list: [full detail](vogte.detail.md)
Human notes ([notes](vogte.notes.md), never overwritten by build)

[Back to map index](../../index.md)
