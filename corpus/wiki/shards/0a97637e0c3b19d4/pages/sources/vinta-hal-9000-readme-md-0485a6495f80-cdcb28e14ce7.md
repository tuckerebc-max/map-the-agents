---
access: public
aliases: []
claim_ids:
- clm_01aab0119d6b225e1aec9585665838c41ab5364e7ab9d40f11a48c89e73deabf
- clm_16b1d164383d255a885856d9fbc751989fd220ecf423e4ef356c995269de243e
- clm_53eadc8c74abc166fc6b3ee2668291610d4cec0140221004ae65973798993cad
- clm_813ff1b8d757e533f1bdae8e485c592f56a785e4d17727f108211e1d2edb9d85
- clm_86e2cdb644da97d4b7b129877b203468e34156029db68bbcd084e142db64c855
- clm_943e46197059f388004f40a59903f617d0d84710857ddb792e0a432ec093ec05
- clm_987e830cf38de163c0c36a51cb8a6484571b8011169a4ddf8b42a9199e243767
- clm_c17f00a74a43c60cf6cebf827abbc7f347bbdcb35a3ddf0fad346dd2014e6943
- clm_e8e7517c3903cc6744877ddbe3af3598706c1b43508b25c486c2b9e87b1f85d3
- clm_ee27e9d1c34e1f309b532158d80f654b2fb01986361d9dd8a49cc138fc364abf
- clm_f781f64ef851ae204fcb28fe4b50825e1b31b02ca364b804070a8192134a6c09
maturity: draft
page_id: pg_b71dfa22e7cf50e2b1cccdcb28e14ce7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ad4147ccf6795c20b7af055d9dee5d0e
title: vinta/hal-9000/README.md @ 0485a6495f80
updated_at: '2026-09-14T04:30:04Z'
---

# vinta/hal-9000/README.md @ 0485a6495f80

<!-- rcw:begin owner=source:src_ad4147ccf6795c20b7af055d9dee5d0e block=evidence -->
- The `hal` CLI supports subcommands including update (with --tags), link/unlink, sync (--force), backup (--prune), restore, and open-the-pod-bay-doors. [@claim:clm_01aab0119d6b225e1aec9585665838c41ab5364e7ab9d40f11a48c89e73deabf]
- Claude Code plugins include hal-output-styles, hal-session-auto-rename (auto-renames sessions as conversations evolve), and hal-voice (plays HAL 9000 voice clips on hook events). [@claim:clm_16b1d164383d255a885856d9fbc751989fd220ecf423e4ef356c995269de243e]
- The project is named after the HAL 9000 computer from Arthur C. Clarke's 2001: A Space Odyssey. [@claim:clm_53eadc8c74abc166fc6b3ee2668291610d4cec0140221004ae65973798993cad]
- Dotfiles include configs for Claude Code settings, Codex, Ghostty, uv, npm, and zsh, described as hardened against supply chain attacks. [@claim:clm_813ff1b8d757e533f1bdae8e485c592f56a785e4d17727f108211e1d2edb9d85]
- A one-line bootstrap command pipes bin/open-the-pod-bay-doors.sh from GitHub into bash. [@claim:clm_86e2cdb644da97d4b7b129877b203468e34156029db68bbcd084e142db64c855]
- Repository development practice: contributors should use `make help` to find targets and prefer Makefile targets over running underlying tools directly; `make test` runs tests and `make hal-completion` regenerates zsh completion after editing bin/hal.py. [@claim:clm_943e46197059f388004f40a59903f617d0d84710857ddb792e0a432ec093ec05]
- The project describes itself as an opinionated AI coding agent and dev environment automation tool for macOS. [@claim:clm_987e830cf38de163c0c36a51cb8a6484571b8011169a4ddf8b42a9199e243767]
- The hal-statusline plugin shows the current model, directory, git branch, and model usage, and adds a grammar check on typed prompts with Traditional Chinese explanations. [@claim:clm_c17f00a74a43c60cf6cebf827abbc7f347bbdcb35a3ddf0fad346dd2014e6943]
- The bootstrap step installs agent skills, Claude Code configs/plugins/rules/statusline, Codex configs, and Ansible roles for Python, Node.js, Bun, Solidity, Docker, Kubernetes, AWS, and Google Cloud. [@claim:clm_e8e7517c3903cc6744877ddbe3af3598706c1b43508b25c486c2b9e87b1f85d3]
- The repo ships agentic skills such as commit (atomic conventional commits), pr, best-practices, blindspot, simple-english, write-like-me, and several refactor/audit skills. [@claim:clm_ee27e9d1c34e1f309b532158d80f654b2fb01986361d9dd8a49cc138fc364abf]
- Skills can be installed into Claude Code via a plugin marketplace command, or into Codex and other agents via `npx skills add vinta/hal-9000`. [@claim:clm_f781f64ef851ae204fcb28fe4b50825e1b31b02ca364b804070a8192134a6c09]
<!-- rcw:end owner=source:src_ad4147ccf6795c20b7af055d9dee5d0e block=evidence -->

## Researcher notes

