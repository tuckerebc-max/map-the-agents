---
access: public
aliases: []
claim_ids:
- clm_00d2c3d0bce651eb108d816f4be920edd0a19690c7026155b900664e871d1a47
- clm_16c182aea755f6e64233528c64d50173f55f38b475459f876f9d20fd7bab514b
- clm_5dcae4ee4df5f9b77f3cced2c2afb04d7aa7146917c6cf5b6279e9a1d987db2b
- clm_6cc0739de8ef8a4da5b72eb3298e9ab7dbf079a78e08a8a20044c12d213d6073
- clm_af237378a9e16b8378a579c9c738365ca6e9e62952c2199f5a3b20aa54c34ebc
- clm_afade1bfe1657ca5dae4694a5d9ce467cec9cf5161bcdac99d5d440a78ccfc11
- clm_c16b78a47618bcb144481ce04691105a286890c1362c75cad4f6a236f90788d9
- clm_c8407759a71af84060a6e23aca93256a4e8717a9cabc831b81a58dc58910f5db
- clm_ff9ce2cb3c56afdc53a6b7e6eca59f3b6d22a01740825f75fa6d91b046bf3d11
maturity: draft
page_id: pg_39da61bd05275350862bb4e7bde90adc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c9b2495c46fa5053aa3544780beccec8
title: dreamide/dream/README.md @ a50297d30940
updated_at: '2026-09-14T01:47:09Z'
---

# dreamide/dream/README.md @ a50297d30940

<!-- rcw:begin owner=source:src_c9b2495c46fa5053aa3544780beccec8 block=evidence -->
- The app is an Electron application; the README describes running the Electron app against a production build and packaging it with electron-builder. [@claim:clm_00d2c3d0bce651eb108d816f4be920edd0a19690c7026155b900664e871d1a47]
- Prebuilt installers are published for macOS (ARM64 and x64 DMGs), Windows x64, and Linux x64 in DEB, RPM, and AppImage formats via GitHub Releases. [@claim:clm_16c182aea755f6e64233528c64d50173f55f38b475459f876f9d20fd7bab514b]
- The README requires at least one supported agent CLI to be installed: Codex, Claude Code, OpenCode, or Cursor Agent. [@claim:clm_5dcae4ee4df5f9b77f3cced2c2afb04d7aa7146917c6cf5b6279e9a1d987db2b]
- Dream is described as a desktop IDE for working with multiple AI coding agents. [@claim:clm_6cc0739de8ef8a4da5b72eb3298e9ab7dbf079a78e08a8a20044c12d213d6073]
- Repository development practice: pushing a v* tag triggers a 'Package installers' workflow that builds all platforms and publishes installers plus latest*.yml update metadata to GitHub Releases; no environment variables are needed for local packaging. [@claim:clm_af237378a9e16b8378a579c9c738365ca6e9e62952c2199f5a3b20aa54c34ebc]
- The project is licensed under MIT. [@claim:clm_afade1bfe1657ca5dae4694a5d9ce467cec9cf5161bcdac99d5d440a78ccfc11]
- Repository development practice: the README documents pnpm-based commands for installing dependencies, dev, build, start, and packaging, with per-platform package scripts and artifacts written to release/. [@claim:clm_c16b78a47618bcb144481ce04691105a286890c1362c75cad4f6a236f90788d9]
- The product offers a multi-project workspace with project tabs, simultaneous chat views, git workflows (status, branch, commit, push, PR), a file explorer with diff rendering, an integrated terminal, and a browser preview panel. [@claim:clm_c8407759a71af84060a6e23aca93256a4e8717a9cabc831b81a58dc58910f5db]
- Installer filenames are unversioned so latest-release download links stay stable, and the app auto-updates from GitHub Releases via electron-updater. [@claim:clm_ff9ce2cb3c56afdc53a6b7e6eca59f3b6d22a01740825f75fa6d91b046bf3d11]
<!-- rcw:end owner=source:src_c9b2495c46fa5053aa3544780beccec8 block=evidence -->

## Researcher notes

