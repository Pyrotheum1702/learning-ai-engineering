# Few-Shot Prompting

> _Question to answer in my own words: What is few-shot prompting?_

## Answer

Few-shot prompting gives the model a handful of worked examples — input paired with the desired output — right in the prompt, before the actual task. The model infers the pattern from those demonstrations and applies it, without any weight updates (this is "in-context learning"). It's the go-to when zero-shot is close but inconsistent: examples pin down the exact output format, tone, edge-case handling, or labeling convention you want. A single example is "one-shot"; several is "few-shot." Practical tips: make examples diverse and representative, keep their format identical to what you want back, and watch the token cost since every example is re-sent on each call (a good candidate for [[prompt-caching]]). Too few or unrepresentative examples can bias the model toward the wrong pattern.

## Notes / sources

- Related: [[zero-shot-prompting]], [[prompt-engineering]]
