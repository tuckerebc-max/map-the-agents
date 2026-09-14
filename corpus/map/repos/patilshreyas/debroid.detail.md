# patilshreyas/debroid -- full detail

[Back to orientation](debroid.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/patilshreyas/debroid/90139a0c1ab51df7b704540a221b541d26621649/a2e8fba98b8e8276.json](../../../wiki/dossiers/patilshreyas/debroid/90139a0c1ab51df7b704540a221b541d26621649/a2e8fba98b8e8276.json)

## specifications (1 claim(s))

- [observation/documented] Debroid is a headless CLI speaking the Java Debug Wire Protocol (JDWP) so AI agents can debug live Android apps via machine-parseable JSON without a GUI. -- evidence: [README.md#L12-L12](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L12-L12) (`clm_19cdc0975ad04bf45b0f2a5d56a5680636788e4ea301aa036d6619b2a4d95d3d`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The daemon listens on localhost (127.0.0.1) without authentication for fast CLI communication, and the README warns it exposes live JVM manipulation and should only run on fully trusted machines. -- evidence: [README.md#L172-L174](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L172-L174) (`clm_156b4340fb2c227cf29b9282859dd38d5d47228a26ea6ffc925cbbac29893b9d`)
- [observation/documented] JSON serialization omits null fields (explicitNulls = false) to shrink payloads and save context tokens for AI agents. -- evidence: [CHANGELOG.md#L38-L38](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CHANGELOG.md#L38-L38) (`clm_5d3c9cb689405016814fcce7f9d94382c350e36570d0ca03bbbcf872ae255fc6`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must run ./gradlew detekt test :cli:build for fast verification and ./gradlew build before final commits, and must never use raw println in the CLI layer—only serialized JSON via kotlinx.serialization. -- evidence: [CONTRIBUTING.md#L21-L22](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L21-L22), [CONTRIBUTING.md#L15-L16](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L15-L16), [CONTRIBUTING.md#L25-L25](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L25-L25), [CONTRIBUTING.md#L18-L18](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L18-L18) (`clm_9271ae6cd91a98ffb73c4b60cafeec033cdc6413914839cf1a1869f1210356dd`)
- [observation/documented] Repository development practice: CLI JSON response models are guarded by golden schema tests in JsonSchemaGoldenTest; contributors update schemas with ./gradlew test -DupdateGoldenSchemas=true and must keep SKILL.md, README command reference, and CHANGELOG.md in sync with any command or output change. -- evidence: [CONTRIBUTING.md#L41-L43](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L41-L43), [CONTRIBUTING.md#L63-L70](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L63-L70), [CONTRIBUTING.md#L61-L61](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L61-L61), [CONTRIBUTING.md#L36-L39](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L36-L39) (`clm_99542f5b662d255ad217bcd9c6cf245fcd7179b5accf9d3b9aa7efd5258e1e98`)

## skills-patterns (1 claim(s))

- [observation/documented] The CLI auto-extracts AI skill instructions to ~/.debroid/skills/debroid-cli/SKILL.md on first run, and the README documents symlink setup for agents like Claude Code, Cursor, Codex, and OpenCode. -- evidence: [README.md#L75-L75](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L75-L75), [README.md#L114-L117](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L114-L117), [README.md#L90-L93](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L90-L93), [README.md#L98-L101](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L98-L101) (`clm_a9ccbf50058029674d93079001b417d066b2a66acff1c18e605c7f2244095e9c`)

## interfaces (1 claim(s))

- [observation/documented] Commands include daemon, stop, launch, attach, detach, break, remove-break, catch-exception, and others, with global options like --port/DEBROID_PORT, --version, --help, --pretty, and --schema. -- evidence: [README.md#L144-L170](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L144-L170) (`clm_fb8e9a8f8b13e6fb5f0122c22ca2b7d7f1cdc8d6665cd7d1b3c6eafff37237e1`)

## memory-state (2 claim(s))

- [observation/documented] Features include recursive deep object inspection with cycle-guards, live variable mutation via set-var, expression evaluation in the target VM, and extraction of shallow locals from Kotlin Continuation frames. -- evidence: [README.md#L22-L29](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L22-L29) (`clm_750def0d7eee7e9b09a4a97abeef2f2436d351a9d363b8099045acfa4aa2ee49`)
- [observation/documented] The in-memory event buffer was increased to 10,000 events, and poll output includes droppedEventsSinceLastPoll to signal unnotified event loss under high volume. -- evidence: [CHANGELOG.md#L19-L22](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CHANGELOG.md#L19-L22) (`clm_4bfee066c64a4b4e972506915a446bb831af56b8f2b1ff50d0676011568ec1e3`)

## orchestration (1 claim(s))

- [observation/documented] CLI commands forward requests to a background daemon that auto-starts on first command, holds a long-lived JDWP socket via ADB port forwarding, and returns strict JSON on stdout. -- evidence: [README.md#L137-L140](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L137-L140) (`clm_478ff84156000bcac64e29f8bb9cbd1e51dce4ea4fc4361bc70799b83dbcd7f9`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Java JDK 11+ with JAVA_HOME set, plus Android SDK and adb on the PATH. -- evidence: [README.md#L40-L41](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L40-L41) (`clm_ae844949d4760acabc8446dea9a2ebbfe3ba00ad105fe17e54f523adfda2f927`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

