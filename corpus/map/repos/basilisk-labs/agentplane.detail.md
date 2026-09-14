# basilisk-labs/agentplane -- full detail

[Back to orientation](agentplane.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/basilisk-labs/agentplane/ecfccc5ad0230fc1876a319be0af5cdb530c339f/f428a157f1df96e8.json](../../../wiki/dossiers/basilisk-labs/agentplane/ecfccc5ad0230fc1876a319be0af5cdb530c339f/f428a157f1df96e8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The design separates semantic judgment (agents) from mechanically authoritative workflow mechanics (CLI), with the CLI resolving authority, transitions, routing, schemas, and stop conditions in code rather than by model guesses. -- evidence: [README.md#L33-L38](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L33-L38), [README.md#L105-L107](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L105-L107), [README.md#L30-L31](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L30-L31), [README.md#L11-L14](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L11-L14) (`clm_fbfa6dec6f4134450cc76d2ea796618168bf82593401f626aeb2f955f69afedb`)
- [observation/documented] Two workflow modes are offered: 'direct' for lighter local routes and 'branch_pr' for worktrees, branches, PR artifacts, and hosted checks; the agent declares a preferred mode but Agentplane can strengthen the route based on observed work. -- evidence: [README.md#L116-L119](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L116-L119), [README.md#L111-L114](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L111-L114) (`clm_d3d6ce3cf3d725e39bc0b89f8f8251a33f4156c463e4909a150d6f99fbb3ffc9`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: POLICY.md requires lint and full tests to pass before merging to main, tests for behavior changes, English-only user-facing strings, no accidental npm releases, and no uncommitted code changes under packages/**. -- evidence: [POLICY.md#L33-L36](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/POLICY.md#L33-L36), [POLICY.md#L17-L27](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/POLICY.md#L17-L27) (`clm_54af9e8c2880354076c646a752754a6a987ca8ec3694c995b3ee6a52e8417d8a`)
- [observation/documented] Repository development practice: contributors work through the agentplane task lifecycle (task new, plan approve, verify, finish), open issues first for architectural or CLI-surface changes, and must keep src/cli, usecases, ports, and adapters layering with OS/git/network access confined to adapters. -- evidence: [CONTRIBUTING.md#L33-L34](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L33-L34), [CONTRIBUTING.md#L51-L59](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L51-L59), [POLICY.md#L51-L59](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/POLICY.md#L51-L59), [CONTRIBUTING.md#L15-L20](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L15-L20), [CONTRIBUTING.md#L38-L41](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L38-L41) (`clm_3bd92d6dbb61ff9b84997bcdf5104c2279e7afcf031f2b1b5c693308014fbb7a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a CLI (npm package 'agentplane', short alias 'ap') with commands such as init, quickstart, task create/active/advance/run, and evaluator list/show/execute. -- evidence: [README.md#L55-L57](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L55-L57), [README.md#L61-L65](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L61-L65), [README.md#L47-L53](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L47-L53), [ROADMAP.md#L100-L100](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/ROADMAP.md#L100-L100) (`clm_2e7b18cde13b2fde3c6870dc745e92a447b192908aed443020cbfa52828f22b2`)
- [observation/documented] task advance returns a bounded episode packet containing the objective, writable scope, context, result schema, an exchange.result_path, and an exact exchange.resume_argv command for returning the typed result. -- evidence: [README.md#L67-L70](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L67-L70) (`clm_2d81e167ba8b55b621418b0ab80a5e452879911a5620eb747ea870975dbf4868`)

## memory-state (1 claim(s))

- [observation/documented] Operating state lives in the repository: AGENTS.md/CLAUDE.md as policy gateway, .agentplane/WORKFLOW.md, per-task README and acr.json (Agent Change Record), and pr/ artifacts; an optional Local Context layer adds source-backed repository knowledge. -- evidence: [README.md#L125-L131](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L125-L131), [README.md#L133-L136](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L133-L136) (`clm_035f0bd1efc93eee97aeeab1f56f08edf6ff5659ec94791467cf1b5fc0792f3a`)

## orchestration (2 claim(s))

- [observation/documented] The control loop issues a bounded semantic episode, the agent returns a semantic result, and the CLI observes facts, runs the formal route, records evidence, and stops at approval, recovery, or verified completion. -- evidence: [README.md#L72-L75](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L72-L75), [README.md#L89-L95](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L89-L95) (`clm_cba1e5b9e301549e54c200b5037d3ff21a08c5bdc889d15715e3c106dc809cec`)
- [observation/documented] A supervisor model prepares a bounded AgentWorkOrder, enforces state and authority preconditions, invokes one specialized semantic role, and records an independent ExecutionReceipt; state fingerprints reject stale results. -- evidence: [README.md#L99-L103](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L99-L103), [ROADMAP.md#L92-L92](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/ROADMAP.md#L92-L92), [ROADMAP.md#L90-L90](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/ROADMAP.md#L90-L90) (`clm_1bc37a795fdb42e459d031a010e8591c0e5fcc568564d3fbb14ec4854b2c558e`)

## tools-permissions (1 claim(s))

- [observation/documented] Writable roots and allowed effects for each episode are carried in that episode's WorkOrder, and semantic episodes cannot perform or claim formal lifecycle transitions. -- evidence: [README.md#L99-L103](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L99-L103) (`clm_7e749beadf11d612b477abadf9e8156314497a0196fb978369c541a111167363`)

## evaluation (1 claim(s))

- [observation/documented] Projects can store prompt modules under .agentplane/evaluators and run a read-only evaluation episode via 'agentplane evaluator execute <task-id>'; the roadmap plans comparative evaluation and quality gates in a later horizon. -- evidence: [ROADMAP.md#L102-L102](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/ROADMAP.md#L102-L102), [ROADMAP.md#L100-L100](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/ROADMAP.md#L100-L100) (`clm_f7f8893373dca19d9be87d75299a84cd36526429ab714c7958e071998e306cea`)

## dependencies (1 claim(s))

- [observation/documented] The CLI requires Node.js 24+ and Git, is distributed via npm, and is MIT licensed. -- evidence: [README.md#L16-L20](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L16-L20), [README.md#L192-L192](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L192-L192), [README.md#L45-L45](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L45-L45) (`clm_c9e78f670e1e03a49b6aaccc5330333d99c279eadb1e28ff93b53edee1d0e804`)

## limitations (1 claim(s))

- [observation/documented] The project is pre-1.0 and under active development; the README advises pinning the CLI version in automation and reviewing release notes when upgrading. -- evidence: [README.md#L178-L179](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L178-L179) (`clm_c30a8292f1ebd0534402d3ba77dfd8feeed6a1c60a2492117dd278910b868a7f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

