# allenai/marg-reviewer

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e4acd42e3a1c @ 6bbc26d2ddc7a913

## Summary (orientation draft, not independently verified)

The README documents a Docker-based demo of the MARG multi-agent scientific review generation system, including required API keys, three review-generation methods, email notifications via AWS SES, and steps to reproduce the paper's Table 2 experiments using a GPT cache and the ARIES dataset.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository contains code for the web interface used in the MARG user study and serves as a demo of the multi-agent review generation system for scientific papers. -- evidence: [README.md#L3-L3](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] Submitted papers are reviewed by three methods: SARG-B ("barebones"), LiZCa ("liang_etal"), and MARG-S ("multi_agent_specialized"). -- evidence: [README.md#L21-L21](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L21-L21)
  - [observation/documented] Email notifications on review completion are handled through Amazon SES, with the outgoing address configured via OUTGOING_EMAIL in review_worker/run_reviewgen.py. -- evidence: [README.md#L21-L21](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L21-L21), [README.md#L12-L12](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L12-L12)
- design-choices (1 claim(s)):
  - [observation/documented] By default the reproduction pipeline uses the cached GPT responses from the paper to ensure reproducibility; the cache can be disabled by deleting the sqlite file or editing align_config.json. -- evidence: [README.md#L36-L36](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L36-L36)
- workflows (1 claim(s)):
  - [observation/documented] The documented reproduction workflow involves decompressing the GPT cache, syncing the ARIES dataset, building and entering the review_worker Docker container, and running paper_align_eval_repro.py per config directory. -- evidence: [README.md#L30-L34](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L30-L34)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The demo runs as a web application on localhost port 8080, where papers can be submitted on the main page and results viewed at a /list-results page. -- evidence: [README.md#L19-L19](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L19-L19), [README.md#L21-L21](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L21-L21)
  - [observation/documented] Results are accessible via two page types: a /result/ page suited to local use, and a /survey/ page that hides method names and randomizes review order. -- evidence: [README.md#L23-L23](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L23-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Alignment/metrics code for reproducing the paper's Table 2 experiments lives in review_worker/paper_align_eval_repro.py, with experiment configs and outputs under review_worker/data/paper_align_eval/. -- evidence: [README.md#L28-L28](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L28-L28)
- dependencies (3 claim(s)):
  - [observation/documented] Running the demo requires Docker (and possibly docker-compose), plus a .env file with an OpenAI API key; AWS credentials are optional and only needed for email notifications via Amazon SES. -- evidence: [README.md#L5-L10](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L5-L10), [README.md#L12-L12](https://github.com/allenai/marg-reviewer/blob/e4acd42e3a1c39d993258b5409a332b2c20f433c/README.md#L12-L12)
More evidence: [full detail](marg-reviewer.detail.md)

Metadata and full claim list: [full detail](marg-reviewer.detail.md)
Human notes ([notes](marg-reviewer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
