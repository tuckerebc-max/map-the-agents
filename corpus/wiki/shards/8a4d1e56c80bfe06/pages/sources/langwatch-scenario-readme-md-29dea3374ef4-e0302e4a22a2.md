---
access: public
aliases: []
claim_ids:
- clm_028099985f51dc5bce17d0da496d557abb257483a092e4079bece7c660245f6d
- clm_068dba450ade9409355fe467ce7202c7e7891ee50b6aecef40c2ad3166cf05d6
- clm_21e0c175660cab9d8b725ef55a3c38fd3a157f2ff9850e9029692256bc265bcd
- clm_55862db130039e88f82b05c442f3be1e8f927add7e5b1481687a7597816a4c68
- clm_64c7a59044579d505e427546a8ccfc05eda760202ef5c28490a7fd71db34c5c4
- clm_8ad4adc84db8c80636513c166125c588ab4243bc851216c4450407b3b29bca50
- clm_9ab498d6322a3f7e85de5638ef37882a8135902285b8692f80400301a3459312
- clm_cf6ae7c67e0e99424a020fbea9b3910acfab18c2fe87cfd4a8d08bde248cfd36
- clm_daf4e583f416bb6e19a3f09b11cbfaacf117b27af3d458bfa9457b9dab85b892
- clm_de79f4f9009aa18f84d25a0ea22c8d4c9ad5c82bc42070a08d8be4ad378be12b
- clm_e504805d98f09534bb566fd3b02ad22a2b5ca49b769937560e4606978c0a5f9f
maturity: draft
page_id: pg_f3a916a05005502ab1cae0302e4a22a2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_34db99264cff54e2817a13a0f63b1bcc
title: langwatch/scenario/README.md @ 29dea3374ef4
updated_at: '2026-09-14T04:04:57Z'
---

# langwatch/scenario/README.md @ 29dea3374ef4

<!-- rcw:begin owner=source:src_34db99264cff54e2817a13a0f63b1bcc block=evidence -->
- The JudgeAgent evaluates agent performance in real time against stated criteria at each turn, deciding whether the simulation proceeds or ends with a verdict. [@claim:clm_028099985f51dc5bce17d0da496d557abb257483a092e4079bece7c660245f6d]
- Voice support ships platform adapters for ElevenLabs, OpenAI Realtime, Twilio Media Streams, Pipecat WebSocket and Gemini Live, with LiveKit, Vapi and generic WebRTC tracked as follow-up work. [@claim:clm_068dba450ade9409355fe467ce7202c7e7891ee50b6aecef40c2ad3166cf05d6]
- Voice surface includes scenario.audio() for injecting clips, background_noise effects, scenario.interrupt(), result.audio.save() capture, and result.latency reporting TTFB plus p50/p95. [@claim:clm_21e0c175660cab9d8b725ef55a3c38fd3a157f2ff9850e9029692256bc265bcd]
- A cache_key option makes the simulated user's input repeatable for a given scenario, and a @scenario.cache decorator caches decorated calls keyed by arguments, scenario, and cache_key. [@claim:clm_55862db130039e88f82b05c442f3be1e8f927add7e5b1481687a7597816a4c68]
- The core entrypoint is scenario.run(), taking a name, description, agents list, optional script of steps, and optional max_turns; script steps are functions receiving the scenario state. [@claim:clm_64c7a59044579d505e427546a8ccfc05eda760202ef5c28490a7fd71db34c5c4]
- Audio dependencies such as ffmpeg, webrtcvad and websockets ship as hard dependencies of the Python package, included in a plain pip install with no extras flag. [@claim:clm_8ad4adc84db8c80636513c166125c588ab4243bc851216c4450407b3b29bca50]
- Agents are integrated by implementing a single call() method, and the framework is documented as available in Python, TypeScript and Go. [@claim:clm_9ab498d6322a3f7e85de5638ef37882a8135902285b8692f80400301a3459312]
- The judge and user simulator rely on LLMs, so even an ElevenLabs-only voice test requires an OPENAI_API_KEY unless both are swapped via scenario.configure. [@claim:clm_cf6ae7c67e0e99424a020fbea9b3910acfab18c2fe87cfd4a8d08bde248cfd36]
- Shipped agent components include a UserSimulatorAgent, a JudgeAgent evaluated against criteria, and a RedTeamAgent for multi-turn adversarial attacks such as Crescendo escalation with per-turn scoring and refusal detection. [@claim:clm_daf4e583f416bb6e19a3f09b11cbfaacf117b27af3d458bfa9457b9dab85b892]
- Scenario is described as an agent testing framework based on simulations, able to test real agent behavior by simulating users across scenarios and edge cases. [@claim:clm_de79f4f9009aa18f84d25a0ea22c8d4c9ad5c82bc42070a08d8be4ad378be12b]
- Debug mode shows messages step by step and allows human intervention mid-conversation; it is enabled via configure(debug=True), a per-scenario field, or the --scenario-debug pytest flag. [@claim:clm_e504805d98f09534bb566fd3b02ad22a2b5ca49b769937560e4606978c0a5f9f]
<!-- rcw:end owner=source:src_34db99264cff54e2817a13a0f63b1bcc block=evidence -->

## Researcher notes

