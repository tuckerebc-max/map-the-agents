---
access: public
aliases: []
claim_ids:
- clm_0303ccd53b17b04ee65988a25bfb67faec8d26edbc1507b5ff18f18412f7beda
- clm_0489701e42f73cd95bc2247a10a506732746d97f0d91347cd1ed3f2769e9bf16
- clm_7471c36dc24cb073ed61562de3e22a9cd3b181085747e1ef444a1ab348d31733
- clm_76d55ba738aaa858b336b3a824f8ae5aecb79528860a7d41789693078dd38706
- clm_8319bbe8444eed661041f438f4289e3f9c99dca86db0366f4c13462cffe8b824
- clm_8382d046c07f4cf9219170e997a6080cdee3c5ca4a488554d010763d68d115bc
- clm_840476d217666629e4660c4177c51349692af76b7391bcd0ca572a72a1c4013f
- clm_936ed3a82a06a41a77eace97728745e4e9c0f48f582dfcdf944cc818d146e314
- clm_b30c620ec388e595fedae723fde60d91f722efc2f7ed80a15e5a61ef880f0f11
- clm_e5234c4eaa048e769a5b9fbef00c1ecbafab0988e769af2338a00bed5d20ffae
- clm_f7efcf77a459a96486140b592a859b2f8667401f121077f92669dee1a7756582
maturity: draft
page_id: pg_fd090bbd0fca5d8f9c80568a11388372
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e49c75f431395e57b98602d9a3568526
title: Nisarg38/claude-northstar/README.md @ 43d89d5aba90
updated_at: '2026-09-14T04:13:10Z'
---

# Nisarg38/claude-northstar/README.md @ 43d89d5aba90

<!-- rcw:begin owner=source:src_e49c75f431395e57b98602d9a3568526 block=evidence -->
- Jujutsu (jj) is an optional companion tool: North Star works with plain git, while jj enables isolated workspaces for parallel tasks, conflicts-as-data, and rollback via an operation log. [@claim:clm_0303ccd53b17b04ee65988a25bfb67faec8d26edbc1507b5ff18f18412f7beda]
- The project targets CLI coding agents such as Claude Code and OpenCode, aiming to shift them from task-by-task execution to autonomous progress toward a shared project vision. [@claim:clm_0489701e42f73cd95bc2247a10a506732746d97f0d91347cd1ed3f2769e9bf16]
- Work is delegated to five sub-agent roles: Product Researcher, Strategist, Developer, QA, and Reviewer, each used at a specific phase such as planning, implementation, or pre-merge review. [@claim:clm_7471c36dc24cb073ed61562de3e22a9cd3b181085747e1ef444a1ab348d31733]
- The autonomous work loop is documented as a repeating cycle of ANALYZE state, PLAN next work, EXECUTE, and EVALUATE progress. [@claim:clm_76d55ba738aaa858b336b3a824f8ae5aecb79528860a7d41789693078dd38706]
- The framework follows a quality pipeline before merging significant work: developer completes, QA verifies, reviewer approves, then merge. [@claim:clm_8319bbe8444eed661041f438f4289e3f9c99dca86db0366f4c13462cffe8b824]
- The agent interrupts the user only for major architecture decisions, ambiguous requirements, and milestone reviews, and deliberately avoids asking about routine task completions or minor implementation choices. [@claim:clm_8382d046c07f4cf9219170e997a6080cdee3c5ca4a488554d010763d68d115bc]
- Installation creates a .claude/harness directory containing north-star.md, project-state.json, decisions.md, progress-log.md, and five sub-agent prompt templates under prompts/. [@claim:clm_840476d217666629e4660c4177c51349692af76b7391bcd0ca572a72a1c4013f]
- The tool is distributed as the npm package claude-northstar and operated via npx commands: init, status, and uninstall. [@claim:clm_936ed3a82a06a41a77eace97728745e4e9c0f48f582dfcdf944cc818d146e314]
- The framework positions the CLI agent session as a Tech Lead that understands the vision, plans milestones, coordinates sub-agents, and asks only strategic questions. [@claim:clm_b30c620ec388e595fedae723fde60d91f722efc2f7ed80a15e5a61ef880f0f11]
- An alternative install path fetches an install.sh script from the GitHub repository via curl and pipes it to bash. [@claim:clm_e5234c4eaa048e769a5b9fbef00c1ecbafab0988e769af2338a00bed5d20ffae]
- project-state.json persists milestones with status and progress values, the current focus, and identified gaps, enabling sessions to resume when the user says 'continue'. [@claim:clm_f7efcf77a459a96486140b592a859b2f8667401f121077f92669dee1a7756582]
<!-- rcw:end owner=source:src_e49c75f431395e57b98602d9a3568526 block=evidence -->

## Researcher notes

