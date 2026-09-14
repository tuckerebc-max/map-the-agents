# foundationagents/metagpt

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: geekan/metagpt (github id 660551251).
Latest snapshot: commit 11cdf466d042 @ 32a1dc0084829e9e

## Summary (orientation draft, not independently verified)

MetaGPT takes a one-line requirement as input and outputs artifacts such as user stories, competitive analysis, requirements, data structures, APIs, and documents. Internally the system models a software company with product manager, architect, project manager, and engineer roles orchestrated via SOPs, summarized by the philosophy 'Code = SOP(Team)'.

## Source coverage

Source coverage (partial): 6 of 16 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] MetaGPT takes a one-line requirement as input and outputs artifacts such as user stories, competitive analysis, requirements, data structures, APIs, and documents. -- evidence: [README.md#L42-L44](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L42-L44)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Internally the system models a software company with product manager, architect, project manager, and engineer roles orchestrated via SOPs, summarized by the philosophy 'Code = SOP(Team)'. -- evidence: [README.md#L42-L44](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L42-L44)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The product exposes a CLI: running `metagpt "Create a 2048 game"` generates a repository in ./workspace. -- evidence: [README.md#L90-L92](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L90-L92), [README.md#L88-L88](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L88-L88)
  - [observation/documented] MetaGPT can also be used as a Python library via `metagpt.software_company.generate_repo`, which returns a ProjectRepo whose structure can be printed. -- evidence: [README.md#L100-L102](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L100-L102), [README.md#L96-L98](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L96-L98), [README.md#L94-L94](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L94-L94)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README requires Python 3.9 or later but below 3.12, and instructs installing node and pnpm before actual use; installation is possible via pip, an editable git clone, or Docker. -- evidence: [README.md#L57-L58](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L57-L58), [README.md#L65-L66](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L65-L66), [README.md#L54-L55](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L54-L55), [README.md#L63-L63](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L63-L63)
- limitations (2 claim(s)):
  - [observation/documented] Per the FAQ, incremental/differential updates (--inc with project path or name), multiple programming languages, and multiple natural languages are supported only in experimental versions. -- evidence: [docs/FAQ-EN.md#L40-L93](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/FAQ-EN.md#L40-L93)
  - [observation/documented] The FAQ states no quantitative success-rate analysis has been done, though gpt-4-turbo code generation reportedly succeeds significantly more often than gpt-3.5-turbo, and loading existing large projects is described as very difficult. -- evidence: [docs/FAQ-EN.md#L40-L93](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/FAQ-EN.md#L40-L93)
- relevance (1 claim(s)):
  - [observation/documented] The project is MIT-licensed, open-sourced June 2023, and its ICLR 2024 paper on multi-agent collaborative meta programming is cited alongside related work such as AFlow, SPO, AOT, FACT, and SELA. -- evidence: [docs/NEWS.md#L3-L3](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/NEWS.md#L3-L3), [README.md#L167-L175](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L167-L175), [README.md#L16-L20](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L16-L20), [docs/ACADEMIC_WORK.md#L10-L60](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/ACADEMIC_WORK.md#L10-L60), [docs/NEWS.md#L20-L20](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/NEWS.md#L20-L20)
More evidence: [full detail](metagpt.detail.md)

Metadata and full claim list: [full detail](metagpt.detail.md)
Human notes ([notes](metagpt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
