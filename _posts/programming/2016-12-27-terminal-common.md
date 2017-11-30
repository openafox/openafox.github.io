---
layout: post
title: Common Terminal Commands.
tag: Useful
category: Programming

excerpt: A list of common Terminal Commands for my reference and maybe yours.
---

I tend to forget a lot of this stuff as I don't use it often (I am not a computer scientist by trade), so here is a list of useful terminal commands.
filpath

* Copy a file

  ~~~bash
  cp [options] source destination
  ~~~
  Options:
  -f = force,
  -R = recursive,
  -v = verbose

* Permissions

  Current permissions

  ~~~bash
  ls -l file
  ~~~

  Change permissions

  ~~~bash
  chmod value file
  ~~~

  Value: 3 digit code for owner, group, all

  7 = no restrictions, 6 = read write, 5 = read execute, 4 = read, 0 = no access

* Move/change name of file

  ~~~bash
  mv [options] source destination
  ~~~

  Options: -f = force, -v = verbose

* Find files and or delete matching a pattern
  ~~~bash
  find . -name "*.bak" -type f

  find . -name "*.bak" -type f -delete
  ~~~~


* Find a file or text in a file

  ~~~bash
  grep [options] search_pattern [file_pattern]
  ~~~
  grep = general regular expression program

  search_pattern =  a regular expression or string in

  file_pattern = a file or directory or file pattern ex. \*.html

  Options:
  -i = ignore case,
  -r = recursive,
  -l = just file names,
  -n = show line number

  +many more [this site][grep] seems to have a pretty complete list with good descriptions

  As for Regular expressions there are lots of great resources out there. I may put a post together with the important to me stuff at some point but here are some resources:

  [Rexegg][regex1]

  [cheatography][regex2]

[grep]:http://www.computerhope.com/unix/ugrep.htm
{: target="_blank"}
[regex1]:http://www.rexegg.com/
{: target="_blank"}
[regex2]:https://www.cheatography.com/davechild/cheat-sheets/regular-expressions/
{: target="_blank"}

