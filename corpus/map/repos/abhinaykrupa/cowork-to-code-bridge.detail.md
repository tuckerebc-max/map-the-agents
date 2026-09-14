# abhinaykrupa/cowork-to-code-bridge -- full detail

[Back to orientation](cowork-to-code-bridge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/abhinaykrupa/cowork-to-code-bridge/30b06c2fb24a916c835a2928d2d274727faab09b/b7f65c950b933f92.json](../../../wiki/dossiers/abhinaykrupa/cowork-to-code-bridge/30b06c2fb24a916c835a2928d2d274727faab09b/b7f65c950b933f92.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The system has four parts: a Cowork skill auto-loaded in each session, a shared bridge folder with queue/, results/, and progress/ subfolders, a daemon managed by launchd or systemd (or started manually), and run_claude.sh which hands tasks to a local Claude Code agent. -- evidence: [README.md#L139-L144](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L139-L144) (`clm_7b99b2a3dfcfa7fc57761246e3d61e7cab499a93796f8ce0d730be757c07125e`)
- [observation/documented] Bundled whitelisted scripts include run_claude.sh, mac_health.sh, mac_ram.sh, mac_disk.sh, mac_top.sh, mac_network.sh, process_kill.sh, port_check.sh, docker_ps.sh, docker_logs.sh, git_status.sh, pkg_outdated.sh, and list_scripts.sh, many supporting --json structured output. -- evidence: [README.md#L229-L248](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L229-L248) (`clm_376fd5eb169bc1d4fca22bd22367d440b66e36109077b5ae68d94f9853569cb9`)

## design-choices (3 claim(s))

- [observation/documented] Rather than a network connection, the bridge uses files on a shared folder that Cowork mounts; the README notes this is slower (about one second per call versus milliseconds for MCP) but works because Cowork's sandbox cannot reach localhost services. -- evidence: [README.md#L504-L504](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L504-L504), [README.md#L502-L502](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L502-L502), [README.md#L498-L498](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L498-L498) (`clm_9d255167431975fb19ea5cc72fe1ffad59481027c992c72c325c9f6969bc0a42`)
- [observation/documented] Requests are idempotent: results are cached by an idempotency key so a retry after a dropped connection returns the cached result instead of re-running the agent or script; tasks are journaled and marked in-flight, and a reboot mid-task is detected rather than silently re-run. -- evidence: [README.md#L35-L35](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L35-L35), [README.md#L146-L146](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L146-L146) (`clm_97cfa7fffdce031793ff195f1acb436c544378e67b24b0054b7c3c764c699333`)
- [observation/documented] An optional plan-approval hook (approve_plan.sh) gates tasks carrying a plan field: exit 0 proceeds and exit 2 rejects with the hook's message returned to Cowork; if the file does not exist, the plan field is silently ignored. -- evidence: [README.md#L210-L210](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L210-L210) (`clm_dfa3b744169701f85a8c7d58baa4fc47a03dfc8c14574f92ac8e352dda71d875`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Tasks are JSON files written to a queue/ folder and results are JSON files in results/, with the daemon polling roughly every second; no network connection exists between the Cowork sandbox and the machine. -- evidence: [README.md#L496-L496](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L496-L496), [README.md#L486-L494](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L486-L494) (`clm_bf9bc3f02a084af72fac83d5a60cead846f3680d5db5f7e6576c4c9aafeda890`)
- [observation/documented] The pip install provides console scripts cowork-to-code-bridge-daemon, -uninstall, and -selfcheck; selfcheck checks six items, prints PASS/FAIL per check, and exits 0 if all pass or 1 if any fail. -- evidence: [README.md#L305-L310](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L305-L310), [README.md#L315-L315](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L315-L315), [README.md#L69-L72](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L69-L72), [README.md#L298-L298](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L298-L298) (`clm_6b14ee9355faf61670896ab1827815e6130cc0142329fab1639f558b0f17349b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Long-running tasks can pause and ask the user a question back through the Cowork session via request_cowork.sh, moving through awaiting_reply, reply_to_machine(), and resume_remote(), with timeouts distinguishable from approvals and parallel tasks getting separate replies. -- evidence: [README.md#L252-L252](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L252-L252) (`clm_a05a1bb40017e0e916c4fd45a07d5af7f297a2ac6503fbdd3b6b942902639302`)

## tools-permissions (2 claim(s))

- [observation/documented] The daemon only runs scripts from ~/.cowork-to-code-bridge/scripts/ whose names match a strict pattern (no path tricks or symlinks), rejects commands with a wrong token, and runs as the normal user without sudo. -- evidence: [README.md#L510-L514](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L510-L514) (`clm_900008f83860e7140c0523c1e44171aa54bd63f4fcac8edf8e28dc53a778cf59`)
- [observation/documented] Per-task controls include a spend cap (max_budget_usd, shown as 2.00 in an example), a permission scope (readonly, plan, edit, or full), and model tier/effort selection; owner-set ceilings (BRIDGE_MAX_BUDGET_USD, BRIDGE_PERMISSION_CEILING) take precedence, with the stricter value winning. -- evidence: [README.md#L208-L208](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L208-L208), [README.md#L202-L206](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L202-L206) (`clm_d2327702b88d5770b2b69066915796c49166159505b04e15df259947b883044e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Native Windows is not supported yet; Windows users must install inside WSL2 (Ubuntu) with systemd enabled. The README also lists threats the bridge cannot defend against, including malicious user-written scripts and an attacker who already has filesystem write access. -- evidence: [README.md#L21-L21](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L21-L21), [README.md#L518-L520](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L518-L520), [README.md#L96-L96](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L96-L96) (`clm_9e9dae7fab30ab30bd3389c00ce2bf90e33f4a20ddd2d960156a53835b4c4fec`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

