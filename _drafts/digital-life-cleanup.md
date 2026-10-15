---
layout: post
title: Cleaning Up My Digital Life
category: Programming   # TODO: or a new category? (Projects/Notes)
tags:
  - Digital Cleanup
  - Google Photos
  - AI Agents
excerpt: Untangling years of digital clutter, starting with 20,000 of my wife's photos that Google Photos quietly copied into my library.
---
**TODO:** 1–2 lines on what prompted the cleanup (new kid? storage bill? just fed up?).

<!-- more -->

## 20,000 photos that weren't mine

Years ago I turned on Google Photos partner sharing with my wife, with "auto-save" on. It saved her
entire history into my library, all the way back to 1992. We share photos other ways now, but removing the
partner doesn't remove what was saved, and Google has no "unsave all" button.

I was sure there used to be an easier way. There isn't. The best option is still a workaround from
[a 2020 Reddit thread](https://www.reddit.com/r/googlephotos/comments/jhn6ym/can_you_delete_photos_from_partner_sharing/):
select her saved photos, share them into a conversation, then trash them from that conversation's
"All photos". Her originals stay untouched.

The catch: doing that by hand means hand-selecting tens of thousands of photos, in batches of ~450, in a
partner view that loads painfully slowly.

So I had Claude do it, driving the browser:
- A script selects only the photos with the little "saved" cloud icon, newest first, 450 at a time.
- It shares the batch to an empty conversation with my other account, checks the dates match, and trashes them.
- Repeat. Forty-some batches.

What went wrong along the way (the useful part):
- Pressing Escape clears a 450-photo selection. Learned that one the hard way.
- My screensaver kicked in and the page just stopped loading. I thought Google was throttling me; nope.
- Clicking Share with 450 selected freezes the page for up to a minute.
- One photo refused to land in the conversation no matter what. Deleted that one by hand.
- Token use climbs with every batch, since the AI re-reads the whole conversation each step. Splitting the
  batches into short-lived helper agents fixed most of that.

I turned the whole thing into scripts plus a Claude skill so nobody else has to figure this out:
[openafox/google-photos-partner-cleanup](https://github.com/openafox/google-photos-partner-cleanup). The scripts work in the browser
console without any AI.

**TODO:** did it actually free up storage once Trash emptied? How much?

## TODO: Next area

**TODO:** what else is part of the cleanup? (email, old accounts, cloud drives, passwords, subscriptions,
devices…) One section each, same pattern: what the mess was, what fixed it, what broke.

## Files and links
- Scripts + Claude skill: [openafox/google-photos-partner-cleanup](https://github.com/openafox/google-photos-partner-cleanup)
- [Original Reddit workaround](https://www.reddit.com/r/googlephotos/comments/jhn6ym/can_you_delete_photos_from_partner_sharing/)
