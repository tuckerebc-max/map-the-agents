# can1357/oh-my-pi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9b2a43514bfc @ d28b45f95a242d11

## Summary (orientation draft, not independently verified)

README evidence for oh-my-pi (omp), a TypeScript/Bun coding agent forked from Pi, describing its CLI/SDK/RPC/ACP surfaces, built-in Rust-backed tools, provider routing, memory, subagents, and benchmark claims. Most claims are documentation-based; no source code slices are present. Evidence coverage: 146 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 135 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The native layer comprises six Rust crates (pi-natives, pi-shell, pi-ast, pi-iso, pi-voice, pi-walker) shipped as a platform-tagged N-API addon for six platforms. -- evidence: [README.md#L452-L453](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L452-L453), [README.md#L450-L450](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L450-L450)
  - [observation/documented] pi-shell is an embedded bash engine (~38k lines) with persistent sessions and in-process coreutils dispatch; pi-walker is a parallel ignore-aware walker shared by grep, glob, workspace, and shell. -- evidence: [README.md#L457-L464](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L457-L464)
- design-choices (3 claim(s)):
  - [observation/documented] omp links search, shell, AST, and other native implementations in-process to avoid fork/exec on the hot path, and the same binary targets macOS, Linux, and Windows without WSL. -- evidence: [README.md#L450-L450](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L450-L450), [README.md#L199-L199](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L199-L199)
  - [observation/documented] Edits use hashline patches anchored by content hashes; stale anchors cause the patch to be rejected before applying, and the README reports 61% fewer output tokens for Grok 4 Fast. -- evidence: [README.md#L207-L207](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L207-L207)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: pull requests are temporarily open to everyone as a trial; a prior vouch requirement is lifted while open contributions are evaluated, and it may return. -- evidence: [README.md#L29-L33](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L29-L33)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] omp offers four entry points sharing one engine: an interactive TUI, a one-shot prompt mode (omp -p), a Node SDK, and stdio-based RPC and ACP modes. -- evidence: [README.md#L496-L496](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L496-L496)
  - [observation/documented] The Node SDK package @oh-my-pi/pi-coding-agent exposes ModelRegistry, SessionManager, createAgentSession, and discoverAuthStorage, with typed session events. -- evidence: [README.md#L508-L508](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L508-L508), [README.md#L510-L510](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L510-L510)
- memory-state (1 claim(s)):
  - [observation/documented] Memory tools include retain, recall, reflect, memory_edit, and learn (which can promote lessons into managed skills), with a selectable memory.backend (local, Hindsight, or Mnemopi) that is project-scoped by default. -- evidence: [README.md#L215-L215](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L215-L215), [README.md#L300-L307](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L300-L307)
- orchestration (2 claim(s)):
  - [observation/documented] The task tool fans out subagents in parallel, optionally workspace-isolated, returning schema-validated results; an Agent Hub (Alt+A) shows live transcripts and lets users steer or kill workers. -- evidence: [README.md#L165-L165](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L165-L165), [README.md#L284-L287](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L284-L287), [README.md#L171-L171](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L171-L171)
More evidence: [full detail](oh-my-pi.detail.md)

Metadata and full claim list: [full detail](oh-my-pi.detail.md)
Human notes ([notes](oh-my-pi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
