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

Austin's bar: flag what is **wrong, harmful, or exposes someone**, not what a stranger
might conceivably misread. He writes candidly in his own voice and keeps his opinions;
that is the point of the blog. Over-flagging wastes his time.

Flag:
- **Sensitive info about other people**: contact details, where they live, health, legal
  or money matters, kids' full names, anything they'd reasonably expect to stay private.
  Names, friendly descriptions, and backgrounds shared warmly are fine.
- **Private details about Austin**: home address, routine, travel dates while away,
  health, finances.
- **Work confidentiality**: employer-internal info, unreleased results, client names,
  NDA material, screenshots of internal systems or other people's data.
- **Demeaning content**: slurs, mocking a person or group, stereotypes used as put-downs.
- **Factual claims that are wrong** when stated as fact (suggest a source or framing like
  "the museum presented it as…", not deletion).
- **Safety**: instructions where a mistake could hurt someone or a system (electrical,
  chemicals, lasers, disabling security) without a warning.

Don't flag: his opinions or political views, accurate cultural observations, light
affectionate jokes, drinking/partying, mild profanity, quotes he attributes correctly.

## Report format

Keep it short. Group by severity, quote the line, suggest an option:

```
Blockers (must fix before push)
- line 42 [secret] `api_key = ...` → remove; revoke the key
Worth a look
- line 12 [private person] friend's home street named → drop the street?
- line 30 [fact] "X happened in 1950" → it was 1945; fix or attribute
Clean: PII scan, images
```

If nothing turns up, say so in one line.
