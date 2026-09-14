# laizhou/opencode_ui

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 453afb7cc9fc @ 3b903129d6dc525f

## Summary (orientation draft, not independently verified)

The product is a JetBrains IDE plugin integrating the OpenCode open-source AI coding agent into the development workflow. Quick Launch opens a connection dialog via Cmd+Esc (Mac) or Ctrl+\ (Win/Linux), letting users connect to an existing OpenCode server by host:port with optional password, or create a new local terminal session on default port 127.0.0.1:4096.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] When OpenCode edits files, the plugin opens a native IDE diff viewer showing changes chronologically with navigation, progress count, and accept (write to disk and git add) or reject (restore pre-edit state) actions. -- evidence: [README.md#L90-L90](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L90-L90), [README.md#L92-L98](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L92-L98)
  - [observation/documented] The plugin sends a system notification when OpenCode transitions from Busy to Idle, and supports auto-resume of the last session, clickable file-path links in terminal output, and remembered connection settings. -- evidence: [README.md#L111-L111](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L111-L111), [README.md#L10-L19](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L10-L19), [README.md#L59-L59](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L59-L59), [README.md#L105-L105](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L105-L105)
- design-choices (2 claim(s)):
  - [observation/documented] Terminal management uses a single persistent terminal tab per project named OpenCode({port}); closing it causes a new one to be created on next launch. -- evidence: [README.md#L124-L124](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L124-L124), [README.md#L126-L128](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L126-L128)
  - [observation/documented] Keyboard shortcuts are customizable through the IDE's Settings > Keymap by searching for 'OpenCode'. -- evidence: [README.md#L115-L115](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L115-L115)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to build with the Gradle wrapper (./gradlew build, runIde, clean build), run tests via ./gradlew test with class/method/pattern filters, and verify with ./gradlew check for lint. -- evidence: [AGENTS.md#L24-L35](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L24-L35), [AGENTS.md#L38-L53](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L38-L53), [AGENTS.md#L56-L59](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L56-L59), [AGENTS.md#L21-L21](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L21-L21)
  - [observation/documented] Repository development practice: the guide mandates Kotlin coding conventions, 4-space indentation, 120-char lines, no wildcard imports, English-only comments and strings, and avoiding double-bang null operators. -- evidence: [AGENTS.md#L63-L63](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L63-L63), [AGENTS.md#L74-L75](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L74-L75), [AGENTS.md#L78-L82](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L78-L82), [AGENTS.md#L66-L71](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L66-L71)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The product is a JetBrains IDE plugin integrating the OpenCode open-source AI coding agent into the development workflow. -- evidence: [README.md#L6-L6](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L6-L6)
  - [observation/documented] Quick Launch opens a connection dialog via Cmd+Esc (Mac) or Ctrl+\ (Win/Linux), letting users connect to an existing OpenCode server by host:port with optional password, or create a new local terminal session on default port 127.0.0.1:4096. -- evidence: [README.md#L56-L57](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L56-L57), [README.md#L54-L54](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L54-L54), [README.md#L10-L19](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L10-L19)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](opencode_ui.detail.md)

Metadata and full claim list: [full detail](opencode_ui.detail.md)
Human notes ([notes](opencode_ui.notes.md), never overwritten by build)

[Back to map index](../../index.md)
