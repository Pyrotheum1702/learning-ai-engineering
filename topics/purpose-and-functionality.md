# Purpose and Functionality

> _Question to answer in my own words: What is the purpose and core functionality of a vector database?_

## Answer

The purpose of a vector database is to store high-dimensional embeddings and make them searchable by meaning rather than by exact matches. Its core functionality centers on similarity search: given a query vector, it finds the stored vectors that are closest according to a distance metric such as cosine similarity, dot product, or Euclidean distance. To do this quickly at scale, it builds specialized indexes (like HNSW or IVF) that enable approximate nearest neighbor (ANN) search instead of brute-force comparison. Beyond search, vector databases provide familiar database features such as inserting, updating, and deleting records, attaching metadata to each vector, and filtering results by that metadata. Together these capabilities make them the backbone of semantic search, recommendation systems, and retrieval-augmented generation (RAG) pipelines.

## Notes / sources

-
