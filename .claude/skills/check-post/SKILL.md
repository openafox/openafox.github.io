---
name: check-post
description: Scan a draft or post for secrets, personal info, GPS in images, and content that could be embarrassing or hurtful in public, before it is pushed. Run before any draft or post is committed, and whenever Austin asks for a check.
---

# Check post

The repo is public, so anything pushed (drafts included) is public. Run this before every
commit of a draft or post. It **flags**; Austin decides. Never silently rewrite content
to "fix" a judgment flag.

## 1. Mechanical scan (script)

```bash
python3 -I .claude/skills/check-post/scan.py <post.md> [...]
```

Finds secrets (API keys, tokens, private keys, password assignments, credentials in URLs),
PII (emails other than openafox@gmail.com, phone numbers, street addresses, coordinates,
SSNs, private IPs), editable Google Docs links, Google Drive links, missing images, and
images still carrying GPS. Re-run `/add-images` with `--strip-only` for GPS hits.

**Secrets are blockers.** Remove them before anything is committed. If a secret was ever
pushed, tell Austin it must be revoked/rotated; deleting it from the file is not enough.

## 2. Judgment read (you)

Read the post once with these questions and list anything that applies:

- **Private people**: anyone besides Austin named or identifiable (full names, photos of
  faces, where they live/work, kids). Suggest first name only or "a friend" unless he
  says they're OK with it.
- **Private details about Austin**: home address or neighborhood, daily routine, travel
  dates while away, health, finances, family situations.
- **Work and confidentiality**: employer-internal info, unreleased results, client names,
  anything under NDA, screenshots showing internal systems or other people's data.
- **Hurtful or careless content**: stereotypes or jokes about nationality, culture,
  gender, race, religion, disability, etc.; mocking specific people; slurs. Note: travel
  posts are where this most often slips in.
- **Things that could age badly or affect jobs**: political or hot-button statements,
  drug or heavy drinking references, harsh criticism of named companies or colleagues.
  These aren't forbidden; just make sure they're deliberate.
- **Safety**: instructions where a mistake could hurt someone (electrical, chemicals,
  pressure, lasers) without a warning.

## Report format

Keep it short. Group by severity, quote the line, suggest an option:

```
Blockers (must fix before push)
- line 42 [secret] `api_key = ...` → remove; revoke the key
Worth a look
- line 12 [private person] "Kaoru-san, my homestay mom" → fine if she's OK with it
- line 30 [tone] "Not Mary Jane…" → deliberate?
Clean: PII scan, images
```

If nothing turns up, say so in one line.
