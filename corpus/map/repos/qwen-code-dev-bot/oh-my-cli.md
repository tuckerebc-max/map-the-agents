# qwen-code-dev-bot/oh-my-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8dce0123dabf @ f1d6b1bdd8870a00

## Summary (orientation draft, not independently verified)

Selected evidence records: oh-my-cli is a small self-hosted code agent CLI that reads and edits files and runs shell commands under a safety plane, against any OpenAI-compatible endpoint. The project is built with Node.js 22, TypeScript, and ESM, and is installed via npm install/build/link or by running the built dist/index.js directly.

## Source coverage

Source coverage (partial): 4 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] oh-my-cli is a small self-hosted code agent CLI that reads and edits files and runs shell commands under a safety plane, against any OpenAI-compatible endpoint. -- evidence: [README.md#L7-L9](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L7-L9)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Approval previews and command-policy denials neutralize spoofing Unicode (bidi controls, zero-width characters, look-alike quotes) by replacing each with a visible [U+XXXX] marker to prevent Trojan Source-style disguise. -- evidence: [README.md#L637-L648](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L637-L648)
  - [observation/documented] Workspace .env loading is gated by folder trust, parsed only for model-config resolution without mutating process.env, and .env.local/.env.production variants and nested .env files are not read. -- evidence: [README.md#L139-L147](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L139-L147)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors install with npm install, npm run build, and npm link (or invoke node dist/index.js), and are pointed to a first-run guide with a --doctor setup check. -- evidence: [README.md#L66-L68](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L66-L68), [README.md#L70-L72](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L70-L72), [README.md#L60-L64](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L60-L64)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] With --output json and -p, the CLI emits a versioned newline-delimited JSON event stream (protocol oh-my-cli.headless) with start, assistant, tool_start, tool_result, usage, retry, error, and complete records. -- evidence: [README.md#L740-L744](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L740-L744), [README.md#L730-L732](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L730-L732), [README.md#L746-L758](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L746-L758)
  - [observation/documented] Model configuration resolves from environment variables, an optional trusted workspace .env, and a user settings file, with environment variables taking highest precedence; raw credential fields like model.apiKey are rejected in favor of apiKeyEnv references. -- evidence: [README.md#L119-L126](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L119-L126), [README.md#L113-L117](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L113-L117), [README.md#L76-L78](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L76-L78)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions persist as JSONL under ~/.oh-my-cli/sessions/ with atomic checkpointing; on resume, complete checkpoints are promoted, partial ones discarded, and corrupt ones quarantined rather than deleted. -- evidence: [README.md#L283-L290](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L283-L290)
  - [observation/documented] Compaction writes a versioned summary sidecar validated against the transcript digest before use, keeping completed tool actions as redacted receipts the resumed model is told not to repeat. -- evidence: [README.md#L303-L312](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L303-L312)
- orchestration (2 claim(s)):
  - [observation/documented] Undo/redo of a completed turn uses content-based checkpoints of only the files the turn's mutating tools touched, restoring pre-images without git reset, and fails closed (exit 2) if files diverged. -- evidence: [README.md#L385-L393](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L385-L393), [README.md#L363-L371](https://github.com/qwen-code-dev-bot/oh-my-cli/blob/8dce0123dabfdae34093088281aaeb890e62d4fd/README.md#L363-L371)
More evidence: [full detail](oh-my-cli.detail.md)

Metadata and full claim list: [full detail](oh-my-cli.detail.md)
Human notes ([notes](oh-my-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
