# MongoDB Atlas

> _Question to answer in my own words: What is MongoDB Atlas Vector Search?_

## Answer

MongoDB Atlas is MongoDB's fully managed cloud database, and its Atlas Vector Search feature adds vector similarity search directly on top of that document database. Embeddings are stored as fields inside regular MongoDB documents, so vector data lives next to the operational and metadata fields an application already uses. Atlas builds an approximate nearest neighbor index over those embeddings and lets you combine vector similarity with normal document queries and filters in the same system. This makes it a natural fit for teams already on MongoDB who want to add semantic search or RAG without introducing a separate vector database.

## Notes / sources

-
