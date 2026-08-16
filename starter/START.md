# START

This is the entrypoint for the personal continuity repository.

## Default route

1. Read `AGENTS.md` for global behavior and safety.
2. For ordinary conversation, read only the relevant files under `context/`.
3. For an existing project, read its `STATE.md`, then `FACTS.md` or `MEMORY.md` only when needed.
4. Treat mutable facts as needing freshness when the current decision depends on them.
5. After substantial work, capture only reusable delta.

## Core rule

`ROUTE → CHECK FRESHNESS → WORK → VERIFY → CAPTURE DELTA`

Do not read the whole repository by default.
