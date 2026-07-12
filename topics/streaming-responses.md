# Streaming Responses

> _Question to answer in my own words: What does it mean to stream an LLM response?_

## Answer

Streaming means the model sends its output token-by-token as it generates, instead of making you wait for the whole completion and returning it in one block. Because LLMs generate autoregressively (one token at a time), the tokens exist before the full answer is done — streaming just forwards them as they arrive, usually over Server-Sent Events (SSE) or a websocket. The big win is *perceived* latency: the user sees text appear almost immediately, which feels far faster even though total generation time is unchanged. It's essential UX for chat apps. The trade-offs: you handle partial output on the client, error handling mid-stream is trickier, and you can't inspect or validate the complete response before the user starts seeing it (relevant for moderation or structured-output parsing).

## Notes / sources

- Related: [[inference]], [[generation]]
