---
access: public
aliases: []
claim_ids:
- clm_143129fed5c74c2b08085027c7d259866a219fb5de706fc546ac687d61cb57e5
- clm_2a75a4d27cc4d14393c3120aac57a6589b182dd3a492d09bb3b03271f1a52ff2
- clm_34eded67735cdb475367893e9b5d1a3c68ff89c5a4f8849f7e5749a23ccb74f1
- clm_5723cc779483262d08a585035b807ad0de57d3d9783ee789b735cf4a7cc5e573
- clm_5a1107dda98ff15127b004cd1344fbbad907ac83e0de2cced33132769a78917c
- clm_746ef0fe0c9accc687c12d9e413503b3793e5ba8d1732072afdcad8f150a61a5
- clm_8265f2721d7e550113969bba288222b30882bdf6e1c101229720a3e9744bed4a
- clm_8ccf7a6c54579992915405c6872f10fe6159e863d602ff78a992e9fd81ad6d70
- clm_c19be55894d6b155d12bce17b5c562df6ddd5866e7c7fa9a8bf1bb147037ea66
- clm_e07fa3d4ceb04642151a02c248f057b4661abbcc030e20ac4b81dac0d9891b37
- clm_e4fe6e5ab1edc977fee4541dcee497d40d94170acd03d167f94bab1a4daec14d
- clm_e50e74f6baaf851763a416dd06162a72582f819ff925771c02d6363680b256ac
- clm_f63fcea83df9c64a7e2afc1fa98e24a7486380e044b5384b17ce2b4d8513fd81
maturity: draft
page_id: pg_92923ff93f335624b6050a437f437315
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b38396e590ec5341831a0c43366658e9
title: d-kimuson/claude-code-viewer/README.md @ 9367cf006be9
updated_at: '2026-09-14T01:44:25Z'
---

# d-kimuson/claude-code-viewer/README.md @ 9367cf006be9

<!-- rcw:begin owner=source:src_b38396e590ec5341831a0c43366658e9 block=evidence -->
- Windows is not supported as an operating system. [@claim:clm_143129fed5c74c2b08085027c7d259866a219fb5de706fc546ac687d61cb57e5]
- The CLI accepts options including --port (default 3000), --hostname, --verbose, --password, --executable, --claude-dir, --api-only, and --base-path. [@claim:clm_2a75a4d27cc4d14393c3120aac57a6589b182dd3a492d09bb3b03271f1a52ff2]
- Configuration can come from command-line options or environment variables such as CCV_PASSWORD and CCV_CC_EXECUTABLE_PATH, with CLI options taking precedence over environment variables. [@claim:clm_34eded67735cdb475367893e9b5d1a3c68ff89c5a4f8849f7e5749a23ccb74f1]
- The app reads Claude Code conversation logs from ~/.claude/projects/<project>/<session-id>.jsonl JSONL files and automatically discovers new projects and sessions. [@claim:clm_5723cc779483262d08a585035b807ad0de57d3d9783ee789b735cf4a7cc5e573]
- The product includes an integrated terminal emulator in a bottom panel, letting users launch Claude Code from the browser without leaving it. [@claim:clm_5a1107dda98ff15127b004cd1344fbbad907ac83e0de2cced33132769a78917c]
- Conversation data is preserved through strict Zod schema validation, with a progressive-disclosure UI that reveals details on demand. [@claim:clm_746ef0fe0c9accc687c12d9e413503b3793e5ba8d1732072afdcad8f150a61a5]
- Authentication is a simple single-password mechanism without multi-user support, role-based access control, or OAuth; more sophisticated access control is left to infrastructure like reverse proxies or VPNs. [@claim:clm_8265f2721d7e550113969bba288222b30882bdf6e1c101229720a3e9744bed4a]
- It is a PWA supporting Add to Home Screen on mobile with an optimized UI and push notifications when sessions complete. [@claim:clm_8ccf7a6c54579992915405c6872f10fe6159e863d602ff78a992e9fd81ad6d70]
- When a password is configured, /api routes require authentication via a ccv-session cookie from /api/auth/login or an Authorization: Bearer header; without a password, API auth is disabled. [@claim:clm_c19be55894d6b155d12bce17b5c562df6ddd5866e7c7fa9a8bf1bb147037ea66]
- Due to Anthropic ToS ambiguity for subscription accounts, chat sending, session resuming, permission approval, and AskUserQuestion are opt-in; read-oriented features work independently of the Agent SDK. [@claim:clm_e07fa3d4ceb04642151a02c248f057b4661abbcc030e20ac4b81dac0d9891b37]
- Requires Node.js 22.13.0 or later and Claude Code v1.0.125 or later; supported operating systems are macOS and Linux only. [@claim:clm_e4fe6e5ab1edc977fee4541dcee497d40d94170acd03d167f94bab1a4daec14d]
- In subscription mode the chat input becomes a copy mode that produces an equivalent claude CLI command, which can be pasted into the built-in terminal to start or resume a session. [@claim:clm_e50e74f6baaf851763a416dd06162a72582f819ff925771c02d6363680b256ac]
- The viewer makes no backups of session files, so when Claude Code's default 30-day cleanup deletes .jsonl transcripts those sessions disappear; users can raise cleanupPeriodDays in ~/.claude/settings.json. [@claim:clm_f63fcea83df9c64a7e2afc1fa98e24a7486380e044b5384b17ce2b4d8513fd81]
<!-- rcw:end owner=source:src_b38396e590ec5341831a0c43366658e9 block=evidence -->

## Researcher notes

