# jo-inc/pi-reflect -- full detail

[Back to orientation](pi-reflect.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jo-inc/pi-reflect/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/48284f3d7486af39.json](../../../wiki/dossiers/jo-inc/pi-reflect/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/48284f3d7486af39.json)

## specifications (1 claim(s))

- [observation/documented] pi-reflect provides iterative self-improvement for pi coding agents: it reads recent conversations and reference material, compares actual behavior against a defined target, and edits the target file to close the gap. -- evidence: [README.md#L18-L18](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L18-L18), [README.md#L14-L14](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L14-L14), [README.md#L16-L16](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L16-L16) (`clm_59cd8c99132308fb69a143c65e8df55b7633b23d4f6518f5301d4a7d055a78dd`)

## components (1 claim(s))

- [observation/documented] Each run collects evidence from transcripts, daily logs, and reference files, sends evidence plus the target file and a prompt to an LLM, then applies the LLM's proposed edits with safety checks. -- evidence: [README.md#L45-L48](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L45-L48) (`clm_5679f1f801687ba24152b92060c54285863babeb737a4b685412abbfd6a69dc0`)

## design-choices (2 claim(s))

- [observation/documented] Edit safety measures include backing up the original, skipping ambiguous matches, rejecting suspiciously large deletions, and auto-committing to git when the target is in a repository. -- evidence: [README.md#L45-L48](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L45-L48), [README.md#L50-L50](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L50-L50) (`clm_5f6696be287d7d7516ac1b6e4e96e716a9d98b685831bac69a75b56a0665a16d`)
- [observation/documented] Data sources support three types (files with glob patterns, shell commands capturing stdout, and HTTP URLs), all with {lookbackDays} interpolation and per-source maxBytes caps; file sources are date-pruned by filename. -- evidence: [README.md#L58-L62](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L58-L62), [README.md#L64-L64](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L64-L64) (`clm_4286e5dbb05ae508648e60708481a621fb154404b62193e9bf1b711eda0b97b0`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm install and npm test (137 tests), and can test locally with pi -e ./extensions/index.ts without installing. -- evidence: [README.md#L163-L167](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L163-L167) (`clm_b568b027e7c0c42f5c87b51c19cf3eb0de0cad9b78da654dfde01559551955bb`)
- [observation/documented] Repository development practice: SETUP.md is an instruction guide addressed to the coding agent for installing, locating a target file, running a first /reflect, and scheduling daily runs via launchd or cron. -- evidence: [SETUP.md#L60-L97](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L60-L97), [SETUP.md#L3-L3](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L3-L3), [SETUP.md#L115-L118](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L115-L118), [SETUP.md#L42-L42](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L42-L42) (`clm_28e7e2ff579406ca590719fb772e6a38e10886e2c37e3205bfc4ede6ec77bcd3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes slash commands: /reflect (optionally with a file path), /reflect-config, /reflect-history, /reflect-stats, and /reflect-backfill. -- evidence: [README.md#L32-L39](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L32-L39) (`clm_519cca9eab04a2918c1d6c6249b735d83f59394dc4e7ad4c9ce1f0ad174862c7`)
- [observation/documented] Configuration lives in ~/.pi/agent/reflect.json with a targets array; each target requires a path and model, and supports lookbackDays, maxSessionBytes, transcripts, transcriptSource, context, prompt, and backupDir fields. -- evidence: [README.md#L124-L135](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L124-L135), [README.md#L137-L147](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L137-L147), [README.md#L122-L122](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L122-L122) (`clm_a734af846c931536b749636279cbd6b5950be5008c9e46eb41601dee1d4d4e85`)

## memory-state (1 claim(s))

- [observation/documented] Targets are any markdown file, e.g. AGENTS.md for behavioral rules, MEMORY.md for long-term memory, or SOUL.md for personality; the prompt determines whether reflect strengthens rules, extracts durable facts, or sharpens identity. -- evidence: [README.md#L20-L20](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L20-L20), [README.md#L94-L98](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L94-L98) (`clm_d122522e3727471b8d69bbae0879a838ed5e8a5014d0640ff18a4dfb3ac593cb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] /reflect-stats tracks reflection impact via a correction-rate trend (corrections per session over time) and rule recidivism (sections edited repeatedly); /reflect-backfill bootstraps stats from historical sessions in dry-run mode without editing files. -- evidence: [README.md#L112-L112](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L112-L112), [README.md#L114-L114](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L114-L114), [README.md#L118-L118](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L118-L118), [README.md#L116-L116](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L116-L116) (`clm_eb1d07658535882fa2790a812ca4b999ffafe927de0715dc34f5d12c636d0af8`)

## dependencies (1 claim(s))

- [observation/documented] The tool requires pi with an LLM API key configured; each run makes one LLM call, estimated at roughly $0.05–0.15 with Sonnet, and models are specified as provider/model-id strings. -- evidence: [README.md#L28-L28](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L28-L28), [README.md#L137-L147](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L137-L147), [SETUP.md#L153-L158](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L153-L158) (`clm_59ee74960cb8cd751211cc325a4b2d0d245ea6016a1934228c96e6771de1d39c`)

## limitations (1 claim(s))

- [observation/documented] Documented runtime constraints: sessions with fewer than 3 exchanges are not considered substantive, and the target file must be at least 100 bytes; skipped edits are logged with reasons such as ambiguous match or text not found. -- evidence: [SETUP.md#L164-L168](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L164-L168) (`clm_42f4ad5dacb79504f42de84f269a6a34fca034edcf82b5d2820131447546e83b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

