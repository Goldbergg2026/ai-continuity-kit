# Starter template

This folder is the smallest practical AI Continuity Kit setup.

Copy it into a **private** repository for your own context.

## What each file does

```text
START.md                    entrypoint: where the assistant starts
AGENTS.md                   global behavior and safety rules
context/PREFERENCES.md      stable interaction preferences
context/FACTS.md            durable reusable facts
context/MEMORY.md           lessons and patterns, not current truth
projects/example/STATE.md   what matters for continuing one project now
projects/example/FACTS.md   verified project facts
projects/example/MEMORY.md  reusable project lessons
BOOTSTRAP_PROMPT.md         one copy-paste instruction to get started
```

## Minimum setup

If you do not have a continuing project yet, you can start with only:

```text
START.md
AGENTS.md
context/PREFERENCES.md
context/FACTS.md
context/MEMORY.md
BOOTSTRAP_PROMPT.md
```

Delete or ignore the example project until you actually need it.

## First 5 minutes

1. Create a private repository.
2. Copy this folder's contents to its root.
3. Put 2–5 real preferences in `context/PREFERENCES.md`.
4. Put only a few genuinely reusable facts in `context/FACTS.md`.
5. Leave `MEMORY.md` nearly empty until a real reusable lesson appears.
6. Give your AI the text from `BOOTSTRAP_PROMPT.md`.
7. Ask a normal question.

## A good first test

Change one mutable fact and make the old value historical.

Then start a new session and ask the assistant which value is current and why.

The system is useful when the assistant can distinguish:

```text
CURRENT
HISTORICAL
UNKNOWN
NEEDS RECHECK
```

without you manually rebuilding the conversation.

## Do not overfill it

A continuity repo is not a diary dump.

Do not paste your entire chat history into `MEMORY.md`.
Do not turn every casual idea into a project.
Do not duplicate the same current fact in multiple places.

Keep only what reduces future reconstruction or future error.
