# patilshreyas/debroid

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 90139a0c1ab5 @ a2e8fba98b8e8276

## Summary (orientation draft, not independently verified)

Debroid is a headless CLI speaking the Java Debug Wire Protocol (JDWP) so AI agents can debug live Android apps via machine-parseable JSON without a GUI. CLI commands forward requests to a background daemon that auto-starts on first command, holds a long-lived JDWP socket via ADB port forwarding, and returns strict JSON on stdout.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Debroid is a headless CLI speaking the Java Debug Wire Protocol (JDWP) so AI agents can debug live Android apps via machine-parseable JSON without a GUI. -- evidence: [README.md#L12-L12](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L12-L12)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The daemon listens on localhost (127.0.0.1) without authentication for fast CLI communication, and the README warns it exposes live JVM manipulation and should only run on fully trusted machines. -- evidence: [README.md#L172-L174](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L172-L174)
  - [observation/documented] JSON serialization omits null fields (explicitNulls = false) to shrink payloads and save context tokens for AI agents. -- evidence: [CHANGELOG.md#L38-L38](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CHANGELOG.md#L38-L38)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must run ./gradlew detekt test :cli:build for fast verification and ./gradlew build before final commits, and must never use raw println in the CLI layer—only serialized JSON via kotlinx.serialization. -- evidence: [CONTRIBUTING.md#L21-L22](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L21-L22), [CONTRIBUTING.md#L15-L16](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L15-L16), [CONTRIBUTING.md#L25-L25](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L25-L25), [CONTRIBUTING.md#L18-L18](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L18-L18)
  - [observation/documented] Repository development practice: CLI JSON response models are guarded by golden schema tests in JsonSchemaGoldenTest; contributors update schemas with ./gradlew test -DupdateGoldenSchemas=true and must keep SKILL.md, README command reference, and CHANGELOG.md in sync with any command or output change. -- evidence: [CONTRIBUTING.md#L41-L43](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L41-L43), [CONTRIBUTING.md#L63-L70](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L63-L70), [CONTRIBUTING.md#L61-L61](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L61-L61), [CONTRIBUTING.md#L36-L39](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CONTRIBUTING.md#L36-L39)
- skills-patterns (1 claim(s)):
  - [observation/documented] The CLI auto-extracts AI skill instructions to ~/.debroid/skills/debroid-cli/SKILL.md on first run, and the README documents symlink setup for agents like Claude Code, Cursor, Codex, and OpenCode. -- evidence: [README.md#L75-L75](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L75-L75), [README.md#L114-L117](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L114-L117), [README.md#L90-L93](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L90-L93), [README.md#L98-L101](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L98-L101)
- interfaces (1 claim(s)):
  - [observation/documented] Commands include daemon, stop, launch, attach, detach, break, remove-break, catch-exception, and others, with global options like --port/DEBROID_PORT, --version, --help, --pretty, and --schema. -- evidence: [README.md#L144-L170](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L144-L170)
- memory-state (2 claim(s)):
  - [observation/documented] Features include recursive deep object inspection with cycle-guards, live variable mutation via set-var, expression evaluation in the target VM, and extraction of shallow locals from Kotlin Continuation frames. -- evidence: [README.md#L22-L29](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/README.md#L22-L29)
  - [observation/documented] The in-memory event buffer was increased to 10,000 events, and poll output includes droppedEventsSinceLastPoll to signal unnotified event loss under high volume. -- evidence: [CHANGELOG.md#L19-L22](https://github.com/PatilShreyas/debroid/blob/90139a0c1ab51df7b704540a221b541d26621649/CHANGELOG.md#L19-L22)
- orchestration (1 claim(s)):
More evidence: [full detail](debroid.detail.md)

Metadata and full claim list: [full detail](debroid.detail.md)
Human notes ([notes](debroid.notes.md), never overwritten by build)

[Back to map index](../../index.md)
