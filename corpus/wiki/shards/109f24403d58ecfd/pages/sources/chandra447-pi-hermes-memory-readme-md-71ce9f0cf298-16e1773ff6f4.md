---
access: public
aliases: []
claim_ids:
- clm_0ed3a5f6dada7c30fad190e6409b953dac3904594f4c982c92b894d0af241f3e
- clm_11d11a9e7a75fb82606133515004e925b83d48417c6f2e400d51fb980408e806
- clm_174d6ccc66bb2780849db40869c7a507e5576cd8de47c0b52f2b4e43cf640d3a
- clm_549b4cc1458defe07304f3f91f87f8a9fa2be589e1464d010f413fa1495f0aa5
- clm_5a94283b8169a656389fee0af3cd4a261aa7698c18e07c334ad0707c65578e74
- clm_5bf8d5fecb60836b6e1d053e2ec3841f211f82ef69f3d17d804384d046475a70
- clm_65d316b872c5828ec056e7cb0e120cb7d9a838d388c2be0335f396ee71ae598d
- clm_66ed01198b939cf0e662e3121f2f3041bd65a0d953c2f47f0f71bc8d4e4835a5
- clm_71c1269ca8202fddf04f70b3b22db72280b795be23766a866cf9bbe9b6d514dc
- clm_720499bf6eb3082cf3586fdb2a464558987791b361f1c13cc447401faf30a128
- clm_76e9df803ff5ea59a70ef0967467ffa240b208119eb05bab76f37c58969014b5
- clm_7a9b488cd6ef4296820e19d84378c46a25e9de0be7474e2b5399c67e39398847
- clm_840b3c4c74a5ae2f348ac648de9d507d6b14ff232c355c08ccad8e9b6823f0fa
- clm_8a0d9d2138ba89ac9efa0eb7b9b1122d1d0f01a5c2e3f9ca9486a5bbbd7ab184
- clm_97623f29447ae2caf1d26dfed8c6ad193480464a0fe682bc2d4815325d48ef54
- clm_d68f1b0302c53cf03ffc047b53c7189bbdd59481ef8649e35b563222ffde01be
- clm_db4b31709c9d5819e3c3635381caf139c887469b57fba85194e2aca9e57210e7
- clm_deeb1d9cfe252fe7a36fe1ed59c9c8e77687df74ff488f6d1486bdee6e0b3dfd
- clm_e6d54ad2abe524e1dd97076f7acc92ba99b5c23b081c67117ab2d66b9828e645
maturity: draft
page_id: pg_351e253dd1205c37b83316e1773ff6f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_032573c44b4453b9b740d354a30300ba
title: chandra447/pi-hermes-memory/README.md @ 71ce9f0cf298
updated_at: '2026-09-14T03:41:06Z'
---

# chandra447/pi-hermes-memory/README.md @ 71ce9f0cf298

<!-- rcw:begin owner=source:src_032573c44b4453b9b740d354a30300ba block=evidence -->
- In legacy-inject mode, when memory hits its character limit the extension spawns a one-shot consolidation child process that merges entries, then reloads and retries the save; in policy-only mode SQLite is the query authority and consolidation is manual via /memory-consolidate. [@claim:clm_0ed3a5f6dada7c30fad190e6409b953dac3904594f4c982c92b894d0af241f3e]
- Standing instructions (/memory-pin) are a user-authored file injected into every session in every memory mode, capped at 20 entries / 2,000 characters, stored in STANDING.md which background processes cannot write; the feature is explicitly not tool enforcement. [@claim:clm_11d11a9e7a75fb82606133515004e925b83d48417c6f2e400d51fb980408e806]
- For create and update, skill_manage prefers structured fields (when_to_use, procedure_steps, pitfalls, verification_steps) rendered into SKILL.md sections, and global creation has duplicate/similarity guards blocking exact slug matches and near-name collisions. [@claim:clm_174d6ccc66bb2780849db40869c7a507e5576cd8de47c0b52f2b4e43cf640d3a]
- The extension manages three knowledge types: MEMORY.md facts (5,000-char cap), USER.md profile (5,000-char cap), and Pi-native SKILL.md procedures with unlimited size. [@claim:clm_549b4cc1458defe07304f3f91f87f8a9fa2be589e1464d010f413fa1495f0aa5]
- By default review, flush, correction save, and manual consolidation use an in-process completeSimple() side-channel, falling back to a pi -p --no-session subprocess on failure; reviewTransport can force subprocess-only behavior. [@claim:clm_5a94283b8169a656389fee0af3cd4a261aa7698c18e07c334ad0707c65578e74]
- Background review triggers every 10 turns or every 15 tool calls, with both counters reset after each review; correction detection saves immediately when the user corrects the agent. [@claim:clm_5bf8d5fecb60836b6e1d053e2ec3841f211f82ef69f3d17d804384d046475a70]
- Recall in policy-only mode is probabilistic: a stored rule only takes effect if the agent calls memory_search before the relevant action, so prohibitions may be missed while preferences survive a missed lookup. [@claim:clm_65d316b872c5828ec056e7cb0e120cb7d9a838d388c2be0335f396ee71ae598d]
- Project-scoped skills are exposed to Pi via the resources_discover hook, which returns the active project's skills directory so Pi discovers them natively without copying into the global folder. [@claim:clm_66ed01198b939cf0e662e3121f2f3041bd65a0d953c2f47f0f71bc8d4e4835a5]
- Memory is stored at two tiers: global facts under ~/.pi/agent/pi-hermes-memory/ and per-project facts under ~/.pi/agent/projects-memory/<project>/, with project memories searchable when the cwd matches. [@claim:clm_71c1269ca8202fddf04f70b3b22db72280b795be23766a866cf9bbe9b6d514dc]
- An optional lazyInitialization mode defers Markdown/SQLite sync, memory loading, maintenance, and session indexing until the first memory operation, while pinned STANDING.md instructions and skill discovery remain available at startup; legacy-inject ignores the option. [@claim:clm_720499bf6eb3082cf3586fdb2a464558987791b361f1c13cc447401faf30a128]
- Documented limitation: the FTS5 trigram tokenizer only supports CJK substring search for terms of three or more characters; one- and two-character memory_search terms may not match. [@claim:clm_76e9df803ff5ea59a70ef0967467ffa240b208119eb05bab76f37c58969014b5]
- An opt-in sessionSearch.variant of 'anchors' makes session_search read session JSONL files directly and return path:startLine-endLine anchors with short reasons instead of summaries. [@claim:clm_7a9b488cd6ef4296820e19d84378c46a25e9de0be7474e2b5399c67e39398847]
- The agent gets memory write tools memory_add, memory_replace, and memory_remove with targets memory, user, project, and failure, plus a skill_manage tool with create, view, patch, update, and delete actions. [@claim:clm_840b3c4c74a5ae2f348ac648de9d507d6b14ff232c355c08ccad8e9b6823f0fa]
- Slash commands include /memory-insights, /memory-skills, /memory-consolidate, /memory-interview, /memory-index-sessions, /memory-sync-markdown, /memory-preview-context, /memory-pin, and /learn-memory-tool. [@claim:clm_8a0d9d2138ba89ac9efa0eb7b9b1122d1d0f01a5c2e3f9ca9486a5bbbd7ab184]
- Memory blocks are wrapped in <memory-context> XML tags with a guard note stating they are not new user input, to prevent the model from treating stored facts as instructions. [@claim:clm_97623f29447ae2caf1d26dfed8c6ad193480464a0fe682bc2d4815325d48ef54]
- The extension depends on better-sqlite3, a native addon that can fail with Node ABI mismatches (e.g. Homebrew-installed Pi); it attempts one automatic npm rebuild and documents a manual rebuild path. [@claim:clm_d68f1b0302c53cf03ffc047b53c7189bbdd59481ef8649e35b563222ffde01be]
- Search tools include session_search over past conversations and memory_search over the extended store; FTS5 with a trigram tokenizer supports multi-word, quoted-phrase, OR-operator, and CJK substring queries of three or more characters. [@claim:clm_db4b31709c9d5819e3c3635381caf139c887469b57fba85194e2aca9e57210e7]
- A hybrid architecture keeps Markdown as the human-readable source of truth while mirroring successful writes into a SQLite store (sessions.db) queried via memory_search; failed core writes are not silently spilled into SQLite-only storage. [@claim:clm_deeb1d9cfe252fe7a36fe1ed59c9c8e77687df74ff488f6d1486bdee6e0b3dfd]
- By default full Markdown memories are not injected into the system prompt; instead a <memory-policy> block tells the agent when to call memory_search, keeping first-turn token usage low. [@claim:clm_e6d54ad2abe524e1dd97076f7acc92ba99b5c23b081c67117ab2d66b9828e645]
<!-- rcw:end owner=source:src_032573c44b4453b9b740d354a30300ba block=evidence -->

## Researcher notes

