# Test Codeless Agent With Sbus
Test project for applicationinsights-agent

# Steps for publish logs to APP Insight
1. Update connection string @ [applicationinsights.json](https://github.com/abhikt48/java-ai-sbus-test/blob/main/src/main/resources/applicationinsights.json)
2. Dowload and copy `applicationinsights-agent-3.5.2.jar` @ [agent](https://github.com/abhikt48/java-ai-sbus-test/tree/main/agent)
3. Update ServiBus configuration @ [TestAiAgentWithMultiTransports.java](https://github.com/abhikt48/java-ai-sbus-test/blob/main/src/main/java/com/abhi/test/ai/agent/latest/TestCodelessAgentWithSbus.java)
4. Run `TestCodelessAgentWithSbus.java` with only one VM argument `-javaagent:"agent/applicationinsights-agent-3.5.2.jar"`
- Which should start successfully
5. Open App Insight to view dependency tree
