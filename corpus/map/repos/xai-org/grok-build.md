# xai-org/grok-build

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 37949780c144 @ 78b0646993cd1a4e

## Summary (orientation draft, not independently verified)

The snapshot is README/CONTRIBUTING/SECURITY documentation for Grok Build, a Rust terminal AI coding agent (CLI/TUI) by SpaceXAI, with no source code slices included. Claims below are limited to what these files state.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repo contains Rust source for the grok CLI/TUI and agent runtime, with crates for the TUI, agent runtime, tools, and workspace (filesystem, VCS, checkpoints). -- evidence: [README.md#L31-L32](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L31-L32), [README.md#L97-L106](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L97-L106)
- design-choices (1 claim(s)):
  - [observation/documented] The repository is periodically synced from the SpaceXAI monorepo, with a SOURCE_REV file recording the full monorepo commit SHA. -- evidence: [README.md#L31-L32](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L31-L32), [README.md#L34-L35](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L34-L35)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: per-crate cargo check/test/clippy and cargo fmt are the documented build, test, and lint commands; clippy.toml and rustfmt.toml sit at the repo root. -- evidence: [README.md#L115-L120](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L115-L120)
  - [observation/documented] Repository development practice: external pull requests and unsolicited patches are not accepted; the public tree exists for transparency and local builds under Apache 2.0. -- evidence: [CONTRIBUTING.md#L6-L8](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/CONTRIBUTING.md#L6-L8), [CONTRIBUTING.md#L3-L4](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/CONTRIBUTING.md#L3-L4)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Grok Build runs as a full-screen terminal TUI that can edit files, execute shell commands, search the web, and manage long-running tasks. -- evidence: [README.md#L13-L17](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L13-L17)
  - [observation/documented] The agent can run interactively, headlessly for scripting/CI, or embedded in editors via the Agent Client Protocol (ACP). -- evidence: [README.md#L13-L17](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L13-L17)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Building from source requires a Rust toolchain pinned by rust-toolchain.toml and DotSlash so hermetic tools like bin/protoc can run. -- evidence: [README.md#L58-L62](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L58-L62)
  - [observation/documented] Third-party notices indicate in-tree source ports of openai/codex and sst/opencode tool implementations, plus a vendored Mermaid diagram stack under third_party/. -- evidence: [README.md#L97-L106](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L97-L106), [README.md#L134-L140](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L134-L140)
- limitations (1 claim(s)):
  - [observation/documented] Windows builds of the project are described as best-effort and not currently tested from this tree; macOS and Linux are supported build hosts. -- evidence: [README.md#L70-L73](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L70-L73)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](grok-build.detail.md) for every claim.)

Metadata and full claim list: [full detail](grok-build.detail.md)
Human notes ([notes](grok-build.notes.md), never overwritten by build)

[Back to map index](../../index.md)
