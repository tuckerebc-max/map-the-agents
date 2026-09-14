---
access: public
aliases: []
claim_ids:
- clm_395fd764caa9be497350bddccba2d3f89a06f0dfd932c4008f5ff2eae243dee5
- clm_433cada7fa89f58dbd215a6c3e8c801ec05d337a9ea357d572c94827dd697e36
- clm_43e04a65e57fe98db28e142c59b407dfe49e3fa4eb704b861079c96124795628
- clm_4c36484d66c9001ef9c48d7ed1505cc9193e6632f1e0a53a49028da3fcf77a6a
- clm_562b20ffe41f6baf0180df973be426249164a5f1cf12287b20b26847ef55943e
- clm_716a96a96797970e9ee08444fe74a273caaefed612d85446a447e038a9ef7ebe
- clm_8172659147badc30166238ef254e289de08d98f567d9a76a391721e474daa679
- clm_96f842bf8e895a2de6454b7538dfd6e88a8c2c30cc55336fb7ecab92d332f69a
- clm_b8313bf54a7739d54148bc81fcc6939fd4770d682ef263649a5ad94d6bbeec5c
- clm_c1fd868764ed5482baf33cc8e1d18703c4d6c95fd3b5a8f62897b7f8a9471760
- clm_c82bcc38c5d66716392763634a1e48caa3203ca3a2d272fc543266900f08a203
- clm_c9853db6953e2fc767c1c9772724e6686d1136010d2c46d6e3c2ee9530564080
- clm_f143f5a5703c82c46fd9c8b872a0a079ffd96ad0d3899d151ee75cb4a0562322
- clm_f51c45a1a4ce58c4ab963021a224c1c4427c9047e7b438c397d1c1353f14f676
maturity: draft
page_id: pg_7e9fe2d86c3d5269a7476faa680a1dd4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_51935a1d6afd5aa8979c5d3815e98a57
title: markshust/hcf/README.md @ 9cfca7de63c3
updated_at: '2026-09-14T04:08:07Z'
---

# markshust/hcf/README.md @ 9cfca7de63c3

<!-- rcw:begin owner=source:src_51935a1d6afd5aa8979c5d3815e98a57 block=evidence -->
- Running HCF requires the Claude Code CLI, a Git repository, and a test framework configured in the project. [@claim:clm_395fd764caa9be497350bddccba2d3f89a06f0dfd932c4008f5ff2eae243dee5]
- Only devils-advocate is enrolled by default (at post-plan); standards-enforcer ships with its enrollment commented out and can be enabled by uncommenting its phase key. [@claim:clm_433cada7fa89f58dbd215a6c3e8c801ec05d337a9ea357d572c94827dd697e36]
- Discovery failures are treated as hard errors (exit 3 for invalid phase/mode, exit 4 for mid-run enrollment change) rather than empty hooks, reflecting a design preference for failing loudly over silently running a different pipeline. [@claim:clm_43e04a65e57fe98db28e142c59b407dfe49e3fa4eb704b861079c96124795628]
- A malformed plansDir value (absolute path, .. segment, or empty string) stops the run rather than falling back to the default plans directory, and the resolver avoids a jq dependency. [@claim:clm_4c36484d66c9001ef9c48d7ed1505cc9193e6632f1e0a53a49028da3fcf77a6a]
- Repository development practice: the plugin can be tested locally without publishing using claude --plugin-dir /path/to/hcf, with skills namespaced as /hcf:skill-name and debug output via --debug. [@claim:clm_562b20ffe41f6baf0180df973be426249164a5f1cf12287b20b26847ef55943e]
- Plans default to .claude/plans/ but a project can set a relative plansDir in an optional .claude/hcf.json; no skill creates or modifies that file, and project-update only validates it if present. [@claim:clm_716a96a96797970e9ee08444fe74a273caaefed612d85446a447e038a9ef7ebe]
- The pipeline uses convention over configuration: there is no central registry, and each agent enrolls itself by declaring a phase, order, and mode in its own YAML frontmatter. [@claim:clm_8172659147badc30166238ef254e289de08d98f567d9a76a391721e474daa679]
- Run state such as task statuses, requirement checkboxes, and retry counts lives in the plan files, so an interrupted run resumes by re-running the plan; terminal outputs are ALL_TASKS_COMPLETE or TASKS_BLOCKED. [@claim:clm_96f842bf8e895a2de6454b7538dfd6e88a8c2c30cc55336fb7ecab92d332f69a]
- HCF does not migrate plan folders when the plans directory changes; the user must move them, and project-update warns if .claude/plans still holds plan folders after a move. [@claim:clm_b8313bf54a7739d54148bc81fcc6939fd4770d682ef263649a5ad94d6bbeec5c]
- HCF separates planning (human-in-the-loop, where human and AI collaborate on requirements) from execution (fully autonomous parallel TDD implementation). [@claim:clm_c1fd868764ed5482baf33cc8e1d18703c4d6c95fd3b5a8f62897b7f8a9471760]
- Repository development practice: contributors fork, create a feature branch, test locally with --plugin-dir, add a CHANGELOG [Unreleased] entry for user-visible changes, and submit a pull request; the repo's own test suite runs via ./tests/run-tests.sh with no dependencies beyond bash/awk/sed/sort/grep. [@claim:clm_c82bcc38c5d66716392763634a1e48caa3203ca3a2d272fc543266900f08a203]
- Skills are invocable as slash commands (/project-setup, /plan-create, /plan-orchestrate) and can also auto-trigger when a user request matches their description; project-setup and project-update are manual-invocation only. [@claim:clm_c9853db6953e2fc767c1c9772724e6686d1136010d2c46d6e3c2ee9530564080]
- plan-orchestrate builds batches from the task dependency graph and runs independent tasks in parallel workers, so many tasks complete in a handful of batches rather than sequentially. [@claim:clm_f143f5a5703c82c46fd9c8b872a0a079ffd96ad0d3899d151ee75cb4a0562322]
- The plugin ships three agents (devils-advocate, tdd-worker, standards-enforcer), four skills (project-setup, project-update, plan-create, plan-orchestrate), and hook scripts including discover-hooks.sh and gate scripts. [@claim:clm_f51c45a1a4ce58c4ab963021a224c1c4427c9047e7b438c397d1c1353f14f676]
<!-- rcw:end owner=source:src_51935a1d6afd5aa8979c5d3815e98a57 block=evidence -->

## Researcher notes

