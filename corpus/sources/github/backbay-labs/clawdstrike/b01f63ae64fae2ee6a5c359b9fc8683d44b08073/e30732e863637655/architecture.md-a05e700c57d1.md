# Hunt Architecture and Data Model

This document describes the technical architecture of the `clawdstrike hunt` subsystem.
It is intended for implementers building or extending the hunt query engine.

> Note: This architecture doc includes forward-looking design material.
> For current implemented CLI flags/subcommands, use the command reference pages in this section.

## System Architecture

```
+------------------------------------------------------------------+
|                        clawdstrike hunt CLI                       |
|                                                                   |
|  +------------+  +-----------+  +----------+  +----------------+ |
|  | NL Parser  |  | Flag/DSL  |  | SIGMA    |  | Scan Engine    | |
|  | (optional) |  | Parser    |  | Compiler |  | (MCP/Skills)   | |
|  +-----+------+  +-----+-----+  +-----+----+  +-------+--------+ |
|        |              |              |                  |          |
|        +------+-------+------+-------+                 |          |
|               |              |                         |          |
|        +------v------+  +----v----------+   +----------v-------+ |
|        | HuntQuery   |  | Correlation   |   | ScanResult       | |
|        | (structured)|  | Rule          |   | (local findings) | |
|        +------+------+  +----+----------+   +----------+-------+ |
|               |              |                         |          |
+------------------------------------------------------------------+
                |              |                         |
    +-----------v--------------v-------------------------v----------+
    |                     Query Execution Engine                     |
    |                                                               |
    |  +-----------------+  +-------------------+  +--------------+ |
    |  | NATS JetStream  |  | Receipt Store     |  | Local FS     | |
    |  | Consumer        |  | (Spine envelopes) |  | Scanner      | |
    |  +--------+--------+  +--------+----------+  +------+-------+ |
    |           |                    |                     |         |
    +-----------+--------------------+---------------------+---------+
                |                    |                     |
+---------------v--------------------v---------------------v--------+
|                        Data Sources                                |
|                                                                    |
|  +-------------------+  +------------------+  +------------------+ |
|  | CLAWDSTRIKE_      |  | CLAWDSTRIKE_     |  | Agent Config     | |
|  | TETRAGON stream   |  | HUBBLE stream    |  | Files            | |
|  | (kernel events)   |  | (network flows)  |  | (.mcp, .claude,  | |
|  |                   |  |                  |  |  skills, etc.)   | |
|  | Subjects:         |  | Subject:         |  |                  | |
|  | ...tetragon.      |  | ...hubble.       |  +------------------+ |
|  |   process_exec.v1 |  |   flow.v1        |                      |
|  |   process_exit.v1 |  |                  |  +------------------+ |
|  |   process_       |  +------------------+  | Spine Envelope   | |
|  |     kprobe.v1     |                       | Store (receipts, | |
|  +-------------------+                       | policy bundles)  | |
|                                              +------------------+ |
+-------------------------------------------------------------------+
                |                    |                     |
+---------------v--------------------v---------------------v--------+
|                     Output Pipeline                                |
|                                                                    |
|  +-------------+  +-----------+  +----------+  +---------------+  |
|  | TimelineEvent|  | HuntResult|  | HuntReport|  | Format/Render|  |
|  | (unified)   |  | (per-mode)|  | (signed) |  | (table/json/ |  |
|  +-------------+  +-----------+  +----------+  |  timeline)    |  |
|                                                 +---------------+  |
+-------------------------------------------------------------------+
```

## Data Sources and Transport

### NATS JetStream Streams

Hunt queries telemetry from two primary JetStream streams. Both use
`StorageType::File`, `RetentionPolicy::Limits`, and `DiscardPolicy::Old`.

#### Tetragon Stream (`CLAWDSTRIKE_TETRAGON`)

Kernel-level process and syscall telemetry published by the tetragon-bridge.

| Property | Value |
|---|---|
| Stream name | `CLAWDSTRIKE_TETRAGON` |
| Subject pattern | `clawdstrike.spine.envelope.tetragon.>` |
| Subjects | `...tetragon.process_exec.v1`, `...tetragon.process_exit.v1`, `...tetragon.process_kprobe.v1` |
| Fact schema | `clawdstrike.sdr.fact.tetragon_event.v1` |
| Default max bytes | 1 GiB |
| Default max age | 86400s (24h) |
| Default replicas | 1 |

Source: `crates/bridges/tetragon-bridge/src/lib.rs` (`NATS_SUBJECT_PREFIX`, `STREAM_NAME`, `BridgeConfig::default()`)

#### Hubble Stream (`CLAWDSTRIKE_HUBBLE`)

Network flow telemetry published by the hubble-bridge via Cilium Hubble Relay.

| Property | Value |
|---|---|
| Stream name | `CLAWDSTRIKE_HUBBLE` |
| Subject | `clawdstrike.spine.envelope.hubble.flow.v1` |
| Fact schema | `clawdstrike.sdr.fact.hubble_flow.v1` |
| Default max bytes | 1 GiB |
| Default max age | 86400s (24h) |
| Default replicas | 1 |

Source: `crates/bridges/hubble-bridge/src/lib.rs` (`NATS_SUBJECT`, `STREAM_NAME`, `BridgeConfig::default()`)

#### NATS Connection and Auth

Hunt connects to NATS using `spine::nats_transport::connect_with_auth()`, which
supports three authentication methods via `NatsAuthConfig`:

- **Credentials file** (`creds_file: Option<String>`) - `.creds` file path
- **Bearer token** (`token: Option<String>`)
- **NKey seed** (`nkey_seed: Option<String>`)

Source: `crates/libs/spine/src/nats_transport.rs:8-16`

### Spine Envelope Structure

Every telemetry event and receipt is wrapped in a Spine signed envelope
(`aegis.spine.envelope.v1`). Hunt consumes and verifies these envelopes.

```
SignedEnvelope (JSON) {
    schema:              "aegis.spine.envelope.v1"
    issuer:              "aegis:ed25519:<64-hex-pubkey>"
    seq:                 u64                              // monotonic per-issuer
    prev_envelope_hash:  Option<"0x<sha256-hex>">         // hash chain link
    issued_at:           "RFC 3339 timestamp"
    capability_token:    null                              // reserved
    fact:                Value                             // typed payload
    envelope_hash:       "0x<sha256-hex>"                  // SHA-256 of canonical unsigned JSON
    signature:           "0x<ed25519-hex>"                 // Ed25519 over canonical unsigned JSON
}
```

Verification (`spine::verify_envelope()`) strips `envelope_hash` and `signature`,
recomputes canonical JSON via RFC 8785, checks hash integrity, then verifies the
Ed25519 signature against the issuer's public key extracted from the
`aegis:ed25519:<hex>` prefix.

Source: `crates/libs/spine/src/envelope.rs:77-109` (`build_signed_envelope`), `envelope.rs:126-163` (`verify_envelope`)


## Core Data Model

### Tetragon Event Facts

Each Tetragon event is mapped to a fact with schema `clawdstrike.sdr.fact.tetragon_event.v1`.
The mapper (`tetragon-bridge/src/mapper.rs`) produces three event types:

#### `process_exec`

```json
{
    "schema": "clawdstrike.sdr.fact.tetragon_event.v1",
    "event_type": "process_exec",
    "severity": "low|medium|high|critical",
    "node_name": "worker-1",
    "process": {
        "pid": 1234,
        "uid": 0,
        "binary": "/usr/bin/curl",
        "arguments": "--silent https://example.com",
        "cwd": "/app",
        "flags": "",
        "pod": {
            "namespace": "default",
            "name": "agent-pod-0",
            "container": { "id": "...", "name": "...", "image": { "id": "...", "name": "..." } },
            "labels": { "app": "agent" },
            "workload": "agent",
            "workload_kind": "Deployment"
        },
        "docker": ""
    },
    "parent": { ... },
    "ancestors": [ ... ]
}
```

#### `process_exit`

Same process/parent structure, plus:
- `signal` - termination signal
- `status` - exit status code
- Severity is always `low`

#### `process_kprobe`

Same process/parent structure, plus:
- `function_name` - kernel function probed (e.g., `"security_file_open"`)
- `action` - kprobe action taken
- `policy_name` - Tetragon tracing policy that triggered the event
- `message` - human-readable description
- `tags` - string array of classification tags
- `args` - structured kprobe arguments (see below)

Kprobe argument types:
```json
[
    { "label": "file", "value": { "file": { "mount": "...", "path": "/etc/shadow" } } },
    { "label": "sock", "value": { "sock": { "saddr": "10.0.0.1", "daddr": "10.0.0.2", "sport": 12345, "dport": 443, "protocol": "tcp" } } },
    { "label": "path", "value": { "path": { "mount": "...", "path": "/var/run/secrets/..." } } },
    { "label": "buf",  "value": { "string": "..." } },
    { "label": "size", "value": { "size": 4096 } },
    { "label": "fd",   "value": { "int": 3 } }
]
```

Source: `crates/bridges/tetragon-bridge/src/mapper.rs:51-248`

### Tetragon Severity Classification

The bridge classifies events into four severity levels:

| Level | Trigger |
|---|---|
| `critical` | Binary path or kprobe file/path arg matches `SENSITIVE_PATHS` (`/etc/shadow`, `/etc/passwd`, `/etc/sudoers`, `/root/.ssh/`, `/proc/kcore`, `/dev/mem`, `/dev/kmem`, `/var/run/secrets/kubernetes.io/`) |
| `high` | Process exec in `SENSITIVE_NAMESPACES` (`kube-system`, `istio-system`, `cilium`) |
| `medium` | Default for `process_exec`; kprobe with socket argument |
| `low` | Default for `process_exit`; kprobe with no sensitive indicators |

Source: `crates/bridges/tetragon-bridge/src/mapper.rs:34-46`, `mapper.rs:160-218`

### Hubble Flow Facts

Each Hubble flow is mapped to a fact with schema `clawdstrike.sdr.fact.hubble_flow.v1`.

```json
{
    "schema": "clawdstrike.sdr.fact.hubble_flow.v1",
    "severity": "low|medium|high|critical",
    "node_name": "worker-1",
    "verdict": "FORWARDED|DROPPED|ERROR|AUDIT|REDIRECTED|TRACED|TRANSLATED|UNKNOWN",
    "traffic_direction": "INGRESS|EGRESS|UNKNOWN",
    "source": {
        "id": 1,
        "identity": 100,
        "namespace": "default",
        "labels": ["app=agent"],
        "pod_name": "agent-pod-0",
        "workloads": [{ "name": "agent", "kind": "Deployment" }],
        "cluster_name": "prod"
    },
    "destination": { ... },
    "ip": {
        "source": "10.0.0.1",
        "destination": "10.0.0.2",
        "ip_version": "IPv4|IPv6",
        "encrypted": false
    },
    "l4": {
        "protocol": "TCP|UDP|ICMPv4|ICMPv6|SCTP",
        "source_port": 12345,
        "destination_port": 443,
        "flags": { "SYN": true, "ACK": false, "FIN": false, "RST": false, "PSH": false }
    },
    "l7": {
        "flow_type": "REQUEST|RESPONSE|SAMPLE",
        "latency_ns": 5000,
        "record": { "type": "http|dns|kafka", ... }
    },
    "is_reply": false,
    "summary": "TCP Flags: SYN",
    "source_names": [],
    "destination_names": ["api.example.com"]
}
```

L7 record variants:
- **HTTP**: `method`, `url`, `code`, `protocol`
- **DNS**: `query`, `ips`, `ttl`, `rcode`, `qtypes`, `rrtypes`
- **Kafka**: `topic`, `api_key`, `api_version`, `error_code`, `correlation_id`

Source: `crates/bridges/hubble-bridge/src/mapper.rs:47-232`

### Hubble Severity Classification

| Level | Trigger |
|---|---|
| `critical` | `DROPPED` verdict and source or destination in `SENSITIVE_NAMESPACES` |
| `high` | `DROPPED` verdict (normal namespace); `ERROR` verdict |
| `medium` | L7 HTTP response code >= 400; DNS non-zero rcode; DNS query to suspicious TLD (`SUSPICIOUS_TLDS`: `.tk`, `.ml`, `.ga`, `.cf`, `.gq`, `.top`, `.xyz`, `.buzz`, `.club`, `.icu`, `.cam`, `.rest`, `.surf`, `.onion`) |
| `low` | `FORWARDED` verdict with no L7 anomalies |

Source: `crates/bridges/hubble-bridge/src/mapper.rs:234-289`

### ClawdStrike Guard Decisions

The `clawdstrike` crate evaluates agent actions through a guard pipeline.
Hunt correlates these decisions with kernel/network telemetry.

#### Guard Trait and Action Types

```rust
// crates/libs/clawdstrike/src/guards/mod.rs:258-273
pub enum GuardAction<'a> {
    FileAccess(&'a str),                          // path
    FileWrite(&'a str, &'a [u8]),                  // path, content
    NetworkEgress(&'a str, u16),                   // host, port
    ShellCommand(&'a str),                         // command string
    McpTool(&'a str, &'a serde_json::Value),       // tool_name, args
    Patch(&'a str, &'a str),                       // file, diff
    Custom(&'a str, &'a serde_json::Value),        // type, payload
}
```

#### GuardResult

```rust
// crates/libs/clawdstrike/src/guards/mod.rs:83-95
pub struct GuardResult {
    pub allowed: bool,
    pub guard: String,        // guard name (e.g., "forbidden_path", "egress_allowlist")
    pub severity: Severity,   // Info | Warning | Error | Critical
    pub message: String,
    pub details: Option<serde_json::Value>,
}
```

#### Severity Mapping (Guard to Decision Taxonomy)

The `decision_taxonomy` module maps guard outcomes to canonical codes:

| Guard Severity | Canonical Severity | Reason Code |
|---|---|---|
| `Info` (allowed) | *(none)* | `ADC_POLICY_ALLOW` |
| `Warning` (allowed) | `"medium"` | `ADC_POLICY_WARN` |
| `Error` (blocked) | `"high"` | `ADC_POLICY_DENY` |
| `Critical` (blocked) | `"critical"` | `ADC_POLICY_DENY` |

Source: `crates/libs/clawdstrike/src/decision_taxonomy.rs:6-78`

#### GuardReport (Aggregated)

```rust
// crates/libs/clawdstrike/src/engine.rs:25-31
pub struct GuardReport {
    pub overall: GuardResult,         // aggregate verdict (fail-closed: any deny = deny all)
    pub per_guard: Vec<GuardResult>,  // individual guard results
    pub evaluation_path: Option<EvaluationPath>,
}
```

### Receipts

Guard decisions are attested as signed receipts.

```rust
// crates/libs/hush-core/src/receipt.rs:157-175
pub struct Receipt {
    pub version: String,                     // "1.0.0" (RECEIPT_SCHEMA_VERSION)
    pub receipt_id: Option<String>,          // unique ID
    pub timestamp: String,                   // ISO-8601
    pub content_hash: Hash,                  // SHA-256 of evaluated content
    pub verdict: Verdict,                    // { passed, gate_id, scores, threshold }
    pub provenance: Option<Provenance>,      // { clawdstrike_version, provider, policy_hash, ruleset, violations }
    pub metadata: Option<JsonValue>,
}
```

#### Verdict

```rust
// crates/libs/hush-core/src/receipt.rs:62-74
pub struct Verdict {
    pub passed: bool,
    pub gate_id: Option<String>,      // guard or gate identifier
    pub scores: Option<JsonValue>,    // guard-specific scoring
    pub threshold: Option<f64>,
}
```

#### ViolationRef (in Provenance)

```rust
// crates/libs/hush-core/src/receipt.rs:119-131
pub struct ViolationRef {
    pub guard: String,        // which guard
    pub severity: String,     // "low" | "medium" | "high" | "critical"
    pub message: String,
    pub action: Option<String>,  // "blocked" | "logged" | ...
}
```

#### SignedReceipt

Receipts are signed with Ed25519 and optionally co-signed:

```rust
// crates/libs/hush-core/src/receipt.rs:289-294
pub struct SignedReceipt {
    pub receipt: Receipt,
    pub signatures: Signatures,   // { signer: Signature, cosigner: Option<Signature> }
}
```

Canonical JSON serialization uses RFC 8785 key sorting. Hashing supports
both SHA-256 (`receipt.hash_sha256()`) and Keccak-256 (`receipt.hash_keccak256()`)
for Ethereum anchoring.

Source: `crates/libs/hush-core/src/receipt.rs`

### Runtime Proofs (Spine Attestation Layer)

The `spine::attestation` module provides the cross-layer binding types that
link kernel evidence, workload identity, and guard decisions.

#### RuntimeProof

```rust
// crates/libs/spine/src/attestation.rs:98-115
pub struct RuntimeProof {
    pub schema: String,              // "clawdstrike.spine.fact.runtime_proof.v1"
    pub fact_id: String,
    pub proof_type: String,          // "execution" | "file_access" | "network"
    pub timestamp: String,           // ISO-8601
    pub execution: ExecutionEvidence,
    pub identity: WorkloadIdentity,
    pub kubernetes: KubernetesMetadata,
    pub network_enforcement: Option<NetworkEnforcement>,
    pub attestation_chain: AttestationChain,
}
```

#### ExecutionEvidence

```rust
// crates/libs/spine/src/attestation.rs:120-136
pub struct ExecutionEvidence {
    pub binary: String,
    pub binary_hash_ima: Option<String>,
    pub arguments: Option<String>,
    pub pid: u64,
    pub uid: Option<u64>,
    pub exec_id: String,              // Tetragon exec_id (primary join key)
    pub parent_exec_id: Option<String>,
    pub capabilities: Option<String>,
    pub namespaces: Option<Value>,
}
```

#### WorkloadIdentity

```rust
// crates/libs/spine/src/attestation.rs:140-146
pub struct WorkloadIdentity {
    pub spiffe_id: String,            // "spiffe://aegis.local/ns/<ns>/sa/<sa>"
    pub svid_serial: Option<String>,
    pub trust_domain: String,
}
```

#### NetworkEnforcement

```rust
// crates/libs/spine/src/attestation.rs:150-158
pub struct NetworkEnforcement {
    pub tetragon_policy: Option<String>,
    pub cilium_network_policy: Option<String>,
    pub observed_connections: Vec<ObservedConnection>,
}

pub struct ObservedConnection {
    pub daddr: String,
    pub dport: u16,
    pub protocol: String,
    pub service: Option<String>,
}
```

#### AttestationChain

The cross-reference chain that binds all layers together:

```rust
// crates/libs/spine/src/attestation.rs:174-186
pub struct AttestationChain {
    pub tetragon_exec_id: String,                   // links to kernel event
    pub spire_svid_hash: Option<String>,             // links to SPIRE identity
    pub clawdstrike_receipt_hash: Option<String>,    // links to guard receipt
    pub aegisnet_envelope_hash: Option<String>,      // links to Spine log entry
}
```

This is the primary join structure for cross-layer correlation. Hunt uses
`AttestationChain` fields to traverse from a kernel event to the guard
decision that governed it, and from there to the cryptographic receipt.

#### NodeAttestation

```rust
// crates/libs/spine/src/attestation.rs:19-31
pub struct NodeAttestation {
    pub schema: String,              // "clawdstrike.spine.fact.node_attestation.v1"
    pub fact_id: String,
    pub node_id: String,             // "aegis:ed25519:<hex>"
    pub system_attestation: SystemAttestation,
    pub transports: Option<TransportBindings>,
    pub issued_at: String,
}
```

`SystemAttestation` carries SPIFFE ID, SVID cert hash, trust domain,
Kubernetes metadata, binary path, and IMA hash.

Source: `crates/libs/spine/src/attestation.rs`

### Marketplace / Policy Attestation Types

Hunt can also query marketplace provenance data for policy lineage tracking:

| Schema | Struct | Purpose |
|---|---|---|
| `clawdstrike.marketplace.policy_attestation.v1` | `PolicyAttestation` | Curator approval of a policy bundle (bundle_id, bundle_hash, feed_id, curator_public_key) |
| `clawdstrike.marketplace.review_attestation.v1` | `ReviewAttestation` | Community review (reviewer, verdict: approve/reject/needs-changes) |
| `clawdstrike.marketplace.revocation.v1` | `PolicyRevocation` | Revocation of a policy bundle (reason, superseded_by) |
| `clawdstrike.marketplace.feed_entry.v1` | `FeedEntryFact` | Feed entry wrapping a policy bundle reference |
| `clawdstrike.marketplace.head_announcement.v1` | `HeadAnnouncement` | Feed head announcement for sync protocol |
| `clawdstrike.marketplace.policy_bundle.v1` | (fact type) | Policy bundle published as Spine envelope via `spine_bridge.rs` |

Source: `crates/libs/spine/src/marketplace_facts.rs`, `crates/libs/spine/src/marketplace_spine.rs`, `crates/libs/clawdstrike/src/spine_bridge.rs`


## Query Execution Pipeline

```
User Input                    Structured Query              NATS / Local FS
===========                   ================              ===============

"show me all denied    --->   HuntQuery {                   JetStream consumers:
 actions from agent-pod"      mode: Telemetry,              - CLAWDSTRIKE_TETRAGON
                              time_range: last_1h,            (process_exec/exit/kprobe)
OR                            filters: [                    - CLAWDSTRIKE_HUBBLE
                                pod_name="agent-pod",         (flow events)
clawdstrike hunt              verdict=denied,
  --pod agent-pod             ],                            Spine envelope store:
  --verdict denied            output: Table,                - Receipt envelopes
  --start 1h                  }                             - Policy bundle envelopes
                              |
                              v
                        +-----------+
                        | Consumer  |    For each envelope:
                        | Loop      | -> 1. Deserialize JSON
                        |           |    2. Verify envelope signature (verify_envelope)
                        |           |    3. Extract fact payload
                        |           |    4. Apply time_range filter (issued_at)
                        |           |    5. Apply field filters (pod, namespace, severity...)
                        |           |    6. Apply severity threshold
                        +-----------+
                              |
                              v
                        +-----------+
                        | Aggregate |    Group by:
                        |           | -> - Time bucket (for timeline)
                        |           |    - Entity (for correlation)
                        |           |    - Severity (for summary)
                        +-----------+
                              |
                              v
                        +-----------+
                        | Format    | -> Table | JSON | Timeline | SIGMA-match
                        +-----------+
                              |
                              v
                        +-----------+
                        | Sign      |    Optional: wrap results in
                        | Report    |    SignedReceipt for forensic
                        +-----------+    evidence chain
```

### Consumer Strategy

Hunt creates ephemeral JetStream consumers with `DeliverPolicy::ByStartTime`
to seek into the time window specified by `--start` / `--end`. For
streaming mode (`hunt watch`), it uses `DeliverPolicy::New` with
`AckPolicy::None` for real-time tailing.

### Filter Cascade

Filters are applied in order of cheapness:

1. **Subject filter** - NATS subject selection (e.g., only `process_exec.v1`)
2. **Time filter** - `issued_at` within `[start, end]`
3. **Field filter** - JSON path matches on fact fields
4. **Severity threshold** - minimum severity level
5. **Correlation filter** - cross-source entity matching (expensive, last)


## Cross-Layer Correlation

Hunt correlates events from different sources to detect multi-step attack
patterns that span kernel, network, and policy enforcement boundaries.

### Join Keys

Events from different sources are correlated using these join keys:

```
Tetragon Event                      Hubble Flow                    Receipt
==============                      ===========                    =======
process.pod.namespace    <--------> source.namespace               provenance.ruleset
process.pod.name         <--------> source.pod_name
process.pid              <--------> (via RuntimeProof.execution)
exec_id                  <--------> (via AttestationChain)
                                                                   receipt_id
                                                                   content_hash

              RuntimeProof.attestation_chain
              ==============================
              tetragon_exec_id -----> Tetragon event exec_id
              spire_svid_hash  -----> WorkloadIdentity SVID
              clawdstrike_receipt_hash -> Receipt hash
              aegisnet_envelope_hash -> Spine envelope

              KubernetesMetadata (shared by all three)
              ==================
              namespace, pod, node, service_account,
              container_image, container_image_digest
```

### Entity Resolution

Hunt resolves entities across sources using a priority-ordered key chain:

1. **SPIFFE ID** (`spiffe://aegis.local/ns/<ns>/sa/<sa>`) - strongest identity
   binding, available in `RuntimeProof.identity.spiffe_id` and
   `NodeAttestation.system_attestation.spiffe_id`

2. **Kubernetes pod** (`namespace/pod`) - available in all three source types
   via `KubernetesMetadata`

3. **Tetragon exec_id** - unique process execution identifier, used in
   `AttestationChain.tetragon_exec_id` to link a RuntimeProof back to the
   raw Tetragon event

4. **PID + node + timestamp** - fallback when exec_id is not available,
   scoped by node name and time window to avoid PID reuse collisions

### Sliding Window Correlation

Multi-step attacks are detected using a sliding time window:

```
Window: [T - correlation_window, T + correlation_window]

For each event E at time T:
  1. Collect all events within the window that share a join key with E
  2. Build an entity graph: {entity_id -> [event1, event2, ...]}
  3. Walk the graph edges looking for pattern matches:
     - exec -> kprobe(sensitive_path) within 5s
     - exec -> network_egress(suspicious_tld) within 30s
     - denied_guard_action -> process_exit(signal=SIGKILL) within 1s
  4. Score matches by severity product and temporal proximity
```

### Correlation Example: Exfiltration Detection

```
T+0.0s:  Tetragon process_exec  binary=/usr/bin/curl  pod=agent-0/default
T+0.1s:  Hubble flow            verdict=FORWARDED dst=suspicious.tk:443 EGRESS
T+0.2s:  ClawdStrike receipt    verdict.passed=false  guard=egress_allowlist
T+0.3s:  Tetragon process_exit  signal=""  status=1  (curl denied by network policy)

Join: pod_name=agent-0, namespace=default, time_window=1s
Result: Correlated sequence -> possible exfiltration attempt (blocked)
```


## Cryptographic Evidence Chain

Hunt reports maintain cryptographic integrity through a layered verification model.

### Layer 1: Spine Envelope Signatures

Every telemetry event arrives inside a signed Spine envelope. Hunt verifies
each envelope before processing:

```
envelope_hash = SHA-256(canonical_json(unsigned_envelope))    // RFC 8785
signature = Ed25519(signing_key, canonical_json(unsigned_envelope))

Verification:
  1. Strip envelope_hash, signature from envelope
  2. Canonicalize remaining JSON (RFC 8785 key sorting)
  3. Recompute SHA-256, compare to claimed envelope_hash
  4. Verify Ed25519 signature against issuer public key
```

Source: `crates/libs/spine/src/envelope.rs:126-163`

### Layer 2: Merkle Inclusion Proofs

Spine checkpoints periodically commit a Merkle root over recent envelopes:

```rust
// crates/libs/spine/src/checkpoint.rs:15-32
checkpoint_statement {
    schema: "aegis.spine.checkpoint_statement.v1",
    log_id,
    checkpoint_seq,
    prev_checkpoint_hash,
    merkle_root,             // SHA-256 Merkle tree root
    tree_size,               // number of leaves
    issued_at,
}
```

Witness co-signatures use domain separation:
```
witness_message = b"AegisNetCheckpointHashV1" || 0x00 || checkpoint_hash
```

Hunt can request Merkle inclusion proofs for specific envelopes to prove
they existed at a given checkpoint, providing non-repudiation for evidence.

Source: `crates/libs/spine/src/checkpoint.rs`

### Layer 3: Receipt Chain Verification

Guard decisions produce `SignedReceipt` values with Ed25519 signatures
over canonical JSON. Hunt verifies the receipt chain:

```
receipt_canonical = canonical_json(receipt)              // RFC 8785
receipt_hash = SHA-256(receipt_canonical)                // or Keccak-256 for EAS
receipt_signature = Ed25519(signer_key, receipt_canonical)

Verification (via SignedReceipt::verify):
  1. Validate receipt version (fail-closed on unsupported: "1.0.0")
  2. Canonicalize receipt JSON
  3. Verify primary signer signature
  4. Verify optional cosigner signature
  5. Return VerificationResult { valid, signer_valid, cosigner_valid, errors, error_codes }
```

Error codes follow the `VFY_*` taxonomy:
- `VFY_SIGNATURE_INVALID`
- `VFY_COSIGNATURE_INVALID`
- `VFY_RECEIPT_VERSION_INVALID`
- `VFY_RECEIPT_VERSION_UNSUPPORTED`

Source: `crates/libs/hush-core/src/receipt.rs:296-406`

### Layer 4: Cross-Layer Binding via AttestationChain

The `AttestationChain` struct cryptographically binds all three layers:

```
         Tetragon exec_id                  SPIRE SVID hash
               |                                |
               v                                v
    +----------+----------+          +----------+---------+
    | Kernel Event        |          | Workload Identity   |
    | (process_exec,      |          | (spiffe_id,         |
    |  kprobe, etc.)      |          |  trust_domain)      |
    +----------+----------+          +----------+----------+
               |                                |
               +--------- AttestationChain -----+
               |                                |
    +----------v----------+          +----------v----------+
    | Guard Receipt       |          | Spine Envelope      |
    | (receipt_hash)      |          | (envelope_hash)     |
    +---------------------+          +---------------------+
```

Hunt traverses these links to build a complete evidence chain from a
user-visible alert back to the kernel-level observation that triggered it.

### Layer 5: Hunt Report Signing

The final hunt report bundles correlated events and their evidence chains
into a `HuntReport` that is itself signed as a `SignedReceipt`:

```
HuntReport {
    query:         HuntQuery,           // the original query
    results:       Vec<HuntResult>,     // matched events
    timeline:      Vec<TimelineEvent>,  // unified timeline
    evidence:      Vec<SignedEnvelope>,  // original Spine envelopes
    receipt_refs:  Vec<String>,         // receipt hashes for cross-reference
    report_hash:   Hash,               // SHA-256 of canonical report
}

SignedReceipt::sign(
    Receipt {
        content_hash: report_hash,
        verdict: Verdict::pass_with_gate("hunt_report"),
        provenance: Provenance { clawdstrike_version, ... },
        metadata: { "hunt_query": ..., "result_count": ... },
    },
    keypair,
)
```

This ensures hunt reports themselves become first-class attested artifacts
that can be published back to Spine for audit trail purposes.


## Scan Subsystem Architecture

The `clawdstrike hunt` command includes a local scan engine that discovers,
introspects, and analyzes MCP server configurations on the host machine.
The scan engine operates as a three-stage pipeline: **Discover -> Introspect -> Analyze**.

```
+-----------------------------------------------------------------+
|                   Scan Pipeline                                  |
|                                                                  |
|  +------------+     +---------------+     +-----------------+    |
|  | Discover   |---->| Introspect    |---->| Analyze         |    |
|  |            |     |               |     |                 |    |
|  | well-known |     | MCP Client    |     | Guard           |    |
|  | config     |     | (3 transports)|     | Evaluation      |    |
|  | paths      |     |               |     |                 |    |
|  | per        |     | initialize()  |     | Verification    |    |
|  | platform   |     | list_tools()  |     | API             |    |
|  +-----+------+     | list_prompts()|     +---------+-------+    |
|        |            | list_*()      |               |            |
|        v            +-------+-------+               v            |
|  +------------+             |             +-----------------+    |
|  | Candidate  |             v             | ScanPathResult  |    |
|  | Client     |     +---------------+     | (per config)    |    |
|  | { name,    |     | Server        |     |                 |    |
|  |   config   |     | Signature     |     | ServerScanResult|    |
|  |   paths }  |     | { metadata,   |     | (per server)    |    |
|  +------------+     |   tools,      |     |                 |    |
|                     |   prompts,    |     | Issues, Labels  |    |
|                     |   resources } |     +-----------------+    |
|                     +---------------+                            |
+-----------------------------------------------------------------+
```

### Stage 1: Discover

The discovery stage enumerates AI agent configurations on disk by probing
well-known paths for each supported client. Platform-specific path resolution
uses `cfg!(target_os)` branching:

- **macOS**: `~/Library/Application Support/...`
- **Linux**: `~/.config/...`
- **Windows**: `%APPDATA%/...`

Supported clients: Claude Desktop, Claude Code, Cursor, VS Code, Windsurf,
Gemini CLI, Kiro, Clawdbot, OpenCode.

Each discovered client yields a `CandidateClient` with a name, a list of
config file paths to probe, and optional skills directories.

Config files are parsed with a JSON5 parser (handling comments and trailing
commas) and validated against a priority-ordered hierarchy of config models:

| Priority | Config Model | Shape | Used By |
|---|---|---|---|
| 1 | `ClaudeCodeConfigFile` | `{ "projects": { "~": { "mcpServers": {...} } } }` | Claude Code `.claude.json` |
| 2 | `ClaudeConfigFile` | `{ "mcpServers": { "name": {...} } }` | Claude Desktop, Cursor |
| 3 | `VSCodeConfigFile` | `{ "mcp": { "servers": {...} } }` | VS Code `settings.json` |
| 4 | `VSCodeMCPConfig` | `{ "servers": {...} }` | VS Code `.vscode/mcp.json` |
| 5 | `UnknownMCPConfig` | `{}` | Fallback (empty server set) |

Individual server entries are discriminated by field presence: a `command`
field indicates `StdioServer`, a `url` field indicates `RemoteServer`.

Source: `crates/libs/clawdstrike/src/hunt/discovery.rs`

### Stage 2: Introspect

The introspection stage connects to each discovered MCP server and queries
its capabilities using read-only JSON-RPC 2.0 calls. No tools are executed,
no resources are read, and no prompts are rendered — only metadata is
collected.

The MCP client supports three transports (see MCP Protocol Architecture
below). For each server, it performs the introspection sequence and produces
a `ServerSignature` containing the server's metadata, tools, prompts,
resources, and resource templates.

For static tools servers (pre-declared tool lists without a running server),
a synthetic `ServerSignature` is constructed without connecting.

Each list call failure is caught independently and results in an empty list —
it does not abort the scan for other entity types.

Source: `crates/libs/clawdstrike/src/hunt/mcp.rs`

### Stage 3: Analyze

The analysis stage evaluates discovered server signatures through two paths:

1. **Guard evaluation** — each tool is checked against the loaded
   clawdstrike policy (see Guard Integration Architecture below)
2. **Verification API** — signatures are submitted to an external analysis
   service that detects prompt injection, tool poisoning, toxic flows, and
   rug pulls; the response merges `issues` and `labels` back into results

Before submission to the verification API, sensitive data (absolute paths,
environment variable values, header values, URL query parameters) is
redacted.

Source: `crates/libs/clawdstrike/src/hunt/analyze.rs`


## Scan Data Model

### ScanPathResult Hierarchy

The scan subsystem produces a hierarchical result structure rooted at
`ScanPathResult` (one per config file scanned):

```
ScanPathResult
├── client: Option<String>            // e.g. "cursor", "claude"
├── path: String                      // config file path
├── servers: Option<Vec<ServerScanResult>>
│   └── ServerScanResult
│       ├── name: Option<String>      // server name from config
│       ├── server: ServerConfig      // connection config (see below)
│       ├── signature: Option<ServerSignature>
│       │   ├── metadata: Value       // MCP InitializeResult
│       │   ├── tools: Vec<Tool>
│       │   ├── prompts: Vec<Prompt>
│       │   ├── resources: Vec<Resource>
│       │   └── resource_templates: Vec<ResourceTemplate>
│       └── error: Option<ScanError>
├── issues: Vec<Issue>                // vulnerability findings
├── labels: Vec<Vec<ScalarToolLabels>> // per-server per-tool risk scores
└── error: Option<ScanError>          // config-level error
```

### ServerConfig Union

Server connection configuration is a discriminated union tagged on the
`type` field:

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum ServerConfig {
    #[serde(rename = "stdio")]
    Stdio(StdioServer),        // command + args + env
    #[serde(rename = "sse")]
    Sse(RemoteServer),         // url + headers (SSE transport)
    #[serde(rename = "http")]
    Http(RemoteServer),        // url + headers (Streamable HTTP)
    #[serde(rename = "skill")]
    Skill(SkillServer),        // path to skill directory
    #[serde(rename = "tools")]
    Tools(StaticToolsServer),  // pre-declared tool signatures
}
```

`StdioServer` includes a command rebalancing step that splits compound
command strings (e.g., `"npx -y some-server"`) into `(command, args)` using
shell-style tokenization.

### Entity Type

Entities represent the individual capabilities exposed by an MCP server:

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum Entity {
    #[serde(rename = "prompt")]
    Prompt(Prompt),
    #[serde(rename = "resource")]
    Resource(Resource),
    #[serde(rename = "tool")]
    Tool(Tool),
    #[serde(rename = "resource_template")]
    ResourceTemplate(ResourceTemplate),
}
```

Entity identity is computed as `md5(description)` for change detection
across scans (falling back to `"no description available"` when description
is `None`).

### Issue

Vulnerability findings from the verification API:

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Issue {
    pub code: String,          // e.g. "TOOL_POISONING", "PROMPT_INJECTION"
    pub message: String,
    /// (server_index, entity_index), (server_index, None), or None
    pub reference: Option<(usize, Option<usize>)>,
    pub extra_data: Option<HashMap<String, serde_json::Value>>,
}
```

### ScanError and ErrorCategory

Errors are categorized to distinguish informational outcomes (config not
found, unknown format) from actual failures:

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ErrorCategory {
    FileNotFound,      // not a failure — config does not exist
    UnknownConfig,     // not a failure — unrecognized format
    ParseError,        // config exists but could not be parsed
    ServerStartup,     // MCP server failed to start
    ServerHttpError,   // MCP server returned HTTP error
    AnalysisError,     // could not reach analysis server
    SkillScanError,    // could not scan skill
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScanError {
    pub message: Option<String>,
    pub exception: Option<String>,
    pub traceback: Option<String>,
    pub is_failure: bool,           // false for FileNotFound, UnknownConfig
    pub category: Option<ErrorCategory>,
    pub server_output: Option<String>, // captured MCP traffic on failure
}
```

### ScalarToolLabels

Per-tool risk scores returned by the verification API, used for toxic flow
detection:

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScalarToolLabels {
    pub is_public_sink: f64,
    pub destructive: f64,
    pub untrusted_content: f64,
    pub private_data: f64,
}
```

Source: `crates/libs/clawdstrike/src/hunt/models.rs`


## MCP Protocol Architecture

The scan engine implements a minimal MCP client for read-only server
introspection. It uses JSON-RPC 2.0 over three transport types and calls
only five RPC methods.

### JSON-RPC 2.0 Message Format

All MCP communication uses JSON-RPC 2.0:

```
Request:     { "jsonrpc": "2.0", "id": <int>, "method": "<name>", "params": {} }
Response:    { "jsonrpc": "2.0", "id": <int>, "result": { ... } }
Error:       { "jsonrpc": "2.0", "id": <int>, "error": { "code": <int>, "message": "...", "data": ... } }
Notification:{ "jsonrpc": "2.0", "method": "<name>" }    (no id, no response)
```

### Transport Layer

```
+-------------------+  +-------------------+  +-------------------+
| StdioTransport    |  | SseTransport      |  | HttpTransport     |
|                   |  |                   |  |                   |
| tokio::process    |  | reqwest +         |  | reqwest POST      |
| Command           |  | eventsource       |  | with streaming    |
|                   |  |                   |  | response body     |
| Write: stdin      |  | Write: HTTP POST  |  |                   |
| Read:  stdout     |  | Read:  SSE events |  | Write: HTTP POST  |
| Framing: newline- |  |                   |  | Read:  response   |
|   delimited JSON  |  |                   |  |   body            |
+-------------------+  +-------------------+  +-------------------+
```

**stdio** — spawns a child process via `tokio::process::Command`. JSON-RPC
messages are written as newline-delimited JSON to stdin and read from stdout.
The command is resolved against PATH and a set of fallback directories (nvm,
npm-global, yarn, pyenv, cargo, homebrew).

**SSE (Server-Sent Events)** — connects via HTTP GET to the SSE endpoint.
The server sends JSON-RPC responses and notifications as SSE events. The
client sends JSON-RPC requests via HTTP POST to a URL provided in an initial
SSE event.

**Streamable HTTP** — uses standard HTTP POST request/response. The response
body may be streamed via chunked transfer encoding. Supports OAuth bearer
token injection via `Authorization` header (no interactive OAuth flow —
only pre-existing token replay).

### Introspection Sequence

```
Client                          Server
  |                                |
  |  --- initialize ----------->  |
  |  <-- InitializeResult ------  |
  |                                |
  |  --- notifications/initialized (no response)
  |                                |
  |  --- prompts/list ----------> |  (if capabilities.prompts or stdio)
  |  <-- { prompts: [...] } ----  |
  |                                |
  |  --- resources/list --------> |  (if capabilities.resources or stdio)
  |  <-- { resources: [...] } --  |
  |                                |
  |  --- resources/templates/list  |  (if capabilities.resources or stdio)
  |  <-- { resourceTemplates: [] } |
  |                                |
  |  --- tools/list ------------> |  (if capabilities.tools or stdio)
  |  <-- { tools: [...] } ------  |
  |                                |
  |  (connection closed)           |
```

For stdio servers, all list endpoints are called regardless of announced
capabilities. For remote servers, list endpoints are gated on the
capabilities advertised in `InitializeResult`. Each list call failure is
caught independently and produces an empty list rather than aborting the
scan.

### Remote URL Probing Strategy

When connecting to a `RemoteServer`, the client generates URL variants and
tries them sequentially with per-attempt timeouts. Given an input URL, three
variants are derived:

| Input URL ends with | `url_with_sse` | `url_with_mcp` | `url_without_end` |
|---|---|---|---|
| `/sse` | as-is | replace `/sse` with `/mcp` | strip `/sse` |
| `/mcp` | replace `/mcp` with `/sse` | as-is | strip `/mcp` |
| neither | append `/sse` | append `/mcp` | as-is |

These variants are tried in a 6-attempt strategy ordered by preferred
transport:

**Default order (prefer Streamable HTTP):**
1. `http + url_with_mcp`
2. `http + url_without_end`
3. `sse  + url_with_mcp`
4. `sse  + url_without_end`
5. `http + url_with_sse`
6. `sse  + url_with_sse`

**SSE-preferred order** (when `type == "sse"`):
1. `sse  + url_with_mcp`
2. `sse  + url_without_end`
3. `http + url_with_mcp`
4. `http + url_without_end`
5. `sse  + url_with_sse`
6. `http + url_with_sse`

On the first successful connection, the client returns immediately. If all
attempts fail, the collected errors are aggregated.

Source: `crates/libs/clawdstrike/src/hunt/mcp.rs`


## Guard Integration Architecture

The scan engine bridges discovered MCP server capabilities into the existing
clawdstrike guard evaluation pipeline. This enables **policy-aware scanning**
— tools are not just catalogued, they are evaluated against the loaded
security policy before any agent invokes them.

### Tool -> GuardAction::McpTool Mapping

Each discovered tool is evaluated as a `GuardAction::McpTool` against the
loaded policy:

```rust
for tool in &signature.tools {
    let action = GuardAction::McpTool(&tool.name, &tool.input_schema);
    let report: GuardReport = engine.evaluate(&action, &context).await;
    // Produces per-guard verdicts: allowed/warned/denied
}
```

This exercises the `McpToolGuard` which restricts MCP tool invocations
based on the policy's `mcp_tools` configuration (allowlist/denylist
patterns). The guard pipeline runs fail-closed: any deny produces an
overall deny verdict.

### Tool Description -> PromptInjectionGuard

Tool descriptions are checked for hidden instructions or prompt injection
payloads using the `PromptInjectionGuard`:

```rust
for tool in &signature.tools {
    let action = GuardAction::Custom(
        "tool_description",
        &json!({"text": tool.description}),
    );
    let report = engine.evaluate(&action, &context).await;
    // Detects prompt injection in tool descriptions
}
```

The `PromptInjectionGuard` uses a 4-layer detection stack (heuristic,
statistical, ML, optional LLM-judge) to identify injection attempts
embedded in tool metadata.

### Entity Descriptions -> SecretLeakGuard

All entity descriptions (tools, prompts, resources, resource templates) are
scanned for leaked secrets:

```rust
for entity in signature.entities() {
    if let Some(desc) = entity.description() {
        let action = GuardAction::FileWrite("entity_description", desc.as_bytes());
        let report = engine.evaluate(&action, &context).await;
        // Detects API keys, tokens, credentials in descriptions
    }
}
```

The `SecretLeakGuard` applies regex-based secret detection patterns to
identify credentials, API keys, and tokens that may have been inadvertently
embedded in entity metadata.

### Cross-Reference with Guard Evaluation Pipeline

The scan guard integration reuses the same `HushEngine` facade and guard
pipeline described in the Guard Decisions section above. The evaluation flow
is:

```
Discovered Tool/Entity
        |
        v
  GuardAction mapping
  (McpTool | Custom | FileWrite)
        |
        v
  HushEngine::evaluate()
        |
        +---> McpToolGuard        (tool name/args vs policy allowlist)
        +---> PromptInjectionGuard (description text analysis)
        +---> SecretLeakGuard     (credential pattern matching)
        +---> ForbiddenPathGuard  (if tool input_schema references paths)
        +---> EgressAllowlistGuard (if tool metadata references URLs)
        |
        v
  GuardReport { overall, per_guard, evaluation_path }
        |
        v
  ScanPathResult.policy_violations[]
```

Each violation is recorded alongside the verification API's `issues`,
giving operators a unified view of both external analysis findings
(tool poisoning, toxic flows) and local policy enforcement results
(guard denials, warnings).

Source: `crates/libs/clawdstrike/src/hunt/mod.rs`, `crates/libs/clawdstrike/src/engine.rs`


## Schema Reference Summary

| Schema | Source Module | Description |
|---|---|---|
| `aegis.spine.envelope.v1` | `spine::envelope` | Signed envelope wrapper |
| `aegis.spine.checkpoint_statement.v1` | `spine::checkpoint` | Merkle checkpoint |
| `clawdstrike.spine.fact.node_attestation.v1` | `spine::attestation` | Node identity binding |
| `clawdstrike.spine.fact.runtime_proof.v1` | `spine::attestation` | Cross-layer runtime proof |
| `clawdstrike.sdr.fact.tetragon_event.v1` | `tetragon_bridge::mapper` | Kernel event fact |
| `clawdstrike.sdr.fact.hubble_flow.v1` | `hubble_bridge::mapper` | Network flow fact |
| `clawdstrike.marketplace.policy_attestation.v1` | `spine::marketplace_facts` | Policy curator approval |
| `clawdstrike.marketplace.review_attestation.v1` | `spine::marketplace_facts` | Community review |
| `clawdstrike.marketplace.revocation.v1` | `spine::marketplace_facts` | Policy revocation |
| `clawdstrike.marketplace.feed_entry.v1` | `spine::marketplace_spine` | Feed entry wrapper |
| `clawdstrike.marketplace.head_announcement.v1` | `spine::marketplace_spine` | Feed head announcement |
| `clawdstrike.marketplace.policy_bundle.v1` | `spine::marketplace_spine` | Policy bundle on Spine |
| `clawdstrike.policy.bundle` | `clawdstrike::spine_bridge` | Policy bundle fact type |
