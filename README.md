# Voidex

This is a python file that will allow any android (with android 10+) 
to have a DeX like interface on an external montitor.

## Prerequisites

To run, you must have installed the following:

- ### On pc:
    * Python3
    * Scrcpy
    * Android debug bridge
- ### On phone:
    * Taskbar (Ver 6 or above)

## Mobile Setup 

Once you have installed the prerequisites, you will need to change some 
settings for the script to work.

**YOU WILL NEED DEVELOPER MODE ENABLED FOR THIS**

- ### Launcher settings
    * You will need to change the default launcher to taskbar in your settings.
    for android, this is under `apps > default apps > launcher`. Select taskbar.
- ### Developer settings
    To enter developer settings, scroll to the bottom of your settings app and select 
    `Developer options`.
    * Enable usb debugging
    * Enable `Force desktop mode on external displays`
    * Enable freeform windows
    * Enable `Force allow apps on external`
    * Enable `Force activities to be resizable`
    * Enable multi window for all apps
    This will require a restart.
- ### Taskbar settings
    * Enable desktop mode (make sure it is the checkbox and not the slider)
    Feel free to play around with the rest of the settings, as they are all mostly customisability.

## Pc Setup

Before starting this step, make sure that your device is recognised in adb.
To do this, use the command `adb devices`. If the output is blank or says unauthorised, 
unplug your device and plug it back in, then accept the usb debugging prompt. When your device 
is connected, it should say `device` next to it when you type in the command.

## Running the file

To run the file, open a terminal and enter `python3 voidex.py`. There is some user input, but you do not
have to run it as root for it to work. once you enter the information, a new window will pop-up, displaying
a secondary display. To exit, simply close the window and the session will be deleted automatically. 

> **Warning:** Will not work on windows!
> The grep command om line 5 will need to be changed to findstr syntax to avoid errors.

## Config

To change screen size, reference line 4. In my limited testing, i have found it to be quite buggy outside
of 1080p or 4k.

**DO NOT CANGE THE DENSITY WITHOUT CHANGING IT IN TASKBAR** Not having a consistent density
causes visual artifacting and an overall loss in quality

The current bitrate of 300,000 b/s was a complete stab in the dark, but works best for 1080p or lower.
this can be changed to a higher value for thunderbolt or usb 3.0 connections.

## Final notes

All of this was tested on an ubuntu 20.04 non-lts laptop with a Samsung M13 running Oneui core(android 13). 
All above software is on the latest versions from either apt or the google play store, and other versions may not have the desired functions. The connection was a non thunderbolt usb 2.0 cable that was running at the aforementioned 300,000 b/s bitrate. This is untested on windows, so if it doesn't work, that will probably be your issue.