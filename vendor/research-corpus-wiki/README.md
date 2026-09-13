# Research Corpus Wiki

A complete research-workbench skill and Python toolkit for turning an existing corpus into a navigable, source-grounded wiki. Canonical Markdown, YAML, and JSONL stay in Git; sources remain untouched.

The package includes the skill entrypoint, progressive operating references, strict shared JSON Schemas, executable commands, synthetic fixtures, automated tests, CI, and two browsing outputs. It does not require a model-provider API key: the workbench's agent extracts and synthesizes through validated proposal packets.

## Install and run

Install this repository's entire folder as the `research-corpus-wiki` skill using your host's skill installer. For a local workbench, copy or check out the full folder into its skill-discovery directory and pin a reviewed commit.

With Python 3.12 and uv:

```bash
uv sync --locked
uv run --locked rcw --help
uv run --locked python scripts/demo.py --output /tmp/research-wiki-demo
uv run --locked pytest tests -q
```

The demonstration uses fictional studies, legal materials, and an interview. Its `public/index.html` and `internal/index.html` show the same corpus through different access ceilings.

On hosted workbenches with non-executable skill mounts, first set `UV_PROJECT_ENVIRONMENT` to an executable directory outside the skill, such as an absolute path under the workbench workspace. Use that same setting for every `uv` command. Ordinary local checkouts can use the default `.venv`.

## Use on a corpus

```bash
uv run --locked rcw init ../research-wiki --sources ../source-packages --profile mixed
uv run --locked rcw inventory ../research-wiki
uv run --locked rcw sync ../research-wiki
```

Use the skill to prepare and complete ingest proposals, compare claims, answer questions from reopened source slices, and file evidence gaps. See [SKILL.md](SKILL.md) for mode routing and [references/inventory-and-ingest.md](references/inventory-and-ingest.md) for exact input formats.

## What is included

- Source inventory, metadata registration, immutable fingerprints, and version history.
- Claims, source slices, citations, entities, relationships, typed pages, and gaps.
- Validated prepare/apply operations, no-op ingestion, stale-base rejection, and journal recovery.
- Source-grounded analysis and Q&A with qualified/refusal outcomes.
- Public/internal/confidential/restricted access inheritance and quotation checks.
- A searchable static HTML wiki, Quartz content adapter and pinned build wrapper, CSL JSON, and BibTeX.
- GitHub review packets and reproducible validation workflow.

The release is ready for installation and a bounded real-corpus pilot. Semantic entailment remains a researcher/reviewer judgment. Full-scale production performance, cross-workbench federation, authentication services, and native PDF/media extraction are outside v0.1. The precise boundary is recorded in [references/workbench-integration.md](references/workbench-integration.md).

Original implementation, licensed under Apache-2.0. No source code or prompts from the unlicensed research-wiki reference were copied.
