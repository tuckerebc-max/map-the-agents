# thudm/swe-dev -- full detail

[Back to orientation](swe-dev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/thudm/swe-dev/72917b610c3749c9e1236b29effd629f8aca6a99/9f087b3cd6585980.json](../../../wiki/dossiers/thudm/swe-dev/72917b610c3749c9e1236b29effd629f8aca6a99/9f087b3cd6585980.json)

## specifications (2 claim(s))

- [observation/documented] SWE-Dev is presented as a software engineering agent focused on training and inference scaling, published as an ACL'25 Findings paper with an arXiv link. -- evidence: [README.md#L13-L13](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L13-L13), [README.md#L3-L5](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L3-L5) (`clm_fbe3b317a2be9f089667d486bcecdf3e91535dec4d85b76daa51a7b35d7eb2f8`)
- [observation/documented] The project links a Hugging Face model release (THUDM/SWE-Dev-32B) and a training dataset (THUDM/SWE-Dev-train). -- evidence: [README.md#L7-L7](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L7-L7) (`clm_73da1334a7974db11058b7d1a6d2f7e89b4759ce452af4ed8eab96208d6ecffd`)

## components (3 claim(s))

- [observation/documented] The test-case generation pipeline has description-generation and code-generation phases, starting from repository information extraction, producing Gherkin scenarios and detailed test cases, with an optional traceback-driven revision step yielding fail-to-pass test cases. -- evidence: [README.md#L33-L33](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L33-L33) (`clm_c113e0d2915b4cdb955bea4dad4440e65626ab84a17bbd764d679835fd281804`)
- [observation/documented] Data collection offers two crawlers: swedev.crawl.get_top_pypi for top PyPI repositories and swedev.crawl.pypi_crawler for all PyPI repositories, followed by swedev.issues.get_tasks_pipeline to process repositories into tasks. -- evidence: [README.md#L110-L117](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L110-L117), [README.md#L91-L97](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L91-L97), [README.md#L101-L105](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L101-L105) (`clm_bc160456103b7b45e29d5bbb78a6e1d91d95424bc8f7783962f916b780c9a08d`)
- [observation/documented] The top-PyPI collection path requires a chrome driver, which the README says can be installed on Ubuntu via apt install chromium-chromedriver. -- evidence: [README.md#L89-L89](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L89-L89) (`clm_3c365e5815674a89cb0d4fbec0ee2ecaa4c291426122e83d271825427eb3727a`)

## design-choices (1 claim(s))

- [observation/documented] For training scaling, a pipeline synthesizes test cases and scales agent trajectories into training data; for inference scaling, the interaction budget within a single run is increased. -- evidence: [README.md#L15-L16](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L15-L16) (`clm_0919b981024e2a711ead9ca60efe4f0783ec861ca345ee871a33f80fa26c04cb`)

## workflows (2 claim(s))

- [observation/documented] Usage instructions direct users to set GitHub tokens and repository directories in conf/config/default.yaml before collection commands, and to configure API info in conf/config.yaml before the generation pipeline. -- evidence: [README.md#L138-L138](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L138-L138), [README.md#L85-L85](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L85-L85) (`clm_6cdd4a0e88de2306fc08319836d8aece258d1872f7f40dbd17b2f6daf5a991a2`)
- [observation/documented] Evaluation can run in a Docker image built from an Ubuntu 22.04-based Dockerfile (swedev-evaluator) or directly via python -m swedev.testcases.eval_testcases, with a --show_report option to view results. -- evidence: [README.md#L169-L180](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L169-L180), [README.md#L186-L191](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L186-L191), [README.md#L195-L199](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L195-L199), [README.md#L161-L161](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L161-L161), [README.md#L166-L167](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L166-L167) (`clm_57388b4568e317081e226b719eef7b4f0c14f9a475b2cfcfcf236f1ff568c818`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Configuration lives in conf/config/default.yaml covering all pipeline stages, and can be validated or printed via python -m swedev.config with --validate or --print flags. -- evidence: [README.md#L39-L39](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L39-L39), [README.md#L53-L55](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L53-L55), [README.md#L45-L47](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L45-L47) (`clm_83516e37244bd4d3ab9169df18c8feee20a668647fff907cf3921ee3c9899fc8`)
- [observation/documented] Configuration values can be overridden on the command line (e.g. paths.local_repo_dir, github.tokens), and code accesses settings through a Config object with stage-specific fields like Config.Testcase.model and Config.Testcase.revise_rounds. -- evidence: [README.md#L67-L68](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L67-L68), [README.md#L61-L63](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L61-L63), [README.md#L75-L79](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L75-L79) (`clm_2c015ef63a51917f7b9a9069b452d12cfa15d70381914f35e07e8582887b0c6d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] On SWE-bench-Verified, reported resolve rates are 23.4% for the 7B model and 36.6% for the 32B model, claimed to outperform state-of-the-art open-source models. -- evidence: [README.md#L18-L19](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L18-L19) (`clm_cddce4ffe0b15b221164c719b1363da6dd2327cb46c0b29cac04c7c0bad71b5f`)
- [observation/documented] The README reports SWE-Dev-32B reaching 34.0% without inference scaling, described as comparable to GPT-4o, with relative improvements measured against each model's base model. -- evidence: [README.md#L27-L27](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L27-L27), [README.md#L23-L23](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L23-L23) (`clm_6217c620c7dd4f9607c1aab4477f70a9a5497b4881338ec3c8180108fea74892`)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt pins libraries including openai==1.42.0, tiktoken==0.7.0, tree-sitter==0.21.3, swebench, selenium, hydra-core>=1.3.2 and omegaconf>=2.3.0; requirements-base.txt lists many pytest plugins plus black, flake8, mypy and pre-commit. -- evidence: [requirements-base.txt#L1-L31](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/requirements-base.txt#L1-L31), [requirements.txt#L1-L22](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/requirements.txt#L1-L22) (`clm_5c6044b40cdccde549c6c9399bbe2d61e1b0190e5da1de41bbb934ce10f22c61`)
- [observation/documented] The project acknowledges building on open-source projects including SWE-bench, Agentless, OpenHands, and Nebius. -- evidence: [README.md#L221-L221](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L221-L221), [README.md#L217-L217](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L217-L217), [README.md#L215-L215](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L215-L215), [README.md#L219-L219](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L219-L219) (`clm_2ab24720cbe0b38f7b4419c0b95241a369ed27b838b62b3aa371d7562c2bd7ea`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

