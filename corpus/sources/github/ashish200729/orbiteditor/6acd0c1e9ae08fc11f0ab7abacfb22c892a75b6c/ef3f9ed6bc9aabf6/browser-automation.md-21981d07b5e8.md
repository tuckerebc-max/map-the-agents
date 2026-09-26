# Browser Automation (Built-in `orbit-ide-browser` MCP server)

Orbit ships a built-in MCP server, `orbit-ide-browser`, that gives agents
Cursor-parity control over the editor's integrated browser. Unlike an external
stdio MCP server, it runs in-process and talks directly to the Electron
`WebContentsView` that powers the simple browser, so there is no separate
Chrome instance to launch and no `npx` dependency.

## Cursor parity

The tool surface, argument shapes, and MCP instructions mirror Cursor's
`cursor-ide-browser` MCP server so that agent skills, playbooks, and prompts
transfer cleanly between the two. Specifically:

- The same 16 tool names are exposed with the same parameter names and
  descriptions (`browser_navigate`, `browser_snapshot`, `browser_click`,
  `browser_cdp`, …).
- The MCP instructions shipped to the model cover the same core workflow,
  lock/unlock ordering, waiting strategy, CDP usage, vision, and rabbit-hole
  avoidance guidance as `cursor-ide-browser`.
- The CDP security denylist matches: `Input.*`, cookie/storage exfiltration,
  permission grant, download, target management, and CDP navigation are denied.

Orbit extensions on top of the cursor parity baseline:

- `browser_hover` — an extra tool for tooltip/menu interactions.
- `browser_navigate` returns an interactive element list by default
  (`includeSnapshot` defaults true) so the common "open a page and type" goal
  finishes in 2 tool calls.
- `browser_type` / `browser_fill` self-focus and self-verify the typed text
  landed in the control (no silent no-ops on contenteditable composers).
- `browser_tabs` accepts `viewId` (a stable tab id) in addition to `index`.
- `browser_press_key` accepts `modifiers`; `browser_drag` accepts
  `intermediateRefs`.

## Enabling

Open **Settings → Browser Automation** and toggle it on (default: on). When
enabled, the server is advertised to every chat thread as an MCP server named
`orbit-ide-browser`, and a small globe badge appears in the chat input footer.

Disabling the toggle removes the server from the agent's tool list and frees
the CDP debugger sessions. The setting syncs to the main process live — no
restart required.

## Tools

The server exposes 17 tools: the 16 tools from Cursor's `cursor-ide-browser`
MCP server (so agent skills and playbooks transfer cleanly) plus one Orbit
superset tool, `browser_hover`. Refs are opaque strings returned by
`browser_snapshot` and are invalidated on every main-frame navigation, so the
agent must re-snapshot after any page mutation before clicking or typing again.

Argument shapes mirror `cursor-ide-browser`'s descriptors. Orbit keeps a few
superset parameters (called out below) and uses `viewId` (a stable tab id) as
the primary tab handle, with `index` accepted as a convenience for parity.

| Tool | Read-only | Description |
|------|-----------|-------------|
| `browser_navigate` | no | Navigate to a URL (reuses tab or opens a new one). Orbit extension: returns interactive refs by default (`includeSnapshot` defaults true). |
| `browser_tabs` | no | List / create / close / select a browser tab. Accepts `index` (cursor parity) or `viewId` (Orbit). Mutating actions (`new`/`close`/`select`) are not parallelized. |
| `browser_lock` | no | Lock or unlock the browser (pointer overlay + Take Control badge). |
| `browser_snapshot` | yes | Capture an accessibility tree with refs (preferred over screenshots). `interactive` defaults false (full tree); set true for a flat textbox-first list. |
| `browser_take_screenshot` | yes | Capture a screenshot as an image result. Supports `type` (png/jpeg), `fullPage`, `ref` (element clip), `filename`, `element`. |
| `browser_click` | no | Click an element by ref. |
| `browser_mouse_click_xy` | no | Click at absolute viewport coordinates. |
| `browser_type` | no | Type text into an element by ref (appends). Supports `clear`, `submit`, `slowly`. Self-focuses and self-verifies. |
| `browser_fill` | no | Clear and fill an element by ref (replace). Self-verifies. |
| `browser_select_option` | no | Select options in a `<select>` by ref. |
| `browser_press_key` | no | Press a keyboard key (Enter, PageDown, …). Orbit extension: `modifiers`. |
| `browser_scroll` | no | Scroll the page or scroll an element into view. Supports `direction`/`amount`, `deltaX`/`deltaY`, `scrollIntoView`, `ref`. |
| `browser_drag` | no | Drag from a source ref to a target ref or viewport coordinates (`targetX`/`targetY`). Orbit extension: `intermediateRefs`. |
| `browser_hover` | no | Hover an element by ref. **Orbit superset** — not in cursor-ide-browser. |
| `browser_highlight` | no | Highlight an element for visual grounding (injects a DOM overlay). Supports `element`, `durationMs`. |
| `browser_get_bounding_box` | yes | Get the bounding box of an element by ref. Supports `element`. |
| `browser_cdp` | no | Send a raw Chrome DevTools Protocol command (denylist enforced). |

### Read-only annotations and subagents

Each tool is annotated with `annotations.readOnly = true` when it cannot mutate
the page. Orbit's subagent policy uses this annotation to filter tools: a
read-only subagent (e.g. an `explore` agent) can call `browser_snapshot` and
`browser_take_screenshot` but not `browser_click` or `browser_type`. Mutating
tools are hidden from such subagents entirely.

### Approval

Mutating browser tools (`browser_click`, `browser_type`, `browser_cdp`, …)
follow the standard MCP tool approval flow — they prompt for permission unless
auto-approval is enabled for "MCP tools" in Settings.

`browser_lock` is exempt from approval because it is an internal coordination
tool: it only toggles whether user pointer events are blocked, and prompting
for it would be noise. It is **not** marked `readOnly` (it mutates lock state
and installs a page overlay), so it runs on the sequential path.

## `browser_cdp` security denylist

`browser_cdp` lets the agent run arbitrary CDP commands for inspection and
profiling, but a centralized denylist blocks anything that could exfiltrate
credentials, escape the tab, or bypass the dedicated interaction tools:

- `Input.*` — use `browser_click` / `browser_type` / `browser_press_key`
- `Network.getCookies`, `Network.getAllCookies`, `Storage.getCookies`,
  `Network.setCookie`, `Storage.setCookies`, `Network.clearBrowserCookies`,
  `Storage.clearCookies`, `Network.getResponseBody`, `Network.getRequestPostData`
  — no credential / response-body access
- `IndexedDB.*`, `CacheStorage.*` — no storage dumps
- `DOM.setFileInputFiles`, `Page.setInterceptFileChooserDialog` — no silent
  local-file upload
- `Browser.grantPermissions`, `Browser.resetPermissions`
- `Page.setDownloadBehavior` — no downloads
- `Page.navigate`, `Page.navigateToHistoryEntry` — use `browser_navigate`
- `Target.createTarget`, `Target.createBrowserContext`,
  `Target.disposeBrowserContext`, `Target.closeTarget`,
  `Target.attachToTarget`, `Target.detachFromTarget` — no target management
  (detach would kill our own debugger session)
- `Emulation.setDeviceMetricsOverride` — would break bounds synchronization

In addition, `Runtime.evaluate` / `Runtime.callFunctionOn` expressions that
reference `document.cookie`, `localStorage`, `sessionStorage`, or `indexedDB`
are denied as a best-effort guard against denylist bypass.

The denylist is defined in
`src/vs/platform/browserView/common/browserAutomationPure.ts` and covered by
contract tests in
`src/vs/workbench/contrib/orbit/test/common/browserAutomationPure.test.ts`.

## Screenshots

`browser_take_screenshot` is Retina-safe and production-hardened:

- **Viewport PNG (default)** — uses Electron's native `webContents.capturePage()`
  on the `WebContentsView` surface. This captures the correct DIP size with no
  CDP clip math, so HiDPI/Retina Macs do not produce the classic
  "content squeezed into the left half + white space on the right" artifact.
  Empty / zero-size native captures are rejected and fall back to CDP.
- **Full-page / element / JPEG** — uses CDP `Page.captureScreenshot` with a
  clip built from `cssContentSize` / `cssVisualViewport` / element bounds
  (CSS pixels). The deprecated device-pixel `contentSize` is never used as a
  CSS clip.
- Options: `type` (`png`/`jpeg`), `fullPage`, `ref` (element clip),
  `filename` (writes under `$TMPDIR/orbit-browser-automation/`), `element`
  (API parity with `cursor-ide-browser`).
- `take_screenshot_afterwards` on navigate/snapshot/click/type/etc. returns an
  **image** result that also carries the textual status/refs, so the model keeps
  actionable refs while vision models receive pixels.

Native capture also re-applies bounds and briefly reveals a hidden view so a
background tab still produces a real frame instead of a blank white rectangle.

## Large responses

Accessibility snapshots and CDP responses can exceed model context limits. The
server spills any response over 64 KB to a temp file under
`$TMPDIR/orbit-browser-automation/` and returns a summary plus the first 4 KB
to the model. The full payload is preserved on disk for inspection. Spill files
older than 24 hours are pruned, and the directory is capped at ~50 files.
Disabling Browser Automation deletes the spill directory.

## Architecture

```
                 ┌───────────────────────────────────────────────────┐
                 │ Electron main process                             │
                 │                                                   │
   agent tool ──►│  OrbitIdeBrowserMcpServer                         │
   callTool      │   ├── BrowserAutomationMainService (CDP, refs,    │
                 │   │   input dispatch, lock, buffers, spill files) │
                 │   └── BrowserViewMainService (WebContentsView)    │
                 │          ▲                                        │
                 │          │ open/select/close tab (sendWhenReady)  │
                 └──────────┼───────────────────────────────────────┘
                            │
                 ┌──────────┴───────────────────────────────────────┐
                 │ Renderer (workbench)                              │
                 │   BrowserTabRegistryService                       │
                 │     listens for orbit:browserAutomation:* IPC     │
                 │     and opens/selects/closes BrowserEditorInput   │
                 └───────────────────────────────────────────────────┘
```

Key files:

| Concern | Path |
|---------|------|
| Tool schemas + instructions | `src/vs/workbench/contrib/orbit/common/builtinMcp/orbitIdeBrowserMcpTypes.ts` |
| Pure helpers (CDP denylist, snapshot YAML) | `src/vs/platform/browserView/common/browserAutomationPure.ts` |
| Automation service contract | `src/vs/platform/browserView/common/browserAutomation.ts` |
| CDP / refs / input dispatch / spill files | `src/vs/platform/browserView/electron-main/browserAutomationMainService.ts` |
| Built-in MCP server (tool dispatch) | `src/vs/workbench/contrib/orbit/electron-main/builtinMcp/orbitIdeBrowserMcpServer.ts` |
| Built-in MCP registry | `src/vs/workbench/contrib/orbit/electron-main/builtinMcp/orbitBuiltinMcpRegistry.ts` |
| MCP channel wiring | `src/vs/workbench/contrib/orbit/electron-main/mcpChannel.ts` |
| Renderer tab registry | `src/vs/workbench/contrib/browserView/electron-sandbox/browserTabRegistryService.ts` |
| Settings toggle | `src/vs/workbench/contrib/orbit/common/orbitSettingsTypes.ts` (`browserAutomationEnabled`) |
| Prompt hint | `src/vs/workbench/contrib/orbit/common/prompt/prompts.ts` (`browserAutomationHint`) |
| Tool renderer (inline screenshots) | `src/vs/workbench/contrib/orbit/browser/react/src/sidebar-tsx/components/toolResults/BrowserMcpToolWrapper.tsx` |
| Status badge | `src/vs/workbench/contrib/orbit/browser/react/src/sidebar-tsx/components/chat/BrowserAutomationStatusBadge.tsx` |

## Input reliability (type / fill)

`browser_type` and `browser_fill` use a Playwright-aligned activation sequence
so text actually appears in the page (not just in the tool result):

1. Scroll the ref into view.
2. Focus the native `WebContents` and click the element (so React/controlled
   inputs enter edit mode — `focus()` alone is not enough).
3. Insert text via CDP `Input.insertText` (or per-key events when `slowly`).
4. For `<input>` / `<textarea>`, verify the value; if it did not update, force
   the native value setter + `InputEvent` (React-safe).
5. `browser_fill` clears via `element.select()` / platform select-all, never
   macOS-broken Home/End selection.

## Background vs visible tabs

- Omit `position` on `browser_navigate` / `browser_tabs` `new` to open a tab
  with `preserveFocus` so the user's current editor keeps keyboard focus. The
  browser tab still loads (native view is created) — do not use `inactive`,
  which would skip pane load and leave automation with no WebContents.
- Pass `position: "active"` or `"side"` when the agent should reveal the browser
  to the user.

## Opening the browser (approval)

When no browser tabs are open and the agent calls `browser_navigate` (or
`browser_tabs` `new`), Orbit shows a clean **Open browser** approval card with
the destination URL — even if "Always allow MCP tools" is enabled. Approving
opens the integrated browser and continues the agent turn. Once a tab exists,
subsequent navigate/click/type tools follow the normal MCP auto-approve setting.

## Background / inactive tabs

Every `BrowserEditorInput` eagerly gets a native `WebContentsView` (preloaded
hidden) so agents can drive inactive tabs without the user switching to each
one. `browser_navigate` also waits until the native view is registered before
snapshotting — fixing the race that produced `Error browser_navigate` /
"Browser view not found" right after open.

## Automation lock UX

When the agent calls `browser_lock`, Orbit:

1. Installs a full-viewport transparent pointer overlay in the page so the user
   cannot click while the agent works.
2. Shows a **Take Control** badge in the browser toolbar chrome. Clicking it
   unlocks the tab (removes the overlay) so the user can interact again.

Agent tools temporarily bypass the overlay for their own click/type/scroll/
drag sequences, then restore it. Keyboard is intentionally *not* swallowed
while locked — CDP agent input shares the same pipeline, and blocking it would
break `browser_type` / `browser_fill` mid-task.

## Golden path (few tools)

Simple goals should complete in **two** tool calls:

1. `browser_navigate { url }` — waits for load and returns a flat interactive
   element list (textboxes first), including DOM-augmented composers (ChatGPT).
   This is the Orbit extension that makes the golden path work: you do not need
   a separate `browser_snapshot` to get refs.
2. `browser_type { ref, text }` — focuses, types, and **verifies** the text.

Do **not** expect a separate `browser_snapshot`, `browser_mouse_click_xy`, or
screenshot just to type. Those are fallbacks when refs are missing or stale.

Note: `browser_snapshot` itself defaults to `interactive: false` (the full
accessibility tree), matching `cursor-ide-browser`. Pass `interactive: true`
when you only want a flat textbox-first ref list.

## Manual test plan

1. Toggle **Browser Automation** on; confirm the globe badge in chat footer.
2. New chat: `Open ChatGPT and type hi in the message box.`
   - Expect ~2 tools: `browser_navigate` then `browser_type` (not click_xy thrash).
   - Confirm **"hi" is visible** in the composer.
3. `Navigate to https://example.com` — confirm interactive refs in the navigate result.
4. Screenshot tool renders inline (not `[Image: image/png]`).
5. Lock → **Take Control** in browser toolbar unlocks.
6. Toggle Browser Automation off mid-session — tools disappear, badge gone.
7. Read-only subagent sees only read-only browser tools.
