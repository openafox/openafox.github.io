---
layout: post
title: Editing a slave hard drive registry.
tag:
    - Lifehacks
    - PC
category: Programming

excerpt: Editing the registry of a secondary hard drive.
---

1. Open *regedit* (Start - run - regedit)
2. Click *HKEY_LOCAL_MACHINE*
3. Click *File* -> *Load Hive*
4. Browse to the slaves *windows\system32\config*
5. Select the *System* or *Software* file (no file extensions)
6. Type a temporary name and click *Open*
7. Apply fixes or find needed *KEYS*
8. When Done - Click the *File* menu and choose *Unload Hive*
9. Close *regedit* - be happy an move on with your life
