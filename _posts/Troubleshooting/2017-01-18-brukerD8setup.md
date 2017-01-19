---
layout: post
title: Installing Bruker D8 Discover software on a new measurement computer.
tag: Fixed
category: Troubleshooting

excerpt: Our Bruker D8 measurement computer died. This is how I installed the software on a 'new' XP machine.
---

On Thursday I had 2 different users tell me the XRD computer would not boot. Its power button was flashing amber and after some internet searching and a few quick diagnostics(unplugging some stuff) I decided it was likely either the mother board or power supply. Knowing that system had blue screened a number of times over the last year, I decided the least painful option would be replacement.

There are 2 replacement options:

1. Pay Bruker a bunch of money(10K+) for a new computer (Win 7), software, and install.
2. Take a similar XP system and attempt to get the software installed (could be easier said then done).

So I thought I would try the install.
Here is the list of what worked (I am not including the numerous steps I took that didn't...):

0. Install old hard drive as slave to get config files (I have backups now but thank goodness that worked)
   * My users also appreciated that I was able to save their data
1. Install Hardware: CronosPlus PCI Board and License Dongle
  * Restart computer and cancel prompts to install drivers
2. Install Bruker software (from CDs: *DIFFRACplus Basic Measurement and Evaluation*)
  * Also on the *Firmware & Software Tools* CD copy the D8 Tools program into the DIFFPLUS folder
3. Install dongle driver (On the *Measurement* CD)
4. Setup static IP: Does not matter which network adapter just as long as the instrument is connected to it
  * 192.168.21.1
  * Subnet mask = default (255.255.255.0)
  * Leave all else blank
  * Also turn off any firewalls for that adapter
5. Restart Computer
6. Open *XRD Config*
  * Load your most recent conf file (ex. [diff_in1.cnf](https://drive.google.com/open?id=0B9fsrnoZMTD_dFd6eFZWLWctdzg))
  * In *XRD Config* click the download CNF button (It should work without a hitch if the system is on)
7. Copy the D8Tools back up [COMPORT.CFN](https://drive.google.com/open?id=0B9fsrnoZMTD_LUdGNzRUb3lDbG8) file into the D8Tools folder (replace what is there)
8. Start D8Tools and make sure you can connect to the system
9. Install [Video Laser Software](https://drive.google.com/open?id=0B9fsrnoZMTD_WVRZWTBWS2RSSVU)
  * Open Video_1.5/ReadMe.TXT and follow the instructions (For our system options are - CronosPlus, color video, and 4Mb)
10. After restart system should be good to go except for the user management system and some issues that occur when adding users

### User Management system

This uses a fairly simple python program I developed plus some OS configuration. The setup is described below:

1. Create a new user account - start it as an admin (control panel - user accounts - Create new account)
2. Remove most programs from C:/Documents and Settings/User/Start Menu
   * This limits users ability to do stuff easily that they shouldn't be doing
3. Log into the new account and right click on the start menu and click options
   * Remove all unneeded features - ex. control panel
4. Log out and back into the admin account - change the new user to a limited account
5. Copy compiled Program use tracker app [PUTAPP](https://github.com/openafox/put_app){: target="_blank"}
6. Follow instructions in the Readme to setup

### Getting XRD Commander and Video to work properly on the user account

This was a bit of a pain to figure out but is "fairly simple" in the end.
It required copying all the associated registry keys from the Admin account to the user account. To do this:

1. Log into the user account then "switch accounts" to the admin account
2. Open Regedit and Navigate to *HKEY_Users*
3. Navigate to the Admins folder/Software
   * Each user has at least 2 files each start with a user key (a long string some how related to your user name) and the long string with *Classes*
4. Select the first *Bruker AXS* Key and click *File -> Export* - Name it what ever you want
   * Repeat this for the other *Bruker AXS, Matrox, and Matrox Imaging*
5. Either copy the Key name of the user account or note the difference from the admin (likely just a different number at the end)
6. Open each of the exported registry files in a text editor
7. Change the Key base to the user name found in step 5
8. Once all the files have been edited double click them to apply the edits
   * This should add the extracted keys to the *User/Software* registry
9. Delete the extracted registry files (no need to keep them) and restart

That should do it. Hopefully I did not miss anything. Good Luck!

