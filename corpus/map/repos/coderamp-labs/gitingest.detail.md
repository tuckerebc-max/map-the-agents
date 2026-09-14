# coderamp-labs/gitingest -- full detail

[Back to orientation](gitingest.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coderamp-labs/gitingest/4e259a02fe72115bee538271622f1234a81c8e1a/eb9e6585fa5a3412.json](../../../wiki/dossiers/coderamp-labs/gitingest/4e259a02fe72115bee538271622f1234a81c8e1a/eb9e6585fa5a3412.json)

## specifications (1 claim(s))

- [observation/documented] Gitingest converts any Git repository into a prompt-friendly text ingest intended for use with LLMs. -- evidence: [README.md#L27-L27](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L27-L27) (`clm_b966d95a8b544f9e5961b2ef6763c4624afdcea63387cc38afe86b515107fb0d`)

## components (1 claim(s))

- [observation/documented] The stack comprises FastAPI backend, Jinja2 HTML templating, Tailwind CSS frontend, tiktoken for token counts, posthog analytics, and Sentry error tracking. -- evidence: [README.md#L342-L347](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L342-L347) (`clm_739bf6fe96cbca2c851c0ce6647328333f899defdf36eb9342ea75ce74b72fcb`)

## design-choices (1 claim(s))

- [observation/documented] The README states that files listed in .gitignore are skipped by default and documents an --include-submodules CLI option. -- evidence: [README.md#L139-L140](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L139-L140), [README.md#L136-L137](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L136-L137) (`clm_435c83d447dcbccc14f76753a730273d6625ff4e31fa72ae9c580addd111da80`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: dev dependencies include pytest, pytest-asyncio, pytest-cov, pytest-mock, and pre-commit; the project targets Python 3.9+ for development. -- evidence: [requirements-dev.txt#L1-L7](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/requirements-dev.txt#L1-L7), [CONTRIBUTING.md#L21-L21](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/CONTRIBUTING.md#L21-L21) (`clm_a69730671e4f381b2ea2cdaad632a8cf9f335b90c5c580ae12bc60a1c16930c9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The README lists a CLI shell command and an importable Python package, and links to the Gitingest front page at gitingest.com. The gitingest command analyzes codebases and produces a text dump. -- evidence: [README.md#L46-L53](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L46-L53), [README.md#L3-L3](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L3-L3), [README.md#L112-L112](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L112-L112) (`clm_80778d11bd68d30b8845e8f4b7984fe044153bb6a08259bf827553345f15cc57`)
- [observation/documented] The Python API exposes `ingest` and `ingest_async`, returning a (summary, tree, content) tuple, with options such as `token`, `include_submodules`, and `output`. -- evidence: [README.md#L157-L157](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L157-L157), [README.md#L183-L183](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L183-L183), [README.md#L159-L159](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L159-L159), [README.md#L180-L181](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L180-L181), [README.md#L172-L172](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L172-L172), [README.md#L187-L188](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L187-L188) (`clm_822d8f2a5aff19b0f595f858e391194b96df1d7ebea9f19f3c6b3eb9f935b2cb`)
- [observation/documented] CLI options include `--token/-t` for private repos, `--include-submodules`, `--include-gitignored`, and `--output/-o` for a file or STDOUT; by default the digest is written to digest.txt. -- evidence: [README.md#L142-L142](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L142-L142), [README.md#L139-L140](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L139-L140), [README.md#L125-L125](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L125-L125), [README.md#L144-L145](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L144-L145), [README.md#L136-L137](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L136-L137) (`clm_935041638a0ee9b8e9cdd20828ddd4369f697ea3639579f3d44ed1cac554153a`)
- [observation/documented] Replacing `hub` with `ingest` in any GitHub URL yields the corresponding digest, and browser extensions for Chrome, Firefox, and Edge are provided (extension source is a separate open-source repo). -- evidence: [README.md#L31-L32](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L31-L32), [README.md#L106-L106](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L106-L106), [README.md#L100-L104](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L100-L104), [README.md#L29-L29](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L29-L29) (`clm_2eca910fba006a2f318df68017321da22c36a81c9d3e4e8199a4967fd837bdbd`)

## memory-state (1 claim(s))

- [observation/documented] The server supports S3 storage of digest files (configurable via S3_* environment variables) and, per the changelog, serves a cached digest when available. -- evidence: [CHANGELOG.md#L15-L16](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/CHANGELOG.md#L15-L16), [CHANGELOG.md#L40-L48](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/CHANGELOG.md#L40-L48), [README.md#L234-L245](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L234-L245), [README.md#L282-L305](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L282-L305) (`clm_6815e8daebbf01f8c6e53390da6a12887bf0b33da9aa7964516097a408fc5082`)

## orchestration (1 claim(s))

- [observation/documented] Deployment is via Docker or Docker Compose: the compose file defines app (prod profile), app-dev (dev profile with hot reload), and a MinIO S3-compatible storage service for development. -- evidence: [README.md#L211-L213](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L211-L213), [README.md#L276-L280](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L276-L280), [README.md#L217-L219](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L217-L219), [README.md#L269-L269](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L269-L269), [README.md#L271-L274](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L271-L274), [README.md#L249-L249](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L249-L249), [README.md#L282-L305](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L282-L305) (`clm_9bc652c4441d35d959a62d0b75d788ab447f8560a1024d96b0f3fc002262873c`)

## tools-permissions (1 claim(s))

- [observation/documented] Private repository access uses a GitHub personal access token supplied via the `--token` option, the Python `token` argument, or the GITHUB_TOKEN environment variable. -- evidence: [README.md#L125-L125](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L125-L125), [README.md#L57-L58](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L57-L58), [README.md#L175-L177](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L175-L177), [README.md#L129-L129](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L129-L129), [README.md#L132-L133](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L132-L133), [README.md#L172-L172](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L172-L172) (`clm_9cfc4236d95bb0b310ee65ba2b2f17ba2c3f7b153b45aff4c5c87b4fd6afee46`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include fastapi, uvicorn, tiktoken, loguru, boto3, prometheus-client, sentry-sdk, and slowapi; tiktoken is used for token estimation and requires Python 3.8+ per the README. -- evidence: [README.md#L46-L53](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L46-L53), [README.md#L57-L58](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L57-L58), [README.md#L342-L347](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/README.md#L342-L347), [requirements.txt#L1-L14](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/requirements.txt#L1-L14) (`clm_ece14df3f0a24c00a88fa8b97617ad41a079a6fa514fea9636aa820093c60934`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

