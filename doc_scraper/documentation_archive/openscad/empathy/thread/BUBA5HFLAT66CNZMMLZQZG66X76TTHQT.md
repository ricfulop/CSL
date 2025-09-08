---
url: https://lists.openscad.org/empathy/thread/BUBA5HFLAT66CNZMMLZQZG66X76TTHQT
scraped_at: 2025-09-08T16:28:12.640799
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

###  failing preview and malformed full render

![](https://www.gravatar.com/avatar/fef1a057596ac6c3b2880a1b46ce1e19?d=blank&s=100)

RW

Roger Whiteley

Wed, Sep 3, 2025 12:52 PM

I've just cloned/compiled and built the latest 3rd September 2025  
OpenSCAD code, in the hope that issues with previous builds [after  
2021.01, which works OK] have been resolved, They haven't :-(. I also  
want to try out the namespace code..

OpenSCAD install built directly from a git clone and following the  
[perfect] instructions for a Debian 12 desktop.

The original code is from <http://www.thingiverse.com/thing:3575>,

The version I use, [lightly modified to create the object I want] is  
attached.

Preview always renders with CSG, painfully slow of course, and the main  
gear object does not preview with teeth, and on moving the Viewport  
around, preview shows a truncated cone when the +Z axis is up [I  
normally view this with +Z down].

The ring that appears to render in fresh air actually serves as a prop  
for the corners of the teeth when exported as an STL for printing, the  
gear is printed coned side up as that is the visible side, there's a  
second ring underneath, which breaks up the support into sections so  
that when printed the rings and support can be removed more easily.

Performing a full render results in clearly visible gaps and slot-like  
grooves on the teeth, which are reproduced in an export, making the STL  
unusable.

Could the development team comment please?

Much appreciated.

Roger.

I've just cloned/compiled and built the latest 3rd September 2025 OpenSCAD
code, in the hope that issues with previous builds [after 2021.01, which works
OK] have been resolved, They haven't :-(. I also want to try out the namespace
code.. OpenSCAD install built directly from a git clone and following the
[perfect] instructions for a Debian 12 desktop. The original code is from
http://www.thingiverse.com/thing:3575, The version I use, [lightly modified to
create the object I want] is attached. Preview always renders with CSG,
painfully slow of course, and the main gear object does not preview with
teeth, and on moving the Viewport around, preview shows a truncated cone when
the +Z axis is up [I normally view this with +Z down]. The ring that appears
to render in fresh air actually serves as a prop for the corners of the teeth
when exported as an STL for printing, the gear is printed coned side up as
that is the visible side, there's a second ring underneath, which breaks up
the support into sections so that when printed the rings and support can be
removed more easily. Performing a full render results in clearly visible gaps
and slot-like grooves on the teeth, which are reproduced in an export, making
the STL unusable. Could the development team comment please? Much appreciated.
Roger.

[ __gearpinionbroken.scad(19.99 KB)
](https://lists.openscad.org/empathy/attachment/679219
"application/x-openscad")

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Wed, Sep 3, 2025 5:24 PM

On 9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote:

____

Could the development team comment please?

I don't know whether I qualify as a member of the development team - I  
haven't gotten my membership card yet - but my comment is "indeed,  
that's interesting; perhaps you could trim it down to a more minimal  
demonstration case".

Everybody: please don't ask the development team to pull apart a  
multi-hundred line program to figure out where the problem is. Do what  
you can first. Chop away everything that doesn't demonstrate the  
problem; normally you can get it down to only a dozen or two lines.  
Doing that doesn't require any knowledge of the internals, but does  
require knowledge of your program - which you have, and the developer  
looking at it doesn't have. Often, in the process you'll find a mistake  
in the program.

Here it's pretty clear that there _is_ a problem in OpenSCAD that leads  
to the preview being different from the render, but you could still chop  
it down to the minimum demonstration. The notches are probably an  
OpenSCAD issue too, since they are there with Manifold but not with CGAL.

On 9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote: > Could the development
team comment please? I don't know whether I qualify as a member of the
development team - I haven't gotten my membership card yet - but my comment is
"indeed, that's interesting; perhaps you could trim it down to a more minimal
demonstration case". Everybody: please don't ask the development team to pull
apart a multi-hundred line program to figure out where the problem is. Do what
you can first. Chop away everything that doesn't demonstrate the problem;
normally you can get it down to only a dozen or two lines. Doing that doesn't
require any knowledge of the internals, but does require knowledge of your
program - which you have, and the developer looking at it doesn't have. Often,
in the process you'll find a mistake in the program. Here it's pretty clear
that there *is* a problem in OpenSCAD that leads to the preview being
different from the render, but you could still chop it down to the minimum
demonstration. The notches are probably an OpenSCAD issue too, since they are
there with Manifold but not with CGAL.

![](https://www.gravatar.com/avatar/095124c1792024c67a3336fc575ec4a6?d=blank&s=100)

NH

nop head

Wed, Sep 3, 2025 5:58 PM

Could it be that the object making the holes is exactly coincident with the  
top of the hole. GCAL will handle that if it is exactly coincident, but  
perhaps manifold depends on floating point accuracy.

On Wed, 3 Sept 2025 at 18:25, Jordan Brown via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

On 9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote:

Could the development team comment please?

I don't know whether I qualify as a member of the development team - I  
haven't gotten my membership card yet - but my comment is "indeed, that's  
interesting; perhaps you could trim it down to a more minimal demonstration  
case".

Everybody: please don't ask the development team to pull apart a  
multi-hundred line program to figure out where the problem is. Do what you  
can first. Chop away everything that doesn't demonstrate the problem;  
normally you can get it down to only a dozen or two lines. Doing that  
doesn't require any knowledge of the internals, but does require knowledge  
of your program - which you have, and the developer looking at it doesn't  
have. Often, in the process you'll find a mistake in the program.

Here it's pretty clear that there _is_ a problem in OpenSCAD that leads to  
the preview being different from the render, but you could still chop it  
down to the minimum demonstration. The notches are probably an OpenSCAD  
issue too, since they are there with Manifold but not with CGAL.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Could it be that the object making the holes is exactly coincident with the
top of the hole. GCAL will handle that if it is exactly coincident, but
perhaps manifold depends on floating point accuracy. On Wed, 3 Sept 2025 at
18:25, Jordan Brown via Discuss < discuss@lists.openscad.org> wrote: > On
9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote: > > Could the development
team comment please? > > > I don't know whether I qualify as a member of the
development team - I > haven't gotten my membership card yet - but my comment
is "indeed, that's > interesting; perhaps you could trim it down to a more
minimal demonstration > case". > > Everybody: please don't ask the development
team to pull apart a > multi-hundred line program to figure out where the
problem is. Do what you > can first. Chop away everything that doesn't
demonstrate the problem; > normally you can get it down to only a dozen or two
lines. Doing that > doesn't require any knowledge of the internals, but does
require knowledge > of your program - which you have, and the developer
looking at it doesn't > have. Often, in the process you'll find a mistake in
the program. > > Here it's pretty clear that there *is* a problem in OpenSCAD
that leads to > the preview being different from the render, but you could
still chop it > down to the minimum demonstration. The notches are probably an
OpenSCAD > issue too, since they are there with Manifold but not with CGAL. >
> > _______________________________________________ > OpenSCAD mailing list >
To unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/901519ec4216a54cde3ac2d5a018b082?d=blank&s=100)

P

pca006132

Wed, Sep 3, 2025 6:13 PM

We haven't yet have issues with that. The problem openscad usually have  
(not necessarily this issue) is when converting manifold mesh to CGAL Nef  
polyhedron for minkowski operation.

On Thu, Sep 4, 2025, 01:58 nop head via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
wrote:

____

Could it be that the object making the holes is exactly coincident with  
the top of the hole. GCAL will handle that if it is exactly coincident, but  
perhaps manifold depends on floating point accuracy.

On Wed, 3 Sept 2025 at 18:25, Jordan Brown via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

On 9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote:

Could the development team comment please?

I don't know whether I qualify as a member of the development team - I  
haven't gotten my membership card yet - but my comment is "indeed, that's  
interesting; perhaps you could trim it down to a more minimal demonstration  
case".

Everybody: please don't ask the development team to pull apart a  
multi-hundred line program to figure out where the problem is. Do what you  
can first. Chop away everything that doesn't demonstrate the problem;  
normally you can get it down to only a dozen or two lines. Doing that  
doesn't require any knowledge of the internals, but does require knowledge  
of your program - which you have, and the developer looking at it doesn't  
have. Often, in the process you'll find a mistake in the program.

Here it's pretty clear that there _is_ a problem in OpenSCAD that leads  
to the preview being different from the render, but you could still chop it  
down to the minimum demonstration. The notches are probably an OpenSCAD  
issue too, since they are there with Manifold but not with CGAL.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

We haven't yet have issues with that. The problem openscad usually have (not
necessarily this issue) is when converting manifold mesh to CGAL Nef
polyhedron for minkowski operation. On Thu, Sep 4, 2025, 01:58 nop head via
Discuss <discuss@lists.openscad.org> wrote: > Could it be that the object
making the holes is exactly coincident with > the top of the hole. GCAL will
handle that if it is exactly coincident, but > perhaps manifold depends on
floating point accuracy. > > On Wed, 3 Sept 2025 at 18:25, Jordan Brown via
Discuss < > discuss@lists.openscad.org> wrote: > >> On 9/3/2025 5:52 AM, Roger
Whiteley via Discuss wrote: >> >> Could the development team comment please?
>> >> >> I don't know whether I qualify as a member of the development team -
I >> haven't gotten my membership card yet - but my comment is "indeed, that's
>> interesting; perhaps you could trim it down to a more minimal demonstration
>> case". >> >> Everybody: please don't ask the development team to pull apart
a >> multi-hundred line program to figure out where the problem is. Do what
you >> can first. Chop away everything that doesn't demonstrate the problem;
>> normally you can get it down to only a dozen or two lines. Doing that >>
doesn't require any knowledge of the internals, but does require knowledge >>
of your program - which you have, and the developer looking at it doesn't >>
have. Often, in the process you'll find a mistake in the program. >> >> Here
it's pretty clear that there *is* a problem in OpenSCAD that leads >> to the
preview being different from the render, but you could still chop it >> down
to the minimum demonstration. The notches are probably an OpenSCAD >> issue
too, since they are there with Manifold but not with CGAL. >> >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/fef1a057596ac6c3b2880a1b46ce1e19?d=blank&s=100)

RW

Roger Whiteley

Thu, Sep 4, 2025 1:12 PM

Jordan

I should have been more clear that I wasn't expecting to get someone  
else to debug the code, only that this code causes the preview and  
rendering systems to not generate a clean object.

Thanks for the suggestion, this is one of the problems with a code block  
that I am essentially reusing without necessarily knowing exactly how it  
functions :-(, not always a good starting point.

I could look through other code that I own and understand and try to  
find a simpler use case, I do recall issues with something else,  
particularly in Preview, now I've built the latest release, its  
installed right over the 2021.05 official version, I still have the  
2024.12.30 version installed via Flatpak, but I think reinstalling from  
the Debian repo will tread over the latest build, such is life..

I've taken a look at the code as it stands, and removed two assign  
statements, @ lines 529 and 533, that I missed, and removed extra braces  
that performed no function.

So I've (re)downloaded the original, and sure enough there are other  
assign statements which I changed to regular variable = some value.

The original still fails to preview correctly, leaving all the teeth  
off, making it a good variable drive system, but not much good for  
transmitting power..

There is a much newer library of bevel gears, here  
<https://www.thingiverse.com/thing:6881272>, which I will have a play  
with, rendering looks good though.

It would be good to simply understand if there's a repeatable problem  
with other code.

Roger.

On 03/09/2025 18:24, Jordan Brown wrote:

____

On 9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote:

> Could the development team comment please?

I don't know whether I qualify as a member of the development team - I  
haven't gotten my membership card yet - but my comment is "indeed,  
that's interesting; perhaps you could trim it down to a more minimal  
demonstration case".

Everybody: please don't ask the development team to pull apart a  
multi-hundred line program to figure out where the problem is. Do  
what you can first. Chop away everything that doesn't demonstrate the  
problem; normally you can get it down to only a dozen or two lines.  
Doing that doesn't require any knowledge of the internals, but does  
require knowledge of your program - which you have, and the developer  
looking at it doesn't have. Often, in the process you'll find a  
mistake in the program.

Here it's pretty clear that there _is_ a problem in OpenSCAD that  
leads to the preview being different from the render, but you could  
still chop it down to the minimum demonstration. The notches are  
probably an OpenSCAD issue too, since they are there with Manifold but  
not with CGAL.

Jordan I should have been more clear that I wasn't expecting to get someone
else to debug the code, only that this code causes the preview and rendering
systems to not generate a clean object. Thanks for the suggestion, this is one
of the problems with a code block that I am essentially reusing without
necessarily knowing exactly how it functions :-(, not always a good starting
point. I could look through other code that I own and understand and try to
find a simpler use case, I do recall issues with something else, particularly
in Preview, now I've built the latest release, its installed right over the
2021.05 official version, I still have the 2024.12.30 version installed via
Flatpak, but I think reinstalling from the Debian repo will tread over the
latest build, such is life.. I've taken a look at the code as it stands, and
removed two assign statements, @ lines 529 and 533, that I missed, and removed
extra braces that performed no function. So I've (re)downloaded the original,
and sure enough there are other assign statements which I changed to regular
variable = some value. The original still fails to preview correctly, leaving
all the teeth off, making it a good variable drive system, but not much good
for transmitting power.. There is a much newer library of bevel gears, here
https://www.thingiverse.com/thing:6881272, which I will have a play with,
rendering looks good though. It would be good to simply understand if there's
a repeatable problem with other code. Roger. On 03/09/2025 18:24, Jordan Brown
wrote: > On 9/3/2025 5:52 AM, Roger Whiteley via Discuss wrote: >> Could the
development team comment please? > > I don't know whether I qualify as a
member of the development team - I > haven't gotten my membership card yet -
but my comment is "indeed, > that's interesting; perhaps you could trim it
down to a more minimal > demonstration case". > > Everybody: please don't ask
the development team to pull apart a > multi-hundred line program to figure
out where the problem is. Do > what you can first. Chop away everything that
doesn't demonstrate the > problem; normally you can get it down to only a
dozen or two lines. > Doing that doesn't require any knowledge of the
internals, but does > require knowledge of your program - which you have, and
the developer > looking at it doesn't have. Often, in the process you'll find
a > mistake in the program. > > Here it's pretty clear that there *is* a
problem in OpenSCAD that > leads to the preview being different from the
render, but you could > still chop it down to the minimum demonstration. The
notches are > probably an OpenSCAD issue too, since they are there with
Manifold but > not with CGAL. > >

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

