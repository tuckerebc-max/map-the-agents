# aaif-goose/goose

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 50666ae0b9a5 @ 869b8f6fee4b256e

## Summary (orientation draft, not independently verified)

goose is a Rust-based general-purpose AI agent shipped as a desktop app, CLI, and API, with an ACP server for custom clients, MCP-based extensions, Docker packaging, and YAML recipes. Evidence: 6 of 16 candidate files stored (README.md, Docker/Linux build guides, custom-distro guide, GOVERNANCE.md, I18N.md); 10 omitted by file budget, including AGENTS.md, CONTRIBUTING.md and SECURITY.md; selection incomplete.

## Source coverage

Source coverage (partial): 6 of 16 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The architecture diagram shows user interfaces (CLI, Electron desktop, custom UIs) above a 'goose serve' ACP HTTP/WebSocket server, above a core goose crate containing providers, MCP extensions, and config/recipes. -- evidence: [CUSTOM_DISTROS.md#L18-L41](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L18-L41)
  - [observation/documented] The Docker image is a multi-stage Debian Bookworm Slim build of about 340MB containing a 32MB goose binary at /usr/local/bin/goose, optimized with LTO, stripping, and size optimization. -- evidence: [BUILDING_DOCKER.md#L47-L50](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L47-L50), [BUILDING_DOCKER.md#L212-L215](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L212-L215)
- design-choices (4 claim(s)):
  - [observation/documented] The project is built in Rust, which the README cites for performance and portability. -- evidence: [README.md#L25-L25](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L25-L25)
  - [observation/documented] The Docker image runs as a non-root 'goose' user (UID 1000) by default and includes git, curl, ca-certificates, and basic shell utilities. -- evidence: [BUILDING_DOCKER.md#L155-L155](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L155-L155), [BUILDING_DOCKER.md#L225-L229](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L225-L229), [BUILDING_DOCKER.md#L219-L221](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L219-L221)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: building the Linux desktop app requires Rust, Node.js 22.9.0+, pnpm 10+, and 'just'; the CLI is built with 'cargo build --release -p goose-cli --bin goose' and packaged via Electron Forge (ZIP recommended, plus DEB and Flatpak). -- evidence: [BUILDING_LINUX.md#L53-L56](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L53-L56), [BUILDING_LINUX.md#L171-L172](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L171-L172), [BUILDING_LINUX.md#L94-L97](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L94-L97), [BUILDING_LINUX.md#L70-L72](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L70-L72), [BUILDING_LINUX.md#L102-L105](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L102-L105)
  - [observation/documented] Repository development practice: BUILDING_LINUX.md asks contributors to Linux build changes to test on multiple distributions, update documentation, and consider CI/CD implications. -- evidence: [BUILDING_LINUX.md#L213-L213](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L213-L213), [BUILDING_LINUX.md#L215-L218](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L215-L218)
- skills-patterns (1 claim(s)):
  - [observation/documented] Recipes are YAML-based task definitions that can bundle extensions and, with sub-recipes and subagents, express multi-step workflows; an example recipe declares extensions with stdio type, command, and args. -- evidence: [CUSTOM_DISTROS.md#L45-L54](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L45-L54), [CUSTOM_DISTROS.md#L218-L228](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L218-L228)
- interfaces (3 claim(s)):
  - [observation/documented] goose ships as a native desktop app for macOS, Linux, and Windows, a full CLI, and an API for embedding it elsewhere. -- evidence: [README.md#L5-L5](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L5-L5), [README.md#L25-L25](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L25-L25)
  - [observation/documented] Docker usage is configured via environment variables such as GOOSE_PROVIDER, GOOSE_MODEL, and provider API keys, with CLI commands like 'goose run -t'. -- evidence: [BUILDING_DOCKER.md#L19-L24](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L19-L24), [BUILDING_DOCKER.md#L74-L79](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L74-L79), [BUILDING_DOCKER.md#L140-L142](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L140-L142)
- memory-state (1 claim(s)):
  - [observation/documented] Secrets are stored via a SecretStorage mechanism that uses the system keyring by default with a file-based fallback available, and configuration lives at ~/.config/goose/config.yaml. -- evidence: [CUSTOM_DISTROS.md#L166-L168](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L166-L168)
More evidence: [full detail](goose.detail.md)

Metadata and full claim list: [full detail](goose.detail.md)
Human notes ([notes](goose.notes.md), never overwritten by build)

[Back to map index](../../index.md)
