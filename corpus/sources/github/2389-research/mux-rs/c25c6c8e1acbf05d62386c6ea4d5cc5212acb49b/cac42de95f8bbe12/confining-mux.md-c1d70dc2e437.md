# Confining mux's built-in tools

mux's built-in tools accept any path and any URL by default. That is the right
default for a trusted, locally-run agent, but a confused or prompt-injected model
can turn `read_file` into `~/.ssh/id_rsa` exfiltration, `write_file` into
arbitrary disk writes, or `web_fetch` into a request to a cloud-metadata endpoint
like `http://169.254.169.254/`.

mux ships **two opt-in guardrails**. Both are **off by default** — existing
constructors are unchanged.

> **This is not a sandbox.** It is in-process defense-in-depth against a *confused
> or injected model*, not against native-code execution. A model that can run an
> un-jailed `bash` can `cat ~/.ssh/id_rsa` or `curl 169.254.169.254` straight
> through the shell, bypassing everything below. **The filesystem jail only has
> teeth in a deployment that also drops or OS-sandboxes `bash`.**

## 1. The filesystem jail (`RootedFs`)

`RootedFs` is a canonicalized root that paths are confined to. Construct the
filesystem tools with `::rooted(...)` instead of `::new()`:

```rust
use mux::confine::RootedFs;
use mux::tools::{EditTool, ListFilesTool, ReadFileTool, SearchTool, WriteFileTool};

let jail = RootedFs::new("/srv/agent/workspace")?; // must exist; canonicalized once
let read = ReadFileTool::rooted(jail.clone());
let write = WriteFileTool::rooted(jail.clone());
let edit = EditTool::rooted(jail.clone());
let search = SearchTool::rooted(jail.clone());
let list = ListFilesTool::rooted(jail);
```

A rooted tool resolves every tool-supplied path against the root:

- relative paths are joined onto the root;
- absolute paths must already be inside the root;
- `..` traversal and symlink escapes are rejected;
- a not-yet-existing leaf (for writes) is allowed if its existing ancestor
  canonicalizes within the root;
- `search` / `list_files` additionally drop glob hits that resolve outside the
  root, so a symlink inside the root cannot leak outside content.

Violations are returned as a tool **error result** (not a hard failure), so the
model sees "path … escapes the confinement root" and can adapt.

### Residual race (TOCTOU)

`read_file` re-verifies containment at open time. Against the confused-model
threat this is sufficient. Against a *local attacker actively swapping a symlink*
between resolution and open, it is best-effort: fully closing the race needs
platform-specific `openat2(RESOLVE_BENEATH)` (Linux), which is not portable and
out of scope.

## 2. The `web_fetch` SSRF guard (`UrlPolicy`)

`WebFetchTool::guarded()` refuses to fetch private/internal addresses and
re-validates the host on **every redirect hop**:

```rust
use mux::tools::WebFetchTool;

let fetch = WebFetchTool::guarded(); // UrlPolicy::public_only()
```

The default `UrlPolicy::public_only()` denies unspecified, loopback, RFC1918
private, link-local (including `169.254.169.254`), CGNAT/shared (`100.64/10`),
IPv6 unique-local (`fc00::/7`), broadcast, documentation ranges, and the
IPv4-mapped IPv6 forms of all of these. Supply your own predicate with
`UrlPolicy::custom(|ip| ...)` and `WebFetchTool::with_url_policy(policy)`.

Guarded mode disables reqwest's automatic redirect following and runs a manual
loop (max 10 hops), resolving and re-checking each hop's host before connecting.

### Residual race (DNS rebinding)

reqwest connects by hostname, so a DNS-rebinding attacker could return a public
IP to our resolver and a private IP to the actual connect. Pinning the connection
to the resolved IP is future hardening; for the confused-model threat, per-hop
resolution plus the deny-list is the right level.

### Known gaps in the deny-list

`is_globally_routable` is a deny-list of unicast ranges; a few non-public ranges
are **not yet blocked** and are treated as routable. If your threat model includes
them, supply a stricter `UrlPolicy::custom(...)`. Tracked in
[#21](https://github.com/2389-research/mux-rs/issues/21):

- **NAT64** `64:ff9b::/96` and **6to4** `2002::/16` — embed an IPv4 address a
  gateway can translate to reach an internal v4 host; the embedded address is not
  currently decoded.
- **IPv4 multicast** `224.0.0.0/4` and **reserved/class-E** `240.0.0.0/4`.
- **Deprecated IPv6 site-local** `fec0::/10` and **IPv6 documentation**
  `2001:db8::/32`.

There is also no overall deadline across the guarded redirect chain (up to 10
hops).

## 3. Vetoing `bash` (and other tools) — use `ApprovalHandler`

mux does **not** ship a `bash` jail, because the existing `ApprovalHandler` hook
(wired into the agent runner) already lets a consumer veto any tool call by
name and raw parameters before it executes:

```rust
use async_trait::async_trait;
use mux::permission::{ApprovalContext, ApprovalHandler};

struct DenyShell;

#[async_trait]
impl ApprovalHandler for DenyShell {
    async fn request_approval(
        &self,
        tool: &str,
        params: &serde_json::Value,
        _context: &ApprovalContext,
    ) -> anyhow::Result<bool> {
        if tool == "bash" {
            return Ok(false); // refuse all shell commands
        }
        Ok(true)
    }
}
```

The cleanest hardening is to simply **not register** `bash` in a confined
deployment. The filesystem jail's guarantees are only real once an
un-jailed shell is out of the model's reach.

## 4. FFI (Swift/Kotlin)

The filesystem jail reaches the FFI consumer through an additive constructor:

```swift
let engine = try MuxEngine.newConfined(dataDir: dataDir, root: workspaceRoot)
```

`new_confined` builds the filesystem built-ins rooted at `root`. `bash` is still
registered; drop it or sandbox it at the OS level for the jail to mean anything.
The `web_fetch` SSRF guard is a Rust-side construct (`web_fetch` is not an FFI
built-in this round).
