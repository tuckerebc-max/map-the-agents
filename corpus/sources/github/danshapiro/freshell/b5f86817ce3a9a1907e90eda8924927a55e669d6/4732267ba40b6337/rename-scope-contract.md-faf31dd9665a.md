# Rename Scope Contract (naming ownership)

Freshell shows several names for one underlying object. Since the unified
agent-names change, there are two regimes:

- **Coding-agent sessions (Claude, Codex, OpenCode — terminal CLI panes and
  fresh\* panes):** ONE durable saved name per session, shared by every
  surface. No other name scope exists for these sessions.
- **Everything else (shells, browsers, document viewers, editors, and
  coding providers outside those three, e.g. Kilroy, Gemini, Kimi,
  Amplifier):** the legacy four-scope model below, unchanged.

## The unified contract (scoped coding-agent sessions)

One Claude, Codex, or OpenCode conversation (a durable provider session,
plus its pre-durable pending identity before the first message
materializes one) has exactly ONE saved name. The pane header, the tab
(when the tab's naming source is that session), the sidebar row, the
history row, the terminal presentation, and every API projection display
that same record. Renaming from ANY of those surfaces — the pane-header
inline editor, the pane context menu, the tab editor, the sidebar menu,
the history editor (desktop or mobile), the Overview card, or the
`/api/session-names`, `/api/sessions/:key`, `/api/terminals/:id`,
`/api/panes/:id`, and `/api/tabs/:id` routes, the CLI `rename-pane` /
`rename-tab` verbs, or the MCP actions — writes the same record
everywhere. There are no separately targetable pane, tab, or terminal
aliases for these sessions, and no group name.

Name sources, in precedence order: an explicit user rename (`manual`),
a migration-protected legacy label (`legacy_protected` — historic origin
unknown, never claimed as human), Freshell's short AI-generated name
(`freshell_ai`), the provider's own AI-generated title (`provider_ai`),
the first message (`first_message`), and the working directory
(`directory`). An automatic offer can only raise rank; a manual name and
an accepted Freshell AI name are protected from late or stale automatic
answers. Automation (agent/API/CLI/MCP calls) defaults to an automatic
suggestion and can never acquire the permanence of a user's rename;
explicit `nameIntent: "user"` is the only automation path that does.

The user-facing control is **Rename** only. There is no "generate a new
name" action, no custom-label control, and no "reset to provider title"
for these sessions (a scoped null/blank rename is refused with
`NAME_RESET_UNSUPPORTED`). Freshell's own short-name generation is
activity-driven and server-side: it runs for UI-, CLI-, and API-created
sessions alike after the first accepted user message, with an immediate
fallback name and bounded retries (three attempts, then the series stays
exhausted). A provider-generated title is a fallback and never
suppresses Freshell's generation.

The name is assigned before the durable provider identity exists (a
pending handle), transfers to that identity atomically at
materialization, and survives refreshes, reconnects, reopening, resuming,
cross-browser use, and server restarts. A multi-session tab stores no
name of its own: it follows its original pane's session while that pane
exists, and a tab rename targets that session — not whichever pane last
had activity or focus.

### Native (provider) sync status and limitations

Accepted manual and Freshell AI names are written back to the provider's
own metadata (Claude custom title, Codex thread name, OpenCode session
title) through supported metadata APIs, with a finite per-revision cycle
budget (at most three write cycles per accepted name). A non-blocking
native sync status (`pending`, `synced`, `unsynced`, `unsupported`) may
be displayed beside the name; it is status data only and never a second
name authority.

Concrete, source-supported limitations:

- **No native human-intent provenance.** The public provider metadata
  cannot reliably distinguish a human rename from an automated one
  (Codex's automatic and human callers send the same request). Native
  observations are therefore always automatic; only Freshell's Rename
  UI or an explicit `nameIntent: "user"` API/CLI/MCP call marks a name
  as human.
- **Finite unsynced recovery.** If a writeback result is ambiguous
  (timeout, restart mid-write), the status stays `unsynced` with the
  reason even after a matching readback, and repair stops once the
  cycle budget is exhausted for that revision. A new accepted name
  decision starts a new bounded series; repeated events never
  replenish one.
- **Serial generation queuing.** Generation and native writeback share
  one serial background worker; a burst of eligible sessions is served
  earliest-due-first, so completion is bounded, not instantaneous.
- **Live redraw is not guaranteed.** An already-running external CLI may
  not redraw an externally changed name promptly; the saved name in
  Freshell still converges everywhere. Native TUI redraw is not
  measured by Freshell.

### Migration and recovery

Pre-existing conflicting saved names (old pane/tab/terminal/session
labels) were consolidated once at boot into the unified record:
reliable explicit-rename recency decided between proven user names, a
deterministic precedence order decided everything else, and the losing
raw evidence was retained in immutable recovery copies under
`<data dir>/name-migration-v1/` without keeping competing overrides
active. Post-migration, the old ladder fields are no longer consulted
for these sessions.

Recovery procedure (documented, the only supported path): read the
immutable evidence in `name-migration-v1/`, then — if a name was lost —
submit a deliberate rename through the normal Rename UI or API. Never
copy a backup over the live name document, never re-introduce old
override rows, and never reactivate competing aliases; a pre-feature
binary rollback requires an approved stopped-scratch restore from the
full config backup.

## The legacy four-scope model (everything else)

Each non-agent name has exactly one owner and each rename surface writes
exactly one scope:

| Scope | Owned by | Written by | Persists |
| --- | --- | --- | --- |
| Pane label | the pane (layout snapshot) | pane header inline rename; `PATCH /api/panes/:id` (agent API / MCP) | layout snapshot only |
| Tab label | the tab (layout organization) | TabBar inline rename; `PATCH /api/tabs/:id`; `name` on a REST/MCP tab create (agent API / MCP) | layout snapshot only |
| Terminal title | the terminal process | `PATCH /api/terminals/:id` (Overview card / terminal context menu) | `terminalOverrides[terminalId]` |
| Session title | the durable provider session | `PATCH /api/sessions/:key` (sidebar/history "Rename") | `sessionOverrides["provider:sessionId"]` |

Hard rules (legacy scopes, unchanged — a request naming a scoped
Claude/Codex/OpenCode target instead routes to the unified authority
above):

1. **Pane/tab renames never write terminal or session overrides.** The
   client `applyPaneRename`/`applyTabRename` thunks are Redux-only; the
   agent-API `PATCH /api/panes/:id` writes the layout store and
   broadcasts `ui.command{pane.rename}` with NO other side effect;
   nothing else PATCHes on a local rename. A stopped/exited pane with a
   retained `sessionRef` obeys the same rule — there is no
   "sessionRef fallback" write.
2. **`PATCH /api/sessions/:key` is the ONLY durable session-rename
   surface.** A non-empty `titleOverride` writes
   `{titleOverride, titleSource:"user"}` and cascades to the LIVE
   terminal running that session (terminal override + registry +
   `terminals.changed` + `cascadedTerminalId` in the response, then
   `sessions.changed`). `{"titleOverride": null}` REMOVES both
   `titleOverride` and `titleSource`. (For a scoped provider this route
   becomes a unified-authority rename; the null/reset form is refused —
   see above.)
3. **Terminal renames are terminal-scoped** and never cascade into
   session overrides (live OR retired identities). (A rename through a
   scoped session's terminal presentation is a unified-authority
   rename of that session's one name.)
4. **Reset to provider title** (sidebar/history context menu, shown when
   the directory row reports `titleOverridden` and the override's source
   is not a sweep rung (`first-message`/`dir` — those would be
   re-applied instantly)): previews current vs provider-native title,
   then issues `{titleOverride: null}`. Reset does NOT rewrite any open
   terminal/pane title — those surfaces are their own scopes. (The
   control does not exist for scoped sessions; their name is never
   cleared.)
5. **Provider-title updates and the auto-title sweep never flip a
   `user`-rung override**, and pane/tab labels can no longer mint one —
   so provider titles update in history exactly until a user makes an
   explicit session rename.
6. **No title-equality inference, ever.** Identity is
   `provider + sessionId`; two same-titled rows are two sessions. No
   dedup, group, or cleanup infers sameness from equal titles.
7. **No mass migration of existing overrides.** The unified consolidation
   above covers the three scoped providers; every other provider's rows
   are untouched. The `titleSource` ladder (`shared/title-source.ts`)
   still governs automatic writers in the legacy scopes, and the
   one-generation `config.backup.json` (refreshed on every persist)
   remains their recoverable path.

## Display precedence (composition of stored labels)

The rules above govern WRITE scoping (who owns which rename surface). This
section records how the DISPLAY composes the several labels one tab or row can
hold at read time — exactly as the code composes them. The "Persists" column
above is untouched by this section. For a scoped coding-agent session every
surface displays the ONE canonical name from the unified contract above; this
section composes the legacy scopes.

**Tab display title** (enforced by `getTabDisplayTitle`, `src/lib/tab-title.ts`;
a session-owned tab displays its source pane's canonical session name through
`selectTabDisplayTitles` instead):

1. **Explicit title** — `tab.title` with `titleSetByUser: true`: a TabBar
   inline rename, a `PATCH /api/tabs/:id`, or an explicit non-empty `name` on a
   REST/MCP tab create (the `tab.create` fold sets the user flag for
   caller-provided names). An empty explicit title falls through.
2. **Single-pane override** — the sole leaf pane's stored non-derived pane
   title, whatever composed it (see the pane ladder below — a registry
   auto-title like "Codex CLI" or a mirrored session title can show as the
   tab title when no explicit title outranks it).
3. **Stored non-derived `tab.title`** set without the user flag (create-time
   mode labels like "Amplifier").
4. **cwd-leaf derived titles** — the `deriveTabName`/`derivePaneTitle`
   fallbacks.

**Pane title** — composed per pane kind (NOT a blanket mirror-over-auto rule;
enforced by the terminal-title cache plus `sessionTitleMirrorMiddleware`,
`src/store/sessionTitleMirror.ts`):

- A **user-set pane title** is never mirrored over.
- **Terminal panes**: a cached terminal-level title outranks the session-title
  mirror — the mirror skips any terminal pane whose `terminalId` has a cached
  title (`collectSessionTitleTargets`, `sessionTitleMirror.ts`), so registry
  auto-titles ("Codex CLI"), `PATCH /api/terminals/:id` renames, and the
  inventory/live folds own that pane; the mirror only titles terminal panes
  with NO cached terminal title (unattached/exited/not-yet-reattached panes).
- **Fresh-agent panes**: no registry pipeline — the session-title mirror is
  their runtime title source (always eligible).
- Fallback: the `initLayout`-derived cwd-leaf.

**Title-less running session rows** (a real session whose transcript has not
yet yielded a title): the sidebar row's label composes the same name order the
client-side fallback row uses — pane title, then the terminal's registry
title, then the provider label (`src/store/selectors/sidebarSelectors.ts`);
every other title-less row keeps the id-prefix fallback. The label is a
display fallback only — `hasTitle` stays false, and a later title-carrying
fetch still overrides it. For a scoped coding-agent row the canonical session
name (live cache, then the row's last-known projection) outranks this
composition; the running-row rungs below it keep a pre-transcript scoped row's
label stable.
