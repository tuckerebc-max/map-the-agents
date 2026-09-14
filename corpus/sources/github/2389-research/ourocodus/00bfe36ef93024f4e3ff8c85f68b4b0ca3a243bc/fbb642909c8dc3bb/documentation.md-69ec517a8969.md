# Documentation Strategy Guide

## Purpose

This guide establishes systematic practices for keeping documentation synchronized with code changes. It provides decision-making heuristics, templates, and workflows for developers and AI agents working on Ourocodus.

## Table of Contents

1. [Documentation Structure](#documentation-structure)
2. [When to Update Documentation](#when-to-update-documentation)
3. [Change Type Matrix](#change-type-matrix)
4. [Documentation Types](#documentation-types)
5. [Templates](#templates)
6. [Workflow Integration](#workflow-integration)
7. [Worked Example: PR #146](#worked-example-pr-146)

---

## Documentation Structure

### Current Organization

```
ourocodus/
├── README.md                    # Project overview, quick start
├── CONTRIBUTING.md              # Development workflow, standards
├── CLAUDE.md                    # AI agent instructions
├── PRD.md                       # Product requirements
├── DEMO-GUIDE.md               # Demo walkthroughs
├── docs/
│   ├── ARCHITECTURE.md         # System architecture
│   ├── SECURITY.md             # Security considerations
│   ├── TESTING.md              # Testing strategy
│   ├── ROADMAP.md              # Feature roadmap
│   ├── implementation/         # Implementation plans
│   ├── plans/                  # Design decisions
│   └── prd/                    # Component PRDs
├── examples/
│   ├── README.md               # Examples index
│   └── demo-*.go               # Runnable examples
└── pkg/*/
    └── README.md               # Package-specific docs
```

### Documentation Hierarchy

**Level 1: Project-Wide** (README.md, CONTRIBUTING.md)
- Target: New contributors, external users
- Content: High-level overview, setup, contribution guidelines
- Update frequency: When major features added or workflows change

**Level 2: Domain Documentation** (docs/*.md)
- Target: Developers working on the project
- Content: Architecture, security, testing strategy
- Update frequency: When system design changes

**Level 3: Component Documentation** (docs/implementation/*.md, pkg/*/README.md)
- Target: Developers working on specific components
- Content: Implementation details, design rationale
- Update frequency: When component behavior changes

**Level 4: Code Documentation** (godoc comments)
- Target: API consumers, code reviewers
- Content: Function/type documentation, examples
- Update frequency: Every time public API changes

**Level 5: Inline Comments** (code comments)
- Target: Future maintainers
- Content: Complex logic explanation, security notes
- Update frequency: When non-obvious code is written

---

## When to Update Documentation

### Decision Tree

```
CODE CHANGE?
    |
    +-- Public API Added/Modified?
    |       |
    |       YES --> [REQUIRED] Update godoc comments
    |               [YES] Add to README API section
    |               [MAYBE] Add to package README
    |
    +-- User-Facing Behavior Changed?
    |       |
    |       YES --> [YES] Update README features/usage
    |               [YES] Update examples if relevant
    |               [MAYBE] Update DEMO-GUIDE.md
    |
    +-- Security-Related Change?
    |       |
    |       YES --> [REQUIRED] Document threat model
    |               [REQUIRED] Update docs/SECURITY.md
    |               [YES] Add inline security comments
    |               [YES] Update README security section
    |
    +-- Architecture/Structure Changed?
    |       |
    |       YES --> [REQUIRED] Update docs/ARCHITECTURE.md
    |               [YES] Update design rationale
    |               [MAYBE] Update diagrams
    |
    +-- Configuration/Deployment Changed?
    |       |
    |       YES --> [REQUIRED] Update deployment docs
    |               [REQUIRED] Update README env vars
    |               [YES] Update CONTRIBUTING.md
    |
    +-- Bug Fix (User-Visible)?
    |       |
    |       YES --> [MAYBE] Update README known issues
    |               [MAYBE] Add example of correct usage
    |
    +-- Bug Fix (Internal)?
    |       |
    |       YES --> [NO] Usually no doc update needed
    |
    +-- Performance Improvement?
    |       |
    |       YES --> [YES] Update README performance claims
    |               [MAYBE] Update architecture docs
    |
    +-- Refactoring (No Behavior Change)?
            |
            YES --> [NO] No doc update needed
                    [MAYBE] Update architecture if structure changed
```

### Quick Rules

**ALWAYS update documentation when:**
- Adding/modifying exported (public) functions, types, or methods
- Changing security-critical code
- Adding new user-facing features
- Changing API contracts or behavior
- Modifying configuration or deployment process

**USUALLY update documentation when:**
- Fixing user-visible bugs
- Improving performance significantly
- Changing error messages or error handling
- Adding new examples or demos

**RARELY update documentation when:**
- Fixing internal bugs with no external impact
- Refactoring without behavior changes
- Adding internal helper functions
- Improving test coverage

---

## Change Type Matrix

| Change Type             | Godoc    | README | Examples | Arch Docs | Security | Config |
|------------------------|----------|--------|----------|-----------|----------|--------|
| New public function    | REQUIRED | YES    | MAYBE    | NO        | NO       | NO     |
| New feature            | REQUIRED | YES    | YES      | MAYBE     | MAYBE    | MAYBE  |
| Bug fix (user-visible) | NO       | YES    | MAYBE    | NO        | NO       | NO     |
| Bug fix (internal)     | NO       | NO     | NO       | NO        | NO       | NO     |
| Security enhancement   | REQUIRED | YES    | YES      | YES       | REQUIRED | MAYBE  |
| Performance improvement| MAYBE    | YES    | NO       | MAYBE     | NO       | NO     |
| Refactoring (internal) | NO       | NO     | NO       | MAYBE     | NO       | NO     |
| API breaking change    | REQUIRED | YES    | YES      | YES       | MAYBE    | YES    |
| Config/env changes     | MAYBE    | YES    | NO       | NO        | MAYBE    | REQUIRED|
| Deployment changes     | NO       | MAYBE  | NO       | NO        | NO       | REQUIRED|

**Legend:**
- **REQUIRED** = Must update before merge
- **YES** = Should update in most cases
- **MAYBE** = Update if significantly relevant
- **NO** = Typically not needed

---

## Documentation Types

### 1. Godoc Comments

**Purpose:** API documentation for exported Go symbols.

**When to write:**
- Every exported function, type, method, constant, variable
- Package-level documentation (doc.go)

**Format:**
```go
// FunctionName does X and returns Y.
// It accepts Z as input and validates A, B, C.
//
// Security: Include security implications if relevant.
//
// Parameters:
//   - param1: Description
//   - param2: Description
//
// Returns:
//   - Success case description
//   - Error case description
//
// Example:
//   result, err := FunctionName(input)
//   if err != nil {
//       // Handle error
//   }
func FunctionName(param1 string, param2 int) (Result, error) {
    // Implementation
}
```

**See template:** [Template 1: Security-Critical Functions](#template-1-security-critical-functions)

### 2. README Sections

**Purpose:** Quick start, features overview, configuration.

**When to update:**
- New user-facing features
- Changed configuration/environment variables
- Security considerations
- Installation/setup changes

**Key sections:**
- Overview
- Quick Start
- Features
- Environment Variables
- Security
- Architecture (high-level)
- Contributing

### 3. Architecture Documentation

**Purpose:** System design, component relationships, design decisions.

**Location:** `docs/ARCHITECTURE.md`

**When to update:**
- New components added
- Component responsibilities change
- Inter-component communication changes
- Design patterns established

### 4. Security Documentation

**Purpose:** Threat models, security considerations, safe usage.

**Location:** `docs/SECURITY.md`

**When to update:**
- Security features added
- Security vulnerabilities fixed
- Threat model changes
- Security-critical code modified

**Format:** See [Template 2: Security Documentation](#template-2-security-documentation)

### 5. Implementation Plans

**Purpose:** Detailed implementation roadmaps for features.

**Location:** `docs/implementation/*.md`, `docs/plans/*.md`

**When to update:**
- New feature implementation started
- Design decisions documented
- Implementation strategy changed

### 6. Examples and Demos

**Purpose:** Runnable code demonstrating features.

**Location:** `examples/`, `DEMO-GUIDE.md`

**When to update:**
- New features need demonstration
- Example behavior changes
- Demo scripts added/modified

**Format:** See [Template 3: Inline Example Comments](#template-3-inline-example-comments)

---

## Templates

### Template 1: Security-Critical Functions

Use this template for functions that have security implications (validation, authentication, authorization, cryptography, etc.):

```go
// ValidateWorkspacePath verifies that a workspace path is under the base directory.
// This function is used to validate workspace paths extracted from container mounts
// to prevent directory traversal attacks when reusing containers.
//
// Security: A malicious actor could create a container with our session labels but
// mount an arbitrary host path at /workspace. This validation ensures we only accept
// paths that are descendants of baseWorkspaceDir.
//
// The validation uses defense-in-depth:
//   1. Resolves both paths to absolute form
//   2. Checks prefix with path separator to prevent name bypass
//   3. Uses filepath.Rel to detect directory traversal with ".."
//
// Parameters:
//   - baseWorkspaceDir: The trusted base directory for all workspaces
//   - workspacePath: The path to validate (typically from container mount inspection)
//
// Returns:
//   - nil if the path is valid and under baseWorkspaceDir
//   - ErrInvalidWorkspacePath if the path is outside baseWorkspaceDir or contains
//     directory traversal attempts
//
// Example:
//   err := ValidateWorkspacePath("/var/workspaces", "/var/workspaces/session-123")
//   if err != nil {
//       return fmt.Errorf("invalid workspace: %w", err)
//   }
func ValidateWorkspacePath(baseWorkspaceDir, workspacePath string) error {
    // Implementation...
}
```

**Key elements:**
- Brief one-line description
- Multi-line detailed explanation
- Explicit "Security:" callout explaining the threat
- Defense strategy explanation
- Parameter descriptions
- Return value descriptions
- Example usage

### Template 2: Security Documentation

Add security-related features to `docs/SECURITY.md`:

```markdown
## Workspace Path Validation

**Location:** `pkg/containersession/workspace.go:48`

**Threat:** Directory Traversal via Malicious Container Labels

A malicious actor could create a container with valid Ourocodus session labels
but mount an arbitrary host path at the `/workspace` mount point. Without
validation, the system would accept this container during reuse/attach operations,
potentially exposing sensitive host directories.

**Attack Vector:**
1. Attacker creates container with labels:
   - `com.ourocodus.containersession.session-id=target-session`
   - `com.ourocodus.containersession.managed-by=ourocodus`
2. Container mounts `/etc` or `/root` at `/workspace`
3. System discovers container during `AttachContainerSession()`
4. Without validation: System grants access to attacker's container
5. With validation: System rejects container with invalid workspace

**Mitigation:** `ValidateWorkspacePath()` function

The validation function ensures workspace paths are descendants of the
configured base directory using defense-in-depth:

1. **Prefix check:** Ensures path starts with base directory + separator
   - Prevents: `/var/workspaces-evil` bypassing `/var/workspaces`
2. **Relative path check:** Uses `filepath.Rel()` to detect `..` traversal
   - Prevents: `/var/workspaces/../../../etc` attacks
3. **Absolute path check:** Ensures relative result is not absolute
   - Prevents: Symbolic link attacks

**Usage:**
```go
manager := containersession.NewManager(
    dockerClient,
    idGen,
    clock,
    logger,
    "/var/workspaces", // Base directory for validation
)
```

**Testing:**
See `pkg/containersession/workspace_test.go` for validation test cases.
```

### Template 3: Inline Example Comments

Add explanatory comments to examples showing security features:

```go
// EXAMPLE: Container Reuse with Security Validation
//
// Process 1: Create and start session
session1, err := manager.CreateContainerSession(ctx, "ubuntu:latest", []string{"/bin/bash"})
if err != nil {
    log.Fatalf("Failed to create session: %v", err)
}
// Container is created with workspace at: /var/workspaces/session-abc

// ... Later, or from different process ...

// Process 2: Discover and attach to existing session
session2, err := manager.AttachContainerSession(ctx, "session-abc")
if err != nil {
    log.Fatalf("Failed to attach: %v", err)
}
// SECURITY: Manager validates workspace path before attaching.
// If container has workspace mount outside /var/workspaces, AttachContainerSession
// returns ErrInvalidWorkspacePath, preventing directory traversal attacks.

// Both session1 and session2 refer to the same container
fmt.Printf("Same container: %v\n", session1.ContainerID() == session2.ContainerID())
```

---

## Workflow Integration

### PR Checklist

Before submitting a PR, verify documentation is updated:

- [ ] **Public API Changes**: Exported functions/types have godoc comments
- [ ] **User-Facing Changes**: README.md features/usage sections updated
- [ ] **Security Changes**: Threat model documented in docs/SECURITY.md
- [ ] **Examples Updated**: Behavior changes reflected in examples/
- [ ] **Architecture Changes**: docs/ARCHITECTURE.md updated if structure changed
- [ ] **Configuration Changes**: README.md environment variables updated
- [ ] **Breaking Changes**: Migration guide added to PR description

### Code Review Checklist

Reviewers should verify:

- [ ] Godoc comments present on all exported symbols
- [ ] Security implications documented for security-critical code
- [ ] Examples demonstrate new features correctly
- [ ] Documentation matches implementation behavior
- [ ] No stale documentation contradicting new code

### CI Integration (Future)

Potential automated checks:

1. **Godoc Coverage Check**
   - Fail if exported symbols lack godoc comments
   - Tool: Custom script or golangci-lint extension

2. **Example Compilation**
   - Ensure all examples in docs compile and run
   - Tool: `go test -run=Example`

3. **Documentation Staleness Detection**
   - Flag docs not updated in 6+ months
   - Tool: Custom script checking git blame

4. **Broken Link Detection**
   - Find broken markdown links
   - Tool: markdown-link-check

---

## Worked Example: PR #146

### Changes Made

**PR #146: Phase 2 Container Reuse & Attach**

1. **Security: Workspace Path Validation**
   - Added `ValidateWorkspacePath()` function
   - Prevents directory traversal attacks
   - Applied in `handleExistingContainer()` and `AttachContainerSession()`

2. **Correctness: Container ID Refresh**
   - Fixed `session.SetContainerID()` to always update
   - Handles container replacement correctly

3. **Quality: Mock Logger Formatting**
   - Fixed test infrastructure

4. **Quality: Demo Error Propagation**
   - Proper error handling in cleanup code

### Documentation Updates Applied

#### 1. Godoc Comments (Already Complete)

**Location:** `pkg/containersession/workspace.go:48-81`

The `ValidateWorkspacePath()` function already has comprehensive godoc:
- One-line summary
- Detailed explanation
- Security threat model
- Parameters and returns
- Usage example

**Status:** COMPLETE in commit 5428ee9

#### 2. Security Documentation (To Add)

**Location:** `docs/SECURITY.md`

**Action:** Add new section documenting workspace path validation

**Content:** See [Template 2: Security Documentation](#template-2-security-documentation)

**Status:** PENDING (this PR)

#### 3. Example Comments (To Add)

**Location:** `examples/demo-container-reuse.go`

**Action:** Add inline comments explaining security validation

**Content:** See [Template 3: Inline Example Comments](#template-3-inline-example-comments)

**Status:** PENDING (this PR)

#### 4. README Update (To Consider)

**Location:** `README.md`

**Action:** Add brief security note under Architecture or Features

**Content:**
```markdown
### Security

**Workspace Isolation:** Container sessions validate workspace mount points
to prevent directory traversal attacks. See [docs/SECURITY.md](docs/SECURITY.md)
for threat model and mitigation strategy.
```

**Status:** PENDING (this PR)

### Applying the Decision Tree

**Q: Public API Added?**
- **A:** YES - `ValidateWorkspacePath()` is exported
- **Action:** REQUIRED: Godoc comments → DONE
- **Action:** YES: Add to README → PENDING

**Q: Security-Related?**
- **A:** YES - Prevents directory traversal attacks
- **Action:** REQUIRED: Document threat model → PENDING (docs/SECURITY.md)
- **Action:** YES: Add inline security comments → PENDING (examples/)

**Q: User-Facing Behavior?**
- **A:** YES - Container attach now validates workspace
- **Action:** YES: Update examples to show validation → PENDING

**Q: Architecture Changed?**
- **A:** NO - Security added to existing flow
- **Action:** Architecture docs optional

### Documentation Checklist for PR #146

- [x] Godoc: ValidateWorkspacePath has comprehensive comments
- [ ] Security: Add workspace validation section to docs/SECURITY.md
- [ ] Examples: Add inline comments explaining security checks
- [ ] README: Add brief security note
- [ ] PR Description: Include security threat model summary

---

## Maintenance Process

### Monthly Documentation Review

**Schedule:** First week of each milestone/sprint

**Agenda:**
1. Review open "documentation-debt" issues
2. Audit recent PRs for missing docs
3. Check for stale documentation (outdated examples, old APIs)
4. Update documentation roadmap

**Output:**
- List of documentation issues to address
- Priority ranking (critical/high/medium/low)
- Assignment of owners

### Documentation Debt Tracking

**Label:** `documentation-debt`

**Severity Levels:**
- **Critical:** Security/API docs missing (fix within 1 sprint)
- **High:** User-facing feature undocumented (fix within 2 sprints)
- **Medium:** Internal architecture unclear (fix within quarter)
- **Low:** Minor improvements, polish (best effort)

**Issue Template:**
```markdown
## Documentation Debt: [Brief Description]

**Type:** [godoc/README/architecture/security/examples]
**Affected Component:** pkg/example or docs/EXAMPLE.md
**Severity:** [critical/high/medium/low]

**Missing Documentation:**
[What is currently undocumented or incorrect]

**Impact:**
[Who is affected and how]

**Proposed Update:**
[What should be documented]

**Related PR/Issue:** #123
```

---

## Summary

This documentation strategy ensures:

1. **Clear heuristics** for determining when to update docs
2. **Consistent templates** for common documentation types
3. **Systematic process** for maintaining documentation quality
4. **Integration** with PR and review workflows
5. **Accountability** through documentation debt tracking

When in doubt, **document more rather than less**. Future maintainers (including AI agents) rely on clear documentation to understand design decisions, security implications, and usage patterns.

For questions or improvements to this guide, open an issue with label `documentation`.
