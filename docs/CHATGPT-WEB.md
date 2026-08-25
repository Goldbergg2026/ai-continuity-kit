# Ordinary ChatGPT web + GitHub

## Field-tested entrypoint workflow

**Status:** field-tested on 2026-08-25 in an ordinary ChatGPT web chat. This is compatibility evidence for one real setup, not a guarantee that every ChatGPT account exposes the same GitHub capabilities.

The useful part is simple: **you do not need Codex, ChatGPT Work, or a separate API runtime just to make the repository act as the continuity entrypoint.**

In the tested setup, ordinary ChatGPT could start from one persistent instruction, open a connected GitHub repository, read `START.md`, and then follow the repository's routing rules to the files relevant to the current request.

```text
Custom Instructions
        ↓
connected GitHub repository
        ↓
START.md
        ↓
route to the relevant owner/context
        ↓
normal ChatGPT conversation
```

## What you need

1. A continuity repository that ChatGPT is allowed to access. For real personal or work context, keep it **private**.
2. GitHub connected in ChatGPT under **Settings → Apps → GitHub**, with access granted to that repository.
3. ChatGPT **Custom Instructions** enabled under **Settings → Personalization → Custom Instructions**.
4. A stable entrypoint such as `START.md` in the repository.

OpenAI documents Custom Instructions as available in ChatGPT on web, desktop, iOS, and Android. OpenAI also documents GitHub repository access in ChatGPT, but notes that GitHub App availability can vary by plan and experience. In particular, a feature may be available in one ChatGPT experience and not exposed in another.

Official references:

- [OpenAI Help — ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)
- [OpenAI Help — Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

## Recommended Custom Instruction

Replace the placeholder repository name with your own private continuity repository:

```text
At the start of every new chat, use the connected GitHub repository <owner>/<continuity-repo>, branch main, and open START.md before the first substantive answer.

Follow the routes declared there and load only the files relevant to my current request. Do not read the whole repository by default.

If GitHub, the repository, or START.md cannot be accessed, say so explicitly instead of substituting old memory or guessing.
```

The instruction stays small on purpose. Stable policy belongs in the repository; Custom Instructions only tell ChatGPT **where to enter**.

## What was actually verified

The field-tested behavior was:

- a new **ordinary ChatGPT web chat** started with the persistent entrypoint rule;
- ChatGPT accessed the connected GitHub repository;
- it opened the designated `START.md` entrypoint;
- it followed repository-defined routing instead of requiring the entire knowledge base in the prompt;
- relevant repository files could then supply durable context for normal chat work.

That is the important compatibility result: **a Git-backed continuity layer can work directly from ordinary ChatGPT when the required GitHub access is available.**

This statement intentionally does **not** mean:

- every account or plan exposes GitHub in ordinary chat;
- every future ChatGPT UI will use the same menu names;
- a successful test today proves permanent future product behavior;
- GitHub access itself grants permission for destructive or unrelated changes.

## Quick verification

After configuring the instruction, open a fresh ordinary ChatGPT chat and ask something that requires repository context, for example:

> Read the configured entrypoint and tell me which file owns the current project state. Do not infer it from chat memory.

A good result should show that ChatGPT uses the repository route. If repository access is unavailable, the correct behavior is to report that limitation rather than pretending the entrypoint was read.

## Why this pattern matters

Without an entrypoint rule, every new chat may need a long manual prompt telling the assistant where everything lives.

With one stable entrypoint:

```text
one small persistent instruction
        ↓
repository-owned routing
        ↓
progressive context loading
```

The repository carries the durable structure; the chat stays lightweight.

Back to the [5-minute quick start](QUICKSTART.md).
