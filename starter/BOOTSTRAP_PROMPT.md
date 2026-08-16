# Bootstrap prompt

Copy the block below into an AI assistant that can read this repository.

```text
Use this repository as a lightweight continuity layer for our work.

Start with START.md, then follow AGENTS.md.

Important rules:
1. Load only the context relevant to my current request. Do not read the entire repository by default.
2. Keep preferences, verified facts, project state, memory/lessons, plans, and dated evidence semantically separate.
3. Do not treat an old chat, old evidence, or memory as current truth when the fact is mutable and the current decision depends on freshness.
4. If a mutable fact may be stale, say so and request or perform the smallest appropriate verification before relying on it.
5. Do not store passwords, tokens, private keys, cookies, session state, or secret values in Git.
6. Technical access is not blanket authorization. Do not perform destructive, production, secret, or unrelated-project changes without explicit scope and appropriate recovery.
7. After substantial work, save only reusable confirmed delta: decisions, verified state, blockers, next step, useful lessons, and evidence pointers. Do not save full conversational transcripts by default.
8. If information is unknown or conflicting, mark it as unknown/conflicting instead of guessing.

First, inspect the minimal starter structure and tell me in plain language:
- what this continuity repository currently knows;
- what is still empty or unknown;
- the smallest useful thing I should fill in first.

Do not create extra structure unless it solves a real recurring problem.
```

## First useful follow-up

After the assistant understands the repository, try:

```text
Based only on relevant current context, what should I do next? Tell me what you know, what may be stale, and what you are inferring.
```

## Why this prompt is intentionally small

The repository should carry durable structure. The prompt should only establish how to use that structure.

If your bootstrap prompt keeps growing, move stable rules into the appropriate owner file instead of creating a giant permanent prompt.
