---
access: public
aliases: []
claim_ids:
- clm_00653a1b3c00132caeae35cfac4b7d5792c44044eaf116ea5a6bf552424bea7d
- clm_5623a75280fb7e9f4933641565fa609999381d70ea48def4c9b29226ebae3abd
- clm_84dacb23bfbc06e56b2a43af5f7f2e0ed13302b9deb50f50d711173ce4ef5e68
- clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46
maturity: draft
page_id: pg_bd58f87c81ab5ff582207e068a440c76
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6153364550b653dbba0bb0301fd48a4d
title: stippi/code-assistant/docs/browser-agency-plan.md @ ba818a46c472
updated_at: '2026-09-14T02:43:45Z'
---

# stippi/code-assistant/docs/browser-agency-plan.md @ ba818a46c472

<!-- rcw:begin owner=source:src_6153364550b653dbba0bb0301fd48a4d block=evidence -->
- Repository development practice: building from source requires the Rust toolchain via rustup, specific Linux system libraries for gpui, the Metal toolchain on macOS, and 'cargo build --release'; browser-agency work followed a TDD/checkpoint style where each step compiles, is tested, and is committable on its own. [@claim:clm_00653a1b3c00132caeae35cfac4b7d5792c44044eaf116ea5a6bf552424bea7d]
- browser_act ships as a normal write tool because capability tags are static per tool; in the default bypass-all tier it runs freely, and embedders wanting gated consequential actions add the outward tag via the extra-capabilities hook. browser_login always prompts regardless of tier. [@claim:clm_5623a75280fb7e9f4933641565fa609999381d70ea48def4c9b29226ebae3abd]
- Browser actions are tagged by capability: navigation, screenshots, and reads are read_only, while submit-style actions with external effect are outward and gated by the existing permission tiers with no new mechanism. [@claim:clm_84dacb23bfbc06e56b2a43af5f7f2e0ed13302b9deb50f50d711173ce4ef5e68]
- The GUI is built on Zed's GPUI framework; the codebase is organized into crates including llm, code_assistant, and web, with the web crate already owning chromiumoxide for browser automation. [@claim:clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46]
<!-- rcw:end owner=source:src_6153364550b653dbba0bb0301fd48a4d block=evidence -->

## Researcher notes

