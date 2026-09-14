# zhixiangluo/10xproductivity -- full detail

[Back to orientation](10xproductivity.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhixiangluo/10xproductivity/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/cfc92ae293e2d435.json](../../../wiki/dossiers/zhixiangluo/10xproductivity/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/cfc92ae293e2d435.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is organized into tool_connections/, triggers/, runtime/, workflows/, tests/, .cursor/skills/, .claude/skills/, and staging/, plus setup guides such as setup.md, add-new-tool.md, and setup-python.md. -- evidence: [README.md#L147-L159](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L147-L159) (`clm_b1dbd2ca5dfce865a0c23e8472d8e1e88b70d723c388d6f9d7b6b936ccae5d8b`)

## design-choices (2 claim(s))

- [observation/documented] The project is positioned as a local-first personal AI assistant stack that reuses the user's existing coding agent, browser sessions, desktop apps, and permissions, explicitly avoiding new company-wide platforms, Slack apps, webhooks, or IT approval. -- evidence: [README.md#L5-L5](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L5-L5), [README.md#L29-L34](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L29-L34), [README.md#L3-L3](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L3-L3) (`clm_068019eb27bee991cf8ead377e1c05a04b8c701f520f710b23b4e3c881a0df57`)
- [observation/documented] The connection philosophy prioritizes zero-friction auth: supported API tokens first, then Agent Browser over existing sessions; OAuth requiring the user to create their own app or register credentials is explicitly rejected. -- evidence: [add-new-tool.md#L113-L113](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L113-L113), [add-new-tool.md#L82-L82](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L82-L82), [add-new-tool.md#L87-L94](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L87-L94) (`clm_1821159ea11e4e0b59af05346dfb84c37c2f7c038772322048bdd0a81470166c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions follow a 'run before you write' rule — every snippet must be executed and seen to succeed — and new tool work starts in TENX_PRIVATE_DIR/personal/, never directly in tool_connections/, with promotion to the public repo only via staging/ and a PR after verification and scrubbing. -- evidence: [README.md#L341-L341](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L341-L341), [add-new-tool.md#L44-L51](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L44-L51) (`clm_88a1bd886750686b0b20c4df52c45a5556c140c89121d5076bf250fed9809725`)

## skills-patterns (1 claim(s))

- [observation/documented] Packaged Cursor and Claude Code skills cover tool setup, enterprise search, workflow creation, UI surface discovery, colleague distillation, and an assistant inbox/orchestrator skill. -- evidence: [README.md#L197-L197](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L197-L197) (`clm_69aa9a134f225fb648805cabe845156d4f62a23851e72d3f0c06e007e8af48b3`)

## interfaces (2 claim(s))

- [observation/documented] The runtime exposes a CLI entry point 10x-host that takes --trigger, --workflow, and --engine arguments, e.g. running a slack-polling trigger with the assistant workflow and the cursor engine. -- evidence: [README.md#L281-L283](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L281-L283), [README.md#L238-L240](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L238-L240) (`clm_701d4f4cf6e92d869a0fbe8a1a44bb64694ab3eef424c4a71f9da30d32056670`)
- [observation/documented] A second CLI, 10x-standup-prep, supports a --meeting-context flag and a --dry-run mode; posting to Slack requires reviewing output first and setting TENX_STANDUP_PREP_SLACK_CHANNEL before using --post. -- evidence: [README.md#L289-L291](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L289-L291), [README.md#L293-L293](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L293-L293) (`clm_1f3451b5fef5a21d4077c8ce5bb84ca8f4ab660e2e6e36ff4d435370789cac88`)

## memory-state (1 claim(s))

- [observation/documented] Private runtime state lives outside the repo by default under ~/.10xProductivity/ (.env tokens, personal/ recipes, verified_connections.md, tmp/ for trigger and scheduler state), overridable via the TENX_PRIVATE_DIR environment variable. -- evidence: [README.md#L163-L169](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L163-L169), [README.md#L171-L171](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L171-L171) (`clm_9950b4a60820e773f2ce4d51d2fabea10b1407ce6130d14c82b677d087cfff22`)

## orchestration (1 claim(s))

- [observation/documented] The architecture separates a push layer (triggers that detect events via desktop/browser notifications, sessions, email, or polling and wake workflows) from a pull layer (tool connections that fetch context or act), with a thin local runtime handling polling, scheduling, state, dedupe, replies, and agent invocation. -- evidence: [README.md#L131-L131](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L131-L131), [README.md#L135-L135](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L135-L135), [README.md#L139-L139](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L139-L139), [README.md#L133-L133](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L133-L133) (`clm_03da786cb1e986324876eeb3e75a1dd024f28e3b5322f9305e90dd8f763f0eb1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Setup requires a coding agent (Cursor, Claude Code, or Codex), a Python virtualenv with an editable dev install (pip install -e ".[dev]"), and optionally Python/Playwright setup per setup-python.md. -- evidence: [README.md#L218-L222](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L218-L222), [README.md#L201-L201](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L201-L201), [README.md#L210-L210](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L210-L210) (`clm_15d4cdd5398ecc3101971110c8412b4c42ec86980f9a209a15a30b39a14a89ee`)

## limitations (2 claim(s))

- [observation/documented] Per the README's status table, tool connections, enterprise search, and agent skills are available today, while triggers, runtime, and reusable workflows are early; learning and memory (scheduled reflection, durable memory) are roadmap items not yet complete. -- evidence: [README.md#L175-L175](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L175-L175), [README.md#L52-L60](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L52-L60) (`clm_88fb1340656cfebd26cee1886e7ced6d0ab09ee1500cbc411cd840262b348812`)
- [observation/documented] The README warns that some workflows automate actions on external platforms in ways that may violate platform Terms of Service, and directs users to LEGAL_NOTICE.md before running automation scripts. -- evidence: [README.md#L345-L345](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L345-L345) (`clm_a0506b716647e182c956caf14563aa7d5fe90c48f15c39764eeca067066e6efd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

