# antigravity-nix (`antigravity-nix`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: jacopone
- License: MIT
- Language: Nix
- Interface: platforms=IDE; install=nix run github:jacopone/antigravity-nix; or add as an input to NixOS/Home Manager configurations
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [jacopone/antigravity-nix](../../repos/jacopone/antigravity-nix.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Auto-updating Nix Flake for Google Antigravity (an agentic IDE/CLI); auto-updates 3x/week via GitHub Actions with hash verification and build testing; provides three components (Antigravity 2.0 Base App, IDE, and CLI 'agy'); offers an FHS bubblewrap-sandboxed environment and a native autoPatchelfHook variant; supports version pinning for reproducible builds.

(captured site page body (agents/antigravity-nix.md), not a verified repo-code finding)
Google ships Antigravity as proprietary binaries that assume standard FHS filesystems, which NixOS lacks; this flake wraps them in an FHS environment with bubblewrap (plus a no-fhs variant using autoPatchelfHook) and exposes three packages: the Antigravity 2.0 base app, the legacy IDE, and the agy CLI. An automated workflow checks upstream daily at 0700 UTC, verifies hashes, tests the build, and publishes tagged pins like v2.0.3-6242596486512640, so users get reproducible versions or automatic tracking. Linux x86_64/aarch64 builds are CI-verified; macOS packages exist but are untested. MIT-licensed packaging of unfree software (allowUnfree required), unofficial and unaffiliated with Google, with 160 stars and active CI.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/antigravity-nix.md)
