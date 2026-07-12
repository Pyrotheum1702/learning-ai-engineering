# Zero-Shot Prompting

> _Question to answer in my own words: What is zero-shot prompting?_

## Answer

Zero-shot prompting is asking an LLM to perform a task by describing it directly, with no examples of the expected input/output. You rely entirely on the knowledge and instruction-following the model already picked up during training — e.g. "Classify this review as positive or negative: …" with nothing showing it what a correct answer looks like. It's the simplest, cheapest approach (fewest tokens, no example curation) and works surprisingly well for common tasks that modern models have seen many variations of. It gets less reliable when the task is unusual, needs a specific output shape, or has subtle rules — that's when you reach for few-shot examples or richer instructions.

## Notes / sources

- Related: [[few-shot-prompting]], [[prompt-engineering]]
