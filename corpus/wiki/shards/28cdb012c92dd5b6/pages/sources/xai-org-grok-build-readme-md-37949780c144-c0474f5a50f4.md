---
access: public
aliases: []
claim_ids:
- clm_03233ce2afee4b086aee14b66554b2e553394ef4bafdb6866179056f22afbbb7
- clm_0d949c7c81fa853fd90900567996a059eaa3712bf1253b0d9ea78955fc67042d
- clm_28bc28297f9e61b03eca1e73dc4ed9bd1bc73cf082bafaa099cc32669816fc18
- clm_6179ddee55b5672cb65474f5e6b4344705d74e621a5ecf91d875bf23c90675c9
- clm_8dd4d24ebb08df51505872ed9d207ba4315bd1281035babda6f735266b9b232e
- clm_b10d053ad46e68b0966a9cb4e47e5105824628f9f06660764d87482cd8b2323d
- clm_dad7feef462f57480a32a7119937d7a5b60cfc4038dc3a74efeaa35607f82ea5
- clm_e763dc42fcec493521723695da5a87096392782b654b9c229f3e73eb56a4d2ba
- clm_ec03aaed84c67c35bd51b479b0a242f82fbf0be9e43eed559f5906636b766d1b
- clm_f043b536a806d0a27e93f8454399ebf157d50c0a70744fa116f647a65324721f
maturity: draft
page_id: pg_737db92ccfb950968499c0474f5a50f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_26b0312db21c5d4ea9381c6f6834725c
title: xai-org/grok-build/README.md @ 37949780c144
updated_at: '2026-09-14T03:23:45Z'
---

# xai-org/grok-build/README.md @ 37949780c144

<!-- rcw:begin owner=source:src_26b0312db21c5d4ea9381c6f6834725c block=evidence -->
- Grok Build runs as a full-screen terminal TUI that can edit files, execute shell commands, search the web, and manage long-running tasks. [@claim:clm_03233ce2afee4b086aee14b66554b2e553394ef4bafdb6866179056f22afbbb7]
- The repository is periodically synced from the SpaceXAI monorepo, with a SOURCE_REV file recording the full monorepo commit SHA. [@claim:clm_0d949c7c81fa853fd90900567996a059eaa3712bf1253b0d9ea78955fc67042d]
- Repository development practice: per-crate cargo check/test/clippy and cargo fmt are the documented build, test, and lint commands; clippy.toml and rustfmt.toml sit at the repo root. [@claim:clm_28bc28297f9e61b03eca1e73dc4ed9bd1bc73cf082bafaa099cc32669816fc18]
- Windows builds of the project are described as best-effort and not currently tested from this tree; macOS and Linux are supported build hosts. [@claim:clm_6179ddee55b5672cb65474f5e6b4344705d74e621a5ecf91d875bf23c90675c9]
- Third-party notices indicate in-tree source ports of openai/codex and sst/opencode tool implementations, plus a vendored Mermaid diagram stack under third_party/. [@claim:clm_8dd4d24ebb08df51505872ed9d207ba4315bd1281035babda6f735266b9b232e]
- The agent can run interactively, headlessly for scripting/CI, or embedded in editors via the Agent Client Protocol (ACP). [@claim:clm_b10d053ad46e68b0966a9cb4e47e5105824628f9f06660764d87482cd8b2323d]
- Repository development practice: the root Cargo.toml is generated and should be treated as read-only; contributors should edit per-crate Cargo.toml files instead. [@claim:clm_dad7feef462f57480a32a7119937d7a5b60cfc4038dc3a74efeaa35607f82ea5]
- Building from source requires a Rust toolchain pinned by rust-toolchain.toml and DotSlash so hermetic tools like bin/protoc can run. [@claim:clm_e763dc42fcec493521723695da5a87096392782b654b9c229f3e73eb56a4d2ba]
- The repo contains Rust source for the grok CLI/TUI and agent runtime, with crates for the TUI, agent runtime, tools, and workspace (filesystem, VCS, checkpoints). [@claim:clm_ec03aaed84c67c35bd51b479b0a242f82fbf0be9e43eed559f5906636b766d1b]
- Prebuilt binaries are published for macOS, Linux, and Windows via install scripts, and the binary authenticates by opening a browser on first launch. [@claim:clm_f043b536a806d0a27e93f8454399ebf157d50c0a70744fa116f647a65324721f]
<!-- rcw:end owner=source:src_26b0312db21c5d4ea9381c6f6834725c block=evidence -->

## Researcher notes

