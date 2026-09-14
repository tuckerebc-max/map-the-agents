# aizenvoltprime/damocles -- full detail

[Back to orientation](damocles.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aizenvoltprime/damocles/b8787a5e9b69694cd607326dcce721bbf1e04bab/87e325b5b99a6e04.json](../../../wiki/dossiers/aizenvoltprime/damocles/b8787a5e9b69694cd607326dcce721bbf1e04bab/87e325b5b99a6e04.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture consists of a Node.js extension host running the pi engine, tools, and permissions; a Vue 3 + Tailwind webview chat interface; and a postMessage bridge between them. -- evidence: [README.md#L543-L545](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L543-L545) (`clm_af6a86650e68ad7010a659d641dd17d6cbb5f3439a8f5a7c587dedda7b2347f7`)

## design-choices (2 claim(s))

- [observation/documented] Asset precedence is builtin > .damocles > .claude/.codex, with project overriding user within a scope and damocles.assetSourcePrecedence (default claude) breaking ties between compat sources; matching is case-insensitive. -- evidence: [README.md#L189-L189](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L189-L189) (`clm_b87671e4d7b2e0c90c18f069f8789d34c4580f786628aa82a44708289831045a`)
- [observation/documented] Project-scope commands, skills, and instruction files are gated on VS Code workspace trust so an untrusted repository cannot inject prompts or hooks; user-scope assets remain unaffected. -- evidence: [README.md#L222-L222](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L222-L222), [README.md#L193-L193](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L193-L193) (`clm_a1bf26e521f7dd1353a5b3a9711685b790a7e9f20a9bc82ecb9a8f335d7d89f1`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: build from source by cloning, running npm install, npm run build, and pressing F5 for the Extension Development Host; npm test runs tests, npm run typecheck type-checks, and npm run build && npm run package produces a .vsix. -- evidence: [README.md#L525-L526](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L525-L526), [README.md#L108-L111](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L108-L111), [README.md#L522-L522](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L522-L522), [README.md#L516-L516](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L516-L516), [README.md#L532-L534](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L532-L534), [README.md#L513-L513](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L513-L513) (`clm_4321b36bbe7cb0275eb44a4c1a8c4b5d8a7bcc1e9c95dc3b7600f64507608153`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills load from .damocles/skills, .claude/skills and .codex/skills SKILL.md files (project and user scopes), with YAML frontmatter descriptions and a name: field that can override the directory name. -- evidence: [README.md#L216-L216](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L216-L216) (`clm_d72fa16d6d14df0c67aa8ccf6b76bd7ae138ca2c0207b899d033c067d7fa1325`)
- [observation/documented] Skill invocation via slash command is auto-approved without a prompt, while agent-initiated skill use triggers an approval prompt with options to approve once, auto-approve for the session, deny, or redirect with new instructions. -- evidence: [README.md#L201-L203](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L201-L203), [README.md#L207-L207](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L207-L207), [README.md#L209-L212](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L209-L212) (`clm_076a6a9b26bf5da9dda7e8dbc2c65fff9f3d29c07c8a154b250c7f897c3af127`)

## interfaces (3 claim(s))

- [observation/documented] The product is a VS Code extension offering a chat panel in the secondary sidebar or as an editor panel (Ctrl+Shift+U), with both modes supporting independent simultaneous sessions. -- evidence: [README.md#L26-L44](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L26-L44) (`clm_e8ec34835e63605e541b88e2b42ab6fbbbacbe8864407c65bbae63725b04ec64`)
- [observation/documented] Slash commands include built-ins like /clear, /compact, /rewind, /remember, /note, /memories, /context and /usage, plus custom commands loaded from .damocles/commands, .claude/commands and .codex/prompts. -- evidence: [README.md#L175-L185](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L175-L185), [README.md#L187-L187](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L187-L187) (`clm_521af124767126478ffb358729d67396f947405e47d006902d46adf5307673d0`)
- [observation/documented] Keyboard shortcuts include Ctrl+K for a prompt navigator, Shift+Tab to cycle permission modes, Escape to cancel a request, and double-Escape to open a rewind popup. -- evidence: [README.md#L122-L127](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L122-L127) (`clm_af80da6bb2397e1139b09ed13a77dc3be51ae77566bc03abac4ba6e7d8bbef9b`)

## memory-state (3 claim(s))

- [observation/documented] Persistent memory is stored locally in SQLite via Node's built-in node:sqlite at ~/.damocles/memory.v3.db, with no native modules or WASM, and memories carry kinds (fact, preference, episode, observation, note) and scopes (session, project, global). -- evidence: [README.md#L307-L307](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L307-L307), [README.md#L321-L325](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L321-L325), [README.md#L313-L319](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L313-L319) (`clm_47fef80094391c2437170ee9591bb62dcae59777d1aece1a0f6b83c1316b86d8`)
- [observation/documented] Each prompt receives a relevance-ranked memory catalog scored from BM25 prompt relevance (50%), recency (15%), scope priority (15%), file proximity (10%), and retrieval boost (10%), with pinned memories injected in full. -- evidence: [README.md#L327-L327](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L327-L327), [README.md#L333-L342](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L333-L342) (`clm_1ee01afe056cd4f6d49fb8a48f9f2d3bc2c052df2ff865a57506a55b87a4fc84`)
- [observation/documented] The agent has ten autonomous memory tools, including save_memory, save_observation, search_memories, get_memory_details, get_memory_history, get_related_memories, forget_memory, save_note/list_notes, and reset_observation_staleness. -- evidence: [README.md#L377-L377](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L377-L377), [README.md#L379-L387](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L379-L387) (`clm_54a8928c5972ed34934134324b4298e09dbfaec30ec8ccfb9c6b7a13cc8cc3f5`)

## orchestration (2 claim(s))

- [observation/documented] Hooks let users run their own commands at session events via hooks.json; the child process receives one JSON object on stdin and replies with one on stdout, and a tool_call hook can block, force-allow, or rewrite a tool call. -- evidence: [README.md#L279-L279](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L279-L279), [README.md#L286-L286](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L286-L286), [docs/hooks.md#L6-L7](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/docs/hooks.md#L6-L7) (`clm_c66a49b9f4185d8862fb7d4b737c35563621dfbcf120ee9f387837ccb801fdb4`)
- [observation/documented] Hook safety is bounded by workspace trust: the global ~/.damocles/hooks.json is always honored while the project-level file is honored only in a trusted workspace, and both files hot-reload on change with global running before project. -- evidence: [README.md#L281-L284](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L281-L284), [docs/hooks.md#L25-L26](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/docs/hooks.md#L25-L26), [docs/hooks.md#L20-L23](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/docs/hooks.md#L20-L23), [docs/hooks.md#L17-L18](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/docs/hooks.md#L17-L18) (`clm_6d8f5f2a1c2e1548468efaadf8a5075be93afe19f1149fcf7ffebabcda387a0c`)

## tools-permissions (2 claim(s))

- [observation/documented] Persistent allow/deny/ask permission rules are evaluated before each tool call, read from an eight-tier priority chain of .damocles and .claude settings files where the first match wins; Damocles writes only to .damocles/. -- evidence: [README.md#L230-L239](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L230-L239), [README.md#L241-L245](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L241-L245), [README.md#L226-L226](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L226-L226) (`clm_bc47b01d4d285a04ca62fe9a1223077d1ee2119bbdc25adda6f5dd2ce45ebc34`)
- [observation/documented] Bash and PowerShell permission rules are evaluated independently, so a Bash rule never auto-allows an equivalent PowerShell command; pattern syntax covers shell prefixes plus Edit(*.ts) and Write(src/**) style file patterns. -- evidence: [README.md#L263-L271](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L263-L271), [README.md#L259-L259](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L259-L259) (`clm_b22f0df364552cc5d98281b7335d751806dcf3e364d46417aa805d8e8b40ceea`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Damocles runs on the pi agent engine and talks to Anthropic and OpenAI directly, keeping its own credentials under ~/.damocles/ isolated from the Claude Code CLI, whose settings and skills it reads but whose credentials it never touches. -- evidence: [README.md#L479-L479](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L479-L479) (`clm_a071ff44888d7b7771dc1187540e4751fb5a9d451b6a19c278f80dccf9960cda`)
- [observation/documented] Requirements include VS Code 1.95.0+, a Claude or ChatGPT/Codex subscription or respective API keys, plus StepFun and DeepSeek provider keys; supported platforms are Windows, macOS, and Linux. -- evidence: [README.md#L471-L475](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L471-L475) (`clm_942c896eb8862499e4aad38d8e9a7b8749fc3ca92fa94d1ebe27ba0b38d37f76`)

## limitations (2 claim(s))

- [observation/documented] Voice features require local audio hardware and are unavailable over SSH, since the extension host runs server-side where no microphone exists. -- evidence: [README.md#L46-L104](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L46-L104) (`clm_e4ee91bbed4ab23cfac208878aa40c8cb9111274d761c5e26f0dae06987c2e26`)
- [observation/documented] The README warns that the Claude 'allowance' authentication mode, which routes OAuth through a third-party plugin impersonating the official Claude Code CLI to draw on included subscription quota, very likely violates Anthropic's Terms of Service. -- evidence: [README.md#L491-L491](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L491-L491), [README.md#L487-L489](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L487-L489) (`clm_0f7c27ceaa1217161883da3f892d00d77c6e866af7962d31ebab250d484909cc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

