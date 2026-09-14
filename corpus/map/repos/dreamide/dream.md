# dreamide/dream

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a50297d30940 @ a82661ac6d1bd95b

## Summary (orientation draft, not independently verified)

Evidence is limited to the README and a TODO checklist of one commit of dreamide/dream, a desktop IDE for working with multiple AI coding agents. The README documents features, supported agent CLIs, platform installers, and pnpm-based development/packaging workflows.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Dream is described as a desktop IDE for working with multiple AI coding agents. -- evidence: [README.md#L3-L3](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The app is an Electron application; the README describes running the Electron app against a production build and packaging it with electron-builder. -- evidence: [README.md#L74-L74](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L74-L74), [README.md#L60-L60](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L60-L60)
  - [observation/documented] Installer filenames are unversioned so latest-release download links stay stable, and the app auto-updates from GitHub Releases via electron-updater. -- evidence: [README.md#L76-L81](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L76-L81)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the README documents pnpm-based commands for installing dependencies, dev, build, start, and packaging, with per-platform package scripts and artifacts written to release/. -- evidence: [README.md#L42-L44](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L42-L44), [README.md#L48-L50](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L48-L50), [README.md#L85-L90](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L85-L90), [README.md#L74-L74](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L74-L74), [README.md#L56-L58](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L56-L58), [README.md#L62-L64](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L62-L64), [README.md#L40-L40](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L40-L40), [README.md#L70-L72](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L70-L72)
  - [observation/documented] Repository development practice: pushing a v* tag triggers a 'Package installers' workflow that builds all platforms and publishes installers plus latest*.yml update metadata to GitHub Releases; no environment variables are needed for local packaging. -- evidence: [README.md#L76-L81](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L76-L81)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product offers a multi-project workspace with project tabs, simultaneous chat views, git workflows (status, branch, commit, push, PR), a file explorer with diff rendering, an integrated terminal, and a browser preview panel. -- evidence: [README.md#L10-L15](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L10-L15)
  - [observation/documented] Prebuilt installers are published for macOS (ARM64 and x64 DMGs), Windows x64, and Linux x64 in DEB, RPM, and AppImage formats via GitHub Releases. -- evidence: [README.md#L31-L31](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L31-L31), [README.md#L27-L28](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L27-L28), [README.md#L34-L36](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L34-L36)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] A TODO checklist enumerates manual functionality tests for a todo feature, including creating items from tool calls, marking completion, preserving items, rendering states, and surviving a chat refresh. -- evidence: [TODO.md#L3-L7](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/TODO.md#L3-L7)
- dependencies (2 claim(s)):
  - [observation/documented] The README requires at least one supported agent CLI to be installed: Codex, Claude Code, OpenCode, or Cursor Agent. -- evidence: [README.md#L18-L22](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L18-L22)
  - [observation/documented] The project is licensed under MIT. -- evidence: [README.md#L94-L94](https://github.com/dreamide/dream/blob/a50297d309405244f40a66ee78486c5c4a3c780b/README.md#L94-L94)
- limitations (1 claim(s)):
More evidence: [full detail](dream.detail.md)

Metadata and full claim list: [full detail](dream.detail.md)
Human notes ([notes](dream.notes.md), never overwritten by build)

[Back to map index](../../index.md)
