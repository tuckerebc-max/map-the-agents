# isrengel/installcursoreditorlinux

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e2759d53e855 @ d07287b8fcb3aa3b

## Summary (orientation draft, not independently verified)

The snapshot is a README-only view of a deprecated Linux installer for Cursor Editor, which was needed only when Cursor shipped as an AppImage and is now superseded by an official .deb package. The README documents prerequisites, an install.sh-driven setup with a systemd update service, CLI usage, and uninstall steps.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The installer is a Bash script (install.sh) that downloads the Cursor IDE application, sets it up as a desktop application, creates a .desktop menu entry, and configures an automatic update script using systemd. -- evidence: [README.md#L28-L30](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L28-L30), [README.md#L94-L97](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L94-L97)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] The documented install workflow clones the repo with --depth=1, runs ./install.sh, then removes the cloned directory; users may edit install.sh beforehand to change settings such as the default installation path of /opt/cursor/. -- evidence: [README.md#L88-L90](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L88-L90), [README.md#L86-L86](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L86-L86), [README.md#L101-L101](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L101-L101)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] After installation, a `cursor` command is available in the terminal, e.g. `cursor --help`, and uninstallation can be done via `cursor --uninstall` or by manually removing /opt/cursor, the /usr/local/bin/cursor binary, and the update-cursor systemd service. -- evidence: [README.md#L137-L139](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L137-L139), [README.md#L113-L115](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L113-L115), [README.md#L143-L148](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L143-L148), [README.md#L111-L111](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L111-L111)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The installer configures a systemd service (update-cursor.service) that checks for and installs Cursor IDE updates; it can be triggered manually with systemctl start or enabled at startup with systemctl enable. -- evidence: [README.md#L121-L123](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L121-L123), [README.md#L127-L129](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L127-L129), [README.md#L119-L119](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L119-L119), [README.md#L125-L125](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L125-L125)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The installation requires Git (to clone the repository), Curl (to download installation files), and Bash, with per-distribution install commands given for Debian/Ubuntu, Arch, Fedora, OpenSUSE, Gentoo, and Solus. -- evidence: [README.md#L46-L46](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L46-L46), [README.md#L28-L30](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L28-L30), [README.md#L76-L76](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L76-L76), [README.md#L38-L38](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L38-L38), [README.md#L54-L54](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L54-L54), [README.md#L69-L69](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L69-L69), [README.md#L61-L61](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L61-L61)
- limitations (2 claim(s)):
  - [observation/documented] The project is deprecated: it was created when Cursor Editor was distributed exclusively as an AppImage, and Cursor now offers an official .deb package for Linux that makes this installer unnecessary. -- evidence: [README.md#L7-L7](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L7-L7), [README.md#L5-L5](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L5-L5)
  - [observation/documented] The repository is kept only for historical and educational purposes, and users are directed to cursor.com for the official Cursor Editor installation. -- evidence: [README.md#L12-L12](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L12-L12), [README.md#L9-L10](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L9-L10)
- relevance (1 claim(s)):
More evidence: [full detail](installcursoreditorlinux.detail.md)

Metadata and full claim list: [full detail](installcursoreditorlinux.detail.md)
Human notes ([notes](installcursoreditorlinux.notes.md), never overwritten by build)

[Back to map index](../../index.md)
