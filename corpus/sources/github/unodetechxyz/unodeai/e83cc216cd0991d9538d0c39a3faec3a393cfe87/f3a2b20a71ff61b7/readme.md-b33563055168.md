<p align="center">
  <img src="images/unode.png" alt="UnodeAi" width="128" height="128">
</p>

# UnodeAi

### Turn AI agents into an organized workforce.

**Every AI coding tool can tell you it finished. UnodeAi can show you what it did.**

A project manager agent breaks your goal into tasks and hands them to specialists. Each one has a role, its
own skills, the model you picked for it, and only the permissions you granted. What an agent *claims* stays
separate from what the framework *observed*. An agent saying “done” is never printed as evidence, and no model
is ever asked to grade another model’s work.

[Get started](#quick-start) · [User guide](USAGE.md) · [Security model](SECURITY.md) ·
[Changelog](CHANGELOG.md) · [Models and pricing](https://www.unodetech.xyz/pricing?lang=en)

<!-- Add the Mission Control screenshot here when a real product asset is available. -->

## Built for the work where “it says it’s done” is not enough

| If you… | UnodeAi gives you |
| --- | --- |
| **Bill for the work** — agency, consultancy, contractor | A run exported as one Markdown file the client can read without installing anything, listing every dispatch, decision, approval and scope grant — and what it left out. A portable JSON variant carries no request text, instructions, command lines or file contents; agents and approvers become document-local ordinals, private routes become bounded categories, and write-time hashes prove change equality without retaining source. It declares both what it withheld and what it kept. |
| **Answer to someone** — regulated, procurement-reviewed, or security-reviewed teams | Evidence that was recorded as the work happened, not reconstructed afterwards. Contract, privacy and GRC roles that are read-only by capability, and a sanctions/export-control skill whose correct output is a refusal routed to a named human. |
| **Run more than one agent** | A coordinator that reports `partial` or `blocked` with a reason per undelivered item instead of going quiet — and, if it ends saying nothing, a closeout UnodeAi writes itself from observed facts, claiming nothing about correctness. |
| **Refuse to hand your code to one vendor** | Per-agent routing across Claude, OpenAI-compatible endpoints and your own gateways. Keys live in the OS keychain. Nothing leaves the machine unasked — no telemetry, no control service, no request at activation. |

## Companies already solved this. We’re teaching it to agents.

A company is not just a group of capable people. It’s a set of agreements: who owns what, who decides, who
reviews, and what gets written down. Those agreements are why a hundred people’s work adds up instead of
colliding.

Nobody designed them in a room. They were worked out over a century of getting it wrong, and they remain the
most tested coordination technology we have.

Agents skipped all of it.

The last three years went into making a single agent more capable. Almost none of it went into how several
agents work together. So a team of agents ends up looking like a company with no job titles, no manager, no
sign-off, and no filing cabinet. Everyone is competent. Nothing is accountable.

If you have given an AI real work, you already know how this feels. It sounds just as confident when it fails
as when it succeeds. Nobody reviews it but you. And when it’s finished, you have a chat log where a record
should be.

A better model doesn’t fix that. Ask a stronger one the same way and it fails the same way, because what was
missing was never intelligence.

**UnodeAi supplies the structure.** Each agent has a role and a mandate. A project manager agent assigns the
work and collects the results. Permissions decide what each one can reach. Finishing means something specific:
a check that ran, or a person who signed off. And the record keeps what an agent claimed apart from what
actually happened, because “I’m done” has never counted as proof in a company either.

This stopped being optional when agent output started leaving the building — into client deliverables, audits
and procurement reviews, where a chat log is not an artifact anyone can accept.

We’ll say what we’re betting on. This structure is proven for people. Whether it works as well for agents is
the question this product exists to answer, and the evidence layer is there so you can judge for yourself.

## What the organization is made of

UnodeAi ships **52 role templates** and **25 team presets** — Software Engineering, Marketing, Sales, Contract
& Compliance, Security & Governance, Business Operations, Revenue Operations, Customer Experience, Data
Intelligence, Product Discovery, and more — so a team is something you assemble, not something you rebuild in
every conversation.

| | The company equivalent |
|---|---|
| **Role** | a job title with a mandate |
| **Skills** | the procedures that job runs on, loaded when they are relevant |
| **Manager** | a project manager agent that assigns work and collects results |
| **Workflow** | a repeatable handoff between roles |
| **Authority** | what this position may reach, and what needs approval first |
| **Evidence** | the file that outlives the conversation |

No single model is best at everything any more, so *which model runs which role* is a decision worth making
per agent rather than per vendor.

## Why us

**The evidence layer is the product, not a feature attached to one.** It is cheap to add a summary view to a
tool that already trusts its agents, and it does not survive contact with a run that went wrong. Here the
separation is structural: verdicts come from recorded writes and observed check results, a delegate's prose
cannot become a green verdict, and the rules are held in place by mutation tests that fail if a sensor stops
sensing.

**Our own claims are auditable too, which is the only reason to believe the rest.** `SECURITY.md` is
re-audited before every release and records what it got wrong — including a boundary the previous release
overstated, corrected in place rather than quietly rewritten. CI builds the shipped artifact, a human
publishes those exact bytes without rebuilding, and the SHA-256 is published so you can check what you
installed against what was reviewed.

**It runs where you already work.** VS Code, Cursor and Windsurf — with your providers, your keys and your
team.

## Quality is a mechanism, not a promise

UnodeAi separates what an agent says from what the framework actually observed.

| What happened | What UnodeAi can honestly say |
|---|---|
| A delegation returned without a framework-visible trace | **No evidence** |
| Read, search, or other tool activity was recorded, but no change was verified | **Tool activity recorded; delivery not checked** |
| Files changed, but no matching passing verification was observed | **Replied, not verified** |
| A recorded change has an observed passing verification result | **Verified** |
| The coordinator explicitly decided to rely on the result | **Coordinator accepted** |
| The coordinator rejected an earlier result | **Coordinator rejected — amended**, with the earlier verdict and reason still visible |
| A decision belongs with a person | **Human intervention required** |

A green framework verdict means a check actually ran and passed. It never means a model declared its own work
good. Likewise, coordinator acceptance is an agent coordinator's explicit decision — not customer,
enterprise, or human acceptance.

The latest mechanism closes a gap our own field run exposed: a coordinator rejected work after an earlier
verdict had already been shown, but the framework never captured that decision. The coordinator can now record
`accepted`, `rejected`, or `needs-human` after it actually decides. A rejection requires a reason,
forwards it to the delegate, and visibly amends the verdict in Chat, Messages, and the Team card. UnodeAi is
capturing a decision the coordinator already made; it is not adding an LLM judge.

## How work moves

1. **You state the outcome.** Use Solo for a focused task or give the Project Manager a substantial goal.
2. **The PM plans and delegates.** It assigns roles, declares task scope, tracks progress, and keeps parallel
   work from silently colliding.
3. **Specialists work inside your boundaries.** Rules guide them; configured tools, approvals, provider
   routes, and folder access define their actual authority.
4. **Optional isolation keeps parallel changes reviewable.** When you enable worktree mode, delegated work
   can run in isolated lanes. UnodeAi does not infer or enable worktree mode from task wording.
5. **Your real check can gate integration.** When worktree mode is enabled and a verify command is configured
   and approved, its observed result can gate the merge. Without those conditions, UnodeAi does not claim an
   automatic quality gate.
6. **You review the integration.** `autoMerge` is off by default. The integration branch and its evidence
   remain available for review before work lands.
7. **You get the record.** See what changed, which tools ran, what passed, what was not checked, and whether a
   later coordinator decision amended an earlier verdict.

## Your process, as files you can inspect

The working agreement belongs with the project:

| What you define | Where it lives | What it does |
|---|---|---|
| **Repository guidance** | `AGENTS.md`, `CLAUDE.md`, `.unode/rules.md` | Records conventions, constraints, review expectations, and project-specific instructions |
| **Team** | `.unode/team.json` | Defines members, roles, model routes, tool capabilities, folder access, MCP grants, and team behavior |
| **Workflows** | The team definition | Encodes repeatable role-to-role work instead of rebuilding the sequence in every chat |

Repository guidance has a documented, inspectable precedence: `AGENTS.md`, then `CLAUDE.md`, then
`.unode/rules.md`. That does not make one file magically impossible to override; it makes the order visible,
reviewable, and changeable through the files you control.

Project knowledge is progressively disclosed. Each turn receives compact, deterministic indexes for the
instruction files and structured Markdown under `docs/`; an agent can load a relevant full source through
the existing root-confined read tool. This reduces standing context without pretending that every task becomes
cheaper — an agent may spend additional turns or tool calls fetching what it needs.

Rules can direct behavior, but they cannot grant authority. Project files do not widen Workspace Trust,
command approval, network consent, MCP grants, write policy, or folder access. Those boundaries remain
host-enforced and separately inspectable.

## Why teams choose UnodeAi

| Advantage | What it means in practice |
|---|---|
| **An AI team that follows your process** | Roles inherit your project rules, handoffs, workflows, and checks instead of requiring your team to adopt a proprietary ritual |
| **Evidence that names its limits** | Status comes from framework-visible actions and checks; later coordinator decisions amend the record rather than rewriting history |
| **Control at the task level** | A delegation can narrow a teammate's folder access for one assignment without permanently changing the agent |
| **A model per role** | Use premium reasoning where it matters, economical models for routine work, and different providers in the same crew |
| **Optional isolated delivery** | User-enabled worktrees separate parallel changes; configured and approved checks can gate integration |
| **Inspectable context and cost** | The context manifest lists sources and estimated text tokens; actual cost appears only where provider usage data supports it |
| **Security controls in the product** | Workspace Trust, per-host egress consent, command/write approval, MCP grants, folder scopes, and credential state are visible controls |

Model choice matters, but it is not the durable moat. Providers change, prices fall, and stronger models
arrive. What lasts is the process, evidence, and authority boundary your team can keep while swapping the
model underneath.

## Built with the team it ships

UnodeAi is built and audited with UnodeAi. Each release asks the shipped product to investigate the prior
release, then turns field evidence into the next mechanical guard.

That practice has changed the product in concrete ways:

- A field run found a read-only result described too generously; the verdict was narrowed to **Tool activity
  recorded; delivery not checked**.
- Another coordinator decision arrived after the displayed verdict; v0.9.47 makes the later rejection visible
  and preserves why it changed.
- Export truncation, temporary task scope, and overlapping delegation are now surfaced because our own audits
  found where a technically correct mechanism was still invisible at the decision point.

This is not a claim that the product validates itself. It is a receipt for how defects are found. Unit tests,
mutation gates, deterministic harness tasks, field runs, and human review each answer different questions;
none is promoted into evidence it did not collect.

## Security without surrendering usefulness

- **No telemetry.** UnodeAi does not run an analytics or remotely reachable control service.
- **Destinations are explicit.** Model data goes to providers you configure; network-capable tools use
  destinations you configured or explicitly approved. UnodeAi does not make an absolute claim that workspace
  data never leaves the machine while you are using a model or approved tool.
- **Workspace Trust is honored.** Execution surfaces stay off in an untrusted workspace.
- **Effects are gated.** Command and write behavior follows the policy you set; MCP servers are default-deny
  per agent until granted.
- **File tools are rooted.** Real-path checks prevent traversal and symlink escapes; task scope can narrow
  access but cannot widen the agent's permanent grant.
- **Secrets use VS Code SecretStorage.** Keys do not belong in team definitions, settings, exports, logs, or
  source control.
- **Human control remains human.** `needs-human` records that a decision is required; coordinator acceptance
  is never presented as enterprise sign-off.

See [SECURITY.md](SECURITY.md) for the complete network, execution, storage, Workspace Trust, and packaging
model.

## Quick start

1. Install UnodeAi and open a trusted workspace.
2. Choose a provider: use the Unode gateway, connect an OpenAI-compatible endpoint, use a local gateway, or
   run Claude through your existing Claude CLI login.
3. Create or import a team, then choose which model, capabilities, folder access, and MCP grants belong to
   each role.
4. Keep the project guidance you already use in `AGENTS.md` or `CLAUDE.md`, and add
   `.unode/rules.md` when you want UnodeAi-specific team guidance.
5. Optionally enable worktree mode. If you want verified merge gating, configure and approve the verify
   command and keep `autoMerge` off until you deliberately choose otherwise.
6. Give Solo a focused task or give the PM a larger outcome. Review the transcript, evidence, changes, and
   integration branch before finalizing.

The [User guide](USAGE.md) covers provider setup, teams, approvals, worktrees, workflows, MCP, exports, and
troubleshooting.

## A growing ecosystem, with bring-your-own paths

The catalog keeps growing across models, roles, skills, and MCP integrations. Growth is not limited to what
ships in one release:

- Start from built-in software, product, research, writing, operations, marketing, sales, finance, and
  governance roles, then edit them or define your own.
- Attach skill playbooks that are progressively disclosed when relevant instead of placing every procedure in
  every prompt.
- Connect supported MCP integrations per agent, with explicit grants.
- Bring your own OpenAI-compatible endpoint, gateway, model, API key, role instructions, workflows, and MCP
  servers; choose from the growing set of validated skill playbooks.

The point of the ecosystem is choice under one governance model. A larger catalog should not become a reason
to hide what an agent can access or where data can go.

## Providers and capabilities

Use the Unode gateway for one account across many models, connect another OpenAI-compatible provider, route to
a local or self-hosted model, or use Claude through your own Claude CLI login. Codex Headless remains visible
as Coming soon while its mediated runner is completed.

Roles can use different providers in the same crew. The surrounding process — context, permissions, approvals,
task scope, evidence, and verification — remains inspectable when you change the model.

Core capabilities include:

- PM-led delegation with async fan-out, progress, result collection, and file-scope conflict detection
- Custom agents, reusable role templates, progressively disclosed skills, and deterministic workflows
- Explicit task-scoped folder access that can narrow but never widen a delegate's permanent grant
- User-enabled git worktrees, reviewable integration branches, and optional verify-command merge gating
- `autoMerge` off by default
- Coordinator `accepted`, `rejected`, and `needs-human` decisions with visible amended verdicts
- Chat, Team, and Messages evidence surfaces, plus exports that disclose retained-window truncation
- Per-turn context manifests with source provenance and estimated text-token counts
- Actual usage and cost only when the selected provider reports enough usage data to support them
- Command and write approvals, rooted file tools, Workspace Trust, per-host egress consent, and default-deny
  MCP grants
- Custom and bring-your-own options across providers, models, roles, workflows, and integrations, alongside a
  growing catalog of validated skill playbooks

## New in v0.9.79

**Shared memory can inform the team without becoming authority.**

- **An agent-selected `contract` is no longer a trust decision.** Every row reloaded from the mutable
  `.unode/memory/notes.md` file is explicitly `untrusted` unless its exact bytes have a separate local
  attestation. `pitfall`, `contract`, and `decision` describe what a note claims; none can grant itself
  priority, permission, or the status of evidence.
- **Review is explicit and reversible.** Run **UnodeAi: Review Shared Memory** to inspect an exact row, cancel
  without changing it, attest it as reviewed team guidance, or revoke that attestation. The host-owned,
  first-workspace-folder-scoped record stores a digest and bounded metadata, never note prose or a person
  identity. A one-byte edit invalidates the match, and untrusted workspaces cannot create or apply attestations.
- **Memory is quoted and bounded before it reaches any teammate.** Text and metadata are structurally encoded,
  so a note containing `</shared_memory>`, a forged trust field, or `SYSTEM:` stays inside one data row. Load
  and append fail closed across symlink/junction escapes, and both row and byte caps apply.
- **The prompt and its receipt now use one memory snapshot.** Previously, a note written between two separate
  reads could make the receipt describe different memory from the prompt. The manifest now reports typed counts
  for the selected untrusted and human-attested rows without retaining their bodies. Attestation changes only
  prompt admission/display; it never widens tools, folders, commands, network, MCP, delegation, hooks, completion,
  or evidence authority. There is no automatic memory-to-rule or memory-to-skill promotion.
- **Cross-provider dispatch no longer interrupts you by default.** When a coordinator hands work to a teammate
  on a different model provider, its brief is sent without a pop-up. Turn off **Allow cross-provider dispatch
  without approval** in Settings → More to be asked every time, as before. It is a user-level setting, so a
  workspace cannot change it, and a destination that cannot be resolved is still refused.
- **The result of something you just did now appears in the middle of the screen.** When you answer a dialog or
  picker — attesting a memory row, restoring a checkpoint, importing a chat, storing a key — the outcome,
  including a refusal, is a centred pop-up instead of a corner notification that was easy to miss.

## Previously in v0.9.78

**The product now says what it is, and two commands stopped depending on a write your editor can refuse.**

- **UnodeAi is an organized AI workforce, not a model picker.** The name, the store description and this
  page now lead with the thing the product actually builds: agents with roles, a manager, handoffs between
  them, and a record of who did what. Choosing models is something you can do here; it is not the point.
- **`UnodeAi: Open Settings` opens the panel first.** Both it and `UnodeAi: Refresh Model Prices` used to
  run a legacy price-coefficient repair *before* doing what you asked. That repair writes to your User
  Settings JSON — and an editor refuses that write while the file has an error or a warning, so the command
  appeared to do nothing at all. The panel now opens, and a price refresh completes and reports its result,
  before the repair starts. **This was never a Cursor-specific defect** — stock VS Code refuses the same
  write, with *"Unable to write into user settings. Please open the user settings to correct
  errors/warnings in it and try again."* Cursor surfaced our ordering mistake; it did not cause it. If the
  repair itself fails you now get a warning that says so and a direct route to User Settings JSON, and the
  work you asked for is already done.
- **A status line that was simply untrue is gone.** The team tools used to state that this release has no
  human acceptance layer. There is one: a person can record a run verdict, and when they do it is kept
  separate from the coordinator's acceptance and never inferred from it. Messages that describe what this
  release can and cannot do are now pinned to a version and re-checked when it changes, so a claim cannot
  quietly outlive the release it describes.

## Previously in v0.9.77

**An agent can look at the project next door — after UnodeAi names the folder out loud and you say yes.**

- **Local project discovery is read-only, and it asks first.** In a trusted workspace, `unode.localReadScope`
  (`workspace` · `parent` · `volume`, default `parent`) lets an agent reach a sibling project without your
  registering it by hand. Before the first read or search outside your workspace, UnodeAi shows the
  **resolved absolute path**, says that a search can walk that whole tree and that filenames and contents may
  be sent to that agent's model provider, and asks once for the session. Declining, dismissing, or being
  unable to show that dialog refuses the access. **Writes, deletes and shell commands do not widen** — they
  stay in the working folder — an untrusted workspace ignores the setting, and per-agent Folder Access
  remains a stricter ceiling. Each admitted access leaves a receipt carrying only an opaque root id, the kind
  of operation, and a count: never a path, query, filename, or file contents.
- **A Git tag is now a checked fact.** The read-only `inspect_git_tag` tool resolves a tag in an
  already-readable local repository to its commit, date and subject, so a version claim about a local
  snapshot rests on the repository rather than on something a document said.
- **The dashboard was looked at in all four bundled themes, and it was not right.** The *done* dot measured
  2.00:1 against the default light theme's background, where 3.00 is the floor. *Done* and
  `Verified / mergeable` are now blue, which separates them from the green *working* dot by lightness as well
  as hue in every theme; verification chips are outlined rather than filled, which fixed two more states that
  were below the text floor or invisible entirely. All twelve chip states were measured after the change.
- **A status dot can no longer vanish** if a theme leaves its colour undefined; it falls back to the editor
  foreground instead.
- **A streamed paragraph containing bold, code or a link keeps your selection too**, not only a paragraph
  that is entirely plain text. A paragraph whose tail is genuinely re-parsed is still rebuilt. The tests hold
  every already-rendered child to the same object across paints, which is the mechanism a selection depends
  on; no test can hold a real browser selection, and that check is scheduled for after this release.

## License

See [LICENSE](LICENSE).
