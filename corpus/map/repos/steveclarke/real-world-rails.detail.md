# steveclarke/real-world-rails -- full detail

[Back to orientation](real-world-rails.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/steveclarke/real-world-rails/45eb4c732febbfb7d6045c68036403fd29f2c368/85e7a6bf1719cd2c.json](../../../wiki/dossiers/steveclarke/real-world-rails/45eb4c732febbfb7d6045c68036403fd29f2c368/85e7a6bf1719cd2c.json)

## specifications (2 claim(s))

- [observation/documented] The project aggregates over 200 active, open source Rails apps and engines in one repository for developers to learn from. -- evidence: [README.md#L7-L7](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L7-L7) (`clm_3111abc15676e846333aa1b8e37670ef148377248af2bcd5c6c523da314c7b89`)
- [observation/documented] It is described as an actively maintained continuation of eliotsykes/real-world-rails. -- evidence: [README.md#L5-L5](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L5-L5) (`clm_b2792dc9c28d2b7d2ef9b9c1cb89c889f0dc72432f316fe49a612c0e23693b60`)

## components (1 claim(s))

- [observation/documented] The full list of included apps and engines with descriptions lives in repos.md, which lists entries such as Discourse, Mastodon, GitLab CE, and Canvas LMS with links and short descriptions. -- evidence: [README.md#L9-L9](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L9-L9), [repos.md#L228-L229](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/repos.md#L228-L229), [repos.md#L475-L476](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/repos.md#L475-L476), [repos.md#L128-L129](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/repos.md#L128-L129) (`clm_493c0713e4078726bbed7dbd1f75914fdc4dcbc37bfd43ad037bb50a68a56226`)

## design-choices (1 claim(s))

- [observation/documented] The project's stated motivation is that aggregating production codebases in one directory makes cross-app pattern research dramatically more useful for AI coding agents than manual grep or custom scripts. -- evidence: [README.md#L23-L23](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L23-L23), [README.md#L13-L13](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L13-L13), [README.md#L15-L15](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L15-L15) (`clm_8d1eb2dc0ec8d91044c7c85a3755392bcb507b0c13abfa565b2bccd776bafbdf`)

## workflows (6 claim(s))

- [observation/documented] Running bin/setup clones all 200+ repositories as git submodules, using roughly 10 GB of disk; bin/setup --full fetches complete git history at about 29 GB. -- evidence: [README.md#L35-L36](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L35-L36) (`clm_2fd128af5415c7e715618e7b7afab17d2ecd27b47f6488b5bb5401fe5772f135`)
- [observation/documented] Provided scripts include bin/setup (with --full and --reset flags), bin/update, bin/status, bin/add for adding apps by GitHub URL, and bin/verify which requires the gh CLI. -- evidence: [README.md#L59-L65](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L59-L65) (`clm_174fa0a8e1a842a417ca147f719565003602fa21b7d77d74e2b35bd3e7d71fed`)
- [observation/documented] Submodules are updated automatically by a weekly GitHub Action that opens a PR; after merging, users pull and run git submodule update, or run bin/update for immediate updates. -- evidence: [README.md#L50-L53](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L50-L53), [README.md#L48-L48](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L48-L48), [README.md#L55-L55](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L55-L55) (`clm_a47ca7bdb9492ee21a6444950553ca90cb6f3c3d7f92e515d34973013e6a9890`)
- [observation/documented] Setup requires git-lfs to be installed, and getting started consists of cloning the repo and running bin/setup. -- evidence: [README.md#L38-L38](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L38-L38), [README.md#L40-L44](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L40-L44) (`clm_0fb483d109a6d3668ab4c3cac45e750fcf87df99406d9ba22054c4d49b978b08`)
- [observation/documented] The analyses/ directory is git-ignored so users can store their own research notes without them being committed or appearing in pull requests. -- evidence: [README.md#L27-L27](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L27-L27), [README.md#L29-L31](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L29-L31) (`clm_61492b0dd6dd118f9f2b57464ef53adbfaf1b2aab1b5d998e08ce2e8120fe346`)
- [observation/documented] Repository development practice: contributions are accepted either by opening an issue with a GitHub URL or by submitting a PR after running bin/add; candidate apps must be open source, Rails-based, actively maintained or high quality, and real-world rather than demos. -- evidence: [README.md#L69-L69](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L69-L69), [README.md#L80-L84](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L80-L84), [README.md#L73-L74](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L73-L74), [README.md#L71-L71](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L71-L71) (`clm_0c1e8b1727b2369bea28ee665b8c5c46397b0549360167ac6975f26838ac72ec`)

## skills-patterns (1 claim(s))

- [observation/documented] The repo ships a /real-world-rails skill for AI coding agents, installable via npx skills add steveclarke/real-world-rails, that teaches agents to search across all included codebases. -- evidence: [README.md#L92-L94](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L92-L94), [README.md#L88-L88](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L88-L88) (`clm_28aed2305aabe5fcec9a78e2b2b544b3af0fb80f64ffc429cc521a71d0daba97`)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README points to related collections including Real World Nuxt, Real World Ruby Apps, Real World Sinatra, and Real World Django. -- evidence: [README.md#L100-L103](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L100-L103) (`clm_1adbb1af3c774d72309311ac5268568cafc9d046fe9fdb7e857bbd21449a9931`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

