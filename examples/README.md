# Examples: what “good continuity” looks like

These are examples of **shape**, not data you should copy blindly.

## Example A — everyday assistant

### Preferences

```md
# PREFERENCES

- Give the short answer first.
- Explain unfamiliar technical terms before using them freely.
- When one option clearly fits, recommend it instead of listing ten alternatives.
```

### Durable facts

```md
# FACTS

- Primary computer OS: Ubuntu 24.04 LTS
  - Last verified: 2026-08-10
  - Recheck after: OS reinstall or major upgrade
```

### Memory

```md
# MEMORY

- When troubleshooting, start with read-only checks before proposing changes.
```

Notice the difference:

- a preference tells the assistant **how to interact**;
- a fact says **what is known** and may include freshness;
- memory stores a **reusable lesson**, not proof of current reality.

---

## Example B — a continuing project

### STATE.md

```md
# Current state

Goal: publish a small personal website.

Current position:
- content draft complete;
- domain connected;
- deployment not yet verified from an external network.

Blocker:
- final external check.

Next step:
- verify homepage and TLS from outside the local network.
```

### FACTS.md

```md
# Verified facts

- Canonical domain: example.com
- Hosting provider: Provider B
- Last verified: 2026-08-16
```

### MEMORY.md

```md
# Reusable lessons

- A previous deployment looked healthy locally while public DNS still pointed to the old host. External verification matters after DNS changes.
```

A new session can now continue from the exact next step without rereading the project's entire history.

---

## Example C — superseded information

Bad:

```md
Server IP: 203.0.113.10
Server IP: 203.0.113.20
```

Which one is current?

Better:

```md
CURRENT:
- Server endpoint: server.example.com
- Last verified: 2026-08-16

HISTORICAL:
- 203.0.113.10 — old host before migration
```

History remains useful, but ownership of the current value is unambiguous.

---

## Example D — evidence is dated

```md
# Evidence

2026-08-16
- clean install completed
- smoke test: PASS
- external connectivity: PASS
```

Three months later this is still valuable evidence of what happened on August 16.

It is **not** automatic proof that the system is still healthy three months later.

---

## Example E — permission boundary

A coding agent has repository write access.

The task says:

```text
Allowed:
- edit documentation in this repository;
- run local validation;
- open a pull request.

Not authorized:
- production deployment;
- secret rotation;
- changes in other repositories;
- destructive cleanup.
```

Technical capability is broader than task authorization, so the narrower task boundary wins.

---

## What these examples are teaching

The system becomes useful when it consistently preserves these distinctions:

```text
PREFERENCE ≠ FACT
FACT ≠ MEMORY
CURRENT ≠ HISTORICAL
PLAN ≠ IMPLEMENTED
EVIDENCE ≠ FOREVER-CURRENT
CAPABILITY ≠ AUTHORIZATION
```

That semantic separation matters more than the exact folder names.
