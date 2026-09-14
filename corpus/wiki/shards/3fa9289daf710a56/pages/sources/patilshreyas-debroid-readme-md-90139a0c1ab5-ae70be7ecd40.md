---
access: public
aliases: []
claim_ids:
- clm_156b4340fb2c227cf29b9282859dd38d5d47228a26ea6ffc925cbbac29893b9d
- clm_19cdc0975ad04bf45b0f2a5d56a5680636788e4ea301aa036d6619b2a4d95d3d
- clm_478ff84156000bcac64e29f8bb9cbd1e51dce4ea4fc4361bc70799b83dbcd7f9
- clm_750def0d7eee7e9b09a4a97abeef2f2436d351a9d363b8099045acfa4aa2ee49
- clm_a9ccbf50058029674d93079001b417d066b2a66acff1c18e605c7f2244095e9c
- clm_ae844949d4760acabc8446dea9a2ebbfe3ba00ad105fe17e54f523adfda2f927
- clm_fb8e9a8f8b13e6fb5f0122c22ca2b7d7f1cdc8d6665cd7d1b3c6eafff37237e1
maturity: draft
page_id: pg_2bbf0543cad15a1bbf30ae70be7ecd40
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bac38073475d5caba93a0c36a4e699fb
title: PatilShreyas/debroid/README.md @ 90139a0c1ab5
updated_at: '2026-09-14T04:15:05Z'
---

# PatilShreyas/debroid/README.md @ 90139a0c1ab5

<!-- rcw:begin owner=source:src_bac38073475d5caba93a0c36a4e699fb block=evidence -->
- The daemon listens on localhost (127.0.0.1) without authentication for fast CLI communication, and the README warns it exposes live JVM manipulation and should only run on fully trusted machines. [@claim:clm_156b4340fb2c227cf29b9282859dd38d5d47228a26ea6ffc925cbbac29893b9d]
- Debroid is a headless CLI speaking the Java Debug Wire Protocol (JDWP) so AI agents can debug live Android apps via machine-parseable JSON without a GUI. [@claim:clm_19cdc0975ad04bf45b0f2a5d56a5680636788e4ea301aa036d6619b2a4d95d3d]
- CLI commands forward requests to a background daemon that auto-starts on first command, holds a long-lived JDWP socket via ADB port forwarding, and returns strict JSON on stdout. [@claim:clm_478ff84156000bcac64e29f8bb9cbd1e51dce4ea4fc4361bc70799b83dbcd7f9]
- Features include recursive deep object inspection with cycle-guards, live variable mutation via set-var, expression evaluation in the target VM, and extraction of shallow locals from Kotlin Continuation frames. [@claim:clm_750def0d7eee7e9b09a4a97abeef2f2436d351a9d363b8099045acfa4aa2ee49]
- The CLI auto-extracts AI skill instructions to ~/.debroid/skills/debroid-cli/SKILL.md on first run, and the README documents symlink setup for agents like Claude Code, Cursor, Codex, and OpenCode. [@claim:clm_a9ccbf50058029674d93079001b417d066b2a66acff1c18e605c7f2244095e9c]
- Prerequisites are Java JDK 11+ with JAVA_HOME set, plus Android SDK and adb on the PATH. [@claim:clm_ae844949d4760acabc8446dea9a2ebbfe3ba00ad105fe17e54f523adfda2f927]
- Commands include daemon, stop, launch, attach, detach, break, remove-break, catch-exception, and others, with global options like --port/DEBROID_PORT, --version, --help, --pretty, and --schema. [@claim:clm_fb8e9a8f8b13e6fb5f0122c22ca2b7d7f1cdc8d6665cd7d1b3c6eafff37237e1]
<!-- rcw:end owner=source:src_bac38073475d5caba93a0c36a4e699fb block=evidence -->

## Researcher notes

