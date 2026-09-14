# Installation

## Signed release (macOS and Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/Weilin0723/PurrCode/v1.0.0/scripts/install.sh | sh
```

The installer detects the host platform, downloads both PurrCode binaries, verifies the archive
against the release `SHA256SUMS`, and installs to `~/.local/bin`. Set `PURRCODE_INSTALL_DIR` to use
another destination. Windows users should download and extract the
`purrcode-x86_64-pc-windows-msvc.zip` release asset.

## npm-compatible package

Node.js 18 or newer can install the cross-platform launcher directly from the GitHub release:

```bash
npm install --global https://github.com/Weilin0723/PurrCode/releases/latest/download/purrcode-1.0.0.tgz
```

The package downloads only the matching native archive, checks it against the digest pinned inside
the npm package, and installs both `purrcode` and `purrcoded`. The public npm registry package uses
the owner scope because npm reserves unscoped names that are too similar to existing packages:

```bash
npm install --global @minaovo/purrcode
```

## From source

Install Rust 1.88 or newer, Git, and the build tools required by your operating system:

```bash
cargo install --locked --path crates/purrcode-cli
cargo install --locked --path crates/purrcode-daemon
purrcode init
```

`purrcode init` discovers Ollama or LM Studio, writes owner-local configuration and persistence,
creates a managed Git workspace, starts the authenticated loopback daemon, and verifies readiness.
Run `purrcode ide --repository PATH` to open the native PurrCode desktop IDE, or
`purrcode` to open the terminal Workbench.

## Release packages

Tagged releases build macOS ARM64/x86_64, Linux ARM64/x86_64, and Windows x86_64 archives. Every
archive has a SHA-256 entry, Sigstore bundle, and GitHub build-provenance attestation. Homebrew and
winget manifests live under `packaging/`.

Check or download a release:

```bash
purrcode upgrade check --channel stable
purrcode upgrade download /tmp/purrcode-release.tar.gz
purrcode upgrade install --channel stable
purrcode upgrade rollback
```

`install` verifies the checksum manifest and both Sigstore bundles before extraction, rejects
unsafe archive paths, atomically rotates `purrcode` and `purrcoded`, and preserves the prior
pair for rollback. Before download it verifies installed repository-skill integrity, platform
support, and required-tool availability. It requires `cosign` and the platform `tar` command.

Downloads are accepted only after Sigstore identity and signed-manifest checksum verification.
Existing destination files are never overwritten.

## Optional isolation dependencies

- macOS: `/usr/bin/sandbox-exec` when available.
- Linux: `bubblewrap` (`bwrap`).
- Windows: process filtering and job controls; inspect `purrcode sandbox doctor`.

PurrCode reports degraded isolation explicitly and does not reinterpret it as a full sandbox.
