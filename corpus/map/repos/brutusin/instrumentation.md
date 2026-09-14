# brutusin/instrumentation

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f1c80c2524a1 @ eba29e281a7e6777

## Summary (orientation draft, not independently verified)

README-only evidence for org.brutusin:instrumentation, a JVM java-agent framework that rewrites class bytecode at load time via ASM to notify custom Interceptor listeners of method lifecycle events. The README also points users to a successor project, ShiftLeftSecurity/bctrace.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is an extensible Java agent framework that instruments JVM programs by modifying bytecode at class-loading time to capture method invocation events (start, finish, errors) and notify custom listeners. -- evidence: [README.md#L4-L4](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L4-L4)
- components (1 claim(s)):
  - [observation/documented] The module provides an Agent class that instantiates a listener from a concrete Interceptor subclass named in the JVM agent arguments. -- evidence: [README.md#L23-L23](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L23-L23)
- design-choices (1 claim(s)):
  - [observation/documented] Instrumentation is implemented as a byte[]-to-byte[] class transformation at load time, leveraging the JDK 1.5 java.lang.instrument package's java-agent mechanism. -- evidence: [README.md#L21-L21](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L21-L21)
- workflows (2 claim(s)):
  - [observation/documented] Deployment workflow: build a fat-jar containing the interceptor class, add 'Premain-Class: org.brutusin.instrumentation.Agent' to the manifest, and launch the target application with -javaagent:myagent.jar=InterceptorClass;optional_parameter on at least JRE 1.5. -- evidence: [README.md#L114-L117](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L114-L117), [README.md#L108-L112](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L108-L112)
  - [observation/documented] The project is licensed under Apache License, Version 2.0, authored by Ignacio del Valle Alles, with support and bug reports handled through the GitHub issues page. -- evidence: [README.md#L131-L131](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L131-L131), [README.md#L127-L127](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L127-L127), [README.md#L136-L137](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L136-L137)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Transformed methods are wrapped so an onStart call precedes the body, onFinished fires on normal return, and onThrowable is invoked and the throwable rethrown on error. -- evidence: [README.md#L47-L47](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L47-L47), [README.md#L32-L45](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L32-L45)
  - [observation/documented] Custom interceptors can filter targets via interceptClass(className, byteCode) and interceptMethod(ClassNode, MethodNode) hooks, and implement lifecycle callbacks including doOnStart, doOnFinish, doOnThrowableThrown, and doOnThrowableUncatched, each receiving the Method, relevant payload, and an executionId. -- evidence: [README.md#L76-L79](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L76-L79), [README.md#L101-L106](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L101-L106), [README.md#L91-L94](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L91-L94), [README.md#L86-L89](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L86-L89), [README.md#L96-L99](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L96-L99), [README.md#L81-L84](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L81-L84)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The framework uses the ASM library to inject instructions into method definitions of classes being loaded. -- evidence: [README.md#L23-L23](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L23-L23)
  - [observation/documented] The artifact is published to Maven Central under groupId org.brutusin, artifactId instrumentation, and depends on org.ow2.asm:asm-all. -- evidence: [README.md#L120-L121](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L120-L121), [README.md#L51-L57](https://github.com/brutusin/instrumentation/blob/f1c80c2524a18e9e2080c28748a0f1d5d77d4be8/README.md#L51-L57)
- limitations (1 claim(s)):
More evidence: [full detail](instrumentation.detail.md)

Metadata and full claim list: [full detail](instrumentation.detail.md)
Human notes ([notes](instrumentation.notes.md), never overwritten by build)

[Back to map index](../../index.md)
