# Comparison: where AI Continuity Kit fits

AI Continuity Kit is not trying to replace every memory or knowledge tool. It is a small continuity/control layer that can sit beside them.

## Quick comparison

| Approach | Best at | Main question it answers | What it may not solve by itself |
|---|---|---|---|
| Native assistant memory | Adaptive personalization | “What should the assistant remember about me?” | Explicit ownership, project state, dated evidence, operational freshness |
| Second brain / notes | Collecting and retrieving knowledge | “Where is what I know?” | Which mutable fact is current; what an agent may change |
| RAG / vector database | Retrieving relevant chunks at scale | “Which stored content is semantically relevant?” | Whether the retrieved statement is still true or authorized for action |
| Project instructions | Steering one agent inside a project | “How should this agent behave here?” | Cross-session state model, historical vs current knowledge, reusable evidence |
| Agent framework | Tools, workflows, automation | “How does the agent execute work?” | Human-readable canonical continuity unless explicitly designed in |
| **AI Continuity Kit** | Explicit, inspectable continuity | **“What do we know, what is current, and what may we do next?”** | Search at massive scale, autonomous execution, model hosting |

## Native ChatGPT-style memory

Native memory is valuable for preferences and adaptive personal context.

AI Continuity Kit adds a different property: **inspectable, versioned, explicit ownership**.

A useful split can be:

```text
native memory       → adaptive personalization
continuity repo     → explicit durable context and project state
live system/API     → current mutable reality
```

The important point is not that one store is “better.” They have different jobs.

## Second brain / Obsidian / personal wiki

A second brain helps you accumulate and retrieve knowledge.

Continuity adds questions such as:

- Is this note historical or current?
- Is this value mutable?
- What event should trigger a recheck?
- Which file owns the current project state?
- Is this a decision, a plan, evidence, or a lesson?

You can use both together.

## RAG and vector databases

RAG is excellent when you have enough material that semantic retrieval matters.

But retrieval and truth are different problems.

A vector search may correctly retrieve an old server address because it is highly relevant. The continuity layer can still say: “this is mutable and the current decision requires a fresh check.”

That makes RAG a possible **retrieval mechanism**, not automatically the canonical owner of current truth.

## Codex / agent project instructions

Project instructions tell an agent how to work.

A continuity layer can additionally preserve:

- current position;
- verified facts;
- decisions;
- reusable lessons;
- evidence;
- blockers;
- next safe step;
- permission boundaries.

This makes project instructions part of the operating model rather than the whole memory model.

## Why Git?

Git is useful here because the content is small, text-first, inspectable, diffable, and recoverable.

Git is **not** automatically the right owner for every type of data. A live database, API, spreadsheet, or running system may own mutable structured state. In that case the repository should store the contract/pointer and verification rules, not a fake duplicate of the live dataset.

## The short version

Use the tool that owns the job:

```text
PERSONALIZATION  → native memory when useful
KNOWLEDGE SEARCH → notes / RAG when useful
CURRENT REALITY  → fresh live source
PROJECT CONTINUITY → explicit state + facts + memory + evidence
EXECUTION        → Codex / agent / automation
AUTHORIZATION    → explicit human/policy boundary
```

AI Continuity Kit is mainly the glue that keeps these meanings from collapsing into one undifferentiated “memory.”
