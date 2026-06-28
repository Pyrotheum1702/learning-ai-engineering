# Generation

> _Question to answer in my own words: What is the generation step in a RAG pipeline?_

## Answer

Generation is the final step of a RAG pipeline, where the language model produces the answer using the retrieved chunks as context. The retrieved passages are combined with the user's question into an augmented prompt — typically with instructions to answer based on the provided context — and the model generates a response grounded in that material rather than relying only on its training data. This grounding is what reduces hallucination and lets the system cite or stay faithful to source documents, and good prompts often ask the model to say when the context doesn't contain the answer. The quality of generation depends heavily on the earlier steps: even a strong model can only be as accurate as the chunks retrieval handed it.

## Notes / sources

-
