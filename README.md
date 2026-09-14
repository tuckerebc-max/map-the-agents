# Map the Agents

An Observatory workbench for keeping small, source-linked Markdown maps of agent
repositories. Navy Yard and Tech Triangle design work can find relevant components,
specifications, workflows and design choices without opening every codebase again.

Start with the [corpus map](corpus/AGENTS_CORPUS.md) or the
[workbench skill](skills/map-the-agents/SKILL.md). A new repository is an observation;
the Observatory can develop it into a signal and an evaluation candidate.

| Part | Purpose |
|---|---|
| [Map and indexes](corpus/map/index.md) | Compact orientations, classes, components, patterns, gaps and freshness. |
| [Workbench skill](skills/map-the-agents/SKILL.md) | Lookup first; retain every public research lead; prepare bounded distillation. |
| [Python package](map_agents/) | Intake, immutable collection, wiki integration, maps and resumable workers. |
| [Existing wiki skill](vendor/research-corpus-wiki/SKILL.md) | Pinned Research Corpus Wiki kernel owns canonical evidence and writes. |
| [Automation](.github/workflows/) | Windows/Linux CI and daily, manual, public-inbox or research-dispatch maintenance. |
| [Operations](docs/operations.md) | Exact commands, budgets, partial failures and recovery. |
| [Architecture](docs/architecture.md) | Data ownership and evidence contracts. |
| [Population pipeline](docs/population.md) | `populate`/`source_review`/`proposal_recovery` CLIs, budgets and recovery. |
| [Selection guides](docs/selection/) | Evidence-linked architecture and coding/evaluation comparisons over distilled repositories. |

## Use locally

From this checkout, with Python 3.12 and uv:

```sh
uv run --python 3.12 python -m map_agents --root corpus status
uv run --python 3.12 python -m map_agents --root corpus query "memory orchestration" --limit 5 --max-chars 2500
```

The frozen [alltheagents.org](https://alltheagents.org/) capture at backing commit
`0709cccb49aff08a4b10beb95a214005a810a363` covers 1,366 union entry pages (1,347
backing-feed entries, 828 published entries, 105 discrepancies across the three source views). Those pages
resolve to 1,020 entry-to-repository leads; separately, 1,018 current repository identities are
tracked, with 34 recorded former-name aliases linking a renamed repository back to its history. 990
of the tracked identities have a verified frozen source package; 28 have a recorded, specific
collection error.
The initial population is complete: **990 current repository profiles and 12,365 source-linked claims**,
with **28 source-unavailable identities** kept as explicit gaps. Of those claims, 12,319 are
documentation-derived and 46 are code-inspected; no discovered agent code was executed.
Read each profile's coverage and freshness rather than assuming complete feature coverage.
[Release validation and evidence](docs/release-validation.md) records the checks, source-review
receipts and independent sampling limits. The separate [synthetic demo](scripts/demo_synthetic.py)
exercises two agent classes through the real wiki kernel without live network or models.

A design agent typically starts at [`corpus/AGENTS_CORPUS.md`](corpus/AGENTS_CORPUS.md), follows
its class/component/pattern/gap/freshness indexes to a repository or theme of interest, narrows with
a bounded `query`, opens the repository's own dossier page under `corpus/map/repos/` for its
source-linked claims and unknowns, and -- once enough repositories are distilled for the question at
hand -- reads the comparative [architecture](docs/selection/architecture.md) or
[coding-and-evaluation](docs/selection/coding-and-evaluation.md) selection guide for a
cross-repository design comparison. Every step preserves the same evidence distinctions: observation
vs. inference, documented vs. code-inspected, partial snapshot coverage, and an explicit unknown for
any facet no current claim supports.

## Connections

The [private GitHub workbench](https://github.com/tuckerebc-max/map-the-agents) receives
`research-completed` dispatches and public inbox commits, and daily maintenance runs bounded
catalog, directory-site and new-lead intake, metadata refresh, source collection and map
building -- see [operations](docs/operations.md). Hosted maintenance has no model secret
configured today, so it never calls a model or distills a repository; feature distillation runs
separately through the documented local [population pipeline](docs/population.md). Every
researched public GitHub candidate a producer sends through the dispatch receiver or the local
`intake` command is retained, including candidates a human shortlist would have dropped; this
repository does not install account-wide research hooks or connect to live WhatsApp automatically.
Supplied private chat exports are processed locally from disk; only the normalized public links
and caller-supplied project tags they contain enter the shared map.

The population pipeline calls a trusted LunaRoute adapter ([`map_agents/lunaroute.py`](map_agents/lunaroute.py)),
using GLM Flash through a `LUNAROUTE_API_KEY` that must
already be set in the environment (never written to a file or receipt); `worker`'s own contract is
generic and has no default model command, so an operator can configure a trusted adapter for another provider
(Gemini, Codex 5.3) instead; a small agent can also read a bounded worker envelope and submit a
proposal locally with no adapter configured at all.

The [Observatory manifest](docs/observatory-manifest.json) locates this workbench under
[Stargazer Observatory](https://github.com/tuckerebc-max/stargazer-observatory).
Source attribution and the existing wiki pin are in [third-party notices](THIRD_PARTY_NOTICES.md).
