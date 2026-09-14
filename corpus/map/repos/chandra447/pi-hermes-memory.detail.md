# chandra447/pi-hermes-memory -- full detail

[Back to orientation](pi-hermes-memory.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/chandra447/pi-hermes-memory/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/c661b291c1be6aa1.json](../../../wiki/dossiers/chandra447/pi-hermes-memory/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/c661b291c1be6aa1.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The extension manages three knowledge types: MEMORY.md facts (5,000-char cap), USER.md profile (5,000-char cap), and Pi-native SKILL.md procedures with unlimited size. -- evidence: [README.md#L81-L85](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L81-L85) (`clm_549b4cc1458defe07304f3f91f87f8a9fa2be589e1464d010f413fa1495f0aa5`)

## design-choices (2 claim(s))

- [observation/documented] Standing instructions (/memory-pin) are a user-authored file injected into every session in every memory mode, capped at 20 entries / 2,000 characters, stored in STANDING.md which background processes cannot write; the feature is explicitly not tool enforcement. -- evidence: [README.md#L196-L196](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L196-L196), [README.md#L207-L212](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L207-L212), [README.md#L216-L216](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L216-L216) (`clm_11d11a9e7a75fb82606133515004e925b83d48417c6f2e400d51fb980408e806`)
- [observation/documented] Memory blocks are wrapped in <memory-context> XML tags with a guard note stating they are not new user input, to prevent the model from treating stored facts as instructions. -- evidence: [README.md#L252-L252](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L252-L252) (`clm_97623f29447ae2caf1d26dfed8c6ad193480464a0fe682bc2d4815325d48ef54`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] For create and update, skill_manage prefers structured fields (when_to_use, procedure_steps, pitfalls, verification_steps) rendered into SKILL.md sections, and global creation has duplicate/similarity guards blocking exact slug matches and near-name collisions. -- evidence: [README.md#L305-L307](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L305-L307), [README.md#L294-L294](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L294-L294), [README.md#L301-L301](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L301-L301), [README.md#L296-L299](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L296-L299) (`clm_174d6ccc66bb2780849db40869c7a507e5576cd8de47c0b52f2b4e43cf640d3a`)
- [observation/documented] Project-scoped skills are exposed to Pi via the resources_discover hook, which returns the active project's skills directory so Pi discovers them natively without copying into the global folder. -- evidence: [README.md#L343-L343](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L343-L343), [README.md#L337-L337](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L337-L337), [README.md#L339-L339](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L339-L339) (`clm_66ed01198b939cf0e662e3121f2f3041bd65a0d953c2f47f0f71bc8d4e4835a5`)

## interfaces (4 claim(s))

- [observation/documented] The agent gets memory write tools memory_add, memory_replace, and memory_remove with targets memory, user, project, and failure, plus a skill_manage tool with create, view, patch, update, and delete actions. -- evidence: [README.md#L274-L280](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L274-L280), [README.md#L268-L268](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L268-L268), [README.md#L262-L266](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L262-L266) (`clm_840b3c4c74a5ae2f348ac648de9d507d6b14ff232c355c08ccad8e9b6823f0fa`)
- [observation/documented] Search tools include session_search over past conversations and memory_search over the extended store; FTS5 with a trigram tokenizer supports multi-word, quoted-phrase, OR-operator, and CJK substring queries of three or more characters. -- evidence: [README.md#L364-L368](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L364-L368), [README.md#L359-L362](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L359-L362), [README.md#L357-L357](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L357-L357) (`clm_db4b31709c9d5819e3c3635381caf139c887469b57fba85194e2aca9e57210e7`)
- [observation/documented] Slash commands include /memory-insights, /memory-skills, /memory-consolidate, /memory-interview, /memory-index-sessions, /memory-sync-markdown, /memory-preview-context, /memory-pin, and /learn-memory-tool. -- evidence: [README.md#L449-L459](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L449-L459), [README.md#L198-L203](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L198-L203) (`clm_8a0d9d2138ba89ac9efa0eb7b9b1122d1d0f01a5c2e3f9ca9486a5bbbd7ab184`)
- [observation/documented] An opt-in sessionSearch.variant of 'anchors' makes session_search read session JSONL files directly and return path:startLine-endLine anchors with short reasons instead of summaries. -- evidence: [README.md#L376-L376](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L376-L376) (`clm_7a9b488cd6ef4296820e19d84378c46a25e9de0be7474e2b5399c67e39398847`)

## memory-state (4 claim(s))

- [observation/documented] Memory is stored at two tiers: global facts under ~/.pi/agent/pi-hermes-memory/ and per-project facts under ~/.pi/agent/projects-memory/<project>/, with project memories searchable when the cwd matches. -- evidence: [README.md#L172-L175](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L172-L175) (`clm_71c1269ca8202fddf04f70b3b22db72280b795be23766a866cf9bbe9b6d514dc`)
- [observation/documented] By default full Markdown memories are not injected into the system prompt; instead a <memory-policy> block tells the agent when to call memory_search, keeping first-turn token usage low. -- evidence: [README.md#L177-L177](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L177-L177) (`clm_e6d54ad2abe524e1dd97076f7acc92ba99b5c23b081c67117ab2d66b9828e645`)
- [observation/documented] A hybrid architecture keeps Markdown as the human-readable source of truth while mirroring successful writes into a SQLite store (sessions.db) queried via memory_search; failed core writes are not silently spilled into SQLite-only storage. -- evidence: [README.md#L387-L389](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L387-L389), [README.md#L391-L391](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L391-L391), [README.md#L382-L385](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L382-L385), [README.md#L380-L380](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L380-L380) (`clm_deeb1d9cfe252fe7a36fe1ed59c9c8e77687df74ff488f6d1486bdee6e0b3dfd`)
- [observation/documented] An optional lazyInitialization mode defers Markdown/SQLite sync, memory loading, maintenance, and session indexing until the first memory operation, while pinned STANDING.md instructions and skill discovery remain available at startup; legacy-inject ignores the option. -- evidence: [README.md#L606-L610](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L606-L610), [README.md#L638-L638](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L638-L638), [README.md#L614-L636](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L614-L636), [README.md#L553-L593](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L553-L593) (`clm_720499bf6eb3082cf3586fdb2a464558987791b361f1c13cc447401faf30a128`)

## orchestration (3 claim(s))

- [observation/documented] Background review triggers every 10 turns or every 15 tool calls, with both counters reset after each review; correction detection saves immediately when the user corrects the agent. -- evidence: [README.md#L395-L395](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L395-L395), [README.md#L419-L419](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L419-L419), [README.md#L421-L422](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L421-L422), [README.md#L424-L424](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L424-L424) (`clm_5bf8d5fecb60836b6e1d053e2ec3841f211f82ef69f3d17d804384d046475a70`)
- [observation/documented] By default review, flush, correction save, and manual consolidation use an in-process completeSimple() side-channel, falling back to a pi -p --no-session subprocess on failure; reviewTransport can force subprocess-only behavior. -- evidence: [README.md#L430-L430](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L430-L430), [README.md#L434-L437](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L434-L437), [README.md#L428-L428](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L428-L428) (`clm_5a94283b8169a656389fee0af3cd4a261aa7698c18e07c334ad0707c65578e74`)
- [observation/documented] In legacy-inject mode, when memory hits its character limit the extension spawns a one-shot consolidation child process that merges entries, then reloads and retries the save; in policy-only mode SQLite is the query authority and consolidation is manual via /memory-consolidate. -- evidence: [README.md#L415-L415](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L415-L415), [README.md#L410-L413](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L410-L413), [README.md#L408-L408](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L408-L408) (`clm_0ed3a5f6dada7c30fad190e6409b953dac3904594f4c982c92b894d0af241f3e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The extension depends on better-sqlite3, a native addon that can fail with Node ABI mismatches (e.g. Homebrew-installed Pi); it attempts one automatic npm rebuild and documents a manual rebuild path. -- evidence: [README.md#L161-L164](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L161-L164), [README.md#L153-L153](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L153-L153), [README.md#L159-L159](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L159-L159) (`clm_d68f1b0302c53cf03ffc047b53c7189bbdd59481ef8649e35b563222ffde01be`)

## limitations (2 claim(s))

- [observation/documented] Documented limitation: the FTS5 trigram tokenizer only supports CJK substring search for terms of three or more characters; one- and two-character memory_search terms may not match. -- evidence: [README.md#L712-L712](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L712-L712), [README.md#L364-L368](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L364-L368) (`clm_76e9df803ff5ea59a70ef0967467ffa240b208119eb05bab76f37c58969014b5`)
- [observation/documented] Recall in policy-only mode is probabilistic: a stored rule only takes effect if the agent calls memory_search before the relevant action, so prohibitions may be missed while preferences survive a missed lookup. -- evidence: [README.md#L194-L194](https://github.com/chandra447/pi-hermes-memory/blob/71ce9f0cf2985a52219b4fba0d3ebdd7c2f598df/README.md#L194-L194) (`clm_65d316b872c5828ec056e7cb0e120cb7d9a838d388c2be0335f396ee71ae598d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

