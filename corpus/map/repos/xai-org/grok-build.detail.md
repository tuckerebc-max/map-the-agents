# xai-org/grok-build -- full detail

[Back to orientation](grok-build.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xai-org/grok-build/37949780c144e37df692e3d669051a21fec24f20/78b0646993cd1a4e.json](../../../wiki/dossiers/xai-org/grok-build/37949780c144e37df692e3d669051a21fec24f20/78b0646993cd1a4e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repo contains Rust source for the grok CLI/TUI and agent runtime, with crates for the TUI, agent runtime, tools, and workspace (filesystem, VCS, checkpoints). -- evidence: [README.md#L31-L32](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L31-L32), [README.md#L97-L106](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L97-L106) (`clm_ec03aaed84c67c35bd51b479b0a242f82fbf0be9e43eed559f5906636b766d1b`)

## design-choices (1 claim(s))

- [observation/documented] The repository is periodically synced from the SpaceXAI monorepo, with a SOURCE_REV file recording the full monorepo commit SHA. -- evidence: [README.md#L31-L32](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L31-L32), [README.md#L34-L35](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L34-L35) (`clm_0d949c7c81fa853fd90900567996a059eaa3712bf1253b0d9ea78955fc67042d`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: per-crate cargo check/test/clippy and cargo fmt are the documented build, test, and lint commands; clippy.toml and rustfmt.toml sit at the repo root. -- evidence: [README.md#L115-L120](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L115-L120) (`clm_28bc28297f9e61b03eca1e73dc4ed9bd1bc73cf082bafaa099cc32669816fc18`)
- [observation/documented] Repository development practice: external pull requests and unsolicited patches are not accepted; the public tree exists for transparency and local builds under Apache 2.0. -- evidence: [CONTRIBUTING.md#L6-L8](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/CONTRIBUTING.md#L6-L8), [CONTRIBUTING.md#L3-L4](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/CONTRIBUTING.md#L3-L4) (`clm_a50abf636087a4f8f677e787100648d8b0107823a0bfd1e5e956f63b03280dc0`)
- [observation/documented] Repository development practice: the root Cargo.toml is generated and should be treated as read-only; contributors should edit per-crate Cargo.toml files instead. -- evidence: [README.md#L108-L111](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L108-L111) (`clm_dad7feef462f57480a32a7119937d7a5b60cfc4038dc3a74efeaa35607f82ea5`)
- [observation/documented] Repository development practice: security vulnerabilities must be reported via the HackerOne program at hackerone.com/x, not through public GitHub issues. -- evidence: [SECURITY.md#L3-L3](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/SECURITY.md#L3-L3), [SECURITY.md#L7-L7](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/SECURITY.md#L7-L7), [SECURITY.md#L5-L5](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/SECURITY.md#L5-L5) (`clm_7ca8c483a7aa7638a7fbf1cfe28d7ba52eb947d75e0bca822df4c597d3812969`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Grok Build runs as a full-screen terminal TUI that can edit files, execute shell commands, search the web, and manage long-running tasks. -- evidence: [README.md#L13-L17](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L13-L17) (`clm_03233ce2afee4b086aee14b66554b2e553394ef4bafdb6866179056f22afbbb7`)
- [observation/documented] The agent can run interactively, headlessly for scripting/CI, or embedded in editors via the Agent Client Protocol (ACP). -- evidence: [README.md#L13-L17](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L13-L17) (`clm_b10d053ad46e68b0966a9cb4e47e5105824628f9f06660764d87482cd8b2323d`)
- [observation/documented] Prebuilt binaries are published for macOS, Linux, and Windows via install scripts, and the binary authenticates by opening a browser on first launch. -- evidence: [README.md#L43-L43](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L43-L43), [README.md#L81-L83](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L81-L83), [README.md#L45-L49](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L45-L49) (`clm_f043b536a806d0a27e93f8454399ebf157d50c0a70744fa116f647a65324721f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Building from source requires a Rust toolchain pinned by rust-toolchain.toml and DotSlash so hermetic tools like bin/protoc can run. -- evidence: [README.md#L58-L62](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L58-L62) (`clm_e763dc42fcec493521723695da5a87096392782b654b9c229f3e73eb56a4d2ba`)
- [observation/documented] Third-party notices indicate in-tree source ports of openai/codex and sst/opencode tool implementations, plus a vendored Mermaid diagram stack under third_party/. -- evidence: [README.md#L97-L106](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L97-L106), [README.md#L134-L140](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L134-L140) (`clm_8dd4d24ebb08df51505872ed9d207ba4315bd1281035babda6f735266b9b232e`)

## limitations (1 claim(s))

- [observation/documented] Windows builds of the project are described as best-effort and not currently tested from this tree; macOS and Linux are supported build hosts. -- evidence: [README.md#L70-L73](https://github.com/xai-org/grok-build/blob/37949780c144e37df692e3d669051a21fec24f20/README.md#L70-L73) (`clm_6179ddee55b5672cb65474f5e6b4344705d74e621a5ecf91d875bf23c90675c9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

