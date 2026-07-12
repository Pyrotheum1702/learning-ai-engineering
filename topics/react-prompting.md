# ReAct (Reason + Act)

> _Question to answer in my own words: What is the ReAct prompting pattern?_

## Answer

ReAct ("Reasoning + Acting") is a prompting pattern that interleaves chain-of-thought reasoning with tool use in a loop. Instead of reasoning in one shot, the model alternates: **Thought** (reason about what to do next) → **Action** (call a tool, e.g. search or a calculator) → **Observation** (the tool's result gets fed back) → and repeats until it reaches a final answer. Grounding each reasoning step in real tool results keeps the model from hallucinating and lets it gather information it doesn't already have. This loop is the conceptual foundation of most LLM agents: it combines the "think it through" benefit of [[chain-of-thought]] with the "actually do something" capability of [[function-calling]]. Costs are the usual agent trade-offs — multiple round-trips, more tokens, and the need to handle tool errors and loop termination.

## Notes / sources

- Related: [[chain-of-thought]], [[function-calling]], [[ai-agents]]
