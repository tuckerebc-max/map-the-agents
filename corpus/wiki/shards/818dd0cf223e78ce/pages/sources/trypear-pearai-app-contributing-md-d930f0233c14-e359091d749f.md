---
access: public
aliases: []
claim_ids:
- clm_327e6e20b42e33a4ce0a7438bc9c374d2cb7ef7b1ecce5769fbe35e23c29fa26
- clm_41bae77e4a9aecf51d7d999c3c388a43b2739ee5463109b6d6f9ccc3a8a8697a
- clm_498b297f86e78bff0600bef8649752ffc4d1fde8098282c7397ac1455ec367c0
- clm_79b20f11d8101daa02ad924778231b81ad6a70906cff3f9da4911529f1498d07
- clm_927d7ebbffbcd371ec8b066226e604517d360783d28588ffaf026704cac34dbc
- clm_bb2ff11b25e7588a24a8f875895ee1b4728d6076352bfad0f4e72a4ab114ab00
- clm_e94ff437cbf5557738c4d09308e67d77eec09fb2c6527d96f627261885367fdc
- clm_f8e5a885886312803a492bbfab56a252e0f09dd95c12a5abeb2fa80adebd5417
maturity: draft
page_id: pg_f85fedc31c465070a6c9e359091d749f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_321961e0284a5284ade5ac15aadd9463
title: trypear/pearai-app/CONTRIBUTING.md @ d930f0233c14
updated_at: '2026-09-14T03:20:38Z'
---

# trypear/pearai-app/CONTRIBUTING.md @ d930f0233c14

<!-- rcw:begin owner=source:src_321961e0284a5284ade5ac15aadd9463 block=evidence -->
- Repository development practice: contributors should fork and use personal feature branches named yourname/branch-name even if they have push rights to the main repo. [@claim:clm_327e6e20b42e33a4ce0a7438bc9c374d2cb7ef7b1ecce5769fbe35e23c29fa26]
- Repository development practice: first-time setup runs scripts/pearai/setup-environment.sh (or .ps1 on Windows), and rebuilds use install-dependencies.sh or yarn. [@claim:clm_41bae77e4a9aecf51d7d999c3c388a43b2739ee5463109b6d6f9ccc3a8a8697a]
- Repository development practice: pull requests require signing a Contributor License Agreement once, one PR per issue with the issue linked, and small, focused changes. [@claim:clm_498b297f86e78bff0600bef8649752ffc4d1fde8098282c7397ac1455ec367c0]
- Repository development practice: unit tests run via ./scripts/test.sh from the pearai-app folder, and automated UI smoke tests are documented in test/smoke. [@claim:clm_79b20f11d8101daa02ad924778231b81ad6a70906cff3f9da4911529f1498d07]
- Repository development practice: contributors need Rust/Cargo, Git, Node 20.18.0, npm 10.8.2, Yarn 1, Python 3.11, and a platform C/C++ toolchain, per the prerequisites list. [@claim:clm_927d7ebbffbcd371ec8b066226e604517d360783d28588ffaf026704cac34dbc]
- Repository development practice: ESLint is used for linting, runnable via yarn eslint or as a VS Code task. [@claim:clm_bb2ff11b25e7588a24a8f875895ee1b4728d6076352bfad0f4e72a4ab114ab00]
- Repository development practice: packaging is manual, using gulp tasks like vscode-[platform] for win32, darwin, and linux targets, followed by extension packaging and manual integration steps. [@claim:clm_e94ff437cbf5557738c4d09308e67d77eec09fb2c6527d96f627261885367fdc]
- PearAI is described as a fork of VSCode, with its main functionality in a separate submodule (pearai-submodule) that is itself a fork of Continue. [@claim:clm_f8e5a885886312803a492bbfab56a252e0f09dd95c12a5abeb2fa80adebd5417]
<!-- rcw:end owner=source:src_321961e0284a5284ade5ac15aadd9463 block=evidence -->

## Researcher notes

