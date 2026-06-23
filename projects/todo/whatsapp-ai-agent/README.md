# Multi-Tenant WhatsApp AI Agent

**Status:** ⬜ Not started · **Type:** Client gig (part-time, short-term)

## Brief

> Seeking an AI Engineer to build a multi-tenant WhatsApp AI Agent using FastAPI, LangGraph, and PostgreSQL. The project involves developing a WhatsApp Business API Chatbot with LLM capabilities. The ideal candidate will have experience in integrating AI models with chat platforms and ensuring scalability and security. This is a part-time role with a short-term engagement.

## Goal

Build a production-ready chatbot that connects to the **WhatsApp Business API** and answers users via an **LLM-driven agent**, where a single deployment serves **multiple tenants** (separate businesses/accounts) with isolated data, configuration, and billing.

## Stack

| Layer | Choice |
|-------|--------|
| API / web server | **FastAPI** (async webhooks, REST) |
| Agent orchestration | **LangGraph** (stateful, multi-step agent flows) |
| Data store | **PostgreSQL** (tenants, conversations, messages, state) |
| Messaging | **WhatsApp Business / Cloud API** (Meta) |
| LLM | Provider TBD (e.g. Claude / OpenAI) |

## Key requirements

- **Multi-tenancy** — one codebase, many businesses; strict per-tenant data isolation (row-level scoping or schema-per-tenant), per-tenant prompts/config/API keys.
- **WhatsApp integration** — inbound webhook handling, message send API, media, delivery/read receipts, template messages, 24-hour session window rules.
- **LLM agent** — LangGraph graph for routing, tool use, and multi-turn conversation; persisted conversation state per user.
- **Scalability** — async processing, background workers/queue for LLM calls, handle bursty inbound volume without blocking webhooks.
- **Security** — webhook signature verification, secrets management, tenant auth/isolation, PII handling, rate limiting.

## Proposed architecture (draft)

```
WhatsApp Cloud API ──webhook──▶ FastAPI ──▶ queue/worker ──▶ LangGraph agent ──▶ LLM
        ▲                          │                              │
        └────── send API ◀─────────┴────── PostgreSQL ◀───────────┘
                                    (tenants, conversations, state, messages)
```

## Build plan

- [ ] Scope tenants model + data isolation strategy (RLS vs schema-per-tenant)
- [ ] FastAPI skeleton + WhatsApp webhook verification & inbound handler
- [ ] PostgreSQL schema: tenants, users, conversations, messages, agent_state
- [ ] WhatsApp send-message client (text, templates, media)
- [ ] LangGraph agent: routing, tools, multi-turn state persistence
- [ ] Wire LLM provider + per-tenant prompts/config
- [ ] Async/background processing so webhooks return fast
- [ ] Security pass: signature verification, secrets, rate limiting, PII
- [ ] Deploy + load/scalability test
- [ ] Docs + handoff

## What I want to learn

- WhatsApp Business API mechanics (webhooks, session windows, templates)
- Multi-tenant patterns in Postgres and how they affect query/auth design
- LangGraph for stateful, tool-using agents over a real chat channel
- Making LLM-backed services scalable and secure in production

## Open questions

- Which LLM provider/model and budget?
- Expected message volume / number of tenants (sizing)?
- Self-serve tenant onboarding, or manual provisioning?
- Hosting target (cloud, container platform)?

## Notes / sources

-
