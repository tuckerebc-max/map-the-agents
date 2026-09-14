# dreamide/dream -- full detail

[Back to orientation](dream.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dreamide/dream/a50297d309405244f40a66ee78486c5c4a3c780b/a82661ac6d1bd95b.json](../../../wiki/dossiers/dreamide/dream/a50297d309405244f40a66ee78486c5c4a3c780b/a82661ac6d1bd95b.json)

## specifications (1 claim(s))

- [observation/documented] Dream is described as a desktop IDE for working with multiple AI coding agents. -- evidence: [README.md#L3-L3](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L3-L3) (`clm_6cc0739de8ef8a4da5b72eb3298e9ab7dbf079a78e08a8a20044c12d213d6073`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The app is an Electron application; the README describes running the Electron app against a production build and packaging it with electron-builder. -- evidence: [README.md#L74-L74](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L74-L74), [README.md#L60-L60](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L60-L60) (`clm_00d2c3d0bce651eb108d816f4be920edd0a19690c7026155b900664e871d1a47`)
- [observation/documented] Installer filenames are unversioned so latest-release download links stay stable, and the app auto-updates from GitHub Releases via electron-updater. -- evidence: [README.md#L76-L81](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L76-L81) (`clm_ff9ce2cb3c56afdc53a6b7e6eca59f3b6d22a01740825f75fa6d91b046bf3d11`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the README documents pnpm-based commands for installing dependencies, dev, build, start, and packaging, with per-platform package scripts and artifacts written to release/. -- evidence: [README.md#L42-L44](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L42-L44), [README.md#L48-L50](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L48-L50), [README.md#L85-L90](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L85-L90), [README.md#L74-L74](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L74-L74), [README.md#L56-L58](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L56-L58), [README.md#L62-L64](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L62-L64), [README.md#L40-L40](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L40-L40), [README.md#L70-L72](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L70-L72) (`clm_c16b78a47618bcb144481ce04691105a286890c1362c75cad4f6a236f90788d9`)
- [observation/documented] Repository development practice: pushing a v* tag triggers a 'Package installers' workflow that builds all platforms and publishes installers plus latest*.yml update metadata to GitHub Releases; no environment variables are needed for local packaging. -- evidence: [README.md#L76-L81](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L76-L81) (`clm_af237378a9e16b8378a579c9c738365ca6e9e62952c2199f5a3b20aa54c34ebc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product offers a multi-project workspace with project tabs, simultaneous chat views, git workflows (status, branch, commit, push, PR), a file explorer with diff rendering, an integrated terminal, and a browser preview panel. -- evidence: [README.md#L10-L15](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L10-L15) (`clm_c8407759a71af84060a6e23aca93256a4e8717a9cabc831b81a58dc58910f5db`)
- [observation/documented] Prebuilt installers are published for macOS (ARM64 and x64 DMGs), Windows x64, and Linux x64 in DEB, RPM, and AppImage formats via GitHub Releases. -- evidence: [README.md#L31-L31](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L31-L31), [README.md#L27-L28](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L27-L28), [README.md#L34-L36](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L34-L36) (`clm_16c182aea755f6e64233528c64d50173f55f38b475459f876f9d20fd7bab514b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A TODO checklist enumerates manual functionality tests for a todo feature, including creating items from tool calls, marking completion, preserving items, rendering states, and surviving a chat refresh. -- evidence: [TODO.md#L3-L7](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/TODO.md#L3-L7) (`clm_9b1e4ee04b5201087bd8fefd7c465c5af2d31b29189dfeaef10647bf8e06f042`)

## dependencies (2 claim(s))

- [observation/documented] The README requires at least one supported agent CLI to be installed: Codex, Claude Code, OpenCode, or Cursor Agent. -- evidence: [README.md#L18-L22](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L18-L22) (`clm_5dcae4ee4df5f9b77f3cced2c2afb04d7aa7146917c6cf5b6279e9a1d987db2b`)
- [observation/documented] The project is licensed under MIT. -- evidence: [README.md#L94-L94](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L94-L94) (`clm_afade1bfe1657ca5dae4694a5d9ce467cec9cf5161bcdac99d5d440a78ccfc11`)

## limitations (1 claim(s))

- [inference/documented] The todo functionality appears to be under development, since its test checklist items are all unchecked in the snapshot. -- evidence: [TODO.md#L3-L7](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/TODO.md#L3-L7) (`clm_43162830842bd92abfa72ab9764a99f01facca71e828d90027f743b78686a396`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

