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

## Use locally

From this checkout, with Python 3.12 and uv:

```sh
uv run --python 3.12 python -m map_agents --root corpus status
uv run --python 3.12 python -m map_agents --root corpus query "memory orchestration" --limit 5 --max-chars 2500
```

The initial live seed is deliberately small; see the map's counts for current coverage.
Leads, collected snapshots and distilled dossiers have separate statuses. Full corpus
population is the next campaign. The separate [synthetic demo](scripts/demo_synthetic.py)
exercises two agent classes through the real wiki kernel without live network or models.

## Connections

The [private GitHub workbench](https://github.com/tuckerebc-max/map-the-agents) receives
`research-completed` dispatches and public inbox commits, and refreshes metadata daily.
Research producers must call this receiver or the local intake command; this repository
does not install account-wide research hooks or connect to live WhatsApp. Supplied chat
exports can be processed locally; only public links and caller-supplied tags enter the map.

No model provider is configured. A small agent can read a bounded worker envelope and
submit a proposal, or an operator can configure a trusted command adapter. The same
contract supports Gemini, Codex 5.3 and GLM Flash; metadata maintenance makes no model calls.

The [Observatory manifest](docs/observatory-manifest.json) locates this workbench under
[Stargazer Observatory](https://github.com/tuckerebc-max/stargazer-observatory).
Source attribution and the existing wiki pin are in [third-party notices](THIRD_PARTY_NOTICES.md).
