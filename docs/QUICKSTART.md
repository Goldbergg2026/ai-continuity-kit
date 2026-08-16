# 5-minute quick start

## 1. Copy the starter

Copy the contents of `starter/` into a new **private** repository that will hold your own continuity data.

## 2. Fill only what you know

Edit:

- `context/PREFERENCES.md` — how you want the assistant to communicate;
- `context/FACTS.md` — a few durable facts that are genuinely useful;
- `context/MEMORY.md` — reusable lessons only after they exist.

Leave unknowns unknown. Do not create a biography just because there is an empty heading.

## 3. Use START.md as the entrypoint

Configure your workflow so ChatGPT or Codex reads `START.md` first when repository access is available.

If your current ChatGPT/Codex surface cannot automatically read a repository, paste only the relevant starter file(s) into the session rather than dumping the whole repository.

## 4. Add a project when needed

Copy `projects/example/` and rename the folder.

Keep:

- `STATE.md` — where the work is now;
- `FACTS.md` — verified reusable facts;
- `MEMORY.md` — lessons and pitfalls.

## 5. Close the loop

After meaningful work:

1. verify the result;
2. update the correct owner;
3. record only the useful delta;
4. commit it.

That is enough for the first version.
