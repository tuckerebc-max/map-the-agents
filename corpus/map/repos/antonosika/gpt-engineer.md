# antonosika/gpt-engineer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a90fcd543eed @ 2f719d3003f5982a

## Summary (orientation draft, not independently verified)

The evidence is README, disclaimer, governance, roadmap, and terms files for gpt-engineer, a CLI tool that generates and improves code from natural-language prompts. It documents usage, model support, a benchmarking binary, and project governance, but contains no source code inspection.

## Source coverage

Source coverage (partial): 6 of 22 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Optional usage-data collection is opt-in: it occurs only when a consent file named .gpte_consent exists in the gpt-engineer directory. -- evidence: [TERMS_OF_USE.md#L11-L11](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/TERMS_OF_USE.md#L11-L11)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors can propose roadmap designs as Google Docs in Discord, submit PRs for roadmap items, or review others' PRs, with volunteer work acknowledged. -- evidence: [ROADMAP.md#L27-L29](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/ROADMAP.md#L27-L29), [ROADMAP.md#L31-L31](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/ROADMAP.md#L31-L31)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Users run the `gpte` CLI against a project directory containing an extension-less `prompt` file with natural-language instructions, e.g. `gpte projects/my-new-project`. -- evidence: [README.md#L57-L60](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L57-L60)
  - [observation/documented] Improving existing code is done by placing a `prompt` file in the target code folder and running `gpte <project_dir> -i`. -- evidence: [README.md#L63-L66](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L63-L66)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Installing gpt-engineer provides a `bench` binary for benchmarking custom agent implementations against public datasets, currently APPS and MBPP, with a separate template repo for getting started. -- evidence: [README.md#L69-L73](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L69-L73)
- dependencies (3 claim(s)):
  - [observation/documented] The tool installs via `python -m pip install gpt-engineer` for stable releases; development setup uses git clone plus poetry install and `poetry shell`. -- evidence: [README.md#L30-L34](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L30-L34), [README.md#L28-L28](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L28-L28)
  - [observation/documented] Python 3.10-3.12 is actively supported; versions 0.2.6 and earlier were the last to support Python 3.8-3.9. -- evidence: [README.md#L36-L36](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L36-L36)
- limitations (1 claim(s)):
  - [observation/documented] The project describes itself as an experimental application provided as-is without warranty, and warns that GPT-4 usage can be expensive, advising users to monitor their own API costs. -- evidence: [DISCLAIMER.md#L3-L3](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/DISCLAIMER.md#L3-L3), [DISCLAIMER.md#L7-L7](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/DISCLAIMER.md#L7-L7)
- relevance (1 claim(s)):
  - [observation/documented] The project positions itself as a code-generation experimentation platform where users specify software in natural language, watch AI write and execute code, and request improvements. -- evidence: [README.md#L17-L20](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L17-L20), [README.md#L10-L10](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L10-L10)

(3 additional claim(s) omitted for length; see [full detail](gpt-engineer.detail.md) for every claim.)

Metadata and full claim list: [full detail](gpt-engineer.detail.md)
Human notes ([notes](gpt-engineer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
