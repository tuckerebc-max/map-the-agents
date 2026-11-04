# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Vibeyard, please report it through [GitHub Security Advisories](https://github.com/elirantutia/vibeyard/security/advisories/new).

**Please do not open a public issue for security vulnerabilities.**

We will acknowledge your report within 72 hours and aim to release a fix within 7 days for critical issues.

## Scope

Vibeyard is a **local desktop application**. It runs on the user's machine and does not expose any network services. The threat model assumes the local user is trusted.

## Known Limitations

- **Unsigned builds** — macOS builds are not code-signed or notarized. Users must bypass Gatekeeper with `xattr -cr` on first launch.
- **Sandbox disabled** — Electron's sandbox is disabled (`sandbox: false`) because `node-pty` requires direct Node.js access from the main process. Context isolation is enabled.
- **Temp directory usage** — Inter-process hook data is written to `/tmp/vibeyard/`. This is planned to move to a user-scoped directory in a future release.
