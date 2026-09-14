# a115/icodes -- full detail

[Back to orientation](icodes.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/a115/icodes/8961152cb0a9a517438ccf707c77a4218f93c6e6/36f1d6ab199e7277.json](../../../wiki/dossiers/a115/icodes/8961152cb0a9a517438ccf707c77a4218f93c6e6/36f1d6ab199e7277.json)

## specifications (1 claim(s))

- [observation/documented] iCODES analyzes and indexes Git commit histories using LLM techniques, summarizing commit intents and enabling semantic search over codebases. -- evidence: [README.md#L4-L4](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L4-L4) (`clm_36b34bb3978f7b4ca98b7d5d86b83a8f00301b5c132feaf753613f9ec431294d`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [inference/documented] The default model choice of gpt-3.5-turbo appears to reflect a deliberate price/quality tradeoff stated in the documentation. -- evidence: [README.md#L21-L21](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L21-L21) (`clm_78dbc26a8b0f0fbda28f2dc69b3c807cf69f8092254fff86c1c45463758a3c25`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: when installing from a cloned repo, Poetry is recommended for dependency management via 'poetry install', and commands are prefixed with 'poetry run python icodes.py'. -- evidence: [README.md#L31-L31](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L31-L31), [README.md#L33-L33](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L33-L33), [README.md#L29-L29](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L29-L29) (`clm_1a9caae5c6a814b2ddf1003b0741221df7c49f37936b0d1bef9b30ae94556021`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI provides an 'inspect-repo' command taking a repository path and an optional --branch-name flag; without a branch it uses the current branch and analyzes the latest commit. -- evidence: [README.md#L45-L45](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L45-L45), [README.md#L41-L41](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L41-L41), [README.md#L43-L43](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L43-L43) (`clm_726c396279c7108e8fe733963f2dfd93807afe634aad74501443b352d5e8d02e`)
- [observation/documented] The 'build-index' command generates an indexed database of commit insights for a given Git repository. -- evidence: [README.md#L52-L52](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L52-L52), [README.md#L54-L54](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L54-L54) (`clm_30db35620469a1b2153e76249e09c65a4e4081e83c651af3fe46796bf1c92f97`)
- [observation/documented] The 'search' command accepts a query plus optional --author, --file, --start-date, and --end-date filters (dates in YYYY-MM-DD format) to find relevant commits. -- evidence: [README.md#L60-L60](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L60-L60), [README.md#L62-L66](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L62-L66) (`clm_f266fbf407a1e954f97e1043b4288a7617ef651021341bf16fb41d4fae4ee83b`)
- [observation/documented] A 'suggest_commit_message' command retrieves currently staged changes, formats them commit-like, and uses the LLM to suggest a commit message shown in console output. -- evidence: [README.md#L76-L76](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L76-L76), [README.md#L80-L80](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L80-L80), [README.md#L78-L78](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L78-L78), [README.md#L82-L82](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L82-L82) (`clm_cfc8d2ffb7b8a827046c85f618bb19433e0e726cacbfca58896e9b28b4b60371`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool requires Python 3.11 or higher and is installable via pip as the 'icodes' package. -- evidence: [README.md#L19-L19](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L19-L19), [README.md#L17-L17](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L17-L17) (`clm_30298d82f98ebae25a8a13a4740d32a4b877bb2ef03e651f55bac1adeaca8005`)
- [observation/documented] The only supported LLM backend is OpenAI; the OPENAI_API_KEY environment variable must be exported, and DEFAULT_MODEL selects the GPT model (default gpt-3.5-turbo). -- evidence: [README.md#L21-L21](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L21-L21) (`clm_a371e45e86c7ab740d6c9e2103aa026a480e05b6c95fac133ce82df6d1b81b1b`)

## limitations (1 claim(s))

- [observation/documented] Semantic search and a web-based UI are listed as 'coming soon' features, indicating they are not yet available in the current tool. -- evidence: [README.md#L8-L13](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L8-L13) (`clm_b0bcd6e08240884581039f57c28a44bffac53308425deac55f0d83ac28df2bf3`)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers seeking to understand and navigate codebases by analyzing commit history, trends, and code evolution patterns. -- evidence: [README.md#L4-L4](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L4-L4), [README.md#L8-L13](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L8-L13) (`clm_b610db0cc560b83c7711ff8d56320834666d5b40946e53589cfcfbf8bc4b8865`)

