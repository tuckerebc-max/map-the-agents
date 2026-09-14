# get-convex/chef

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d8a6cb6a6f22 @ 3abf79f07186783f

## Summary (orientation draft, not independently verified)

Chef is an AI full-stack web app builder built on Convex, forked from bolt.diy, with a hosted webapp and local-run option. Evidence covers its architecture, auth model, and contributor/release workflows; no code-level behavior is directly inspected.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Chef is described as an AI app builder that creates full-stack web apps with a built-in database, zero-config auth, file uploads, real-time UIs, and background workflows. -- evidence: [README.md#L8-L9](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L8-L9)
- components (2 claim(s)):
  - [observation/documented] The chef-agent directory handles the agentic loop by injecting system prompts, defining tools, and calling model providers. -- evidence: [README.md#L112-L112](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L112-L112)
  - [observation/documented] The repository includes a template directory used as the starting point for all Chef projects, and a convex directory storing chats and user metadata. -- evidence: [README.md#L116-L116](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L116-L116), [README.md#L118-L118](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L118-L118)
- design-choices (2 claim(s)):
  - [observation/documented] Chef's capabilities come from being built on Convex, whose APIs the README describes as an ideal fit for code generation. -- evidence: [README.md#L11-L11](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L11-L11)
  - [observation/documented] The project is a fork of the stable branch of bolt.diy. -- evidence: [README.md#L17-L17](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L17-L17)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: local setup uses nvm, pnpm, a VITE_CONVEX_URL placeholder, and 'npx convex dev --once' to provision a Convex project, then 'pnpm run dev' plus 'npx convex dev'. -- evidence: [README.md#L50-L57](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L50-L57), [README.md#L97-L98](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L97-L98), [README.md#L93-L94](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L93-L94)
  - [observation/documented] Repository development practice: PRs target main; a commit queue blocks on tests, formatting, lints, and typechecking via pnpm scripts, and the repo has very few tests and no e2e tests. -- evidence: [DEVELOPMENT.md#L7-L9](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L7-L9), [DEVELOPMENT.md#L64-L64](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L64-L64), [DEVELOPMENT.md#L54-L56](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L54-L56)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Chef is offered as a hosted webapp at chef.convex.dev with a free tier, and can also be run locally following README instructions. -- evidence: [README.md#L23-L24](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L23-L24)
  - [observation/documented] A chefshot directory defines a CLI interface for interacting with the Chef webapp. -- evidence: [README.md#L114-L114](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L114-L114)
- memory-state (1 claim(s)):
  - [inference/documented] Chef appears to use a WebContainer-style environment: a documented debug global exposes 'chefWebContainer' as the unix-ish container where tooling and generated code run. -- evidence: [DEVELOPMENT.md#L130-L135](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L130-L135)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Chef ships with an authentication configuration tied to Convex's internal control plane for user accounts; forks for production must replace it with their own auth. -- evidence: [README.md#L29-L29](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L29-L29), [README.md#L26-L27](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L26-L27)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](chef.detail.md)

Metadata and full claim list: [full detail](chef.detail.md)
Human notes ([notes](chef.notes.md), never overwritten by build)

[Back to map index](../../index.md)
