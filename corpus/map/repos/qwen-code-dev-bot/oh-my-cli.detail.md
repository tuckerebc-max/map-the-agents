# qwen-code-dev-bot/oh-my-cli -- full detail

[Back to orientation](oh-my-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/qwen-code-dev-bot/oh-my-cli/8dce0123dabfdae34093088281aaeb890e62d4fd/f1d6b1bdd8870a00.json](../../../wiki/dossiers/qwen-code-dev-bot/oh-my-cli/8dce0123dabfdae34093088281aaeb890e62d4fd/f1d6b1bdd8870a00.json)

## specifications (1 claim(s))

- [observation/documented] oh-my-cli is a small self-hosted code agent CLI that reads and edits files and runs shell commands under a safety plane, against any OpenAI-compatible endpoint. -- evidence: [README.md#L7-L9](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L7-L9) (`clm_acb39ede77441a53dbf584003f465dc20f2ae13dc19235d97d811d2e569500a5`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Approval previews and command-policy denials neutralize spoofing Unicode (bidi controls, zero-width characters, look-alike quotes) by replacing each with a visible [U+XXXX] marker to prevent Trojan Source-style disguise. -- evidence: [README.md#L637-L648](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L637-L648) (`clm_8dc6e19137cd8c607b258edf77dd7cbfc6973695bf82e1277368dddb4b8d9dfb`)
- [observation/documented] Workspace .env loading is gated by folder trust, parsed only for model-config resolution without mutating process.env, and .env.local/.env.production variants and nested .env files are not read. -- evidence: [README.md#L139-L147](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L139-L147) (`clm_66517b652e54c27eea6295c96ccf87f50a372adfe4f36248de6006e56f1574d9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors install with npm install, npm run build, and npm link (or invoke node dist/index.js), and are pointed to a first-run guide with a --doctor setup check. -- evidence: [README.md#L66-L68](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L66-L68), [README.md#L70-L72](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L70-L72), [README.md#L60-L64](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L60-L64) (`clm_1650f165fb9b0cfeed6dce694fccc83d6405b3c18e62fb04fd4f99c09664441a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] With --output json and -p, the CLI emits a versioned newline-delimited JSON event stream (protocol oh-my-cli.headless) with start, assistant, tool_start, tool_result, usage, retry, error, and complete records. -- evidence: [README.md#L740-L744](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L740-L744), [README.md#L730-L732](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L730-L732), [README.md#L746-L758](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L746-L758) (`clm_abee26576b49a4b2e3c0b250c106359835e7cda9a9a04ae4f57a0eea4aaab717`)
- [observation/documented] Model configuration resolves from environment variables, an optional trusted workspace .env, and a user settings file, with environment variables taking highest precedence; raw credential fields like model.apiKey are rejected in favor of apiKeyEnv references. -- evidence: [README.md#L119-L126](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L119-L126), [README.md#L113-L117](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L113-L117), [README.md#L76-L78](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L76-L78) (`clm_3139133b998a08d66cb7a73dd18541ca5d94999b7dd8b7ebf83937e888cd6319`)
- [observation/documented] Named model profiles can be declared in the user settings file and selected via --profile, --list-profiles, or a defaultProfile, with project-local settings files unable to set profiles. -- evidence: [README.md#L151-L155](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L151-L155), [README.md#L172-L175](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L172-L175), [README.md#L184-L188](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L184-L188) (`clm_4696e232862a3ec2e1c35f3bd6403883afe60ae3aff6bbba54888ad71ad8722e`)
- [observation/documented] Session-targeted flags (--resume, --session-stats, --tasks, --export-session, --compact, --undo-turn, --redo-turn, --session) accept an exact id or user-owned name and fail closed on ambiguous, corrupt, or unknown values. -- evidence: [README.md#L248-L253](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L248-L253), [README.md#L255-L260](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L255-L260) (`clm_35bd6a4b4f60cca6240187e0adb17f53db053376f5dafd6c239d87900806c56a`)
- [observation/documented] A --delivery-web command serves a loopback-only web delivery board (default port 4317, configurable via --web-port) with /remote-control and /dynamic-workflow pages that expose no credentials or file server. -- evidence: [README.md#L222-L223](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L222-L223), [README.md#L227-L231](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L227-L231) (`clm_618bcd1772bc99379ea6217b080ee79415ed9d7a369bc2dd67c9720c1d4867c7`)

## memory-state (2 claim(s))

- [observation/documented] Sessions persist as JSONL under ~/.oh-my-cli/sessions/ with atomic checkpointing; on resume, complete checkpoints are promoted, partial ones discarded, and corrupt ones quarantined rather than deleted. -- evidence: [README.md#L283-L290](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L283-L290) (`clm_7c3c9b8f0f7f190911a5d54e28196bb82bf3b6a77681d8df574b077c6a0532dc`)
- [observation/documented] Compaction writes a versioned summary sidecar validated against the transcript digest before use, keeping completed tool actions as redacted receipts the resumed model is told not to repeat. -- evidence: [README.md#L303-L312](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L303-L312) (`clm_092106189ce2baae2f059c1d1d8c7a7f2ead208cc4ff0564bd4828525dd52ab7`)

## orchestration (2 claim(s))

- [observation/documented] Undo/redo of a completed turn uses content-based checkpoints of only the files the turn's mutating tools touched, restoring pre-images without git reset, and fails closed (exit 2) if files diverged. -- evidence: [README.md#L385-L393](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L385-L393), [README.md#L363-L371](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L363-L371) (`clm_34a3cebc5dfe9ac5c68ca8b4381dfc5e091aba20b4b4668e2b401fb3b1f12aff`)
- [observation/documented] Side questions answer clarifications against a bounded read-only session snapshot with tool execution and workspace mutation structurally disabled, leaving the source session byte-identical. -- evidence: [README.md#L397-L402](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L397-L402), [README.md#L420-L425](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L420-L425) (`clm_a44269fa06978844121d5cd4af43abf3b00df667ad3efcf951e187d49654b506`)

## tools-permissions (3 claim(s))

- [observation/documented] Three approval modes exist: default prompts for every mutating tool and denies without a TTY, auto-edit allows write/edit but still prompts for shell, and yolo allows all tools without prompting; read operations never require approval. -- evidence: [README.md#L633-L633](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L633-L633), [README.md#L629-L631](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L629-L631) (`clm_10cbbcb9bcd171f47eccb713cb1e6d14f4a48bbc6c372e46e5f9ad04f6813438`)
- [observation/documented] Folder trust is a fail-closed top-level boundary: workspaces are untrusted by default, trust is recorded in a user-owned store a project cannot write, and approval modes are subordinate to it. -- evidence: [README.md#L658-L664](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L658-L664), [README.md#L652-L656](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L652-L656) (`clm_0f0a4d28d856fd5f60a1cbf94b9f37c35aa418d7309544e6b14e1abb6f7a9f2c`)
- [observation/documented] Trust enforcement is opt-in via --enforce-folder-trust or OMC_ENFORCE_FOLDER_TRUST=1; trust states include trusted, sandbox-enforced, untrusted, and sandbox-unavailable, with mutation denied in the latter two. -- evidence: [README.md#L675-L677](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L675-L677), [README.md#L668-L673](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L668-L673) (`clm_1ad7d991a2c594d6c88b93602ec36c27c33fd6e9870780bd83189f8a1a1ba4d8`)

## evaluation (1 claim(s))

- [observation/documented] The CLI offers run summaries and scorecards: --summary emits metadata-only outcome/exit/reason/token/cost data, and --baseline/--candidate compare two summary files captured via --summary-out. -- evidence: [README.md#L813-L821](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L813-L821), [README.md#L774-L780](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L774-L780), [README.md#L823-L827](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L823-L827) (`clm_df8d09fa449e52ec1c323fb4989c5c0a9c2f45a29ad6ce3580be5b998409724b`)

## dependencies (1 claim(s))

- [observation/documented] The project is built with Node.js 22, TypeScript, and ESM, and is installed via npm install/build/link or by running the built dist/index.js directly. -- evidence: [README.md#L3-L3](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L3-L3), [README.md#L66-L68](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L66-L68), [README.md#L60-L64](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L60-L64) (`clm_4ba1e3cf6dbd27990927fa465a83787fa952c28862ba80aabdca071a78446048`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets terminal-based code-agent workflows with headless CI automation, spend budgets, and an Electron desktop shell, and is Apache-2.0 licensed with contribution and security policies. -- evidence: [README.md#L13-L33](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L13-L33), [README.md#L40-L43](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L40-L43) (`clm_ae480fb18081c8b6e3e1af5c1f743db1d99be70ac5b73fd92b290a1f7503ddc8`)

