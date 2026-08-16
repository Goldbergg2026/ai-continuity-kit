# Use cases

AI Continuity Kit is most useful when a conversation is temporary but the work is not.

The examples below are intentionally small. The project is not trying to turn every part of life into a knowledge-management system.

## 1. Everyday preferences without a biography dump

You want an assistant to remember a few stable interaction preferences:

```md
# PREFERENCES

- Prefer a short answer first, then details when useful.
- Explain unfamiliar technical terms in plain language before using jargon.
- Do not present ten alternatives when one clearly fits.
```

This is different from storing every personal detail you ever mentioned.

**Value:** future conversations feel consistent without requiring a giant personal profile.

---

## 2. A project that survives new chats

You are building a website, bot, home lab, research project, or business process over several weeks.

`STATE.md` answers:

- where are we now?
- what is blocked?
- what changed recently?
- what is the exact next step?

A new session does not need to reconstruct the whole project from old conversation history.

**Value:** less repeated explanation and less accidental regression to an older plan.

---

## 3. Mutable facts that can go stale

Some facts are useful but should not be trusted forever:

```md
- Hosting provider: Provider B
- Last verified: 2026-08-16
- Recheck after: migration, outage, account change, DNS cutover
```

The date is not decoration. It tells the assistant when an old fact may need verification before it affects a decision.

**Value:** memory helps continuity without silently becoming stale runtime truth.

---

## 4. Preserve a decision and its reason

A project chooses PostgreSQL instead of SQLite.

Storing only the result can make the decision look arbitrary later. A compact decision record can preserve:

```text
Decision: PostgreSQL
Reason: multiple writers + existing managed deployment
Rejected for now: SQLite
Revisit when: single-user/offline becomes the dominant use case
```

**Value:** future changes can challenge the actual reasoning instead of repeating the same debate from zero.

---

## 5. Keep lessons separate from current facts

A deployment once failed because a configuration mount disappeared after a container rebuild.

That belongs in `MEMORY.md` as a reusable diagnostic clue.

It does **not** mean every future deployment failure has the same cause.

**Value:** past experience improves investigation without turning a historical pattern into an unquestioned current fact.

---

## 6. Hand work between ChatGPT and Codex

ChatGPT may help define intent, tradeoffs, and next steps. Codex may implement changes in a repository.

A continuity layer gives both tools explicit shared context:

```text
human intent
    ↓
current project state
    ↓
verified facts
    ↓
allowed action scope
    ↓
implementation
    ↓
verification
    ↓
updated state / reusable lesson
```

**Value:** the handoff is based on inspectable state rather than one model trying to reconstruct another model's conversation.

---

## 7. Broad technical access, narrow permission

An agent may technically be able to write files, call APIs, or run commands.

That does not automatically mean it is authorized to:

- delete data;
- deploy to production;
- rotate credentials;
- change a different project;
- expose a private repository.

The continuity model can preserve the difference between **capability** and **authorization**.

**Value:** fewer accidental side effects when agent tooling becomes more powerful.

---

## 8. Evidence without pretending it is forever-current

A test passes today.

Store that as dated evidence:

```text
2026-08-16 — end-to-end test PASS
```

Later, if the system changes, the evidence remains valuable history — but it is not automatically proof that the system still works now.

**Value:** historical proof remains useful without creating false confidence.

---

## When not to use it

Do not create structure just because you can.

A one-off recipe question, casual brainstorm, translation, or disposable task usually does not need a persistent project.

The smallest useful continuity layer is the right one.
