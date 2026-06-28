# Embedding

> _Question to answer in my own words: What is the embedding step in a RAG pipeline?_

## Answer

In a RAG pipeline, embedding is the step that converts each text chunk into a numerical vector using an embedding model, so the meaning of the text becomes something a machine can compare mathematically. The same model is later used to embed the user's query, which is what lets the system measure semantic similarity between the question and the stored chunks. Choosing an embedding model (dimensionality, domain fit, cost, and whether it's hosted or open-source) directly affects retrieval quality, and the query and the documents must be embedded with the same model so they live in the same vector space. This is the indexing-time counterpart to retrieval: embed once up front, store the vectors, then reuse them for every query. (See the general concept in embeddings.)

## Notes / sources

-
