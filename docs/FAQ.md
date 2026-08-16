# FAQ

## Do I need to be a programmer?

No. The Lite model is just a small set of Markdown files in a private repository. Git helps with history and recovery, but you do not need to understand software architecture to use the core idea.

## Do I need Codex?

No. The continuity model can be useful with ChatGPT alone. Codex becomes relevant when you want an agent to work inside repositories or perform implementation tasks.

## Is this a replacement for ChatGPT Memory?

No.

Native memory is useful for adaptive personalization. This kit is for explicit, inspectable continuity: project state, verified facts, decisions, lessons, evidence, and permission boundaries.

## Is this a second brain?

It can complement one, but its main goal is different.

A second brain usually asks: “How do I store and retrieve what I know?”

AI Continuity Kit asks: “Which knowledge is current, which is historical, who owns it, and what should happen next?”

## Why not just save every chat?

Because transcripts contain repetition, abandoned ideas, temporary details, errors, and superseded decisions.

The project prefers **reusable delta**:

- confirmed decisions;
- verified state;
- blockers;
- exact next step;
- useful lessons;
- evidence pointers;
- explicit uncertainty.

## Why Markdown?

Because it is human-readable, easy for AI tools to consume, diffable in Git, portable, and requires no runtime dependency.

Markdown is not mandatory for every data type. Live databases and external systems should remain authoritative when they are the natural owner of current structured data.

## Why Git?

Git gives you version history, diffs, rollback, branching, and a clear record of changes.

The project does not claim Git is a universal database. It is primarily a good control/documentation layer for small explicit knowledge.

## What does “one fact, one owner” mean?

If a mutable fact has three independent “current” copies, they can drift.

The idea is to define one canonical owner and let other places link to or summarize it.

## What is a freshness check?

A freshness check asks whether an old fact is still trustworthy **for the current decision**.

For example, a hardware model may be stable for years. A service endpoint, DNS record, deployment status, or account balance may require a new check much sooner.

## Do facts need expiration dates?

Not necessarily.

Freshness can be event-driven rather than time-driven. A fact may require recheck after a deployment, migration, reboot, incident, credential rotation, or other relevant change.

## Does this automatically connect ChatGPT and Codex?

No. The repository is the shared, inspectable context layer. Each tool still needs a supported way to read the relevant repository/files in your environment.

## Is it safe to store personal data here?

The public repository is only a template. Your real continuity repository should normally be private.

Do not commit passwords, tokens, private keys, cookies, session state, secret-bearing configuration, or other credentials.

## Can I use this with Obsidian?

Yes. The files are ordinary Markdown. Obsidian can be a useful human interface while Git remains the versioning layer.

## Can I use this with RAG or a vector database?

Yes. RAG can retrieve relevant material, while the continuity model can still define ownership, freshness, and current-vs-historical meaning.

## Will this become a huge bureaucracy?

It should not.

The design rule is: **start with Lite and add structure only after a real recurring problem appears.**

If the system creates more friction than it removes, simplify it.

## What is the smallest useful setup?

For many people:

```text
START.md
AGENTS.md
context/PREFERENCES.md
context/FACTS.md
context/MEMORY.md
```

Add a project only when you actually need durable project state.

## What should I try first?

Copy [`starter/`](../starter/) into a private repository, use [`BOOTSTRAP_PROMPT.md`](../starter/BOOTSTRAP_PROMPT.md), then ask:

> What do you know that is relevant to this request, what might be stale, and what is the next useful step?
