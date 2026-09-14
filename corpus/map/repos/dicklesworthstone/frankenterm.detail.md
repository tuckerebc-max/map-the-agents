# dicklesworthstone/frankenterm -- full detail

[Back to orientation](frankenterm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dicklesworthstone/frankenterm/9416f404da44cd59c8d95de17c18c94fb8bea2c2/89d4a383e008b698.json](../../../wiki/dossiers/dicklesworthstone/frankenterm/9416f404da44cd59c8d95de17c18c94fb8bea2c2/89d4a383e008b698.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] `ft` runs as the invoking user with no privilege separation; captured terminal bytes are redacted only on read surfaces, with the on-disk SQLite store holding raw bytes protected by file permissions. -- evidence: [SECURITY.md#L60-L86](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L60-L86), [SECURITY.md#L57-L58](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L57-L58) (`clm_12c60edba7a308a82be3f81c29c71c2eb639390ea1e236841cf3a70b9fd5eff4`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: releases must go exclusively through Doodlestein Self-Releaser (dsr) — doctor/health, quality, build, release, and verify commands — and GitHub Actions must never be inspected, triggered, or relied on for any claim. -- evidence: [AGENTS.md#L15-L16](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L15-L16), [AGENTS.md#L23-L33](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L23-L33), [AGENTS.md#L18-L21](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L18-L21), [AGENTS.md#L35-L45](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L35-L45) (`clm_90d4ae62b6f68a2efcf473f9a331a7a481ffd9adafe7c428d8d37bc2274ac33c`)
- [observation/documented] Repository development practice: agents may never delete files without explicit written permission, must not use git worktrees, must work on `main` (never `master`), and must avoid destructive commands like `git reset --hard` or `rm -rf` without explicit user authorization. -- evidence: [AGENTS.md#L197-L197](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L197-L197), [AGENTS.md#L187-L191](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L187-L191), [AGENTS.md#L166-L166](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L166-L166), [AGENTS.md#L110-L110](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L110-L110), [AGENTS.md#L112-L112](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L112-L112), [AGENTS.md#L168-L171](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L168-L171) (`clm_ea459120c95ef373dc95284b07d23d0ea39ff717f607af8c2648befd82f69f66`)
- [observation/documented] Repository development practice: direct tokio usage is forbidden; all async must go through the project's `runtime_async` asupersync wrapper, enforced by compile-time sealed traits, source grep guards, cargo-deny bans, and test-time checks. -- evidence: [AGENTS.md#L282-L298](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L282-L298), [AGENTS.md#L278-L278](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L278-L278), [AGENTS.md#L280-L280](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L280-L280) (`clm_0ee652287001d4ae33177d0b3def495535969f804b700a099122d4820b1cb305`)
- [observation/documented] Repository development practice: upstream WezTerm fixes are backported weekly via a read-only tracking ref with manual per-commit ports tagged `Upstream-WezTerm: <sha>`; blind pulls, merges, or bulk directory copies from upstream are prohibited. -- evidence: [AGENTS.md#L220-L228](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L220-L228), [AGENTS.md#L230-L260](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L230-L260), [AGENTS.md#L214-L218](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L214-L218) (`clm_d0137f85e3295818a0c7cb73a24b1869f1ff54f424ef2c9b638fd419f2146987`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The stdio MCP transport (`ft mcp serve`) inherits the OS uid/gid with no in-band authentication, while MCP tool inputs are validated via workspace containment, size caps, and approval gating on mutating tools. -- evidence: [SECURITY.md#L60-L86](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L60-L86) (`clm_fb337e2cf51c4d55e0ea07500271d803daf8ee09719cd38d19a134f779f14511`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] Per its security policy, the project has no CVE pipeline (fixes tracked by bead and commit) and release artifacts are not yet signed. -- evidence: [SECURITY.md#L104-L110](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L104-L110) (`clm_dad1a5bf1de07d03a0856f07526352d88fca3e59476413bff9f3b0b3dda7959e`)
- [observation/documented] The threat model treats host compromise and pre-existing DB write access as out of scope (attacker-equivalent), and notes findings requiring those positions should be reported as normal bugs. -- evidence: [SECURITY.md#L48-L53](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L48-L53), [SECURITY.md#L60-L86](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L60-L86) (`clm_735a327598ce7b0decf61d1f827a564edb2d08ccab93bbd6b104e417e8f48e20`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

