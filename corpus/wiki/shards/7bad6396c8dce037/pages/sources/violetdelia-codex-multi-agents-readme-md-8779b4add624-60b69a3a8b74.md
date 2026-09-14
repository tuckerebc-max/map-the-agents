---
access: public
aliases: []
claim_ids:
- clm_06991b2811b02eaca5c47dcf1d64959573cd7d114bff4735993285b6ca0cc04b
- clm_5061463f4cbc54d88c9be68960b0be61c4c4c68493a0d3b812b06a570d58383a
- clm_5180424416e410768227d15de4d4d541104dee7a7a555ac457bea5f6fdbb687f
- clm_970d2baab40f6bc72574d106ee2f9a2071820e73da5437f807a70ac2b4fa02a6
- clm_a9c7deeeb1cfb2ba1e62ba78e4c86421b9a837a710bf5edf59f3d6d3dc94b70d
- clm_b72d01d9c33d35a0b75aa168d9c0a31ccba70a8278b64d852a5705827c70772e
- clm_c452aa956a39f8404b20cf3c0bceeec0b7dd010581c04abf18816276f59cb8fe
- clm_e7738045c10138a0f299fd3b1a852532864a066a2e8030764e0051a6bb0f2e29
- clm_ed4e2989e3bbc3befb9f60c765a6a6131e9dabf6c6d270576a45e31fc262c310
maturity: draft
page_id: pg_764edb86a28350e4893d60b69a3a8b74
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_134570d80cd35726a3e8327fc33698a3
title: violetDelia/codex-multi-agents/README.md @ 8779b4add624
updated_at: '2026-09-14T03:22:08Z'
---

# violetDelia/codex-multi-agents/README.md @ 8779b4add624

<!-- rcw:begin owner=source:src_134570d80cd35726a3e8327fc33698a3 block=evidence -->
- A tmux-based communication CLI, codex-multi-agents-tmux.sh, provides -init-env to initialize an agent session and -talk with -from/-to/-agents-list/-message/-log to send messages between agents. [@claim:clm_06991b2811b02eaca5c47dcf1d64959573cd7d114bff4735993285b6ca0cc04b]
- The README recommends a task pipeline template: spec task, implementation task, review/re-review task, merge task, and sync-confirmation task. [@claim:clm_5061463f4cbc54d88c9be68960b0be61c4c4c68493a0d3b812b06a570d58383a]
- The toolkit exposes a roster-management CLI, codex-multi-agents-list.sh, supporting at least -file, -status, -add (with -name and -type), and -init flags per the README examples. [@claim:clm_5180424416e410768227d15de4d4d541104dee7a7a555ac457bea5f6fdbb687f]
- The toolkit is packaged as a skill under skills/codex-multi-agents, with example files (agents-lists.md, TODO.md, commands-quickstart.md, common-guides.md), a SKILL.md, and an EXTENSIONS.md covering division of labor, dispatch, blocking, merge, and sync strategies. [@claim:clm_970d2baab40f6bc72574d106ee2f9a2071820e73da5437f807a70ac2b4fa02a6]
- Dispatch messages are advised to always state the worktree path (verified to exist), an acceptance command such as a pytest invocation, and to use -pause and ask when blocked. [@claim:clm_a9c7deeeb1cfb2ba1e62ba78e4c86421b9a837a710bf5edf59f3d6d3dc94b70d]
- The system coordinates work among named roles (e.g. 管理员 dispatching to 小王) via a shared agents-list file and per-task worktree paths. [@claim:clm_b72d01d9c33d35a0b75aa168d9c0a31ccba70a8278b64d852a5705827c70772e]
- Documented failure modes include 'target session not found' (fixed by running tmux -init-env first), 'worktree not found' (create or fix the path before dispatch), and 'task already exists in running list' when re-dispatching a running task. [@claim:clm_c452aa956a39f8404b20cf3c0bceeec0b7dd010581c04abf18816276f59cb8fe]
- A task CLI, codex-multi-agents-task.sh, operates on a TODO file and supports -new (with -from, -to, -worktree, -log, -info), -dispatch, -done, -pause, -continue, and -status -task-list operations. [@claim:clm_e7738045c10138a0f299fd3b1a852532864a066a2e8030764e0051a6bb0f2e29]
- Task state appears persisted in the TODO file passed via -file, and markdown log files (used with -new and -done in the examples) appear to record task history. [@claim:clm_ed4e2989e3bbc3befb9f60c765a6a6131e9dabf6c6d270576a45e31fc262c310]
<!-- rcw:end owner=source:src_134570d80cd35726a3e8327fc33698a3 block=evidence -->

## Researcher notes

