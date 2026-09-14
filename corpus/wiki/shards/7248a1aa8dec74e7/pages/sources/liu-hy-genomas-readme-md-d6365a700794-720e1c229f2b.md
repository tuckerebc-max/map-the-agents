---
access: public
aliases: []
claim_ids:
- clm_0e0829451014a6cbd00d03da3be23076b29e5dc7b0684c714d26d6986e4caba9
- clm_0f46e5e1bf9353cab532a97f3b9e2ba8657ea21221e2b1e0e73d11fe3de89fce
- clm_42f4c4d8f12ac16be3ef03f265ead00eb322d28c3274ea2599890b989aee8708
- clm_47e3b0dc79dc4d57a86823b73e2e012122499bba756bfd64f69d04b2d641e17e
- clm_4f7bfd89681142653de527c61693108beb18bc981a03f754888cc3f2f6abaad2
- clm_a275697a9eb050747bfcc4ab6acfbb6ef15f63d17660afd8fa6a30b067d0b5fc
- clm_a7a0151c5f6c5f731e944a315ef1d975a2c9f9f9dad5bf9a5f3890fb2e7c69c4
- clm_d1a14f265dd464dde2a720b79002c411e4ce2e1e244cb0117a120bb3f3f4c993
- clm_d90d582e773bc9e5e0074062eb369753ce35b515820fe314c80bb4cd8878e7de
- clm_e27c3ba7837f16d2b6bd636480076c05a1a54f9e9fc23fb06d57219e45365ecc
- clm_f9aee05364d355991297de85cc3f3b6231116a88070ade4eaa675d47ecd00f2d
maturity: draft
page_id: pg_ba724e1871255e7ba4c0720e1c229f2b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4f2074962ebb5915bc125c5e1cf21b04
title: Liu-Hy/GenoMAS/README.md @ d6365a700794
updated_at: '2026-09-14T04:06:53Z'
---

# Liu-Hy/GenoMAS/README.md @ d6365a700794

<!-- rcw:begin owner=source:src_4f2074962ebb5915bc125c5e1cf21b04 block=evidence -->
- The system implements checkpoint resume logic: rerunning the same command after an interruption continues from where it left off, clearing outputs of half-finished tasks. [@claim:clm_0e0829451014a6cbd00d03da3be23076b29e5dc7b0684c714d26d6986e4caba9]
- The CLI supports per-role model overrides (e.g., --code-reviewer-model, --domain-expert-model, --statistician-model, --planning-model) that override the global --model and --api settings. [@claim:clm_0f46e5e1bf9353cab532a97f3b9e2ba8657ea21221e2b1e0e73d11fe3de89fce]
- The framework provides a typed messaging communication protocol for code-driven analysis, a notebook-style workflow where agents plan, write, execute, debug, and backtrack, and customizable agent roles. [@claim:clm_42f4c4d8f12ac16be3ef03f265ead00eb322d28c3274ea2599890b989aee8708]
- The stated design philosophy balances controllability of traditional workflows with autonomous-agent flexibility, favoring minimal encapsulation for easier agent experiments. [@claim:clm_47e3b0dc79dc4d57a86823b73e2e012122499bba756bfd64f69d04b2d641e17e]
- Setup involves downloading ~42 GB of GenoTEX input data, validating it with download/validator.py, creating a Python 3.10 conda environment, and configuring API keys in a .env file copied from env.example. [@claim:clm_4f7bfd89681142653de527c61693108beb18bc981a03f754888cc3f2f6abaad2]
- A full benchmark run over all 1,384 GenoTEX trait-condition pairs is estimated at 3-5 days and $300+ in API cost; experiments require up to 20K input tokens, relevant for local GPU deployment. [@claim:clm_a275697a9eb050747bfcc4ab6acfbb6ef15f63d17660afd8fa6a30b067d0b5fc]
- The repository contains two main components: a general multi-agent framework for automating scientific workflows, and a specialized GenoMAS implementation for gene expression analysis. [@claim:clm_a7a0151c5f6c5f731e944a315ef1d975a2c9f9f9dad5bf9a5f3890fb2e7c69c4]
- An --generate-action-units mode generates Action Unit prompts from agent guidelines, optionally pausing for manual editing, with a --non-interactive variant for automated pipelines. [@claim:clm_d1a14f265dd464dde2a720b79002c411e4ce2e1e244cb0117a120bb3f3f4c993]
- The README reports a 60.38% F1 score on the GenoTEX benchmark, claimed to substantially outperform open-domain and generic biomedical agents. [@claim:clm_d90d582e773bc9e5e0074062eb369753ce35b515820fe314c80bb4cd8878e7de]
- A --parallel-mode cohorts option with --max-workers enables concurrent cohort preprocessing, reducing wall-clock time, though large worker counts may hit API rate limits. [@claim:clm_e27c3ba7837f16d2b6bd636480076c05a1a54f9e9fc23fb06d57219e45365ecc]
- GenoMAS analyzes transcriptomic datasets from GEO and TCGA to identify trait-related genes while accounting for confounders. [@claim:clm_f9aee05364d355991297de85cc3f3b6231116a88070ade4eaa675d47ecd00f2d]
<!-- rcw:end owner=source:src_4f2074962ebb5915bc125c5e1cf21b04 block=evidence -->

## Researcher notes

