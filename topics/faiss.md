# FAISS

> _Question to answer in my own words: What is FAISS?_

## Answer

FAISS (Facebook AI Similarity Search) is an open-source library from Meta for efficient similarity search and clustering of dense vectors. Unlike a full database, it is a building block: a high-performance library you embed in your own code, without a built-in persistence layer, API server, or metadata management. It offers many index types — such as Flat (exact), IVF, HNSW, and product quantization (PQ) — that let you trade off search accuracy against speed and memory, and it can run on both CPU and GPU for very large datasets. FAISS is widely used as the engine underneath other tools and in custom pipelines where developers want fine-grained control over indexing and nearest-neighbor search.

## Notes / sources

-
