---
access: public
aliases: []
claim_ids:
- clm_1aa62b3f9bf573abec8aaa02356bec1f8463366f73aac39a829e198d15b6c490
- clm_3ed2955cbcbfe13de480288197471e8a07f4f1b57883a3b3367d18588f7f5676
- clm_414978fb23471071bb022d4cf608c86ee6867ee13e6ad9a60d81d0ca52c71f69
- clm_4ae536c8d4bfc6d3685b31f4c3e160a2720366ec7111e1f4906e8089e5fe2a13
- clm_4f8d76953140fdfd7d146670d8c5e9dd2a9c28a6595be59bc45bb0036bcc6a23
- clm_55718a22ece9d6a122c394ad39ed3fdc21cdd4afca19a238bc2dde8da0525145
- clm_754d00b01ed591828812e41971dfb6f30ace674d7ad6e0e7691abc9118ef4d82
- clm_7f35ecc6278348c7f94936dc04ee74c2e91852fbd716819ceb6918d9e18075db
- clm_8b6d78c7883d39f4daaed1ea64c035cbcc03b56b98af96984f64eee318396bd2
- clm_c6de7e1d48e5a0b82ad01433fe0a14b228ae2cee14bd2f607cafe5a17e4e34cb
- clm_e4867eaf18a8eb7ef33839806768004447c1628fc545d196f5445953c2c808d4
maturity: draft
page_id: pg_f935c052b21a5b0b8a5c4e3aecbc1c9b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a79e9df099a05d4196058e640a174b9b
title: bastani-inc/atomic/README.md @ ca64fa07885f
updated_at: '2026-09-14T03:05:36Z'
---

# bastani-inc/atomic/README.md @ ca64fa07885f

<!-- rcw:begin owner=source:src_a79e9df099a05d4196058e640a174b9b block=evidence -->
- Atomic implements the Agent Skills standard and can use configured Claude Code or Codex skill directories without rewriting them; skills can be auto-selected from descriptions or invoked with /skill:<name>. [@claim:clm_1aa62b3f9bf573abec8aaa02356bec1f8463366f73aac39a829e198d15b6c490]
- Atomic is a fork of Pi and works with providers, tools, MCP servers, skills, and extensions from an existing Pi stack; it connects to model providers directly rather than wrapping other coding tools. [@claim:clm_3ed2955cbcbfe13de480288197471e8a07f4f1b57883a3b3367d18588f7f5676]
- Workflows persist artifacts such as plans, logs, transcripts, reviewer notes, check output, and summaries; research commonly lives in research/ and specs in specs/. [@claim:clm_414978fb23471071bb022d4cf608c86ee6867ee13e6ad9a60d81d0ca52c71f69]
- The Linux musl release archives bundle their C++ runtime and run on stock Alpine, but Android and Termux are unsupported; provider availability depends on credentials, subscription, region, and the provider catalog. [@claim:clm_4ae536c8d4bfc6d3685b31f4c3e160a2720366ec7111e1f4906e8089e5fe2a13]
- Stages can prompt an agent, run tools, call MCP servers, save artifacts, branch, retry, run in parallel, or pause for approval; specialized subagents handle focused work while a parent agent or workflow controls the larger task. [@claim:clm_4f8d76953140fdfd7d146670d8c5e9dd2a9c28a6595be59bc45bb0036bcc6a23]
- The CLI exposes workflow management commands including /workflow list, inputs, status, connect, quit, and resume; quitting pauses a run so it can resume later. [@claim:clm_55718a22ece9d6a122c394ad39ed3fdc21cdd4afca19a238bc2dde8da0525145]
- Atomic ships three top-level building blocks: workflows, skills, and specialized subagents, with nine bundled subagent definitions such as worker, debugger, and codebase-analyzer. [@claim:clm_754d00b01ed591828812e41971dfb6f30ace674d7ad6e0e7691abc9118ef4d82]
- Non-interactive use is supported via atomic -p "<prompt>", which prints the response and exits; provider credentials are stored in ~/.atomic/agent/auth.json with owner-only permissions where the platform supports them. [@claim:clm_7f35ecc6278348c7f94936dc04ee74c2e91852fbd716819ceb6918d9e18075db]
- Package installation requires Node.js 22.19 or newer plus npm, pnpm, Yarn, or Bun (Bun 1.4.2+ for Bun installs); a self-contained release archive path needs no Node.js or package manager. [@claim:clm_8b6d78c7883d39f4daaed1ea64c035cbcc03b56b98af96984f64eee318396bd2]
- Workflows are authored as TypeScript workflow({...}) definitions whose stage dependencies must form a directed acyclic graph; cyclic graphs are unsupported, and loop/repair iterations must create distinct tracked work per iteration. [@claim:clm_c6de7e1d48e5a0b82ad01433fe0a14b228ae2cee14bd2f607cafe5a17e4e34cb]
- Atomic has no built-in sandbox or command-level shell permission gate; tools and extensions run with the user's permissions, and the README recommends running autonomous work in a devcontainer, VM, or remote machine. [@claim:clm_e4867eaf18a8eb7ef33839806768004447c1628fc545d196f5445953c2c808d4]
<!-- rcw:end owner=source:src_a79e9df099a05d4196058e640a174b9b block=evidence -->

## Researcher notes

