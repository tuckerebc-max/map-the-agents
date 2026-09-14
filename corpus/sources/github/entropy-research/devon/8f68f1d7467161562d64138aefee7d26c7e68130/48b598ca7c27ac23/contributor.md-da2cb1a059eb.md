# Contributor

## Basic Overview

Devon consists of following components:
1. Environments: Enviornments are what an agent interacts with. Currently we have two basic types of Environments : LocalShell and User, which are to interact with shell and user respectively. All enviornments have to inherit from devon_agent/environment.py
2. Tools: Tools are functions that an agent can use to interact with the environment. Tools have to be registered to environments to be used by the agent. The registration happens in the session. All tools have to inherit from devon_agent/tool.py
3. Agents: Agents act based on previous observations and decide what tools to use. Agents have to inherit from devon_agent/agent.py. Currently there are two types of agents: TaskAgent, ConverstaionalAgent. By default ConverstaionalAgent is used as its a better user experience.
4. Session: Session is where everything is orchestrated. Session is responsible for managing the tools and the environments. Currently there is only one type of session. Working on adding the ability to have different types of sessions.
5. Config: Most state and configuration is stored in a config object. The defintion is in devon_agent/config.py.


Event System
1. Communication between Agent, tools, and environments happens through event handler and emitting events. These handlers are declared in Session.
2. To add a tool or enviornment, there shouldnt be an explixcit need to change the handler. By just registering enviornments with the session and tools with the enviornments, everythinh should work off the bat.

