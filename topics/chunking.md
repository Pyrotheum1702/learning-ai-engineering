# Chunking

> _Question to answer in my own words: What is chunking in a RAG pipeline?_

## Answer

Chunking is the first step in building a RAG pipeline: breaking large source documents into smaller, self-contained pieces ("chunks") that can each be embedded and retrieved independently. It matters because embedding models and context windows have size limits, and because retrieval works best when each chunk is focused enough to be clearly relevant or not to a given query. The main design choices are chunk size and overlap — too large and a chunk mixes several topics and dilutes relevance, too small and it loses the surrounding context needed to be useful. Strategies range from simple fixed-size splits to smarter approaches that break on sentence, paragraph, or semantic boundaries so each chunk stays coherent.

## Notes / sources

-
