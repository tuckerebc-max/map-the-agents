---
access: public
aliases: []
claim_ids:
- clm_1b32a37841f2bfc5edbf9aa70de1599ef6b3374e5906d6b3329e90fa775736bd
- clm_213f4067ea4bfbba48a888ba5b31965cbe966dfc76f319b834f9c68a6af46a83
- clm_47d1aef7cefd4e9706603fcd21591024b8bfc10141fffb6e256a3bcd612a2bde
- clm_4baebc9aa6ff8d96f282a67b8f93742ba3f7fdddc2f382bf94614d82fd3290d1
- clm_630f464f0b624d1108fcf6f0faa481b8c64800fc24a7b7c120e4d088dcb45216
- clm_7fd05814e743d758c61beeb11cccfbe6516a9855740f343db433509c9efc41a9
- clm_93d049f13402b55a31e500483d03f3f2a702be0cdffaa173d53f68406b5bea55
- clm_9615230e83f7574c8d3104046ad3f8b80361b412f07f5d7679a6121e0aa563c6
- clm_af362b0902bcc9553983d402246be3dac275c3f7462a11418169bb5534d19ea2
- clm_d9790da24976d619614be573fcd4fc13967075ce8a67e02a7045772eee9da5a7
- clm_da456f583572300d30b967c49c2e912606c9f45278901952b625c39378f7b84d
- clm_e9fabc5d902b30151e33d340598688f80c93972d18076b92ebd97ed8ba52bce3
maturity: draft
page_id: pg_da670a630d8c5d4aa1662d6b08a14f1a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9518d514cedd593b85bbfeb68e6970db
title: darrenapfel/claudecode-orchestrator/readme.md @ a83e990b2139
updated_at: '2026-09-14T03:45:40Z'
---

# darrenapfel/claudecode-orchestrator/readme.md @ a83e990b2139

<!-- rcw:begin owner=source:src_9518d514cedd593b85bbfeb68e6970db block=evidence -->
- Milestone completion includes starting the service in the background, smoke-testing endpoints, generating testing guides and a feedback form, and processing user feedback into fix sprints. [@claim:clm_1b32a37841f2bfc5edbf9aa70de1599ef6b3374e5906d6b3329e90fa775736bd]
- The framework orchestrates multiple specialized personas (orchestrator, PM, architect, engineer, UX designer, QA and support roles) working in parallel as a simulated software team. [@claim:clm_213f4067ea4bfbba48a888ba5b31965cbe966dfc76f319b834f9c68a6af46a83]
- Repository development practice: contributors modify orchestrator-files/, rebuild with node build-orchestrator.js, test via ./orchestrator.sh local, and submit pull requests. [@claim:clm_47d1aef7cefd4e9706603fcd21591024b8bfc10141fffb6e256a3bcd612a2bde]
- Each task produces an EVIDENCE.md with reproducible proof, complete test outputs, timestamped screenshots, and actual command execution, and validated tasks are committed with per-task file isolation. [@claim:clm_4baebc9aa6ff8d96f282a67b8f93742ba3f7fdddc2f382bf94614d82fd3290d1]
- The project is explicitly marked deprecated in favor of a new project (www.limeriq.ai), so the framework appears unmaintained at this commit. [@claim:clm_630f464f0b624d1108fcf6f0faa481b8c64800fc24a7b7c120e4d088dcb45216]
- The product's validation harness runs four parallel validators (PM end-to-end, test engineer suites and service startup, performance, security) to check milestone quality. [@claim:clm_7fd05814e743d758c61beeb11cccfbe6516a9855740f343db433509c9efc41a9]
- Parallel execution is enforced: independent tasks must be created simultaneously in one message, with visual guides and system-level warnings against sequential execution. [@claim:clm_93d049f13402b55a31e500483d03f3f2a702be0cdffaa173d53f68406b5bea55]
- Installation is via an orchestrator.sh script with 'global' and 'local' modes, and global installs require explicit 'y' confirmation before overwriting, canceling on any other input. [@claim:clm_9615230e83f7574c8d3104046ad3f8b80361b412f07f5d7679a6121e0aa563c6]
- State lives in a .work workspace organized into foundation, milestones (with per-sprint tasks, integration, numbered validation and fix-cycle directories, and completion docs), and discovery folders. [@claim:clm_af362b0902bcc9553983d402246be3dac275c3f7462a11418169bb5534d19ea2]
- Work follows a nine-step workflow from discovery and requirements through parallel implementation, integration, validation, fix cycles, milestone completion, and feedback processing. [@claim:clm_d9790da24976d619614be573fcd4fc13967075ce8a67e02a7045772eee9da5a7]
- Validation failures trigger documented fix cycles that repeat until all validators pass; the protocol treats multiple cycles as normal, honest progress. [@claim:clm_da456f583572300d30b967c49c2e912606c9f45278901952b625c39378f7b84d]
- The design philosophy is 'quality through truth': every claim requires evidence, failures are documented and fixed rather than hidden, which the docs say saves tokens by catching issues early. [@claim:clm_e9fabc5d902b30151e33d340598688f80c93972d18076b92ebd97ed8ba52bce3]
<!-- rcw:end owner=source:src_9518d514cedd593b85bbfeb68e6970db block=evidence -->

## Researcher notes

