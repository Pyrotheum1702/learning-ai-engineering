# Google ADK

> _Question to answer in my own words: What is the Google Agent Development Kit (ADK)?_

## Answer

The Google Agent Development Kit (ADK) is Google's open-source framework for building, evaluating, and deploying AI agents — it's the same toolkit Google uses to build its own agents. It is code-first and model-agnostic: it works best with Gemini but can use other models too, and it provides primitives for defining agents, giving them tools, orchestrating multi-agent systems, streaming responses, and evaluating behavior. ADK is available in Python (with Java support as well) and integrates with Vertex AI Agent Engine for managed deployment. It sits at the framework layer — you write agent logic with ADK, then optionally run it on Google Cloud's managed runtime for scaling and operations.

## Notes / sources

-
