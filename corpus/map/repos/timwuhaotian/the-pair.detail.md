# timwuhaotian/the-pair -- full detail

[Back to orientation](the-pair.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/timwuhaotian/the-pair/8d678875f777fb838ed944daf376d5220e39bd59/26b6dc489930ec38.json](../../../wiki/dossiers/timwuhaotian/the-pair/8d678875f777fb838ed944daf376d5220e39bd59/26b6dc489930ec38.json)

## specifications (1 claim(s))

- [observation/documented] The Pair is a free, open-source desktop app running two AI coding agents: a read-only Mentor that plans and reviews, and an Executor that writes code and runs commands, cross-checking each other's work. -- evidence: [README.md#L53-L53](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L53-L53), [llms.txt#L3-L3](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/llms.txt#L3-L3) (`clm_253c50f7f0225a6bef01fb1103d26154a5cca98057d9ef0dd5fea2de3111677f`)

## components (1 claim(s))

- [observation/documented] The documented Rust backend includes PairManager (lifecycle), MessageBroker (state machine), ProcessSpawner (multi-provider), ContextBridge, QualityGate, SmartPause, Git Tracker, Worktrees, Session Snapshot, Resource Monitoring, Acceptance, and Report Generator modules. -- evidence: [README.md#L266-L301](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L266-L301) (`clm_57fb6157afd3c0dbb4d46ad23f796ee4cea74f251cdd76496b2eb5ce90021b00`)

## design-choices (1 claim(s))

- [observation/documented] Design principles emphasize trust through transparency (visible agent activity, resource usage, git changes), status-driven color coding (blue mentoring, purple executing, amber paused, green finished), and refined glassmorphism aesthetics. -- evidence: [.impeccable.md#L22-L26](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/.impeccable.md#L22-L26), [.impeccable.md#L15-L15](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/.impeccable.md#L15-L15) (`clm_7c2ed2e66e2f32740547a82738d59b67c1eb480e48bfa83adbb2c2b589b4aef3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's Development section documents npm scripts for building and testing, including npm test for JS and Rust unit tests, typecheck, lint, e2e, and platform-specific build commands. -- evidence: [README.md#L373-L394](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L373-L394), [README.md#L343-L348](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L343-L348), [README.md#L171-L176](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L171-L176) (`clm_75cf532ff4c887ec864560f8036d354d79a206bdcd580e93a910bc65d9d052c9`)

## skills-patterns (1 claim(s))

- [observation/documented] The Japanese README documents a skill system that lets users attach project-specific skill files to guide agent behavior. -- evidence: [README.ja.md#L80-L91](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.ja.md#L80-L91) (`clm_ab744fbdb91145789fd8ca5362b29de2ec26ee50256384fd977c754606b95ee1`)

## interfaces (2 claim(s))

- [observation/documented] The product is model-agnostic: it can pair provider CLIs including opencode, Claude Code, OpenAI Codex, Gemini CLI, and Kimi Code in any combination, plus local models via Ollama. -- evidence: [README.md#L53-L53](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L53-L53), [README.md#L422-L422](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L422-L422), [llms.txt#L17-L22](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/llms.txt#L17-L22) (`clm_e503dbd2ed75c7658f7ddf87c196fc2e6291cbd052a168000735f39a19ec893b`)
- [observation/documented] Besides the desktop app, a terminal CLI edition called Pair Code is available on npm (installable globally via npm install -g pair-code), sharing the same Mentor + Executor design. -- evidence: [README.md#L117-L120](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L117-L120), [README.md#L115-L115](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L115-L115), [README.md#L122-L122](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L122-L122) (`clm_d57c855cabaf32f9c107aaeded378a9909e258a1d3d4bc6ca20ee3e979ebd5c7`)

## memory-state (1 claim(s))

- [observation/documented] Session snapshots are saved automatically; on relaunch the app detects interrupted sessions and offers to restore them with full conversation history and turn state. -- evidence: [llms.txt#L26-L31](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/llms.txt#L26-L31), [README.md#L446-L446](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L446-L446), [README.md#L89-L101](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L89-L101) (`clm_44c3166fc8505eaa9932da57e432394649fb40b2a15c7cb52e50c9d164e5fdfc`)

## orchestration (2 claim(s))

- [observation/documented] The agent workflow loops through Mentoring, Executing, and Reviewing stages, and runs are capped at a flat 20-iteration default, pausing for human review when the budget is reached. -- evidence: [README.md#L442-L442](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L442-L442), [README.md#L319-L319](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L319-L319), [README.md#L305-L317](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L305-L317) (`clm_4045cbc87953f2c5ec04e42aa6a9f0bd67fc7e1d34d20d43ae44827b13b42a77`)
- [observation/documented] Coordination features include structured handoff prompts, quality gates, smart-pause logic, and a per-turn step-cycle guard that kills runaway agent processes to prevent CPU exhaustion. -- evidence: [README.md#L442-L442](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L442-L442), [README.md#L128-L145](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L128-L145), [README.md#L89-L101](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L89-L101) (`clm_9a0121c1ee5328eb5810974e4f291e190d8510fb5559d18b000a65336f0cd78b`)

## tools-permissions (1 claim(s))

- [observation/documented] Full automation mode operates with workspace-scoped permissions, and each pair stores its own runtime permissions under .pair/runtime/<pairId>/; global opencode permissions are not modified — permissions are session-specific. -- evidence: [README.md#L243-L243](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L243-L243), [README.md#L245-L246](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L245-L246), [README.md#L128-L145](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L128-L145) (`clm_1c670e34e6b9c69d0e2ee32123e7192ff5aec08d3d8dd7d05537f2c5bb8473ca`)

## evaluation (1 claim(s))

- [inference/documented] No benchmark or agent-performance evaluation harness appears in the provided evidence; the only test-related material is the repository's own unit/e2e test scripts, so agent task performance appears unmeasured in this snapshot. -- evidence: [README.md#L373-L394](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L373-L394) (`clm_f6b04680f526d06708e644c382a79f806d73e6abb428163f83346a458c70e5c6`)

## dependencies (2 claim(s))

- [observation/documented] The tech stack is Tauri 2.x with a Rust backend, React 19 + TypeScript frontend, Tailwind CSS v4, Zustand state, Framer Motion, and Lucide React icons. -- evidence: [README.md#L410-L410](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L410-L410), [README.md#L254-L262](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L254-L262) (`clm_31ef6244862bc709729aed83ece8c1b746bbd0c7a535af1539b829750d498e84`)
- [observation/documented] The app requires at least one AI provider CLI (opencode, Claude Code, Codex, Antigravity, or Kimi Code); Codex, Claude, Gemini, and Kimi are detected from installed CLIs and sign-in state. -- evidence: [README.md#L214-L215](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L214-L215), [README.md#L239-L239](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L239-L239), [README.md#L188-L189](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L188-L189) (`clm_9a08c5d1988fd4fb42657cb85a7ccaceb55dcced7ae2070c3296b9eb07a53d94`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

