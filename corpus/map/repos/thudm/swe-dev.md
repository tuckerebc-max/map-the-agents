# thudm/swe-dev

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 72917b610c37 @ 9f087b3cd6585980

## Summary (orientation draft, not independently verified)

SWE-Dev is an SWE agent project (ACL'25 Findings) focused on training and inference scaling, with a documented pipeline for GitHub data collection, test-case generation, evaluation, and dataset creation, plus released 7B/32B models and a training dataset.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] SWE-Dev is presented as a software engineering agent focused on training and inference scaling, published as an ACL'25 Findings paper with an arXiv link. -- evidence: [README.md#L13-L13](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L13-L13), [README.md#L3-L5](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L3-L5)
  - [observation/documented] The project links a Hugging Face model release (THUDM/SWE-Dev-32B) and a training dataset (THUDM/SWE-Dev-train). -- evidence: [README.md#L7-L7](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L7-L7)
- components (3 claim(s)):
  - [observation/documented] The test-case generation pipeline has description-generation and code-generation phases, starting from repository information extraction, producing Gherkin scenarios and detailed test cases, with an optional traceback-driven revision step yielding fail-to-pass test cases. -- evidence: [README.md#L33-L33](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L33-L33)
  - [observation/documented] Data collection offers two crawlers: swedev.crawl.get_top_pypi for top PyPI repositories and swedev.crawl.pypi_crawler for all PyPI repositories, followed by swedev.issues.get_tasks_pipeline to process repositories into tasks. -- evidence: [README.md#L110-L117](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L110-L117), [README.md#L91-L97](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L91-L97), [README.md#L101-L105](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L101-L105)
- design-choices (1 claim(s)):
  - [observation/documented] For training scaling, a pipeline synthesizes test cases and scales agent trajectories into training data; for inference scaling, the interaction budget within a single run is increased. -- evidence: [README.md#L15-L16](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L15-L16)
- workflows (2 claim(s)):
  - [observation/documented] Usage instructions direct users to set GitHub tokens and repository directories in conf/config/default.yaml before collection commands, and to configure API info in conf/config.yaml before the generation pipeline. -- evidence: [README.md#L138-L138](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L138-L138), [README.md#L85-L85](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L85-L85)
  - [observation/documented] Evaluation can run in a Docker image built from an Ubuntu 22.04-based Dockerfile (swedev-evaluator) or directly via python -m swedev.testcases.eval_testcases, with a --show_report option to view results. -- evidence: [README.md#L169-L180](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L169-L180), [README.md#L186-L191](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L186-L191), [README.md#L195-L199](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L195-L199), [README.md#L161-L161](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L161-L161), [README.md#L166-L167](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L166-L167)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Configuration lives in conf/config/default.yaml covering all pipeline stages, and can be validated or printed via python -m swedev.config with --validate or --print flags. -- evidence: [README.md#L39-L39](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L39-L39), [README.md#L53-L55](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L53-L55), [README.md#L45-L47](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L45-L47)
  - [observation/documented] Configuration values can be overridden on the command line (e.g. paths.local_repo_dir, github.tokens), and code accesses settings through a Config object with stage-specific fields like Config.Testcase.model and Config.Testcase.revise_rounds. -- evidence: [README.md#L67-L68](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L67-L68), [README.md#L61-L63](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L61-L63), [README.md#L75-L79](https://github.com/THUDM/SWE-Dev/blob/72917b610c3749c9e1236b29effd629f8aca6a99/README.md#L75-L79)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
More evidence: [full detail](swe-dev.detail.md)

Metadata and full claim list: [full detail](swe-dev.detail.md)
Human notes ([notes](swe-dev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
