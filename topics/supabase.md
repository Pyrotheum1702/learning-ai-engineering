# Supabase

> _Question to answer in my own words: How is Supabase used as a vector store?_

## Answer

Supabase is an open-source backend platform, often described as a Firebase alternative, that is built on top of PostgreSQL. For vector search it relies on the `pgvector` extension, which adds a vector column type and similarity operators to Postgres, letting you store embeddings right alongside your existing relational data. This means you can run similarity searches with familiar SQL and combine them with normal filters, joins, and constraints in a single database. Supabase is especially convenient for teams already using Postgres, since it avoids running a separate dedicated vector database while still supporting semantic search and RAG.

## Notes / sources

-
