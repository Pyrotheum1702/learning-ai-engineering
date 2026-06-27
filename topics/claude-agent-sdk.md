# Claude Agent SDK

> _Question to answer in my own words: What is the Claude Agent SDK?_

## Answer

The Claude Agent SDK is Anthropic's framework for building agents on Claude (it grew out of, and was formerly called, the Claude Code SDK). Instead of just giving you raw model calls, it provides the whole harness around the model: it runs the agent loop, handles tool use, and gives the agent access to a real workspace through built-in tools like reading/writing files and running bash commands. It integrates with the Model Context Protocol (MCP) so the agent can connect to external tools and data, supports subagents for delegating parallel or isolated work, and manages context over long runs through compaction and context editing, plus a permission system to gate sensitive actions. It's available in TypeScript and Python, and is the same foundation that powers Claude Code, so it's a strong choice for building autonomous, tool-using agents that gather context, act, and verify their work.

## Notes / sources

-
