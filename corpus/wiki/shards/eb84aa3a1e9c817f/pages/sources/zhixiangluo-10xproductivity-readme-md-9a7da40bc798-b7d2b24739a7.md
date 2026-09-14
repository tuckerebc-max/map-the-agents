---
access: public
aliases: []
claim_ids:
- clm_03da786cb1e986324876eeb3e75a1dd024f28e3b5322f9305e90dd8f763f0eb1
- clm_068019eb27bee991cf8ead377e1c05a04b8c701f520f710b23b4e3c881a0df57
- clm_15d4cdd5398ecc3101971110c8412b4c42ec86980f9a209a15a30b39a14a89ee
- clm_1f3451b5fef5a21d4077c8ce5bb84ca8f4ab660e2e6e36ff4d435370789cac88
- clm_69aa9a134f225fb648805cabe845156d4f62a23851e72d3f0c06e007e8af48b3
- clm_701d4f4cf6e92d869a0fbe8a1a44bb64694ab3eef424c4a71f9da30d32056670
- clm_88a1bd886750686b0b20c4df52c45a5556c140c89121d5076bf250fed9809725
- clm_88fb1340656cfebd26cee1886e7ced6d0ab09ee1500cbc411cd840262b348812
- clm_9950b4a60820e773f2ce4d51d2fabea10b1407ce6130d14c82b677d087cfff22
- clm_a0506b716647e182c956caf14563aa7d5fe90c48f15c39764eeca067066e6efd
- clm_b1dbd2ca5dfce865a0c23e8472d8e1e88b70d723c388d6f9d7b6b936ccae5d8b
maturity: draft
page_id: pg_9874205e2b185911ae80b7d2b24739a7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8b423c7f8e1e5eb09bfee65848222ffc
title: ZhixiangLuo/10xProductivity/README.md @ 9a7da40bc798
updated_at: '2026-09-14T04:34:21Z'
---

# ZhixiangLuo/10xProductivity/README.md @ 9a7da40bc798

<!-- rcw:begin owner=source:src_8b423c7f8e1e5eb09bfee65848222ffc block=evidence -->
- The architecture separates a push layer (triggers that detect events via desktop/browser notifications, sessions, email, or polling and wake workflows) from a pull layer (tool connections that fetch context or act), with a thin local runtime handling polling, scheduling, state, dedupe, replies, and agent invocation. [@claim:clm_03da786cb1e986324876eeb3e75a1dd024f28e3b5322f9305e90dd8f763f0eb1]
- The project is positioned as a local-first personal AI assistant stack that reuses the user's existing coding agent, browser sessions, desktop apps, and permissions, explicitly avoiding new company-wide platforms, Slack apps, webhooks, or IT approval. [@claim:clm_068019eb27bee991cf8ead377e1c05a04b8c701f520f710b23b4e3c881a0df57]
- Setup requires a coding agent (Cursor, Claude Code, or Codex), a Python virtualenv with an editable dev install (pip install -e ".[dev]"), and optionally Python/Playwright setup per setup-python.md. [@claim:clm_15d4cdd5398ecc3101971110c8412b4c42ec86980f9a209a15a30b39a14a89ee]
- A second CLI, 10x-standup-prep, supports a --meeting-context flag and a --dry-run mode; posting to Slack requires reviewing output first and setting TENX_STANDUP_PREP_SLACK_CHANNEL before using --post. [@claim:clm_1f3451b5fef5a21d4077c8ce5bb84ca8f4ab660e2e6e36ff4d435370789cac88]
- Packaged Cursor and Claude Code skills cover tool setup, enterprise search, workflow creation, UI surface discovery, colleague distillation, and an assistant inbox/orchestrator skill. [@claim:clm_69aa9a134f225fb648805cabe845156d4f62a23851e72d3f0c06e007e8af48b3]
- The runtime exposes a CLI entry point 10x-host that takes --trigger, --workflow, and --engine arguments, e.g. running a slack-polling trigger with the assistant workflow and the cursor engine. [@claim:clm_701d4f4cf6e92d869a0fbe8a1a44bb64694ab3eef424c4a71f9da30d32056670]
- Repository development practice: contributions follow a 'run before you write' rule — every snippet must be executed and seen to succeed — and new tool work starts in TENX_PRIVATE_DIR/personal/, never directly in tool_connections/, with promotion to the public repo only via staging/ and a PR after verification and scrubbing. [@claim:clm_88a1bd886750686b0b20c4df52c45a5556c140c89121d5076bf250fed9809725]
- Per the README's status table, tool connections, enterprise search, and agent skills are available today, while triggers, runtime, and reusable workflows are early; learning and memory (scheduled reflection, durable memory) are roadmap items not yet complete. [@claim:clm_88fb1340656cfebd26cee1886e7ced6d0ab09ee1500cbc411cd840262b348812]
- Private runtime state lives outside the repo by default under ~/.10xProductivity/ (.env tokens, personal/ recipes, verified_connections.md, tmp/ for trigger and scheduler state), overridable via the TENX_PRIVATE_DIR environment variable. [@claim:clm_9950b4a60820e773f2ce4d51d2fabea10b1407ce6130d14c82b677d087cfff22]
- The README warns that some workflows automate actions on external platforms in ways that may violate platform Terms of Service, and directs users to LEGAL_NOTICE.md before running automation scripts. [@claim:clm_a0506b716647e182c956caf14563aa7d5fe90c48f15c39764eeca067066e6efd]
- The repository is organized into tool_connections/, triggers/, runtime/, workflows/, tests/, .cursor/skills/, .claude/skills/, and staging/, plus setup guides such as setup.md, add-new-tool.md, and setup-python.md. [@claim:clm_b1dbd2ca5dfce865a0c23e8472d8e1e88b70d723c388d6f9d7b6b936ccae5d8b]
<!-- rcw:end owner=source:src_8b423c7f8e1e5eb09bfee65848222ffc block=evidence -->

## Researcher notes

