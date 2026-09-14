---
access: public
aliases: []
claim_ids:
- clm_02e4d74770b65c3b2719c7caf70acc5720976c3ce1529c16df7cf718bfc8ce14
- clm_1a56f924f5030c9f015928c4d1b462d8a119993d7d1ee8c0b32746959bb2af4d
- clm_2d201c7f6b500375e234eeb825d3be5cd8fca958b61e5144e3414bb6478bbc3d
- clm_2ea065a1e416ed0da84c1ba7b3be598e14bd560daa6cf7d83eeff152edc802d0
- clm_4f4d961868003efe652726f09c98a7d9555b6d94508e80e18523074c6e4bf423
- clm_60af8cd4579a340bfacf3cf6b182f6046a72708daaf82f27d5a31e940a40067b
- clm_616a7f39b408dbe9499745569b5e7aa77f9f077ae99045f382427ed015115c08
- clm_98612d7fe81ad42500dd03c68479f5d61780664736b189c2c90231412b154135
- clm_cde3da9aeef81b3504198ca0c1712a41655e78a32c15975afdaf4f23ff8e86aa
- clm_e3423a2dc4b68357bbb647fb9a04996bec4ca654ed5da0e07b3ee1b2607f2f30
- clm_ea4c4365622c3628ce30c5701e52cfe9cea5fade4c24db0fa0f98015883594c2
- clm_f94df984a6b57a91217bef48eb35e4679207381ba92dbf0bca70092826aaa908
maturity: draft
page_id: pg_19bf043b88d05e9d85c90ec885f61776
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b7664c10e2975bd2b0ce399eacab1d46
title: TencentQQGYLab/AppAgent/README.md @ 2c1900422caf
updated_at: '2026-09-14T04:25:32Z'
---

# TencentQQGYLab/AppAgent/README.md @ 2c1900422caf

<!-- rcw:begin owner=source:src_b7664c10e2975bd2b0ce399eacab1d46 block=evidence -->
- An optional grid overlay can be brought up on the screen so the agent can tap or swipe anywhere, useful for UI elements lacking a numeric tag. [@claim:clm_02e4d74770b65c3b2719c7caf70acc5720976c3ce1529c16df7cf718bfc8ce14]
- The agent communicates with the Android device through Android Debug Bridge (adb) from a PC, with USB debugging enabled on the device; an Android Studio emulator is also supported and auto-detected. [@claim:clm_1a56f924f5030c9f015928c4d1b462d8a119993d7d1ee8c0b32746959bb2af4d]
- The README links to an evaluation benchmark (testset.md) that was released in January 2024 and used during the team's testing of AppAgent. [@claim:clm_2d201c7f6b500375e234eeb825d3be5cd8fca958b61e5144e3414bb6478bbc3d]
- The agent is powered by a multimodal model such as GPT-4V (gpt-4-vision-preview) or the alternative qwen-vl-max, configured via config.yaml with an API key and request interval. [@claim:clm_2ea065a1e416ed0da84c1ba7b3be598e14bd560daa6cf7d83eeff152edc802d0]
- During exploration or demonstration, the agent generates documentation for interacted UI elements and saves it for use in the deployment phase; deployment can auto-detect an existing documentation base for an app. [@claim:clm_4f4d961868003efe652726f09c98a7d9555b6d94508e80e18523074c6e4bf423]
- The agent learns to use new apps either by autonomous exploration or by observing human demonstrations, producing a knowledge base it later consults for complex tasks. [@claim:clm_60af8cd4579a340bfacf3cf6b182f6046a72708daaf82f27d5a31e940a40067b]
- The agent acts through a simplified action space mimicking human interactions like tapping and swiping, avoiding the need for system back-end access so it works across diverse apps. [@claim:clm_616a7f39b408dbe9499745569b5e7aa77f9f077ae99045f382427ed015115c08]
- AppAgent is described as a novel LLM-based multimodal agent framework designed to operate smartphone applications. [@claim:clm_98612d7fe81ad42500dd03c68479f5d61780664736b189c2c90231412b154135]
- In deployment, if no documentation base exists for an app, the agent can run without documentation but success rate is not guaranteed. [@claim:clm_cde3da9aeef81b3504198ca0c1712a41655e78a32c15975afdaf4f23ff8e86aa]
- Users run `learn.py` to enter autonomous exploration or human demonstration mode, and `run.py` for deployment, supplying app name and task description via prompts. [@claim:clm_e3423a2dc4b68357bbb647fb9a04996bec4ca654ed5da0e07b3ee1b2607f2f30]
- The qwen-vl-max alternative model is free but reportedly performs poorer than GPT-4V in the AppAgent context, and each GPT-4V request/response pair costs around $0.03. [@claim:clm_ea4c4365622c3628ce30c5701e52cfe9cea5fade4c24db0fa0f98015883594c2]
- The project requires Python 3 and dependencies installed via requirements.txt, which lists packages including argparse, colorama, dashscope, opencv-python, pyshine, pyyaml, and requests. [@claim:clm_f94df984a6b57a91217bef48eb35e4679207381ba92dbf0bca70092826aaa908]
<!-- rcw:end owner=source:src_b7664c10e2975bd2b0ce399eacab1d46 block=evidence -->

## Researcher notes

