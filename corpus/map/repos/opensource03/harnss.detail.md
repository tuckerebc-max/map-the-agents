# opensource03/harnss -- full detail

[Back to orientation](harnss.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/opensource03/harnss/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/3c8c248556fb7ab2.json](../../../wiki/dossiers/opensource03/harnss/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/3c8c248556fb7ab2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (5 claim(s))

- [observation/documented] The app supports three execution engines: Claude Code via the Anthropic Agent SDK, Codex via a JSON-RPC app-server, and ACP agents via the Agent Client Protocol. -- evidence: [README.md#L149-L153](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L149-L153) (`clm_cc5acf0bca626beae7a3848c6b0011114324cf0b2c625bd74662f59503c64ed4`)
- [observation/documented] MCP servers can be connected per project over stdio, SSE, or HTTP transports, with in-app OAuth handling and token persistence across sessions. -- evidence: [README.md#L97-L97](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L97-L97), [README.md#L173-L173](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L173-L173) (`clm_a38a80c8d755af0b21b6994f25d266411d4b0ccf1c36cad1deb28eff798fbcd2`)
- [observation/documented] Built-in panels include a multi-tab PTY terminal backed by native shell processes, an embedded browser, git staging/commit/push with worktree support, and AI-generated commit messages from the staged diff. -- evidence: [README.md#L105-L105](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L105-L105), [README.md#L101-L101](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L101-L101) (`clm_6df7c027fbc627cdd89d350643de5f59c319f85be95331bc0126b5bd99f26f12`)
- [observation/documented] An Agent Store lets users browse and install agents from the ACP community registry, or define custom agents with command, arguments, environment variables, and icon via Settings. -- evidence: [README.md#L167-L167](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L167-L167), [README.md#L113-L113](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L113-L113) (`clm_c430cce67ac5dfb5d3d8fe15af8c438cf6ed71b41416a81b3407163f4ecf20d9`)
- [observation/documented] Voice input is supported via native macOS dictation or an on-device Whisper model requiring no API key, alongside configurable OS notifications for approvals, permission prompts, and session events. -- evidence: [README.md#L129-L129](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L129-L129) (`clm_21735609f7c09dfc9e6248cfd20a40acde943779b9e55ce09338c54a7bd52b6a`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors should fork the repo, create a feature branch, follow conventions in CLAUDE.md, test with pnpm dev, and open a pull request; local development uses pnpm install and pnpm dev. -- evidence: [README.md#L213-L216](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L213-L216), [README.md#L194-L199](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L194-L199) (`clm_57fccd7aa1f39faf94b4d2a0343c00eb5c377f5e8608898593e9efce818a2afa`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Harnss is a cross-platform desktop app providing a single interface to run, manage, and switch between AI coding agents including Claude Code, Codex, and ACP-compatible agents. -- evidence: [README.md#L26-L26](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L26-L26) (`clm_858ee248c94c03ff299f784e6055eecbe63e31232a5601d22a135b89f5192f09`)
- [observation/documented] Tool calls render as interactive cards with word-level diffs, syntax highlighting, inline bash output, nested subagent progress tracking, and a per-turn Changes panel. -- evidence: [README.md#L93-L93](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L93-L93) (`clm_ee9c34132fb7cd3faaab7213c9bd19ebd165621de536e281d07e8a6d38dfd274`)

## memory-state (1 claim(s))

- [observation/documented] Sessions, history, and panel settings are scoped per project; projects map to disk folders and can be grouped into named Spaces with custom icons and colors. -- evidence: [README.md#L109-L109](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L109-L109) (`clm_7f1ca87a67f8f38107fe4dc17f40552a69c818cf9d5c19cdbeb50b45842b929e`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product offers three permission levels (Ask First, Accept Edits, Allow All) plus a plan mode where the agent drafts a plan before changes; modes can be switched mid-session without losing context. -- evidence: [README.md#L117-L117](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L117-L117) (`clm_b92dd9cb97c61d2f931ca91890f57e2c674f7669593ccb09238f54715ea292de`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running Claude Code requires a Claude account (subscription or API key); Codex requires the Codex CLI in PATH plus an OpenAI API key or ChatGPT account; ACP agents have agent-specific requirements. -- evidence: [README.md#L149-L153](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L149-L153) (`clm_51f068d7ff7e96dfac712ab7556441697e9100da1fc38e99119e81ffd7aa08b7`)

## limitations (2 claim(s))

- [observation/documented] Pre-built release binaries are currently unsigned, requiring macOS users to bypass Gatekeeper via right-click Open and Windows users to click through Defender warnings. -- evidence: [README.md#L179-L180](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L179-L180) (`clm_683238a7e6f7bd6a2f8d665581adb9bd6667c8d0f1be4e5c0f29d56bb57c233b`)
- [observation/documented] The README states Harnss is in early development with issues to be expected, and a large rewrite toward a more production-ready app is pending. -- evidence: [README.md#L4-L5](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L4-L5), [README.md#L1-L2](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L1-L2) (`clm_b6b3ffc886dbf4153a1c33c16b39888d05542927fd418cd9e39ed7283894562c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

