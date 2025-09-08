---
url: https://lists.openscad.org/empathy/thread/TFQY6AS5DNE2M6DIEQLM5YHYGPQDVSFA
scraped_at: 2025-09-08T16:28:24.728401
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

###  Re: Object/module references/geometry values (was Re: Re: Modules as
functions)

![](https://www.gravatar.com/avatar/fef1a057596ac6c3b2880a1b46ce1e19?d=blank&s=100)

RW

Roger Whiteley

Mon, Aug 25, 2025 10:00 AM

On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote:

<snip>

____

The only thing I'd like to see, is a center keyword that if left out,  
defaults to true, not false.

YES x 2

Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask...
but my scary English teacher would have hauled me over the coals [disliked
English, loved Technical Drawing].

I've been rewriting self written modules that accept either spelling, that's
what used to be called defensive programming.

TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated.

Point and click has never been my bag.

So the question is, WIIFM? how will OO make OpenSCAD easier to use? or will it
make obscure geometrical mind bending easier for the use cases that need it?

Roger.

On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote: <snip> >
The only thing I'd like to see, is a center keyword that if left out, >
defaults to true, not false. > YES x 2 Can we have Centre spelt properly
please ;-), yeah I KNOW that's a big ask... but my scary English teacher would
have hauled me over the coals [disliked English, loved Technical Drawing].
I've been rewriting self written modules that accept either spelling, that's
what used to be called defensive programming. TBH the whole OO conversation,
has mostly gone over my head, but I'm with Gene, math != good fun. and FreeCAD
= monumental and pointless steep learning curve when OpenSCAD has a lower
point of useful entry, with the added bonus of developer participation, which
is much appreciated. Point and click has never been my bag. So the question
is, WIIFM? how will OO make OpenSCAD easier to use? or will it make obscure
geometrical mind bending easier for the use cases that need it? Roger.

![](https://www.gravatar.com/avatar/26ae84d97e681e25b603e4df740e8b48?d=blank&s=100)

GB

Glenn Butcher

Mon, Aug 25, 2025 1:32 PM

I know I'm a little late to the whole center/(centre?) discussion, but  
I've 2 cents...

In all my modeling I've used center=true maybe 10 times, mainly to keep  
from having to type some sort of translate /2 thing. A lot of my  
modeling involves difference() to cut precise angles in wall and roof  
components, so I want some corner of the cutter on the z axis (sometimes  
x or y) to rotate it to a particular angle prior to moving it to where  
it'll do the cutting. I find myself in the majority of primitives  
automatically adding 'translate[0,0,0] rotate[0,0,0]' to the front of  
it so I can subsequently modify those parameters to spin/move the thing  
where I want. One of these days I might sit down and wrap my head  
around BOSL2 attachments, but not anytime soon....

If there is to be made a IMHO useful change to the center parameter, it  
would be a vector of booleans to selectively center on various axes.  
And, scalar '1' would do all three.

Glenn

On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote:

____

On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote:

<snip>

____

The only thing I'd like to see, is a center keyword that if left out,  
defaults to true, not false.

YES x 2

Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask...
but my scary English teacher would have hauled me over the coals [disliked
English, loved Technical Drawing].

I've been rewriting self written modules that accept either spelling, that's
what used to be called defensive programming.

TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated.

Point and click has never been my bag.

So the question is, WIIFM? how will OO make OpenSCAD easier to use? or will it
make obscure geometrical mind bending easier for the use cases that need it?

Roger.

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

I know I'm a little late to the whole center/(centre?) discussion, but I've 2
cents... In all my modeling I've used center=true maybe 10 times, mainly to
keep from having to type some sort of translate /2 thing. A lot of my modeling
involves difference() to cut precise angles in wall and roof components, so I
want some corner of the cutter on the z axis (sometimes x or y) to rotate it
to a particular angle prior to moving it to where it'll do the cutting. I find
myself in the majority of primitives automatically adding 'translate[0,0,0]
rotate[0,0,0]' to the front of it so I can subsequently modify those
parameters to spin/move the thing where I want. One of these days I might sit
down and wrap my head around BOSL2 attachments, but not anytime soon.... If
there is to be made a IMHO useful change to the center parameter, it would be
a vector of booleans to selectively center on various axes. And, scalar '1'
would do all three. Glenn On 8/25/2025 4:00 AM, Roger Whiteley via Discuss
wrote: > On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote: >
> <snip> > >> The only thing I'd like to see, is a center keyword that if left
out, >> defaults to true, not false. >> > YES x 2 > > Can we have Centre spelt
properly please ;-), yeah I KNOW that's a big ask... but my scary English
teacher would have hauled me over the coals [disliked English, loved Technical
Drawing]. > > I've been rewriting self written modules that accept either
spelling, that's what used to be called defensive programming. > > TBH the
whole OO conversation, has mostly gone over my head, but I'm with Gene, math
!= good fun. and FreeCAD = monumental and pointless steep learning curve when
OpenSCAD has a lower point of useful entry, with the added bonus of developer
participation, which is much appreciated. > > Point and click has never been
my bag. > > So the question is, WIIFM? how will OO make OpenSCAD easier to
use? or will it make obscure geometrical mind bending easier for the use cases
that need it? > > Roger. > > _______________________________________________ >
OpenSCAD mailing list > To unsubscribe send an email todiscuss-
leave@lists.openscad.org

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Mon, Aug 25, 2025 1:50 PM

Jordan you could protect name space by doing something like

$defaults=object(center=true);

Glenn you can position objects in BOSL2 in the way that you want to without  
having to understand attachments. You only need anchoring for that. It’s  
described in the tutorial under “basic object positioning”

Example:

include<BOSL2/std.scad>  
cube(10, anchor=[1,0,0]);

That makes a cube centered in y and z and aligned with the origin in x. So  
the same as translate([5,0,0]) applied to a centered cube.

On Mon, Aug 25, 2025 at 09:33 Glenn Butcher via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I know I'm a little late to the whole center/(centre?) discussion, but  
I've 2 cents...

In all my modeling I've used center=true maybe 10 times, mainly to keep  
from having to type some sort of translate /2 thing. A lot of my modeling  
involves difference() to cut precise angles in wall and roof components, so  
I want some corner of the cutter on the z axis (sometimes x or y) to rotate  
it to a particular angle prior to moving it to where it'll do the cutting.  
I find myself in the majority of primitives automatically adding  
'translate[0,0,0] rotate[0,0,0]' to the front of it so I can subsequently  
modify those parameters to spin/move the thing where I want. One of these  
days I might sit down and wrap my head around BOSL2 attachments, but not  
anytime soon....

If there is to be made a IMHO useful change to the center parameter, it  
would be a vector of booleans to selectively center on various axes. And,  
scalar '1' would do all three.

Glenn  
On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote:

On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote:

<snip>

The only thing I'd like to see, is a center keyword that if left out,  
defaults to true, not false.

YES x 2

Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask...
but my scary English teacher would have hauled me over the coals [disliked
English, loved Technical Drawing].

I've been rewriting self written modules that accept either spelling, that's
what used to be called defensive programming.

TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated.

Point and click has never been my bag.

So the question is, WIIFM? how will OO make OpenSCAD easier to use? or will it
make obscure geometrical mind bending easier for the use cases that need it?

Roger.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Jordan you could protect name space by doing something like
$defaults=object(center=true); Glenn you can position objects in BOSL2 in the
way that you want to without having to understand attachments. You only need
anchoring for that. It’s described in the tutorial under “basic object
positioning” Example: include<BOSL2/std.scad> cube(10, anchor=[1,0,0]); That
makes a cube centered in y and z and aligned with the origin in x. So the same
as translate([5,0,0]) applied to a centered cube. On Mon, Aug 25, 2025 at
09:33 Glenn Butcher via Discuss < discuss@lists.openscad.org> wrote: > I know
I'm a little late to the whole center/(centre?) discussion, but > I've 2
cents... > > In all my modeling I've used center=true maybe 10 times, mainly
to keep > from having to type some sort of translate /2 thing. A lot of my
modeling > involves difference() to cut precise angles in wall and roof
components, so > I want some corner of the cutter on the z axis (sometimes x
or y) to rotate > it to a particular angle prior to moving it to where it'll
do the cutting. > I find myself in the majority of primitives automatically
adding > 'translate[0,0,0] rotate[0,0,0]' to the front of it so I can
subsequently > modify those parameters to spin/move the thing where I want.
One of these > days I might sit down and wrap my head around BOSL2
attachments, but not > anytime soon.... > > If there is to be made a IMHO
useful change to the center parameter, it > would be a vector of booleans to
selectively center on various axes. And, > scalar '1' would do all three. > >
Glenn > On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote: > > On Sat,
2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote: > > <snip> > > >
The only thing I'd like to see, is a center keyword that if left out, >
defaults to true, not false. > > > YES x 2 > > Can we have Centre spelt
properly please ;-), yeah I KNOW that's a big ask... but my scary English
teacher would have hauled me over the coals [disliked English, loved Technical
Drawing]. > > I've been rewriting self written modules that accept either
spelling, that's what used to be called defensive programming. > > TBH the
whole OO conversation, has mostly gone over my head, but I'm with Gene, math
!= good fun. and FreeCAD = monumental and pointless steep learning curve when
OpenSCAD has a lower point of useful entry, with the added bonus of developer
participation, which is much appreciated. > > Point and click has never been
my bag. > > So the question is, WIIFM? how will OO make OpenSCAD easier to
use? or will it make obscure geometrical mind bending easier for the use cases
that need it? > > Roger. > > > _______________________________________________
> OpenSCAD mailing list > To unsubscribe send an email to discuss-
leave@lists.openscad.org > > _______________________________________________ >
OpenSCAD mailing list > To unsubscribe send an email to discuss-
leave@lists.openscad.org

![](https://www.gravatar.com/avatar/26ae84d97e681e25b603e4df740e8b48?d=blank&s=100)

GB

Glenn Butcher

Mon, Aug 25, 2025 2:48 PM

I'm putting the finishing touches on my most recent project, but I'm  
considering starting the next one in BOSL2. That's the thing, once you  
start something in BOSL2, it's gotta be all in that, so I'll have some  
prep work to find equivalents for all that I do in native OpenSCAD.

To that end, it would seem to me that native OpenSCAD is becoming more  
the 'assembly language' of the scripting CAD space, enough primitives  
available to allow more capable stuff like BOSL2. Treat it like that,  
and making breaking changes to the language becomes more problematic...

Oh, here is my most recent project:

The stone walls are a product of three bespoke c++ programs that feed  
OpenSCAD's surface() and polygon() modules. And, the roof segments were  
difference()ed with cutting cubes rotated at the origin...

Glenn

On 8/25/2025 7:50 AM, Adrian Mariano via Discuss wrote:

____

Jordan you could protect name space by doing something like

$defaults=object(center=true);

Glenn you can position objects in BOSL2 in the way that you want to  
without having to understand attachments. You only need anchoring for  
that. It’s described in the tutorial under “basic object positioning”

Example:

include<BOSL2/std.scad>  
cube(10, anchor=[1,0,0]);

That makes a cube centered in y and z and aligned with the origin in  
x. So the same as translate([5,0,0]) applied to a centered cube.

On Mon, Aug 25, 2025 at 09:33 Glenn Butcher via Discuss  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

    
    
     I know I'm a little late to the whole center/(centre?) discussion,
     but I've 2 cents...
    
     In all my modeling I've used center=true maybe 10 times, mainly to
     keep from having to type some sort of translate /2 thing.  A lot
     of my modeling involves difference() to cut precise angles in wall
     and roof components, so I want some corner of the cutter on the z
     axis (sometimes x or y) to rotate it to a particular angle prior
     to moving it to where it'll do the cutting.  I find myself in the
     majority of primitives automatically adding 'translate[0,0,0]
     rotate[0,0,0]' to the front of it  so I can subsequently modify
     those parameters to spin/move the thing where I want.  One of
     these days I might sit down and wrap my head around BOSL2
     attachments, but not anytime soon....
    
     If there is to be made a IMHO useful change to the center
     parameter, it would be a vector of booleans to selectively center
     on various axes. And, scalar '1' would do all three.
    
     Glenn
    
     On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote:
    

____

    
    
    On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote:<snip>
    

____

    
    
    The only thing I'd like to see, is a center keyword that if left out,
     defaults to true, not false.
    
    
     YES x 2
    
     Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask... but my scary English teacher would have hauled me over the coals [disliked English, loved Technical Drawing].	
    
     I've been rewriting self written modules that accept either spelling, that's what used to be called defensive programming.
    
     TBH the whole OO conversation, has mostly gone over my head, but I'm with Gene, math != good fun. and FreeCAD = monumental and pointless steep learning curve when OpenSCAD has a lower point of useful entry, with the added bonus of developer participation, which is much appreciated.
    
     Point and click has never been my bag.
    
     So the question is, WIIFM? how will OO make OpenSCAD easier to use? or will it make obscure geometrical mind bending easier for the use cases that need it?
    
     Roger.
    
     _______________________________________________
     OpenSCAD mailing list
     To unsubscribe send an email todiscuss-leave@lists.openscad.org
    
    
    
     _______________________________________________
     OpenSCAD mailing list
     To unsubscribe send an email to discuss-leave@lists.openscad.org
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

I'm putting the finishing touches on my most recent project, but I'm
considering starting the next one in BOSL2. That's the thing, once you start
something in BOSL2, it's gotta be all in that, so I'll have some prep work to
find equivalents for all that I do in native OpenSCAD. To that end, it would
seem to me that native OpenSCAD is becoming more the 'assembly language' of
the scripting CAD space, enough primitives available to allow more capable
stuff like BOSL2. Treat it like that, and making breaking changes to the
language becomes more problematic... Oh, here is my most recent project: The
stone walls are a product of three bespoke c++ programs that feed OpenSCAD's
surface() and polygon() modules. And, the roof segments were difference()ed
with cutting cubes rotated at the origin... Glenn On 8/25/2025 7:50 AM, Adrian
Mariano via Discuss wrote: > Jordan you could protect name space by doing
something like > > $defaults=object(center=true); > > Glenn you can position
objects in BOSL2 in the way that you want to > without having to understand
attachments. You only need anchoring for > that. It’s described in the
tutorial under “basic object positioning” > > Example: > >
include<BOSL2/std.scad> > cube(10, anchor=[1,0,0]); > > That makes a cube
centered in y and z and aligned with the origin in > x. So the same as
translate([5,0,0]) applied to a centered cube. > > On Mon, Aug 25, 2025 at
09:33 Glenn Butcher via Discuss > <discuss@lists.openscad.org> wrote: > > I
know I'm a little late to the whole center/(centre?) discussion, > but I've 2
cents... > > In all my modeling I've used center=true maybe 10 times, mainly
to > keep from having to type some sort of translate /2 thing. A lot > of my
modeling involves difference() to cut precise angles in wall > and roof
components, so I want some corner of the cutter on the z > axis (sometimes x
or y) to rotate it to a particular angle prior > to moving it to where it'll
do the cutting. I find myself in the > majority of primitives automatically
adding 'translate[0,0,0] > rotate[0,0,0]' to the front of it so I can
subsequently modify > those parameters to spin/move the thing where I want.
One of > these days I might sit down and wrap my head around BOSL2 >
attachments, but not anytime soon.... > > If there is to be made a IMHO useful
change to the center > parameter, it would be a vector of booleans to
selectively center > on various axes. And, scalar '1' would do all three. > >
Glenn > > On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote: >> On Sat,
2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote: >> >> <snip> >> >>>
The only thing I'd like to see, is a center keyword that if left out, >>>
defaults to true, not false. >>> >> YES x 2 >> >> Can we have Centre spelt
properly please ;-), yeah I KNOW that's a big ask... but my scary English
teacher would have hauled me over the coals [disliked English, loved Technical
Drawing]. >> >> I've been rewriting self written modules that accept either
spelling, that's what used to be called defensive programming. >> >> TBH the
whole OO conversation, has mostly gone over my head, but I'm with Gene, math
!= good fun. and FreeCAD = monumental and pointless steep learning curve when
OpenSCAD has a lower point of useful entry, with the added bonus of developer
participation, which is much appreciated. >> >> Point and click has never been
my bag. >> >> So the question is, WIIFM? how will OO make OpenSCAD easier to
use? or will it make obscure geometrical mind bending easier for the use cases
that need it? >> >> Roger. >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email todiscuss-leave@lists.openscad.org >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/678515/200)
](https://lists.openscad.org/empathy/attachment/678515)

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Mon, Aug 25, 2025 2:57 PM

There may be advantages to being entirely in BOSL2 but it is not required.  
Basic openscad still works. You can ease into it, in other words. There are  
many BOSL2 users who don’t use attachments for example.

On Mon, Aug 25, 2025 at 10:48 Glenn Butcher via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I'm putting the finishing touches on my most recent project, but I'm  
considering starting the next one in BOSL2. That's the thing, once you  
start something in BOSL2, it's gotta be all in that, so I'll have some prep  
work to find equivalents for all that I do in native OpenSCAD.

To that end, it would seem to me that native OpenSCAD is becoming more the  
'assembly language' of the scripting CAD space, enough primitives available  
to allow more capable stuff like BOSL2. Treat it like that, and making  
breaking changes to the language becomes more problematic...

Oh, here is my most recent project:

The stone walls are a product of three bespoke c++ programs that feed  
OpenSCAD's surface() and polygon() modules. And, the roof segments were  
difference()ed with cutting cubes rotated at the origin...

Glenn  
On 8/25/2025 7:50 AM, Adrian Mariano via Discuss wrote:

Jordan you could protect name space by doing something like

$defaults=object(center=true);

Glenn you can position objects in BOSL2 in the way that you want to  
without having to understand attachments. You only need anchoring for that.  
It’s described in the tutorial under “basic object positioning”

Example:

include<BOSL2/std.scad>  
cube(10, anchor=[1,0,0]);

That makes a cube centered in y and z and aligned with the origin in x.  
So the same as translate([5,0,0]) applied to a centered cube.

On Mon, Aug 25, 2025 at 09:33 Glenn Butcher via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I know I'm a little late to the whole center/(centre?) discussion, but  
I've 2 cents...

In all my modeling I've used center=true maybe 10 times, mainly to keep  
from having to type some sort of translate /2 thing. A lot of my modeling  
involves difference() to cut precise angles in wall and roof components, so  
I want some corner of the cutter on the z axis (sometimes x or y) to rotate  
it to a particular angle prior to moving it to where it'll do the cutting.  
I find myself in the majority of primitives automatically adding  
'translate[0,0,0] rotate[0,0,0]' to the front of it so I can subsequently  
modify those parameters to spin/move the thing where I want. One of these  
days I might sit down and wrap my head around BOSL2 attachments, but not  
anytime soon....

If there is to be made a IMHO useful change to the center parameter, it  
would be a vector of booleans to selectively center on various axes. And,  
scalar '1' would do all three.

Glenn  
On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote:

On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote:

<snip>

The only thing I'd like to see, is a center keyword that if left out,  
defaults to true, not false.

YES x 2

Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask...
but my scary English teacher would have hauled me over the coals [disliked
English, loved Technical Drawing].

I've been rewriting self written modules that accept either spelling, that's
what used to be called defensive programming.

TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated.

Point and click has never been my bag.

So the question is, WIIFM? how will OO make OpenSCAD easier to use? or will it
make obscure geometrical mind bending easier for the use cases that need it?

Roger.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

There may be advantages to being entirely in BOSL2 but it is not required.
Basic openscad still works. You can ease into it, in other words. There are
many BOSL2 users who don’t use attachments for example. On Mon, Aug 25, 2025
at 10:48 Glenn Butcher via Discuss < discuss@lists.openscad.org> wrote: > I'm
putting the finishing touches on my most recent project, but I'm > considering
starting the next one in BOSL2. That's the thing, once you > start something
in BOSL2, it's gotta be all in that, so I'll have some prep > work to find
equivalents for all that I do in native OpenSCAD. > > To that end, it would
seem to me that native OpenSCAD is becoming more the > 'assembly language' of
the scripting CAD space, enough primitives available > to allow more capable
stuff like BOSL2. Treat it like that, and making > breaking changes to the
language becomes more problematic... > > Oh, here is my most recent project: >
> The stone walls are a product of three bespoke c++ programs that feed >
OpenSCAD's surface() and polygon() modules. And, the roof segments were >
difference()ed with cutting cubes rotated at the origin... > > Glenn > On
8/25/2025 7:50 AM, Adrian Mariano via Discuss wrote: > > Jordan you could
protect name space by doing something like > > $defaults=object(center=true);
> > Glenn you can position objects in BOSL2 in the way that you want to >
without having to understand attachments. You only need anchoring for that. >
It’s described in the tutorial under “basic object positioning” > > Example: >
> include<BOSL2/std.scad> > cube(10, anchor=[1,0,0]); > > That makes a cube
centered in y and z and aligned with the origin in x. > So the same as
translate([5,0,0]) applied to a centered cube. > > On Mon, Aug 25, 2025 at
09:33 Glenn Butcher via Discuss < > discuss@lists.openscad.org> wrote: > >> I
know I'm a little late to the whole center/(centre?) discussion, but >> I've 2
cents... >> >> In all my modeling I've used center=true maybe 10 times, mainly
to keep >> from having to type some sort of translate /2 thing. A lot of my
modeling >> involves difference() to cut precise angles in wall and roof
components, so >> I want some corner of the cutter on the z axis (sometimes x
or y) to rotate >> it to a particular angle prior to moving it to where it'll
do the cutting. >> I find myself in the majority of primitives automatically
adding >> 'translate[0,0,0] rotate[0,0,0]' to the front of it so I can
subsequently >> modify those parameters to spin/move the thing where I want.
One of these >> days I might sit down and wrap my head around BOSL2
attachments, but not >> anytime soon.... >> >> If there is to be made a IMHO
useful change to the center parameter, it >> would be a vector of booleans to
selectively center on various axes. And, >> scalar '1' would do all three. >>
>> Glenn >> On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote: >> >> On
Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote: >> >> <snip>
>> >> >> The only thing I'd like to see, is a center keyword that if left out,
>> defaults to true, not false. >> >> >> YES x 2 >> >> Can we have Centre
spelt properly please ;-), yeah I KNOW that's a big ask... but my scary
English teacher would have hauled me over the coals [disliked English, loved
Technical Drawing]. >> >> I've been rewriting self written modules that accept
either spelling, that's what used to be called defensive programming. >> >>
TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated. >> >> Point and click has
never been my bag. >> >> So the question is, WIIFM? how will OO make OpenSCAD
easier to use? or will it make obscure geometrical mind bending easier for the
use cases that need it? >> >> Roger. >> >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/678519/200)
](https://lists.openscad.org/empathy/attachment/678519)

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Mon, Aug 25, 2025 3:18 PM

Appreciate your great work Glenn  
Looks really wonderful

On Mon, 25 Aug, 2025, 8:18 pm Glenn Butcher via Discuss, <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I'm putting the finishing touches on my most recent project, but I'm  
considering starting the next one in BOSL2. That's the thing, once you  
start something in BOSL2, it's gotta be all in that, so I'll have some prep  
work to find equivalents for all that I do in native OpenSCAD.

To that end, it would seem to me that native OpenSCAD is becoming more the  
'assembly language' of the scripting CAD space, enough primitives available  
to allow more capable stuff like BOSL2. Treat it like that, and making  
breaking changes to the language becomes more problematic...

Oh, here is my most recent project:

The stone walls are a product of three bespoke c++ programs that feed  
OpenSCAD's surface() and polygon() modules. And, the roof segments were  
difference()ed with cutting cubes rotated at the origin...

Glenn  
On 8/25/2025 7:50 AM, Adrian Mariano via Discuss wrote:

Jordan you could protect name space by doing something like

$defaults=object(center=true);

Glenn you can position objects in BOSL2 in the way that you want to  
without having to understand attachments. You only need anchoring for that.  
It’s described in the tutorial under “basic object positioning”

Example:

include<BOSL2/std.scad>  
cube(10, anchor=[1,0,0]);

That makes a cube centered in y and z and aligned with the origin in x.  
So the same as translate([5,0,0]) applied to a centered cube.

On Mon, Aug 25, 2025 at 09:33 Glenn Butcher via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I know I'm a little late to the whole center/(centre?) discussion, but  
I've 2 cents...

In all my modeling I've used center=true maybe 10 times, mainly to keep  
from having to type some sort of translate /2 thing. A lot of my modeling  
involves difference() to cut precise angles in wall and roof components, so  
I want some corner of the cutter on the z axis (sometimes x or y) to rotate  
it to a particular angle prior to moving it to where it'll do the cutting.  
I find myself in the majority of primitives automatically adding  
'translate[0,0,0] rotate[0,0,0]' to the front of it so I can subsequently  
modify those parameters to spin/move the thing where I want. One of these  
days I might sit down and wrap my head around BOSL2 attachments, but not  
anytime soon....

If there is to be made a IMHO useful change to the center parameter, it  
would be a vector of booleans to selectively center on various axes. And,  
scalar '1' would do all three.

Glenn  
On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote:

On Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote:

<snip>

The only thing I'd like to see, is a center keyword that if left out,  
defaults to true, not false.

YES x 2

Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask...
but my scary English teacher would have hauled me over the coals [disliked
English, loved Technical Drawing].

I've been rewriting self written modules that accept either spelling, that's
what used to be called defensive programming.

TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated.

Point and click has never been my bag.

So the question is, WIIFM? how will OO make OpenSCAD easier to use? or will it
make obscure geometrical mind bending easier for the use cases that need it?

Roger.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Appreciate your great work Glenn Looks really wonderful On Mon, 25 Aug, 2025,
8:18 pm Glenn Butcher via Discuss, < discuss@lists.openscad.org> wrote: > I'm
putting the finishing touches on my most recent project, but I'm > considering
starting the next one in BOSL2. That's the thing, once you > start something
in BOSL2, it's gotta be all in that, so I'll have some prep > work to find
equivalents for all that I do in native OpenSCAD. > > To that end, it would
seem to me that native OpenSCAD is becoming more the > 'assembly language' of
the scripting CAD space, enough primitives available > to allow more capable
stuff like BOSL2. Treat it like that, and making > breaking changes to the
language becomes more problematic... > > Oh, here is my most recent project: >
> The stone walls are a product of three bespoke c++ programs that feed >
OpenSCAD's surface() and polygon() modules. And, the roof segments were >
difference()ed with cutting cubes rotated at the origin... > > Glenn > On
8/25/2025 7:50 AM, Adrian Mariano via Discuss wrote: > > Jordan you could
protect name space by doing something like > > $defaults=object(center=true);
> > Glenn you can position objects in BOSL2 in the way that you want to >
without having to understand attachments. You only need anchoring for that. >
It’s described in the tutorial under “basic object positioning” > > Example: >
> include<BOSL2/std.scad> > cube(10, anchor=[1,0,0]); > > That makes a cube
centered in y and z and aligned with the origin in x. > So the same as
translate([5,0,0]) applied to a centered cube. > > On Mon, Aug 25, 2025 at
09:33 Glenn Butcher via Discuss < > discuss@lists.openscad.org> wrote: > >> I
know I'm a little late to the whole center/(centre?) discussion, but >> I've 2
cents... >> >> In all my modeling I've used center=true maybe 10 times, mainly
to keep >> from having to type some sort of translate /2 thing. A lot of my
modeling >> involves difference() to cut precise angles in wall and roof
components, so >> I want some corner of the cutter on the z axis (sometimes x
or y) to rotate >> it to a particular angle prior to moving it to where it'll
do the cutting. >> I find myself in the majority of primitives automatically
adding >> 'translate[0,0,0] rotate[0,0,0]' to the front of it so I can
subsequently >> modify those parameters to spin/move the thing where I want.
One of these >> days I might sit down and wrap my head around BOSL2
attachments, but not >> anytime soon.... >> >> If there is to be made a IMHO
useful change to the center parameter, it >> would be a vector of booleans to
selectively center on various axes. And, >> scalar '1' would do all three. >>
>> Glenn >> On 8/25/2025 4:00 AM, Roger Whiteley via Discuss wrote: >> >> On
Sat, 2025-08-23 at 23:32 -0400, gene heskett via Discuss wrote: >> >> <snip>
>> >> >> The only thing I'd like to see, is a center keyword that if left out,
>> defaults to true, not false. >> >> >> YES x 2 >> >> Can we have Centre
spelt properly please ;-), yeah I KNOW that's a big ask... but my scary
English teacher would have hauled me over the coals [disliked English, loved
Technical Drawing]. >> >> I've been rewriting self written modules that accept
either spelling, that's what used to be called defensive programming. >> >>
TBH the whole OO conversation, has mostly gone over my head, but I'm with
Gene, math != good fun. and FreeCAD = monumental and pointless steep learning
curve when OpenSCAD has a lower point of useful entry, with the added bonus of
developer participation, which is much appreciated. >> >> Point and click has
never been my bag. >> >> So the question is, WIIFM? how will OO make OpenSCAD
easier to use? or will it make obscure geometrical mind bending easier for the
use cases that need it? >> >> Roger. >> >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/678525/200)
](https://lists.openscad.org/empathy/attachment/678525) [ ![Attached
image](https://lists.openscad.org/empathy/image/678524/200)
](https://lists.openscad.org/empathy/attachment/678524)

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Aug 25, 2025 6:36 PM

Let's, fingers crossed, try to switch the subject to something more  
appropriate. Coalescing replies to several messages (Roger, Adrian, Glenn).

On 8/25/2025 12:00 PM, Roger Whiteley via Discuss wrote:

____

____

The only thing I'd like to see, is a center keyword that if left out,  
defaults to true, not false.

YES x 2

I'm thinking of something along the lines of

    
    
    $center = true;
    

and $center would be used by default in any call where "center" was not  
specified. As with any special variable, you could put it at the top  
level and switch over your entire program, or in a more limited scope.

____

Can we have Centre spelt properly please ;-), yeah I KNOW that's a big ask...
but my scary English teacher would have hauled me over the coals [disliked
English, loved Technical Drawing].

Easy enough. I believe I added an alias mechanism that makes it  
basically trivial. The question is whether we want to go that way. (Do  
we also want "radius" as an alias of "r"? Et cetera.) Torsten, Marius?

On 8/25/2025 3:50 PM, Adrian Mariano via Discuss wrote:

____

Jordan you could protect name space by doing something like

$defaults=object(center=true);

Yes, I was thinking about that. It becomes a bit tedious to override  
_one_ entry - especially if an entry itself is an object.

But, once per scope, you can do

    
    
    $defaults = object($defaults, center=true);
    

If you want to override a value in an entry that is itself an object,  
you could do something like

    
    
    // East got squashed.
    $defaults = object($defaults, magic=object($defaults.magic, witch="West"));
    

On 8/25/2025 3:32 PM, Glenn Butcher via Discuss wrote:

____

If there is to be made a IMHO useful change to the center parameter,  
it would be a vector of booleans to selectively center on various  
axes. And, scalar '1' would do all three.

I have a justified-cube function that accepts a three-element list of  
integers. -1 puts the cube on the negative side of the axis, 0 centers  
it, and +1 puts it on the positive side. That's actually terser than  
the list-of-three-booleans, and I find it to be quite convenient.  
That's what I would push if we were to go there. No strong feeling on  
whether it would be called "center" or a new name.

BOSL2 anchors do a more complete job, of course. (And their ability,  
IIRC, to pull back in just a little to create overlaps is a winner.)

Let's, fingers crossed, try to switch the subject to something more
appropriate. Coalescing replies to several messages (Roger, Adrian, Glenn). On
8/25/2025 12:00 PM, Roger Whiteley via Discuss wrote: >> The only thing I'd
like to see, is a center keyword that if left out, >> defaults to true, not
false. >> > YES x 2 I'm thinking of something along the lines of $center =
true; and $center would be used by default in any call where "center" was not
specified. As with any special variable, you could put it at the top level and
switch over your entire program, or in a more limited scope. > Can we have
Centre spelt properly please ;-), yeah I KNOW that's a big ask... but my scary
English teacher would have hauled me over the coals [disliked English, loved
Technical Drawing]. Easy enough. I believe I added an alias mechanism that
makes it basically trivial. The question is whether we want to go that way.
(Do we also want "radius" as an alias of "r"? Et cetera.) Torsten, Marius? On
8/25/2025 3:50 PM, Adrian Mariano via Discuss wrote: > Jordan you could
protect name space by doing something like > > $defaults=object(center=true);
Yes, I was thinking about that. It becomes a bit tedious to override *one*
entry - especially if an entry itself is an object. But, once per scope, you
can do $defaults = object($defaults, center=true); If you want to override a
value in an entry that is itself an object, you could do something like //
East got squashed. $defaults = object($defaults, magic=object($defaults.magic,
witch="West")); On 8/25/2025 3:32 PM, Glenn Butcher via Discuss wrote: > > If
there is to be made a IMHO useful change to the center parameter, > it would
be a vector of booleans to selectively center on various > axes. And, scalar
'1' would do all three. > I have a justified-cube function that accepts a
three-element list of integers. -1 puts the cube on the negative side of the
axis, 0 centers it, and +1 puts it on the positive side. That's actually
terser than the list-of-three-booleans, and I find it to be quite convenient.
That's what I would push if we were to go there. No strong feeling on whether
it would be called "center" or a new name. BOSL2 anchors do a more complete
job, of course. (And their ability, IIRC, to pull back in just a little to
create overlaps is a winner.)

![](https://www.gravatar.com/avatar/605cbbee6fefc10271a27ee79bba5157?d=blank&s=100)

TP

Torsten Paul

Mon, Aug 25, 2025 6:57 PM

On 25.08.25 20:36, Jordan Brown via Discuss wrote:

____

I'm thinking of something along the lines of

    
    
     $center = true;
    

I think that's a bad solution that will break all existing scripts using  
older libraries.

Also I _REALLY_ would suggest stopping with all the $ inventions. They  
do have their place but it feels like they are always pushed as magic  
enough to solve all issues. They are not.

ciao,  
Torsten.

On 25.08.25 20:36, Jordan Brown via Discuss wrote: > I'm thinking of something
along the lines of > > $center = true; I think that's a bad solution that will
break all existing scripts using older libraries. Also I *REALLY* would
suggest stopping with all the $ inventions. They do have their place but it
feels like they are always pushed as magic enough to solve all issues. They
are not. ciao, Torsten.

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Aug 25, 2025 7:16 PM

On 8/25/2025 8:57 PM, Torsten Paul via Discuss wrote:

____

On 25.08.25 20:36, Jordan Brown via Discuss wrote:

____

I'm thinking of something along the lines of

$center = true;

I think that's a bad solution that will break all existing scripts using  
older libraries.

To be clear, the default for $center would be false, so there would be  
no change unless you opt in. Don't do that if your model, or the  
libraries you call, can't handle it.

A library might well want to routinely set $center=false (or  
$center=true) so that it is independent of the caller's preferences.

____

Also I _REALLY_ would suggest stopping with all the $ inventions. They  
do have their place but it feels like they are always pushed as magic  
enough to solve all issues. They are not.

They are the closest thing we have to a mechanism to allow a program, or  
a subprogram at whatever level, to opt in to alternative behavior.

Can you think of a _better_ way to make it so that cube() is centered,  
for programs that want it to be, without requiring "center=true" on  
every invocation? It sure seems like "opt in for this subtree" is a  
reasonable approach.

On 8/25/2025 8:57 PM, Torsten Paul via Discuss wrote: > On 25.08.25 20:36,
Jordan Brown via Discuss wrote: >> I'm thinking of something along the lines
of >> >> $center = true; > > I think that's a bad solution that will break all
existing scripts using > older libraries. To be clear, the default for $center
would be false, so there would be no change unless you opt in. Don't do that
if your model, or the libraries you call, can't handle it. A library might
well want to routinely set $center=false (or $center=true) so that it is
independent of the caller's preferences. > Also I *REALLY* would suggest
stopping with all the $ inventions. They > do have their place but it feels
like they are always pushed as magic > enough to solve all issues. They are
not. They are the closest thing we have to a mechanism to allow a program, or
a subprogram at whatever level, to opt in to alternative behavior. Can you
think of a *better* way to make it so that cube() is centered, for programs
that want it to be, without requiring "center=true" on every invocation? It
sure seems like "opt in for this subtree" is a reasonable approach.

![](https://www.gravatar.com/avatar/605cbbee6fefc10271a27ee79bba5157?d=blank&s=100)

TP

Torsten Paul

Mon, Aug 25, 2025 7:21 PM

On 25.08.25 21:16, Jordan Brown via Discuss wrote:

____

A library might well want to routinely set $center=false (or  
$center=true) so that it is independent of the caller's preferences.

That is not possible without again breaking things, e.g. callbacks  
(children()) passed in from the user script that would assume they  
can control this without specifying it every time (which totally  
defeats the underlying idea).

ciao,  
Torsten.

On 25.08.25 21:16, Jordan Brown via Discuss wrote: > A library might well want
to routinely set $center=false (or > $center=true) so that it is independent
of the caller's preferences. That is not possible without again breaking
things, e.g. callbacks (children()) passed in from the user script that would
assume they can control this without specifying it every time (which totally
defeats the underlying idea). ciao, Torsten.

[Next
page](https://lists.openscad.org/empathy/thread/TFQY6AS5DNE2M6DIEQLM5YHYGPQDVSFA?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

