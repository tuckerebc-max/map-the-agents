---
access: public
aliases: []
claim_ids:
- clm_9ef6f051824f29988f18b9657fd327695e71b43f41d44bdd19d0ad813380dd2f
- clm_b8fa05cd744f317cc191d5e3d32fc126c296dc3484d0b5ccb2aa0e1159a17183
- clm_bed82846bba2df1c454fe00cf07e28c8efc9a13835b6e95a60174f3bf6fd4678
- clm_c69dcfae9bab0606dc85417860b81d5ea2504fb44f3e4b8e46e463f2bac98f7a
- clm_db79fa544a6d6824eec2af225c6372862eda6ef3abb381a67a65d57dfa95b1ab
- clm_e3d36677ff0027f70548783283f85b5471fa4b8a435b3ab55768dc95fc6f1347
maturity: draft
page_id: pg_fcb915854c0a5ed59eca2eeadc98a20f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d816d6bc61495da18a93db27f4337791
title: zjrosen/perles/docs/CONTROL_PLANE.md @ f97afa7a7c44
updated_at: '2026-09-14T04:34:23Z'
---

# zjrosen/perles/docs/CONTROL_PLANE.md @ f97afa7a7c44

<!-- rcw:begin owner=source:src_d816d6bc61495da18a93db27f4337791 block=evidence -->
- The Control Plane supports multiple concurrent workflows with resource governance, health monitoring with stuck-workflow recovery, a dashboard TUI, and unified event aggregation. [@claim:clm_9ef6f051824f29988f18b9657fd327695e71b43f41d44bdd19d0ad813380dd2f]
- The dashboard TUI offers keyboard actions for navigating workflows, filtering, starting (s), pausing (p), stopping (x), creating (n/N), and opening detail views. [@claim:clm_b8fa05cd744f317cc191d5e3d32fc126c296dc3484d0b5ccb2aa0e1159a17183]
- Workflows move through states Pending, Running, Paused, Completed, Failed, and Stopped, with documented transitions including stop from pending, running, or paused. [@claim:clm_bed82846bba2df1c454fe00cf07e28c8efc9a13835b6e95a60174f3bf6fd4678]
- Control Plane behavior is configured in ~/.config/perles/config.yaml under orchestration.control_plane, with resource policy defaults of 5 concurrent workflows, 10 workers, 5 AI calls, and MCP ports 9000-9100. [@claim:clm_c69dcfae9bab0606dc85417860b81d5ea2504fb44f3e4b8e46e463f2bac98f7a]
- The Control Plane comprises ControlPlane (lifecycle entry point), Registry (in-memory workflow storage), Supervisor, ResourceScheduler, HealthMonitor, and CrossWorkflowEventBus. [@claim:clm_db79fa544a6d6824eec2af225c6372862eda6ef3abb381a67a65d57dfa95b1ab]
- Workflow instances track identity, state, priority, labels, timestamps, runtime infrastructure/session/MCP port, token budget, and last heartbeat/progress times; the Registry stores them in memory. [@claim:clm_e3d36677ff0027f70548783283f85b5471fa4b8a435b3ab55768dc95fc6f1347]
<!-- rcw:end owner=source:src_d816d6bc61495da18a93db27f4337791 block=evidence -->

## Researcher notes

