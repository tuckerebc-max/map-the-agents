# isrengel/installcursoreditorlinux -- full detail

[Back to orientation](installcursoreditorlinux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/isrengel/installcursoreditorlinux/e2759d53e85519ae018cde76b182315d383cb741/d07287b8fcb3aa3b.json](../../../wiki/dossiers/isrengel/installcursoreditorlinux/e2759d53e85519ae018cde76b182315d383cb741/d07287b8fcb3aa3b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The installer is a Bash script (install.sh) that downloads the Cursor IDE application, sets it up as a desktop application, creates a .desktop menu entry, and configures an automatic update script using systemd. -- evidence: [README.md#L28-L30](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L28-L30), [README.md#L94-L97](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L94-L97) (`clm_5ddba213812cdea99461a536c824979a4c1ef6faecd2efa90891154a6929ae4b`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] The documented install workflow clones the repo with --depth=1, runs ./install.sh, then removes the cloned directory; users may edit install.sh beforehand to change settings such as the default installation path of /opt/cursor/. -- evidence: [README.md#L88-L90](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L88-L90), [README.md#L86-L86](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L86-L86), [README.md#L101-L101](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L101-L101) (`clm_cb7ad368d020f497525c5aa1fc6d9f6ca13cbf959bad48cb0d19d3a78bfb60d1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] After installation, a `cursor` command is available in the terminal, e.g. `cursor --help`, and uninstallation can be done via `cursor --uninstall` or by manually removing /opt/cursor, the /usr/local/bin/cursor binary, and the update-cursor systemd service. -- evidence: [README.md#L137-L139](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L137-L139), [README.md#L113-L115](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L113-L115), [README.md#L143-L148](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L143-L148), [README.md#L111-L111](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L111-L111) (`clm_b4e35970b48b0fd150efbde2a6059ca1be8d77e946a13f6d0ae994c4b02a9746`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The installer configures a systemd service (update-cursor.service) that checks for and installs Cursor IDE updates; it can be triggered manually with systemctl start or enabled at startup with systemctl enable. -- evidence: [README.md#L121-L123](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L121-L123), [README.md#L127-L129](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L127-L129), [README.md#L119-L119](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L119-L119), [README.md#L125-L125](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L125-L125) (`clm_8f502858b04e04c39fe9109b0b93fda6ee0b3f229e01493cb849e1293f07f8e6`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The installation requires Git (to clone the repository), Curl (to download installation files), and Bash, with per-distribution install commands given for Debian/Ubuntu, Arch, Fedora, OpenSUSE, Gentoo, and Solus. -- evidence: [README.md#L46-L46](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L46-L46), [README.md#L28-L30](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L28-L30), [README.md#L76-L76](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L76-L76), [README.md#L38-L38](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L38-L38), [README.md#L54-L54](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L54-L54), [README.md#L69-L69](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L69-L69), [README.md#L61-L61](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L61-L61) (`clm_56c4a45c1ee3d3185c1dbb1f71598a75c0b382ac89e9c6811cd4693196265ab5`)

## limitations (2 claim(s))

- [observation/documented] The project is deprecated: it was created when Cursor Editor was distributed exclusively as an AppImage, and Cursor now offers an official .deb package for Linux that makes this installer unnecessary. -- evidence: [README.md#L7-L7](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L7-L7), [README.md#L5-L5](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L5-L5) (`clm_e668155c6de290f7f3b86e04b729c0f49bdc54283041df17401c0cce079f1bca`)
- [observation/documented] The repository is kept only for historical and educational purposes, and users are directed to cursor.com for the official Cursor Editor installation. -- evidence: [README.md#L12-L12](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L12-L12), [README.md#L9-L10](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L9-L10) (`clm_a8c2018dc54ce25e0cafd8983fefd2a98fa89f067fbbea812ee3bc4d7b4ff9a7`)

## relevance (1 claim(s))

- [observation/documented] The guide targets installing Cursor AI Code Editor as a desktop application on any Linux distribution, describing Cursor as a VSCode-based, AI-powered editor with ChatGPT integration. -- evidence: [README.md#L16-L16](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L16-L16), [README.md#L20-L20](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L20-L20), [README.md#L105-L107](https://github.com/IsRengel/InstallCursorEditorLinux/blob/e2759d53e85519ae018cde76b182315d383cb741/README.md#L105-L107) (`clm_402b1da94ccf7d73d058acf7b551d18c362988805ed64f2d4ce921a5c12625ad`)

