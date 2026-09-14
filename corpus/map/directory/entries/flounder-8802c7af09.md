# flounder (`flounder`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: adshao
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=Autonomous; install=npx skills add adshao/flounder --skill flounder -g -a codex -a claude-code; or from source: nvm use, npm install, npm run build, npm run sandbox:build (requires Node 24 LTS)
- Model providers: OpenAI (Codex), Anthropic (Claude Code)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [adshao/flounder](../../repos/adshao/flounder.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Autonomous white-hat security auditor that turns coding agents (Codex, Claude Code) into an end-to-end security audit pipeline (Prepare-\>Map-\>Dig-\>Synthesize-\>Verify-\>Confirm-\>Report). Audit strategy comes from the model, not hardcoded rules; findings require execution-grounded proof (must cite passing local commands). Sandboxed OCI execution with network-sealed discovery; strong fit for Solidity/EVM and ZK targets.

(captured site page body (agents/flounder.md), not a verified repo-code finding)
Flounder addresses the gap between chat-based vulnerability discussions and real audits: security work needs hours of sustained, skeptical investigation, containerized tooling, and evidence rather than plausible prose. It runs a seven-phase pipeline (prepare, map, dig, synthesize, verify, confirm, report) around the coding agent, supplying an OCI/Apple container sandbox with network sealing and read-only rootfs, a command policy, SQLite-backed durable state, and execution gates; the model chooses audit strategy while Flounder enforces the boundary. Findings require passing local proof tests with differential confirmation and refutation checks, so false positives get filtered before reporting. Security researchers use it for blind capability audits, incident investigation from transaction hashes, bug bounties, and disclosure preparation, with particular depth in Solidity/EVM, Cairo/Starknet, and TON.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/flounder.md)
