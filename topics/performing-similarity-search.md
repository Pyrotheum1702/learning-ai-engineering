# Performing Similarity Search

> _Question to answer in my own words: How is similarity search performed in a vector database?_

## Answer

Similarity search starts by converting the query into an embedding using the same model that produced the stored vectors, so the query and the data live in the same vector space. The database then measures how close that query vector is to the stored vectors using a distance or similarity metric such as cosine similarity, dot product, or Euclidean distance. Rather than scanning everything, it walks its approximate nearest neighbor index to efficiently return the top-k closest matches, often combined with metadata filters to restrict the candidates. Those nearest neighbors are the most semantically relevant items, which is exactly what powers semantic search results and the retrieval step in a RAG pipeline.

## Notes / sources

-
