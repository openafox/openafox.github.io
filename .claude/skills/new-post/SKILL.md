---
name: new-post
description: Draft a blog post for openafox.com from Austin's rough notes (project write-up or tech note) into _drafts/, in his voice. Use when he shares notes, photos, or a project to write up, or asks to polish a draft.
---

# New post

Turn rough notes into a draft Austin will polish with you. He supplies the facts; you
supply structure and prose in his voice.

## Steps

1. **Pick the type.** *Project write-up* (something built, fixed, or made) or *tech note*
   (how to do X, reference he'll come back to). Ask only if it's genuinely unclear.
2. **Read `voice.md`** in this folder. Read one reference post it lists only if needed.
3. **Choose a slug**: short, lowercase, hyphenated (`garage-shelf-build`). Confirm it if
   the notes don't make it obvious.
4. **Images**: if he gave photos, process them first with the add-images skill
   (`python3 -I .claude/skills/add-images/process_images.py <slug> <paths>`) and use the
   Markdown lines it prints.
5. **Write `_drafts/<slug>.md`** using the template below. Leave out sections the notes
   have nothing for rather than padding them.
6. **Report back** briefly: draft path, the list of TODOs, and how to preview:
   `./serve.sh --drafts` → http://localhost:4000.

## Rules
- **Never invent facts.** No made-up numbers, dates, part names, outcomes, or motives.
  Where a gap matters, write a visible marker: `**TODO:** what size was the bolt?`
- Keep his wording where his notes already say it well.
- Drafts stay out of git until `/publish` (the repo is public).

## Polishing together
When he edits a draft or says what to change, apply it, then look at *what kind* of
change it was. If a pattern shows up (cuts intros, prefers fewer headings, more detail on
failures), propose a one-line addition to "Learned from polishing" in `voice.md`, and add
it only once he agrees.

## Front matter

```yaml
---
layout: post
title: Plain descriptive title
category: Projects        # or Notes
tags:
  - Woodworking
excerpt: One sentence on what this is and why it exists.
# last_updated: YYYY-MM-DD   # tech notes: set when revising an already-published note
---
```

## Template: project write-up

```markdown
<1–3 sentences: what it is and what prompted it>

## <What I was going for>
Goal, constraints, budget/time if he mentioned them.

## <How I built it>
Steps, materials, tools, photos inline. Drawings or models here.

## <What went wrong / what I'd change>
Failures, fixes, lessons.

## <Result>
Where it ended up, photos, what's next.

## Files and links
Repos, models, parts lists, sources.
```

## Template: tech note

```markdown
<1–2 sentences: the problem and the context it came up in>

## Steps
1. …

## Gotchas
- …

## Sources
- …
```
