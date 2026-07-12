# System Prompting

> _Question to answer in my own words: What is a system prompt and how is it different from a user prompt?_

## Answer

A system prompt is a special, high-priority instruction that sets the model's role, behavior, tone, constraints, and context *before* the conversation starts — separate from the back-and-forth user messages. Where a user prompt is the specific request ("summarize this email"), the system prompt is the standing brief ("You are a concise assistant that always replies in British English and never invents facts"). Models are trained to weight system instructions above user instructions, which is what makes them useful for guardrails: defining persona, output format, refusal boundaries, and available tools that should hold across every turn. Good system prompting is where a lot of an app's "personality" and safety live — but it isn't foolproof, since a cleverly crafted user message can still try to override it (prompt injection), so it's a strong default, not a hard security boundary.

## Notes / sources

- Related: [[prompt-engineering]], [[input-format]], [[context-engineering]]
