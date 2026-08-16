# Roadmap

AI Continuity Kit should grow only when a real usability or reliability problem justifies the extra structure.

## Current: v0.2 preview — make the value obvious

Focus:

- clear public positioning;
- 5-minute first success;
- realistic examples;
- explain the difference between memory, current truth, and evidence;
- simple starter template;
- privacy-first defaults;
- public feedback on where the model creates or removes friction.

Success means a new user can answer these questions quickly:

1. Why would I need this?
2. How is it different from normal AI memory or a second brain?
3. What do I do first?
4. How do I know it is working?

## Next: v0.3 — onboarding without hand-editing everything

Candidate work:

- guided setup workflow;
- starter generator or lightweight initializer;
- clearer compatibility notes for common AI surfaces;
- automatic structure validation;
- secret/leakage checks for public mistakes;
- migration guide from ad-hoc prompt folders and chat summaries.

No implementation is promised until the simplest useful design is validated.

## Later: measured reliability

Potential directions:

- context-budget metrics;
- stale-fact/freshness linting;
- semantic owner validation;
- session handoff format;
- explicit agent permission envelope;
- multi-repository continuity;
- CI checks for duplicated current owners;
- optional live-data owner pointers.

## Explicit non-goals

The roadmap does **not** aim to become:

- a full autonomous agent platform;
- another vector database;
- a mandatory all-life productivity system;
- a transcript warehouse;
- a giant framework that must be understood before use.

## Design test for every feature

Before adding a feature, ask:

```text
Does this reduce reconstruction, stale-context risk, unsafe ambiguity, or repeated work?
```

If not, it probably does not belong in the core.

If a feature is useful only for advanced users, it should not make the Lite path heavier.
