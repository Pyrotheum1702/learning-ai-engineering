# Chain-of-Thought (CoT)

> _Question to answer in my own words: What is chain-of-thought prompting?_

## Answer

Chain-of-thought prompting asks the model to reason step by step and show its intermediate work before giving a final answer — as simple as adding "Let's think step by step" or providing examples that spell out the reasoning. Because the model generates one token at a time and conditions on what it has already written, producing the reasoning first gives it more "room to compute" and tends to sharply improve accuracy on multi-step problems: math, logic, planning, complex extraction. The trade-offs are more tokens (higher cost and latency) and longer outputs you often need to parse to pull out just the final answer. Note that many newer "reasoning" models do this internally by default, so you don't always have to prompt for it explicitly.

## Notes / sources

- Related: [[react-prompting]], [[prompt-engineering]]
