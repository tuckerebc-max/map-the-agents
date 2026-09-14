---
access: public
aliases: []
claim_ids:
- clm_2eca910fba006a2f318df68017321da22c36a81c9d3e4e8199a4967fd837bdbd
- clm_435c83d447dcbccc14f76753a730273d6625ff4e31fa72ae9c580addd111da80
- clm_6815e8daebbf01f8c6e53390da6a12887bf0b33da9aa7964516097a408fc5082
- clm_739bf6fe96cbca2c851c0ce6647328333f899defdf36eb9342ea75ce74b72fcb
- clm_80778d11bd68d30b8845e8f4b7984fe044153bb6a08259bf827553345f15cc57
- clm_822d8f2a5aff19b0f595f858e391194b96df1d7ebea9f19f3c6b3eb9f935b2cb
- clm_935041638a0ee9b8e9cdd20828ddd4369f697ea3639579f3d44ed1cac554153a
- clm_9bc652c4441d35d959a62d0b75d788ab447f8560a1024d96b0f3fc002262873c
- clm_9cfc4236d95bb0b310ee65ba2b2f17ba2c3f7b153b45aff4c5c87b4fd6afee46
- clm_b966d95a8b544f9e5961b2ef6763c4624afdcea63387cc38afe86b515107fb0d
- clm_ece14df3f0a24c00a88fa8b97617ad41a079a6fa514fea9636aa820093c60934
maturity: draft
page_id: pg_6d2dfae360155814a5f2b773637ae32a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_707ca8c514e75ba09249b09439d69d3f
title: coderamp-labs/gitingest/README.md @ 4e259a02fe72
updated_at: '2026-09-14T05:05:10Z'
---

# coderamp-labs/gitingest/README.md @ 4e259a02fe72

<!-- rcw:begin owner=source:src_707ca8c514e75ba09249b09439d69d3f block=evidence -->
- Replacing `hub` with `ingest` in any GitHub URL yields the corresponding digest, and browser extensions for Chrome, Firefox, and Edge are provided (extension source is a separate open-source repo). [@claim:clm_2eca910fba006a2f318df68017321da22c36a81c9d3e4e8199a4967fd837bdbd]
- The README states that files listed in .gitignore are skipped by default and documents an --include-submodules CLI option. [@claim:clm_435c83d447dcbccc14f76753a730273d6625ff4e31fa72ae9c580addd111da80]
- The server supports S3 storage of digest files (configurable via S3_* environment variables) and, per the changelog, serves a cached digest when available. [@claim:clm_6815e8daebbf01f8c6e53390da6a12887bf0b33da9aa7964516097a408fc5082]
- The stack comprises FastAPI backend, Jinja2 HTML templating, Tailwind CSS frontend, tiktoken for token counts, posthog analytics, and Sentry error tracking. [@claim:clm_739bf6fe96cbca2c851c0ce6647328333f899defdf36eb9342ea75ce74b72fcb]
- The README lists a CLI shell command and an importable Python package, and links to the Gitingest front page at gitingest.com. The gitingest command analyzes codebases and produces a text dump. [@claim:clm_80778d11bd68d30b8845e8f4b7984fe044153bb6a08259bf827553345f15cc57]
- The Python API exposes `ingest` and `ingest_async`, returning a (summary, tree, content) tuple, with options such as `token`, `include_submodules`, and `output`. [@claim:clm_822d8f2a5aff19b0f595f858e391194b96df1d7ebea9f19f3c6b3eb9f935b2cb]
- CLI options include `--token/-t` for private repos, `--include-submodules`, `--include-gitignored`, and `--output/-o` for a file or STDOUT; by default the digest is written to digest.txt. [@claim:clm_935041638a0ee9b8e9cdd20828ddd4369f697ea3639579f3d44ed1cac554153a]
- Deployment is via Docker or Docker Compose: the compose file defines app (prod profile), app-dev (dev profile with hot reload), and a MinIO S3-compatible storage service for development. [@claim:clm_9bc652c4441d35d959a62d0b75d788ab447f8560a1024d96b0f3fc002262873c]
- Private repository access uses a GitHub personal access token supplied via the `--token` option, the Python `token` argument, or the GITHUB_TOKEN environment variable. [@claim:clm_9cfc4236d95bb0b310ee65ba2b2f17ba2c3f7b153b45aff4c5c87b4fd6afee46]
- Gitingest converts any Git repository into a prompt-friendly text ingest intended for use with LLMs. [@claim:clm_b966d95a8b544f9e5961b2ef6763c4624afdcea63387cc38afe86b515107fb0d]
- Runtime dependencies include fastapi, uvicorn, tiktoken, loguru, boto3, prometheus-client, sentry-sdk, and slowapi; tiktoken is used for token estimation and requires Python 3.8+ per the README. [@claim:clm_ece14df3f0a24c00a88fa8b97617ad41a079a6fa514fea9636aa820093c60934]
<!-- rcw:end owner=source:src_707ca8c514e75ba09249b09439d69d3f block=evidence -->

## Researcher notes

