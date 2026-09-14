# coderamp-labs/gitingest

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4e259a02fe72 @ eb9e6585fa5a3412

## Summary (orientation draft, not independently verified)

Selected evidence records: Gitingest converts any Git repository into a prompt-friendly text ingest intended for use with LLMs. The product is offered as a CLI shell command, an importable Python package, and a web service; a `gitingest` command analyzes codebases and produces a text dump.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Gitingest converts any Git repository into a prompt-friendly text ingest intended for use with LLMs. -- evidence: [README.md#L27-L27](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L27-L27)
- components (1 claim(s)):
  - [observation/documented] The stack comprises FastAPI backend, Jinja2 HTML templating, Tailwind CSS frontend, tiktoken for token counts, posthog analytics, and Sentry error tracking. -- evidence: [README.md#L342-L347](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L342-L347)
- design-choices (1 claim(s)):
  - [observation/documented] The README states that files listed in .gitignore are skipped by default and documents an --include-submodules CLI option. -- evidence: [README.md#L139-L140](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L139-L140), [README.md#L136-L137](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L136-L137)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: dev dependencies include pytest, pytest-asyncio, pytest-cov, pytest-mock, and pre-commit; the project targets Python 3.9+ for development. -- evidence: [requirements-dev.txt#L1-L7](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/requirements-dev.txt#L1-L7), [CONTRIBUTING.md#L21-L21](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/CONTRIBUTING.md#L21-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The README lists a CLI shell command and an importable Python package, and links to the Gitingest front page at gitingest.com. The gitingest command analyzes codebases and produces a text dump. -- evidence: [README.md#L46-L53](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L46-L53), [README.md#L3-L3](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L3-L3), [README.md#L112-L112](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L112-L112)
  - [observation/documented] The Python API exposes `ingest` and `ingest_async`, returning a (summary, tree, content) tuple, with options such as `token`, `include_submodules`, and `output`. -- evidence: [README.md#L157-L157](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L157-L157), [README.md#L183-L183](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L183-L183), [README.md#L159-L159](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L159-L159), [README.md#L180-L181](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L180-L181), [README.md#L172-L172](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L172-L172), [README.md#L187-L188](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L187-L188)
- memory-state (1 claim(s)):
  - [observation/documented] The server supports S3 storage of digest files (configurable via S3_* environment variables) and, per the changelog, serves a cached digest when available. -- evidence: [CHANGELOG.md#L15-L16](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/CHANGELOG.md#L15-L16), [CHANGELOG.md#L40-L48](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/CHANGELOG.md#L40-L48), [README.md#L234-L245](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L234-L245), [README.md#L282-L305](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L282-L305)
- orchestration (1 claim(s)):
  - [observation/documented] Deployment is via Docker or Docker Compose: the compose file defines app (prod profile), app-dev (dev profile with hot reload), and a MinIO S3-compatible storage service for development. -- evidence: [README.md#L211-L213](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L211-L213), [README.md#L276-L280](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L276-L280), [README.md#L217-L219](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L217-L219), [README.md#L269-L269](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L269-L269), [README.md#L271-L274](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L271-L274), [README.md#L249-L249](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L249-L249), [README.md#L282-L305](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L282-L305)
- tools-permissions (1 claim(s)):
  - [observation/documented] Private repository access uses a GitHub personal access token supplied via the `--token` option, the Python `token` argument, or the GITHUB_TOKEN environment variable. -- evidence: [README.md#L125-L125](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L125-L125), [README.md#L57-L58](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L57-L58), [README.md#L175-L177](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L175-L177), [README.md#L129-L129](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L129-L129), [README.md#L132-L133](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L132-L133), [README.md#L172-L172](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L172-L172)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Runtime dependencies include fastapi, uvicorn, tiktoken, loguru, boto3, prometheus-client, sentry-sdk, and slowapi; tiktoken is used for token estimation and requires Python 3.8+ per the README. -- evidence: [README.md#L46-L53](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L46-L53), [README.md#L57-L58](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L57-L58), [README.md#L342-L347](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L342-L347), [requirements.txt#L1-L14](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/requirements.txt#L1-L14)
More evidence: [full detail](gitingest.detail.md)

Metadata and full claim list: [full detail](gitingest.detail.md)
Human notes ([notes](gitingest.notes.md), never overwritten by build)

[Back to map index](../../index.md)
