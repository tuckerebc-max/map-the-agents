# anomalyco/opencode -- full detail

[Back to orientation](opencode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/anomalyco/opencode/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/62fba2c78cec8b3e.json](../../../wiki/dossiers/anomalyco/opencode/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/62fba2c78cec8b3e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The README documents two built-in agents switchable with the Tab key: build (default, full access) and plan (read-only, denies file edits by default and asks before running bash commands), plus a general subagent invoked via @general. -- evidence: [README.md#L104-L108](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L104-L108), [README.md#L102-L102](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L102-L102), [README.md#L110-L111](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L110-L111) (`clm_8f729e7c537ee21ae268179046ee5dafdbcd30d81eea055a0f05f9e8f6a795e2`)
- [observation/code-inspected] The plan agent's permission config denies all edit tools except plan markdown files under .opencode/plans and the global plans data directory, and denies the general task subagent. -- evidence: [packages/opencode/src/agent/agent.ts#L140-L265](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L140-L265) (`clm_1b722a96998551c2e371ccd69cb681aff5ce7826205a90242f0e3ba809be73b9`)
- [observation/code-inspected] An agent 'generate' capability creates new agent configurations from a natural-language description via a model generateObject call with a JSON schema (identifier, whenToUse, systemPrompt), avoiding existing agent names. -- evidence: [packages/opencode/src/agent/agent.ts#L58-L62](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L58-L62), [packages/opencode/src/agent/agent.ts#L388-L416](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L388-L416), [packages/opencode/src/agent/agent.ts#L64-L80](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L64-L80) (`clm_1176f09332c5614cc004d9b9eeb3ebd6559e421adfe33d32b6505671c4bdc9e1`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to read CONTRIBUTING.md before submitting pull requests, and derivative projects using 'opencode' in their name must state they are unaffiliated with the OpenCode team. -- evidence: [README.md#L125-L125](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L125-L125), [README.md#L121-L121](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L121-L121) (`clm_fc1ca4942c79f5850132d0872162d751598a6781dfdd6f5ca83d9fa84d75c4bb`)

## skills-patterns (1 claim(s))

- [observation/code-inspected] Users can define custom agents in config; entries can disable built-ins or add new agents whose properties (model, prompt, permissions, mode, etc.) are merged over defaults. -- evidence: [packages/opencode/src/agent/agent.ts#L267-L294](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L267-L294) (`clm_f02872071bd0737ac15bb3d378e35a9ef8f52c8eda09471ede5acaf61b1d7ef8`)

## interfaces (4 claim(s))

- [observation/code-inspected] Agent configuration is a schema with name, description, mode (subagent/primary/all), permission ruleset, optional model, prompt, temperature, topP, steps, variant, color, and hidden fields. -- evidence: [packages/opencode/src/agent/agent.ts#L35-L56](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L35-L56) (`clm_bf240727f34ea7d66dad7a62252e6ffdd0813477d8cbf800033efacd24ee93ea`)
- [observation/documented] The install script resolves its target directory by priority: OPENCODE_INSTALL_DIR, XDG_BIN_DIR, $HOME/bin, then $HOME/.opencode/bin as fallback. -- evidence: [README.md#L89-L92](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L89-L92), [README.md#L87-L87](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L87-L87) (`clm_fb4a742c61058378a2a37f96f8b255894389ee4a827d408ef50887732cf8911a`)
- [observation/documented] A desktop application is offered in BETA for macOS (arm64/x64 dmg), Windows exe, and Linux deb/rpm/AppImage, also installable via Homebrew cask or Scoop extras. -- evidence: [README.md#L69-L69](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L69-L69), [README.md#L82-L83](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L82-L83), [README.md#L80-L80](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L80-L80), [README.md#L71-L76](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L71-L76) (`clm_e2c4a7e02780c99a606d0a060b9d957ee88177403dc648913f9761d6ebb17d7a`)
- [observation/documented] The client architecture derives Promise and Effect SDK clients from a public HttpApi; an Embedded OpenCode host reuses the same router and handlers over an in-memory HTTP transport. -- evidence: [CONTEXT.md#L73-L75](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L73-L75), [CONTEXT.md#L80-L82](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L80-L82) (`clm_645ac21eec51b4cff13e948c1f843e5af8a06e547f02ce06d3ac89ef6585cda7`)

## memory-state (2 claim(s))

- [observation/documented] CONTEXT.md defines a session runtime where sessions preserve durable conversation history and assemble a System Context from typed Context Sources, with changes admitted as Mid-Conversation System Messages at safe provider-turn boundaries. -- evidence: [CONTEXT.md#L22-L24](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L22-L24), [CONTEXT.md#L39-L40](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L39-L40), [CONTEXT.md#L3-L3](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L3-L3), [CONTEXT.md#L15-L17](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L15-L17) (`clm_d2adc8097b8bd0ef4ea7fbabdfb8bed7b1a3e2021af15b73cf1be3316352ab7c`)
- [observation/documented] Tool outputs exceeding history limits are projected into bounded Model Tool Output, with full oversized output retained in a managed temporary file under a shared tool-output directory. -- evidence: [CONTEXT.md#L54-L55](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L54-L55), [CONTEXT.md#L57-L58](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L57-L58) (`clm_9cd244ecc341f8f15c68a067fe2177e5916cb3901bdcc67957c0084961560d26`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/code-inspected] The agent module defines default permission rules: wildcard allow, ask for doom_loop and external directories, deny for question and plan transitions, and ask for reading .env files while allowing .env.example. -- evidence: [packages/opencode/src/agent/agent.ts#L119-L136](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L119-L136) (`clm_7f26c1b592ffbe2129326498d0d5cce2264b8fc21bcb9f65126676d220a41058`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/code-inspected] The agent implementation uses the Effect ecosystem (Effect, Context, Layer, Schema), the Vercel AI SDK (generateObject/streamObject), remeda, and OpenTelemetry tracing when experimental.openTelemetry is enabled. -- evidence: [packages/opencode/src/agent/agent.ts#L7-L10](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L7-L10), [packages/opencode/src/agent/agent.ts#L355-L378](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L355-L378), [packages/opencode/src/agent/agent.ts#L12-L33](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L12-L33) (`clm_52653c22300f4bf762d55655160607ebada35949b0ede69d870973b2ed46199c`)
- [observation/documented] OpenCode is installable via a curl script and many package managers including npm/bun/pnpm/yarn, Scoop, Chocolatey, Homebrew, pacman, AUR, mise, and nix. -- evidence: [README.md#L53-L62](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L53-L62), [README.md#L50-L50](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L50-L50) (`clm_12835b3581a8ee06b361d386a3427530e6fe681c6be566b795a534fede23bed5`)

## limitations (1 claim(s))

- [observation/documented] CONTEXT.md flags that the legacy experimental.chat.system.transform plugin hook can arbitrarily mutate the baseline system prompt, and V2 plugins do not yet expose an equivalent hook. -- evidence: [CONTEXT.md#L225-L225](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L225-L225) (`clm_76811de7c97bae5ef508e5093e34fb07476bb588abef97791352c5e1feacb3af`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_6c7268dd6bfcb348664b0ce013f3326b9e27cccf809f56386628c2edfa7ac63d, clm_78cb75480cd45010aff93a3de8eb72e5ac22eec06e46134cd5801b6ad765290d

