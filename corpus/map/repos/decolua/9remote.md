# decolua/9remote

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2f5d212b1d04 @ ec56ca565012a576

## Summary (orientation draft, not independently verified)

The snapshot contains only the README of 9remote, a proprietary remote-access tool (terminal, remote desktop, file explorer via phone/browser) distributed as an npm CLI; source code is not published yet. Claims below are documentation-based product descriptions.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Documented host support is macOS (Intel and Apple Silicon), Linux x64/arm64, and Windows x64; clients include modern browsers, iOS 14+, Android 8+, and a Tauri desktop app. -- evidence: [README.md#L364-L368](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L364-L368), [README.md#L359-L362](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L359-L362)
- components (1 claim(s)):
  - [observation/documented] Documented features include a WebSocket PTY terminal, WebRTC-based remote desktop streaming, file explorer, code editor, git integration, and a proxy exposing local dev-server ports through the tunnel. -- evidence: [README.md#L267-L271](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L267-L271), [README.md#L98-L115](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L98-L115)
- design-choices (3 claim(s)):
  - [observation/documented] Connectivity uses a Cloudflare Quick Tunnel with outbound-only connections, so no ports need to be opened and it works behind NAT, firewalls, and hotspots. -- evidence: [README.md#L327-L331](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L327-L331), [README.md#L44-L49](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L44-L49)
  - [observation/documented] A LocalFirstAdapter reportedly races LAN versus tunnel connections and picks the faster one, keeping traffic local when phone and host share Wi-Fi. -- evidence: [README.md#L338-L338](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L338-L338)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Running `9remote` starts a TUI mode with an interactive menu and QR code; `9remote ui` opens a web dashboard at localhost:2208, and a PORT env var can change the port. -- evidence: [README.md#L391-L393](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L391-L393), [README.md#L283-L286](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L283-L286)
  - [observation/documented] On first run the tool generates a permanent key tied to the machine ID and a one-time 30-minute key shown as a QR code for pairing a phone. -- evidence: [README.md#L232-L236](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L232-L236), [README.md#L229-L230](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L229-L230), [README.md#L227-L227](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L227-L227)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Access control is a Pair Device model: each new device must be explicitly approved before it can reach the host, and pending/rejected devices are managed from the TUI menu. -- evidence: [README.md#L44-L49](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L44-L49), [README.md#L297-L302](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L297-L302)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Documented stack: Node.js 20+, node-pty for PTY sessions, node-datachannel (WebRTC) plus robotjs for desktop control, Socket.IO for real-time, Preact agent UI, Next.js 16 web client, Tauri 2 desktop app, Expo mobile app, and Cloudflare Workers edge API. -- evidence: [README.md#L376-L385](https://github.com/decolua/9remote/blob/2f5d212b1d040b63728f52c3d7f9e79d559ed03a/README.md#L376-L385)
- limitations (2 claim(s)):
More evidence: [full detail](9remote.detail.md)

Metadata and full claim list: [full detail](9remote.detail.md)
Human notes ([notes](9remote.notes.md), never overwritten by build)

[Back to map index](../../index.md)
