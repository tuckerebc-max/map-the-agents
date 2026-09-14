---
access: public
aliases: []
claim_ids:
- clm_1618d0c863512ddecae3a20455489038043eb3a765d0a875b558426c5ae895ab
- clm_19a7406c704a6ca45244343d8b40471d776f4f4abc55eb6b864a2f93586a3ba8
- clm_2590d0d49472d28229ed6c4ef24d8119fc575a6c82c05b5f8167c8f276a0ab09
- clm_2668981d4fdf7c9838bca14c8b85605ddd9670824ca14194522bc22c226df6a5
- clm_4bfb4238e3b08aa99cf002e5a6e9b312975ac82ac5e682045d97d82601c389e2
- clm_4d7e8a9fb96c733758a26537a268fb98ee4ca072a24a45ed94a7d825483a8779
- clm_848c248d4a02dd987968653d4cdc6c0159b48d9a8dbdd3ca784c2588c3232755
- clm_c9015b4119d240afdb1e979a0b8fa9e0903f896d7bb8d122a978650d33311bd1
- clm_ca4ec86b62900a295ebab566ac1baaf7f035593a2fa23cc88c55fac1ffac1f4a
- clm_cf60fd9a8bb028ed440145187df1d19f71fb91fb9280c99d461ecd01cd5eb738
- clm_de753f0d1ff4bba374e8062c9f6b6528daee48cf9897bee35ba6273f5b71b823
- clm_f27ed7772d5e1925479c831eab57862470a7902808d3f643a20a49a7262392ef
maturity: draft
page_id: pg_33c9d1c245495661a5b4caefabe6f491
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_866d8e990906542e96a92c6d4df66b1d
title: changkun/wallfacer/README.md @ 9acd2b092578
updated_at: '2026-09-14T01:40:39Z'
---

# changkun/wallfacer/README.md @ 9acd2b092578

<!-- rcw:begin owner=source:src_866d8e990906542e96a92c6d4df66b1d block=evidence -->
- The product provides oversight tooling: per-task event timelines, diffs against the default branch, AI-generated oversight summaries, and token/cost tracking by task, activity, and turn. [@claim:clm_1618d0c863512ddecae3a20455489038043eb3a765d0a875b558426c5ae895ab]
- Users control agent autonomy per task, spec, or project, from fully autonomous loops (implement, test, commit, push) to stepping in at any point. [@claim:clm_19a7406c704a6ca45244343d8b40471d776f4f4abc55eb6b864a2f93586a3ba8]
- Specs follow a seven-state lifecycle (vague, drafted, validated, testing, complete, plus stale and archived) with a dependency DAG and atomic dispatch and undo. [@claim:clm_2590d0d49472d28229ed6c4ef24d8119fc575a6c82c05b5f8167c8f276a0ab09]
- Execution is built from agents (sub-roles like impl, test, commit-msg, title, oversight), flows composing agents into pipelines, tasks that pick a flow, and scheduled routines. [@claim:clm_2668981d4fdf7c9838bca14c8b85605ddd9670824ca14194522bc22c226df6a5]
- User-authored agents and fleets are defined as YAML under ~/.wallfacer/{agents,flows}/ and edited on a unified Agent Graph surface without restarting the server. [@claim:clm_4bfb4238e3b08aa99cf002e5a6e9b312975ac82ac5e682045d97d82601c389e2]
- The CLI surface includes wallfacer run, status, spec, auth, web, and doctor, with -help flags per command. [@claim:clm_4d7e8a9fb96c733758a26537a268fb98ee4ca072a24a45ed94a7d825483a8779]
- The product is harness-agnostic, working with Claude Code, Codex, Cursor, OpenCode, and Pi via a pluggable harness layer, and users bring their own LLM provider. [@claim:clm_848c248d4a02dd987968653d4cdc6c0159b48d9a8dbdd3ca784c2588c3232755]
- Wallfacer is described as an autonomous engineering platform spanning chat, specs, task boards, and code, with agents operating at every abstraction level. [@claim:clm_c9015b4119d240afdb1e979a0b8fa9e0903f896d7bb8d122a978650d33311bd1]
- Wallfacer is pre-1.0; the HTTP API, ~/.wallfacer on-disk layout, and WALLFACER_* environment variables may change between releases, and all Go packages live under internal/ with no importable public API. [@claim:clm_ca4ec86b62900a295ebab566ac1baaf7f035593a2fa23cc88c55fac1ffac1f4a]
- Specs serve as an intermediate representation: ideas become structured, versioned, reviewable specs that agents reason about and implement against, rather than going straight to code. [@claim:clm_cf60fd9a8bb028ed440145187df1d19f71fb91fb9280c99d461ecd01cd5eb738]
- The planning chat exposes slash commands such as /create, /validate, /break-down, and /dispatch to drive the spec lifecycle. [@claim:clm_de753f0d1ff4bba374e8062c9f6b6528daee48cf9897bee35ba6273f5b71b823]
- Each task runs as a host process in its own git worktree, enabling parallel agent execution without conflicts. [@claim:clm_f27ed7772d5e1925479c831eab57862470a7902808d3f643a20a49a7262392ef]
<!-- rcw:end owner=source:src_866d8e990906542e96a92c6d4df66b1d block=evidence -->

## Researcher notes

