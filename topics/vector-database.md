# Vector Database

> _Question to answer in my own words: What role does the vector database play in a RAG pipeline?_

## Answer

In a RAG pipeline, the vector database is where the chunk embeddings are stored, indexed, and searched. After each chunk is embedded, its vector — usually along with the original text and metadata — is written to the vector database, which builds an approximate-nearest-neighbor index over those vectors. At query time, the user's question is embedded and the database returns the chunks whose vectors are most similar, which become the context handed to the model. So the vector database is the retrieval backbone of RAG: it makes semantic search over a large knowledge base fast enough to happen on every request. (See the broader concept in Vector DBs.)

## Notes / sources

-
