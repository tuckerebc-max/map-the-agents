# shrijayan/itwillsync -- full detail

[Back to orientation](itwillsync.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shrijayan/itwillsync/f12b57bf7385cfaedc119a90d147d90e1437a7f2/49324d424dafa83f.json](../../../wiki/dossiers/shrijayan/itwillsync/f12b57bf7385cfaedc119a90d147d90e1437a7f2/49324d424dafa83f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The architecture pairs a node-pty-backed agent process and HTTP/WebSocket server on the laptop with a browser terminal client on the phone, connected via WebSocket with token auth. -- evidence: [README.md#L60-L72](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L60-L72) (`clm_243aa14ba3aeb9977d8b6ba699823383a98149e041d49e2141a2ef596cc125d1`)
- [observation/documented] The monorepo contains packages for the CLI (main npm package), a web-client browser terminal, a hub dashboard daemon, a landing page, and VitePress docs. -- evidence: [README.md#L199-L206](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L199-L206), [CONTRIBUTING.md#L32-L38](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L32-L38) (`clm_82f86f56c02c3003ff186abb3e7472b3e50f675c6341557a234cb632efe71f7a`)

## design-choices (4 claim(s))

- [observation/documented] The product is agent-agnostic: it works with any terminal-based tool, citing Claude Code, Aider, Codex, Goose, Cline, and Copilot CLI, without vendor lock-in. -- evidence: [README.md#L120-L120](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L120-L120), [README.md#L130-L130](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L130-L130), [README.md#L44-L47](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L44-L47) (`clm_8ef14b8cc2eafe8960fcf64a9e7afbd34dbdbc97dd5f41cbc6986231ee38563b`)
- [observation/documented] Connections run over the local network (or Tailscale) with no cloud component, no accounts, and no telemetry; three connection modes are local WiFi (default), Tailscale, and localhost-only. -- evidence: [README.md#L134-L138](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L134-L138), [README.md#L49-L52](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L49-L52) (`clm_3f2df59fc645581ded2c2128d8c93ee38cf9f7a4c7d2e1adfda2fe317295a197`)
- [observation/documented] The client auto-reconnects with scrollback buffer sync after connection drops, renders via WebGL on desktop with canvas fallback on mobile, and plays audio notifications when agents need attention. -- evidence: [README.md#L181-L184](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L181-L184) (`clm_b272bb8d2c1c1b21e492b4063262f53d0f979c80b75389f4297cb76f744fa599`)
- [observation/documented] A first-run setup wizard detects the network and saves the connection preference; per-session overrides via --tailscale/--local and a re-run via 'npx itwillsync setup' are supported. -- evidence: [README.md#L147-L148](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L147-L148), [README.md#L140-L140](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L140-L140), [README.md#L151-L152](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L151-L152) (`clm_9d5d31dad10242132779c21a7fa2ab2e41e14f71cf39cefec8226e32de5ce3bb`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use Node 22+ via nvm and pnpm 10+, build packages in order (web-client, hub, CLI) with pnpm build, run pnpm test (optionally with --coverage), and open focused PRs against main with tests and passing CI. -- evidence: [CONTRIBUTING.md#L55-L57](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L55-L57), [CONTRIBUTING.md#L71-L71](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L71-L71), [CONTRIBUTING.md#L9-L11](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L9-L11), [CONTRIBUTING.md#L84-L88](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L84-L88), [CONTRIBUTING.md#L42-L46](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L42-L46), [CONTRIBUTING.md#L67-L69](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L67-L69), [CONTRIBUTING.md#L60-L61](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L60-L61) (`clm_eae6dd8cc17c310ec477b5c9cae1668f9131230091e2b4464c105443035951e7`)
- [observation/documented] Repository development practice: code style is TypeScript with ESM modules, no linter is enforced yet (follow existing patterns), dependencies should stay minimal, and contributions are MIT-licensed. -- evidence: [CONTRIBUTING.md#L105-L107](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L105-L107), [CONTRIBUTING.md#L111-L111](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L111-L111) (`clm_2b3acfa713a425ff1c1d1d27ad16cff190ab5e9e5f67213a8a7d783831ff7c53`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI is invoked as npx itwillsync followed by an agent command (e.g. claude, aider, or any terminal command), with no install required but Node.js 20+ needed. -- evidence: [README.md#L30-L30](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L30-L30), [README.md#L24-L28](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L24-L28) (`clm_9e42627bab5d304617b92e771633d76c768790ea1c302285a4cbbc30a35a3a61`)
- [observation/documented] Documented CLI flags include --port (default 7964), --localhost, --tailscale, --local, --no-qr, a setup subcommand, and -h/-v. -- evidence: [README.md#L156-L165](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L156-L165) (`clm_10647f653b6300ff706196fbd3a23ed9165972c91357df4a8cab220d3266fec8`)
- [observation/documented] On startup the tool prints a QR code in the terminal; scanning it opens a browser-based terminal (xterm.js) on the phone with a touch keyboard and extra keys bar. -- evidence: [README.md#L181-L184](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L181-L184), [README.md#L60-L72](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L60-L72), [README.md#L179-L179](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L179-L179), [README.md#L74-L77](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L74-L77) (`clm_7259c6ab8a3722472e3a87a10cb277cf5ad25f57ff70c740efd099a304da0610`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A hub daemon provides a multi-session dashboard showing each agent's name, working directory, status, and uptime, with real-time WebSocket updates and tap-to-open full terminal. -- evidence: [README.md#L90-L90](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L90-L90), [README.md#L112-L116](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L112-L116) (`clm_41d7703f37ca8a016627434b5e5c55d21e212122608a2ef858798b2d32665705`)

## tools-permissions (1 claim(s))

- [observation/documented] Security model: WebSocket messages are encrypted with NaCl secretbox (XSalsa20-Poly1305), each session gets a random 64-character token embedded in the QR URL, auth uses constant-time comparison, and 5 failed attempts lock out an IP for 60 seconds. -- evidence: [README.md#L169-L175](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L169-L175) (`clm_f18cc7263a3c3dc889cb827a8d92cce538e463b2cb49d51bad7cd7fb9ec72a9a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

