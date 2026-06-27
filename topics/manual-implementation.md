# Manual Implementation

> _Question to answer in my own words: What does it mean to build an AI agent by manual implementation (without a framework)?_

## Answer

Manual implementation means building the agent loop yourself with direct calls to an LLM API, instead of relying on a framework or SDK. You write the loop by hand: send the prompt to the model, parse any tool calls it returns, execute those tools, feed the results back, and repeat until the model is done — while also managing conversation state, memory, prompt construction, and error handling yourself. This gives you full control and complete transparency into what the agent does, which makes it excellent for learning exactly what frameworks abstract away. The trade-off is more boilerplate: you end up reinventing retries, tool routing, and context management, so for most production work people reach for an agent SDK or framework instead. (On the roadmap this option is greyed out/struck through for that reason — worth understanding, but usually not the path you ship.)

## Notes / sources

-
