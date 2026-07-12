# Prompt Caching

> _Question to answer in my own words: What is prompt caching and why does it matter?_

## Answer

Prompt caching lets the model provider store the processed state of a large, unchanging chunk of your prompt — a long system prompt, a document, few-shot examples, tool definitions — so it doesn't have to be re-processed on every request. You mark a stable prefix as cacheable; the first call pays full price to build the cache, and subsequent calls that reuse that exact prefix read from it at a large discount and lower latency. It works because LLMs process tokens left-to-right, so a shared prefix produces identical intermediate state that can be reused. The catch: the cached portion must be an exact, byte-for-byte prefix and put the variable content (the user's actual question) *after* the cached block. Caches also expire after a short TTL. It's one of the main levers for cutting cost and latency in production apps that repeatedly send the same big context.

## Notes / sources

- Related: [[context]], [[tokens]]
