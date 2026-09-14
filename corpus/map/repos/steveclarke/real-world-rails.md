# steveclarke/real-world-rails

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 45eb4c732feb @ 85e7a6bf1719cd2c

## Summary (orientation draft, not independently verified)

This repository is a curated aggregation of 200+ open source Rails apps and engines as git submodules, intended as a learning and AI-agent research corpus. Evidence is mostly README documentation describing setup scripts, update automation, contribution criteria, and an included agent skill. Evidence coverage: 157 of 275 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project aggregates over 200 active, open source Rails apps and engines in one repository for developers to learn from. -- evidence: [README.md#L7-L7](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L7-L7)
  - [observation/documented] It is described as an actively maintained continuation of eliotsykes/real-world-rails. -- evidence: [README.md#L5-L5](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The full list of included apps and engines with descriptions lives in repos.md, which lists entries such as Discourse, Mastodon, GitLab CE, and Canvas LMS with links and short descriptions. -- evidence: [README.md#L9-L9](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L9-L9), [repos.md#L228-L229](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/repos.md#L228-L229), [repos.md#L475-L476](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/repos.md#L475-L476), [repos.md#L128-L129](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/repos.md#L128-L129)
- design-choices (1 claim(s)):
  - [observation/documented] The project's stated motivation is that aggregating production codebases in one directory makes cross-app pattern research dramatically more useful for AI coding agents than manual grep or custom scripts. -- evidence: [README.md#L23-L23](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L23-L23), [README.md#L13-L13](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L13-L13), [README.md#L15-L15](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L15-L15)
- workflows (6 claim(s)):
  - [observation/documented] Running bin/setup clones all 200+ repositories as git submodules, using roughly 10 GB of disk; bin/setup --full fetches complete git history at about 29 GB. -- evidence: [README.md#L35-L36](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L35-L36)
  - [observation/documented] Provided scripts include bin/setup (with --full and --reset flags), bin/update, bin/status, bin/add for adding apps by GitHub URL, and bin/verify which requires the gh CLI. -- evidence: [README.md#L59-L65](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L59-L65)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repo ships a /real-world-rails skill for AI coding agents, installable via npx skills add steveclarke/real-world-rails, that teaches agents to search across all included codebases. -- evidence: [README.md#L92-L94](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L92-L94), [README.md#L88-L88](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L88-L88)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README points to related collections including Real World Nuxt, Real World Ruby Apps, Real World Sinatra, and Real World Django. -- evidence: [README.md#L100-L103](https://github.com/steveclarke/real-world-rails/blob/45eb4c732febbfb7d6045c68036403fd29f2c368/README.md#L100-L103)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](real-world-rails.detail.md) for every claim.)

Metadata and full claim list: [full detail](real-world-rails.detail.md)
Human notes ([notes](real-world-rails.notes.md), never overwritten by build)

[Back to map index](../../index.md)
