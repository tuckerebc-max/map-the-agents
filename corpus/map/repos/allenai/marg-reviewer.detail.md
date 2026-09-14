# allenai/marg-reviewer -- full detail

[Back to orientation](marg-reviewer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/allenai/marg-reviewer/e4acd42e3a1c39d993258b5409a332b2c20f433c/6bbc26d2ddc7a913.json](../../../wiki/dossiers/allenai/marg-reviewer/e4acd42e3a1c39d993258b5409a332b2c20f433c/6bbc26d2ddc7a913.json)

## specifications (1 claim(s))

- [observation/documented] The repository contains code for the web interface used in the MARG user study and serves as a demo of the multi-agent review generation system for scientific papers. -- evidence: [README.md#L3-L3](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L3-L3) (`clm_410f8c64d8d2a41acdbd4252ef064d2ad8bbb3ca71df8615e749353624829e11`)

## components (2 claim(s))

- [observation/documented] Submitted papers are reviewed by three methods: SARG-B ("barebones"), LiZCa ("liang_etal"), and MARG-S ("multi_agent_specialized"). -- evidence: [README.md#L21-L21](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L21-L21) (`clm_7590d98a2276240f8b314c203826b7ef66a0fd4ce1d63a4adc32e5597ba110af`)
- [observation/documented] Email notifications on review completion are handled through Amazon SES, with the outgoing address configured via OUTGOING_EMAIL in review_worker/run_reviewgen.py. -- evidence: [README.md#L21-L21](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L21-L21), [README.md#L12-L12](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L12-L12) (`clm_f30c794b517ee1802d239a08bd3ed92db84bbccb9f1576bc62862149e6e99217`)

## design-choices (1 claim(s))

- [observation/documented] By default the reproduction pipeline uses the cached GPT responses from the paper to ensure reproducibility; the cache can be disabled by deleting the sqlite file or editing align_config.json. -- evidence: [README.md#L36-L36](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L36-L36) (`clm_a1eac8139e923f61c2d04ba50ac18d766ac0c850117cfe846ed9c4168f04e499`)

## workflows (1 claim(s))

- [observation/documented] The documented reproduction workflow involves decompressing the GPT cache, syncing the ARIES dataset, building and entering the review_worker Docker container, and running paper_align_eval_repro.py per config directory. -- evidence: [README.md#L30-L34](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L30-L34) (`clm_3e79cb9524a663e1123804584369004a0e795290949dd97a8bfba7e731eab4c2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The demo runs as a web application on localhost port 8080, where papers can be submitted on the main page and results viewed at a /list-results page. -- evidence: [README.md#L19-L19](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L19-L19), [README.md#L21-L21](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L21-L21) (`clm_870e0816c05087d97250011ddac8bd78c2106fce4922b1f6833c77e3ff515c14`)
- [observation/documented] Results are accessible via two page types: a /result/ page suited to local use, and a /survey/ page that hides method names and randomizes review order. -- evidence: [README.md#L23-L23](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L23-L23) (`clm_2c835b02424166d36c3e0b4d4144cd2cbdd3838ef07d3a43068858de89b78048`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Alignment/metrics code for reproducing the paper's Table 2 experiments lives in review_worker/paper_align_eval_repro.py, with experiment configs and outputs under review_worker/data/paper_align_eval/. -- evidence: [README.md#L28-L28](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L28-L28) (`clm_ed5cd658a9c052d71acbd49d5a3cc81761eaaa64c0d1b786a1f28551858f56f0`)

## dependencies (3 claim(s))

- [observation/documented] Running the demo requires Docker (and possibly docker-compose), plus a .env file with an OpenAI API key; AWS credentials are optional and only needed for email notifications via Amazon SES. -- evidence: [README.md#L5-L10](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L5-L10), [README.md#L12-L12](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L12-L12) (`clm_cb5edc2ccfb25e6b2cfd22e0e0285a1a306ea6197ef2249e7bd00039bc1a8a19`)
- [observation/documented] Reproducing experiments requires the ARIES dataset (paper texts and human reviewer data) downloaded from a public S3 bucket, plus a provided compressed GPT request cache (gpt3_cache.sqlite.xz). -- evidence: [README.md#L30-L34](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L30-L34) (`clm_fa6ba8e7b398de003ebffb5fe8f30b81ed31beb7d4e55f5bac9bed628f8af3d2`)
- [observation/documented] The code is licensed under Apache 2.0 and copyrighted 2023 by the Allen Institute for Artificial Intelligence. -- evidence: [README.md#L42-L42](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L42-L42), [README.md#L40-L40](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L40-L40) (`clm_dca51674df8f390cf11f0a6b23e09f60d1f77f6c3157e11516fb76e3c0f8f9d9`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

