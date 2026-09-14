---
access: public
aliases: []
claim_ids:
- clm_177fd386b796e3afa2f39c569f20c5858d4462abeb3c15d04ebf2164b7b91e2f
- clm_1c49c1fae4258d95de0abc4cf4dd6d9fd749464a8b458b38c16d949673c7ce41
- clm_22c39c780ce9b703a46c1130f08bc00dc043a2b6045866a0730dfca25dc94511
- clm_31799fa410e759f6199b6b0ff2205071c9ed4abfdde7bebb64715a0a44b43f79
- clm_a7214538f8b3ea1fab2ee34bca831fff49d4d695f35fe8adf9d8aeb4da12297e
- clm_d11c603c3825dd625f1a1801c7ae074377531796d42c121cb5afcdc07d577f43
- clm_fbba4f4433e8a236e51d28882eb61c2ff5fd51be933692d3957b512656b15b26
maturity: draft
page_id: pg_211060065895576696dffd34c2d4abba
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_814a7c129471583aa9b8550d44f0814e
title: humanlayer/humanlayer/DEVELOPMENT.md @ 99abe673498c
updated_at: '2026-09-14T02:04:25Z'
---

# humanlayer/humanlayer/DEVELOPMENT.md @ 99abe673498c

<!-- rcw:begin owner=source:src_814a7c129471583aa9b8550d44f0814e block=evidence -->
- Repository development practice: the monorepo offers make setup, check-test, check, and test targets, plus check-py/test-py for Python; TypeScript and Go projects are expected to define their own commands in package.json and Makefiles. [@claim:clm_177fd386b796e3afa2f39c569f20c5858d4462abeb3c15d04ebf2164b7b91e2f]
- Repository development practice: MCP servers launched by Claude Code sessions are passed HUMANLAYER_DAEMON_SOCKET so they connect to the daemon instance that launched them. [@claim:clm_1c49c1fae4258d95de0abc4cf4dd6d9fd749464a8b458b38c16d949673c7ce41]
- Repository development practice: DEVELOPMENT.md describes parallel 'nightly' (stable) and 'dev' (testing) environments so daemon or WUI changes can be tested without restarting the daemon and breaking active Claude sessions. [@claim:clm_22c39c780ce9b703a46c1130f08bc00dc043a2b6045866a0730dfca25dc94511]
- Repository development practice: the daemon and WUI respect HUMANLAYER_DAEMON_SOCKET, HUMANLAYER_DATABASE_PATH, and HUMANLAYER_DAEMON_VERSION_OVERRIDE environment variables, with the socket variable defaulting to ~/.humanlayer/daemon.sock. [@claim:clm_31799fa410e759f6199b6b0ff2205071c9ed4abfdde7bebb64715a0a44b43f79]
- Repository development practice: make targets such as daemon-nightly, wui-nightly, daemon-dev, wui-dev, copy-db-to-dev, cleanup-dev, and dev-status build and run each environment; make daemon-dev starts with a fresh database copy. [@claim:clm_a7214538f8b3ea1fab2ee34bca831fff49d4d695f35fe8adf9d8aeb4da12297e]
- Repository development practice: the two environments use separate Unix sockets (daemon.sock vs daemon-dev.sock) and separate databases (daemon.db vs timestamped dev DBs) to prevent accidental cross-connections. [@claim:clm_d11c603c3825dd625f1a1801c7ae074377531796d42c121cb5afcdc07d577f43]
- Repository development practice: npx humanlayer launch accepts a custom daemon socket via a --daemon-socket flag, the HUMANLAYER_DAEMON_SOCKET environment variable, or a daemon_socket entry in humanlayer.json. [@claim:clm_fbba4f4433e8a236e51d28882eb61c2ff5fd51be933692d3957b512656b15b26]
<!-- rcw:end owner=source:src_814a7c129471583aa9b8550d44f0814e block=evidence -->

## Researcher notes

