# Workbench integration

## Install

Keep the whole skill folder together: SKILL.md, agents metadata, references, scripts/rcw_core, schemas, assets, pyproject.toml, and uv.lock. Install the folder in the workbench's skill-discovery directory or use the host's GitHub skill installer against a reviewed commit. Never install only SKILL.md: its deterministic tools and references are part of the capability.

Run `uv sync --locked --project PATH_TO_SKILL`; then invoke `uv run --locked --project PATH_TO_SKILL python PATH_TO_SKILL/scripts/rcw.py --help`. The installed Python distribution also provides `rcw`. Windows users may use PowerShell paths and a Python 3.12 environment; the kernel uses portable pathlib operations and does not require zsh or macOS.

If the skill is on a mount that prohibits binary execution, set `UV_PROJECT_ENVIRONMENT` to an absolute path in an executable workbench directory before both commands. Do not put its virtual environment inside the mounted skill. This hosted configuration was exercised during release validation.

Each company/workbench owns its own corpus, source location, access decisions, and review branch. The central repository owns the skill. Do not copy production corpora into the skill repository. Pin a release or full commit, and record that pin in the workbench's capability configuration and corpus lock.

## Research orchestration handoff

A completed upstream package supplies extracted source text, a completion manifest, attribution, exact original locators, source types, permissions, and unresolved questions. The wiki consumes it without changing it. The feedback loop returns gaps, disputed/qualifying relationships, missing-original records, and changed or missing source paths. Route new external searches back to the research workflow rather than answering from unsupported summaries.

## GitHub delivery

The repository package includes CI for Python 3.12, schema/record validation, executable integration tests, lint/type checks, and a synthetic demonstration. It never puts confidential source fixtures into a public repository; all bundled examples are synthetic. A private corpus should supply its own designated reviewers and branch protection. The skill can prepare review artifacts but does not manage GitHub permissions itself.

## v0.1 implementation boundary

Implemented: initialization, metadata registration outside source roots, inventory and resumable sync planning, ingest prepare/apply, source versions/slices/claims, entity and relationship proposals, typed pages, gap records/pages, analysis prepare/apply, lexical evidence Q&A, audit, journal recovery, review packets, HTML view, Quartz content adapter/build wrapper, and CSL JSON/BibTeX exports.

The implementation simplifies the design document where that improves portability: operation IDs use UUIDv4; config is a strict flat schema; apply-time leases replace long-lived extraction locks; commands return JSON with stable error codes; the HTML renderer is included as a zero-service browsing option. All canonical records and proposals use shared Pydantic/JSON Schema contracts.

The runtime validates evidence structure and permissions, not scientific entailment or legal correctness. Semantic extraction and synthesis remain agent/reviewer work. Entity identities are proposals; approved identity resolution and cross-clone merges use reviewed Git changes. Prior source versions require preservation upstream. Search is lexical and bounded. Quartz is an optional separately pinned dependency. Broad deployment requires a real corpus pilot; synthetic correctness and throughput tests do not establish production performance for arbitrary research files.

## Verify and upgrade

Run `uv run --locked --project PATH_TO_SKILL pytest PATH_TO_SKILL/tests -q`. Run `scripts/demo.py --output EMPTY_DIRECTORY` with the same environment to build the bundled fixture corpus and its public/internal views. Run `scripts/export_schemas.py --check` to detect schema drift.

Release validation on September 13, 2026: 50 automated tests passed; all 16 exported schemas matched the runtime models; lint, core type checks, and skill metadata validation passed. An independent skill-use run created a four-source wiki, a qualified answer, evidence gaps, and a filtered public view; four repeat ingestions preserved all 28 canonical files byte for byte. Its analysis-batch finding was fixed and covered by a regression test. An actual Quartz v5 build succeeded at commit `f1fba3fc55cbf60a60a5d09c95a49c042cdab63a`. Synthetic inventory took about 2.8 seconds for 5,000 packages on the test host; that measures inventory only. GitHub-hosted CI is included but must be checked after upload.

Before upgrading, commit the corpus, read the new contract, and run the candidate skill against an isolated copy. Keep schema version 1.0 until a deliberate migration is supplied. Do not silently rewrite IDs or use a moving Git branch as a deployment pin.

## Adapter choices and research basis

The September 12, 2026 comparison screened fifteen established GitHub options alongside [nraford7/research-wiki](https://github.com/nraford7/research-wiki). The latter supplied a useful orientation-layer concept but had no detected license when inspected; this package independently implements the workflow without copying its code or prompts. These projects inform the design; they are not all bundled integrations.

| Project | Strength used to guide this skill | v0.1 relationship |
|---|---|---|
| [Foam](https://github.com/foambubble/foam) | Markdown knowledge maps and human editing | Portable Markdown can be browsed in editors |
| [Quartz](https://github.com/jackyzha0/quartz) | Search, backlinks, and navigable static wikis | Implemented content adapter and pinned build wrapper |
| [zk](https://github.com/zk-org/zk) | Small, automation-friendly CLI above plain files | CLI design reference |
| [SilverBullet](https://github.com/silverbulletmd/silverbullet) | Programmable queries over a Markdown workspace | Future query/viewer candidate |
| [Logseq](https://github.com/logseq/logseq) | Block-level connections and source annotations | Navigation reference; no database dependency |
| [Zettlr](https://github.com/Zettlr/Zettlr) | Research writing and citation workflows | CSL/BibTeX interoperability |
| [Gollum](https://github.com/gollum/gollum) | Git history and conventional wiki editing | Git-native storage reference |
| [Wiki.js](https://github.com/requarks/wiki) | Multi-user collaboration and authentication | Future authenticated adapter, not included |
| [Semantic MediaWiki](https://github.com/SemanticMediaWiki/SemanticMediaWiki) | Typed facts and relationships | Typed entity/relationship ledger |
| [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) | Searchable formal documentation | Future publication adapter |
| [Quarto](https://github.com/quarto-dev/quarto-cli) | Research publishing with citations and cross-references | Future report adapter |
| [Jupyter Book](https://github.com/jupyter-book/jupyter-book) | Reproducible computational research publications | Future computational-corpus adapter |
| [Manubot](https://github.com/manubot/rootstock) | GitHub review and citation checks for research prose | CI and review-packet pattern |
| [TiddlyWiki](https://github.com/TiddlyWiki/TiddlyWiki5) | Self-contained, nonlinear browsing | Offline HTML-view pattern |
| [SiYuan](https://github.com/siyuan-note/siyuan) | Rich evidence workspaces with query and API access | Workflow reference; no app-specific canonical format |

The portable kernel is the shared contract across workbenches. A renderer can be replaced without moving the evidence ledger into its database or confusing a generated page with an inspected original source.
