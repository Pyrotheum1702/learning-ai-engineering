# Retrieval Process

> _Question to answer in my own words: What happens during the retrieval step of a RAG pipeline?_

## Answer

The retrieval process is the step that, given a user query, finds the most relevant chunks to feed to the model. The query is embedded with the same model used on the documents, then compared against the stored vectors in the vector database to find the nearest neighbors by a similarity metric like cosine similarity, returning the top-k most relevant chunks. This step often includes refinements such as metadata filtering to narrow the candidate set, hybrid search that blends semantic and keyword matching, and reranking to reorder the initial results by relevance before they're used. Retrieval is the heart of RAG: the quality of what it surfaces sets a ceiling on how good and how grounded the final answer can be.

## Notes / sources

-
