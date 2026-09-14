# generalaction/emdash -- full detail

[Back to orientation](emdash.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/generalaction/emdash/fccf350847097c8f9d9de3e7e5c98b0d292a4554/a2795a7f46ba37a1.json](../../../wiki/dossiers/generalaction/emdash/fccf350847097c8f9d9de3e7e5c98b0d292a4554/a2795a7f46ba37a1.json)

## specifications (1 claim(s))

- [observation/documented] Emdash is a desktop app for running AI coding agents in parallel, with each task isolated in its own Git worktree so multiple fixes or features can be explored, reviewed, and merged. -- evidence: [README.md#L21-L23](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L21-L23) (`clm_6514d5b0d6701d5dd13283e71cfc97e125a884d14b6dc4257923ca12403de3fd`)

## components (3 claim(s))

- [observation/documented] Features include running multiple agents without juggling terminals, per-agent worktree/branch isolation, sending issues from trackers like Linear, GitHub, Jira, and GitLab into agents, and reviewing diffs, creating PRs, inspecting CI checks, and merging from one place. -- evidence: [README.md#L32-L37](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L32-L37) (`clm_7d08750c5326d617b80795b420eb2361d0355f7a86b6c6d3a94b02ad00f3fa23`)
- [observation/documented] For agents with lifecycle-hook support, Emdash installs marker-tagged hook entries in the agent's user-level config to track status, notifications, and resumable sessions, and the hooks do nothing when the agent runs outside Emdash. -- evidence: [README.md#L57-L59](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L57-L59) (`clm_805b85d9785cb040ac97653d33c1df42f89fd638524b1359c7aad5b0571cc28a`)
- [observation/documented] Remote projects connect over SSH/SFTP with support for SSH agent, key, and password authentication, and credentials are stored in the OS keychain. -- evidence: [README.md#L66-L68](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L66-L68) (`clm_9e7fc5ac97f25d6e15cc3814748100478487b97578df8f9963da3ce9e2a55821`)

## design-choices (2 claim(s))

- [observation/documented] The app is local-first: app state lives in a local SQLite database, and Emdash does not send the user's code or chats to Emdash servers, though agent CLIs may send data to their own providers. -- evidence: [README.md#L77-L78](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L77-L78), [README.md#L74-L75](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L74-L75) (`clm_a21824de18d7b92dd3510f3c36b0a8a565f0de8bfb0cbd648456d3314f8fdede`)
- [observation/documented] Telemetry is optional and can be disabled in Settings or by launching with TELEMETRY_ENABLED=false. -- evidence: [README.md#L82-L84](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L82-L84), [README.md#L80-L80](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L80-L80) (`clm_3d4cd6a4a9c73b66fe5cf10bc74a617403e06e8f73625ff4489adb8b579ecd83`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the merge gate is four root commands (format, lint, typecheck, test) run via pnpm/Nx, with CI running a code-consistency workflow using nx affected on touched projects and dependents, and browser Vitest projects skipped in CI. -- evidence: [AGENTS.md#L213-L228](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L213-L228), [AGENTS.md#L60-L66](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L60-L66) (`clm_19fa31ca829cb9298196219c6f446d30c9136399ad70d71914fb43d3d128b84b`)
- [observation/documented] Repository development practice: the repo is a pnpm workspace monorepo; only pnpm on PATH is needed since package.json pins pnpm 10.28.2 and Node 24.14.0 with onFail download, so the toolchain self-provisions. -- evidence: [AGENTS.md#L49-L54](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L49-L54), [AGENTS.md#L10-L14](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L10-L14) (`clm_02abb82eb315375260f135cd7ac118e1a718adb2f167faae6a06a6494712bebb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product works with local projects and remote machines over SSH, and drives CLI agents the user already has, such as Claude Code, Codex, OpenCode, and Amp. -- evidence: [README.md#L25-L26](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L25-L26) (`clm_03adde549d86554f5a38331d79b1938234767068a65129b1b15e86f9b070e937`)
- [observation/documented] Emdash automatically detects installed provider CLIs and supports agents including Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, and GitHub Copilot. -- evidence: [README.md#L53-L55](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L53-L55) (`clm_0da47d90d37e39b1b0862666b0a0b9bb64201e01ffd1f8bd795344388a09cd27`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Desktop builds are distributed for macOS (Homebrew cask plus Apple Silicon and Intel DMGs), Windows (MSI installer and portable exe), and Linux x64/ARM64 (AppImage, DEB, RPM). -- evidence: [README.md#L41-L46](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L41-L46) (`clm_77cfed20756f688336c7c0254efe2120271531ec035d1bd922fd196624f90964`)

## limitations (1 claim(s))

- [observation/documented] The README notes that agent CLIs may send code, prompts, and context to their own providers, so data handling depends on which provider the user chooses. -- evidence: [README.md#L77-L78](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L77-L78) (`clm_4d7dad5aa85c07803d0b404239d2d754bcdee89d2c16d5841cb68496915c99b7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

