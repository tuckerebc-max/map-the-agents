# gszhangwei/open-spdd -- full detail

[Back to orientation](open-spdd.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gszhangwei/open-spdd/59669ac18c1c0bdee76b780771ac51567a73d52c/6eae32fd657aa164.json](../../../wiki/dossiers/gszhangwei/open-spdd/59669ac18c1c0bdee76b780771ac51567a73d52c/6eae32fd657aa164.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The tool auto-detects the user's AI coding environment and writes command templates into tool-specific directories, e.g. .cursor/commands/, .claude/commands/, .github/copilot-prompts/, and .agents/skills/ for Codex. -- evidence: [README.md#L262-L269](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L262-L269), [README.md#L96-L100](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L96-L100) (`clm_25d241e423f3b63ba40541ead00be523410d682c2b5c115cdd2352028b9c3f3e`)

## design-choices (4 claim(s))

- [observation/documented] The methodology centers on a 7-dimension REASONS Canvas (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards) treating prompts as executable design contracts rather than task lists. -- evidence: [README.md#L17-L17](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L17-L17), [README.md#L38-L52](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L38-L52), [README.md#L32-L32](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L32-L32), [README.md#L36-L36](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L36-L36) (`clm_555964487ad8ec88bd7062d648c2a9ba3ccd90b821ce1700b27bfc8b77570758`)
- [observation/documented] All templates are embedded in a single Go binary via Go's embed directive, and the tool provides an interactive terminal UI for command selection. -- evidence: [README.md#L96-L100](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L96-L100) (`clm_e9bf170ad00901d1aa623bf9829e79978d02481c55518939be917b03ba767ad3`)
- [observation/documented] For Codex, skills are generated as project-scoped SKILL.md bundles under .agents/skills/ with implicit invocation disabled by default, opt-in via --allow-implicit. -- evidence: [README.md#L275-L275](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L275-L275) (`clm_9f20e03f6131c60c6754ed4ad5fa7c154cf294cbd5744b7463ef52ac821f0601`)
- [observation/documented] Generated OpenCode command files intentionally omit frontmatter name fields to avoid command alias conflicts in OpenCode. -- evidence: [README.md#L271-L271](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L271-L271) (`clm_26d340e4a7e8a083ae281fa2dff787df5615b1e54c08d11430dcb41fa6fa3dee`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run tests with go test ./tests/..., with verbose and per-module variants like ./tests/detector/... and ./tests/templates/..., and can build from source with go build ./cmd/openspdd. -- evidence: [README.md#L384-L389](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L384-L389), [README.md#L398-L398](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L398-L398), [README.md#L401-L403](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L401-L403), [README.md#L395-L395](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L395-L395) (`clm_350faa9514b4a1dee56052eb15efa092fbe539cd5b85bb8f5d3c1ea13c918caf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The uninstall command detects the install method (Homebrew or go install), prints a plan, requires confirmation by default, and refuses to act on unclassifiable installs such as manually copied binaries. -- evidence: [README.md#L150-L150](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L150-L150), [README.md#L163-L163](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L163-L163) (`clm_2403e05eb1cd79ad1144e1ba98887f4d940741d142920e26c49898d8fb42d697`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool is written in Go and installable via Homebrew (gszhangwei/tools/openspdd), go install from cmd/openspdd, a scripts/install.sh script, or prebuilt GitHub Releases binaries. -- evidence: [README.md#L384-L389](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L384-L389), [README.md#L106-L108](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L106-L108), [README.md#L119-L121](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L119-L121), [README.md#L137-L137](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L137-L137), [README.md#L146-L146](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L146-L146) (`clm_cd3f4e9d6e9e1327e6093b81d24c929a2a4ae408cb03ab52303263caace958ac`)

## limitations (1 claim(s))

- [observation/documented] On some Codex versions, skills from untrusted projects are silently ignored; users must mark the project trusted in ~/.codex/config.toml or restart Codex if skills do not appear. -- evidence: [README.md#L275-L275](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L275-L275) (`clm_d47d422b246e25bd9cb9122ccffcdc1e04aef697f6039254b7ee83c6b8fae3f3`)

## relevance (1 claim(s))

- [observation/documented] The project targets AI-assisted business development where design-intent drift causes rework, recommending itself for enterprise features, team collaboration, and complex refactoring, but not for one-off scripts. -- evidence: [docs/design-philosophy.md#L3-L3](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/docs/design-philosophy.md#L3-L3), [docs/design-philosophy.md#L15-L15](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/docs/design-philosophy.md#L15-L15), [README.md#L373-L380](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L373-L380) (`clm_ecd7c5f79fef260c23ef913f74b0c30ef6cf0c20b7f75f8a4f49ea47f7ac0031`)

