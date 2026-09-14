# h5i-dev/h5i -- full detail

[Back to orientation](h5i.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/h5i-dev/h5i/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/0b836cce6be3abbe.json](../../../wiki/dossiers/h5i-dev/h5i/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/0b836cce6be3abbe.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The engine is the HTTP client: every request is policy-checked and recorded before bytes move, and a fetch that cannot be recorded is refused, so the log is a decision record. -- evidence: [MANUAL.md#L229-L234](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L229-L234), [MANUAL.md#L14-L16](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L14-L16) (`clm_6d00511d06a0790e4de2617a462177f4d28cd89472f34b6e6c1092f4f66bc45c`)
- [observation/documented] A session grants only the origin it was opened on; --allow adds named origins, loopback is reachable by default unless --no-loopback, and off-origin subresources are refused and logged. -- evidence: [MANUAL.md#L252-L254](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L252-L254), [MANUAL.md#L245-L250](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L245-L250) (`clm_38ba189317864945afe8c1d41cb03d4d03fa179bae3ce0d11de810b9b754496d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The manual's command table lists groups including browser, box, box share, ui, runner, skill, plugin, websec, recon, join, and shell completions. -- evidence: [MANUAL.md#L137-L149](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L137-L149) (`clm_4a6b5bcd7d94345e631ed06921e78a771c7af6fa484985289b04469997fc6340`)
- [observation/documented] Browser sessions are driven by verbs such as open, snapshot, click, type, extract, markdown, requests, audit, screenshot, reload, and close, with @ref handles identifying page elements. -- evidence: [README.md#L99-L107](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/README.md#L99-L107), [README.md#L39-L44](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/README.md#L39-L44), [MANUAL.md#L165-L173](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L165-L173) (`clm_54d1a8c542f6fc1c53662bb895bfdc1d229de4e5a4068bcffb3f5b2a8b86eaf2`)
- [observation/documented] Verbs resolve a session via --session name or id, the H5I_BROWSER_SESSION variable, or the last-opened session; there is deliberately no single-live-session default. -- evidence: [MANUAL.md#L208-L211](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L208-L211), [MANUAL.md#L190-L193](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L190-L193) (`clm_70494c6b379bdb0bd2eb145eeb4e30c2d4330a0c548f4f72b530f2eeb593eab0`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Boxes are disposable environments holding code, agent, toolchain and optionally the browser session; box export produces a patch, report, receipt and timelines, and the agent has no direct host write path. -- evidence: [MANUAL.md#L35-L50](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L35-L50), [MANUAL.md#L93-L96](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L93-L96) (`clm_18a7e7f62eecae052005e8ee7f6437bae63aca2c6beb93a38d4d6027c83440fd`)

## tools-permissions (1 claim(s))

- [observation/documented] By default a session runs unsandboxed on the host machine; --in places it in a box whose egress allowlist is enforced at a network boundary outside the engine. -- evidence: [MANUAL.md#L225-L227](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L225-L227), [MANUAL.md#L334-L339](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L334-L339), [MANUAL.md#L369-L373](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L369-L373) (`clm_3ab328624b2f95a74a76b5c6f16456314774aac88a2ede622f236c238d2f2cc6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] h5i is one Rust binary with no server, daemon, or SaaS; websec and recon are optional plugins shipped as separate archives and registered via h5i plugin install. -- evidence: [MANUAL.md#L29-L29](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L29-L29), [MANUAL.md#L117-L120](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L117-L120) (`clm_8ce1c36a01b02366afdc324ae26bd0a02a9424c21a966f7670075322b204ee98`)

## limitations (3 claim(s))

- [observation/documented] The manual states the browser is incomplete: Canvas, WebSockets, Workers and IndexedDB are absent, and of twenty SPAs measured, eighteen read usefully and one not at all. -- evidence: [MANUAL.md#L58-L70](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L58-L70) (`clm_45dd7056130d09882cca1838a55ae14d96c23f2d76aad537f1fab23caa36cba0`)
- [observation/documented] Resident sessions in a box on Linux require a tier that keeps the engine alive; the supervised tier cannot hold a resident process because its seccomp-notify gate dies with the starting command. -- evidence: [MANUAL.md#L375-L382](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L375-L382), [MANUAL.md#L408-L412](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L408-L412) (`clm_1b0ca20ffdf79af0f570cfc76422ddf2c23e0b5f74647cd3983fd9de50ad20b7`)
- [observation/documented] Only the firefox-143-linux identity is currently supported; Chrome identities need client hints and WebGL capabilities the engine lacks, and identity consistency is explicitly not anonymity. -- evidence: [MANUAL.md#L310-L311](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L310-L311), [MANUAL.md#L304-L308](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L304-L308) (`clm_874bc843f28ba695dcd5feb2c491b275a844395f747185bb0650c700608c102f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

