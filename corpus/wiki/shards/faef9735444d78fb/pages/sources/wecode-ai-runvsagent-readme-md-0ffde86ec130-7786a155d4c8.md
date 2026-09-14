---
access: public
aliases: []
claim_ids:
- clm_09c45aaf3d1a772bf51cdaf1f747c1f6ea6fe9c1937baf2f4ebf629e0934e2c7
- clm_2947817d82dd5b5cce85b93176f68aca8fbc4d5cfd265c0cbc573d86d80266f0
- clm_6859bb1535713b4163716b2419b52e1681474eedfda3f5b75b542935c005b743
- clm_6c6378ad04d7f703e15e7c2a7749ddcdc4dc905398ca9aecf2d122bd3a6dd050
- clm_8468c6b325b07f2faf74cc6a56bea0320a0b21b2edbf1dbf9a9d20238a80cec5
- clm_b7d402438206cba92193ba59578920f75710a926ed1b0502006c0f91ce05521d
- clm_bf949f48eb313105470f7a19e477dc133fad8123e74b16f998832ed6932bbd70
- clm_cdcbfae34b72386ba213117d0cf287bc8e0796b7bc21a443edc3d4dfceb056b6
- clm_db2ab1d18f439268aca9bbf70c6ee872d1259837e3da2404ab398fc08456d8b2
maturity: draft
page_id: pg_74626de78bdd5b4e9ecf7786a155d4c8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_61a3bbbf58c85b9281dcec56aeae336e
title: wecode-ai/RunVSAgent/README.md @ 0ffde86ec130
updated_at: '2026-09-14T03:22:43Z'
---

# wecode-ai/RunVSAgent/README.md @ 0ffde86ec130

<!-- rcw:begin owner=source:src_61a3bbbf58c85b9281dcec56aeae336e block=evidence -->
- Supported agents listed are Roo Code, Cline, and Kilo Code, with Cline described as able to create/edit files, execute commands, and use the browser with user permission. [@claim:clm_09c45aaf3d1a772bf51cdaf1f747c1f6ea6fe9c1937baf2f4ebf629e0934e2c7]
- RPC communication runs over Unix Domain Sockets or Named Pipes, per the documented technology stack. [@claim:clm_2947817d82dd5b5cce85b93176f68aca8fbc4d5cfd265c0cbc573d86d80266f0]
- Supported JetBrains IDEs include IntelliJ IDEA, WebStorm, PyCharm, PhpStorm, RubyMine, CLion, GoLand, DataGrip, Rider, and Android Studio. [@claim:clm_6859bb1535713b4163716b2419b52e1681474eedfda3f5b75b542935c005b743]
- The plugin can be installed from the JetBrains Marketplace via Settings/Preferences > Plugins, or from a GitHub Releases .zip via 'Install Plugin from Disk', followed by an IDE restart. [@claim:clm_6c6378ad04d7f703e15e7c2a7749ddcdc4dc905398ca9aecf2d122bd3a6dd050]
- The JetBrains plugin and extension host communicate bidirectionally via RPC, described as high-performance inter-process communication for real-time data exchange. [@claim:clm_8468c6b325b07f2faf74cc6a56bea0320a0b21b2edbf1dbf9a9d20238a80cec5]
- Running the product requires JetBrains IDE 2023.1 or later for optimal compatibility, and the build prerequisites include Node.js 18+, Git, and JDK 17+. [@claim:clm_b7d402438206cba92193ba59578920f75710a926ed1b0502006c0f91ce05521d]
- RunVSAgent is a cross-platform tool that lets developers run VSCode-based coding agents and extensions inside JetBrains IDEs such as IntelliJ IDEA, WebStorm, and PyCharm. [@claim:clm_bf949f48eb313105470f7a19e477dc133fad8123e74b16f998832ed6932bbd70]
- The extension host source includes main.ts, extensionManager.ts for extension lifecycle, rpcManager.ts for the RPC layer, and webViewManager.ts for WebView support. [@claim:clm_cdcbfae34b72386ba213117d0cf287bc8e0796b7bc21a443edc3d4dfceb056b6]
- The architecture comprises a Kotlin JetBrains plugin (UI integration, editor bridge), a Node.js extension host with a VSCode API compatibility layer and agent manager, and the VSCode agents themselves. [@claim:clm_db2ab1d18f439268aca9bbf70c6ee872d1259837e3da2404ab398fc08456d8b2]
<!-- rcw:end owner=source:src_61a3bbbf58c85b9281dcec56aeae336e block=evidence -->

## Researcher notes

