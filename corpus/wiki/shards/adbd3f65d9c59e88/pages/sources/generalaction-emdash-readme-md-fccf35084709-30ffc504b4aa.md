---
access: public
aliases: []
claim_ids:
- clm_03adde549d86554f5a38331d79b1938234767068a65129b1b15e86f9b070e937
- clm_0da47d90d37e39b1b0862666b0a0b9bb64201e01ffd1f8bd795344388a09cd27
- clm_3d4cd6a4a9c73b66fe5cf10bc74a617403e06e8f73625ff4489adb8b579ecd83
- clm_4d7dad5aa85c07803d0b404239d2d754bcdee89d2c16d5841cb68496915c99b7
- clm_6514d5b0d6701d5dd13283e71cfc97e125a884d14b6dc4257923ca12403de3fd
- clm_77cfed20756f688336c7c0254efe2120271531ec035d1bd922fd196624f90964
- clm_7d08750c5326d617b80795b420eb2361d0355f7a86b6c6d3a94b02ad00f3fa23
- clm_805b85d9785cb040ac97653d33c1df42f89fd638524b1359c7aad5b0571cc28a
- clm_9e7fc5ac97f25d6e15cc3814748100478487b97578df8f9963da3ce9e2a55821
- clm_a21824de18d7b92dd3510f3c36b0a8a565f0de8bfb0cbd648456d3314f8fdede
maturity: draft
page_id: pg_5481b869184c56aa9b0c30ffc504b4aa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5879b01558695dffbeacc4234d326bc9
title: generalaction/emdash/README.md @ fccf35084709
updated_at: '2026-09-14T01:50:03Z'
---

# generalaction/emdash/README.md @ fccf35084709

<!-- rcw:begin owner=source:src_5879b01558695dffbeacc4234d326bc9 block=evidence -->
- The product works with local projects and remote machines over SSH, and drives CLI agents the user already has, such as Claude Code, Codex, OpenCode, and Amp. [@claim:clm_03adde549d86554f5a38331d79b1938234767068a65129b1b15e86f9b070e937]
- Emdash automatically detects installed provider CLIs and supports agents including Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, and GitHub Copilot. [@claim:clm_0da47d90d37e39b1b0862666b0a0b9bb64201e01ffd1f8bd795344388a09cd27]
- Telemetry is optional and can be disabled in Settings or by launching with TELEMETRY_ENABLED=false. [@claim:clm_3d4cd6a4a9c73b66fe5cf10bc74a617403e06e8f73625ff4489adb8b579ecd83]
- The README notes that agent CLIs may send code, prompts, and context to their own providers, so data handling depends on which provider the user chooses. [@claim:clm_4d7dad5aa85c07803d0b404239d2d754bcdee89d2c16d5841cb68496915c99b7]
- Emdash is a desktop app for running AI coding agents in parallel, with each task isolated in its own Git worktree so multiple fixes or features can be explored, reviewed, and merged. [@claim:clm_6514d5b0d6701d5dd13283e71cfc97e125a884d14b6dc4257923ca12403de3fd]
- Desktop builds are distributed for macOS (Homebrew cask plus Apple Silicon and Intel DMGs), Windows (MSI installer and portable exe), and Linux x64/ARM64 (AppImage, DEB, RPM). [@claim:clm_77cfed20756f688336c7c0254efe2120271531ec035d1bd922fd196624f90964]
- Features include running multiple agents without juggling terminals, per-agent worktree/branch isolation, sending issues from trackers like Linear, GitHub, Jira, and GitLab into agents, and reviewing diffs, creating PRs, inspecting CI checks, and merging from one place. [@claim:clm_7d08750c5326d617b80795b420eb2361d0355f7a86b6c6d3a94b02ad00f3fa23]
- For agents with lifecycle-hook support, Emdash installs marker-tagged hook entries in the agent's user-level config to track status, notifications, and resumable sessions, and the hooks do nothing when the agent runs outside Emdash. [@claim:clm_805b85d9785cb040ac97653d33c1df42f89fd638524b1359c7aad5b0571cc28a]
- Remote projects connect over SSH/SFTP with support for SSH agent, key, and password authentication, and credentials are stored in the OS keychain. [@claim:clm_9e7fc5ac97f25d6e15cc3814748100478487b97578df8f9963da3ce9e2a55821]
- The app is local-first: app state lives in a local SQLite database, and Emdash does not send the user's code or chats to Emdash servers, though agent CLIs may send data to their own providers. [@claim:clm_a21824de18d7b92dd3510f3c36b0a8a565f0de8bfb0cbd648456d3314f8fdede]
<!-- rcw:end owner=source:src_5879b01558695dffbeacc4234d326bc9 block=evidence -->

## Researcher notes

