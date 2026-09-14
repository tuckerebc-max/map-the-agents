---
access: public
aliases: []
claim_ids:
- clm_02a67e5fbd8668710ef87e77d6a7f37949cf8271012baeaaa6a29ba1a0cc7255
- clm_2dcc3989d0b6b40663e797f5005a2a58a72f5c14f8a00c44668b7b263e68a213
- clm_308719839b799042f0d33499aa4b79f1fcaa4c07a263ae45f87f5b02c9a32039
- clm_3fc01ec2cf3f6d16e7e7d84b6c7883a00215834cb8cdad4775c380061ee79393
- clm_5166c510d594cfebe5ac17cd5ea67ddfbf4a3f819e189c51f5806b84a072ea55
- clm_58d49cb0f4bbf07aa2f5bbceb66c3bb570d386c58df373e7437011bad4b2d702
- clm_5fdb4a55b5f93b8e54ab4685d3897a0a1f243dcb65affd7316d34188af16d0ca
- clm_68b982be134a8e8f6e2c67f9ad093146411768073c38a57ca7321ec7be2855b5
- clm_a6b21826e31b91d28a20606c7db0ad041f1309935f98c49d0766efa6068f5a83
- clm_e49b74051b68b59b2510320f15ea466d3feb96182df10ee601e2eb6e1d9226fe
- clm_f723a986601aab63a03fdc1f1d0673b3deb16cf23fb23408fb86a3e98396b525
maturity: draft
page_id: pg_518a36828e9e59798347b0921aeb08d6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_074816f558215de0a5e8986c98cdcc40
title: respeak-io/episko/README.md @ 974192b540db
updated_at: '2026-09-14T02:36:30Z'
---

# respeak-io/episko/README.md @ 974192b540db

<!-- rcw:begin owner=source:src_074816f558215de0a5e8986c98cdcc40 block=evidence -->
- Task discovery never executes the project: just --dump, task --list and mise tasks ls sit behind a trust gate, Makefiles are parsed statically, and tasks that cannot run are shown greyed with the reason rather than hidden. [@claim:clm_02a67e5fbd8668710ef87e77d6a7f37949cf8271012baeaaa6a29ba1a0cc7255]
- Episko gives each coding-agent session its own real terminal; Claude Code and Codex are first-class integrated providers, while other installed CLIs work through a terminal-only adapter pane. [@claim:clm_2dcc3989d0b6b40663e797f5005a2a58a72f5c14f8a00c44668b7b263e68a213]
- Release builds target Apple-silicon macOS and Windows x64; Intel Macs are not covered and Linux is not packaged. The macOS build is self-signed but not notarized, so Gatekeeper quarantines the download and users must clear the quarantine flag before opening. [@claim:clm_308719839b799042f0d33499aa4b79f1fcaa4c07a263ae45f87f5b02c9a32039]
- The app discovers and runs tasks the project already ships — .episko/tasks.toml, .vscode/tasks.json and launch.json, package.json scripts, justfile, Taskfile.yml, mise.toml, Makefile, Cargo.toml — in the same PTY panes as agent sessions. [@claim:clm_3fc01ec2cf3f6d16e7e7d84b6c7883a00215834cb8cdad4775c380061ee79393]
- Building from source requires Node.js 18+, pnpm, stable Rust with Tauri system dependencies, and at least one supported coding-agent CLI on PATH. [@claim:clm_5166c510d594cfebe5ac17cd5ea67ddfbf4a3f819e189c51f5806b84a072ea55]
- Telemetry POSTs are tagged with a launch id so events route to the correct pane, and routing survives /clear, /compact and /resume, each of which makes Claude mint a new runtime session_id; the permission hook is a blocking call held open until answered. [@claim:clm_58d49cb0f4bbf07aa2f5bbceb66c3bb570d386c58df373e7437011bad4b2d702]
- When Claude or Codex requests to run something, the app surfaces the command with a risk read and lets the user allow, deny, or hand it to the terminal; starting permission/sandbox policy is stored per integrated agent. [@claim:clm_5fdb4a55b5f93b8e54ab4685d3897a0a1f243dcb65affd7316d34188af16d0ca]
- Personal preferences go to localStorage while project facts go to .episko/tasks.toml, described as the only file the app writes, edited via toml_edit so comments and ordering survive; shared digests and notes can be committed as .episko/digest.md and .episko/notes.toml. [@claim:clm_68b982be134a8e8f6e2c67f9ad093146411768073c38a57ca7321ec7be2855b5]
- Each project gets a dashboard with per-day commit and session summaries, issues with triage suggestions, GitHub claims that mark an issue as taken by an agent, and worktree checkouts; feature depth degrades for plain git repos and bare folders. [@claim:clm_a6b21826e31b91d28a20606c7db0ad041f1309935f98c49d0766efa6068f5a83]
- On each Claude launch the app writes a throwaway --settings file whose statusLine command and lifecycle hooks POST to a tiny_http server on an ephemeral localhost port; Codex launches use a loopback App Server, and both transports feed one provider-neutral event reducer. [@claim:clm_e49b74051b68b59b2510320f15ea466d3feb96182df10ee601e2eb6e1d9226fe]
- The app is built on Tauri v2 with a Rust backend and system WebView frontend, uses portable-pty for PTYs (forkpty on macOS, ConPTY on Windows), tiny_http as a localhost telemetry receiver, and xterm.js for terminal rendering. [@claim:clm_f723a986601aab63a03fdc1f1d0673b3deb16cf23fb23408fb86a3e98396b525]
<!-- rcw:end owner=source:src_074816f558215de0a5e8986c98cdcc40 block=evidence -->

## Researcher notes

