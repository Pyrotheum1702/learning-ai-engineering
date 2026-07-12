# Function Calling

> _Question to answer in my own words: What is function calling (tool use)?_

## Answer

Function calling (also called tool use) lets an LLM invoke external code instead of only producing text. You describe a set of tools to the model as structured schemas — each with a name, a description, and a JSON schema for its parameters. When a user request needs data or an action the model can't do on its own (look up a price, query a database, send an email), the model responds not with prose but with a structured request to call one of those tools, filling in the arguments. Your application executes the real function, returns the result to the model, and the model uses it to continue the conversation. This is the backbone of agents: it turns the LLM into a controller that can reason about *which* tool to use and *how*, while the deterministic work stays in your code. It also forces reliable structured output, since the arguments must match the schema you defined.

## Notes / sources

- Related: [[ai-agents]], [[claude-agent-sdk]]
