# AGENTS

## Knowledge discipline

Keep these categories distinct:

- `CURRENT FACT` — verified current reality;
- `USER DECISION` — explicit choice;
- `PLAN` — desired future state;
- `MEMORY` — reusable lesson, not current truth;
- `EVIDENCE` — dated proof;
- `UNKNOWN` — not yet proven.

A plausible guess must not be promoted to a fact.

## Interaction

Use the user's explicit current request first. Use personal context only when it materially improves the answer.

## Actions

“Check”, “review”, and “analyze” mean read-only unless the user clearly asks for a change.

Technical access does not imply permission to modify production systems, reveal secrets, delete data, or expand scope.

## Secrets

Never store passwords, tokens, private keys, cookies, session state, or secret-bearing config in this repository.

## Completion

For substantial work:

`RESULT → VERIFY → UPDATE CORRECT OWNER → RECORD NEXT STEP / LESSON IF USEFUL`
