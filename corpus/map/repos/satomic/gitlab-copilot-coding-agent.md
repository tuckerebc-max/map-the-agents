# satomic/gitlab-copilot-coding-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c768d1266af5 @ 51a0ffd4ad935453

## Summary (orientation draft, not independently verified)

The evidence (README.md and I18N_README.md) documents a GitLab-based coding agent that relays issue/MR events through a Flask webhook service to CI/CD pipelines running GitHub Copilot CLI, with three workflows (issue assignment, MR note updates, MR review) and multilingual prompt templates. Evidence coverage: 149 of 302 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Described as a fully automated coding agent powered by GitHub Copilot CLI and GitLab CI/CD, enabling autonomous code implementation and code review via issue assignments, MR comments, and reviewer assignments. -- evidence: [README.md#L5-L5](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] Three components are documented: the app repository, a Flask-based webhook relay service that captures GitLab events, and the Copilot Coding Agent repository acting as a CI/CD orchestrator. -- evidence: [README.md#L62-L64](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L62-L64)
- design-choices (2 claim(s)):
  - [observation/documented] If a merge request already exists for an issue, the agent detects it and posts a notification asking the user to continue in the existing MR rather than creating a duplicate. -- evidence: [README.md#L302-L302](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L302-L302)
  - [observation/documented] Intermediate execution files such as patch_raw.txt, todo.md, plan.json, commit_msg.txt, and mr_summary.txt are generated during runs but excluded from commits. -- evidence: [README.md#L377-L382](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L377-L382)
- workflows (3 claim(s)):
  - [observation/documented] The issue assignment workflow proceeds: acknowledge issue, generate TODO plan, create MR, implement code, push changes, then update MR and issue. -- evidence: [README.md#L68-L73](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L68-L73)
  - [observation/documented] The MR note workflow handles quick updates: a comment triggers the pipeline, the agent acknowledges, implements changes, pushes to the source branch, and posts a summary comment. -- evidence: [README.md#L75-L80](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L75-L80)
- skills-patterns (1 claim(s)):
  - [observation/documented] Prompt templates are organized per language (en, zh, ja, hi, ko, th) under prompts/ directories, with a scripts/load_prompt.sh loader that selects language via COPILOT_LANGUAGE and falls back to English. -- evidence: [I18N_README.md#L9-L14](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L9-L14), [I18N_README.md#L106-L110](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L106-L110), [I18N_README.md#L104-L104](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L104-L104), [I18N_README.md#L20-L100](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L20-L100)
- interfaces (4 claim(s)):
  - [observation/documented] Three trigger interfaces are supported: assigning an issue to Copilot, commenting @copilot-agent in an MR, and assigning Copilot as an MR reviewer; each maps to a distinct workflow (issue, mr_update, mr_review). -- evidence: [README.md#L26-L32](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L26-L32), [README.md#L40-L49](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L40-L49)
  - [observation/documented] The webhook service is configured via environment variables including PIPELINE_TRIGGER_TOKEN, PIPELINE_PROJECT_ID, WEBHOOK_SECRET_TOKEN, COPILOT_AGENT_USERNAME, LISTEN_HOST/PORT, ENABLE_INLINE_REVIEW_COMMENTS, and COPILOT_LANGUAGE. -- evidence: [README.md#L182-L197](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L182-L197)
- memory-state (1 claim(s)):
  - [observation/documented] The prompt loader supports template variable substitution using {variable_name} syntax, accepting variables from environment or arguments, with Python-based safe substitution for special characters and emojis. -- evidence: [I18N_README.md#L106-L110](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L106-L110), [I18N_README.md#L218-L218](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L218-L218), [I18N_README.md#L318-L318](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L318-L318)
More evidence: [full detail](gitlab-copilot-coding-agent.detail.md)

Metadata and full claim list: [full detail](gitlab-copilot-coding-agent.detail.md)
Human notes ([notes](gitlab-copilot-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
