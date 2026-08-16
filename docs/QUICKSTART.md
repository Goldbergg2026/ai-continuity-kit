# 5-minute quick start

The goal is to get one useful result quickly, not to design a perfect knowledge system.

## Minute 1 — create a private home

Copy the contents of [`starter/`](../starter/) into a new **private** repository for your real continuity data.

You can keep the example project for reference or delete it until you need a continuing project.

## Minute 2 — add only a few real things

Edit:

- `context/PREFERENCES.md` — 2–5 stable interaction preferences;
- `context/FACTS.md` — a few durable facts that are genuinely useful;
- `context/MEMORY.md` — leave nearly empty until a reusable lesson actually appears.

Do not create a biography just because a file exists.

## Minute 3 — bootstrap the assistant

Open [`starter/BOOTSTRAP_PROMPT.md`](../starter/BOOTSTRAP_PROMPT.md) and paste it into an AI assistant that can read the repository.

If your current tool cannot read a repository directly, provide only `START.md`, `AGENTS.md`, and the small context file relevant to the task. Do not dump the whole repository by default.

## Minute 4 — ask a normal question

Try:

> Based only on relevant current context, what should I do next? Tell me what you know, what may be stale, and what you are inferring.

A good result should clearly distinguish known facts from uncertainty.

## Minute 5 — test continuity

Change or supersede one mutable fact, then start a fresh session.

Ask:

> Which value is current, which one is historical, and why?

If the assistant can answer without you manually rebuilding the whole conversation, the continuity loop is working.

---

## Add a project only when needed

When work has durable state worth continuing, copy `projects/example/` and rename the folder.

Keep three roles clear:

- `STATE.md` — where the work is now, blockers, next step;
- `FACTS.md` — verified reusable facts;
- `MEMORY.md` — lessons and pitfalls, not proof of current reality.

After meaningful work:

```text
VERIFY RESULT
    ↓
UPDATE THE RIGHT OWNER
    ↓
SAVE ONLY REUSABLE DELTA
    ↓
COMMIT
```

That is enough for a first real setup.

Next: [examples](../examples/README.md) · [FAQ](FAQ.md) · [comparison](COMPARISON.md)
