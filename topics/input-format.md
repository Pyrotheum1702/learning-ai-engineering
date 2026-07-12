# Input Format

> _Question to answer in my own words: What does "input format" mean in prompt engineering?_

## Answer

Input format is about deliberately structuring the text you send to an LLM so it can parse the request reliably. Instead of a wall of prose, you use consistent delimiters and layout — headings, XML-style tags (`<context>…</context>`), Markdown sections, numbered steps, or JSON — to separate instructions from data, examples from the task, and context from the question. Clear formatting reduces ambiguity, makes it obvious which part is untrusted user input (helping against prompt injection), and makes the model's job closer to "fill in the blank" than "guess what I meant." Matching the *output* format you ask for (e.g. "respond in JSON") to a well-structured input usually improves accuracy and consistency.

## Notes / sources

-
