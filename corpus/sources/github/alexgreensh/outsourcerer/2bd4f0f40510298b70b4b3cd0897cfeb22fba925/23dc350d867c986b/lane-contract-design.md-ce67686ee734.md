# Lane-Contract Design — one descriptor per lane

> Companion to `docs/lane-contract-inventory.md`. This proposes a single lane-descriptor
> interface every lane routes through, so the ~61 scattered per-lane sites collapse into
> one declaration per lane. It is design only — no production file is edited here.
>
> Base: `outsourcerer.sh` v0.11.1 @ `0ad7182`.

## Problem

Today a lane is described by ~12 parallel `case` statements plus a bespoke
`delegate_<lane>` function (see the inventory). The same conceptual lane is referred to by
up to three strings — **provider**, **lane code**, **dispatch vehicle** — and each table
keys on a different one. Adding a lane means editing all of them in lockstep; missing one
is a silent routing bug (the "-m claude-opus-4-8 quietly ran on Devin" class of fix that
already had to be patched by hand at `outsourcerer.sh:12858`).

A parallel worker (Slice 1) is adding lane-down state: `_lane_down_mark` /
`_lane_down_active` markers and a lane-down dispatch skip. That state currently has no
home. The contract must reserve one so the two slices land together.

## Proposal: one `lane_descriptor` per lane

Every lane declares a single descriptor. The router (`route_delegate`) and every
attribute table read from the descriptor instead of from a `case` branch. A lane is added
by writing one descriptor, not by editing twelve tables.

### Descriptor fields

```
lane_descriptor {
  # ---- identity ----
  name            : the canonical lane code (dv | or | cc | cx | gm | local |
                   droid | cursor | hermes | warp | cline | claudex | tokenrouter)
  aliases         : every other string this lane is known by, so the three
                   naming layers collapse: provider names, disp vehicles, and
                   legacy codes. e.g. cc -> { "cc", "ccnative", "claude-native" },
                   or -> { "or", "ccor", "codexor", "openrouter" }.
  provider        : the --provider value(s) that route here when no -m pins a lane.
                   empty for lanes where the model alias is the sole selector.

  # ---- availability / liveness ----
  ready           : a probe () -> bool. Replaces _ready_lanes' bespoke per-lane
                   block (inventory §F). Fast + best-effort; a slow probe is
                   time-capped by the caller. Returns the readiness DETAIL string
                   too (e.g. "glm/swe", "funded", "byok", "key-capped") so the
                   brief/handshake never hardcodes lane copy.
  cli             : the CLI binary this lane needs on PATH, or empty (local/
                   tokenrouter have no CLI; tokenrouter's gate is the KEY).
  cli_missing_hint: the install hint shown on a fail-fast missing-CLI die.
                   Replaces the per-lane strings in route_delegate:12883-12887.

  # ---- lane HEALTH (Slice 1 convergence point) ----
  health          : a slot, not a function. Holds the lane-down state the
                   parallel Slice-1 worker is introducing:
                     health.mark   : "down" | ""   (the _lane_down_mark value)
                     health.active : bool          (the _lane_down_active flag)
                     health.since  : epoch         (when it went down)
                     health.reason : short string  (quota / cli-dead / probe-fail)
                   The router reads health BEFORE dispatch: a down lane is
                   SKIPPED (the Slice-1 lane-down dispatch skip), not died on,
                   so fallback can route around it. A lane sets its own health
                   via lane_health_set / lane_health_clear helpers; the
                   descriptor only declares that it PARTICIPATES in health
                   tracking (participates: true|false). This is the clean home
                   for _lane_disp too: a future _lane_disp helper reads
                   descriptor.disp, not a case statement.

  # ---- model-id resolution ----
  resolve_model   : (alias) -> launchable id. Replaces _devin_model_for,
                   _devin_resolve_model, _gemini_api_id, _lane_model_for
                   (inventory §E). For engine lanes (droid/cursor/hermes/warp/
                   cline) this is passthrough — the engine owns its catalog.
  default_model   : the model used when no -m is given. Replaces
                   _route_provider_default_model (12726). empty = no default
                   (tokenrouter: a run without -m is a user error).
  owns_catalog    : bool. If true, -m is passed verbatim and alias resolution
                   is SKIPPED (the engine-lane alias skip, route_delegate:12852).
  catalog_lane    : the catalog key for live-catalog validation, or empty.
                   Replaces the _catalog_path whitelist (1099). Only
                   dv/warp/gm/gi carry a live catalog today.

  # ---- dispatch ----
  disp            : the dispatch vehicle string (devin | ccor | codexor |
                   ccnative | cxnative | gmnative | claudex | droid | cursor |
                   hermes | warp | cline | tokenrouter | local). This is what
                   _lane_disp would return. Replaces _fallback_disp_lane (12566)
                   and the final-dispatch case (13103).
  dispatch        : (tier, argv) -> rc. The delegate body. Replaces the
                   delegate_<lane> functions (inventory §D). The descriptor
                   owns: tier->autonomy-flag mapping, effort handling, the
                   actual CLI invocation, and ledger recording.
  tier_flags      : (tier) -> flag array + posture string. Replaces the
                   per-delegate tier case blocks (e.g. droid --auto low/medium/
                   high at 10951-10956).
  effort_map      : (effort) -> native flag or empty. Replaces _droid_effort
                   (10938), _agy_effort (10711), and the advisory-only prints.

  # ---- quota / cost ----
  quota_key       : the quota-pool this lane counts against. Replaces
                   _quota_lane_key (2571). Most lanes = their own name; the OR
                   vehicles (ccor/codexor) fold to "or"; gi folds to "gm".
  cost_class      : local | limited | credits. Replaces _route_resolution's
                   case (12681-12682), which drives _route_confirm copy.
  cost_disclosure : the user-visible cost string. Replaces
                   _lane_cost_disclosure (2461) — one branch per lane becomes
                   one field per descriptor.
  is_cloud        : bool. Replaces _is_cloud_lane (11618). Drives the cloud
                   gate (_cloud_disclose) and secret scan.
  run_cost        : (launch_epoch) -> cost string for the ledger. Replaces the
                   per-delegate _fg_run_cost calls.
}
```

### What the router becomes

`route_delegate` stops being a lane encyclopedia. It reads the descriptor for the
resolved lane and calls its methods:

```
# pseudocode for the post-contract route_delegate core
desc = lane_descriptor_for(resolved_lane)   # one lookup, not 12 case branches
if !desc.ready()  or  desc.health.mark == "down":   # Slice-1 skip lives here
    skip_or_fallback(desc)
    return
if desc.cli and !have(desc.cli):  die(desc.cli_missing_hint)
id = desc.owns_catalog ? MODEL : desc.resolve_model(MODEL)
if !desc.default_model and !MODEL_EXPLICIT:  die("needs -m")
if desc.catalog_lane:  _catalog_validate(desc.catalog_lane, id)
_route_resolution(desc.disp, id, desc.cost_class)   # class from descriptor
_cloud_disclose(desc.disp, id, task)  if desc.is_cloud
desc.dispatch(tier, argv)             # the delegate body, now a method
```

Every `case "$lane" in ...` table in §B of the inventory becomes a field read. The
`delegate_<lane>` functions become `dispatch` methods on their descriptors.

## Before / after: the droid lane

Droid is a clean engine lane: it owns its catalog, has a CLI gate, a tier->autonomy
mapping, an effort map, and a cost string. It currently spreads across 8 sites.

### BEFORE (today, scattered across the file)

```sh
# 1. _effective_lane:1952 — engine lanes where provider IS the lane
case "$2" in droid|cursor|hermes|warp|cline|claudex|tokenrouter) printf '%s' "$2"; return ;; esac

# 2. _ready_lanes:6093 — bespoke readiness
have droid && lanes="$lanes droid=byok"

# 3. route_delegate:12852 — engine-lane alias skip
if [ "$MODEL_EXPLICIT" = "1" ] && [ "$PROVIDER" != "droid" ] && ... ; then

# 4. route_delegate:12878+12883 — engine CLI gate + install hint
case "$disp" in
  droid)  have droid || die "droid CLI not on PATH (Factory Droid lane). Install it using the official guide: https://docs.factory.ai/cli. Then run 'droid' once to log in." ;;
  ...

# 5. _route_provider_default_model:12733
droid|cursor|hermes|warp|cline) printf '%s-default' "$1" ;;

# 6. _lane_cost_disclosure:2472
droid)  printf 'cash depends on your Factory plan or BYOK model; BYOK usage is measured or estimated by its provider' ;;

# 7. _is_cloud_lane:11620 / _route_resolution:12681
droid) return 0 ;;            # cloud
ccnative|cxnative|gmnative|devin|droid|cursor|hermes|warp|cline) ROUTE_COST_CLASS=limited ;;

# 8. _droid_effort:10938 + delegate_droid:10943 — the whole delegate
_droid_effort() {
  case "$1" in minimal) echo "none" ;; low) echo "low" ;; medium) echo "medium" ;;
    high|xhigh|max) echo "high" ;; *) echo "" ;; esac
}
delegate_droid() {
  local tier="$1"
  ...
  have droid || die "droid CLI not on PATH ..."
  case "$tier" in
    auto)         aflag=(--auto low);    posture="READ-ONLY ..." ;;
    accept-edits) aflag=(--auto medium); posture="MUTATING ..." ;;
    autonomous)   aflag=(--auto medium); posture="MUTATING ..." ;;
    dangerous)    aflag=(--auto high);   posture="DANGER ..." ;;
  esac
  if [ "${MODEL_EXPLICIT:-0}" = "1" ] && [ -n "$id" ]; then
    id="$(_lane_model_for droid "$id")"; ...; _validate_model_token "$id"; mflag=(-m "$id")
  fi
  local de; de="$(_droid_effort "$EFFORT")"; ... eff=(-r "$de")
  ...
  droid exec ${mflag[@]} ${aflag[@]} ${eff[@]} -o text "$wrapped"
  record_ledger droid "$ledger_model" "$ttier" "$tier" "$task" "$(_fg_run_cost droid 0 "")" droid
}
```

### AFTER (one descriptor, the router is lane-agnostic)

```sh
# The entire droid lane, in one place:
lane_descriptor_droid() {
  cat <<'DESC'
  name=droid
  aliases=droid
  provider=droid
  cli=droid
  cli_missing_hint="droid CLI not on PATH (Factory Droid lane). Install it using the official guide: https://docs.factory.ai/cli. Then run 'droid' once to log in."
  owns_catalog=yes
  default_model=droid-default
  catalog_lane=
  disp=droid
  quota_key=droid
  cost_class=limited
  is_cloud=yes
  cost_disclosure=cash depends on your Factory plan or BYOK model; BYOK usage is measured or estimated by its provider
  participates_health=yes
DESC
}

# ready probe
droid_ready() { have droid && printf 'byok'; }

# tier -> autonomy flags + posture
droid_tier_flags() {
  case "$1" in
    auto)         printf '%s\t%s' '--auto low'    'READ-ONLY (--auto low: reads + safe read-only cmds, no edits)' ;;
    accept-edits) printf '%s\t%s' '--auto medium' 'MUTATING (--auto medium: edits + safe commands)' ;;
    autonomous)   printf '%s\t%s' '--auto medium' 'MUTATING (--auto medium; droid has no separate OS-sandbox exec mode)' ;;
    dangerous)    printf '%s\t%s' '--auto high'   'DANGER (--auto high: full autonomy incl. riskier commands)' ;;
    *) return 1 ;;
  esac
}

# effort -> native flag
droid_effort_map() {
  case "$1" in minimal) echo none ;; low) echo low ;; medium) echo medium ;;
    high|xhigh|max) echo high ;; *) echo '' ;; esac
}

# the dispatch body (was delegate_droid)
droid_dispatch() {
  local tier="$1"; shift
  [ "${#REST[@]}" -gt 0 ] || die "no task prompt given"
  local task="${REST[*]}" id="${MODEL:-}" model_key="${MODEL:-droid}" ledger_model="droid-default"
  local flags_posture; flags_posture="$(droid_tier_flags "$tier")" || die "bad tier: $tier"
  local aflag="${flags_posture%%$'\t'*}" posture="${flags_posture#*$'\t'}"
  local mflag=()
  if [ "${MODEL_EXPLICIT:-0}" = "1" ] && [ -n "$id" ]; then
    _validate_model_token "$id"; mflag=(-m "$id")
  else id="(droid default/configured)"; fi
  local eff=()
  if [ -n "$EFFORT" ]; then local de; de="$(droid_effort_map "$EFFORT")"
    [ -n "$de" ] && { eff=(-r "$de"); printf '>>> [effort] reasoning=%s (native: droid exec -r %s)\n' "$EFFORT" "$de" >&2; }; fi
  local ttier; ttier="$(resolve_tier "$model_key" "${TTIER:-}")" || ttier="capable"
  local wrapped; wrapped="$(_build_prompt "$model_key" "$task" "$ttier")"
  _tier_banner "droid (Factory)" "$id" "$ttier" "$posture | $(_lane_cost_disclosure droid)"
  local rc=0
  droid exec ${mflag[@]+"${mflag[@]}"} ${aflag[@]+"${aflag[@]}"} ${eff[@]+"${eff[@]}"} -o text "$wrapped" || rc=$?
  record_ledger droid "$ledger_model" "$ttier" "$tier" "$task" "$(_fg_run_cost droid 0 "")" droid
  printf '>>> [receipt] %s.\n' "$(_lane_cost_disclosure droid)" >&2
  return "$rc"
}
```

The 8 scattered sites collapse to one descriptor file. The router calls
`droid_dispatch`, reads `droid`'s `cost_class`/`is_cloud`/`quota_key`/`disp` from the
descriptor, and the Slice-1 lane-down skip reads `health.mark` from the same place. No
`case "$lane" in droid)` branch survives outside the descriptor.

## Migration shape (for the later landing, not this slice)

This slice produces docs only. The later refactor lands incrementally to keep the test
suite green at every step:

1. **Introduce the descriptor table** alongside the existing `case` statements, with the
   router reading from descriptors first and falling back to the `case` on any
   unregistered lane. No behavior change.
2. **Port one lane at a time** into its descriptor (droid first, per the illustration),
   deleting its branches from each table as it goes. Each port is a standalone commit the
   test suite must pass.
3. **Wire `lane_health`** when Slice 1 lands its markers: the descriptor's
   `participates_health` flag turns on the skip, and `_lane_disp` (if introduced) reads
   `descriptor.disp`.
4. **Remove the fallback `case` statements** once every lane is ported.

The descriptor is the single seam. The inventory (`docs/lane-contract-inventory.md`) is
the checklist of sites each port must retire.
