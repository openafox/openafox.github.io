---
name: idea
description: Capture a blog post idea in IDEAS.md, or list/pick from saved ideas. Use when Austin says "idea:", "add to the idea box", or asks what he could write about next.
---

# Idea box

`IDEAS.md` at the repo root is a plain checklist. It is excluded from the built site but
visible on GitHub, so keep entries free of anything private.

## Add
Append under `## Inbox`, newest last, keeping his words:

```markdown
- [ ] 2026-10-12 — <idea in a line> (<optional pointers: repo, photos folder, notebook>)
```

Commit with `Idea: <short idea>` and push only if he asks; otherwise leave it for the
next commit.

## List / pick
Show the open items briefly. When he picks one, check it off (`- [x]`), and start
`/new-post` with whatever notes he has.
