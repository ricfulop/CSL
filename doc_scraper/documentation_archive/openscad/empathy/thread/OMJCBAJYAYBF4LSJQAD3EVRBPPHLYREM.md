---
url: https://lists.openscad.org/empathy/thread/OMJCBAJYAYBF4LSJQAD3EVRBPPHLYREM
scraped_at: 2025-09-08T16:28:14.622751
title: Untitled
---

[ ![](/empathy/images/logo.png) ]( https://lists.openscad.org/empathy)

____

Hi,

Guest

![Pic](/empathy/images/default.jpg)

__

Sign In

Remember Me

Sign In

[ Click here to sign up for new account. ](/register)

[ Forgot your password? ](/password/reset)

###
[discuss@lists.openscad.org](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

OpenSCAD general discussion Mailing-list

[View all
threads](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

###  Re: Can I get a previous nightly build?

![](https://www.gravatar.com/avatar/b19e2e8fa3505b0c13f5f8aba31dab95?d=blank&s=100)

MK

Marius Kintel

Thu, Sep 4, 2025 3:04 AM

Try some older versions as well in case this is a recent issue.  
Perhaps someone else here on Windows have better experiences they can share?

-Marius

____

On Sep 3, 2025, at 22:33, Nathan
Sokalski[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com) wrote:

Thank you for that information. I tried getting
OpenSCAD-2025.08.31-x86-64-Installer.exe, and it did not work. I had to turn
off some security things like Windows Defender (but I think I had to do this
with the other times when it did work, so I doubt that is the problem), and
when I run the installer, it installs with (what looks like) no problem, but
when I open a model, the console says

Loaded design …  
Used file cache size: 6 files

The title also includes "OpenSCAD (Not Responding)". I don't know if Windows
Defender is causing a problem during installation, or if there is something
else, but I'm running out of ideas.

Try some older versions as well in case this is a recent issue. Perhaps
someone else here on Windows have better experiences they can share? -Marius >
On Sep 3, 2025, at 22:33, Nathan Sokalski <njsokalski@hotmail.com> wrote: > >
Thank you for that information. I tried getting
OpenSCAD-2025.08.31-x86-64-Installer.exe, and it did not work. I had to turn
off some security things like Windows Defender (but I think I had to do this
with the other times when it did work, so I doubt that is the problem), and
when I run the installer, it installs with (what looks like) no problem, but
when I open a model, the console says > > Loaded design … > Used file cache
size: 6 files > > The title also includes "OpenSCAD (Not Responding)". I don't
know if Windows Defender is causing a problem during installation, or if there
is something else, but I'm running out of ideas. >

![](https://www.gravatar.com/avatar/a313c0e6b5e5da0a7c00ccc5880e4a68?d=blank&s=100)

MM

Michael Marx (spintel)

Thu, Sep 4, 2025 4:17 AM

Nathan,

See my posts 'Windows 11, Long OpenSCAD start-up time', for me it takes ~20-25
seconds for the 'Not Responding' to clear.  
Once running it seems normal.

I raised a GitHub issue:

<https://github.com/openscad/openscad/issues/6158#issuecomment-3247753385>

So it can be investigated. See if that describes your behaviour.

Let us know if it does not eventually give you a normal GUI window.

____

but when I open a model, the console says

Is that by clicking on a .scad file to Open OpenSCAD?

I don't see that.

Try just running OpenSCAD and select 'New' (presuming you get the welcome
screen), instead of clicking on a .scad file.

I think it has Design/Automatic-Reload&Preview set by default (turn that off),
so depending on your model that may add some start time.

(presuming from file cache = 6 files, that it may not be trivial model?)

* * *

From: Marius Kintel via Discuss
[mailto:[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)]  
Sent: Thursday, September 04, 2025 1:05 PM  
To: Nathan Sokalski via Discuss  
Cc: Nathan Sokalski; Marius Kintel  
Subject: [OpenSCAD] Re: Can I get a previous nightly build?

Try some older versions as well in case this is a recent issue.

Perhaps someone else here on Windows have better experiences they can share?

-Marius

On Sep 3, 2025, at 22:33, Nathan Sokalski
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com) wrote:

Thank you for that information. I tried getting
OpenSCAD-2025.08.31-x86-64-Installer.exe, and it did not work. I had to turn
off some security things like Windows Defender (but I think I had to do this
with the other times when it did work, so I doubt that is the problem), and
when I run the installer, it installs with (what looks like) no problem, but
when I open a model, the console says

Loaded design …

Used file cache size: 6 files

The title also includes "OpenSCAD (Not Responding)". I don't know if Windows
Defender is causing a problem during installation, or if there is something
else, but I'm running out of ideas.

Nathan, See my posts 'Windows 11, Long OpenSCAD start-up time', for me it
takes ~20-25 seconds for the 'Not Responding' to clear. Once running it seems
normal. I raised a GitHub issue:
https://github.com/openscad/openscad/issues/6158#issuecomment-3247753385 So it
can be investigated. See if that describes your behaviour. Let us know if it
does not eventually give you a normal GUI window. > but when I open a model,
the console says Is that by clicking on a .scad file to Open OpenSCAD? I don't
see that. Try just running OpenSCAD and select 'New' (presuming you get the
welcome screen), instead of clicking on a .scad file. I think it has
Design/Automatic-Reload&Preview set by default (turn that off), so depending
on your model that may add some start time. (presuming from file cache = 6
files, that it may not be trivial model?) _____ From: Marius Kintel via
Discuss [mailto:discuss@lists.openscad.org] Sent: Thursday, September 04, 2025
1:05 PM To: Nathan Sokalski via Discuss Cc: Nathan Sokalski; Marius Kintel
Subject: [OpenSCAD] Re: Can I get a previous nightly build? Try some older
versions as well in case this is a recent issue. Perhaps someone else here on
Windows have better experiences they can share? -Marius On Sep 3, 2025, at
22:33, Nathan Sokalski <njsokalski@hotmail.com> wrote: Thank you for that
information. I tried getting OpenSCAD-2025.08.31-x86-64-Installer.exe, and it
did not work. I had to turn off some security things like Windows Defender
(but I think I had to do this with the other times when it did work, so I
doubt that is the problem), and when I run the installer, it installs with
(what looks like) no problem, but when I open a model, the console says Loaded
design … Used file cache size: 6 files The title also includes "OpenSCAD (Not
Responding)". I don't know if Windows Defender is causing a problem during
installation, or if there is something else, but I'm running out of ideas.

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

