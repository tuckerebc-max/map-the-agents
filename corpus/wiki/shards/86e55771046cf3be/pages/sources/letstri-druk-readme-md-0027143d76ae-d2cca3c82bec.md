---
access: public
aliases: []
claim_ids:
- clm_1ea97589fc09cc3c9a5e2a5a8c20af49bddfd7f15319a0ec5b417763f9138c6a
- clm_71bf604e8412f63257947af3bb028e4cb5bde25fefcc561b7c7b51fecfd94384
- clm_78058d77cacd79537172b9114aa5000b5b02b9d1115ee8c2a5f3ae0b85be173d
- clm_8b08e78c02254e2eec7ead41eacacce3e6faf9399a33fac7f0a8ca69a655e38f
- clm_8dc27333aac07ad2c116b035c8650fac1b25dada335761b672f954fcb83055ad
- clm_a430b203a9162023bd6c5e191de86b6fd4f1e136a7ce1b514478476405b5235a
- clm_b90d760fdf0b3054128d8003b3c8ece1f9d565365349e3c54a489998cc968502
- clm_cc6dfd0780483a2792d13ae3b92ad8c3e0d78e4390d6f2d0638042a3de825313
- clm_f979a6de9d96a60ed4746574451b6ceec5c65d75edb7bbe051ae4453a384f7cc
maturity: draft
page_id: pg_1e2e22b92bc1575fbdc7d2cca3c82bec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f9a45e70bfc652f5abd17376411b4060
title: letstri/druk/README.md @ 0027143d76ae
updated_at: '2026-09-14T04:05:49Z'
---

# letstri/druk/README.md @ 0027143d76ae

<!-- rcw:begin owner=source:src_f9a45e70bfc652f5abd17376411b4060 block=evidence -->
- Repository development practice: the extension market is a folder in this repo served raw from main, so a merged pull request makes an extension installable immediately; contributing one is a JSON file plus a PR. [@claim:clm_1ea97589fc09cc3c9a5e2a5a8c20af49bddfd7f15319a0ec5b417763f9138c6a]
- Review notes persist in review.json beside the config, keyed by project, so an external agent can read and append answers while druk is open; answers reference a parent note id. [@claim:clm_71bf604e8412f63257947af3bb028e4cb5bde25fefcc561b7c7b51fecfd94384]
- The CLI accepts a directory, a file, or a file with line/column (e.g. src/main.ts:42:7); npx and bunx work without installing. [@claim:clm_78058d77cacd79537172b9114aa5000b5b02b9d1115ee8c2a5f3ae0b85be173d]
- PDF tabs are read-only, and corrupt, encrypted or unsupported PDFs stay closable while showing why they could not be rendered. [@claim:clm_8b08e78c02254e2eec7ead41eacacce3e6faf9399a33fac7f0a8ca69a655e38f]
- Druk is a terminal code editor offering a file tree, tabs, search, PDF viewing, git marks, and syntax highlighting for 30+ languages, usable with keyboard and mouse. [@claim:clm_8dc27333aac07ad2c116b035c8650fac1b25dada335761b672f954fcb83055ad]
- Druk ships as one self-contained executable requiring no Node or Bun, distributed via install script, Homebrew, npm/bun launchers, .deb/.rpm, and release binaries for macOS, Linux and Windows. [@claim:clm_a430b203a9162023bd6c5e191de86b6fd4f1e136a7ce1b514478476405b5235a]
- Druk remembers each project's open tabs, active file and expanded folders and restores them on the next open of that directory. [@claim:clm_b90d760fdf0b3054128d8003b3c8ece1f9d565365349e3c54a489998cc968502]
- Extensions are JSON manifests, never code: installing one executes nothing, and manifests are read at startup with reload available via 'r' in the extensions panel. [@claim:clm_cc6dfd0780483a2792d13ae3b92ad8c3e0d78e4390d6f2d0638042a3de825313]
- F1 opens a command palette containing every feature; Ctrl+P fuzzy-opens files and Ctrl+K shows a transient strip of keys valid in the current pane. [@claim:clm_f979a6de9d96a60ed4746574451b6ceec5c65d75edb7bbe051ae4453a384f7cc]
<!-- rcw:end owner=source:src_f9a45e70bfc652f5abd17376411b4060 block=evidence -->

## Researcher notes

