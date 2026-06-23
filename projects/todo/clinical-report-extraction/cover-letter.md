# Cover Letter — Structured Extraction from Pathology Reports & Clinical Notes

Hi,

Your work — extracting structured information from pathology reports and clinical notes with LLMs — is squarely the kind of problem I want to be building. Turning messy, free-text clinical documents into reliable structured data is as much an evaluation-and-refinement problem as a prompting one, and that's exactly where I'd focus.

How I'd approach it:

- **Reliable structured extraction:** drive the LLM with a defined output schema (function calling / structured outputs) and validate every result against that schema, so downstream tools get consistent, typed fields instead of free text — and malformed or low-confidence outputs get flagged rather than silently passed through.
- **Handling real clinical text:** pathology reports and notes are full of templates, abbreviations, negations ("no evidence of..."), and inconsistent formatting. I'd build extraction that's robust to that, and where useful, map fields to standard vocabularies (SNOMED, ICD-10, LOINC) so the output is interoperable.
- **Refinement loop:** the real work is making it trustworthy. I'd stand up an eval set against a labeled ground truth, measure field-level precision/recall, and iterate on prompts, schema, and retrieval — keeping a human-in-the-loop review path for ambiguous cases and minimizing hallucinated values.
- **Medical data, handled carefully:** I treat PHI as the priority — minimizing exposure, supporting de-identification where appropriate, and being mindful of HIPAA and where data is processed (e.g. on-prem or BAA-covered model providers).

[Optional: 1–2 sentences on relevant experience — e.g. LLM extraction / NLP / structured-output work, or comfort with clinical/medical data. Add a portfolio or GitHub link.]

I'd love to start with a short call to understand which document types and fields matter most, and what "good enough" accuracy looks like for you.

A few questions to scope it well: what fields/schema are you extracting today, do you have any labeled examples to evaluate against, and are there constraints on where the data can be processed (on-prem vs. a specific model provider)?

Best,
Quang Duoc
pyrotheum1702@gmail.com
