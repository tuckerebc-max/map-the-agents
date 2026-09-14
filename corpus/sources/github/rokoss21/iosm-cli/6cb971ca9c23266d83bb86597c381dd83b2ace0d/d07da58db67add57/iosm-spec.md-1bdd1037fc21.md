# IOSM v1.0 - Technical Specification and Playbook

Status: Normative specification

## Abstract

IOSM (Improve -> Optimize -> Shrink -> Modularize) is an algorithmic methodology for engineering excellence. It defines a reproducible cycle for improving technical systems through explicit phases, measurable Quality Gates, normalized metrics, evidence-confidence rules, and an aggregate health score named the IOSM-Index. Unlike purely declarative process models, IOSM is intended to be implemented in tooling, executed in delivery workflows, and audited through machine-readable evidence.

## Executive Summary

- Purpose: reduce chaotic improvement work, lower the cost of change, increase predictability, and align engineering action with business value.
- Method: run iterative IOSM cycles in a fixed order, evaluate each phase against Quality Gates, validate change hypotheses, enforce cross-metric guardrails, and compute an IOSM-Index from normalized metrics.
- Outcome: clearer systems, more resilient performance, lower cognitive load, cleaner interfaces, safer modular evolution, stronger delivery flow, and reusable organizational learning.
- Result: a methodology that can be adopted manually, automated in CI/CD, benchmarked across teams or services, and safely extended for AI-assisted engineering.

## Table of Contents

1. [Scope](#1-scope)
2. [Normative Language](#2-normative-language)
3. [Definitions](#3-definitions)
4. [Values and Axioms](#4-values-and-axioms)
5. [Conformance](#5-conformance)
6. [Required Artifacts](#6-required-artifacts)
7. [Configuration Model](#7-configuration-model)
8. [Operating Profiles and Adaptive Thresholds](#8-operating-profiles-and-adaptive-thresholds)
9. [Planning and Economic Decision](#9-planning-and-economic-decision)
10. [Change Hypothesis Protocol](#10-change-hypothesis-protocol)
11. [Cycle Lifecycle](#11-cycle-lifecycle)
12. [Metrics Model](#12-metrics-model)
13. [Evidence Confidence and Decision Quality](#13-evidence-confidence-and-decision-quality)
14. [IOSM-Index and Stabilization](#14-iosm-index-and-stabilization)
15. [Phases and Quality Gates](#15-phases-and-quality-gates)
16. [Fitness Functions](#16-fitness-functions)
17. [Agent and Automation Governance](#17-agent-and-automation-governance)
18. [Anti-Patterns](#18-anti-patterns)
19. [Reporting and Learning Closure](#19-reporting-and-learning-closure)
20. [Scaling and Adoption](#20-scaling-and-adoption)
21. [Conclusion](#21-conclusion)

## 1. Scope

This document specifies IOSM as a methodology for continuous system improvement.

It defines:

- the mandatory order of phases;
- the minimum required artifacts;
- the canonical metrics model;
- the Quality Gate semantics;
- the change hypothesis protocol;
- the evidence-confidence model;
- the IOSM-Index calculation;
- the minimum evidence required to claim conformance.

This document does not prescribe:

- a specific programming language or platform;
- a specific observability stack;
- a single backlog management tool;
- a single graph-partitioning or profiling implementation;
- a single model or agent framework for automation.

## 2. Normative Language

The keywords `MUST`, `MUST NOT`, `REQUIRED`, `SHOULD`, `SHOULD NOT`, and `MAY` in this document are to be interpreted as normative requirements.

- `MUST` and `MUST NOT` indicate absolute requirements.
- `SHOULD` and `SHOULD NOT` indicate strong recommendations that may be deviated from only with explicit justification.
- `MAY` indicates an optional capability.

## 3. Definitions

- `System`: the software product, service, platform, subsystem, or module under improvement.
- `Cycle`: one full IOSM iteration from planning through scoring and decision.
- `Cycle Scope`: the declared subset of the system targeted by a given cycle, expressed in modules, services, domains, contracts, or bounded components.
- `Cycle Capacity`: the configured upper bound on how many goals, scope elements, and expected coordinated changes may be admitted into a single cycle.
- `Phase`: one of the four ordered stages: Improve, Optimize, Shrink, Modularize.
- `Goal`: a prioritized improvement objective selected for the current cycle.
- `Quality Gate`: a deterministic pass/fail evaluation performed after a phase.
- `Metric`: a quantitative measurement normalized into the range `[0.0, 1.0]` unless otherwise stated.
- `Fitness Function`: an executable architectural or operational rule that continuously checks a constraint.
- `Baseline`: the measured pre-change state used for comparison in Optimize, Shrink, Modularize, and guardrail evaluation.
- `Observation Window`: the time range or sample range used to collect measurements.
- `Waiver`: an explicit, time-bound exception that permits temporary non-conformance while recording debt.
- `Change Surface`: the number of modules, services, or public contracts that must change together to deliver a feature or fix.
- `Contract`: a stable boundary agreement between modules, services, or APIs.
- `Invariant Catalog`: the versioned set of system invariants used for logical consistency evaluation.
- `Delivery Boundary`: the declared unit over which delivery flow is measured, such as repository, service, deployable, or team-owned stream.
- `Evidence`: a raw measurement, report, trace, benchmark, test result, or structured observation used to support a metric or decision.
- `Evidence Tier`: the trust class of evidence. Tier `A` is direct automated production-grade evidence, Tier `B` is automated synthetic or staging evidence, and Tier `C` is manual, sampled, or proxy evidence.
- `Evidence Confidence`: a normalized confidence score in the range `[0.0, 1.0]` representing freshness, reproducibility, and source quality of the evidence.
- `Hypothesis Card`: the formal record of an intended change, expected metric deltas, business validation signal, guardrails, and rollback trigger.
- `Guardrail`: a limit on acceptable negative delta for a non-target metric or critical system property.
- `Criticality Profile`: the operating profile that determines evidence strictness, waiver policy, and gate posture for the system.
- `Automation Actor`: a human, script, CI job, or AI agent that performs analysis, change generation, or validation within a cycle.
- `Learning Artifact`: a persisted insight such as a glossary delta, decision log entry, pattern, anti-pattern, or playbook update derived from a cycle.
- `Stabilization`: a state in which the system maintains the target IOSM-Index for a configured number of consecutive cycles with no blocking gate failures, no blocking guardrail violations, and sufficient decision confidence.
- `Metric Drift`: repeated decline of a canonical metric across consecutive cycles.

## 4. Values and Axioms

- Clarity is a prerequisite for speed.
- Efficiency is defined as performance x resilience.
- Simplicity reduces risk, operational cost, and onboarding friction.
- Modularity is the primary mechanism for safe long-term evolution.
- Metrics take precedence over opinion in gate evaluation.
- Economics of change governs prioritization.
- Improvements are incomplete until validated by business, operational, or user feedback.
- A successful change is one that improves its target outcome without causing hidden damage elsewhere.
- Automation must increase auditability, not reduce it.
- Learning closure is part of the methodology, not an afterthought.

These axioms are normative for interpretation of the methodology. Implementations MAY vary in tooling, but they MUST preserve these semantics.

## 5. Conformance

An implementation may claim to be `IOSM-conformant` only if all of the following are true:

- it executes the phases in the exact order `Improve -> Optimize -> Shrink -> Modularize`;
- it evaluates a Quality Gate after every phase;
- it records a Hypothesis Card for every selected goal;
- it records an explicit Cycle Scope for every cycle;
- it validates cycle capacity before phase execution;
- when multiple hypotheses exist, it records a cycle-level interaction assessment before execution;
- it enforces guardrails against unacceptable cross-metric regression;
- it computes the six canonical metrics: `semantic`, `logic`, `performance`, `simplicity`, `modularity`, and `flow`;
- it calculates the IOSM-Index using weights that sum to `1.0`;
- it records evidence tier and evidence confidence for each canonical metric;
- it produces and persists evidence artifacts for each cycle;
- it persists learning artifacts or a justified `no_learning_delta` decision for each cycle;
- it maintains a versioned Invariant Catalog and applies Gate I against a baseline or approved delta of that catalog;
- it defines at least two fitness functions for the system;
- it records waivers explicitly and never treats a waived failure as an unqualified pass;
- it does not declare stabilization while a blocking waiver remains open;
- if automation actors are used, it records their provenance and approval path.

An implementation SHOULD automate gate evaluation and report generation. An implementation MAY automate phase execution, but automation is not required for conformance.

## 6. Required Artifacts

Each conformant implementation MUST maintain the following artifacts.

| Artifact | Purpose | Minimum Contents |
| --- | --- | --- |
| `iosm.yaml` | Method configuration | thresholds, weights, cycle policy, reporting policy |
| Baseline Report | Pre-change reference | timestamps, scope, cycle scope, delivery boundary, baseline measurements, source systems |
| Hypothesis Card Set | Change intent | goal id, expected delta, guardrails, business signal, rollback trigger, owner |
| Invariant Catalog | Logic baseline | invariant ids, descriptions, owners, status, version |
| Phase Report | Per-phase evidence | inputs, actions taken, outputs, gate measurements, pass/fail |
| Cycle Report | End-of-cycle record | cycle scope, goals, gate results, metrics, confidences, IOSM-Index, decision |
| Metrics History | Trend analysis | per-cycle normalized metrics, confidences, and raw measurements |
| Waiver Register | Governance | waiver id, scope, rationale, expiry, owner, status |
| Contract Catalog | Boundary control | public interfaces, schemas, consumer/provider mapping |
| Decision Log | Governance memory | accepted tradeoffs, rejected options, approval path |
| Pattern Library | Reuse | successful plays, preconditions, expected deltas |

Artifacts MAY be stored as Markdown, JSON, YAML, or database records. They MUST be serializable for audit and comparison across cycles.

## 7. Configuration Model

### 7.1 Required Configuration Semantics

The configuration model MUST define:

- planning behavior;
- cycle stopping policy;
- cycle capacity policy;
- Quality Gate thresholds;
- cross-metric guardrails;
- evidence-confidence policy;
- metric target policy;
- waiver policy;
- IOSM-Index weights;
- reporting behavior;
- automation governance behavior.

Threshold semantics:

- normalized thresholds MUST be in the range `[0.0, 1.0]`;
- time thresholds MUST use explicit units;
- count thresholds MUST be integers;
- weights MUST sum to `1.0`;
- `max_iterations_per_phase` MUST be greater than or equal to `1`;
- guardrail budgets MUST be zero or positive.

### 7.2 Canonical Example

```yaml
iosm:
  metadata:
    system_name: billing-api
    scope: service
    criticality_profile: standard
    delivery_boundary: billing-api-service
  planning:
    use_economic_decision: true
    prioritization_formula: wsjf_confidence
    min_confidence: 0.70
    hypothesis_required: true
    cycle_scope_required: true
  cycle_capacity:
    max_goals: 3
    max_scope_items: 5
    max_expected_change_surface: 3
  cycle_policy:
    max_iterations_per_phase: 3
    stabilization:
      target_index: 0.98
      consecutive_cycles: 3
      global_metric_floor: 0.60
      max_consecutive_unexplained_declines: 2
      metric_floors:
        logic: 0.95
        performance: 0.85
  quality_gates:
    gate_I:
      semantic_min: 0.95
      logical_consistency_min: 1.00
      duplication_max: 0.05
    gate_O:
      latency_ms:
        p50_max: 60
        p95_max: 150
        p99_max: 250
      error_budget_respected: true
      chaos_pass_rate_min: 1.00
    gate_S:
      at_least_one_dimension: true
      api_surface_reduction_min: 0.20
      dependency_hygiene_min: 0.95
      onboarding_time_minutes_max: 15
      regression_budget_max: 0
    gate_M:
      change_surface_max: 3
      coupling_max: 0.20
      cohesion_min: 0.80
      contracts_pass: true
  guardrails:
    max_negative_delta:
      semantic: 0.02
      logic: 0.00
      performance: 0.03
      simplicity: 0.03
      modularity: 0.02
      flow: 0.02
  evidence:
    min_decision_confidence: 0.80
    freshness_sla_hours:
      tier_a: 24
      tier_b: 168
    min_metric_confidence:
      semantic: 0.70
      logic: 0.90
      performance: 0.90
      simplicity: 0.70
      modularity: 0.70
      flow: 0.80
  waivers:
    max_duration_days: 14
    require_human_approval: true
  metric_targets:
    semantic:
      glossary_coverage_min: 0.95
      naming_consistency_min: 0.95
      ambiguity_ratio_max: 0.05
    logic:
      invariant_pass_rate_min: 1.00
    performance:
      latency_ms:
        p50_max: 60
        p95_max: 150
        p99_max: 250
    simplicity:
      onboarding_time_minutes_max: 15
    modularity:
      change_surface_max: 3
    flow:
      lead_time_hours_max: 24
      deploy_frequency_per_week_min: 5
      change_failure_rate_max: 0.15
      review_latency_hours_max: 24
  index:
    weights:
      semantic: 0.15
      logic: 0.20
      performance: 0.25
      simplicity: 0.15
      modularity: 0.15
      flow: 0.10
  automation:
    allow_agents: true
    human_approval_required_for:
      - waivers
      - public_contract_changes
      - threshold_relaxation
      - destructive_data_changes
  reporting:
    persist_history: true
    output_format: json
  learning:
    update_pattern_library: true
    update_decision_log: true
    update_glossary: true
```

### 7.3 Validation Rules

```pseudocode
FUNCTION VALIDATE_CONFIG(config):
    ASSERT SUM(config.index.weights.*) = 1.0
    ASSERT config.planning.cycle_scope_required = true
    ASSERT config.cycle_capacity.max_goals >= 1
    ASSERT config.cycle_capacity.max_scope_items >= 1
    ASSERT config.cycle_capacity.max_expected_change_surface >= 1
    ASSERT config.cycle_policy.max_iterations_per_phase >= 1
    ASSERT 0.0 <= config.cycle_policy.stabilization.target_index <= 1.0
    ASSERT config.cycle_policy.stabilization.consecutive_cycles >= 1
    ASSERT config.cycle_policy.stabilization.max_consecutive_unexplained_declines >= 0
    ASSERT 0.0 <= config.cycle_policy.stabilization.global_metric_floor <= 1.0
    ASSERT config.waivers.max_duration_days >= 1
    ASSERT METRIC_TARGETS_DECLARED(config.metric_targets)
    ASSERT ALL_NORMALIZED_THRESHOLDS_IN_RANGE(config)
    ASSERT ALL_NORMALIZED_THRESHOLDS_IN_RANGE(config.cycle_policy.stabilization.metric_floors)
    ASSERT ALL_GUARDRAILS_ARE_NON_NEGATIVE(config.guardrails)
    ASSERT ALL_CONFIDENCE_THRESHOLDS_IN_RANGE(config.evidence)
```

## 8. Operating Profiles and Adaptive Thresholds

### 8.1 Canonical Profiles

IOSM supports operating profiles so the methodology can remain strict while still adapting to context.

Canonical profiles:

- `standard`: default profile for most production systems.
- `critical`: for safety-sensitive, revenue-critical, regulated, or high-blast-radius systems.
- `exploratory`: for discovery, prototyping, or innovation work that is not yet eligible for stabilization claims.

Profile semantics:

- `standard` MUST use canonical semantics with configurable thresholds.
- `critical` MUST require stricter evidence confidence for `logic` and `performance`, shorter waiver duration, and no positive interpretation of incomplete evidence.
- `critical` SHOULD set `waivers.max_duration_days` lower than the default standard profile.
- `exploratory` MAY use relaxed thresholds for non-safety metrics, but it MUST preserve `logic` and contract safety and it MUST NOT declare stabilization.

### 8.2 Metric Target Calibration Contract

All normalization targets MUST be declared in `iosm.yaml` under `metric_targets`.

Rules:

- a conformant implementation MUST be able to trace every normalization target back to configuration or an approved adaptive-threshold rule;
- targets MUST NOT be loosened without human approval and a Decision Log entry;
- targets MAY be tightened through the adaptive-threshold mechanism only if that mechanism is explicitly enabled;
- targets used in reporting MUST include their source: `configured`, `adapted`, or `waived`.

### 8.3 Adaptive Threshold Rule

Thresholds MAY be tightened automatically after repeated stable cycles. Thresholds MUST NOT be loosened automatically.

Rules:

- automatic tightening MUST be monotonic;
- automatic tightening SHOULD use successful historical cycles only;
- automatic loosening MUST require human approval and a Decision Log entry;
- adaptive rules MUST be explicit in configuration or policy.

Canonical tightening proposal:

```pseudocode
FUNCTION PROPOSE_THRESHOLD_TIGHTENING(history, metric_name, current_threshold, metric_kind, safety_margin):
    successes <- FILTER(
        history,
        cycle -> NOT cycle.has_blocking_failure AND NOT cycle.has_guardrail_violation AND NOT cycle.incomplete
    )
    stable_sample <- TAKE_LAST(successes, 5)
    IF SIZE(stable_sample) < 5 THEN RETURN current_threshold

    median_value <- MEDIAN(MAP(stable_sample, cycle -> cycle.values[metric_name]))

    IF metric_kind = HIGHER_IS_BETTER:
        RETURN MAX(current_threshold, median_value - safety_margin)
    IF metric_kind = LOWER_IS_BETTER:
        RETURN MIN(current_threshold, median_value + safety_margin)
```

## 9. Planning and Economic Decision

IOSM is not only a technical optimization loop. A cycle MUST begin by selecting economically relevant goals.

Each backlog item SHOULD be scored using the following factors:

- `business_value`: expected economic or user impact;
- `urgency`: time sensitivity or deadline pressure;
- `risk_reduction`: expected reduction in operational, security, or delivery risk;
- `opportunity_enablement`: expected unlocking of future work;
- `effort`: estimated implementation cost;
- `confidence`: confidence in the estimates.

Canonical prioritization formula:

```pseudocode
FUNCTION ECONOMIC_SCORE(item):
    numerator <- item.business_value + item.urgency + item.risk_reduction + item.opportunity_enablement
    denominator <- MAX(item.effort, 1)
    RETURN (numerator / denominator) * item.confidence
```

Selection rules:

- goals MUST be ordered by descending economic score;
- items below `min_confidence` SHOULD be deferred or re-estimated;
- goals selected for a cycle SHOULD fit within one cycle's operational capacity;
- a cycle MUST NOT start without at least one selected goal unless it is an explicitly scheduled audit cycle;
- critical profile systems SHOULD include at least one risk-reducing goal in every non-audit cycle.

### 9.1 Cycle Scope

Each cycle MUST declare a Cycle Scope before phase execution.

Cycle Scope rules:

- Cycle Scope MUST identify the subset of the system intentionally targeted by the cycle;
- Cycle Scope MAY include modules, services, bounded contexts, public contracts, or data domains;
- metrics and reports MAY still observe whole-system effects, but the cycle MUST distinguish in-scope change from system-wide observation;
- `change_surface` MUST be evaluated relative to the declared Cycle Scope and any out-of-scope components that must change with it;
- a cycle MUST NOT claim local improvement while silently expanding scope without updating the Cycle Scope declaration.

Canonical shape:

```yaml
cycle_scope:
  modules:
    - checkout-service
    - pricing-service
  contracts:
    - checkout-api-v1
  rationale: "latency path optimization and API simplification"
```

### 9.2 Cycle Capacity

Each cycle MUST fit within declared Cycle Capacity.

Cycle Capacity rules:

- a cycle MUST NOT admit more goals than `cycle_capacity.max_goals`;
- a cycle MUST NOT admit more scope items than `cycle_capacity.max_scope_items`;
- a cycle MUST NOT begin if estimated coordinated change exceeds `cycle_capacity.max_expected_change_surface`;
- capacity validation MUST occur before phase execution;
- if candidate work exceeds capacity, the implementation MUST reduce the cycle plan rather than silently overfill it.

Canonical validation:

```pseudocode
FUNCTION VALIDATE_CYCLE_CAPACITY(goals, cycle_scope, hypotheses, cycle_capacity):
    goal_count <- SIZE(goals)
    scope_size <- COUNT_SCOPE_ITEMS(cycle_scope)
    expected_change_surface <- ESTIMATE_EXPECTED_CHANGE_SURFACE(hypotheses, cycle_scope)

    pass <- (
        goal_count <= cycle_capacity.max_goals AND
        scope_size <= cycle_capacity.max_scope_items AND
        expected_change_surface <= cycle_capacity.max_expected_change_surface
    )

    RETURN {pass, goal_count, scope_size, expected_change_surface}
```

## 10. Change Hypothesis Protocol

IOSM treats change as a falsifiable hypothesis, not as a vague activity.

Each selected goal MUST have a Hypothesis Card that defines:

- hypothesis id;
- goal id and owner;
- change statement;
- target metrics and expected positive deltas;
- allowed negative deltas for non-target metrics;
- expected business or user validation signal;
- validation method and observation window;
- rollback trigger;
- confidence in the hypothesis.

Canonical Hypothesis Card shape:

```yaml
hypothesis:
  id: hyp-latency-001
  goal_id: reduce-checkout-latency
  owner: payments-team
  statement: "If cache miss paths are removed, p95 latency will decrease without harming API clarity."
  expected_positive_delta:
    performance: 0.05
  allowed_negative_delta:
    semantic: 0.00
    logic: 0.00
    simplicity: 0.02
    modularity: 0.01
    flow: 0.01
  expected_business_signal:
    metric: checkout_conversion
    direction: up
  validation:
    method: production_observation
    window: 7d
  rollback_trigger:
    - contracts_break
    - change_failure_rate_up_10_percent
  confidence: 0.80
```

Guardrail rule:

- a cycle MAY improve one target metric while allowing limited non-target regression;
- any regression beyond the declared guardrail budget MUST fail the cycle unless an explicit waiver exists;
- `logic` and contract safety SHOULD default to zero negative budget.

Budget composition rule:

- global guardrails define the maximum allowed negative delta at methodology level;
- Hypothesis Cards MAY define stricter budgets for the metrics they touch;
- a hypothesis MUST NOT define a softer budget than the global guardrail for the same metric;
- when multiple hypotheses exist in one cycle, the cycle MUST derive a single effective cycle budget before phase execution.

Cross-hypothesis interaction rule:

- when a cycle contains more than one hypothesis, the implementation MUST assess interactions between them before phase execution;
- pairwise hypothesis safety is insufficient if the combined cycle budget or expected change surface becomes unsafe;
- interaction findings MUST be recorded in the Cycle Report;
- unresolved blocking interaction conflicts MUST fail planning or force cycle reduction before execution.

Canonical budget composition:

```pseudocode
FUNCTION EFFECTIVE_BUDGET(global_budget, hypothesis_budget):
    RETURN MIN(global_budget, hypothesis_budget)

FUNCTION BUILD_HYPOTHESIS_BUDGET(global_budgets, hypothesis):
    effective <- COPY(global_budgets)

    FOR metric IN effective:
        hypothesis_budget <- COALESCE(hypothesis.allowed_negative_delta[metric], global_budgets[metric])
        effective[metric] <- EFFECTIVE_BUDGET(effective[metric], hypothesis_budget)

    RETURN effective

FUNCTION BUILD_CYCLE_BUDGET(global_budgets, hypotheses):
    cycle_budget <- COPY(global_budgets)

    FOR hypothesis IN hypotheses:
        FOR metric IN cycle_budget:
            hypothesis_budget <- COALESCE(hypothesis.allowed_negative_delta[metric], global_budgets[metric])
            cycle_budget[metric] <- EFFECTIVE_BUDGET(cycle_budget[metric], hypothesis_budget)

    RETURN cycle_budget

FUNCTION ASSESS_HYPOTHESIS_INTERACTIONS(hypotheses, cycle_budget):
    conflicts <- []

    FOR pair IN ALL_PAIRS(hypotheses):
        IF TARGETS_COMPETE(pair.left, pair.right):
            APPEND(conflicts, {type: "target_conflict", pair: pair})
        IF COMBINED_NEGATIVE_BUDGET_EXCEEDS_CYCLE_BUDGET(pair.left, pair.right, cycle_budget):
            APPEND(conflicts, {type: "budget_conflict", pair: pair})
        IF EXPECTED_SCOPE_EXPANSION(pair.left, pair.right):
            APPEND(conflicts, {type: "scope_expansion", pair: pair})

    pass <- IS_EMPTY(conflicts)
    RETURN {pass, conflicts}
```

Canonical guardrail evaluation:

```pseudocode
FUNCTION VALIDATE_GUARDRAILS(before_metrics, after_metrics, budgets):
    violations <- []

    FOR metric IN budgets:
        negative_delta <- before_metrics[metric] - after_metrics[metric]
        IF negative_delta > budgets[metric]:
            APPEND(violations, {metric, negative_delta, budgets[metric]})

    pass <- IS_EMPTY(violations)
    RETURN {pass, violations}
```

Hypothesis validation rule:

```pseudocode
FUNCTION EVALUATE_HYPOTHESIS(card, before_metrics, after_metrics, business_signal, global_budgets):
    target_success <- ALL_TARGET_DELTAS_MET(card.expected_positive_delta, before_metrics, after_metrics)
    guardrails_ok <- VALIDATE_GUARDRAILS(
        before_metrics,
        after_metrics,
        BUILD_HYPOTHESIS_BUDGET(global_budgets, card)
    )
    signal_ok <- MATCHES_EXPECTED_SIGNAL(card.expected_business_signal, business_signal)
    RETURN {pass: target_success AND guardrails_ok.pass AND signal_ok}

FUNCTION EVALUATE_HYPOTHESIS_SET(cards, before_metrics, after_metrics, business_signals, global_budgets):
    results <- []

    FOR card IN cards:
        signal <- business_signals[card.goal_id]
        result <- EVALUATE_HYPOTHESIS(card, before_metrics, after_metrics, signal, global_budgets)
        APPEND(results, {id: card.id, pass: result.pass})

    RETURN results
```

## 11. Cycle Lifecycle

### 11.1 Canonical State Machine

The canonical execution order is fixed:

`PLAN -> HYPOTHESIZE -> IMPROVE -> GATE_I -> OPTIMIZE -> GATE_O -> SHRINK -> GATE_S -> MODULARIZE -> GATE_M -> SCORE -> LEARN -> DECIDE`

If a Quality Gate fails, control returns to the same phase. A phase MUST NOT be skipped without a recorded waiver.

### 11.2 Orchestrator

```pseudocode
ALGORITHM IOSM_ORCHESTRATOR(system, config):
    VALIDATE_CONFIG(config)
    history <- LOAD_HISTORY(system)

    LOOP:
        backlog_items <- GET_BACKLOG_FOR(system)
        prioritized_goals <- PRIORITIZE(backlog_items, config.planning)
        IF IS_EMPTY(prioritized_goals) THEN BREAK

        cycle_scope <- DEFINE_CYCLE_SCOPE(system, prioritized_goals)
        preview_cycle <- PREPARE_CYCLE(system, cycle_scope, prioritized_goals)
        baseline <- CAPTURE_BASELINE(system, cycle_scope)
        baseline_metrics <- COLLECT_METRICS(system, baseline, preview_cycle, cycle_scope)
        hypotheses <- BUILD_HYPOTHESIS_CARDS(prioritized_goals, baseline_metrics)
        capacity_report <- VALIDATE_CYCLE_CAPACITY(
            prioritized_goals,
            cycle_scope,
            hypotheses,
            config.cycle_capacity
        )
        IF NOT capacity_report.pass THEN
            prioritized_goals <- REDUCE_TO_CYCLE_CAPACITY(
                prioritized_goals,
                cycle_scope,
                hypotheses,
                config.cycle_capacity
            )
            cycle_scope <- DEFINE_CYCLE_SCOPE(system, prioritized_goals)
            preview_cycle <- PREPARE_CYCLE(system, cycle_scope, prioritized_goals)
            baseline <- CAPTURE_BASELINE(system, cycle_scope)
            baseline_metrics <- COLLECT_METRICS(system, baseline, preview_cycle, cycle_scope)
            hypotheses <- BUILD_HYPOTHESIS_CARDS(prioritized_goals, baseline_metrics)

        cycle_budget <- BUILD_CYCLE_BUDGET(config.guardrails.max_negative_delta, hypotheses)
        interaction_report <- ASSESS_HYPOTHESIS_INTERACTIONS(hypotheses, cycle_budget)
        IF NOT interaction_report.pass THEN
            RETURN FAIL_CYCLE_PLAN(interaction_report)

        cycle <- START_CYCLE(system, cycle_scope, prioritized_goals)
        cycle.baseline_metrics <- baseline_metrics
        cycle.hypotheses <- hypotheses
        SAVE_HYPOTHESES(cycle, hypotheses)

        FOR phase IN [IMPROVE, OPTIMIZE, SHRINK, MODULARIZE]:
            attempts <- 0
            passed <- false

            WHILE attempts < config.cycle_policy.max_iterations_per_phase AND NOT passed:
                result <- RUN_PHASE(phase, system, cycle_scope, prioritized_goals, baseline, hypotheses)
                report <- EVALUATE_GATE(phase, result, config.quality_gates)
                SAVE_PHASE_REPORT(cycle, phase, result, report)

                IF report.pass THEN
                    passed <- true
                ELSE
                    attempts <- attempts + 1
                    CREATE_REMEDIATION_ITEM(cycle, phase, report)

            IF NOT passed THEN
                IF HAS_ACTIVE_WAIVER(cycle, phase) THEN
                    MARK_PHASE_WAIVED(cycle, phase)
                ELSE
                    RETURN FAIL_CYCLE(cycle, phase)

        after_metrics <- COLLECT_METRICS(system, baseline, cycle, cycle_scope)
        evidence <- COLLECT_EVIDENCE_CONFIDENCE(system, cycle, cycle_scope)
        guardrail_report <- VALIDATE_GUARDRAILS(
            baseline_metrics.values,
            after_metrics.values,
            cycle_budget
        )

        IF NOT guardrail_report.pass AND NOT HAS_ACTIVE_WAIVER(cycle, GUARDRAIL):
            RETURN FAIL_CYCLE(cycle, GUARDRAIL)

        hypothesis_results <- EVALUATE_HYPOTHESIS_SET(
            hypotheses,
            baseline_metrics.values,
            after_metrics.values,
            READ_BUSINESS_SIGNALS(system, cycle_scope, cycle),
            config.guardrails.max_negative_delta
        )

        index <- CALC_IOSM_INDEX(after_metrics.values, config.index.weights)
        decision_confidence <- CALC_DECISION_CONFIDENCE(evidence.metric_confidences, config.index.weights)
        learning <- RUN_LEARNING_CLOSURE(cycle, hypotheses, hypothesis_results)
        decision <- DECIDE_NEXT_CYCLE(
            index,
            decision_confidence,
            after_metrics,
            evidence,
            history,
            cycle,
            config
        )

        SAVE_CYCLE_REPORT(
            cycle,
            after_metrics,
            evidence,
            hypothesis_results,
            guardrail_report,
            capacity_report,
            interaction_report,
            learning,
            index,
            decision_confidence,
            decision
        )
        APPEND(history, {
            cycle_id: cycle.id,
            cycle_scope: cycle_scope,
            index: index,
            decision_confidence: decision_confidence,
            values: after_metrics.values,
            metric_tiers: evidence.metric_tiers,
            metric_deltas: CALCULATE_METRIC_DELTAS(baseline_metrics.values, after_metrics.values),
            decline_coverage: ASSESS_DECLINE_COVERAGE(
                baseline_metrics.values,
                after_metrics.values,
                hypotheses,
                HAS_ACTIVE_BLOCKING_WAIVER(cycle)
            ),
            incomplete: after_metrics.incomplete,
            has_blocking_failure: HAS_BLOCKING_FAILURE(cycle),
            has_guardrail_violation: NOT guardrail_report.pass,
            has_active_blocking_waiver: HAS_ACTIVE_BLOCKING_WAIVER(cycle),
            decision: decision
        })

        IF decision = STOP THEN RETURN {index, after_metrics, history}
```

### 11.3 Failure Semantics

- if a phase fails its gate, remediation MUST occur within the same phase;
- if a phase exceeds `max_iterations_per_phase`, the cycle MUST fail unless an active waiver exists;
- if guardrails are violated, the cycle MUST fail unless an explicit waiver covers the violation;
- a waiver MUST have an owner, rationale, expiry, and explicit scope;
- waived failures MUST remain visible in reports;
- a cycle with waived failures MAY continue, but it MUST NOT be considered stabilized;
- exploratory profile cycles MUST continue or fail, but MUST NOT stop as stabilized.

## 12. Metrics Model

### 12.1 Canonical Metrics

All canonical metrics MUST be normalized to the range `[0.0, 1.0]`.

| Metric | Meaning | Canonical Intent |
| --- | --- | --- |
| `semantic` | structural clarity and terminological coherence | the system says one thing in one way |
| `logic` | invariant correctness and contradiction-free behavior | the system behaves consistently |
| `performance` | latency, reliability, and resilience | the system is fast enough and survives disruption |
| `simplicity` | reduced cognitive load and interface sprawl | the system is easier to use and change |
| `modularity` | decoupling, cohesion, and contract discipline | the system evolves with low blast radius |
| `flow` | delivery throughput and change safety | the organization can ship changes predictably |

Metric boundary policy:

- `semantic` MUST measure terminology, naming, glossary coverage, and conceptual ambiguity only;
- `simplicity` MUST measure interface surface, dependency load, and onboarding friction only;
- evidence that primarily reflects naming or term consistency MUST contribute to `semantic` and MUST NOT also be counted toward `simplicity`;
- evidence that primarily reflects API breadth, dependency sprawl, or onboarding friction MUST contribute to `simplicity` and MUST NOT also be counted toward `semantic`.

### 12.2 Normalization Helpers

```pseudocode
FUNCTION CLAMP01(value):
    RETURN MIN(1.0, MAX(0.0, value))

FUNCTION NORMALIZE_HIGHER_IS_BETTER(actual, target):
    RETURN CLAMP01(actual / target)

FUNCTION NORMALIZE_LOWER_IS_BETTER(actual, target):
    IF actual <= 0 THEN RETURN 1.0
    RETURN CLAMP01(target / actual)
```

All `target` inputs used in normalization MUST be sourced from `metric_targets` or from an approved adaptive-threshold update.

### 12.3 Canonical Metric Formulas

Implementations MAY use equivalent data sources, but they MUST preserve the following semantics.

```pseudocode
FUNCTION MEASURE_SEMANTIC(glossary_coverage, naming_consistency, ambiguity_inverse):
    RETURN ROUND((glossary_coverage + naming_consistency + ambiguity_inverse) / 3, 3)

FUNCTION MEASURE_LOGIC(passed_invariants, total_invariants):
    RETURN ROUND(passed_invariants / MAX(total_invariants, 1), 3)

FUNCTION MEASURE_PERFORMANCE(latency_score, reliability_score, resilience_score):
    RETURN ROUND(0.50 * latency_score + 0.30 * reliability_score + 0.20 * resilience_score, 3)

FUNCTION MEASURE_SIMPLICITY(api_surface_score, dependency_hygiene, onboarding_score):
    RETURN ROUND(0.40 * api_surface_score + 0.30 * dependency_hygiene + 0.30 * onboarding_score, 3)

FUNCTION MEASURE_MODULARITY(coupling_score, cohesion_score, contract_score, change_surface_score):
    RETURN ROUND(0.35 * coupling_score + 0.25 * cohesion_score + 0.20 * contract_score + 0.20 * change_surface_score, 3)

FUNCTION MEASURE_FLOW(lead_time_score, deploy_frequency_score, change_failure_score, review_latency_score):
    RETURN ROUND(0.35 * lead_time_score + 0.25 * deploy_frequency_score + 0.25 * change_failure_score + 0.15 * review_latency_score, 3)
```

### 12.4 Raw Measurement Mapping

Canonical mappings SHOULD be implemented as follows:

- `glossary_coverage`: fraction of key domain terms with approved definitions.
- `naming_consistency`: fraction of sampled identifiers that match naming rules and glossary.
- `ambiguity_inverse`: `1 - ambiguity_ratio`.
- `latency_score`: average of normalized `p50`, `p95`, and `p99`.
- `reliability_score`: `1.0` when the error budget is respected, otherwise `0.0`.
- `resilience_score`: chaos test pass rate.
- `api_surface_score`: normalized reduction in public endpoints, commands, or externally visible operations.
- `dependency_hygiene`: `1 - (unused_or_shadow_dependencies / total_dependencies)`.
- `onboarding_score`: normalized lower-is-better score for onboarding time.
- `coupling_score`: normalized inverse of measured inter-module coupling.
- `cohesion_score`: normalized cohesion of bounded components.
- `contract_score`: `1.0` when all required contracts pass, otherwise `0.0`.
- `change_surface_score`: normalized lower-is-better score for modules changed together.
- `lead_time_score`, `deploy_frequency_score`, `change_failure_score`, and `review_latency_score`: normalized delivery flow indicators.

Flow boundary rule:

- `flow` MUST be computed from a declared Delivery Boundary;
- the Delivery Boundary MUST be recorded in the Baseline Report and Cycle Report;
- cross-system comparison of `flow` MUST NOT be performed unless the compared systems use declared and materially equivalent delivery boundaries.

### 12.5 Canonical Collection Shape

```pseudocode
FUNCTION COLLECT_METRICS(system, baseline, cycle, cycle_scope):
    semantic <- MEASURE_SEMANTIC_FROM_SYSTEM(system)
    logic <- MEASURE_LOGIC_FROM_SYSTEM(system)
    performance <- MEASURE_PERFORMANCE_FROM_SYSTEM(system)
    simplicity <- MEASURE_SIMPLICITY_FROM_SYSTEM(system)
    modularity <- MEASURE_MODULARITY_FROM_SYSTEM(system)
    flow <- MEASURE_FLOW_FROM_SYSTEM(system)

    values <- {semantic, logic, performance, simplicity, modularity, flow}
    raw <- LOAD_RAW_MEASUREMENTS(system, cycle)
    incomplete <- ANY_MISSING(values)

    RETURN {values, raw, incomplete}
```

### 12.6 Mandatory Completeness Rule

A conformant cycle MUST collect all six canonical metrics. If one or more metric inputs are unavailable, the cycle MUST be marked `incomplete` and MUST NOT be used to declare stabilization.

## 13. Evidence Confidence and Decision Quality

### 13.1 Evidence Tiers

Each canonical metric MUST record its highest-quality supporting evidence tier:

- Tier `A`: direct, automated, production-grade or authoritative primary evidence;
- Tier `B`: automated synthetic, staging, sampled, or reconstructed evidence;
- Tier `C`: manual, inferred, proxy, or partially reproducible evidence.

### 13.2 Evidence Confidence

Evidence confidence combines source quality, freshness, and reproducibility.

Canonical tier bases:

- Tier `A` = `1.00`
- Tier `B` = `0.80`
- Tier `C` = `0.60`

Canonical freshness scoring:

- `1.00` if evidence age is less than or equal to `24h`;
- `0.80` if evidence age is greater than `24h` and less than or equal to `7d`;
- `0.60` if evidence age is greater than `7d` and less than or equal to `30d`;
- `0.40` if evidence age is greater than `30d`.

Canonical reproducibility scoring:

- `1.00` if the measurement is automatically rerunnable, has at least `3` successful reruns, and observed variance is less than or equal to `5%`;
- `0.80` if the measurement is automatically rerunnable, has at least `2` successful reruns, and observed variance is less than or equal to `10%`;
- `0.60` if the measurement is rerunnable only once, sampled, or partially automated;
- `0.40` if the measurement is manual, inferred, or not independently reproducible.

Canonical scoring helpers:

```pseudocode
FUNCTION FRESHNESS_SCORE(age_hours):
    IF age_hours <= 24 THEN RETURN 1.00
    IF age_hours <= 168 THEN RETURN 0.80
    IF age_hours <= 720 THEN RETURN 0.60
    RETURN 0.40

FUNCTION REPRODUCIBILITY_SCORE(rerun_count, variance_percent, automation_level):
    IF automation_level = FULL AND rerun_count >= 3 AND variance_percent <= 5 THEN RETURN 1.00
    IF automation_level = FULL AND rerun_count >= 2 AND variance_percent <= 10 THEN RETURN 0.80
    IF automation_level IN [PARTIAL, SAMPLED] THEN RETURN 0.60
    RETURN 0.40
```

Canonical confidence formula:

```pseudocode
FUNCTION EVIDENCE_CONFIDENCE(tier_base, freshness_score, reproducibility_score):
    RETURN ROUND(0.50 * tier_base + 0.25 * freshness_score + 0.25 * reproducibility_score, 3)
```

### 13.3 Decision Confidence

Decision confidence is the weighted aggregate of metric confidences.

```pseudocode
FUNCTION CALC_DECISION_CONFIDENCE(metric_confidences, weights):
    RETURN ROUND(
        weights.semantic * metric_confidences.semantic +
        weights.logic * metric_confidences.logic +
        weights.performance * metric_confidences.performance +
        weights.simplicity * metric_confidences.simplicity +
        weights.modularity * metric_confidences.modularity +
        weights.flow * metric_confidences.flow,
        3
    )
```

### 13.4 Decision Rules

- a cycle MUST record confidence for all six canonical metrics;
- if a metric confidence is below the configured minimum, the cycle MAY continue but MUST NOT be considered stabilization-grade evidence;
- `critical` profile systems MUST use Tier `A` evidence for `logic` and `performance`;
- `exploratory` profile systems MAY use Tier `B` or `C` evidence, but MUST NOT declare stabilization;
- missing confidence data MUST mark the cycle `incomplete`.

Canonical evidence collection:

```pseudocode
FUNCTION COLLECT_EVIDENCE_CONFIDENCE(system, cycle, cycle_scope):
    metric_confidences <- {
        semantic: READ_CONFIDENCE(system, cycle, semantic),
        logic: READ_CONFIDENCE(system, cycle, logic),
        performance: READ_CONFIDENCE(system, cycle, performance),
        simplicity: READ_CONFIDENCE(system, cycle, simplicity),
        modularity: READ_CONFIDENCE(system, cycle, modularity),
        flow: READ_CONFIDENCE(system, cycle, flow)
    }

    metric_tiers <- {
        semantic: READ_TIER(system, cycle, semantic),
        logic: READ_TIER(system, cycle, logic),
        performance: READ_TIER(system, cycle, performance),
        simplicity: READ_TIER(system, cycle, simplicity),
        modularity: READ_TIER(system, cycle, modularity),
        flow: READ_TIER(system, cycle, flow)
    }

    RETURN {metric_confidences, metric_tiers}
```

## 14. IOSM-Index and Stabilization

### 14.1 IOSM-Index

The IOSM-Index is the weighted aggregate of the six canonical metrics.

```pseudocode
FUNCTION CALC_IOSM_INDEX(metrics, weights):
    ASSERT SUM(weights.*) = 1.0
    RETURN ROUND(
        weights.semantic * metrics.semantic +
        weights.logic * metrics.logic +
        weights.performance * metrics.performance +
        weights.simplicity * metrics.simplicity +
        weights.modularity * metrics.modularity +
        weights.flow * metrics.flow,
        3
    )
```

### 14.2 Stabilization Rule

A system MAY be declared `stabilized` only when all of the following are true:

- `IOSM-Index >= target_index`;
- every canonical metric in the stabilization window is greater than or equal to `global_metric_floor`;
- every configured metric-specific floor in the stabilization window is satisfied;
- the target is maintained for `consecutive_cycles` cycles;
- no blocking gate failure exists in those cycles;
- no blocking guardrail violation exists in those cycles;
- no active blocking waiver exists;
- no cycle in the stabilization window is marked `incomplete`;
- decision confidence is greater than or equal to `min_decision_confidence`;
- no canonical metric exceeds the configured limit for consecutive unexplained declines;
- for `critical` profile systems, the stabilization window MUST include at least one cycle with Tier `A` evidence for both `logic` and `performance`;
- for `standard` profile systems, the stabilization window SHOULD include at least one cycle with Tier `A` evidence for both `logic` and `performance`;
- the operating profile is not `exploratory`.

Canonical floor evaluation:

```pseudocode
FUNCTION METRIC_FLOORS_MET(metrics, stabilization_policy):
    FOR metric IN metrics:
        IF metrics[metric] < stabilization_policy.global_metric_floor:
            RETURN false

    FOR metric, floor IN stabilization_policy.metric_floors:
        IF metrics[metric] < floor:
            RETURN false

    RETURN true

FUNCTION CALCULATE_METRIC_DELTAS(before_metrics, after_metrics):
    deltas <- {}

    FOR metric IN after_metrics:
        deltas[metric] <- ROUND(after_metrics[metric] - before_metrics[metric], 3)

    RETURN deltas

FUNCTION ASSESS_DECLINE_COVERAGE(before_metrics, after_metrics, hypotheses, has_active_blocking_waiver):
    coverage <- {}

    FOR metric IN after_metrics:
        delta <- after_metrics[metric] - before_metrics[metric]
        IF delta >= 0 THEN
            coverage[metric] <- true
        ELSE
            coverage[metric] <- (
                ANY(hypotheses, hypothesis -> metric IN KEYS(hypothesis.allowed_negative_delta)) OR
                has_active_blocking_waiver
            )

    RETURN coverage

FUNCTION HAS_EXCESS_UNEXPLAINED_DRIFT(cycles, max_consecutive_unexplained_declines):
    FOR metric IN CANONICAL_METRICS:
        streak <- 0

        FOR cycle IN REVERSE(cycles):
            IF cycle.metric_deltas[metric] < 0 AND NOT cycle.decline_coverage[metric] THEN
                streak <- streak + 1
            ELSE
                BREAK

        IF streak > max_consecutive_unexplained_declines THEN
            RETURN true

    RETURN false
```

### 14.3 Next-Cycle Decision

```pseudocode
FUNCTION DECIDE_NEXT_CYCLE(index, decision_confidence, metrics, evidence, history, cycle, config):
    current <- {
        index: index,
        values: metrics.values,
        metric_tiers: evidence.metric_tiers,
        metric_deltas: CALCULATE_METRIC_DELTAS(cycle.baseline_metrics.values, metrics.values),
        decline_coverage: ASSESS_DECLINE_COVERAGE(
            cycle.baseline_metrics.values,
            metrics.values,
            cycle.hypotheses,
            HAS_ACTIVE_BLOCKING_WAIVER(cycle)
        ),
        incomplete: metrics.incomplete,
        has_blocking_failure: HAS_BLOCKING_FAILURE(cycle),
        has_guardrail_violation: HAS_GUARDRAIL_VIOLATION(cycle),
        has_active_blocking_waiver: HAS_ACTIVE_BLOCKING_WAIVER(cycle)
    }
    recent <- TAKE_LAST(history + [current], config.cycle_policy.stabilization.consecutive_cycles)

    IF config.metadata.criticality_profile = "exploratory" THEN RETURN CONTINUE
    IF metrics.incomplete THEN RETURN CONTINUE
    IF decision_confidence < config.evidence.min_decision_confidence THEN RETURN CONTINUE
    IF ANY(recent.has_blocking_failure) THEN RETURN CONTINUE
    IF ANY(recent.has_guardrail_violation) THEN RETURN CONTINUE
    IF ANY(recent.has_active_blocking_waiver) THEN RETURN CONTINUE
    IF HAS_EXCESS_UNEXPLAINED_DRIFT(
        history + [current],
        config.cycle_policy.stabilization.max_consecutive_unexplained_declines
    ) THEN RETURN CONTINUE
    IF NOT ALL(MAP(recent, cycle -> METRIC_FLOORS_MET(cycle.values, config.cycle_policy.stabilization))) THEN RETURN CONTINUE
    IF NOT EVIDENCE_THRESHOLDS_MET(evidence, config.evidence.min_metric_confidence) THEN RETURN CONTINUE
    IF config.metadata.criticality_profile = "critical" AND NOT HAS_TIER_A_WINDOW(recent, [logic, performance]) THEN RETURN CONTINUE
    IF ALL(recent.index >= config.cycle_policy.stabilization.target_index) THEN RETURN STOP
    RETURN CONTINUE
```

## 15. Phases and Quality Gates

### 15.1 Improve

Objective: make the system understandable, coherent, and contradiction-resistant before attempting deeper optimization or restructuring.

Required activities:

- build or refine the domain glossary;
- enforce naming conventions aligned with the glossary;
- detect and remove duplications;
- define and instrument critical invariants.

Required outputs:

- glossary or glossary delta;
- duplication map;
- invariant catalog;
- Improve phase measurements;
- links from the work performed to one or more Hypothesis Cards.

Invariant catalog governance:

- a baseline Invariant Catalog MUST exist before Gate I evaluation;
- Improve MAY add or refine invariants, but it MUST NOT silently remove existing invariants;
- removal or semantic weakening of an invariant MUST require a waiver or explicit human-approved Decision Log entry;
- Gate I logical consistency MUST be evaluated against the baseline Invariant Catalog plus any approved additive delta.

Canonical algorithm:

```pseudocode
FUNCTION RUN_IMPROVE(system, cycle_scope, goals, baseline, hypotheses):
    baseline_invariants <- LOAD_BASELINE_INVARIANT_CATALOG(system)
    glossary <- BUILD_GLOSSARY(system)
    system <- APPLY_NAMING_CONVENTIONS(system, glossary)
    duplicates <- FIND_DUPLICATIONS(system)
    system <- ELIMINATE_DUPLICATIONS(system, duplicates)
    invariants <- EXTEND_INVARIANT_CATALOG(baseline_invariants, goals)
    system <- INSTRUMENT_ASSERTIONS(system, invariants)
    invariant_catalog_valid <- VALIDATE_INVARIANT_CATALOG_DELTA(baseline_invariants, invariants)
    glossary_coverage <- MEASURE_GLOSSARY_COVERAGE(glossary)
    naming_consistency <- MEASURE_NAMING_CONSISTENCY(system, glossary)
    ambiguity_inverse <- MEASURE_AMBIGUITY_INVERSE(system)
    semantic <- MEASURE_SEMANTIC(glossary_coverage, naming_consistency, ambiguity_inverse)
    logical_consistency <- CHECK_INVARIANTS(system, invariants)
    duplication <- MEASURE_DUPLICATION(system)
    RETURN {semantic, logical_consistency, duplication, invariant_catalog_valid}
```

Gate I:

```pseudocode
FUNCTION EVALUATE_GATE_I(result, gate):
    pass <- (
        result.invariant_catalog_valid = true AND
        result.semantic >= gate.semantic_min AND
        result.logical_consistency >= gate.logical_consistency_min AND
        result.duplication <= gate.duplication_max
    )
    RETURN {pass, result}
```

### 15.2 Optimize

Objective: improve speed and resilience using measured bottlenecks and explicit reliability constraints.

Entry criteria:

- baseline performance measurements exist;
- Improve has passed or has an explicit waiver.

Required activities:

- capture baseline profiles;
- identify bottlenecks;
- apply targeted optimizations;
- apply resilience patterns;
- run chaos tests and benchmarks.

Required outputs:

- baseline profile;
- bottleneck list;
- benchmark summary;
- resilience and chaos results;
- delta against the relevant Hypothesis Cards.

Canonical algorithm:

```pseudocode
FUNCTION RUN_OPTIMIZE(system, cycle_scope, goals, baseline, hypotheses):
    baseline_profile <- PROFILE(system)
    bottlenecks <- IDENTIFY_BOTTLENECKS(baseline_profile)
    system <- APPLY_OPTIMIZATIONS(system, bottlenecks)
    system <- APPLY_RESILIENCE_PATTERNS(system)
    chaos_pass_rate <- RUN_CHAOS_TESTS(system)
    latency_ms <- RUN_BENCHMARKS(system)
    error_budget_respected <- CHECK_ERROR_BUDGET(system)
    RETURN {latency_ms, error_budget_respected, chaos_pass_rate}
```

Gate O:

```pseudocode
FUNCTION EVALUATE_GATE_O(result, gate):
    pass <- (
        result.latency_ms.p50 <= gate.latency_ms.p50_max AND
        result.latency_ms.p95 <= gate.latency_ms.p95_max AND
        result.latency_ms.p99 <= gate.latency_ms.p99_max AND
        result.error_budget_respected = gate.error_budget_respected AND
        result.chaos_pass_rate >= gate.chaos_pass_rate_min
    )
    RETURN {pass, result}
```

### 15.3 Shrink

Objective: reduce unnecessary surface area, dependency sprawl, and onboarding cost without functional regression.

Interpretation rule:

- Shrink MUST reduce at least one surface dimension materially: public API surface, dependency load, or onboarding friction;
- Shrink MUST NOT be treated as a mandatory API-reduction exercise when the better simplification comes from dependency or onboarding cleanup.

Required activities:

- detect redundant or overlapping APIs;
- remove or merge low-value interfaces;
- inventory and remove unused dependencies;
- measure onboarding time and cognitive load indicators.

Required outputs:

- API reduction delta;
- dependency cleanup delta;
- regression report;
- onboarding measurement;
- delta against the relevant Hypothesis Cards.

Canonical algorithm:

```pseudocode
FUNCTION RUN_SHRINK(system, cycle_scope, goals, baseline, hypotheses):
    redundant <- FIND_REDUNDANT_APIS(system)
    system <- REMOVE_OR_MERGE_APIS(system, redundant)
    deps <- LIST_DEPENDENCIES(system)
    system <- REMOVE_UNUSED_DEPS(system, deps)
    api_reduction <- MEASURE_API_SURFACE_REDUCTION(system)
    onboarding_time <- MEASURE_ONBOARDING(system)
    regression <- MEASURE_REGRESSION(system)
    dependency_hygiene <- MEASURE_DEPENDENCY_HYGIENE(system)
    RETURN {api_reduction, dependency_hygiene, regression, onboarding_time}
```

Gate S:

```pseudocode
FUNCTION EVALUATE_GATE_S(result, gate):
    surface_ok <- result.api_reduction >= gate.api_surface_reduction_min
    dependency_ok <- result.dependency_hygiene >= gate.dependency_hygiene_min
    onboarding_ok <- result.onboarding_time <= gate.onboarding_time_minutes_max

    pass <- (
        (surface_ok OR dependency_ok OR onboarding_ok) AND
        result.regression <= gate.regression_budget_max
    )
    RETURN {pass, result}
```

### 15.4 Modularize

Objective: reduce blast radius and enable safe independent evolution through clear partitions and contracts.

Required activities:

- build the dependency graph;
- identify or refine partitions;
- refactor toward lower coupling and clearer ownership;
- define and test explicit contracts.

Required outputs:

- dependency graph;
- partition definition;
- contract catalog or contract delta;
- modularity measurements;
- delta against the relevant Hypothesis Cards.

Canonical algorithm:

```pseudocode
FUNCTION RUN_MODULARIZE(system, cycle_scope, goals, baseline, hypotheses):
    graph <- BUILD_DEP_GRAPH(system)
    partitions <- PARTITION_GRAPH(graph)
    system <- REFACTOR_TO_PARTITIONS(system, partitions)
    contracts <- DEFINE_CONTRACTS(system)
    tests <- RUN_CONTRACT_TESTS(system, contracts)
    contracts_pass <- ALL_PASS(tests)
    change_surface <- MEASURE_CHANGE_SURFACE(system)
    coupling <- MEASURE_COUPLING(system)
    cohesion <- MEASURE_COHESION(system)
    RETURN {contracts_pass, change_surface, coupling, cohesion}
```

Gate M:

```pseudocode
FUNCTION EVALUATE_GATE_M(result, gate):
    pass <- (
        result.change_surface <= gate.change_surface_max AND
        result.coupling <= gate.coupling_max AND
        result.cohesion >= gate.cohesion_min AND
        result.contracts_pass = gate.contracts_pass
    )
    RETURN {pass, result}
```

### 15.5 Gate Integrity Rules

- a failed gate MUST create explicit remediation work or terminate the cycle;
- a later phase MUST NOT compensate for a failed earlier gate without either passing that earlier gate or recording a waiver;
- phase outputs MUST be attached to the phase report;
- gate thresholds MAY be stricter than the canonical example, but they MUST NOT change the meaning of the gate;
- a gate pass does not override a guardrail violation;
- a phase SHOULD report which Hypothesis Cards it materially advanced.

## 16. Fitness Functions

Fitness Functions are executable constraints that continuously guard architecture and operating assumptions.

Rules:

- a conformant implementation MUST define at least `2` fitness functions;
- a conformant implementation SHOULD run fitness functions at least on every merge to the main integration branch;
- blocking fitness functions MUST fail the build or deployment pipeline;
- non-blocking fitness functions MUST still be reported and trended;
- each fitness function SHOULD declare `id`, `owner`, `severity`, and `scope`;
- systems with public APIs MUST include `stable_interfaces`;
- critical profile systems SHOULD treat interface stability and layering violations as blocking.

Canonical examples:

```pseudocode
FITNESS check_bundle_size(max_mb):
    size <- BUILD_ARTIFACT_SIZE()
    ASSERT size <= max_mb

FITNESS enforce_layering():
    graph <- BUILD_DEP_GRAPH()
    ASSERT NO_EDGE_FROM(layer=ui TO layer=data)

FITNESS stable_interfaces():
    diff <- OPENAPI_DIFF(prev, curr)
    ASSERT NO_BREAKING_CHANGES(diff)
```

Recommended metadata shape:

```yaml
fitness_functions:
  - id: layering
    severity: blocking
    owner: architecture
    scope: repository
  - id: stable_interfaces
    severity: blocking
    owner: api-platform
    scope: public-api
```

## 17. Agent and Automation Governance

IOSM explicitly permits automation actors, including AI agents, but treats them as governed actors rather than implicit authority.

Automation roles:

- `observer`: collects metrics, evidence, and reports;
- `analyst`: proposes hypotheses, prioritization, and remediation;
- `implementer`: generates or applies changes;
- `reviewer`: checks gates, contracts, and evidence integrity.

Governance rules:

- every automation actor MUST be identifiable in the Cycle Report;
- AI-generated changes MUST include provenance, diff scope, and linked evidence;
- public contract changes MUST require human approval;
- waivers MUST require human approval;
- threshold relaxation MUST require human approval;
- destructive data changes MUST require human approval;
- an automation actor MUST NOT approve its own high-risk change in isolation.

Recommended approval matrix:

| Action | Human Approval Required |
| --- | --- |
| Hypothesis creation | No |
| Metric collection | No |
| Code generation for low-risk internal change | No |
| Public contract change | Yes |
| Waiver issuance | Yes |
| Threshold relaxation | Yes |
| Destructive migration or deletion | Yes |

## 18. Anti-Patterns

The following behaviors are considered IOSM anti-patterns:

- selective phase execution;
- optimization without a baseline;
- modularity performed only for appearance while coupling rises;
- endless Improve loops with no measurable delta;
- Shrink actions that break contracts or usability;
- micro-optimizations that degrade developer experience;
- waived failures that remain open indefinitely;
- AI-generated changes with no provenance or no verification path;
- threshold loosening without explicit approval and logged rationale;
- unexplained multi-cycle decline of a canonical metric;
- metric gaming that improves the IOSM-Index while harming business or user outcomes.

Canonical detector:

```pseudocode
FUNCTION DETECT_ANTIPATTERNS(obs):
    IF obs.no_baseline AND obs.optimize THEN FLAG("Optimization without baseline")
    IF obs.skipped_phase THEN FLAG("Skipped phase")
    IF obs.modules_up AND obs.coupling_up THEN FLAG("False modularity")
    IF obs.improve_iterations > obs.max_iterations_per_phase THEN FLAG("Endless Improve cycle")
    IF obs.api_surface_down AND obs.breaking_contracts THEN FLAG("Shrink broke contracts")
    IF obs.open_waivers_expired > 0 THEN FLAG("Expired waiver debt")
    IF obs.ai_change AND NOT obs.provenance_complete THEN FLAG("Unverifiable AI change")
    IF obs.threshold_relaxed AND NOT obs.human_approved THEN FLAG("Unauthorized threshold relaxation")
    IF obs.metric_drift_unexplained THEN FLAG("Unexplained metric drift")
    IF obs.index_up AND obs.business_signal_down THEN FLAG("Metric gaming")
```

An anti-pattern finding SHOULD create a remediation item and SHOULD appear in the cycle report.

## 19. Reporting and Learning Closure

### 19.1 Required Cycle Report Fields

Each cycle report MUST include:

- cycle id;
- system, scope, criticality profile, and delivery boundary;
- cycle scope;
- cycle capacity report;
- observation window;
- selected goals;
- Hypothesis Cards and their outcomes;
- hypothesis interaction assessment;
- phase reports and gate outcomes;
- normalized metrics;
- evidence tiers and evidence confidences;
- raw measurements sufficient to reproduce the metrics;
- guardrail evaluation;
- metric deltas and decline coverage;
- IOSM-Index;
- decision confidence;
- waivers;
- automation actors and approval path;
- anti-pattern findings;
- learning artifacts;
- final decision: `CONTINUE`, `STOP`, or `FAIL`.

### 19.2 Learning Closure

Learning closure is mandatory. Each cycle MUST update or explicitly decline to update:

- glossary delta;
- Decision Log entry;
- Pattern Library entry for successful reusable change plays;
- anti-pattern catalog entry for failed or risky patterns;
- threshold review recommendation when repeated success or repeated failure is observed.

Learning closure rule:

- a cycle is not methodologically complete until its learning artifacts are persisted or a justified `no_learning_delta` decision is recorded.

### 19.3 Example Report Shape

```json
{
  "cycle_id": "iosm-2026-03-05-001",
  "system": "billing-api",
  "scope": "service",
  "criticality_profile": "standard",
  "delivery_boundary": "billing-api-service",
  "cycle_scope": {
    "modules": ["checkout-service", "pricing-service"],
    "contracts": ["checkout-api-v1"]
  },
  "cycle_capacity": {
    "goal_count": 2,
    "scope_size": 3,
    "expected_change_surface": 2,
    "pass": true
  },
  "window": "2026-03-01/2026-03-05",
  "goals": ["reduce checkout latency", "remove redundant admin APIs"],
  "hypotheses": [
    {
      "id": "hyp-latency-001",
      "pass": true
    }
  ],
  "hypothesis_interactions": {
    "pass": true,
    "conflicts": []
  },
  "gates": {
    "gate_I": { "pass": true },
    "gate_O": { "pass": true },
    "gate_S": { "pass": true },
    "gate_M": { "pass": false, "waived": false }
  },
  "metrics": {
    "semantic": 0.96,
    "logic": 1.00,
    "performance": 0.93,
    "simplicity": 0.90,
    "modularity": 0.78,
    "flow": 0.82
  },
  "metric_confidences": {
    "semantic": 0.82,
    "logic": 0.95,
    "performance": 0.94,
    "simplicity": 0.80,
    "modularity": 0.78,
    "flow": 0.88
  },
  "metric_tiers": {
    "semantic": "B",
    "logic": "A",
    "performance": "A",
    "simplicity": "B",
    "modularity": "B",
    "flow": "A"
  },
  "guardrails": {
    "pass": true,
    "violations": []
  },
  "metric_deltas": {
    "semantic": 0.01,
    "logic": 0.00,
    "performance": 0.05,
    "simplicity": 0.02,
    "modularity": -0.01,
    "flow": 0.01
  },
  "decline_coverage": {
    "semantic": true,
    "logic": true,
    "performance": true,
    "simplicity": true,
    "modularity": true,
    "flow": true
  },
  "iosm_index": 0.90,
  "decision_confidence": 0.88,
  "automation_actors": [
    { "type": "ci", "role": "observer" },
    { "type": "agent", "role": "analyst" }
  ],
  "anti_patterns": [],
  "learning_artifacts": [
    "pattern: cache-first-read-path",
    "decision-log: keep public schema unchanged"
  ],
  "decision": "CONTINUE"
}
```

Reports MAY be enriched with links to dashboards, pull requests, benchmark runs, schema diffs, and approval records.

## 20. Scaling and Adoption

IOSM MAY be applied at multiple levels:

- module level;
- service level;
- platform level;
- portfolio level.

Scaling rules:

- lower-level cycles SHOULD feed evidence into higher-level cycles;
- portfolio comparisons SHOULD use the same metric normalization rules;
- target thresholds MAY vary by scope, but the canonical metric meanings MUST remain unchanged;
- exploratory profile results MAY inform future standards, but MUST NOT be treated as stabilization-grade benchmarks.

Recommended adoption roadmap:

- weeks 0-2: establish `gate_I` and `gate_S`, baseline reports, guardrails, and metrics history;
- days 30-60: automate `gate_O`, contract tests, decision logging, and core fitness functions;
- by day 90: compute repeatable IOSM-Index values, decision confidence, and learning closure outputs;
- after stabilization: benchmark across systems, tighten thresholds gradually, and operationalize Pattern Library reuse.

## 21. Conclusion

In this form, IOSM is more than a philosophy. It is a methodology specification with defined artifacts, deterministic gates, canonical metrics, a falsifiable hypothesis model, evidence-confidence rules, explicit decision logic, governed automation, and mandatory learning closure. Teams may adapt thresholds and tooling, but a conformant implementation must preserve the semantics defined in this document.
