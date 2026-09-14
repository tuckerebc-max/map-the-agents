---
access: public
aliases: []
claim_ids:
- clm_0919b981024e2a711ead9ca60efe4f0783ec861ca345ee871a33f80fa26c04cb
- clm_2ab24720cbe0b38f7b4419c0b95241a369ed27b838b62b3aa371d7562c2bd7ea
- clm_2c015ef63a51917f7b9a9069b452d12cfa15d70381914f35e07e8582887b0c6d
- clm_3c365e5815674a89cb0d4fbec0ee2ecaa4c291426122e83d271825427eb3727a
- clm_57388b4568e317081e226b719eef7b4f0c14f9a475b2cfcfcf236f1ff568c818
- clm_6217c620c7dd4f9607c1aab4477f70a9a5497b4881338ec3c8180108fea74892
- clm_6cdd4a0e88de2306fc08319836d8aece258d1872f7f40dbd17b2f6daf5a991a2
- clm_73da1334a7974db11058b7d1a6d2f7e89b4759ce452af4ed8eab96208d6ecffd
- clm_83516e37244bd4d3ab9169df18c8feee20a668647fff907cf3921ee3c9899fc8
- clm_bc160456103b7b45e29d5bbb78a6e1d91d95424bc8f7783962f916b780c9a08d
- clm_c113e0d2915b4cdb955bea4dad4440e65626ab84a17bbd764d679835fd281804
- clm_cddce4ffe0b15b221164c719b1363da6dd2327cb46c0b29cac04c7c0bad71b5f
- clm_fbe3b317a2be9f089667d486bcecdf3e91535dec4d85b76daa51a7b35d7eb2f8
maturity: draft
page_id: pg_efa46d2221a35541bfca98836262d7cf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_00bb22c6b26756bdb3814ecccb954f89
title: THUDM/SWE-Dev/README.md @ 72917b610c37
updated_at: '2026-09-14T04:26:51Z'
---

# THUDM/SWE-Dev/README.md @ 72917b610c37

<!-- rcw:begin owner=source:src_00bb22c6b26756bdb3814ecccb954f89 block=evidence -->
- For training scaling, a pipeline synthesizes test cases and scales agent trajectories into training data; for inference scaling, the interaction budget within a single run is increased. [@claim:clm_0919b981024e2a711ead9ca60efe4f0783ec861ca345ee871a33f80fa26c04cb]
- The project acknowledges building on open-source projects including SWE-bench, Agentless, OpenHands, and Nebius. [@claim:clm_2ab24720cbe0b38f7b4419c0b95241a369ed27b838b62b3aa371d7562c2bd7ea]
- Configuration values can be overridden on the command line (e.g. paths.local_repo_dir, github.tokens), and code accesses settings through a Config object with stage-specific fields like Config.Testcase.model and Config.Testcase.revise_rounds. [@claim:clm_2c015ef63a51917f7b9a9069b452d12cfa15d70381914f35e07e8582887b0c6d]
- The top-PyPI collection path requires a chrome driver, which the README says can be installed on Ubuntu via apt install chromium-chromedriver. [@claim:clm_3c365e5815674a89cb0d4fbec0ee2ecaa4c291426122e83d271825427eb3727a]
- Evaluation can run in a Docker image built from an Ubuntu 22.04-based Dockerfile (swedev-evaluator) or directly via python -m swedev.testcases.eval_testcases, with a --show_report option to view results. [@claim:clm_57388b4568e317081e226b719eef7b4f0c14f9a475b2cfcfcf236f1ff568c818]
- The README reports SWE-Dev-32B reaching 34.0% without inference scaling, described as comparable to GPT-4o, with relative improvements measured against each model's base model. [@claim:clm_6217c620c7dd4f9607c1aab4477f70a9a5497b4881338ec3c8180108fea74892]
- Usage instructions direct users to set GitHub tokens and repository directories in conf/config/default.yaml before collection commands, and to configure API info in conf/config.yaml before the generation pipeline. [@claim:clm_6cdd4a0e88de2306fc08319836d8aece258d1872f7f40dbd17b2f6daf5a991a2]
- The project links a Hugging Face model release (THUDM/SWE-Dev-32B) and a training dataset (THUDM/SWE-Dev-train). [@claim:clm_73da1334a7974db11058b7d1a6d2f7e89b4759ce452af4ed8eab96208d6ecffd]
- Configuration lives in conf/config/default.yaml covering all pipeline stages, and can be validated or printed via python -m swedev.config with --validate or --print flags. [@claim:clm_83516e37244bd4d3ab9169df18c8feee20a668647fff907cf3921ee3c9899fc8]
- Data collection offers two crawlers: swedev.crawl.get_top_pypi for top PyPI repositories and swedev.crawl.pypi_crawler for all PyPI repositories, followed by swedev.issues.get_tasks_pipeline to process repositories into tasks. [@claim:clm_bc160456103b7b45e29d5bbb78a6e1d91d95424bc8f7783962f916b780c9a08d]
- The test-case generation pipeline has description-generation and code-generation phases, starting from repository information extraction, producing Gherkin scenarios and detailed test cases, with an optional traceback-driven revision step yielding fail-to-pass test cases. [@claim:clm_c113e0d2915b4cdb955bea4dad4440e65626ab84a17bbd764d679835fd281804]
- On SWE-bench-Verified, reported resolve rates are 23.4% for the 7B model and 36.6% for the 32B model, claimed to outperform state-of-the-art open-source models. [@claim:clm_cddce4ffe0b15b221164c719b1363da6dd2327cb46c0b29cac04c7c0bad71b5f]
- SWE-Dev is presented as a software engineering agent focused on training and inference scaling, published as an ACL'25 Findings paper with an arXiv link. [@claim:clm_fbe3b317a2be9f089667d486bcecdf3e91535dec4d85b76daa51a7b35d7eb2f8]
<!-- rcw:end owner=source:src_00bb22c6b26756bdb3814ecccb954f89 block=evidence -->

## Researcher notes

