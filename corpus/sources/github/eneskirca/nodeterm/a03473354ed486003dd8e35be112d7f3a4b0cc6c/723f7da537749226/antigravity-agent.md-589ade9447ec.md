# Antigravity (`agy`) as a nodeterm agent

Google's Antigravity CLI (`agy`, measured on **1.2.3**, Windows 11; the **1.2.12** Linux binary and
the hook reference embedded in it were read on 2026-09-28) is a builtin agent id — and, since Google
stopped serving Gemini CLI to personal accounts on 2026-06-18, the replacement for the `gemini` agent
for most users (`docs/gemini-agent.md`):
`AGENT_CONFIG.antigravity` in `src/shared/agents/config.ts` — label `Antigravity`, colour `#00a3a3`
(provisional), `launchCmd: 'agy'`, `expectedProcess: 'agy'`, `promptInjectionMode:
'flag-interactive'` with **`promptFlag: '--prompt-interactive'`**. It is a member of exactly ONE
capability lists, `AGENT_HOOK_TARGETS` — the RUNNING / NEEDS YOU badge, the unread dot, completion
notifications, `--after` dependencies and trigger targets — and `RESUMABLE_AGENTS`: a cold restore
relaunches `agy --conversation=<id>` (the spelling agy prints in its own exit hint), where the id is
the hook payload's `conversationId`. A dead id is the safe failure: agy logs "Conversation %s not
found, ignoring --conversation flag" and starts fresh (1.2.12 binary). Everything else is a leaf that
does not exist yet (§7).

Launch reachability uses the same vendor-location lookup as hook installation. The measured agy
1.2.7 installer on Windows wrote `%LOCALAPPDATA%\agy\bin` into the user PATH as `REG_SZ`; Windows
kept the percent expression literal, so `where agy` failed while the executable at that location ran
normally. A local Antigravity PTY therefore APPENDS the detected executable's directory to its own
PATH, and only when no entry already names it (`pathWithAgyDir`) — it used to prepend, which on
macOS/Linux moved a shared directory (`/usr/local/bin`, `~/.local/bin`) ahead of the user's own
tools. Plain terminals and SSH sessions remain untouched.

The brand mark is `src/renderer/assets/antigravity-color.svg` (Google's multi-colour arch, from
`@lobehub/icons-static-svg` 1.95.1, MIT) in `AGENT_LOGO` (`lib/brandPulse.ts`): `AgentIcon` draws it
in every menu, header and card, and `brandPulsePlan` makes it the pulsing RUNNING indicator on the
canvas and in the notch HUD.

> Sibling documents: `docs/grok-agent.md`, `docs/gemini-agent.md`, `docs/copilot-agent.md`. The
> distilled rules are **Adding a new agent** in `CLAUDE.md`.

> **Where the facts come from.** Everything marked *measured* was run against the real `agy` 1.2.3
> on Windows 11, in a temporary HOME, or measured on that machine with the code in this change.
> Everything else is in §8, the device checklist. POSIX (mac/Linux) has NOT been run against a real,
> logged-in `agy`: the generated command and script were run the way agy documents it (`sh -c`, cwd =
> the hooks.json directory, fixture payloads on stdin) under dash and bash-posix, and the 1.2.12
> Linux binary was seen to LOAD our hooks.json (`hooks_manager.go: loaded 1 named hooks`), but no
> hook fired — that needs a signed-in account.

---

## 1. The one fact that shapes everything: a hook is a synchronous gate

`agy` reads its global hooks from **`~/.gemini/config/hooks.json`** (its bundled `hooks.md`). Hooks
run **synchronously**, block the agent loop, and their **stdout is read as a decision**. nodeterm
subscribes to `PreToolUse`, so our hook stands in front of **every tool call of every `agy` on the
machine — inside nodeterm and outside it**. A wrong byte there denies tools everywhere.

### 1.1 What `PreToolUse` stdout does (measured, 1.2.3)

| hook stdout | exit | result |
|---|---|---|
| nothing | 0 | tool **runs** |
| `{}` | 0 | **DENIED** (`tool call denied by pre-tool hook`) |
| `{"decision":""}` | 0 | **DENIED** |
| `{"decision":"ask"}` | 0 | runs under the user's normal policy (respects "always allow"; loses to `--dangerously-skip-permissions`) |
| `{"decision":"allow"}` | 0 | runs with no prompt |
| any non-JSON text | 0 | **DENIED** (protojson unmarshal error) |
| nothing | 1 | **DENIED** (`… returned exit status 1`) |

In 1.2.3 a silent `PreToolUse` executes; `{}`, `{"decision":""}`, non-JSON output and a non-zero
exit deny. A run with all five hooks silent behaved exactly like a run with no hooks.

### 1.2 What we answer — ONE table (`src/core/agents/hooks/antigravity-decision.ts`)

| event | stdout |
|---|---|
| `PreToolUse` | `{"decision":"ask"}` |
| `Stop` | `{"decision":""}` |
| `PreInvocation`, `PostInvocation`, `PostToolUse` | `{}` |
| unknown or empty | **nothing** |

Rules a change must keep:
- **Never `allow`** (it approves what the user did not) and **never `force_ask`** (per the vendor
  docs it re-opens the prompt ignoring the user's cache — not measured).
- **`Stop` must never print `"continue"`** — that keeps `agy` from stopping.
- **The default for an unknown event is silence, not `{}`.** If the event name were ever lost and
  the real event was `PreToolUse`, `{}` would deny the tool.
- **The table exists once.** The POSIX script, the POSIX command's missing-script fallback and the
  Windows wrapper's bail path all render from it. Two hand-written copies diverged within fifteen
  minutes during development.

### 1.3 Hook stdout is model input, not a log

`PreInvocation` accepts `injectSteps`, so anything we print can become a message in the user's
conversation, and any stray byte turns the answer into "non-JSON → DENY". The managed script prints
the answer FIRST — before the codex prelude, the `NODETERM_NODE_ID` gate, the stdin read and the
endpoint file — then runs `command exec >/dev/null 2>&1 || :`. `command` matters: a redirection
failure on a bare special builtin exits a POSIX shell non-zero, which is a DENY. `curl` output goes
to `/dev/null` for the same reason.

---

## 2. The event name is not in the payload

None of the five payloads carries its event name (measured), and `PreInvocation` /
`PostInvocation` have identical keys. So:

- the hooks.json command exports it as **`NODETERM_AGY_EVENT`** (POSIX) or passes it as the
  wrapper's first argument (Windows) — the argument survives `agy`'s dispatch (measured);
- the script POSTs it as the form field **`nodeterm_hook_event`**;
- `hook-server.ts` merges that field into the parsed payload **after** `JSON.parse`, like
  `nodeterm_pending_id` / `nodeterm_answered`, so a value planted in the agent's JSON never wins. The
  name is deliberately not `hook_event_name`, a real field for four other agents.

---

## 3. The state mapping (`normalizeAntigravity`, pure)

| event | state |
|---|---|
| `PreInvocation` | `working`; **`newTurn` only when `invocationNum === 0`** |
| `PreToolUse` with `toolCall.name === 'ask_question'` | `waiting` (NEEDS YOU) |
| other `PreToolUse` | `working` |
| `PostToolUse` of `ask_question` | `working` |
| other `PostToolUse` | nothing |
| `Stop`, `fullyIdle === false` | `working` (not terminal) |
| `Stop`, otherwise | `done`; `errored` only for `terminationReason === 'ERROR'` |
| anything else | nothing |

Why each one:
- **`fullyIdle` is the "really finished" bit** (measured with a background tool: a
  `Stop fullyIdle:false` at the end of the model's turn, the tool's `PostToolUse` 27.5 s later, then a
  `Stop fullyIdle:true`). Strict `=== false`: a payload without the field reads as finished. With this
  rule the late `PostToolUse` is simply the tool's real end.
- **`terminationReason` is UPPER_SNAKE** — a closed enum of 12 read from the binary (`ERROR`,
  `NO_TOOL_CALL`, `TERMINAL_CUSTOM_HOOK`, `USER_CANCELED`, `MAX_*`…). The bundled docs' lowercase
  example is wrong. Only `ERROR` sets `errored`; the others are unhappy ends, not API errors.
- **`newTurn` on `invocationNum === 0`.** `PreInvocation` fires per model call, but `agy` numbers the
  calls of one execution from 0, and every measured execution starts at 0 — including the one that
  resumes after a background tool. A turn boundary is load-bearing: `lastTurnError` (#521) is retired
  only by `newTurn`, so without it one errored turn held every `--after` dependent QUEUED for the rest
  of the app run; and the done-holdoff drops a non-`newTurn` `working` within 3 s of a `done`.
  `newTurn`'s other effects (fan-out clears, the prompt line) have nothing to act on for `agy`.
  Consequence worth knowing: the resume after a background tool also starts at 0, so it retires a
  `lastTurnError` with no new user prompt — correct in practice, since that resumed execution is a
  new turn, and one that finishes cleanly is a successful one.
- **NEEDS YOU is a closed set of one.** The step-type enum in the binary has `ASK_QUESTION` and no
  `ASK_PERMISSION`, so there is no `ask_permission` tool to match. Measured: 63 s
  between the question's `PreToolUse` and `PostToolUse` while it sat on screen.

### 3.1 Limits of that mapping

- **`agy`'s own permission prompt fires no hook.** A session parked on "Run this command?" shows
  RUNNING, indistinguishable from a slow tool. This is a CLI limit; do not try to guess.
- **ESC fires no `Stop`** (measured: the last event is `PreInvocation`, and nothing follows). A
  cancelled turn leaves the node on RUNNING. `agy` has no SessionEnd, so the DROPPED chip does not
  apply (`antigravity` is not in `SESSION_END_CAPABLE`). `--print-timeout` expiring behaves the same.
- **NEEDS YOU can be cleared early.** The normalizer has no state, so it does not correlate
  `PreToolUse`/`PostToolUse` by `stepIdx`; only the question's own `PostToolUse` closes it, and a
  background tool's `PostToolUse` is ignored. But any OTHER `working` event arriving while the
  question is open — a parallel tool's `PreToolUse`, a `PreInvocation`, a `Stop fullyIdle:false` —
  would clear it. None of those was observed during an open question; not measured either way. ESC
  during a question leaves NEEDS YOU until the next `PreInvocation`.

---

## 4. The hooks.json we write (`src/core/agents/hooks/antigravity.ts`)

- **Only where `agy` is installed.** Before anything else, the installer looks for `agy`: the
  PATH (with PATHEXT on Windows, through the shared `findExecutableSync`), then the vendor's own
  install locations — `~/.local/bin/agy` on macOS/Linux and `%LOCALAPPDATA%\agy\bin\agy.exe` on
  Windows (antigravity.google/docs/cli/install). It is a file lookup, never a spawn.
- **The snap is NOT the vendor's, and it cannot see our hook.** On Ubuntu, typing `agy` without it
  installed answers `snap install antigravity-cli` (measured 2026-09-28). That snap is a community
  wrapper (`snap info antigravity-cli`: "This is not an official Google product") and strictly
  confined, so its `$HOME` is `~/snap/antigravity-cli/current` and the hooks.json it reads is not
  the `~/.gemini/config/hooks.json` we write — the codex snap trap again. The failure is the SAFE
  one (the hook cannot gate anything it is never shown, so no tool is denied), but every badge on
  such a node stays dark. Recommend the vendor installer
  (`curl -fsSL https://antigravity.google/cli/install.sh | bash`, which verifies a sha512 from the
  vendor manifest and writes `~/.local/bin/agy`).
- **Two passes per launch** (`installAntigravityHooksWithProbe`, desktop and Server Edition). At
  boot the lookup may only see the PATH the process inherited — a GUI app on macOS/Linux starts with
  a minimal one — so the **boot pass** installs if it finds `agy` and otherwise does nothing at all.
  Once the login-shell PATH probe (`resolveShellPath`) has settled — or failed, leaving the
  inherited PATH — a **final pass** repeats the lookup, only if the boot pass found nothing: found ⇒
  install; not found ⇒ withdraw a bundle of ours. A bundle is therefore never withdrawn on the
  strength of the boot pass alone. On Windows the probe answers at once and the inherited PATH is
  already the user's, so the final pass just repeats the same lookup. Both passes write to the paths
  resolved before the first one. An `agy` installed later gets the hook the next time nodeterm
  opens.
- **The opt-out is agy's own switch.** `"enabled": false` on the `nodeterm-status` bundle turns the
  whole gate off, and the installer carries it across every rewrite (the handlers are still
  refreshed, so switching it back on gets the current commands). Only a literal `false` counts.
- **Published through the shared settings transaction** (`updateSettingsFile`, #851): a symlinked
  hooks.json (dotfiles) keeps its link and the target is updated, the file's mode is kept, our writers
  serialize behind a lock, and a file that changed while the update was computed (agy's own `/hooks`
  editor writes it too) is not overwritten.
- **One bundle, `nodeterm-status`**, rewritten whole on every install (collapses duplicates, #558).
  Every other top-level key is kept as is; an entry of ours found in another bundle is swept out
  (matched through `normalizeHookCommand`, both leaves on every platform, and ANCHORED on
  `.nodeterm/agent-hooks/` — a user's own gate at `~/work/agent-hooks/antigravity.sh` is not ours).
- **Two shapes**: `PreToolUse`/`PostToolUse` are grouped (`[{ "matcher": "*", "hooks": [...] }]`),
  `PreInvocation`/`Stop` are flat handler lists. `"*"` is the matcher the measurement ran with.
  `PostInvocation` is not subscribed.
- **`"timeout": 5`** on every handler (`agy`'s default is 30 s).
- A hooks.json we cannot parse, or whose top level is not an object, is **left untouched** and the
  install is skipped (the codex precedent).
- **Never** `~/.gemini/settings.json` (the Gemini CLI's; `agy` does not read hooks from it —
  measured, so there is no cross-fire) and never `~/.gemini/GEMINI.md`.
- Paths resolve through `os.homedir()` via the DEFAULT import, so a test that spies it redirects the
  whole install. The installer-registry test (`hooks/index.test.ts`) calls it with its defaults.

### 4.1 POSIX command

```
NODETERM_AGY_EVENT='Stop'; export NODETERM_AGY_EVENT; if [ -r '<script>' ]; then sh '<script>' || :; else printf '%s\n' '{"decision":""}'; cat >/dev/null 2>&1 || :; fi
```

The missing-script branch answers from the same table and drains stdin. `|| :` forces exit 0 like
the Windows wrapper's `exit /b 0`: the script answers FIRST and sources the endpoint file after, so a
syntax error there used to leak out as status 2 beside a valid answer — a pair agy was never
measured on (silence + exit 1 is a measured DENY). `agy` documents `sh -c` on Unix, cwd = the
directory holding hooks.json, `~` expanded (1.2.12's embedded hooks.md). Run that way under dash and
bash-posix against a fake/unreachable/blackholed endpoint, a missing or unreadable script, empty or
200 KB stdin, no curl, an unwritable TMPDIR and a HOME with a space: every PreToolUse printed exactly
`{"decision":"ask"}` and exited 0. Not yet run under a logged-in agy.

### 4.2 Windows command — no quotes, relative, guarded

```
if exist ..\..\.nodeterm\agent-hooks\antigravity-hook.cmd (call ..\..\.nodeterm\agent-hooks\antigravity-hook.cmd Stop) & exit 0
```

Each piece is a measured failure of the alternative:

- **No quotes.** `agy` (a Go binary) passes the command to `cmd /c` as ONE argument escaped the
  MSVCRT way — inner `"` become `\"`, which cmd.exe does not understand. The codex form
  (`cmd.exe /d /c call "<wrapper> " Event`) failed with exit 1 under the real `agy`, **denying every
  tool**. Node's default (non-verbatim) `spawn` escapes the same way and reproduces it byte for byte;
  a test with `windowsVerbatimArguments: true` passes while the real `agy` fails.
- **Relative.** Without quotes an absolute path breaks at the space in `C:\Users\John Doe`. The hook's
  cwd is the directory holding hooks.json (vendor-documented, and measured: every event reported
  `cwd=…/.gemini/config`), so `..\..\.nodeterm\agent-hooks` reaches our wrapper with no profile name in
  the string. The installer computes it from the two paths and **refuses to install** when the result
  would need quoting (another drive, a space in between). **If a future `agy` changes the hook cwd**,
  the guard finds nothing and the command falls silent: tools keep running, only the badge goes dark.
- **Guarded.** A missing target makes cmd print "is not recognized" and exit 1 — measured as a DENY
  of every tool. `if exist … & exit 0` turns "nodeterm is gone" into silence + exit 0 (measured: the
  tool ran).
- **One wrapper, the event as its argument** (`antigravity-hook.cmd`): exports
  `NODETERM_AGY_EVENT=%~1`, `DisableDelayedExpansion` (`!` is legal in a path), finds Git Bash with
  the codex wrapper's search, runs the same `antigravity.sh`, answers from the table when there is no
  shell or no script, drains stdin, always `exit /b 0`. Never PowerShell (~4× the start cost).

### 4.3 AutoRun: the installer refuses

`agy` runs `cmd /c` **without `/d`**, so cmd.exe first runs the registry `AutoRun` command (`cmd /?`).
Anything it prints lands ahead of our answer → non-JSON → DENY; a silent `cd` moves the cwd the
relative command depends on. So, on Windows and **before writing anything**, the installer reads
the three values cmd.exe consults with `reg query` (`antigravity-autorun.ts`):

- `HKEY_CURRENT_USER\Software\Microsoft\Command Processor\AutoRun`
- `HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\AutoRun`
- `HKEY_LOCAL_MACHINE\Software\WOW6432Node\Microsoft\Command Processor\AutoRun`

Any non-empty value ⇒ **nothing is installed, and a `nodeterm-status` bundle an earlier launch wrote
is withdrawn** (the installer runs at every launch; an AutoRun that appeared later would otherwise
keep denying tools through the old bundle). An unreadable registry ⇒ the same: not installing costs
the badge, installing wrongly costs every tool call, and removing our bundle can never deny one.
The same withdrawal happens when the layout admits no quote-free command. Foreign keys are kept,
an unparseable hooks.json is left alone, and a file with nothing of ours is not rewritten.

How it reads: `reg.exe` by absolute path under `%SystemRoot%` (or `%windir%`) — with neither set it
does not run at all and the answer is "unreadable". HKLM queries carry `/reg:64`, so a 32-bit
process still sees the 64-bit view agy's cmd.exe uses (answers were identical with and without the
switch on the 64-bit machine it was checked on). `reg` answers exit 1 with a localized message both
for a missing key (the HKCU key is usually missing) and for a failure, so absence is decided by
listing the PARENT key, never by reading the error.

**Where the user sees it:** only in the app's log (`[agent-hooks] antigravity install skipped: …`).
The line is written after the withdrawal and says what really happened: withdrawn, nothing to
withdraw, file left untouched (not JSON), or — if the write failed — that the bundle is STILL ACTIVE
and must be removed by hand.
There is no UI surface. **To enable Antigravity status**, remove (or empty) the `AutoRun` value and
restart nodeterm.

The effect of a real AutoRun on `agy` has not been reproduced (it would mean writing the registry).

---

## 5. Cost

Measured on Windows 11 (20 runs, dispatched as `agy` does):

| case | answer on stdout | process exit (what `agy` waits for) |
|---|---|---|
| inside a nodeterm node | ~100 ms | **~520 ms** |
| plain terminal (no `NODETERM_NODE_ID`) | ~95 ms | **~155 ms** |

A tool step fires three of the four subscribed events, so ~1.6 s of hook per step inside nodeterm
on Windows. The time goes to Git Bash forks (~55 ms each) for the token read, the temp file and the
path conversion before the POST is backgrounded. Accepted for now; trimming those forks is a
Windows follow-up.

On POSIX the POST already runs in the background: the part agy waits for measured **2–40 ms** (dash
and bash-posix). It matters that it stays that way — a foreground POST against an endpoint that
accepts and never answers, plus the bounded failover walk, measured **~6 s**, past our 5 s handler
timeout, on every tool call. `antigravity-script.test.ts` pins it with a curl that stalls for 6 s.

---

## 6. The three surfaces

- **Desktop**: full. The target of the MVP is Windows.
- **Server Edition**: by construction — the normalizer is `src/shared`, the field merge and the
  installer are `src/core`, and `installManagedAgentHooks` runs in both shells. Neither raw hook
  listener has an antigravity branch (both read `transcript_path`, which `agy` spells
  `transcriptPath`), so there is nothing to keep in parity.
- **Mobile**: N/A — the status mirror is agent-agnostic, so the state reaches the phone as is. The
  phone cannot launch an Antigravity node, and its hand-copied brand colours do not know this one
  (follow-up for @eneskirca once the colour is final).
- **Kanban**: nothing of its own; the card and modal read the same status.

---

## 7. Out of scope, and why

| not here | why |
|---|---|
| In-place restart / Eco | `/exit` and `/quit` are documented (1.2.12), but `ask_question` maps to `waiting`, which the restart's busy gate does not refuse — an `/exit` would be typed into an open question. Map it to `blocked` (or treat `waiting` as busy for agy) and check on a device that the pane returns to a shell (agy runs sidecar processes) before adding `EXIT_SEQUENCES.antigravity` |
| Permission modes | flags exist (`--mode accept-edits\|plan`, `--dangerously-skip-permissions`) but there is no row in `approval-mode.ts`. Until there is, nodes run under `agy`'s default policy — so its permission prompt (which fires no hook, §3.1) is what a node shows as RUNNING |
| Context meter | no token count or window in hooks or transcript (the TUI's "1.1k tokens" is per thought block) |
| Chat panel (⌘M, and the phone's Chat screen), context link, transfer | the transcript's LOCATION is measured, its record shapes are not. See §7.1 |
| Canvas control | the shim and the discovery file already exist — `agy` reads `~/.gemini/GEMINI.md` (measured), where the Gemini CLI's nodeterm blocks are — but antigravity is not in `CANVAS_CONTROL_CAPABLE`, so the session gets no `NODETERM_CANVAS_CONTROL` and the shim answers "not a nodeterm agent node". Joining is the follow-up; check what else that list gates first |
| Subagent cards | `invoke_subagent` exists in the step enum; never provoked |
| Session name, rename | title lives in SQLite (not measured); no rename command |
| SSH projects | no remote installer yet (it would write the POSIX form over the ControlMaster). `LOCAL_ONLY_HOOK_AGENTS` / `hasHooksOverSsh` make `--after` refuse an agy dependency there; a trigger aimed at one queues until its (never-coming) `done`, visibly on the trigger card |

Also worth knowing: `agy` asks "Do you trust the contents of this project?" the first time it opens a
folder, before any turn.

### 7.1 The chat view: what is known, and why nothing ships yet

`antigravity` is deliberately NOT in `CHAT_CAPABLE` (pinned in `config.capabilities.test.ts`). On
an agy node, ⌘M therefore opens the rendered terminal OUTPUT (`TerminalMarkdownView`), never the
conversation view, and the phone's Chat screen answers `unsupported` (its relay `page()` is gated on
`canChat`). That is the honest answer until the record shapes below are captured. A parser written from the vendor's prose would map the user's and the
model's text and then have to guess everything else, which is rule 14 of "Adding a new agent" in
`CLAUDE.md`: a guess must degrade to nothing, never to something wrong. An unwired skeleton is not
shipped either, because a module whose only reader is its own test is a plan, not a feature.

**Measured** (1.2.3, Windows; the hook payloads in
`src/shared/agents/__fixtures__/antigravity/hook-payloads.json`):
- **Location.** Every payload names `transcriptPath` =
  `<agy home>/brain/<conversationId>/.system_generated/logs/transcript_full.jsonl`, next to
  `artifactDirectoryPath` = `<agy home>/brain/<conversationId>`, with `<agy home>` =
  `~/.gemini/antigravity-cli`. On Linux, the 1.2.12 binary created `~/.gemini/antigravity-cli/brain/`
  under a fresh HOME (2026-09-28). The directory stayed empty, because no turn runs without a
  sign-in.
- **Session id.** `normalizeAntigravity` already maps `conversationId` to the event's `sessionId`
  (the same id `agy --conversation=<id>` resumes), so a node's own id reaches `agentStatus`. The
  locator must key on that id and nothing else: `brain/` holds every conversation on the machine,
  so a "newest file" fallback would show a stranger's session.

**Vendor-described, never captured.** The 1.2.12 binary embeds instructions that tell its own model
how to read these files. They say:
- JSONL, one "step" (action) per line.
- `step_index` is the step's index in the trajectory.
- `source` is e.g. `USER_EXPLICIT`, `MODEL` or `SYSTEM`.
- `type`: `USER_INPUT` is the user's prompt, and `PLANNER_RESPONSE` is the agent's response and its
  tool calls.
- `status` is e.g. `DONE` or `ERROR`. `created_at` is an ISO 8601 timestamp.
- `content` is the text: the user's request, the model's response, or tool responses.
- `thinking` holds the reasoning (on `PLANNER_RESPONSE`), and `tool_calls` is "an array of tool calls
  … including their arguments".
- `media` is `[{mime_type, uri}]`; the bytes are not in the file.
- `truncated_fields` appears only in the compact `transcript.jsonl`, which truncates large
  `content`/`thinking`/`tool_calls`. It never appears in `transcript_full.jsonl`.

That settles which file to read (`transcript_full.jsonl`) and nothing more.

**Unknown, and each one is a guess that would render wrong:**
1. **The element shape of `tool_calls`**: the keys for the name, the arguments and any id, and
   whether the arguments are an object or a JSON string.
2. **How a tool's RESULT is recorded, and how it links to its call.** `content` "or tool responses"
   suggests a step of its own. The step-type enum in the binary has ~120 values (`RUN_COMMAND`,
   `VIEW_FILE`, `GREP_SEARCH`, `ASK_QUESTION`, `INVOKE_SUBAGENT`, `ERROR_MESSAGE`, `CHECKPOINT`, …),
   and nothing says which field points back at the call (`step_index`? an id?).
3. **The serialized spelling of the enums.** The vendor text writes `USER_INPUT`, the proto name is
   `CORTEX_STEP_TYPE_USER_INPUT`, and a parser matching the wrong one renders an empty thread.
4. **Whether a `USER_INPUT` `content` is exactly what the person typed**, or is wrapped in injected
   tags or metadata. Tooling text must never appear in the shape of something the human said.
5. **Whether the file is append-only.** The status enum also has `RUNNING`, `GENERATING`,
   `WAITING`, `PENDING` and `QUEUED`. If a step's line is rewritten when its status changes, byte
   offsets are not stable keys. The paged read (claude's) would then be wrong, and the single capped
   whole-file read (grok's) is the only safe shape. **This one decides the paging design.**
6. **The model name.** It is not a documented step field. The hook payload's `modelName` exists, but
   the chat reader reads the file.
7. **What an ESC-cancelled turn, an errored tool, a compaction/summary and an `invoke_subagent` child
   write**, and whether a child's steps land in the parent's file.

**Remote nodes.** There is no SSH hook installer for agy (§7, SSH projects). A remote agy node never
reports a `conversationId`, so there is nothing to locate on the host. When this lands, a remote node
must answer `remoteOnly` → unreadable, like grok, and never read this machine's `brain/`.

The capture that unblocks all of it is §8.1 (items 17–24), with `scripts/agy-transcript-shape.mjs`.

---

## 8. Device checklist — what is NOT verified

1. **`terminationReason: 'ERROR'`** never produced (bad model name exits before any hook; a timeout
   emits no `Stop`; a failing tool is not a turn error). Whether `Stop.error` carries text is unknown.
2. **POSIX** (mac/Linux) under a real, signed-in `agy`: the command and script ran under dash and
   bash-posix the way agy documents dispatch, and 1.2.12 loaded our hooks.json, but no hook has fired
   (macOS `/bin/sh` is bash 3.2, approximated with bash 5.2 in posix mode).
3. **`--mode accept-edits` with an edit tool** and our `ask` answer.
4. **`force_ask`** never emitted; its behaviour is the vendor's description.
5. **`invocationNum`** restarting at 0 inside one turn in other scenarios (`force_continue`,
   `MAX_*`, hook-terminated runs). Measured only for execution start and the resume after a
   background tool.
6. **A real `AutoRun`** affecting `agy` (§4.3) — hypothesis from `cmd /?`.
7. **The 5 s timeout** — what `agy` does when a `PreToolUse` hook exceeds it (likely a deny).
8. **NEEDS YOU cleared early** by another `working` event during an open question (§3.1).
9. **`PostToolUse` after a `Stop fullyIdle:true`** — never seen in 17 runs; not proven impossible.
10. **The hooks.json in a workspace** (`<repo>/.agents/hooks.json`) and its precedence over the
    global one.
11. **A hook cwd other than the hooks.json directory** (§4.2) — the fallback is designed, not seen.
12. **Access-denied registry** for the AutoRun reader (falls to "unreadable"), and `/reg:64` on a
    32-bit Windows (an error there also falls to "unreadable" = no install).
13. **The `agy` lookup on macOS/Linux** (a GUI app's PATH, `~/.local/bin`) — only unit-tested with a
    fake home; on Windows the vendor path and the PATH both exist on the machine it was written on.
14. **Resume**: that the hook's `conversationId` is the id `agy --conversation=<id>` accepts, and that
    `invoke_subagent` children do not fire hooks under their OWN `conversationId` (if they do, the
    recorded id — and the node's `done` — would flip to the child).
15. **`Stop` → `{"decision":""}` on 1.2.12.** `StopResult.decision` is a proto enum there and the
    binary carries `unknown StopResult decision: %v`. Turns completed under it on 1.2.3; silence was
    measured safe for every event. Re-check on the current version.
16. **Whether agy waits on the hook's process GROUP or only the direct child and its pipes** — the
    backgrounded POST is safe only in the second case (a runner that waits on the child returned in
    12–16 ms while a 6 s walk was still running).

### 8.1 The chat-view capture (§7.1), items 17–24

One session answers all of them. Run it on a machine with the vendor-installed, signed-in `agy` (not
the snap, §4), in a throwaway workspace with a synthetic prompt, so the file holds no one's work.
The raw transcript stays on that machine. What leaves it is the output of
`scripts/agy-transcript-shape.mjs`, which prints keys, nesting, enum values and lengths, never the
text (review it before sharing: a key can itself be data). Commit only SYNTHETIC fixtures built
from that dump, never a slice of a real file.

```sh
mkdir -p /tmp/agy-cap && cd /tmp/agy-cap && git init -q && printf 'hello\n' > a.txt
agy --prompt-interactive 'Read a.txt, then run `echo hi`, then run `sleep 30` in the background, then ask me which of JSON or YAML I prefer, then answer in two paragraphs with a markdown list.'
# Answer the question. Before the background sleep finishes, in a second shell:
ID=$(ls -t ~/.gemini/antigravity-cli/brain | head -1)
L=~/.gemini/antigravity-cli/brain/$ID/.system_generated/logs
node scripts/agy-transcript-shape.mjs "$L/transcript_full.jsonl" --snapshot /tmp/agy-cap/snap.json
# After the final Stop (the sleep's PostToolUse, then Stop fullyIdle:true):
node scripts/agy-transcript-shape.mjs "$L/transcript_full.jsonl" --compare /tmp/agy-cap/snap.json
node scripts/agy-transcript-shape.mjs "$L/transcript_full.jsonl" > /tmp/agy-cap/full.shape
node scripts/agy-transcript-shape.mjs "$L/transcript.jsonl" > /tmp/agy-cap/compact.shape
```

On Windows, run the same from Git Bash, where `~` is `%USERPROFILE%`.

17. **Every record's shape** (`full.shape`): the key set per `type`, and which lines a turn writes.
18. **`tool_calls` elements** (the summary's `toolCallKeys`): the name/arguments/id keys, and
    whether the arguments are an object or a string.
19. **The tool result**: which line follows a `PLANNER_RESPONSE` with `tool_calls`, what its `type`
    and `source` are, and which field names the call it answers.
20. **Enum spelling** (the summary's `enums`): `USER_INPUT` or `CORTEX_STEP_TYPE_USER_INPUT`.
21. **`USER_INPUT` `content`**: compare its `<text:N>` length with the prompt you typed. A longer
    value means injected wrapping; read that one line locally to see the wrapper's shape.
22. **Append-only**: `--compare` must print `append-only` across the background tool's status change.
    `rewritten` means byte offsets are not stable keys, and the reader must be grok's single capped
    read (`olderCursor: null`), not claude's paged window.
23. **The model name**: which key, if any, carries it (`gemini-3.8-flash-high` in the hook payload).
24. **The failure paths**, one short extra session each, dumped the same way: ESC mid-turn, a
    command that fails, a pasted image (`media`), `/compact` or a long session, and an
    `invoke_subagent` child (does its step list land in the parent's file?). Also confirm that
    `compact.shape` carries `truncated_fields` and `full.shape` never does, and whether any
    environment variable relocates `~/.gemini/antigravity-cli` on macOS/Linux.
