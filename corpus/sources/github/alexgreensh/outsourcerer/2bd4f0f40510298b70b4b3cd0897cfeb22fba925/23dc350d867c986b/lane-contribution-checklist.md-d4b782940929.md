# Lane-Contribution Checklist — before you add a new lane

> Modeled on a peer OSS provider-contribution checklist, adapted to outsourcerer's lanes.
> Use this when adding a new lane (devin / cc / codex / gemini / droid / cursor / warp /
> cline / openrouter / tokenrouter / local, or a new one). It is the gate the
> lane-contract descriptor (`docs/lane-contract-design.md`) makes enforceable.
>
> Base: `outsourcerer.sh` v0.11.1 @ `0ad7182`. References are to the inventory at
> `docs/lane-contract-inventory.md`.

## How to use this

Each section is a hard gate. A PR adding a lane must satisfy every checked item. "Lane
module" means the one `lane_descriptor_<name>` declaration plus its `dispatch` /
`ready` / `resolve_model` / `tier_flags` / `effort_map` helpers — the single place the
lane lives after the contract lands. Until the contract lands, the "lane module" is the
set of `delegate_<lane>` + the per-lane `case` branches, and this checklist is what keeps
that set complete.

---

## 1. Architecture

- [ ] **The lane lives in one place.** After the contract: one `lane_descriptor_<name>`
      declaration and its helper functions. Before the contract: the `delegate_<lane>`
      function plus its branches. No lane-specific logic scattered across unrelated
      functions.
- [ ] **The router factory has an explicit case for the lane.** `route_delegate`'s
      final-dispatch `case` (`outsourcerer.sh:13103`) names the lane's disp vehicle, OR
      (post-contract) the descriptor is registered so the router looks it up. No
      "fall-through to a default lane" — an unregistered lane must fail loud, not
      silently route to devin.
- [ ] **No lane-specific url / token / model logic outside the lane module.** Endpoint
      URLs, API keys, model-id aliases, and effort maps all live in the descriptor (or
      the `delegate_<lane>` before the contract). The router never contains a
      `case "$lane" in <name>)` branch for these. If you find yourself editing
      `_route_provider_default_model`, `_lane_cost_disclosure`, or `_droid_effort`-style
      helpers, you are editing the wrong file — that logic belongs in the lane module.
- [ ] **The three naming layers are reconciled.** The lane's `aliases` field lists every
      string it is known by (provider name, lane code, disp vehicle, legacy codes). The
      router, the fallback dedupe (`_fallback_disp_lane` / `_fallback_provider_for_lane`),
      and the quota key (`_quota_lane_key`) all resolve through `aliases`, not through
      separate `case` branches that can drift.
- [ ] **Engine-lane catalog ownership is declared.** If the lane owns its model catalog
      (droid/cursor/hermes/warp/cline pattern), `owns_catalog=yes` so alias resolution is
      skipped (`route_delegate:12852`). If the lane has a live catalog to validate
      against (dv/warp/gm/gi pattern), `catalog_lane` is set so `_catalog_validate` runs.
      A lane is one or the other, never both, never neither by accident.

## 2. Auth / API

- [ ] **Model-id resolution is via the lane interface.** Aliases -> launchable id goes
      through `resolve_model` (the descriptor) or `_lane_model_for` /
      `<lane>_resolve_model` (pre-contract). The router never hand-maps an alias for the
      lane. Cross-lane siblings (e.g. kimi shared by devin/droid/warp) go through
      `_lane_model_for`, which is itself routed by lane, not inlined.
- [ ] **Tokens / creds are resolved by the lane, not the router.** The lane's `ready`
      probe or `dispatch` body loads its own key/endpoint (e.g. `_tr_load_key`,
      `_claudex_token`, `CURSOR_API_KEY`). The router does not know how the lane
      authenticates. A missing credential fails fast inside the lane module, before the
      cloud gate and before auto-detach would bury the error in a detached job.
- [ ] **The dispatch spec is declared.** `disp` (the dispatch vehicle) is a descriptor
      field, so `_fallback_disp_lane`, `_so_resolve`, and the final-dispatch `case` all
      read the same value. A lane that can be reached via two vehicles (e.g. gm text vs
      gi image, or cc native vs ccor via OpenRouter) declares both and the router picks
      by context, not by a duplicated `case` in `_so_resolve`.
- [ ] **The lane declares its cloud status.** `is_cloud` drives the cloud gate
      (`_cloud_disclose`) and the secret scan. A local lane (ollama/lmstudio/llama.cpp)
      sets `is_cloud=no` so the gate is skipped entirely. Getting this wrong ships repo
      content (or a `.env`) off-machine, or pointlessly gates a local lane.
- [ ] **Per-lane/repo trust is honored.** If the lane can be trusted for the
      credential-file hard-block in specific repos, it appears in
      `trusted-lanes.json` and `_lane_trusted_for_pwd` resolves it. The trust grant is
      never an env var (it would inherit into bg/fanout children and widen the trusted
      set).

## 3. Tests

- [ ] **Lane selection test.** A test asserts that `-m <model>` under `--provider <lane>`
      resolves to the lane's disp vehicle and the lane's resolved model id. This is the
      test that catches a new lane silently falling through to the devin default (the
      "-m claude-opus-4-8 ran on Devin" class of regression).
- [ ] **Unsupported-lane behavior test.** `--provider <bogus>` dies with a clear message
      listing the valid lanes, and a lane whose CLI is missing dies fast (pre-cloud-gate,
      pre-auto-detach) with the install hint, not inside a detached job.
- [ ] **Existing lane tests still pass.** Adding a lane must not change routing for any
      existing lane. Run the full conformance suite. A new branch in a shared `case`
      table that shadows an earlier branch is the classic silent regression here.
- [ ] **Quota-key fold test.** If the lane shares a quota pool (e.g. two OR vehicles fold
      to `or`, or an image vehicle folds to `gm`), a test asserts the fold so a cap on
      one vehicle is seen by the other. If the lane has its own pool, a test asserts it
      does NOT fold into a sibling's.
- [ ] **Lane-down skip test (when Slice 1 lands).** With `health.mark=down` set, the
      router skips the lane and falls through to a ready fallback (or dies with the reset
      reason if none). A down lane is skipped, not died-on, so fallback can route around
      it.

## 4. Documentation

- [ ] **README / env-var notes.** The lane's `--provider` name, its CLI install steps,
      its env vars (endpoint URL, API key, profile, harness), and its cost class appear
      in the README. A user should be able to set up the lane from the README alone.
- [ ] **Design doc updated.** `docs/lane-contract-design.md` lists the new lane's
      descriptor, and `docs/lane-contract-inventory.md` is updated if the refactor
      introduces a new site (or retires one). The inventory count (~61 sites) is the
      regression baseline: a new lane that adds sites instead of a descriptor is a
      contract violation.
- [ ] **Cost disclosure is honest.** The `cost_disclosure` string matches what the lane
      actually bills. "metered cash" vs "spends your plan limits" vs "$0 cash + $0 plan"
      are different promises to the user; the `_lane_cost_disclosure` branch (or the
      descriptor field) must match the lane's real billing model. A BYOK lane never
      claims "$0 cash" — the user's key provider bills.
- [ ] **Brief / handshake copy is not hardcoded.** The lane's readiness detail (the
      string `_ready_lanes` emits, e.g. "byok", "funded", "key-capped") comes from the
      `ready` probe, not from a hardcoded `echo` in `cmd_brief`. A new lane that adds an
      `echo` line to `cmd_brief` instead of a `ready` detail is dodging the contract.

---

## Quick pre-PR self-check

Before opening a PR that adds or changes a lane, grep the file for the lane name. Every
hit outside the lane's own descriptor / `delegate_<lane>` is a site the contract wants to
retire. If you are adding a hit rather than removing one, stop and re-read section 1.

```
grep -n "<lane-name>\|<disp-vehicle>\|<provider-name>" outsourcerer.sh
```

The goal: a lane is added by writing one descriptor, not by editing twelve tables. This
checklist is the gate that keeps it that way.
