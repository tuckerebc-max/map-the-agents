---
access: public
aliases: []
claim_ids:
- clm_215c76b1af08b84eb4f57767c371bd3a8d8337a0e04422881bd9b067122752d4
- clm_24528ca1bdda2761bf77f8f736dfae4976235a918d8b3f6a0a922a980b8a7e55
- clm_3f3c0196ac00caaf31ca4a6cf2d35758960c83cc9cfe2d467427384904aab5f7
- clm_3f62c514c38311429a2087520347796b77c341624049f3dd7391005a4cf8db5a
- clm_4448072f61d662e9e2e674571d9a8ac371ea9f1db92f7526ffd653d3bd96a9e7
- clm_a229bb0d40bcf0d851ac39bc427c686b964d71a993dd376c40a1a034346eafdd
- clm_a3541efc1d76c3cd4ce15bf5b9204c9a5e02648e2715854e4d212c8f3c0bd2a2
- clm_a6bc451443aff029121ce9edb2b0953c9fd3febe76291cbbf1ea39173998c752
- clm_ab3743db6e359fa943a0a4a1327cea80abf7a3c56154611856997284a59707f1
- clm_aed654ddf94c8f9921a4e72aa87dd0b7232535675eda085e08549aca5c6f7220
- clm_d521cfbee0422e329b54c9eef3d43c3768770a714eab1e7bb3be5709f0bed160
- clm_dee5873d8c84ef9d39d94bff203659f2c0306eee1f1a9d687df80d35fbde6fc4
maturity: draft
page_id: pg_1bbbebd561675212a38a469280fde703
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_db91aa82fec6527ca5f319f8cd834734
title: brutusin/instrumentation/README.md @ f1c80c2524a1
updated_at: '2026-09-14T03:39:37Z'
---

# brutusin/instrumentation/README.md @ f1c80c2524a1

<!-- rcw:begin owner=source:src_db91aa82fec6527ca5f319f8cd834734 block=evidence -->
- Transformed methods are wrapped so an onStart call precedes the body, onFinished fires on normal return, and onThrowable is invoked and the throwable rethrown on error. [@claim:clm_215c76b1af08b84eb4f57767c371bd3a8d8337a0e04422881bd9b067122752d4]
- The framework uses the ASM library to inject instructions into method definitions of classes being loaded. [@claim:clm_24528ca1bdda2761bf77f8f736dfae4976235a918d8b3f6a0a922a980b8a7e55]
- Custom interceptors can filter targets via interceptClass(className, byteCode) and interceptMethod(ClassNode, MethodNode) hooks, and implement lifecycle callbacks including doOnStart, doOnFinish, doOnThrowableThrown, and doOnThrowableUncatched, each receiving the Method, relevant payload, and an executionId. [@claim:clm_3f3c0196ac00caaf31ca4a6cf2d35758960c83cc9cfe2d467427384904aab5f7]
- The project is an extensible Java agent framework that instruments JVM programs by modifying bytecode at class-loading time to capture method invocation events (start, finish, errors) and notify custom listeners. [@claim:clm_3f62c514c38311429a2087520347796b77c341624049f3dd7391005a4cf8db5a]
- The project is licensed under Apache License, Version 2.0, authored by Ignacio del Valle Alles, with support and bug reports handled through the GitHub issues page. [@claim:clm_4448072f61d662e9e2e674571d9a8ac371ea9f1db92f7526ffd653d3bd96a9e7]
- Deployment workflow: build a fat-jar containing the interceptor class, add 'Premain-Class: org.brutusin.instrumentation.Agent' to the manifest, and launch the target application with -javaagent:myagent.jar=InterceptorClass;optional_parameter on at least JRE 1.5. [@claim:clm_a229bb0d40bcf0d851ac39bc427c686b964d71a993dd376c40a1a034346eafdd]
- Interceptors receive an init(String arg) callback with an optional parameter supplied through the JVM agent arguments. [@claim:clm_a3541efc1d76c3cd4ce15bf5b9204c9a5e02648e2715854e4d212c8f3c0bd2a2]
- A complete working example is available in the separate brutusin/logging-instrumentation repository, which is listed as a dependent module. [@claim:clm_a6bc451443aff029121ce9edb2b0953c9fd3febe76291cbbf1ea39173998c752]
- Instrumentation is implemented as a byte[]-to-byte[] class transformation at load time, leveraging the JDK 1.5 java.lang.instrument package's java-agent mechanism. [@claim:clm_ab3743db6e359fa943a0a4a1327cea80abf7a3c56154611856997284a59707f1]
- The artifact is published to Maven Central under groupId org.brutusin, artifactId instrumentation, and depends on org.ow2.asm:asm-all. [@claim:clm_aed654ddf94c8f9921a4e72aa87dd0b7232535675eda085e08549aca5c6f7220]
- The module provides an Agent class that instantiates a listener from a concrete Interceptor subclass named in the JVM agent arguments. [@claim:clm_d521cfbee0422e329b54c9eef3d43c3768770a714eab1e7bb3be5709f0bed160]
- The README itself directs users to ShiftLeftSecurity/bctrace, described as a more mature and stable version of this project, suggesting this repository is superseded. [@claim:clm_dee5873d8c84ef9d39d94bff203659f2c0306eee1f1a9d687df80d35fbde6fc4]
<!-- rcw:end owner=source:src_db91aa82fec6527ca5f319f8cd834734 block=evidence -->

## Researcher notes

