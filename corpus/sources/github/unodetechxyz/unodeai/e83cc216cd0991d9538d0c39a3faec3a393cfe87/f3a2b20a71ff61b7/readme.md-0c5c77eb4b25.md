# UnodeAi Web Wiki

Version covered: UnodeAi 0.9.79

**Turn AI agents into an organized workforce.** A project manager agent breaks your goal into tasks and hands them to specialists, each with a role, its own skills, the model you chose, and only the permissions you granted. Where an objective check exists, UnodeAi records whether it ran and passed; where judgment is needed, a person records an explicit verdict. What an agent claims stays separate from what the framework observed.

## Codex Headless — Coming soon

Codex Headless is visible to show the planned third connection family, but it cannot be selected, configured,
made the default, or started in this release. `unode.codexCliPath` is reserved and no available route launches a
Codex CLI process. Existing saved Codex routes remain importable for migration, then are rejected by the host
before backend construction.

The planned cloud runner has separate effect-level safety gates. Do not configure a Codex CLI for UnodeAi
until that runner is released.

## How the team reports results and boundaries

**Shared team memory is context, not authority.** `memory_note` appends to `.unode/memory/notes.md` in the first
workspace folder and writes the host-selected routing tier plus an agent-selected semantic kind: `pitfall`,
`contract`, or `decision`. Once the mutable file is reloaded, all of those fields are recorded claims rather than
durable proof. Every prompt row is structurally encoded and labelled `untrusted` by default; count and byte bounds
remain in force, and a `contract` has no special trust or retention right.

Run **UnodeAi: Review Shared Memory** to inspect an exact row, then separately confirm or revoke a local
`human-attested` label. That host-owned record changes prompt admission/display only: it does not verify truth,
identify who clicked, or grant tools, folders, commands, network, MCP, delegation, hooks, completion, or evidence
authority. Editing one byte invalidates the match. New attestations are refused in an untrusted workspace, and
path resolution fails closed if the memory file or a parent link escapes the primary folder. There is no automatic
memory-to-rule or memory-to-skill promotion, and UnodeAi does not claim recalled notes are current or correct.

**One coordinator dispatches.** The first PM in a team roster is the single coordinator. Only it can dispatch,
collect, or inspect delegation handles. A worker can send the coordinator a normal message proposing work, but
the host does not parse that message and only validates the structured action the coordinator later chooses. This
removes worker fan-out for now; a future hierarchy must make every sub-coordinator's handles visible to its lead.

**Coordinator briefs get their own destination consent.** A coordinator may attach short, sourced orientation
to one assignment. It reaches the worker as a coordinator claim, never host evidence, and `basisRefs` must be
both declared in the contract and granted to that attempt; otherwise dispatch is refused before the worker
starts. A brief can paraphrase your documents and goes in the worker's prompt rather than through a read tool.
When its resolved model destination differs from the coordinator's, it is sent without a pop-up by default; turn
off **Allow cross-provider dispatch without approval** (Settings → More) to get a per-dispatch modal naming that
destination, where declining refuses the dispatch. The same destination never asks, and an unresolvable one is
refused. The setting is user-level only, so a workspace cannot change it. Briefs are retained
only in the internal run record and excluded from portable evidence and activity/conversation exports.

**The input-substitution rule follows the contract.** A task declaring at least one required input still tells
its worker to report a context gap rather than substitute web content. A task declaring none — including one
declaring only optional inputs — carries no substitution rule, because `optional` means the work can be
completed without that input; if a source must be consulted, declare it required. The card neither grants nor
removes web access.

**A denied request stays denied on its tool card.** Host tools carry `success`, `refused`, or `failed` from
the decision point, and a refusal carries a closed capability, scope, trust, or consent reason. The UI does not
re-read English result text to guess whether permission was granted. MCP and subprocess text is marked as
external instead of being treated as a host-authored decision.

**A refusal can explain the safe next step without widening it.** A reviewed host-authored literal may follow
the same bounded refusal reason, but no path, credential, command, destination, or a person's free-form web
denial reason reaches the model. On OpenAI-compatible connections, task-only artifact and context-gap tools
are offered only for a live contracted attempt; a stale direct request still reaches the handler for its
accurate refusal. Claude's connection-time tool schema stays unchanged.

**The dashboard and stream keep their meaning while they update.** Dashboard status colours use VS Code theme
tokens, and every one carries a fallback, so a theme that defines none of a token changes a dot's colour rather
than erasing it. **Done is blue rather than green**: measured in all four bundled themes, the previous green
fell below the contrast floor on the default light theme and sat almost on top of the green *working* dot in
both dark themes. Verification chips are outlined instead of filled, which keeps their text readable while
giving the two neutral states a visible shape they did not have in three of the four themes. A growing streamed
paragraph keeps its DOM node across paced paints — including one carrying bold, inline code or a link, whose
already-rendered parts are untouched as the text grows — preserving a selection in that paragraph; a paragraph
whose tail is genuinely re-parsed is still rebuilt. Three authority boundaries that change no product surface
now have their missing tests; the release runner requires all 12 targeted mutations to be killed.

**A worktree lane is merged only when integration moves.** After a successful Git merge, UnodeAi compares the
integration branch's `HEAD` with the value observed before the command. An unchanged `HEAD` is shown as
`nothing to merge`; a changed `HEAD` is shown as `merged`, regardless of Git's output language.

**A collected batch containing a failed subtask is a failed step.** `await_tasks` and `collect_ready_tasks`
record the failure as the tool call's status while collecting, so the step cannot show as a completed call
that happens to mention a failure in its text.

**An unfinished turn settles as partial.** The complete report remains visible while the unfinished structured
activity is carried separately. Partial stops waiting cards and wakes the coordinator, but it does not become a
completed delivery, a green evidence verdict, or a workflow gate pass; a workflow pauses before dispatching its
next step.

**Task status combines durable history with live handle facts.** Worker state, wait-window state, result state,
and read-receipt state are separate. A timeout may therefore have an open late-result window and a pending
result at the same time. Only a ready result names `collect_ready_tasks`; pending work asks the coordinator to
end its turn and wait for the host wake, not to poll or call the hidden compatibility alias.

A teammate's "Done" text is never the verdict on its own; the framework attaches its own evidence label to every delegated result. A green status means something verifiable happened — a recorded write with an observed passing check — not that the agent said it did.

- **Verified (green)** — a recorded file write AND an observed passing `run_checks` / completion gate. An agent that only read files never reaches it.
- **Tool activity recorded; delivery not checked** — read or search activity ran but no write was recorded. It tells you the mechanism ran, not that the requested result landed.
- **Replied, not verified** — file changes were recorded but checks did not pass or run (or a claimed pass does not match the framework's record). The PM should run checks or send it to review.
- **No evidence** — the reply had no framework-visible tool activity. It is not a completed task.

**Coordinator dispositions.** After the coordinator has actually decided whether to rely on a settled result, it may record one. 0.9.47 offered three; one round of real use produced nine distinguishable outcomes, so 0.9.48 records all nine rather than rounding them to the nearest of three: `accepted`, `accepted-with-caveat`, `accepted-after-rework`, `accepted-despite-framework-no-evidence`, `rejected`, `needs-rework`, `superseded`, `deferred`, `needs-human`. All but the three plain acceptances require a concrete reason, and a rejection forwards that reason to the delegate; the earlier verdict is *visibly amended* in the Workbench transcript, Activity, and the Team card — never silently rewritten. `needs-rework` is its own state, not a flag on `rejected`: one says the coordinator will not rely on the result, the other says the loop continues. No LLM judges whether prose "really delivered"; the disposition is an explicit decision, not an inference from the reply. Coordinator-accepted is an agent's decision, **not** enterprise or customer acceptance.

**A refused dispatch is a receipt, not a disposition.** When a coordinator declines to send work at all there is no result to assess, so it is kept as a separate `rejected-at-dispatch` record with its reason, and metrics report dispatch attempts, work actually dispatched, and refusals separately.

**Under-crediting is now counted too.** The framework already reported how often a green verdict was later rejected. 0.9.48 adds the other direction — how often a `no-evidence` or `replied-not-verified` result was accepted anyway. A correct answer built from context already on screen and a worker that guessed leave the same empty trace; UnodeAi does not pretend to tell them apart, because doing so means reading the prose, which is the self-grading this design excludes. It counts how often the distinction mattered instead.

**Per-agent command narrowing.** Command approval is a workspace-wide policy; an individual agent can be narrowed further in the Agent Builder — *Inherit global* (the default) or *Restrict to selected*. The editor shows a checklist built from the live global allowlist rather than a text box, so a per-agent setting can only narrow and never widen, and every saved selection is re-intersected with the current global allowlist at check time. An empty restricted list means that agent runs no commands, which is deliberately distinct from inheriting.

**What each context source says about itself.** The per-turn context receipt now shows two filesystem facts for each file-backed source: how long ago it was modified, with a visible note at 90 days or older, and whether a mechanical signal suggests it may be sensitive. Neither is a judgement — an old file is not a wrong file, and the sensitivity signal is a pattern, path, file-mode and `.gitignore` check, not a classifier, with no model reading the file and no matched content copied into the panel. Both are report-only: nothing is blocked or redacted from them in this release.

**Activity export truncation.** An exported message log keeps a 300-item retained window. When older activity was dropped by that window, the export *declares the omission and the omitted count* rather than silently appearing complete — so a short-looking export tells you what it is missing instead of looking broken.

**Run evidence packs.** A coordinator's first real delegation opens a run. It closes only when that coordinator gives a user-facing closeout after all delegated work settles; an unfinished coordinator leaves an explicit open run across restarts, and later dispatches remain in that visibly open run until it closes. Use `UnodeAi: Export Run Evidence Pack` to export one run as standalone Markdown without installing the extension. The pack carries dispatches, refusals, observed framework evidence, append-only coordinator dispositions, exercised approval/scope/grant receipts, and context-source labels. Its completeness statement is about that run, not the rolling Activity window. Coordinator acceptance is not human or customer acceptance, and no model judges whether the work was correct. Raw approved commands, context contents, and credential values are excluded.

**Portable Run Evidence.** The current `portable-run-evidence/3` schema distinguishes complete and partial run
closeout, carries delegation completion independently from its evidence verdict, and exports
`readReceipt: observed | not-observed` rather than asserting that a missing receipt means no read occurred.
The portable JSON maps a human decision's exact internal actor identity to a document-local `approver-1`; an
exercised MCP grant has no approver because no decision happened at that moment. Exact built-in routes survive
only when the builder validates their connection and endpoint, while a private custom route becomes
`custom-gateway` and its hostname stays internal. Complete file changes carry validated SHA-256 before/after
hashes and a deterministic root computed at write time, never source or diff bytes. A consulted PDF contributes
only a document-local content ordinal, class, extraction outcome, page coverage, truncation, and OCR state —
never its URL/query, attachment name, temporary path, raw bytes or extracted text. Relative changed paths,
timestamps, and hashes are deliberately retained and declared inside the artifact; historical or incompletely
observed fields stay explicitly unavailable.

**Stopping work.** While anything is running the status bar shows `⏹ Stop N`; one click ends every running turn, and it appears only while agents are working so its presence answers "is the crew still going". A coordinator can stop its own team too: `broadcast` and `send_message` only deliver a message and a teammate already mid-turn finishes regardless, so `cancel_task` ends the turn instead — one assignment by handle, one teammate by name, or the whole team. Two limits are structural: a coordinator cannot stop itself, because that would end the turn making the call, and a solo agent belongs to no team.

**What your key actually pays.** A gateway publishes what a model costs; what *your key* is charged is settled internally and frequently not reported. Both settings that cover it belong to the key rather than the account, because two keys on one account can sit in different billing groups with different prices and different callable models. `unode.priceGroup` names the group per connection; where several exist and none is named, UnodeAi shows the **undiscounted** rate rather than guessing the cheapest, since an under-estimate takes money without warning. `unode.priceMultiplier` states what fraction of the published price the key pays, and UnodeAi asks for it when you store a key. **Exactly one discount is applied** — a stated coefficient and a gateway-reported group ratio answer the same question, so a stated `1` deliberately suppresses a discount the gateway would have applied, and an unset connection lets the gateway answer. `0` is allowed and means the key is free; an empty box and Esc both mean list price, never free.

**Temporary task scope.** A coordinator can narrow a teammate's folder access for one assignment — intersected with the agent's configured Folder Access, only narrower and never wider; a read-only assignment also removes write and shell tools. The delegation card shows the temporary scope while it is active and marks it ended afterwards, so a normally write-capable agent can be sent on a read-only audit without changing its saved configuration. A request inside the saved Folder Access but outside that assignment returns a bounded task-scope refusal and the agent may continue with a granted action or report the gap; a request outside saved Folder Access remains terminal. **The boundary has not relaxed:** no refused path is newly readable or writable. A real path escape still ends the turn; a command-line out-of-root heuristic still blocks execution but lets the turn continue, and an expired, unsupported, or unforwarded temporary asset remains unavailable without ending useful work.

**Local project discovery is explicit, not a pre-registered Agent Builder folder.** `unode.localReadScope` has three values: `workspace`, `parent` (the trusted-workspace default), and `volume`. `parent` lets an agent follow an already-evidenced sibling project; `volume` is deliberately more expansive. On the first read, directory listing, Git-tag inspection, or `search_files` walk through that root, UnodeAi shows the resolved absolute path and asks once for the current extension session. The confirmation says that agents may search the entire tree and that returned names and contents may reach the configured model provider; volume adds an other-users-profile warning. Denial, dismissal, or an unavailable dialog blocks the read. Writes, deletes, generic shell access, and Claude native access stay in the working folder; Folder Access can still narrow the root. Tool cards and run evidence record only an opaque root id, action and count — not a path, query, filename or content.

**Directory listings are listings.** The activity card now says **List** / **Listed N folders** for directory operations rather than calling them reads.

This folder contains a static, website-ready wiki for UnodeAi.

## Media: what is local, and what needs a second approval

**Downloading a file and uploading it to a provider are two different acts, and UnodeAi asks separately.**

- **PDFs are read locally, by page.** A PDF — fetched with approval, or attached from your machine — is
  checked by its signature, held in a temporary asset store under an opaque id, and read through page-scoped
  tools that always state the range they covered against the document total. Its filename, bytes, source URL
  and temporary path never reach the model, chat history, or exported evidence.
- **Sending a stored image to a vision model needs its own approval.** An image an agent downloaded is not
  uploaded anywhere by default. It goes only when the exact route is known to support vision — never on an
  unknown — and only after a prompt naming the provider, host, byte count and estimated input cost. Your
  earlier download approval does not cover it, and neither does ordinary model-egress approval. The grant is
  per host *and* per purpose: allowing vision never allows transcription.
- **An approved image is used once.** It is dropped after that request, including when the request fails or
  you cancel, so a later turn cannot resend it without asking again. A route that rejects it is recorded as
  unsupported for that route alone, and the model is told the image was omitted — a text-only answer is
  never presented as analysis.
- **Video is unsupported and says so.** No decoder, native module, WASM, or downloaded runtime ships in the
  extension. Metadata inspection is not offered as video understanding.

## Files

- `index.html` - self-contained HTML page with embedded CSS and JavaScript.

## Website Integration

The page is intentionally static. It can be:

- linked directly from `www.weroam.xyz` or `www.unodetech.xyz`;
- copied into an existing site route such as `/unodeai/wiki`;
- embedded in an iframe;
- converted into a CMS page by copying the `<main>` content and the CSS variables.

Recommended route:

```text
/unodeai/wiki
```

The page links to:

- `https://www.weroam.xyz`
- `https://www.unodetech.xyz`
- `https://www.unodetech.xyz/pricing?lang=en`

No build step is required.
