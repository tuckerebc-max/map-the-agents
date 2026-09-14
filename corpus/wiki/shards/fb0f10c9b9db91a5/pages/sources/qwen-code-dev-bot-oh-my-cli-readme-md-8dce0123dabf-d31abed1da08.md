---
access: public
aliases: []
claim_ids:
- clm_092106189ce2baae2f059c1d1d8c7a7f2ead208cc4ff0564bd4828525dd52ab7
- clm_0f0a4d28d856fd5f60a1cbf94b9f37c35aa418d7309544e6b14e1abb6f7a9f2c
- clm_10cbbcb9bcd171f47eccb713cb1e6d14f4a48bbc6c372e46e5f9ad04f6813438
- clm_1650f165fb9b0cfeed6dce694fccc83d6405b3c18e62fb04fd4f99c09664441a
- clm_1ad7d991a2c594d6c88b93602ec36c27c33fd6e9870780bd83189f8a1a1ba4d8
- clm_3139133b998a08d66cb7a73dd18541ca5d94999b7dd8b7ebf83937e888cd6319
- clm_34a3cebc5dfe9ac5c68ca8b4381dfc5e091aba20b4b4668e2b401fb3b1f12aff
- clm_35bd6a4b4f60cca6240187e0adb17f53db053376f5dafd6c239d87900806c56a
- clm_4696e232862a3ec2e1c35f3bd6403883afe60ae3aff6bbba54888ad71ad8722e
- clm_4ba1e3cf6dbd27990927fa465a83787fa952c28862ba80aabdca071a78446048
- clm_618bcd1772bc99379ea6217b080ee79415ed9d7a369bc2dd67c9720c1d4867c7
- clm_66517b652e54c27eea6295c96ccf87f50a372adfe4f36248de6006e56f1574d9
- clm_7c3c9b8f0f7f190911a5d54e28196bb82bf3b6a77681d8df574b077c6a0532dc
- clm_8dc6e19137cd8c607b258edf77dd7cbfc6973695bf82e1277368dddb4b8d9dfb
- clm_a44269fa06978844121d5cd4af43abf3b00df667ad3efcf951e187d49654b506
- clm_abee26576b49a4b2e3c0b250c106359835e7cda9a9a04ae4f57a0eea4aaab717
- clm_acb39ede77441a53dbf584003f465dc20f2ae13dc19235d97d811d2e569500a5
- clm_ae480fb18081c8b6e3e1af5c1f743db1d99be70ac5b73fd92b290a1f7503ddc8
- clm_df8d09fa449e52ec1c323fb4989c5c0a9c2f45a29ad6ce3580be5b998409724b
maturity: draft
page_id: pg_633343bdce685292ae50d31abed1da08
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_850d525e7a915e2ab622ed96e9291910
title: qwen-code-dev-bot/oh-my-cli/README.md @ 8dce0123dabf
updated_at: '2026-09-14T02:34:12Z'
---

# qwen-code-dev-bot/oh-my-cli/README.md @ 8dce0123dabf

<!-- rcw:begin owner=source:src_850d525e7a915e2ab622ed96e9291910 block=evidence -->
- Compaction writes a versioned summary sidecar validated against the transcript digest before use, keeping completed tool actions as redacted receipts the resumed model is told not to repeat. [@claim:clm_092106189ce2baae2f059c1d1d8c7a7f2ead208cc4ff0564bd4828525dd52ab7]
- Folder trust is a fail-closed top-level boundary: workspaces are untrusted by default, trust is recorded in a user-owned store a project cannot write, and approval modes are subordinate to it. [@claim:clm_0f0a4d28d856fd5f60a1cbf94b9f37c35aa418d7309544e6b14e1abb6f7a9f2c]
- Three approval modes exist: default prompts for every mutating tool and denies without a TTY, auto-edit allows write/edit but still prompts for shell, and yolo allows all tools without prompting; read operations never require approval. [@claim:clm_10cbbcb9bcd171f47eccb713cb1e6d14f4a48bbc6c372e46e5f9ad04f6813438]
- Repository development practice: contributors install with npm install, npm run build, and npm link (or invoke node dist/index.js), and are pointed to a first-run guide with a --doctor setup check. [@claim:clm_1650f165fb9b0cfeed6dce694fccc83d6405b3c18e62fb04fd4f99c09664441a]
- Trust enforcement is opt-in via --enforce-folder-trust or OMC_ENFORCE_FOLDER_TRUST=1; trust states include trusted, sandbox-enforced, untrusted, and sandbox-unavailable, with mutation denied in the latter two. [@claim:clm_1ad7d991a2c594d6c88b93602ec36c27c33fd6e9870780bd83189f8a1a1ba4d8]
- Model configuration resolves from environment variables, an optional trusted workspace .env, and a user settings file, with environment variables taking highest precedence; raw credential fields like model.apiKey are rejected in favor of apiKeyEnv references. [@claim:clm_3139133b998a08d66cb7a73dd18541ca5d94999b7dd8b7ebf83937e888cd6319]
- Undo/redo of a completed turn uses content-based checkpoints of only the files the turn's mutating tools touched, restoring pre-images without git reset, and fails closed (exit 2) if files diverged. [@claim:clm_34a3cebc5dfe9ac5c68ca8b4381dfc5e091aba20b4b4668e2b401fb3b1f12aff]
- Session-targeted flags (--resume, --session-stats, --tasks, --export-session, --compact, --undo-turn, --redo-turn, --session) accept an exact id or user-owned name and fail closed on ambiguous, corrupt, or unknown values. [@claim:clm_35bd6a4b4f60cca6240187e0adb17f53db053376f5dafd6c239d87900806c56a]
- Named model profiles can be declared in the user settings file and selected via --profile, --list-profiles, or a defaultProfile, with project-local settings files unable to set profiles. [@claim:clm_4696e232862a3ec2e1c35f3bd6403883afe60ae3aff6bbba54888ad71ad8722e]
- The project is built with Node.js 22, TypeScript, and ESM, and is installed via npm install/build/link or by running the built dist/index.js directly. [@claim:clm_4ba1e3cf6dbd27990927fa465a83787fa952c28862ba80aabdca071a78446048]
- A --delivery-web command serves a loopback-only web delivery board (default port 4317, configurable via --web-port) with /remote-control and /dynamic-workflow pages that expose no credentials or file server. [@claim:clm_618bcd1772bc99379ea6217b080ee79415ed9d7a369bc2dd67c9720c1d4867c7]
- Workspace .env loading is gated by folder trust, parsed only for model-config resolution without mutating process.env, and .env.local/.env.production variants and nested .env files are not read. [@claim:clm_66517b652e54c27eea6295c96ccf87f50a372adfe4f36248de6006e56f1574d9]
- Sessions persist as JSONL under ~/.oh-my-cli/sessions/ with atomic checkpointing; on resume, complete checkpoints are promoted, partial ones discarded, and corrupt ones quarantined rather than deleted. [@claim:clm_7c3c9b8f0f7f190911a5d54e28196bb82bf3b6a77681d8df574b077c6a0532dc]
- Approval previews and command-policy denials neutralize spoofing Unicode (bidi controls, zero-width characters, look-alike quotes) by replacing each with a visible [U+XXXX] marker to prevent Trojan Source-style disguise. [@claim:clm_8dc6e19137cd8c607b258edf77dd7cbfc6973695bf82e1277368dddb4b8d9dfb]
- Side questions answer clarifications against a bounded read-only session snapshot with tool execution and workspace mutation structurally disabled, leaving the source session byte-identical. [@claim:clm_a44269fa06978844121d5cd4af43abf3b00df667ad3efcf951e187d49654b506]
- With --output json and -p, the CLI emits a versioned newline-delimited JSON event stream (protocol oh-my-cli.headless) with start, assistant, tool_start, tool_result, usage, retry, error, and complete records. [@claim:clm_abee26576b49a4b2e3c0b250c106359835e7cda9a9a04ae4f57a0eea4aaab717]
- oh-my-cli is a small self-hosted code agent CLI that reads and edits files and runs shell commands under a safety plane, against any OpenAI-compatible endpoint. [@claim:clm_acb39ede77441a53dbf584003f465dc20f2ae13dc19235d97d811d2e569500a5]
- The project targets terminal-based code-agent workflows with headless CI automation, spend budgets, and an Electron desktop shell, and is Apache-2.0 licensed with contribution and security policies. [@claim:clm_ae480fb18081c8b6e3e1af5c1f743db1d99be70ac5b73fd92b290a1f7503ddc8]
- The CLI offers run summaries and scorecards: --summary emits metadata-only outcome/exit/reason/token/cost data, and --baseline/--candidate compare two summary files captured via --summary-out. [@claim:clm_df8d09fa449e52ec1c323fb4989c5c0a9c2f45a29ad6ce3580be5b998409724b]
<!-- rcw:end owner=source:src_850d525e7a915e2ab622ed96e9291910 block=evidence -->

## Researcher notes

