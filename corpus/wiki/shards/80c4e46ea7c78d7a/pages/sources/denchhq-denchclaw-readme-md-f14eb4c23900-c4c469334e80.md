---
access: public
aliases: []
claim_ids:
- clm_0a61ac4fd5959db8953d87a72b62191a05797638e9580d37f011349b807edcf7
- clm_643d7ce14e79a30fc5872f000ae54ca7a5934973096b5084f885848b1949bb1a
- clm_6cffd5f5b16d9fca6b952b7dc1d8f69f46eec0cca6f17a4610f0e06dd89d15ad
- clm_700e3a0317cf2eea3354b15d1e279f02d4def9f0809c1ce55f501d87a1b0beea
- clm_ab05579102803d9f7115c940f0be3d366375581dff984005ea1497272ac54582
- clm_b87f23ed0415829893b9b14b2c15b8921f6d1d9f40dd229c89b2490fc25b906a
- clm_bde32b3a9aaa60757e366a3e61713dc84d13ef0bcb178e999f0ecf84c70bcac0
- clm_f464192fdd2dd52c7873dbec40e325cf7e615e6181e1c3390fccc37cb86b6555
maturity: draft
page_id: pg_b3251bdbcd695fc99841c4c469334e80
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_77054f8dd98358f0b345a3121ec80258
title: DenchHQ/DenchClaw/README.md @ f14eb4c23900
updated_at: '2026-09-14T03:45:14Z'
---

# DenchHQ/DenchClaw/README.md @ f14eb4c23900

<!-- rcw:begin owner=source:src_77054f8dd98358f0b345a3121ec80258 block=evidence -->
- DenchClaw provides an npm CLI with subcommands bootstrap, update, restart, start, and stop for onboarding and managing the web server. [@claim:clm_0a61ac4fd5959db8953d87a72b62191a05797638e9580d37f011349b807edcf7]
- Setting DENCHCLAW_DAEMONLESS=1 skips all gateway daemon management and launchd installation across commands, for Docker or environments without systemd/launchd; the gateway must then be run as a foreground process. [@claim:clm_643d7ce14e79a30fc5872f000ae54ca7a5934973096b5084f885848b1949bb1a]
- After onboarding, the web UI is served at localhost:3100 by default. [@claim:clm_6cffd5f5b16d9fca6b952b7dc1d8f69f46eec0cca6f17a4610f0e06dd89d15ad]
- Gateway connections use device pairing: a 'pairing required' error means the local device awaits approval, and pending operator requests can be listed and approved via 'openclaw --profile dench devices list/approve'. [@claim:clm_700e3a0317cf2eea3354b15d1e279f02d4def9f0809c1ce55f501d87a1b0beea]
- OpenClaw commands for DenchClaw must be prefixed with 'openclaw --profile dench', e.g. gateway restart or config set gateway.port 19001. [@claim:clm_ab05579102803d9f7115c940f0be3d366375581dff984005ea1497272ac54582]
- Bootstrap creates a dedicated OpenClaw gateway under ~/.openclaw-dench on port 19001, separate from a usual ~/.openclaw gateway, with config in ~/.openclaw-dench/openclaw.json. [@claim:clm_b87f23ed0415829893b9b14b2c15b8921f6d1d9f40dd229c89b2490fc25b906a]
- Repository development practice: local development uses pnpm (pnpm install, pnpm build, pnpm dev, and pnpm web:dev for Web UI development). [@claim:clm_bde32b3a9aaa60757e366a3e61713dc84d13ef0bcb178e999f0ecf84c70bcac0]
- Manual install requires Node 22+ and is run via 'npx denchclaw@latest bootstrap'; the product is built on OpenClaw and must be kept up to date with it. [@claim:clm_f464192fdd2dd52c7873dbec40e325cf7e615e6181e1c3390fccc37cb86b6555]
<!-- rcw:end owner=source:src_77054f8dd98358f0b345a3121ec80258 block=evidence -->

## Researcher notes

