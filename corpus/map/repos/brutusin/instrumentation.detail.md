# brutusin/instrumentation -- full detail

[Back to orientation](instrumentation.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/brutusin/instrumentation/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/eba29e281a7e6777.json](../../../wiki/dossiers/brutusin/instrumentation/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/eba29e281a7e6777.json)

## specifications (1 claim(s))

- [observation/documented] The project is an extensible Java agent framework that instruments JVM programs by modifying bytecode at class-loading time to capture method invocation events (start, finish, errors) and notify custom listeners. -- evidence: [README.md#L4-L4](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L4-L4) (`clm_3f62c514c38311429a2087520347796b77c341624049f3dd7391005a4cf8db5a`)

## components (1 claim(s))

- [observation/documented] The module provides an Agent class that instantiates a listener from a concrete Interceptor subclass named in the JVM agent arguments. -- evidence: [README.md#L23-L23](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L23-L23) (`clm_d521cfbee0422e329b54c9eef3d43c3768770a714eab1e7bb3be5709f0bed160`)

## design-choices (1 claim(s))

- [observation/documented] Instrumentation is implemented as a byte[]-to-byte[] class transformation at load time, leveraging the JDK 1.5 java.lang.instrument package's java-agent mechanism. -- evidence: [README.md#L21-L21](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L21-L21) (`clm_ab3743db6e359fa943a0a4a1327cea80abf7a3c56154611856997284a59707f1`)

## workflows (2 claim(s))

- [observation/documented] Deployment workflow: build a fat-jar containing the interceptor class, add 'Premain-Class: org.brutusin.instrumentation.Agent' to the manifest, and launch the target application with -javaagent:myagent.jar=InterceptorClass;optional_parameter on at least JRE 1.5. -- evidence: [README.md#L114-L117](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L114-L117), [README.md#L108-L112](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L108-L112) (`clm_a229bb0d40bcf0d851ac39bc427c686b964d71a993dd376c40a1a034346eafdd`)
- [observation/documented] The project is licensed under Apache License, Version 2.0, authored by Ignacio del Valle Alles, with support and bug reports handled through the GitHub issues page. -- evidence: [README.md#L131-L131](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L131-L131), [README.md#L127-L127](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L127-L127), [README.md#L136-L137](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L136-L137) (`clm_4448072f61d662e9e2e674571d9a8ac371ea9f1db92f7526ffd653d3bd96a9e7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Transformed methods are wrapped so an onStart call precedes the body, onFinished fires on normal return, and onThrowable is invoked and the throwable rethrown on error. -- evidence: [README.md#L47-L47](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L47-L47), [README.md#L32-L45](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L32-L45) (`clm_215c76b1af08b84eb4f57767c371bd3a8d8337a0e04422881bd9b067122752d4`)
- [observation/documented] Custom interceptors can filter targets via interceptClass(className, byteCode) and interceptMethod(ClassNode, MethodNode) hooks, and implement lifecycle callbacks including doOnStart, doOnFinish, doOnThrowableThrown, and doOnThrowableUncatched, each receiving the Method, relevant payload, and an executionId. -- evidence: [README.md#L76-L79](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L76-L79), [README.md#L101-L106](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L101-L106), [README.md#L91-L94](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L91-L94), [README.md#L86-L89](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L86-L89), [README.md#L96-L99](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L96-L99), [README.md#L81-L84](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L81-L84) (`clm_3f3c0196ac00caaf31ca4a6cf2d35758960c83cc9cfe2d467427384904aab5f7`)
- [observation/documented] Interceptors receive an init(String arg) callback with an optional parameter supplied through the JVM agent arguments. -- evidence: [README.md#L114-L117](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L114-L117), [README.md#L71-L74](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L71-L74) (`clm_a3541efc1d76c3cd4ce15bf5b9204c9a5e02648e2715854e4d212c8f3c0bd2a2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The framework uses the ASM library to inject instructions into method definitions of classes being loaded. -- evidence: [README.md#L23-L23](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L23-L23) (`clm_24528ca1bdda2761bf77f8f736dfae4976235a918d8b3f6a0a922a980b8a7e55`)
- [observation/documented] The artifact is published to Maven Central under groupId org.brutusin, artifactId instrumentation, and depends on org.ow2.asm:asm-all. -- evidence: [README.md#L120-L121](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L120-L121), [README.md#L51-L57](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L51-L57) (`clm_aed654ddf94c8f9921a4e72aa87dd0b7232535675eda085e08549aca5c6f7220`)

## limitations (1 claim(s))

- [observation/documented] The README itself directs users to ShiftLeftSecurity/bctrace, described as a more mature and stable version of this project, suggesting this repository is superseded. -- evidence: [README.md#L1-L1](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L1-L1) (`clm_dee5873d8c84ef9d39d94bff203659f2c0306eee1f1a9d687df80d35fbde6fc4`)

## relevance (1 claim(s))

- [observation/documented] A complete working example is available in the separate brutusin/logging-instrumentation repository, which is listed as a dependent module. -- evidence: [README.md#L124-L124](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L124-L124), [README.md#L62-L62](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L62-L62) (`clm_a6bc451443aff029121ce9edb2b0953c9fd3febe76291cbbf1ea39173998c752`)

