# andrewyng/context-hub -- full detail

[Back to orientation](context-hub.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/andrewyng/context-hub/67dcbeb2eb42c808549f08397920ad58be7c2206/1791801ae21ba245.json](../../../wiki/dossiers/andrewyng/context-hub/67dcbeb2eb42c808549f08397920ad58be7c2206/1791801ae21ba245.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product is an npm-distributed CLI requiring Node.js >= 18, installed globally as @aisuite/chub. -- evidence: [README.md#L5-L7](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L5-L7), [README.md#L11-L15](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L11-L15) (`clm_8beffb885d0430f3af8f61df56c218d13dea62acc9794a8099b920d9810a6d8f`)

## design-choices (2 claim(s))

- [observation/documented] Annotations are local notes persisted across sessions and re-injected on future fetches only with --with-annotations, which is off by default, with contents treated as untrusted input. -- evidence: [README.md#L91-L91](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L91-L91), [README.md#L68-L68](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L68-L68) (`clm_ea370d5d003fee4a5b2ab5de8e0636c9ac0ee741992678599ef1d8231aa34b84`)
- [observation/documented] Feedback is up/down ratings sent to doc authors so content improves for everyone, separate from local annotations. -- evidence: [README.md#L38-L38](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L38-L38), [README.md#L70-L70](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L70-L70) (`clm_7a6716dcba05b3390693224fe5a4befc9aa70c5bde4f88c309b9686b1baf7067`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors fork from main, add/update tests, run 'cd cli && npm test', validate with 'chub build content/ --validate-only', then submit a pull request. -- evidence: [CONTRIBUTING.md#L40-L45](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L40-L45) (`clm_75bada682e3c02b1d3c1799549b4228f0a4cee047384e838d16f3b98b2c01da5`)
- [observation/documented] Repository development practice: tests run via npm test, test:watch, and test:coverage inside the cli directory, using Vitest unit tests plus e2e/integration tests. -- evidence: [CONTRIBUTING.md#L29-L34](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L29-L34), [CONTRIBUTING.md#L56-L73](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L56-L73) (`clm_daa641780112880aa40395ed10bd7f94a67f5004ed2764a36028560de3a3a853`)
- [observation/documented] Repository development practice: docs are contributed as <author>/docs/<name>/DOC.md with YAML frontmatter (name, description, languages, versions, tags, updated-on) and optional references/ files; skills follow a similar SKILL.md pattern. -- evidence: [CONTRIBUTING.md#L98-L99](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L98-L99), [CONTRIBUTING.md#L103-L104](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L103-L104), [CONTRIBUTING.md#L84-L94](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L84-L94), [CONTRIBUTING.md#L81-L82](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L81-L82), [CONTRIBUTING.md#L106-L114](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L106-L114) (`clm_7f8944ac89337ced4a0e703faf602ddc92fe82a7ababae91e71d35ca126df6b7`)
- [observation/documented] Repository development practice: code style mandates ES modules, no build step, minimal dependencies preferring Node built-ins, and every command supporting --json output. -- evidence: [CONTRIBUTING.md#L49-L52](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/CONTRIBUTING.md#L49-L52) (`clm_4495b0f0d6f599d45e2e0d2e66b278c7eee21af0e6c4c0d5c8b735ff6d35fd7d`)

## skills-patterns (1 claim(s))

- [observation/documented] Agents can use Chub via a SKILL.md agent skill; for Claude Code the README suggests placing it in ~/.claude/skills/get-api-docs. -- evidence: [README.md#L19-L19](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L19-L19) (`clm_cbf258251a6c39233fdad18cb3adff84bd46f3a411329ebde6d8445eeb4ecb74`)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands including chub search [query], chub get <id> [--lang py|js], chub annotate (note, --clear, --list), and chub feedback <id> <up|down>. -- evidence: [README.md#L53-L60](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L53-L60) (`clm_ddf7bebf19103cf7014976772071eeaffe604f74483163030d7c717d51b26995`)
- [observation/documented] Fetches support language variants via --lang (e.g. py or js) for the same doc ID such as openai/chat. -- evidence: [README.md#L44-L47](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L44-L47) (`clm_e1a200125d6287a726b95e49e67d77bf0706484d7044ff58b506f5e74d1b348b`)
- [observation/documented] Docs can have multiple reference files; --file fetches specific references and --full fetches everything, aimed at avoiding wasted tokens. -- evidence: [README.md#L87-L87](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L87-L87) (`clm_2aff4e41def7e685b8214d11777e2457e9bb71ffa196269a587af06a507e0703`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is MIT licensed and content is plain markdown with YAML frontmatter maintained in the repo. -- evidence: [README.md#L101-L101](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L101-L101), [README.md#L95-L95](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/README.md#L95-L95) (`clm_ca0862d3589d7febbe2cdfebec82f61c6aa66f02e0d1e1d97fb728d475802d31`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

