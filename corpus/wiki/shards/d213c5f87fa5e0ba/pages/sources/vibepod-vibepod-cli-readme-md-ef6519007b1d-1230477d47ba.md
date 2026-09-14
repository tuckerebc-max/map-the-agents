---
access: public
aliases: []
claim_ids:
- clm_3dbcc01d27a7595931ef4e502a5001acfd59a66f9f972c02f0033bfc42a88a7e
- clm_4159193229c12321477102e459493848f58508a800d2f989df15964f27e1c450
- clm_5835348860345d9d0d91ce0e68f0d4f6378517660cfe16d6ca8f8bbde6244210
- clm_65cc574b85b2d8a5f9efa36f1c855bda2b1ab476aa5abfcf379e73838cbb5b5a
- clm_718605621670a3b371a48d654c4c4b2de63b573a603ad07da77607bb1ae4162f
- clm_8ebe4a6ab137885c1e9b9ff564cfee3a0418039e0220a972aac6dfa2e0d88600
- clm_a5c4ffb79a0645efc9a4f803666364306864eaba630392c31d9710da2edf9363
- clm_b6ec1f0db41fcf1a048564c6adca0287e2245852b103ad24e02b9f1a8f76037a
- clm_e571f591456707e025b6162ad43133b5cb9107c0f1256c63a64c83faadb4b670
- clm_e91eaa48f1a08e42e542895ab9a6557da30db892c06592384ef78b9d81740138
- clm_f7492468b539c503e317b0cef46179c58eb1bd30e2fa892b8f531ba7e47bded3
maturity: draft
page_id: pg_c6fef79f1fc75c6dbd8f1230477d47ba
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0da32aa802d754e78c8c9e564f0d43e5
title: VibePod/vibepod-cli/README.md @ ef6519007b1d
updated_at: '2026-09-14T03:21:45Z'
---

# VibePod/vibepod-cli/README.md @ ef6519007b1d

<!-- rcw:begin owner=source:src_0da32aa802d754e78c8c9e564f0d43e5 block=evidence -->
- Each agent runs in its own Docker or Podman container, with default images published under the `vibepod` namespace on Docker Hub (e.g. `vibepod/claude:latest`, `vibepod/codex:latest`). [@claim:clm_3dbcc01d27a7595931ef4e502a5001acfd59a66f9f972c02f0033bfc42a88a7e]
- Metrics are collected locally while agents run and served through a built-in dashboard managed via `vp logs start/stop/status`, showing per-agent HTTP traffic, usage over time, and Claude token metrics. [@claim:clm_4159193229c12321477102e459493848f58508a800d2f989df15964f27e1c450]
- The project describes itself as privacy-first: all metrics are collected and stored locally and never sent to the cloud. [@claim:clm_5835348860345d9d0d91ce0e68f0d4f6378517660cfe16d6ca8f8bbde6244210]
- `--ikwid` appends each agent's auto-approval/permission-skip flag when supported; e.g. claude gets `--dangerously-skip-permissions`, gemini and qwen get `--approval-mode=yolo`, and several agents (opencode, auggie, tau, jcode, freebuff, dsh) are listed as not supported. [@claim:clm_65cc574b85b2d8a5f9efa36f1c855bda2b1ab476aa5abfcf379e73838cbb5b5a]
- The CLI is installable via pip (`pip install vibepod`), Homebrew, and conda-forge (conda, mamba, pixi). [@claim:clm_718605621670a3b371a48d654c4c4b2de63b573a603ad07da77607bb1ae4162f]
- Project overlays let users commit a FROM-less Dockerfile fragment in `.vibepod/overlay/`; VibePod auto-builds a cached, content-addressed image layer on top of the agent's base image. [@claim:clm_8ebe4a6ab137885c1e9b9ff564cfee3a0418039e0220a972aac6dfa2e0d88600]
- `vp run <agent> --acp` turns the CLI into an Agent Client Protocol adapter so the containerized agent appears in ACP-capable editors like Zed, with isolation, profiles, overlays and proxy metrics intact. [@claim:clm_a5c4ffb79a0645efc9a4f803666364306864eaba630392c31d9710da2edf9363]
- Reusable prompt recipes ('skills') can be installed per-project or per-user with `vp skills add`. [@claim:clm_b6ec1f0db41fcf1a048564c6adca0287e2245852b103ad24e02b9f1a8f76037a]
- Implemented v1 commands include `vp run`, `vp stop <agent|--all>`, `vp list`, `vp config init/show/path`, and `vp version`. [@claim:clm_e571f591456707e025b6162ad43133b5cb9107c0f1256c63a64c83faadb4b670]
- The product is a unified CLI named `vp`; `vp run <agent>` launches an agent with no required configuration, and extra arguments after `--` are forwarded to the agent process. [@claim:clm_e91eaa48f1a08e42e542895ab9a6557da30db892c06592384ef78b9d81740138]
- Individual images can be overridden per agent via environment variables such as `VP_IMAGE_CLAUDE`, plus `VP_DATASETTE_IMAGE` for the dashboard and `VP_SKILLS_ENGINE_IMAGE` for skills commands. [@claim:clm_f7492468b539c503e317b0cef46179c58eb1bd30e2fa892b8f531ba7e47bded3]
<!-- rcw:end owner=source:src_0da32aa802d754e78c8c9e564f0d43e5 block=evidence -->

## Researcher notes

