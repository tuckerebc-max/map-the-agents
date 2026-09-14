# kirodotdev/kiro -- full detail

[Back to orientation](kiro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kirodotdev/kiro/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/0f0f944d18d31554.json](../../../wiki/dossiers/kirodotdev/kiro/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/0f0f944d18d31554.json)

## specifications (1 claim(s))

- [observation/documented] Kiro's Specs feature structures requirements, design decisions, and implementation tasks, with a Requirements Analysis step to find contradictions and gaps before coding. -- evidence: [README.md#L41-L47](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L41-L47) (`clm_69161c6d445fcf7b326fb6284ada8a2fbd7e30a5be43f1b8ab15edbda876ffb8`)

## components (1 claim(s))

- [observation/documented] The Crew surface is described as a persistent open-source development workspace with memory, scheduling, and multi-channel access. -- evidence: [README.md#L31-L37](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L31-L37) (`clm_35057af0d1e9ced09caa75eb53973e395777f880c2a9aade3d4aa0d20a5bdd9b`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] The repository hosts automation for triaging and managing its own GitHub issues, while the Kiro product source code is not hosted here. -- evidence: [README.md#L19-L19](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L19-L19) (`clm_5cb4c9cb06f700171ce5aed17452974fe0cadbc098fe0839848ae12fb7b914aa`)
- [observation/documented] Maintainers are advised to apply the pending-response label consistently, monitor workflow logs, and adjust the 7-day threshold if their community needs more time. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L460-L462](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L460-L462), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L464-L466](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L464-L466), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L452-L454](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L452-L454) (`clm_ee06d390ad5670ba67ec9c13df0c7243a56fb20b7cd46603863b1177c763d672`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Kiro is described as an agentic AI development platform spanning IDE, CLI, Web, Mobile, and Crew surfaces, powered by a unified agent harness. -- evidence: [README.md#L29-L29](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L29-L29), [README.md#L7-L9](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L7-L9) (`clm_54ebdb959a882791efa8c287db229af3d98a3e0b53dbd5ec3bd960649bf951a1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (4 claim(s))

- [observation/documented] The stale-issue workflow runs daily at midnight UTC via cron and can also be triggered manually with gh workflow run close-stale.yml. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L23-L25](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L23-L25), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L10-L13](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L10-L13), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L27-L30](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L27-L30) (`clm_ecb18d162b7f86cdc6bfb6f072b483b1e58a31297032a3f0a9eeac1d10baa743`)
- [observation/documented] The workflow targets open issues labeled 'pending-response', closes those inactive for 7 or more days, and posts a closing comment explaining the closure and how to reopen. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L5-L5](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L5-L5), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L283-L290](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L283-L290), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L251-L253](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L251-L253), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L292-L292](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L292-L292) (`clm_57b45cd9a6217209dfe2ce39625ddc8a5b19034e1ace0ffc1b015d4a9c2aa484`)
- [observation/documented] Inactivity is measured from the more recent of the label-application date and the last activity date, where activity means new comments or any label change. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L217-L221](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L217-L221), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L205-L209](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L205-L209), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L194-L196](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L194-L196) (`clm_c42d55e89d7823ad82e8a520b89fc10ece52924e5c99f33138d2d74afe7cadc9`)
- [observation/documented] GitHub API calls use retry with exponential backoff (up to 3 retries at 1s, 2s, 4s), and per-issue errors are logged without stopping processing of remaining issues. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L486-L490](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L486-L490), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L492-L495](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L492-L495), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L508-L511](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L508-L511), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L499-L506](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L499-L506) (`clm_e7746c93cde4593477bd3b969127e422c869351a8a81c0e267723c1c9878d026`)

## tools-permissions (2 claim(s))

- [observation/documented] The product includes a permissions feature for setting agent access boundaries, plus Hooks, Powers, and MCP for tools and external integrations. -- evidence: [README.md#L41-L47](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L41-L47) (`clm_a30f4e211afb89c065727f54ec9eb679192cd59d841ce7b5ff3a1901a9c3436a`)
- [observation/documented] The stale-issue workflow requires GitHub permissions of issues:write (close issues, post comments) and contents:read (access scripts). -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L515-L519](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L515-L519), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L521-L523](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L521-L523) (`clm_1de13b58669272bd4649e9379411f996a9fd33a9e646ac37cf4eec1f54402ec4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The automation appears to be TypeScript scripts using the Octokit GitHub client, built with npm, based on code examples and build instructions in the docs. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L341-L345](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L341-L345), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L104-L116](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L104-L116), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L336-L339](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L336-L339), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L59-L67](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L59-L67) (`clm_d9b249c073a96104d8ab56ccb5bf331eb06f0d958c13ef67240c5060498ad30a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

