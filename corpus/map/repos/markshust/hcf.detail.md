# markshust/hcf -- full detail

[Back to orientation](hcf.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/markshust/hcf/9cfca7de63c309ee6b5b38088cd446af85e9ff46/fd7ae5cfbe800a29.json](../../../wiki/dossiers/markshust/hcf/9cfca7de63c309ee6b5b38088cd446af85e9ff46/fd7ae5cfbe800a29.json)

## specifications (1 claim(s))

- [observation/documented] HCF separates planning (human-in-the-loop, where human and AI collaborate on requirements) from execution (fully autonomous parallel TDD implementation). -- evidence: [README.md#L38-L41](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L38-L41), [README.md#L36-L36](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L36-L36) (`clm_c1fd868764ed5482baf33cc8e1d18703c4d6c95fd3b5a8f62897b7f8a9471760`)

## components (1 claim(s))

- [observation/documented] The plugin ships three agents (devils-advocate, tdd-worker, standards-enforcer), four skills (project-setup, project-update, plan-create, plan-orchestrate), and hook scripts including discover-hooks.sh and gate scripts. -- evidence: [README.md#L318-L351](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L318-L351) (`clm_f51c45a1a4ce58c4ab963021a224c1c4427c9047e7b438c397d1c1353f14f676`)

## design-choices (5 claim(s))

- [observation/documented] The pipeline uses convention over configuration: there is no central registry, and each agent enrolls itself by declaring a phase, order, and mode in its own YAML frontmatter. -- evidence: [README.md#L121-L121](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L121-L121), [README.md#L151-L155](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L151-L155), [README.md#L142-L142](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L142-L142), [README.md#L144-L149](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L144-L149) (`clm_8172659147badc30166238ef254e289de08d98f567d9a76a391721e474daa679`)
- [observation/documented] Only devils-advocate is enrolled by default (at post-plan); standards-enforcer ships with its enrollment commented out and can be enabled by uncommenting its phase key. -- evidence: [README.md#L161-L161](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L161-L161), [README.md#L138-L138](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L138-L138), [README.md#L163-L174](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L163-L174) (`clm_433cada7fa89f58dbd215a6c3e8c801ec05d337a9ea357d572c94827dd697e36`)
- [observation/documented] A malformed plansDir value (absolute path, .. segment, or empty string) stops the run rather than falling back to the default plans directory, and the resolver avoids a jq dependency. -- evidence: [CHANGELOG.md#L27-L27](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/CHANGELOG.md#L27-L27), [README.md#L381-L385](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L381-L385) (`clm_4c36484d66c9001ef9c48d7ed1505cc9193e6632f1e0a53a49028da3fcf77a6a`)
- [observation/documented] There is deliberately no 'execution' hook; the implementation loop is already covered by the pre/post-implementation and pre/post-batch hooks, so an execution hook would only duplicate them. -- evidence: [HOOKS.md#L31-L36](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/HOOKS.md#L31-L36) (`clm_c2be8e669245e73cc1a5935749e4217e8a86014a82241f7843fb5fc865f164ad`)
- [inference/documented] Discovery failures are treated as hard errors (exit 3 for invalid phase/mode, exit 4 for mid-run enrollment change) rather than empty hooks, reflecting a design preference for failing loudly over silently running a different pipeline. -- evidence: [CHANGELOG.md#L55-L59](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/CHANGELOG.md#L55-L59), [README.md#L214-L214](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L214-L214), [CHANGELOG.md#L67-L68](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/CHANGELOG.md#L67-L68) (`clm_43e04a65e57fe98db28e142c59b407dfe49e3fa4eb704b861079c96124795628`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork, create a feature branch, test locally with --plugin-dir, add a CHANGELOG [Unreleased] entry for user-visible changes, and submit a pull request; the repo's own test suite runs via ./tests/run-tests.sh with no dependencies beyond bash/awk/sed/sort/grep. -- evidence: [CHANGELOG.md#L62-L64](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/CHANGELOG.md#L62-L64), [README.md#L483-L487](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L483-L487) (`clm_c82bcc38c5d66716392763634a1e48caa3203ca3a2d272fc543266900f08a203`)
- [observation/documented] Repository development practice: the plugin can be tested locally without publishing using claude --plugin-dir /path/to/hcf, with skills namespaced as /hcf:skill-name and debug output via --debug. -- evidence: [README.md#L461-L463](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L461-L463), [README.md#L416-L416](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L416-L416), [README.md#L418-L420](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L418-L420), [README.md#L422-L425](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L422-L425) (`clm_562b20ffe41f6baf0180df973be426249164a5f1cf12287b20b26847ef55943e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Skills are invocable as slash commands (/project-setup, /plan-create, /plan-orchestrate) and can also auto-trigger when a user request matches their description; project-setup and project-update are manual-invocation only. -- evidence: [README.md#L302-L307](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L302-L307), [README.md#L427-L427](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L427-L427), [README.md#L300-L300](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L300-L300) (`clm_c9853db6953e2fc767c1c9772724e6686d1136010d2c46d6e3c2ee9530564080`)
- [observation/documented] Plans default to .claude/plans/ but a project can set a relative plansDir in an optional .claude/hcf.json; no skill creates or modifies that file, and project-update only validates it if present. -- evidence: [README.md#L377-L379](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L377-L379), [README.md#L367-L371](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L367-L371), [README.md#L364-L365](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L364-L365), [README.md#L373-L375](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L373-L375) (`clm_716a96a96797970e9ee08444fe74a273caaefed612d85446a447e038a9ef7ebe`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] plan-orchestrate builds batches from the task dependency graph and runs independent tasks in parallel workers, so many tasks complete in a handful of batches rather than sequentially. -- evidence: [README.md#L230-L233](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L230-L233), [README.md#L237-L237](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L237-L237), [README.md#L245-L245](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L245-L245), [README.md#L239-L243](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L239-L243) (`clm_f143f5a5703c82c46fd9c8b872a0a079ffd96ad0d3899d151ee75cb4a0562322`)
- [observation/documented] Run state such as task statuses, requirement checkboxes, and retry counts lives in the plan files, so an interrupted run resumes by re-running the plan; terminal outputs are ALL_TASKS_COMPLETE or TASKS_BLOCKED. -- evidence: [README.md#L100-L100](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L100-L100), [README.md#L311-L314](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L311-L314) (`clm_96f842bf8e895a2de6454b7538dfd6e88a8c2c30cc55336fb7ecab92d332f69a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running HCF requires the Claude Code CLI, a Git repository, and a test framework configured in the project. -- evidence: [README.md#L410-L412](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L410-L412) (`clm_395fd764caa9be497350bddccba2d3f89a06f0dfd932c4008f5ff2eae243dee5`)

## limitations (1 claim(s))

- [observation/documented] HCF does not migrate plan folders when the plans directory changes; the user must move them, and project-update warns if .claude/plans still holds plan folders after a move. -- evidence: [README.md#L387-L390](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L387-L390), [CHANGELOG.md#L25-L25](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/CHANGELOG.md#L25-L25) (`clm_b8313bf54a7739d54148bc81fcc6939fd4770d682ef263649a5ad94d6bbeec5c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

