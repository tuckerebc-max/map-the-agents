# decolua/9remote -- full detail

[Back to orientation](9remote.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/decolua/9remote/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/ec56ca565012a576.json](../../../wiki/dossiers/decolua/9remote/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/ec56ca565012a576.json)

## specifications (1 claim(s))

- [observation/documented] Documented host support is macOS (Intel and Apple Silicon), Linux x64/arm64, and Windows x64; clients include modern browsers, iOS 14+, Android 8+, and a Tauri desktop app. -- evidence: [README.md#L364-L368](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L364-L368), [README.md#L359-L362](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L359-L362) (`clm_b5d5df1519001fe76bf712b8f10d9eb3f376a2a7a1cf8b88d7b8f9c9babe61e3`)

## components (1 claim(s))

- [observation/documented] Documented features include a WebSocket PTY terminal, WebRTC-based remote desktop streaming, file explorer, code editor, git integration, and a proxy exposing local dev-server ports through the tunnel. -- evidence: [README.md#L267-L271](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L267-L271), [README.md#L98-L115](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L98-L115) (`clm_558a78834dca145b97491084aa8db3be1da19771fc5133b7d8686374771e1c00`)

## design-choices (3 claim(s))

- [observation/documented] Connectivity uses a Cloudflare Quick Tunnel with outbound-only connections, so no ports need to be opened and it works behind NAT, firewalls, and hotspots. -- evidence: [README.md#L327-L331](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L327-L331), [README.md#L44-L49](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L44-L49) (`clm_9e6241f01445377f59b13aec5a3c21664d5b44718f1a824191afae7ec43a76ea`)
- [observation/documented] A LocalFirstAdapter reportedly races LAN versus tunnel connections and picks the faster one, keeping traffic local when phone and host share Wi-Fi. -- evidence: [README.md#L338-L338](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L338-L338) (`clm_b038b5d8db222ef321470f12320a246944dda8ec07089152932d9f02baaae403`)
- [observation/documented] Remote desktop uses adaptive framerate (60ms active, 400ms idle) with tile-based diff rendering so only changed screen regions are sent. -- evidence: [README.md#L255-L258](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L255-L258) (`clm_5b5de097917769c1521417c9a0d3094f73efd264b951a8d5de180d32d8c18047`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Running `9remote` starts a TUI mode with an interactive menu and QR code; `9remote ui` opens a web dashboard at localhost:2208, and a PORT env var can change the port. -- evidence: [README.md#L391-L393](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L391-L393), [README.md#L283-L286](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L283-L286) (`clm_2478597e4b29f09c2ae1c894913985983206eb0e0207f4163aefee7242361179`)
- [observation/documented] On first run the tool generates a permanent key tied to the machine ID and a one-time 30-minute key shown as a QR code for pairing a phone. -- evidence: [README.md#L232-L236](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L232-L236), [README.md#L229-L230](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L229-L230), [README.md#L227-L227](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L227-L227) (`clm_baf6918bb45c7adb2d1c1c54a0882221ddf95cdfe4d30f5d2737fa7af524c937`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Access control is a Pair Device model: each new device must be explicitly approved before it can reach the host, and pending/rejected devices are managed from the TUI menu. -- evidence: [README.md#L44-L49](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L44-L49), [README.md#L297-L302](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L297-L302) (`clm_ca77a94557a5051aaf22bcf6d55a0cf10955baeffe2a5c7d5ba5818fb2d802c8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Documented stack: Node.js 20+, node-pty for PTY sessions, node-datachannel (WebRTC) plus robotjs for desktop control, Socket.IO for real-time, Preact agent UI, Next.js 16 web client, Tauri 2 desktop app, Expo mobile app, and Cloudflare Workers edge API. -- evidence: [README.md#L376-L385](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L376-L385) (`clm_56c66faea893302ee940f6cb7d590b0adc895b98b07dfb19a8110ed79d22d87b`)

## limitations (2 claim(s))

- [observation/documented] The project is proprietary and not open-source; the npm package is free during development, with MIT licensing planned only after a star milestone. -- evidence: [README.md#L309-L309](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L309-L309), [README.md#L442-L442](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L442-L442), [README.md#L311-L311](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L311-L311), [README.md#L444-L444](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L444-L444), [README.md#L446-L446](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L446-L446) (`clm_1bd859a9c43b8f5bb56ceba786b4a83dd51005ba61ba302a5e77f1d639f611b1`)
- [observation/documented] Remote desktop on macOS requires the user to grant Screen Recording and Accessibility permissions to Terminal or the 9Remote desktop app, and restart 9Remote afterward. -- evidence: [README.md#L399-L401](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L399-L401), [README.md#L245-L245](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L245-L245), [README.md#L247-L248](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L247-L248) (`clm_336e370e098293fec031ee9a7802e85ce1de6dcc93554657bd52e44f08543b3e`)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers who want to reach their dev machine's terminal, desktop, and files from a phone or browser, and is stated to work with terminal-based AI coding tools like Claude Code and Codex CLI. -- evidence: [README.md#L352-L352](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L352-L352), [README.md#L345-L350](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L345-L350), [README.md#L8-L8](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L8-L8) (`clm_9686ba383edf3920446c4276a7ff172a4d8712b017d432f304d7ac857b7acba4`)

