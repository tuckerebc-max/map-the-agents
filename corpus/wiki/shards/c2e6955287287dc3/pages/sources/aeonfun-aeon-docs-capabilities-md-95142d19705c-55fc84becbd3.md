---
access: public
aliases: []
claim_ids:
- clm_05238a9ba3ab42a8c795857dfa72d7ef826a7efc4448d82d0c2dad2dc57c7869
- clm_5f001f6525c45d78b17de8657799f68ad39f813c06aa0aaee070352d0a4218e2
- clm_958577e6bdd5a79ee293e4b5ac5a4b97ce478b15ed4400cb55691640eb4c6879
- clm_f6fc7f6df588f8bc53d7c4170a8ab700d8eac9ddbb51ffb0996592c12c5f6268
maturity: draft
page_id: pg_b69f0084c49b5df3a13055fc84becbd3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_43f416c435675cc0bb524b093a7f79ba
title: aeonfun/aeon/docs/CAPABILITIES.md @ 95142d19705c
updated_at: '2026-09-14T01:29:55Z'
---

# aeonfun/aeon/docs/CAPABILITIES.md @ 95142d19705c

<!-- rcw:begin owner=source:src_43f416c435675cc0bb524b093a7f79ba block=evidence -->
- The capabilities field is documentation only, not a gate: unknown values are rejected at install, but any allow-listed combination installs and nothing enforces the declared capabilities at runtime. [@claim:clm_05238a9ba3ab42a8c795857dfa72d7ef826a7efc4448d82d0c2dad2dc57c7869]
- If no OS sandbox is available, run-harness warns that read-only is advisory on stderr and only the tool-allowlist and post-run layers apply; CI installs bubblewrap explicitly to avoid silent downgrade. [@claim:clm_5f001f6525c45d78b17de8657799f68ad39f813c06aa0aaee070352d0a4218e2]
- The one runtime-enforced axis is the SKILL.md mode tier: read-only mode strips write tools, mounts the repo read-only via an OS sandbox (bwrap on Linux, sandbox-exec on macOS) across all nine harnesses, and a post-run guard reverts stray writes. [@claim:clm_958577e6bdd5a79ee293e4b5ac5a4b97ce478b15ed4400cb55691640eb4c6879]
- Repository development practice: adding a new capability value requires one PR updating the taxonomy doc, the schema reference, and the install-skill-pack allow-list constant, enforced by a ci-capabilities-parity workflow that fails when the three disagree. [@claim:clm_f6fc7f6df588f8bc53d7c4170a8ab700d8eac9ddbb51ffb0996592c12c5f6268]
<!-- rcw:end owner=source:src_43f416c435675cc0bb524b093a7f79ba block=evidence -->

## Researcher notes

