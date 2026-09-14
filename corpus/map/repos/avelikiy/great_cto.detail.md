# avelikiy/great_cto -- full detail

[Back to orientation](great_cto.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/avelikiy/great_cto/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/8463cdb3ab3d551e.json](../../../wiki/dossiers/avelikiy/great_cto/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/8463cdb3ab3d551e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The system uses about 70 specialized agents with their own review gates, plus critics for architecture, spec, and schema that run before planning. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264) (`clm_8dd84f5bd01fbe557570566361b745db9fa9c30cc8470f57990825892fd4fc86`)

## design-choices (2 claim(s))

- [observation/documented] An 'approval-level' setting in .great_cto/PROJECT.md controls where the pipeline stops, from 'auto' (0 stops) through the default 'gates-only' (3 stops) to 'ship-only' (1 stop at deploy). -- evidence: [README.md#L149-L155](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L149-L155) (`clm_8dc8aecfab573f92199621de441a22961d79b3f5f571affc8c2de10711d98420`)
- [observation/documented] The product follows a rule that a thing which did not happen must never look like one that did: missing harnesses show 'unavailable', undecidable checks show 'unverifiable', unmeasured costs show 'unmeasured', and unassessed stages show 'null'. -- evidence: [README.md#L196-L201](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L196-L201) (`clm_357c787f72ec9f8643146ba754680d5fe9c262c996f95ce0ed67be5910ace9a8`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md mandates the bd (beads) issue tracker for all task tracking, non-interactive shell flags, and a mandatory session-completion workflow ending in a successful git push. -- evidence: [AGENTS.md#L65-L77](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L65-L77), [AGENTS.md#L3-L3](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L3-L3), [AGENTS.md#L24-L26](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L24-L26), [AGENTS.md#L55-L57](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L55-L57) (`clm_db82df4765a4cfebb97d5f475084d7a7464cb3c9496f7b4694fbf4ca96061f68`)
- [observation/documented] Repository development practice: CLAUDE.md sets code style rules (TypeScript strict mode, ESM only, Node >= 20 with node: prefix, zero runtime dependencies in packages/board/server.mjs) and a commit format '<type>: <description>'. -- evidence: [CLAUDE.md#L58-L62](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/CLAUDE.md#L58-L62) (`clm_28f2db65ed43e1de83a47e90449c7ea719a4a04f0207678fc325d384a10a8bba`)
- [observation/documented] Repository development practice: agents working in this repo must never mention private project names in public-facing artifacts, using the placeholder <private-project> instead, enforced by a pre-push hook. -- evidence: [CLAUDE.md#L20-L20](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/CLAUDE.md#L20-L20), [CLAUDE.md#L10-L11](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/CLAUDE.md#L10-L11), [CLAUDE.md#L28-L28](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/CLAUDE.md#L28-L28) (`clm_99479fa51bd5985c8294ab5a99f7247e2a4aa46c54d5309e064558fda6c640f4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Users interact via slash commands: /start to describe a product or feature and run the pipeline, /inbox for pending gates and blocked tasks, and /digest for weekly DORA metrics and cost roll-ups. -- evidence: [README.md#L96-L100](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L96-L100) (`clm_da8a421c9a09af8d21dbd6faaccee8c984b7ecd6ca1ce6e462151baabec59d33`)
- [observation/documented] A web board at localhost:3141 shows Decisions, Ledger (costs), Fleet, and Harness screens, and renders never-run scans as 'n/a' rather than a green zero. -- evidence: [README.md#L66-L69](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L66-L69) (`clm_f8ac1291ee794115efac84357687950f4dd3dde948b22397438743a5f574f24e`)
- [observation/documented] The tool installs via 'npx great-cto init', with an '--host codex' variant that installs skills and an MCP server instead of the Claude Code pipeline. -- evidence: [README.md#L106-L113](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L106-L113), [README.md#L12-L14](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L12-L14) (`clm_a1a9b07908cbf11b42acb8181063dab2f31c39add148e38b04094ce7464f918d`)

## memory-state (1 claim(s))

- [observation/documented] Decisions, lessons, and promoted patterns persist per project and globally across sessions, and an interrupted run resumes knowing which stages already ran. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264) (`clm_f521cd83e367f14d3a34e0ebeb3692f4484f505c6e32694f982fbbaf2f9d03e6`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Agents are scope-restricted at write time: an agent is described as physically unable to touch files outside its brief, refused at write rather than flagged at review. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264) (`clm_b4ece05db271e7b785e8b76c07d13d0091a61cd39da34f92b9e556f52a692644`)
- [observation/documented] Per-agent budgets in PROJECT.md ('agent-budgets:') make the pipeline decline to dispatch past a stage's spending cap and name the number; unmeasured runs hold nothing rather than firing a budget. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264), [README.md#L219-L223](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L219-L223) (`clm_9247e38aeafdcac56ad862f87a6b2a007648cff57e911193c9abe00e4aba06a3`)

## evaluation (1 claim(s))

- [observation/documented] An open benchmark built seven products with a median token cost of $171 and a median quality score of 70/100 (range 58-86), measured 2026-07-10, with a reproduction doc cited. -- evidence: [README.md#L72-L77](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L72-L77), [README.md#L31-L32](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L31-L32) (`clm_83bbf83f043afe56f460a5fbfff429d2431be07c2e2b9543f12d89ff5366201a`)

## dependencies (1 claim(s))

- [observation/documented] Requires Node >= 18.17; companion plugins Superpowers and Beads install automatically, and users are told to verify the plugin loaded via 'claude plugin list --json'. -- evidence: [README.md#L102-L104](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L102-L104) (`clm_a835415e02ad16f0407f9e24caddc775f9b1eec121875e7db2508c41299ad028`)

## limitations (3 claim(s))

- [observation/documented] On Codex the pipeline does not run: hooks, slash commands, the gate chain and secret-scan are unavailable there because the host lacks a plugin surface for them; only skills and the MCP server work. -- evidence: [README.md#L106-L113](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L106-L113) (`clm_dd5445f844f24db32a3917fbdf18a87fd44c5a61d21b0c02d09f8bc5132a30c4`)
- [observation/documented] Per-agent cost attribution is unreliable: cost is read from the host's session transcript, which covers the session rather than one subagent, so per-agent figures can be inflated and should be treated as a ceiling. -- evidence: [README.md#L272-L286](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L272-L286) (`clm_c12ac87655548397741ee5fc5c9baac9ba426fe75d7a8e39cb34b900f06fa78b`)
- [observation/documented] The tool is positioned for a solo builder, is not a CI/CD system (gates run locally, merging still goes through GitHub Actions), and is not certification-audited despite PCI/HIPAA/SOC2 scaffolds. -- evidence: [README.md#L272-L286](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L272-L286) (`clm_343e4a063e6081fd5573b2f5f1c60e6573398ec21db5860274d87aef4aecbac7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

