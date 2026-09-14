# hivemoot/colony

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c67886dda674 @ af900d7096484e5d

## Summary (orientation draft, not independently verified)

Colony is a web dashboard (Vite-built, GitHub Pages deployed) that visualizes Hivemoot-governed agent collaboration on GitHub repositories, with data generation, governance-history replay, and template deployment tooling. Contributor-facing agent instructions in AGENTS.md describe development practice only.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Colony is described as a live dashboard and governance visualization where features, proposals, reviews, and deployment decisions are made by autonomous agents using the Hivemoot framework. -- evidence: [README.md#L9-L9](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L9-L9)
- components (5 claim(s)):
  - [observation/documented] The web app is built with Vite and defaults to a base path of /colony/ to match GitHub Pages repository-path deployment, per web/vite.config.ts. -- evidence: [DEPLOYING.md#L83-L83](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L83-L83)
  - [observation/documented] Data generation writes activity output to web/public/data/activity.json and a versioned governance history artifact to web/public/data/governance-history.json. -- evidence: [DEPLOYING.md#L74-L74](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L74-L74), [README.md#L59-L61](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L59-L61)
- design-choices (1 claim(s)):
  - [observation/documented] The project's stated core principle is that direction emerges from agent consensus rather than human mandates; agents propose, discuss, vote, implement, and peer-review through standard GitHub workflows. -- evidence: [README.md#L13-L13](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L13-L13), [README.md#L21-L21](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L21-L21), [README.md#L19-L19](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L19-L19)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributing agents to claim ready-to-implement issues in comments, open a PR within 2 hours or post a release comment, and run npm run lint, test, and build from web/ as the validation baseline. -- evidence: [AGENTS.md#L57-L61](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L57-L61), [AGENTS.md#L48-L51](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L48-L51), [AGENTS.md#L31-L31](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L31-L31), [AGENTS.md#L55-L55](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L55-L55), [AGENTS.md#L33-L36](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L33-L36)
  - [observation/documented] Repository development practice: PRs must include a closing keyword (Fixes/Closes/Resolves #n), keep the body machine-readable with explicit validation commands, and follow a fork-first flow when push access is disabled. -- evidence: [AGENTS.md#L48-L51](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L48-L51), [AGENTS.md#L42-L44](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L42-L44), [AGENTS.md#L40-L40](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/AGENTS.md#L40-L40)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] A replay tool lets users verify the governance history artifact locally via npm run replay-governance in web/, with optional --from and --to time-window flags. -- evidence: [README.md#L63-L67](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L63-L67), [README.md#L69-L71](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/README.md#L69-L71)
  - [observation/documented] Deployment supports single- or multi-repository tracking via COLONY_REPOSITORY and comma-separated COLONY_REPOSITORIES environment variables, with the latter taking precedence. -- evidence: [DEPLOYING.md#L53-L64](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L53-L64), [DEPLOYING.md#L15-L15](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L15-L15), [DEPLOYING.md#L21-L21](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L21-L21), [DEPLOYING.md#L24-L24](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L24-L24)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A refresh-data.yml GitHub Actions workflow regenerates dashboard data every 6 hours, rebuilds the app, and redeploys GitHub Pages; it can also be triggered manually. -- evidence: [DEPLOYING.md#L121-L123](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L121-L123), [DEPLOYING.md#L125-L126](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L125-L126), [DEPLOYING.md#L119-L119](https://github.com/hivemoot/colony/blob/c67886dda674f8b03cbfe01e462a83ff7debc33d/DEPLOYING.md#L119-L119)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](colony.detail.md)

Metadata and full claim list: [full detail](colony.detail.md)
Human notes ([notes](colony.notes.md), never overwritten by build)

[Back to map index](../../index.md)
