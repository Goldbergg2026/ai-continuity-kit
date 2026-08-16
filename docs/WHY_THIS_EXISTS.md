# Why this exists

AI assistants are getting better at remembering and retrieving context.

That creates a second problem: **remembered context can be useful and still be wrong for the present moment**.

A preference such as “keep answers concise” may remain valid for a long time.
A deployment status may change in minutes.
A project decision can be superseded.
A test result is evidence about a point in time.
A lesson from an old incident can guide investigation without proving the same incident is happening again.

When all of those are stored under one vague label — “memory” — the assistant has to guess what each statement means.

AI Continuity Kit makes those meanings explicit.

```text
PREFERENCE   → how to interact
FACT         → what is known
STATE        → what matters now
MEMORY       → reusable lesson
PLAN         → intended future
EVIDENCE     → dated proof
UNKNOWN      → not established
```

The project is deliberately small because the problem is not lack of data. The problem is **semantic collapse**: too many different kinds of information being treated as if they were equally current and equally authoritative.

The continuity layer gives the human and AI a shared way to avoid that collapse.

## The intended experience

The person should not become a knowledge-base administrator.

The ideal loop is:

```text
speak normally
→ assistant routes to the smallest relevant context
→ freshness is checked when it matters
→ work is performed
→ result is verified
→ only reusable delta is saved
```

The files are implementation detail. The value is that future sessions can continue with less reconstruction and less false confidence.
