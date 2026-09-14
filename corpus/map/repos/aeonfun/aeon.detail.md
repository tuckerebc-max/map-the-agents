# aeonfun/aeon -- full detail

[Back to orientation](aeon.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aeonfun/aeon/95142d19705ca379815e7fc9493a497ee0504e8d/76226e8365f601b0.json](../../../wiki/dossiers/aeonfun/aeon/95142d19705ca379815e7fc9493a497ee0504e8d/76226e8365f601b0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The ./notify tool writes a structured JSON payload to a queue, and a post-run scripts/notify-deliver.sh is the only place channel tokens are consumed, rendering per channel (Telegram, Discord, Slack, Buzz) with per-send audit lines. -- evidence: [CHANGELOG.md#L104-L346](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/CHANGELOG.md#L104-L346) (`clm_76aaf847bf733c892162aade675cab31d8c0e6edc7873c64ec95b14ee3c8d206`)
- [observation/documented] Aeon dispatches to ten coding-agent CLIs via a run-harness contract, including Cursor, Hermes, GLM, and Vercel's fx, with credentials surfaced as dashboard Access Keys rows. -- evidence: [CHANGELOG.md#L66-L102](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/CHANGELOG.md#L66-L102) (`clm_94152b4b1bee22d28bb277eaf4cc2b6954eeecca1001e294cf3ad36d73464262`)

## design-choices (2 claim(s))

- [observation/documented] The ADK recommends a GitHub App over personal access tokens: no credential custody, least-privilege fixed permissions, instant revocation on uninstall, and free multi-tenancy since GitHub tracks installations. -- evidence: [docs/ADK.md#L50-L53](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L50-L53) (`clm_8317142fd9228a982dcdfe7b990c2471db09c8c05f0be94eb28f83076f04b871`)
- [observation/documented] Tenant isolation requires re-verifying with the user's token on every request that they still have access to the stored installation/repo, because otherwise any authenticated user could drive someone else's agent. -- evidence: [docs/ADK.md#L135-L135](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L135-L135), [docs/ADK.md#L124-L124](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L124-L124) (`clm_873544ab4ac9bced1a9d81bc9e86088baf051f80e0ec65b1cd1d6f5f59c9bfd2`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: adding a new capability value requires one PR updating the taxonomy doc, the schema reference, and the install-skill-pack allow-list constant, enforced by a ci-capabilities-parity workflow that fails when the three disagree. -- evidence: [docs/CAPABILITIES.md#L121-L121](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L121-L121), [docs/CAPABILITIES.md#L117-L119](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L117-L119) (`clm_f6fc7f6df588f8bc53d7c4170a8ab700d8eac9ddbb51ffb0996592c12c5f6268`)
- [observation/documented] Repository development practice: pack authors can pre-flight locally with scripts/validate-pack.sh from an Aeon checkout, and listing requires a PR adding a README Community Packs row plus a catalog/skill-packs.json entry. -- evidence: [docs/ADK.md#L320-L322](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L320-L322) (`clm_84bbdb21091952122b79b586d18a485f7c850aaeda3a11a5605ebbb28fef2d89`)

## skills-patterns (2 claim(s))

- [observation/documented] A skill is a single Markdown file with frontmatter (name, description, category, requires, var, mode) plus a prompt; there is no plugin API or compilation step. -- evidence: [docs/ADK.md#L262-L271](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L262-L271), [docs/ADK.md#L260-L260](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L260-L260) (`clm_8524fb1b262679e3fac671019cd367fd0d69680faf901154f15bf6ce77e7f856`)
- [observation/documented] Skill packs are published in their own repo with a skills-pack.json manifest; the installer security-scans each SKILL.md, records provenance in skills.lock, and registers skills disabled so the operator remains the trust boundary. -- evidence: [docs/ADK.md#L330-L330](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L330-L330), [docs/ADK.md#L288-L288](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L288-L288) (`clm_f5eea402cf66e85fe3a35855ce71c966c67f9fdaa4800195c1a8b7b05e6607d5`)

## interfaces (4 claim(s))

- [observation/documented] An Aeon instance is a GitHub repo plus GitHub Actions with no Aeon server or API; integrators read/write files and dispatch workflows via GitHub APIs such as Contents, Actions Secrets, and workflow_dispatch. -- evidence: [docs/ADK.md#L23-L32](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L23-L32), [docs/ADK.md#L21-L21](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L21-L21) (`clm_dca220d4e9a1e4aa481d33e90b5d416ee54dcf72048b5889e9c26f6ff669613a`)
- [observation/documented] The ADK auth pattern uses three credentials: a user OAuth token (no scope param, since permissions come from the App definition), an App JWT used only to mint installation tokens, and a ~1h installation token scoped to one installation's repos. -- evidence: [docs/ADK.md#L89-L91](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L89-L91) (`clm_237bb214a120db62f18f37f0ce3d8441c4cc38d3d4e8f5ee302771f8ef008b9f`)
- [observation/documented] On-demand skill runs go through a single aeon.yml workflow accepting workflow_dispatch inputs: skill (required, regex-checked), var, model (must match a choice option or GitHub returns 422), and harness (claude default or grok). -- evidence: [docs/ADK.md#L185-L185](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L185-L185), [docs/ADK.md#L187-L192](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L187-L192) (`clm_2ed9ba23f17ddc20849fc9047515cdcffbdec3b18bc9ce8f93ff7a408afade1b`)
- [observation/documented] catalog/skills.json is the machine-readable skill catalog; each entry carries a slug, description, category, a single universal var input, required env keys, and needed MCP servers. -- evidence: [docs/ADK.md#L174-L177](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L174-L177), [docs/ADK.md#L162-L172](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L162-L172), [docs/ADK.md#L160-L160](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L160-L160) (`clm_4b0dd74d164e45d121a5fc9927ef055d5f5eb5c77446f71deab2b378e39722fc`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (3 claim(s))

- [observation/documented] The capabilities field is documentation only, not a gate: unknown values are rejected at install, but any allow-listed combination installs and nothing enforces the declared capabilities at runtime. -- evidence: [docs/CAPABILITIES.md#L70-L70](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L70-L70), [docs/CAPABILITIES.md#L129-L131](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L129-L131), [docs/CAPABILITIES.md#L72-L74](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L72-L74), [docs/CAPABILITIES.md#L76-L76](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L76-L76) (`clm_05238a9ba3ab42a8c795857dfa72d7ef826a7efc4448d82d0c2dad2dc57c7869`)
- [observation/documented] The one runtime-enforced axis is the SKILL.md mode tier: read-only mode strips write tools, mounts the repo read-only via an OS sandbox (bwrap on Linux, sandbox-exec on macOS) across all nine harnesses, and a post-run guard reverts stray writes. -- evidence: [docs/CAPABILITIES.md#L89-L89](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L89-L89), [docs/CAPABILITIES.md#L91-L95](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L91-L95), [docs/CAPABILITIES.md#L82-L82](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L82-L82), [docs/CAPABILITIES.md#L97-L97](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L97-L97) (`clm_958577e6bdd5a79ee293e4b5ac5a4b97ce478b15ed4400cb55691640eb4c6879`)
- [observation/documented] If no OS sandbox is available, run-harness warns that read-only is advisory on stderr and only the tool-allowlist and post-run layers apply; CI installs bubblewrap explicitly to avoid silent downgrade. -- evidence: [docs/CAPABILITIES.md#L107-L107](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L107-L107) (`clm_5f001f6525c45d78b17de8657799f68ad39f813c06aa0aaee070352d0a4218e2`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The instance needs at least one model credential (CLAUDE_CODE_OAUTH_TOKEN, ANTHROPIC_API_KEY, or an LLM gateway key), resolved by prefix with auto-cascading. -- evidence: [docs/ADK.md#L250-L250](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L250-L250) (`clm_9a8da15adaa4c4cf4254aec05b68ff86678c6f4557b33f58641dd211e3af2c14`)

## limitations (2 claim(s))

- [observation/documented] workflow_dispatch returns 204 with no run id, so integrators must either poll the runs list by dispatch time or subscribe to the workflow_run webhook for exact correlation. -- evidence: [docs/ADK.md#L210-L211](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L210-L211), [docs/ADK.md#L208-L208](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L208-L208) (`clm_090d7ba6aace523cc012b625ea653f96f6fdefb3e480064748b7f260ba8a6bf4`)
- [observation/documented] GitHub delivers only about 10% of 5-minute schedule ticks; the scheduler also accepts repository_dispatch type cron-tick so a backend can act as an uptime pinger, with a debt model preventing double-firing. -- evidence: [docs/ADK.md#L229-L229](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L229-L229) (`clm_ebab8a19ea9bb1f24897b6cc00b85303329a790a21b4e4e24c1d0ee80829faf3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

