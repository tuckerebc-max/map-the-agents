# esengine/deepseek-reasonix

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8679e1f0b614 @ 1fb4383a9229e205

## Summary (orientation draft, not independently verified)

Selected evidence records: Reasonix implements Agent Client Protocol v1 as an NDJSON JSON-RPC 2.0 agent over stdin/stdout, launched via `reasonix acp`, with diagnostics sent to stderr. ACP exposes session lifecycle methods including session/new, load, resume, prompt, cancel, list, close, and delete, each session owning an isolated controller, workspace root, model, and transcript.

## Source coverage

Source coverage (partial): 6 of 190 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product ships as a single CGO_ENABLED=0 static Go binary, cross-compilable to six targets (darwin/linux/windows × amd64/arm64) with one command. -- evidence: [README.md#L89-L90](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L89-L90), [README.md#L59-L72](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L59-L72)
- design-choices (2 claim(s)):
  - [observation/documented] Configuration is declared in reasonix.toml covering providers, the agent, enabled tools, and plugins, with no hardcoded models; DeepSeek ships as a preset and any OpenAI-compatible endpoint is a config entry. -- evidence: [README.md#L59-L72](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L59-L72)
  - [observation/documented] MCP servers contribute tools, prompts, and resources, and Extension Protocol v1 sidecars can intercept runtime events and contribute providers and structured UI. -- evidence: [README.md#L59-L72](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L59-L72)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: build from source with `make build` (bin/reasonix) and `make cross` (dist/), and build desktop packages via scripts/desktop-build.sh one platform per run. -- evidence: [README.md#L130-L133](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L130-L133), [README.md#L140-L142](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L140-L142)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] Reasonix implements Agent Client Protocol v1 as an NDJSON JSON-RPC 2.0 agent over stdin/stdout, launched via `reasonix acp`, with diagnostics sent to stderr. -- evidence: [docs/ACP.md#L36-L39](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L36-L39), [docs/ACP.md#L11-L14](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L11-L14), [docs/ACP.md#L26-L30](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L26-L30)
  - [observation/documented] ACP exposes session lifecycle methods including session/new, load, resume, prompt, cancel, list, close, and delete, each session owning an isolated controller, workspace root, model, and transcript. -- evidence: [docs/ACP.md#L117-L119](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L117-L119), [docs/ACP.md#L121-L130](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L121-L130)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Permission presets are read-only, workspace-write, and danger-full-access; tool-approval changes update the gate in place without rebuilding the session controller. -- evidence: [docs/ACP.md#L142-L147](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L142-L147), [docs/ACP.md#L169-L171](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L169-L171)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Building the CLI requires Go 1.26+ with a pinned toolchain directive; the desktop build additionally requires Node 24+ and pnpm 10 for the frontend and Electron shell. -- evidence: [README.md#L137-L138](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L137-L138), [README.md#L127-L128](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L127-L128)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](deepseek-reasonix.detail.md) for every claim.)

Metadata and full claim list: [full detail](deepseek-reasonix.detail.md)
Human notes ([notes](deepseek-reasonix.notes.md), never overwritten by build)

[Back to map index](../../index.md)
