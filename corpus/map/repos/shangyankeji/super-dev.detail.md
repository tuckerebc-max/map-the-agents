# shangyankeji/super-dev -- full detail

[Back to orientation](super-dev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shangyankeji/super-dev/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/352741a68f351de0.json](../../../wiki/dossiers/shangyankeji/super-dev/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/352741a68f351de0.json)

## specifications (1 claim(s))

- [observation/documented] The document engine generates initial frameworks for PRD, Architecture, and UIUX documents (covering user personas, data models, design tokens, etc.), which the host model then deepens using user requirements, web research, and expert knowledge. -- evidence: [README.md#L276-L276](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L276-L276), [README.md#L278-L282](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L278-L282), [README.md#L284-L284](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L284-L284) (`clm_005182a0a23ca7e4fe8125176b055247e6ddad070da760246c886b11d1454d37`)

## components (2 claim(s))

- [observation/documented] Eleven built-in domain expert agents (PRODUCT, PM, ARCHITECT, UI, UX, SECURITY, CODE, DBA, QA, DEVOPS, RCA) are injected into host prompts at specific pipeline stages, each with Profile, Knowledge, Rules, and Protocol layers. -- evidence: [README.md#L228-L228](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L228-L228), [README.md#L214-L226](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L214-L226), [README.md#L212-L212](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L212-L212) (`clm_7a8274a7dac206414b52c4cc22664d4205c020c58d1e87aed6caa61e51a8bbae`)
- [observation/documented] A built-in knowledge base under `knowledge/` is described as 270+ files across 23 domains, with staged loading (L1 index / L2 detail / L3 deep reference) under token budgeting and SQLite-tracked usage for data-driven weight optimization. -- evidence: [README.md#L337-L337](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L337-L337), [README.md#L350-L356](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L350-L356) (`clm_0a44730768f8d5ad9b87ea332ea86f8e25db9cbe1179c2173365db3f781c404e`)

## design-choices (3 claim(s))

- [observation/documented] UI/UX decisions are frozen into contract artifacts (`output/*-ui-contract.json`, `design-tokens.css`, alignment reports) that host prompts, UI review, quality gates, proof-pack, and release readiness must stay consistent with. -- evidence: [README.md#L243-L247](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L243-L247), [README.md#L241-L241](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L241-L241), [README.md#L249-L249](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L249-L249) (`clm_844a119c3fd5adfa05dac109a37dc96cca5ff21aa9444ab1951a6d019925aed8`)
- [observation/documented] Quality governance uses 25 declarative YAML validation rules (14 default plus 11 red-team) with project-level custom overrides, plus default/balanced/enterprise policy presets. -- evidence: [README.md#L294-L304](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L294-L304) (`clm_2518843849e4ecc23d6e820f865598927c81174edfec521f0872e081cc8cf3e3`)
- [observation/documented] The architecture divides responsibility: hosts handle model inference, web search, coding, terminal execution, and file modification, while Super Dev governs process, documents, knowledge push, validation rules, gates, and audit artifacts. -- evidence: [README.md#L533-L539](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L533-L539), [README.md#L79-L80](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L79-L80) (`clm_0fa810dc19d76f90ff315469333444ec05e1c56c7cbdf20de6f49b5af8c72aa1`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The terminal CLI is scoped to onboarding, updating, and uninstalling: `super-dev`, `super-dev update`, and `super-dev uninstall`, with `super-dev uninstall --dry-run` offered as a preview of what would be deleted. -- evidence: [README.md#L129-L131](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L129-L131), [README.md#L180-L186](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L180-L186), [README.md#L172-L176](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L172-L176) (`clm_eb4eb8f756f33e6d75921b5a183574df44a81b62ecade9993e5fb641986d92c1`)
- [observation/documented] After onboarding, hosts trigger the pipeline via `/super-dev <request>`, `super-dev: <request>`, or a competition fast mode `/super-dev-seeai`, with the exact trigger varying by host (e.g. Codex CLI uses `$super-dev`). -- evidence: [README.md#L416-L419](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L416-L419), [README.md#L135-L139](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L135-L139), [README.md#L577-L590](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L577-L590) (`clm_6dd14b5bd72c8d42a0f8ff9f1aebe8a5aaa9541bada936c34fce7d6c292a37f0`)
- [observation/documented] The onboarding wizard presents an interactive host selector with arrow-key navigation, Space to check hosts, Enter to install, and A/C/I/R/U shortcuts (select all, CLI-only, IDE-only, clear, upgrade), then prints the chosen host's trigger syntax. -- evidence: [README.md#L414-L414](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L414-L414), [README.md#L416-L419](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L416-L419), [README.md#L404-L412](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L404-L412) (`clm_1191fd92766655fdb92885eabb8b989f3df676cdc62d7f301ab8bbb6084e15fc`)

## memory-state (1 claim(s))

- [observation/documented] Session continuity is persisted in `.super-dev/SESSION_BRIEF.md` and `.super-dev/workflow-state.json` (current action, host first-sentence, machine-side actions, continuity rules), and recovery from `.super-dev/` and `output/` artifacts is the default scenario after interruption. -- evidence: [README.md#L145-L151](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L145-L151), [README.md#L261-L272](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L261-L272) (`clm_5f0c112105434551f045e0d3e47c3f24b80883d4a351ba330d7add7f5ed7512e`)

## orchestration (2 claim(s))

- [observation/documented] The standard pipeline is research -> docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery, with mandatory user confirmation gates after the three documents and after the frontend preview. -- evidence: [README.md#L523-L523](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L523-L523), [README.md#L261-L272](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L261-L272) (`clm_7ae08704e01ef7ddd35a80400e7a55140591f5940986c3443b247838178524c8`)
- [observation/documented] Existing projects follow a baseline-first chain (baseline -> baseline_confirm -> delta research -> docs...), interrupted runs resume from checkpoints, and each stage has a timeout mechanism to prevent infinite waiting. -- evidence: [README.md#L261-L272](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L261-L272) (`clm_e889648b0e48d7e171cf9689e375c5ae46dab1e9df4308867511e6da75b5656f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation auto-installs Python dependencies declared in pyproject.toml (e.g. rich, pyyaml, ddgs, requests, beautifulsoup4, fastapi, uvicorn) but explicitly does not install host applications, Node.js, Docker, databases, or other system environments. -- evidence: [README.md#L454-L460](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L454-L460), [README.md#L464-L467](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L464-L467), [README.md#L471-L472](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L471-L472), [README.md#L452-L452](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L452-L452) (`clm_5d6bfaf5b6d02dcc7b7f43508a3f7de6cd3bbada078ccdf7a654523c2e38203c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

