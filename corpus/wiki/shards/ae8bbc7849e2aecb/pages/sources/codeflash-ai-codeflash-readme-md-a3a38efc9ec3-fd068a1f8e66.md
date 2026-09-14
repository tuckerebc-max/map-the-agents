---
access: public
aliases: []
claim_ids:
- clm_443a7019da2bc313b421ebb210b9d5a9bc971491012c9cd5519842374c8b0653
- clm_7d851ecef6911863daab06c55a31ba9fc467ce58a588135d3f7d21ef4eeda081
- clm_8885e8b091a26cc1def242f0b638286df8674b6d7f4e008c3a55ada4269f68da
- clm_949d5e5f97b915ae92efd84e17da8aefe4c561a33d93b3e1991be4db652b3fb6
- clm_c4da67cf2db1de57602f9f12efb6f10d84078dbe9d67c80f563c968c5c977e02
maturity: draft
page_id: pg_b2b0af341a3d58998e91fd068a1f8e66
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c610bb39b97f5455b12eada4e7a77247
title: codeflash-ai/codeflash/README.md @ a3a38efc9ec3
updated_at: '2026-09-14T01:41:44Z'
---

# codeflash-ai/codeflash/README.md @ a3a38efc9ec3

<!-- rcw:begin owner=source:src_c610bb39b97f5455b12eada4e7a77247 block=evidence -->
- Configuration is stored in the project's `pyproject.toml` under a `[tool.codeflash]` section, with settings such as module-root, tests-root, formatter-cmds, git-remote, ignore-paths, override-fixtures, and benchmarks-root. [@claim:clm_443a7019da2bc313b421ebb210b9d5a9bc971491012c9cd5519842374c8b0653]
- The CLI supports optimizing a whole codebase with `codeflash --all`, a single script with `codeflash optimize myscript.py`, and per docs a single function via `codeflash --file path --function name`. [@claim:clm_7d851ecef6911863daab06c55a31ba9fc467ce58a588135d3f7d21ef4eeda081]
- The Python tool is installed via pip (or as a dev dependency with uv/poetry) and requires Python 3.9 or above; setup includes generating a Codeflash API key and installing a GitHub app. [@claim:clm_8885e8b091a26cc1def242f0b638286df8674b6d7f4e008c3a55ada4269f68da]
- Codeflash is described as a general-purpose Python optimizer that uses LLMs to generate optimization candidates, tests them for correctness, benchmarks them, and opens merge-ready pull requests with the best optimization. [@claim:clm_949d5e5f97b915ae92efd84e17da8aefe4c561a33d93b3e1991be4db652b3fb6]
- The tool is licensed under the BSL-1.1 license, with the LICENSE file located in the codeflash directory of the repository. [@claim:clm_c4da67cf2db1de57602f9f12efb6f10d84078dbe9d67c80f563c968c5c977e02]
<!-- rcw:end owner=source:src_c610bb39b97f5455b12eada4e7a77247 block=evidence -->

## Researcher notes

