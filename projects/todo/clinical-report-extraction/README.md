# Structured Extraction from Pathology Reports & Clinical Notes

**Status:** ⬜ Not started · **Type:** Client gig (biotech)

## Brief

> We are a small biotech company building tools to extract structured information from pathology reports and clinical notes using LLMs. We are looking for an AI engineer to help develop and refine these tools. The ideal candidate will have experience with AI and LLMs, and be comfortable working with medical data.

## Goal

Develop and refine LLM-based tools that turn unstructured clinical documents (pathology reports, clinical notes) into **reliable, validated structured data** that downstream systems can consume.

## Key considerations

- **Structured output:** schema-constrained extraction (function calling / JSON schema) with validation; flag low-confidence or malformed results instead of passing them through.
- **Messy clinical text:** templates, abbreviations, negation ("no evidence of…"), inconsistent formatting; optionally map to standard vocabularies (SNOMED, ICD-10, LOINC).
- **Evaluation & refinement:** labeled ground-truth eval set, field-level precision/recall, prompt/schema iteration, human-in-the-loop review, hallucination control.
- **Medical data / PHI:** de-identification where appropriate, HIPAA awareness, careful control over where data is processed (on-prem vs. BAA-covered provider).

## Open questions

- What fields / output schema are they extracting today?
- Are there labeled examples to evaluate against?
- Where can the data be processed (on-prem, specific model provider, BAA)?
- Document volume and which document types take priority?

## Application

- [cover-letter.md](cover-letter.md)

## Notes / sources

-
