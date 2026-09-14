# markshust/hcf

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9cfca7de63c3 @ fd7ae5cfbe800a29

## Summary (orientation draft, not independently verified)

HCF is a Claude Code plugin that separates interactive planning from autonomous parallel TDD execution, with agents self-enrolling into 8 lifecycle hooks via YAML frontmatter. Evidence covers its skills, agents, hook pipeline, plans-directory configuration, and repository development practices. Evidence coverage: 128 of 162 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] HCF separates planning (human-in-the-loop, where human and AI collaborate on requirements) from execution (fully autonomous parallel TDD implementation). -- evidence: [README.md#L38-L41](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L38-L41), [README.md#L36-L36](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L36-L36)
- components (1 claim(s)):
  - [observation/documented] The plugin ships three agents (devils-advocate, tdd-worker, standards-enforcer), four skills (project-setup, project-update, plan-create, plan-orchestrate), and hook scripts including discover-hooks.sh and gate scripts. -- evidence: [README.md#L318-L351](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L318-L351)
- design-choices (5 claim(s)):
  - [observation/documented] The pipeline uses convention over configuration: there is no central registry, and each agent enrolls itself by declaring a phase, order, and mode in its own YAML frontmatter. -- evidence: [README.md#L121-L121](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L121-L121), [README.md#L151-L155](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L151-L155), [README.md#L142-L142](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L142-L142), [README.md#L144-L149](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L144-L149)
  - [observation/documented] Only devils-advocate is enrolled by default (at post-plan); standards-enforcer ships with its enrollment commented out and can be enabled by uncommenting its phase key. -- evidence: [README.md#L161-L161](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L161-L161), [README.md#L138-L138](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L138-L138), [README.md#L163-L174](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L163-L174)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, create a feature branch, test locally with --plugin-dir, add a CHANGELOG [Unreleased] entry for user-visible changes, and submit a pull request; the repo's own test suite runs via ./tests/run-tests.sh with no dependencies beyond bash/awk/sed/sort/grep. -- evidence: [CHANGELOG.md#L62-L64](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/CHANGELOG.md#L62-L64), [README.md#L483-L487](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L483-L487)
  - [observation/documented] Repository development practice: the plugin can be tested locally without publishing using claude --plugin-dir /path/to/hcf, with skills namespaced as /hcf:skill-name and debug output via --debug. -- evidence: [README.md#L461-L463](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L461-L463), [README.md#L416-L416](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L416-L416), [README.md#L418-L420](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L418-L420), [README.md#L422-L425](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L422-L425)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Skills are invocable as slash commands (/project-setup, /plan-create, /plan-orchestrate) and can also auto-trigger when a user request matches their description; project-setup and project-update are manual-invocation only. -- evidence: [README.md#L302-L307](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L302-L307), [README.md#L427-L427](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L427-L427), [README.md#L300-L300](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L300-L300)
  - [observation/documented] Plans default to .claude/plans/ but a project can set a relative plansDir in an optional .claude/hcf.json; no skill creates or modifies that file, and project-update only validates it if present. -- evidence: [README.md#L377-L379](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L377-L379), [README.md#L367-L371](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L367-L371), [README.md#L364-L365](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L364-L365), [README.md#L373-L375](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L373-L375)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] plan-orchestrate builds batches from the task dependency graph and runs independent tasks in parallel workers, so many tasks complete in a handful of batches rather than sequentially. -- evidence: [README.md#L230-L233](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L230-L233), [README.md#L237-L237](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L237-L237), [README.md#L245-L245](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L245-L245), [README.md#L239-L243](https://github.com/markshust/hcf/blob/9cfca7de63c309ee6b5b38088cd446af85e9ff46/README.md#L239-L243)
More evidence: [full detail](hcf.detail.md)

Metadata and full claim list: [full detail](hcf.detail.md)
Human notes ([notes](hcf.notes.md), never overwritten by build)

[Back to map index](../../index.md)
