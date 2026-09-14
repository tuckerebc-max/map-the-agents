---
access: public
aliases: []
claim_ids:
- clm_29c0e03f35f6202596b3f122d0d3627000ab90e800ff8811414cb9294a2f6e79
- clm_32bfd63c12fff0746c2b632a7355f98f0708c2ca567f4c156edde5fe9448abd7
- clm_5aca87cd9562f1eaa5f0b1116863031ef4a16b2a3dc71771837a4de3395d19db
- clm_5d90bcc44b72f1308fe99e13d7dc4869736365320d04a6b1a3d0f1745d4b3e47
- clm_7312beede696695ddd0b4316b693779358cd23e0bb3a5283967bf1cf21bdbca6
- clm_74a640042a3d3ef04c5638fb83a484e5944b0efa7403ec445daa608944135269
- clm_78c30067e7dceb7c479ebbff9c6024e17f63eb6cd17807bd119e51b40491252a
- clm_86fd158e31385fa47535914e660eabd35e633436dd84543ffc0f100540885653
- clm_bc2b1bcff517ed85c391ade1f7fc9b1bf0b0b95b72be32b6ab35331eabe28766
- clm_d9a65cdee0dce8bb8766d2eebf840dd490af449d7a3619e47b930646aea73674
- clm_ddff4cbb116985b5467190e07fe5b6aa3b9374378898acdd604dc2ee4846d14f
- clm_ee074a789ea566314b7903a3be3089380c9ae6b8acf3de770f211e90ef4f7eb2
maturity: draft
page_id: pg_6573ebe6958355f688405482172d676c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0f88a7c96ed8575a92f5bcbf671e48df
title: arphanetx/Monocle/README.md @ 6a865d767a96
updated_at: '2026-09-14T03:36:01Z'
---

# arphanetx/Monocle/README.md @ 6a865d767a96

<!-- rcw:begin owner=source:src_0f88a7c96ed8575a92f5bcbf671e48df block=evidence -->
- Queries are written in plain text because the tool is backed by an LLM, allowing open-ended natural language questions about a binary without prior knowledge. [@claim:clm_29c0e03f35f6202596b3f122d0d3627000ab90e800ff8811414cb9294a2f6e79]
- While processing, Monocle shows a live table sorted by score, listing each analyzed function with a 0-10 relevance score and an explanation; zero-scored functions get no explanation. [@claim:clm_32bfd63c12fff0746c2b632a7355f98f0708c2ca567f4c156edde5fe9448abd7]
- Repository development practice: contributors should fork the repo, create a descriptively named branch, test changes, submit a pull request with a detailed description, and address maintainer feedback before merge. [@claim:clm_5aca87cd9562f1eaa5f0b1116863031ef4a16b2a3dc71771837a4de3395d19db]
- Python dependencies are listed in requirements.txt, including transformers[torch]>=4.28.1, torch>=1.13.1, bitsandbytes>=0.39.0, rich, and huggingface_hub. [@claim:clm_5d90bcc44b72f1308fe99e13d7dc4869736365320d04a6b1a3d0f1745d4b3e47]
- At least 16GB RAM and a dedicated Nvidia GPU with 4GB+ memory are recommended; lower-spec machines can run it but significantly slower. [@claim:clm_7312beede696695ddd0b4316b693779358cd23e0bb3a5283967bf1cf21bdbca6]
- Repository development practice: the project follows the Contributor Covenant Code of Conduct, and bugs or feature requests should be reported via GitHub issues with reproduction details. [@claim:clm_74a640042a3d3ef04c5638fb83a484e5944b0efa7403ec445daa608944135269]
- Monocle has been tested on Windows 11 and is expected, though not confirmed, to be compatible with Unix and other systems. [@claim:clm_78c30067e7dceb7c479ebbff9c6024e17f63eb6cd17807bd119e51b40491252a]
- The CLI takes a binary path and a search target, e.g. monocle --binary <path-to-binary> --find <component-to-find> on Unix, with a monocle.exe variant on Windows. [@claim:clm_86fd158e31385fa47535914e660eabd35e633436dd84543ffc0f100540885653]
- Monocle requires Nvidia CUDA for improved LLM performance, plus Ghidra installed with analyzeHeadless available in the environment. [@claim:clm_bc2b1bcff517ed85c391ade1f7fc9b1bf0b0b95b72be32b6ab35331eabe28766]
- Monocle performs natural language searches against compiled binaries: given a binary and search criteria, it decompiles the binary and uses an in-built LLM to identify and score matching code areas. [@claim:clm_d9a65cdee0dce8bb8766d2eebf840dd490af449d7a3619e47b930646aea73674]
- Monocle uses Ghidra headless to enable decompilation of compiled binaries. [@claim:clm_ddff4cbb116985b5467190e07fe5b6aa3b9374378898acdd604dc2ee4846d14f]
- The runtime model is Mistral-7B-Instruct-v0.2, an instruct fine-tuned Mistral-7B-v0.2 with 7.24B parameters, BF16 tensors, and a 32k context window. [@claim:clm_ee074a789ea566314b7903a3be3089380c9ae6b8acf3de770f211e90ef4f7eb2]
<!-- rcw:end owner=source:src_0f88a7c96ed8575a92f5bcbf671e48df block=evidence -->

## Researcher notes

