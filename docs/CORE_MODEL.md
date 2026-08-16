# Core model

The model is deliberately small.

## Knowledge classes

### Current fact

A claim intended to describe reality now. If the underlying thing can change, record when/how it was verified and re-check it when a decision depends on it.

### User decision

An explicit choice. It remains valid until replaced by a later incompatible decision or the user changes it.

### Plan / target

A desired future state. It must never be presented as already implemented.

### Memory / lesson

Reusable experience that may help future work. Memory is guidance, not current truth.

### Evidence

A dated observation, test, log excerpt, screenshot reference, commit, or other proof of what was true at a particular time.

### Unknown

Something not proven. Prefer `UNKNOWN / NEEDS CHECK` over filling the gap with a plausible guess.

## Ownership

For any mutable concept, prefer one canonical owner.

Other pages may summarize or link to it, but should not independently become a second current source of truth.

## Freshness

Freshness is event-sensitive, not just time-sensitive.

A fact may need re-checking after:

- deployment;
- reboot;
- credential rotation;
- network/DNS change;
- incident;
- hardware replacement;
- a later explicit user correction.

## Capture rule

After substantial work, save only what will improve a future session:

- new decision;
- verified current state;
- blocker;
- exact next step;
- reusable lesson;
- evidence pointer;
- important uncertainty.

Do not save ordinary conversational filler by default.
