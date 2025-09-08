---
url: https://lists.openscad.org/empathy/thread/NCF57LG735PPBWYC7K64NTZIIX5DDZVG
scraped_at: 2025-09-08T16:28:13.653139
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

###  Windows 11, Long OpenSCAD start-up time?

![](https://www.gravatar.com/avatar/a313c0e6b5e5da0a7c00ccc5880e4a68?d=blank&s=100)

MM

Michael Marx (spintel)

Tue, Sep 2, 2025 9:09 AM

Is there a known issue with recent builds and Windows 11?

I just installed OpenSCAD in Windows 11 for the first time.

OpenSCAD Nightly version 2025.08.31 (git f0e3acd24)

When starting it takes ~20s to paint the editor/preview/console window.

ie the Window box with title shows straight away, but with blank contents.  
During which '(Not Responding)' is shown on the title bar with a blue spinner
cursor.

If the 'welcome screen' option is set, the welcome screen displays quickly,  
but then doing anything shows the above behaviour.

2021.01 starts up promptly.

Is there a known issue with recent builds and Windows 11? I just installed
OpenSCAD in Windows 11 for the first time. OpenSCAD Nightly version 2025.08.31
(git f0e3acd24) When starting it takes ~20s to paint the
editor/preview/console window. ie the Window box with title shows straight
away, but with blank contents. During which '(Not Responding)' is shown on the
title bar with a blue spinner cursor. If the 'welcome screen' option is set,
the welcome screen displays quickly, but then doing anything shows the above
behaviour. 2021.01 starts up promptly.

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Tue, Sep 2, 2025 10:55 AM

I bought a new PC in part because of slow OpenSCAD startup times. I  
have no idea why it needs to take so long, but that was the only  
solution I could find.

Jon

On 9/2/2025 5:09 AM, Michael Marx (spintel) via Discuss wrote:

____

Is there a known issue with recent builds and Windows 11?

I just installed OpenSCAD in Windows 11 for the first time.

OpenSCAD Nightly version 2025.08.31 (git f0e3acd24)

When starting it takes ~20s to paint the editor/preview/console window.

ie the Window box with title shows straight away, but with blank contents.  
During which '(Not Responding)' is shown on the title bar with a blue  
spinner cursor.

If the 'welcome screen' option is set, the welcome screen displays  
quickly,  
but then doing anything shows the above behaviour.

2021.01 starts up promptly.

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

I bought a new PC in part because of slow OpenSCAD startup times. I have no
idea why it needs to take so long, but that was the only solution I could
find. Jon On 9/2/2025 5:09 AM, Michael Marx (spintel) via Discuss wrote: > >
Is there a known issue with recent builds and Windows 11? > > I just installed
OpenSCAD in Windows 11 for the first time. > > OpenSCAD Nightly version
2025.08.31 (git f0e3acd24) > > When starting it takes ~20s to paint the
editor/preview/console window. > > ie the Window box with title shows straight
away, but with blank contents. > During which '(Not Responding)' is shown on
the title bar with a blue > spinner cursor. > > If the 'welcome screen' option
is set, the welcome screen displays > quickly, > but then doing anything shows
the above behaviour. > > 2021.01 starts up promptly. > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org \-- This email
has been checked for viruses by AVG antivirus software. www.avg.com

![](https://www.gravatar.com/avatar/901519ec4216a54cde3ac2d5a018b082?d=blank&s=100)

P

pca006132

Tue, Sep 2, 2025 2:08 PM

Sounds like OpenGL related issue...

What is the status of MSVC build? I think we need someone to use MSVC to  
build the binary and do profiling on it.

On 9/2/25 18:55, Jon Bondy via Discuss wrote:

____

I bought a new PC in part because of slow OpenSCAD startup times. I  
have no idea why it needs to take so long, but that was the only  
solution I could find.

Jon

On 9/2/2025 5:09 AM, Michael Marx (spintel) via Discuss wrote:

____

Is there a known issue with recent builds and Windows 11?

I just installed OpenSCAD in Windows 11 for the first time.

OpenSCAD Nightly version 2025.08.31 (git f0e3acd24)

When starting it takes ~20s to paint the editor/preview/console window.

ie the Window box with title shows straight away, but with blank  
contents.  
During which '(Not Responding)' is shown on the title bar with a blue  
spinner cursor.

If the 'welcome screen' option is set, the welcome screen displays  
quickly,  
but then doing anything shows the above behaviour.

2021.01 starts up promptly.

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

[http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient](http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient)  
Virus-free.www.avg.com  
[http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient](http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient)

<#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

Sounds like OpenGL related issue... What is the status of MSVC build? I think
we need someone to use MSVC to build the binary and do profiling on it. On
9/2/25 18:55, Jon Bondy via Discuss wrote: > > I bought a new PC in part
because of slow OpenSCAD startup times. I > have no idea why it needs to take
so long, but that was the only > solution I could find. > > Jon > > > On
9/2/2025 5:09 AM, Michael Marx (spintel) via Discuss wrote: >> >> Is there a
known issue with recent builds and Windows 11? >> >> I just installed OpenSCAD
in Windows 11 for the first time. >> >> OpenSCAD Nightly version 2025.08.31
(git f0e3acd24) >> >> When starting it takes ~20s to paint the
editor/preview/console window. >> >> ie the Window box with title shows
straight away, but with blank >> contents. >> During which '(Not Responding)'
is shown on the title bar with a blue >> spinner cursor. >> >> If the 'welcome
screen' option is set, the welcome screen displays >> quickly, >> but then
doing anything shows the above behaviour. >> >> 2021.01 starts up promptly. >>
>> >> _______________________________________________ >> OpenSCAD mailing list
>> To unsubscribe send an email todiscuss-leave@lists.openscad.org > >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > Virus-free.www.avg.com >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > > > <#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2> >
> _______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/605cbbee6fefc10271a27ee79bba5157?d=blank&s=100)

TP

Torsten Paul

Tue, Sep 2, 2025 2:17 PM

On 02.09.25 16:08, pca006132 via Discuss wrote:

____

What is the status of MSVC build? I think we need someone to use MSVC to  
build the binary and do profiling on it.

Not 100% finished, but here's a current status:

<https://github.com/openscad/openscad/issues/6123>

Otherwise, make sure remote 3d printing services are disabled.  
(Disabled is the default)

Preferences -> 3D Print -> General -> "Enable remote print services"

ciao,  
Torsten.

On 02.09.25 16:08, pca006132 via Discuss wrote: > What is the status of MSVC
build? I think we need someone to use MSVC to > build the binary and do
profiling on it. Not 100% finished, but here's a current status:
https://github.com/openscad/openscad/issues/6123 Otherwise, make sure remote
3d printing services are disabled. (Disabled is the default) Preferences -> 3D
Print -> General -> "Enable remote print services" ciao, Torsten.

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Tue, Sep 2, 2025 2:18 PM

On 9/2/2025 2:09 AM, Michael Marx (spintel) via Discuss wrote:

____

Is there a known issue with recent builds and Windows 11?

It's known. I believe Torsten understands what's causing it, if perhaps  
not why.

I don't immediately see an issue filed.

On 9/2/2025 2:09 AM, Michael Marx (spintel) via Discuss wrote: > > Is there a
known issue with recent builds and Windows 11? > It's known. I believe Torsten
understands what's causing it, if perhaps not why. I don't immediately see an
issue filed.

![](https://www.gravatar.com/avatar/605cbbee6fefc10271a27ee79bba5157?d=blank&s=100)

TP

Torsten Paul

Tue, Sep 2, 2025 2:20 PM

On 02.09.25 16:18, Jordan Brown via Discuss wrote:

____

It's known. I believe Torsten understands what's causing it,  
if perhaps not why.

I _thought_ it's related to the GUI font configuration, but I  
have seen other reports that cast some doubt on that.

ciao,  
Torsten.

On 02.09.25 16:18, Jordan Brown via Discuss wrote: > It's known. I believe
Torsten understands what's causing it, > if perhaps not why. I *thought* it's
related to the GUI font configuration, but I have seen other reports that cast
some doubt on that. ciao, Torsten.

![](https://www.gravatar.com/avatar/a313c0e6b5e5da0a7c00ccc5880e4a68?d=blank&s=100)

MM

Michael Marx (spintel)

Tue, Sep 2, 2025 2:35 PM

I'm happy to be the guinea pig on this.  
Library info attached.  
It was a new OpenSCAD install today (W11 new'ish - some weeks), so defaults
mostly.  
The first run, hence defaults, seemed painfully slow, I presumed it was doing
first run configuration overheads.  
But later ones also slow.  
Confirmed Remote Print Services are disabled.

I'll raise an issue tomorrow (00:32hrs now)...

____

\-----Original Message-----  
From: Torsten Paul via Discuss
[mailto:[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)]  
Sent: Wednesday, September 03, 2025 12:21 AM  
To: [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Torsten Paul  
Subject: [OpenSCAD] Re: Windows 11, Long OpenSCAD start-up time?

On 02.09.25 16:18, Jordan Brown via Discuss wrote:

____

It's known. I believe Torsten understands what's causing it,  
if perhaps not why.

I _thought_ it's related to the GUI font configuration, but I  
have seen other reports that cast some doubt on that.

ciao,  
Torsten.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I'm happy to be the guinea pig on this. Library info attached. It was a new
OpenSCAD install today (W11 new'ish - some weeks), so defaults mostly. The
first run, hence defaults, seemed painfully slow, I presumed it was doing
first run configuration overheads. But later ones also slow. Confirmed Remote
Print Services are disabled. I'll raise an issue tomorrow (00:32hrs now)... >
\-----Original Message----- > From: Torsten Paul via Discuss
[mailto:discuss@lists.openscad.org] > Sent: Wednesday, September 03, 2025
12:21 AM > To: discuss@lists.openscad.org > Cc: Torsten Paul > Subject:
[OpenSCAD] Re: Windows 11, Long OpenSCAD start-up time? > > On 02.09.25 16:18,
Jordan Brown via Discuss wrote: > > It's known. I believe Torsten understands
what's causing it, > > if perhaps not why. > > I *thought* it's related to the
GUI font configuration, but I > have seen other reports that cast some doubt
on that. > > ciao, > Torsten. >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

[ __W11slowstartup-libinfo.txt(8.23 KB)
](https://lists.openscad.org/empathy/attachment/679124 "text/plain")

![](https://www.gravatar.com/avatar/63a0c2c7be96f2acab6aa0ba54bb1357?d=blank&s=100)

GS

Guenther Sohler

Thu, Sep 4, 2025 6:31 AM

For me it looks like, the culprit is here:

<https://github.com/openscad/openscad/blob/master/src/gui/Preferences.cc#L747>

Only in windows builds emitting this signal takes 7 seconds.  
Remarkably enough, I cannot find where this signal is connected to, so can  
we skip sleeping 7 seconds here ?

If yes, look forward to reusing that fix.

On Tue, Sep 2, 2025 at 4:36 PM Michael Marx (spintel) via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I'm happy to be the guinea pig on this.  
Library info attached.  
It was a new OpenSCAD install today (W11 new'ish - some weeks), so  
defaults mostly.  
The first run, hence defaults, seemed painfully slow, I presumed it was  
doing first run configuration overheads.  
But later ones also slow.  
Confirmed Remote Print Services are disabled.

I'll raise an issue tomorrow (00:32hrs now)...

____

\-----Original Message-----  
From: Torsten Paul via Discuss
[mailto:[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)]  
Sent: Wednesday, September 03, 2025 12:21 AM  
To: [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Torsten Paul  
Subject: [OpenSCAD] Re: Windows 11, Long OpenSCAD start-up time?

On 02.09.25 16:18, Jordan Brown via Discuss wrote:

____

It's known. I believe Torsten understands what's causing it,  
if perhaps not why.

I _thought_ it's related to the GUI font configuration, but I  
have seen other reports that cast some doubt on that.

ciao,  
Torsten.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

For me it looks like, the culprit is here:
https://github.com/openscad/openscad/blob/master/src/gui/Preferences.cc#L747
Only in windows builds emitting this signal takes 7 seconds. Remarkably
enough, I cannot find where this signal is connected to, so can we skip
sleeping 7 seconds here ? If yes, look forward to reusing that fix. On Tue,
Sep 2, 2025 at 4:36 PM Michael Marx (spintel) via Discuss <
discuss@lists.openscad.org> wrote: > I'm happy to be the guinea pig on this. >
Library info attached. > It was a new OpenSCAD install today (W11 new'ish -
some weeks), so > defaults mostly. > The first run, hence defaults, seemed
painfully slow, I presumed it was > doing first run configuration overheads. >
But later ones also slow. > Confirmed Remote Print Services are disabled. > >
I'll raise an issue tomorrow (00:32hrs now)... > > > \-----Original
Message----- > > From: Torsten Paul via Discuss
[mailto:discuss@lists.openscad.org] > > Sent: Wednesday, September 03, 2025
12:21 AM > > To: discuss@lists.openscad.org > > Cc: Torsten Paul > > Subject:
[OpenSCAD] Re: Windows 11, Long OpenSCAD start-up time? > > > > On 02.09.25
16:18, Jordan Brown via Discuss wrote: > > > It's known. I believe Torsten
understands what's causing it, > > > if perhaps not why. > > > > I *thought*
it's related to the GUI font configuration, but I > > have seen other reports
that cast some doubt on that. > > > > ciao, > > Torsten. > >
_______________________________________________ > > OpenSCAD mailing list > >
To unsubscribe send an email to discuss-leave@lists.openscad.org >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

