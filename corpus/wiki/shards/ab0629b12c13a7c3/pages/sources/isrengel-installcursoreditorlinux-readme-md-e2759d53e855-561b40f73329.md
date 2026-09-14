---
access: public
aliases: []
claim_ids:
- clm_402b1da94ccf7d73d058acf7b551d18c362988805ed64f2d4ce921a5c12625ad
- clm_56c4a45c1ee3d3185c1dbb1f71598a75c0b382ac89e9c6811cd4693196265ab5
- clm_5ddba213812cdea99461a536c824979a4c1ef6faecd2efa90891154a6929ae4b
- clm_8f502858b04e04c39fe9109b0b93fda6ee0b3f229e01493cb849e1293f07f8e6
- clm_a8c2018dc54ce25e0cafd8983fefd2a98fa89f067fbbea812ee3bc4d7b4ff9a7
- clm_b4e35970b48b0fd150efbde2a6059ca1be8d77e946a13f6d0ae994c4b02a9746
- clm_cb7ad368d020f497525c5aa1fc6d9f6ca13cbf959bad48cb0d19d3a78bfb60d1
- clm_e668155c6de290f7f3b86e04b729c0f49bdc54283041df17401c0cce079f1bca
maturity: draft
page_id: pg_e6b8a1e8c0fa5d039c66561b40f73329
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f096c4f9bcba5d42a93ca5d0b6e608ab
title: IsRengel/InstallCursorEditorLinux/README.md @ e2759d53e855
updated_at: '2026-09-14T03:59:19Z'
---

# IsRengel/InstallCursorEditorLinux/README.md @ e2759d53e855

<!-- rcw:begin owner=source:src_f096c4f9bcba5d42a93ca5d0b6e608ab block=evidence -->
- The guide targets installing Cursor AI Code Editor as a desktop application on any Linux distribution, describing Cursor as a VSCode-based, AI-powered editor with ChatGPT integration. [@claim:clm_402b1da94ccf7d73d058acf7b551d18c362988805ed64f2d4ce921a5c12625ad]
- The installation requires Git (to clone the repository), Curl (to download installation files), and Bash, with per-distribution install commands given for Debian/Ubuntu, Arch, Fedora, OpenSUSE, Gentoo, and Solus. [@claim:clm_56c4a45c1ee3d3185c1dbb1f71598a75c0b382ac89e9c6811cd4693196265ab5]
- The installer is a Bash script (install.sh) that downloads the Cursor IDE application, sets it up as a desktop application, creates a .desktop menu entry, and configures an automatic update script using systemd. [@claim:clm_5ddba213812cdea99461a536c824979a4c1ef6faecd2efa90891154a6929ae4b]
- The installer configures a systemd service (update-cursor.service) that checks for and installs Cursor IDE updates; it can be triggered manually with systemctl start or enabled at startup with systemctl enable. [@claim:clm_8f502858b04e04c39fe9109b0b93fda6ee0b3f229e01493cb849e1293f07f8e6]
- The repository is kept only for historical and educational purposes, and users are directed to cursor.com for the official Cursor Editor installation. [@claim:clm_a8c2018dc54ce25e0cafd8983fefd2a98fa89f067fbbea812ee3bc4d7b4ff9a7]
- After installation, a `cursor` command is available in the terminal, e.g. `cursor --help`, and uninstallation can be done via `cursor --uninstall` or by manually removing /opt/cursor, the /usr/local/bin/cursor binary, and the update-cursor systemd service. [@claim:clm_b4e35970b48b0fd150efbde2a6059ca1be8d77e946a13f6d0ae994c4b02a9746]
- The documented install workflow clones the repo with --depth=1, runs ./install.sh, then removes the cloned directory; users may edit install.sh beforehand to change settings such as the default installation path of /opt/cursor/. [@claim:clm_cb7ad368d020f497525c5aa1fc6d9f6ca13cbf959bad48cb0d19d3a78bfb60d1]
- The project is deprecated: it was created when Cursor Editor was distributed exclusively as an AppImage, and Cursor now offers an official .deb package for Linux that makes this installer unnecessary. [@claim:clm_e668155c6de290f7f3b86e04b729c0f49bdc54283041df17401c0cce079f1bca]
<!-- rcw:end owner=source:src_f096c4f9bcba5d42a93ca5d0b6e608ab block=evidence -->

## Researcher notes

