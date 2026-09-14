# nisarg38/claude-northstar -- full detail

[Back to orientation](claude-northstar.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nisarg38/claude-northstar/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/4cc9aa49933b76d8.json](../../../wiki/dossiers/nisarg38/claude-northstar/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/4cc9aa49933b76d8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Installation creates a .claude/harness directory containing north-star.md, project-state.json, decisions.md, progress-log.md, and five sub-agent prompt templates under prompts/. -- evidence: [README.md#L106-L118](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L106-L118) (`clm_840476d217666629e4660c4177c51349692af76b7391bcd0ca572a72a1c4013f`)

## design-choices (4 claim(s))

- [observation/documented] The framework positions the CLI agent session as a Tech Lead that understands the vision, plans milestones, coordinates sub-agents, and asks only strategic questions. -- evidence: [README.md#L74-L79](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L74-L79) (`clm_b30c620ec388e595fedae723fde60d91f722efc2f7ed80a15e5a61ef880f0f11`)
- [observation/documented] The autonomous work loop is documented as a repeating cycle of ANALYZE state, PLAN next work, EXECUTE, and EVALUATE progress. -- evidence: [README.md#L93-L100](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L93-L100) (`clm_76d55ba738aaa858b336b3a824f8ae5aecb79528860a7d41789693078dd38706`)
- [observation/documented] The agent interrupts the user only for major architecture decisions, ambiguous requirements, and milestone reviews, and deliberately avoids asking about routine task completions or minor implementation choices. -- evidence: [README.md#L170-L172](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L170-L172), [README.md#L168-L168](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L168-L168), [README.md#L174-L177](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L174-L177) (`clm_8382d046c07f4cf9219170e997a6080cdee3c5ca4a488554d010763d68d115bc`)
- [observation/documented] The framework follows a quality pipeline before merging significant work: developer completes, QA verifies, reviewer approves, then merge. -- evidence: [README.md#L157-L164](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L157-L164), [CLAUDE.md#L86-L89](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L86-L89) (`clm_8319bbe8444eed661041f438f4289e3f9c99dca86db0366f4c13462cffe8b824`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the installed CLAUDE.md instructs the agent to always read north-star.md, project-state.json, and decisions.md at session start, then either capture a new vision or report state and work autonomously. -- evidence: [CLAUDE.md#L29-L33](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L29-L33), [CLAUDE.md#L22-L27](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L22-L27), [CLAUDE.md#L13-L13](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L13-L13), [CLAUDE.md#L15-L20](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L15-L20) (`clm_94dd46b257a455c049d503af548b56873f660ab78fa5059919e2b0784a4d302d`)
- [observation/documented] Repository development practice: sub-agents are spawned via the Task tool with subagent_type 'general-purpose', using prompt files from .claude/harness/prompts/ with injected context. -- evidence: [CLAUDE.md#L49-L55](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L49-L55), [CLAUDE.md#L57-L60](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L57-L60), [CLAUDE.md#L47-L47](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L47-L47) (`clm_d3830b80a00ff9cc1f3082bf3417517cfed6082a6a80ecc059e759c0e9355253`)
- [observation/documented] Repository development practice: state files have defined update triggers — project-state.json after each session, decisions.md on technical choices, progress-log.md at session end, and north-star.md when the vision changes. -- evidence: [CLAUDE.md#L77-L82](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L77-L82) (`clm_28b59b57b6991d23b35e89f2e1ac89a29d6282ada921bfa5c2ebccf5281c64e5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The tool is distributed as the npm package claude-northstar and operated via npx commands: init, status, and uninstall. -- evidence: [README.md#L32-L34](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L32-L34), [README.md#L43-L44](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L43-L44), [README.md#L40-L40](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L40-L40), [README.md#L5-L6](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L5-L6) (`clm_936ed3a82a06a41a77eace97728745e4e9c0f48f582dfcdf944cc818d146e314`)
- [observation/documented] An alternative install path fetches an install.sh script from the GitHub repository via curl and pipes it to bash. -- evidence: [README.md#L48-L50](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L48-L50) (`clm_e5234c4eaa048e769a5b9fbef00c1ecbafab0988e769af2338a00bed5d20ffae`)

## memory-state (1 claim(s))

- [observation/documented] project-state.json persists milestones with status and progress values, the current focus, and identified gaps, enabling sessions to resume when the user says 'continue'. -- evidence: [README.md#L157-L164](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L157-L164), [README.md#L144-L153](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L144-L153), [README.md#L142-L142](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L142-L142), [README.md#L68-L68](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L68-L68) (`clm_f7efcf77a459a96486140b592a859b2f8667401f121077f92669dee1a7756582`)

## orchestration (1 claim(s))

- [observation/documented] Work is delegated to five sub-agent roles: Product Researcher, Strategist, Developer, QA, and Reviewer, each used at a specific phase such as planning, implementation, or pre-merge review. -- evidence: [README.md#L83-L89](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L83-L89) (`clm_7471c36dc24cb073ed61562de3e22a9cd3b181085747e1ef444a1ab348d31733`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Jujutsu (jj) is an optional companion tool: North Star works with plain git, while jj enables isolated workspaces for parallel tasks, conflicts-as-data, and rollback via an operation log. -- evidence: [README.md#L193-L196](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L193-L196), [README.md#L183-L183](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L183-L183) (`clm_0303ccd53b17b04ee65988a25bfb67faec8d26edbc1507b5ff18f18412f7beda`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets CLI coding agents such as Claude Code and OpenCode, aiming to shift them from task-by-task execution to autonomous progress toward a shared project vision. -- evidence: [README.md#L10-L10](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L10-L10), [README.md#L3-L3](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L3-L3), [README.md#L23-L26](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L23-L26) (`clm_0489701e42f73cd95bc2247a10a506732746d97f0d91347cd1ed3f2769e9bf16`)

