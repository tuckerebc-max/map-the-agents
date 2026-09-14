---
access: public
aliases: []
claim_ids:
- clm_01f5e19021dc4290a8fd9a00bbcdeb6d986495a85e991f82c986b34febcd962a
- clm_162a7d2e8c1640cc9d5a19a9d0e17a2f389d1ca9d45a6492822e89fe1e567f27
- clm_1c28f692173bd31c4f2d762a0612d63667ab3464043a61f684d94870b4738fe7
- clm_30cbb58265061dd19205a8e14b540c65b087c7c18f7df3300a53ae1fd6313e79
- clm_347c5aae074284cf8093545186ee780273a2de1ad5dcf43f01a262cadfcaa8a8
- clm_61b2875ed31f9b14a511b022de11d8303e93564374c3e7bc9b2569c17bb4c3b2
- clm_70d444e2b608a2b5066b3fa2537f14ef1b22c3079dd0db567d1d503eda9fc66b
- clm_77b3f5647a2ab4bd0aaa53a815091dae89240b4e37ccfafdc325e74c3e92244f
- clm_f387c6efa74b31f252a990c48b24ad3573d6dbff336cd769c32181106591030c
maturity: draft
page_id: pg_7f0938fcec825ea18410be67b0b6423f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5bc9b497b35257bda2c1f6f25db3a70d
title: NeuralInverse/neuralinverse/README.md @ 2d68ded2f2b7
updated_at: '2026-09-14T02:21:25Z'
---

# NeuralInverse/neuralinverse/README.md @ 2d68ded2f2b7

<!-- rcw:begin owner=source:src_5bc9b497b35257bda2c1f6f25db3a70d block=evidence -->
- The project is built on Microsoft's VS Code (MIT-licensed); the OSS edition's additions are licensed under Apache 2.0, and the commercial NeuralInverse product adds proprietary features. [@claim:clm_01f5e19021dc4290a8fd9a00bbcdeb6d986495a85e991f82c986b34febcd962a]
- Power Mode (Cmd+Alt+P) is an autonomous coding agent with 22+ tools and concurrent sub-agents; Agent Manager (Cmd+Alt+A) handles model management and orchestration. [@claim:clm_162a7d2e8c1640cc9d5a19a9d0e17a2f389d1ca9d45a6492822e89fe1e567f27]
- The IDE exposes AI chat and inline edit via Ctrl+L/Ctrl+K keybindings, with sidebar chat, inline diffs, autocomplete, and Fast Apply. [@claim:clm_1c28f692173bd31c4f2d762a0612d63667ab3464043a61f684d94870b4738fe7]
- The project targets AI-assisted work on legacy modernization, firmware development, and regulated or safety-critical codebases, positioning itself as an open-source Cursor alternative. [@claim:clm_30cbb58265061dd19205a8e14b540c65b087c7c18f7df3300a53ae1fd6313e79]
- Repository development practice: contributors build from source with npm install, npm run watch and watchreact watchers, and launch a dev instance via scripts/code.sh or code.bat; Node 20.18.2 is specified via .nvmrc. [@claim:clm_347c5aae074284cf8093545186ee780273a2de1ad5dcf43f01a262cadfcaa8a8]
- The product supports a bring-your-own-LLM model across 20 providers (cloud, local, gateway) with per-feature model selection, and the README states API keys never leave the user's machine. [@claim:clm_61b2875ed31f9b14a511b022de11d8303e93564374c3e7bc9b2569c17bb4c3b2]
- Repository development practice: the repo ships a Dev Containers/Codespaces container, with at least 4 cores and 6 GB RAM (8 GB recommended) needed for a full build. [@claim:clm_70d444e2b608a2b5066b3fa2537f14ef1b22c3079dd0db567d1d503eda9fc66b]
- CE-specific code is organized under src/vs/workbench/contrib/ in modules for AI chat (void/), Power Mode, Agent Manager (neuralInverse/), firmware, and modernisation. [@claim:clm_77b3f5647a2ab4bd0aaa53a815091dae89240b4e37ccfafdc325e74c3e92244f]
- Specialized modules include Firmware & Embedded (Cmd+Alt+F) with 357 MCU variants, SVD register maps, 22 fw_* tools, and Legacy Modernisation (Cmd+Alt+M) with a 5-stage pipeline and 61 translation profiles. [@claim:clm_f387c6efa74b31f252a990c48b24ad3573d6dbff336cd769c32181106591030c]
<!-- rcw:end owner=source:src_5bc9b497b35257bda2c1f6f25db3a70d block=evidence -->

## Researcher notes

