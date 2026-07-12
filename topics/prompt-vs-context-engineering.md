# Prompt vs. Context Engineering

> _Question to answer in my own words: What's the difference between prompt engineering and context engineering?_

## Answer

They're related but operate at different scopes. **Prompt engineering** is about crafting the wording of a single instruction — the phrasing, structure, examples, and format of what you ask — to get a good response for one task. **Context engineering** is the broader discipline of managing *everything* in the model's context window across a whole system or conversation: which documents to retrieve, how much history to keep, what tool outputs to include, how to summarize or prune, and in what order to arrange it all so the model has exactly the right information and nothing that distracts or overflows the window.

A rough analogy: prompt engineering is writing one good question; context engineering is deciding what reference material sits on the desk when the model answers. As apps grew into multi-turn agents with RAG and tools, the bottleneck shifted from "word the prompt well" to "assemble the right context" — so context engineering is really a superset that includes prompt engineering as one of its pieces. The failure modes differ too: bad prompts give vague or misformatted answers, while bad context engineering causes hallucination, ignored information ("lost in the middle"), context-window overflow, and runaway token cost.

## Notes / sources

- Related: [[prompt-engineering]], [[context-engineering]], [[context]]
