---
access: public
aliases: []
claim_ids:
- clm_1f0afc0379d6f78fead65f4817ce14570c548ab15146850ae9365fe69cf3e71f
- clm_3aaa73238993505a6bde83eadb1f8e8b10d075420e2fe3f0d6915f32151ea6c7
- clm_56d0a970385bf2e72ea307271b096d2f3ae552fefbe260ab935956141088821d
- clm_70992677d6bcb6e660f2ca5a35654f69fc301bcab847623c7bb40f25b68e659a
- clm_7d041da455c6625a54a9ea334e3efacb60bd02adc17b636db50ca02c51c24eb2
- clm_c503c7d7cc21d6f8be57e004081ad9a4959b8b0f5123f6f83a094cb126de9bbc
maturity: draft
page_id: pg_dc6843afebb25e0e9725b6b11f725b66
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_927814d17f9a53e58ec0c616e88922d0
title: sr5434/CodegebraGPT/README.md @ 780307f4b361
updated_at: '2026-09-14T04:23:17Z'
---

# sr5434/CodegebraGPT/README.md @ 780307f4b361

<!-- rcw:begin owner=source:src_927814d17f9a53e58ec0c616e88922d0 block=evidence -->
- The README says about 100k samples are used for training (the 100k-text subset) out of roughly one million combined samples, to save costs. [@claim:clm_1f0afc0379d6f78fead65f4817ce14570c548ab15146850ae9365fe69cf3e71f]
- The project's stated purpose is finetuning multimodal LLMs on STEM datasets. [@claim:clm_3aaa73238993505a6bde83eadb1f8e8b10d075420e2fe3f0d6915f32151ea6c7]
- As of this snapshot, dataset compilation/preprocessing is marked complete while finetuning and Hugging Face release remain unchecked, so the model appears not yet trained or released. [@claim:clm_56d0a970385bf2e72ea307271b096d2f3ae552fefbe260ab935956141088821d]
- The planned base model for finetuning is upstage/SOLAR-10.7B-Instruct-v1.0, using the QLoRA method. [@claim:clm_70992677d6bcb6e660f2ca5a35654f69fc301bcab847623c7bb40f25b68e659a]
- Training data is drawn from public Hugging Face datasets including MetaMathQA, Camel AI math/chemistry/physics/biology, GSM8K, MMLU, Evol Instruct Code, Glaive code assistant, arXiv-derived instruct sets, and ScienceQA. [@claim:clm_7d041da455c6625a54a9ea334e3efacb60bd02adc17b636db50ca02c51c24eb2]
- The model is named after the author's earlier Codegebra equation-solving program and is intended as its successor with a more natural interface and expanded abilities. [@claim:clm_c503c7d7cc21d6f8be57e004081ad9a4959b8b0f5123f6f83a094cb126de9bbc]
<!-- rcw:end owner=source:src_927814d17f9a53e58ec0c616e88922d0 block=evidence -->

## Researcher notes

