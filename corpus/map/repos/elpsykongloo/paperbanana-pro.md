# elpsykongloo/paperbanana-pro

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3d9d1f11647e @ b699785fdaa1e74d

## Summary (orientation draft, not independently verified)

Evidence consists of README, CONTRIBUTING, code-of-conduct, and a requirements file for PaperBanana-Pro, a Chinese-language academic-figure generation tool with GUI/CLI/Viewer entry points and a multi-agent pipeline. No source code slices are present, so all claims are documentation-based.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The documented pipeline comprises six stages: Retriever (few-shot retrieval), Planner (structured visual descriptions), Stylist, Visualizer (image or Matplotlib code), Critic (multi-round review), and optional Polish. -- evidence: [README.md#L212-L219](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L212-L219)
- design-choices (3 claim(s)):
  - [observation/documented] The README describes a registry-driven pipeline (Pipeline Registry) intended to replace hardcoded branching so new flows can be added via configuration. -- evidence: [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40)
  - [observation/documented] Generation runs as background async jobs with a real-time event timeline, supporting 40+ concurrent candidates, and results are packaged in a `Bundle v1` `.bundle.json` format preserving timelines and review records. -- evidence: [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions require a Contributor License Agreement, and all submissions—including those from project members—must go through GitHub pull-request review. -- evidence: [CONTRIBUTING.md#L20-L23](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/CONTRIBUTING.md#L20-L23), [CONTRIBUTING.md#L8-L12](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/CONTRIBUTING.md#L8-L12)
  - [observation/documented] Repository development practice: the project adopts a Contributor Covenant v1.4-based code of conduct and follows Google's Open Source Community Guidelines. -- evidence: [code-of-conduct.md#L93-L95](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/code-of-conduct.md#L93-L95), [CONTRIBUTING.md#L27-L28](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/CONTRIBUTING.md#L27-L28)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes a `paperbanana` command whose default form launches a GUI frontend on port 8501, equivalent to `paperbanana gui`. -- evidence: [README.md#L161-L163](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L161-L163)
  - [observation/documented] A CLI batch mode exists via `paperbanana run` with parameters including `--task_name` (diagram/plot), `--exp_mode`, `--provider`, `--max_critic_rounds`, `--retrieval_setting`, and `--resume`. -- evidence: [README.md#L188-L195](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L188-L195), [README.md#L182-L184](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L182-L184)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The optional PaperBananaBench dataset (dwzhu/PaperBananaBench on Hugging Face) supplies few-shot reference examples and an evaluation benchmark; retrieval can be set to `none` to skip it. -- evidence: [README.md#L135-L135](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L135-L135), [README.md#L133-L133](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L133-L133)
- dependencies (2 claim(s)):
  - [observation/documented] The project targets Python 3.12 or later, installs via `uv sync --locked` plus `uv tool install --editable .`, and requirements.txt contains an editable self-dependency. -- evidence: [README.md#L12-L21](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L12-L21), [requirements.txt#L3-L3](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/requirements.txt#L3-L3), [README.md#L118-L124](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L118-L124)
  - [observation/documented] Four providers are officially supported: Gemini, OpenAI, Openrouter, and Evolink; any OpenAI-compatible API can also be added by supplying a Base URL. -- evidence: [README.md#L148-L148](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L148-L148), [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40)
- limitations (1 claim(s)):
More evidence: [full detail](paperbanana-pro.detail.md)

Metadata and full claim list: [full detail](paperbanana-pro.detail.md)
Human notes ([notes](paperbanana-pro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
