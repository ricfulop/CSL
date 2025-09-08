---
url: https://lists.openscad.org/empathy/thread/TRFGO4ETFYDXFK3D56IRVZCASYX5M2WI
scraped_at: 2025-09-08T16:28:08.634720
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

###  odd behaviors of BOSL2's offset_stroke() with respect to $fn

![](https://www.gravatar.com/avatar/efffe97fbbe5ef43492550ef734147d9?d=blank&s=100)

TA

Todd Allen

Sun, Sep 7, 2025 6:08 PM

// I think this code demonstrates inappropriate handling of $fn in BOSL2's  
offset_stroke().

include <BOSL2/std.scad>  
include <BOSL2/rounding.scad>

$fn= $preview ? 16 : 128;

function cclip_p(arc, fn, id, od) =  
let(  
ax2 = (360-arc)_0.5,  
p0 = difference(  
circle(d=id, $fn=fn),  
arc(n=2, r=10_od, angle=[270-ax2,270+ax2], wedge=true)),  
// difference returns a region, strip back to a path without last point  
p1 = list_head(p0[0])  
) p1;

module cclip(color, arc, fn, id, od, p=0) {  
p1 = p ? p : cclip_p(arc, fn, id, od);  
w=[0,od-id];

    
    
    echo(color=color, w=w, p1=p1);
    
    // with $fn=6 end treatments have 2 segments not 3?
    // there is weird behavior for which outer path points are rounded
    // outer path points are rounded much finer than $fn=6
    back(12) color(color) offset_stroke(p1, start="round", end="round",
    

width=w, $fn=6);

    
    
    // with $fn=8 end treatments have 3 segments and all outer path points
    

are rounded  
color(color) offset_stroke(p1, start="round", end="round", width=w,  
$fn=8);

    
    
    // with pointed end treatments all outer points are rounded, $fn has no
    

effect  
fwd(12) color(color) offset_stroke(p1, start="pointed", end="pointed",  
width=w, $fn=8);  
}

d = 6.82;  
// only the right most outer point is rounded  
right(-12) cclip("yellow", arc=239.0, fn=6, id=d, od=d+1.75);  
// with smaller inner diameter all outer points are rounded  
right(0) cclip("green", arc=239.0, fn=6, id=d-0.75, od=d+1.75);  
// slightly increased arc and only leftmost outer point isn't rounded  
right(12) cclip("red", arc=239.001, fn=6, id=d-0.75, od=d+1.75);  
// same points as before but not computed and right most outer point is  
also not rounded  
red_p = [[-2.28771, -1.29435], [-3.035, 0], [-1.5175, 2.62839], [1.5175,  
2.62839], [3.035, 0], [2.28771, -1.29435]];  
right(24) cclip("blue", arc=0, fn=6, id=d-0.75, od=d+1.75, p=red_p);  
[image: offset_stroke.png]

// I think this code demonstrates inappropriate handling of $fn in BOSL2's
offset_stroke(). include <BOSL2/std.scad> include <BOSL2/rounding.scad> $fn=
$preview ? 16 : 128; function cclip_p(arc, fn, id, od) = let( ax2 =
(360-arc)*0.5, p0 = difference( circle(d=id, $fn=fn), arc(n=2, r=10*od,
angle=[270-ax2,270+ax2], wedge=true)), // difference returns a region, strip
back to a path without last point p1 = list_head(p0[0]) ) p1; module
cclip(color, arc, fn, id, od, p=0) { p1 = p ? p : cclip_p(arc, fn, id, od);
w=[0,od-id]; echo(color=color, w=w, p1=p1); // with $fn=6 end treatments have
2 segments not 3? // there is weird behavior for which outer path points are
rounded // outer path points are rounded much finer than $fn=6 back(12)
color(color) offset_stroke(p1, start="round", end="round", width=w, $fn=6); //
with $fn=8 end treatments have 3 segments and all outer path points are
rounded color(color) offset_stroke(p1, start="round", end="round", width=w,
$fn=8); // with pointed end treatments all outer points are rounded, $fn has
no effect fwd(12) color(color) offset_stroke(p1, start="pointed",
end="pointed", width=w, $fn=8); } d = 6.82; // only the right most outer point
is rounded right(-12) cclip("yellow", arc=239.0, fn=6, id=d, od=d+1.75); //
with smaller inner diameter all outer points are rounded right(0)
cclip("green", arc=239.0, fn=6, id=d-0.75, od=d+1.75); // slightly increased
arc and only leftmost outer point isn't rounded right(12) cclip("red",
arc=239.001, fn=6, id=d-0.75, od=d+1.75); // same points as before but not
computed and right most outer point is also not rounded red_p = [[-2.28771,
-1.29435], [-3.035, 0], [-1.5175, 2.62839], [1.5175, 2.62839], [3.035, 0],
[2.28771, -1.29435]]; right(24) cclip("blue", arc=0, fn=6, id=d-0.75,
od=d+1.75, p=red_p); [image: offset_stroke.png]

[ ![Attached image](https://lists.openscad.org/empathy/image/679623/200)
](https://lists.openscad.org/empathy/attachment/679623)

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Mon, Sep 8, 2025 3:18 AM

Note that BOSL2 bug reports are best raised as issues on the BOSL2 github.

It appears there is an off-by-one error in the rounding for "round". There  
was also a bug in how offset() handled the facet count that I recently  
fixed.

On Sun, Sep 7, 2025 at 2:09 PM Todd Allen via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

// I think this code demonstrates inappropriate handling of $fn in BOSL2's  
offset_stroke().

include <BOSL2/std.scad>  
include <BOSL2/rounding.scad>

$fn= $preview ? 16 : 128;

function cclip_p(arc, fn, id, od) =  
let(  
ax2 = (360-arc)_0.5,  
p0 = difference(  
circle(d=id, $fn=fn),  
arc(n=2, r=10_od, angle=[270-ax2,270+ax2], wedge=true)),  
// difference returns a region, strip back to a path without last point  
p1 = list_head(p0[0])  
) p1;

module cclip(color, arc, fn, id, od, p=0) {  
p1 = p ? p : cclip_p(arc, fn, id, od);  
w=[0,od-id];

    
    
     echo(color=color, w=w, p1=p1);
    
     // with $fn=6 end treatments have 2 segments not 3?
     // there is weird behavior for which outer path points are rounded
     // outer path points are rounded much finer than $fn=6
     back(12) color(color) offset_stroke(p1, start="round", end="round",
    

width=w, $fn=6);

    
    
     // with $fn=8 end treatments have 3 segments and all outer path points
    

are rounded  
color(color) offset_stroke(p1, start="round", end="round", width=w,  
$fn=8);

    
    
     // with pointed end treatments all outer points are rounded, $fn has
    

no effect  
fwd(12) color(color) offset_stroke(p1, start="pointed", end="pointed",  
width=w, $fn=8);  
}

d = 6.82;  
// only the right most outer point is rounded  
right(-12) cclip("yellow", arc=239.0, fn=6, id=d, od=d+1.75);  
// with smaller inner diameter all outer points are rounded  
right(0) cclip("green", arc=239.0, fn=6, id=d-0.75, od=d+1.75);  
// slightly increased arc and only leftmost outer point isn't rounded  
right(12) cclip("red", arc=239.001, fn=6, id=d-0.75, od=d+1.75);  
// same points as before but not computed and right most outer point is  
also not rounded  
red_p = [[-2.28771, -1.29435], [-3.035, 0], [-1.5175, 2.62839], [1.5175,  
2.62839], [3.035, 0], [2.28771, -1.29435]];  
right(24) cclip("blue", arc=0, fn=6, id=d-0.75, od=d+1.75, p=red_p);  
[image: offset_stroke.png]

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Note that BOSL2 bug reports are best raised as issues on the BOSL2 github. It
appears there is an off-by-one error in the rounding for "round". There was
also a bug in how offset() handled the facet count that I recently fixed. On
Sun, Sep 7, 2025 at 2:09 PM Todd Allen via Discuss <
discuss@lists.openscad.org> wrote: > // I think this code demonstrates
inappropriate handling of $fn in BOSL2's > offset_stroke(). > > include
<BOSL2/std.scad> > include <BOSL2/rounding.scad> > > $fn= $preview ? 16 : 128;
> > function cclip_p(arc, fn, id, od) = > let( > ax2 = (360-arc)*0.5, > p0 =
difference( > circle(d=id, $fn=fn), > arc(n=2, r=10*od,
angle=[270-ax2,270+ax2], wedge=true)), > // difference returns a region, strip
back to a path without last point > p1 = list_head(p0[0]) > ) p1; > > module
cclip(color, arc, fn, id, od, p=0) { > p1 = p ? p : cclip_p(arc, fn, id, od);
> w=[0,od-id]; > > echo(color=color, w=w, p1=p1); > > // with $fn=6 end
treatments have 2 segments not 3? > // there is weird behavior for which outer
path points are rounded > // outer path points are rounded much finer than
$fn=6 > back(12) color(color) offset_stroke(p1, start="round", end="round", >
width=w, $fn=6); > > // with $fn=8 end treatments have 3 segments and all
outer path points > are rounded > color(color) offset_stroke(p1,
start="round", end="round", width=w, > $fn=8); > > // with pointed end
treatments all outer points are rounded, $fn has > no effect > fwd(12)
color(color) offset_stroke(p1, start="pointed", end="pointed", > width=w,
$fn=8); > } > > d = 6.82; > // only the right most outer point is rounded >
right(-12) cclip("yellow", arc=239.0, fn=6, id=d, od=d+1.75); > // with
smaller inner diameter all outer points are rounded > right(0) cclip("green",
arc=239.0, fn=6, id=d-0.75, od=d+1.75); > // slightly increased arc and only
leftmost outer point isn't rounded > right(12) cclip("red", arc=239.001, fn=6,
id=d-0.75, od=d+1.75); > // same points as before but not computed and right
most outer point is > also not rounded > red_p = [[-2.28771, -1.29435],
[-3.035, 0], [-1.5175, 2.62839], [1.5175, > 2.62839], [3.035, 0], [2.28771,
-1.29435]]; > right(24) cclip("blue", arc=0, fn=6, id=d-0.75, od=d+1.75,
p=red_p); > [image: offset_stroke.png] >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/679639/200)
](https://lists.openscad.org/empathy/attachment/679639)

![](https://www.gravatar.com/avatar/efffe97fbbe5ef43492550ef734147d9?d=blank&s=100)

TA

Todd Allen

Mon, Sep 8, 2025 4:04 PM

Thanks Adrian!

____

Note that BOSL2 bug reports are best raised as issues on the BOSL2

github.

My apologies. My frame of mind was still somewhat confused rather than  
this is definitely a bug meriting a bug report. The documentation said  
roughly "the number of segments for end rounding and offset rounding are  
computed in the usual way with respect to special variables." I did not  
have certainty as to what that meant. I wondered, is each rounding formed  
from equal length segments with the number of segments set by a floor or  
ceiling? I tried to gain clarity with experimentation and the results  
made no sense to me but I still wasn't certain what the results should be  
or that I wasn't making a mistake in the invocation. I turned to this  
email list as a place welcoming of confused user thoughts and I was  
hesitant to pollute the expert developer level discourse on github.

On Sun, Sep 7, 2025 at 10:18 PM Adrian Mariano via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

Note that BOSL2 bug reports are best raised as issues on the BOSL2  
github.

It appears there is an off-by-one error in the rounding for "round".  
There was also a bug in how offset() handled the facet count that I  
recently fixed.

On Sun, Sep 7, 2025 at 2:09 PM Todd Allen via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

// I think this code demonstrates inappropriate handling of $fn in  
BOSL2's offset_stroke().

include <BOSL2/std.scad>  
include <BOSL2/rounding.scad>

$fn= $preview ? 16 : 128;

function cclip_p(arc, fn, id, od) =  
let(  
ax2 = (360-arc)_0.5,  
p0 = difference(  
circle(d=id, $fn=fn),  
arc(n=2, r=10_od, angle=[270-ax2,270+ax2], wedge=true)),  
// difference returns a region, strip back to a path without last  
point  
p1 = list_head(p0[0])  
) p1;

module cclip(color, arc, fn, id, od, p=0) {  
p1 = p ? p : cclip_p(arc, fn, id, od);  
w=[0,od-id];

    
    
     echo(color=color, w=w, p1=p1);
    
     // with $fn=6 end treatments have 2 segments not 3?
     // there is weird behavior for which outer path points are rounded
     // outer path points are rounded much finer than $fn=6
     back(12) color(color) offset_stroke(p1, start="round", end="round",
    

width=w, $fn=6);

    
    
     // with $fn=8 end treatments have 3 segments and all outer path
    

points are rounded  
color(color) offset_stroke(p1, start="round", end="round", width=w,  
$fn=8);

    
    
     // with pointed end treatments all outer points are rounded, $fn has
    

no effect  
fwd(12) color(color) offset_stroke(p1, start="pointed",  
end="pointed", width=w, $fn=8);  
}

d = 6.82;  
// only the right most outer point is rounded  
right(-12) cclip("yellow", arc=239.0, fn=6, id=d, od=d+1.75);  
// with smaller inner diameter all outer points are rounded  
right(0) cclip("green", arc=239.0, fn=6, id=d-0.75, od=d+1.75);  
// slightly increased arc and only leftmost outer point isn't rounded  
right(12) cclip("red", arc=239.001, fn=6, id=d-0.75, od=d+1.75);  
// same points as before but not computed and right most outer point is  
also not rounded  
red_p = [[-2.28771, -1.29435], [-3.035, 0], [-1.5175, 2.62839], [1.5175,  
2.62839], [3.035, 0], [2.28771, -1.29435]];  
right(24) cclip("blue", arc=0, fn=6, id=d-0.75, od=d+1.75, p=red_p);  
[image: offset_stroke.png]

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Thanks Adrian! > Note that BOSL2 bug reports are best raised as issues on the
BOSL2 github. My apologies. My frame of mind was still somewhat confused
rather than this is definitely a bug meriting a bug report. The documentation
said roughly "the number of segments for end rounding and offset rounding are
computed in the usual way with respect to special variables." I did not have
certainty as to what that meant. I wondered, is each rounding formed from
equal length segments with the number of segments set by a floor or ceiling? I
tried to gain clarity with experimentation and the results made no sense to me
but I still wasn't certain what the results should be or that I wasn't making
a mistake in the invocation. I turned to this email list as a place welcoming
of confused user thoughts and I was hesitant to pollute the expert developer
level discourse on github. On Sun, Sep 7, 2025 at 10:18 PM Adrian Mariano via
Discuss < discuss@lists.openscad.org> wrote: > Note that BOSL2 bug reports are
best raised as issues on the BOSL2 > github. > > It appears there is an off-
by-one error in the rounding for "round". > There was also a bug in how
offset() handled the facet count that I > recently fixed. > > > On Sun, Sep 7,
2025 at 2:09 PM Todd Allen via Discuss < > discuss@lists.openscad.org> wrote:
> >> // I think this code demonstrates inappropriate handling of $fn in >>
BOSL2's offset_stroke(). >> >> include <BOSL2/std.scad> >> include
<BOSL2/rounding.scad> >> >> $fn= $preview ? 16 : 128; >> >> function
cclip_p(arc, fn, id, od) = >> let( >> ax2 = (360-arc)*0.5, >> p0 = difference(
>> circle(d=id, $fn=fn), >> arc(n=2, r=10*od, angle=[270-ax2,270+ax2],
wedge=true)), >> // difference returns a region, strip back to a path without
last >> point >> p1 = list_head(p0[0]) >> ) p1; >> >> module cclip(color, arc,
fn, id, od, p=0) { >> p1 = p ? p : cclip_p(arc, fn, id, od); >> w=[0,od-id];
>> >> echo(color=color, w=w, p1=p1); >> >> // with $fn=6 end treatments have 2
segments not 3? >> // there is weird behavior for which outer path points are
rounded >> // outer path points are rounded much finer than $fn=6 >> back(12)
color(color) offset_stroke(p1, start="round", end="round", >> width=w, $fn=6);
>> >> // with $fn=8 end treatments have 3 segments and all outer path >>
points are rounded >> color(color) offset_stroke(p1, start="round",
end="round", width=w, >> $fn=8); >> >> // with pointed end treatments all
outer points are rounded, $fn has >> no effect >> fwd(12) color(color)
offset_stroke(p1, start="pointed", >> end="pointed", width=w, $fn=8); >> } >>
>> d = 6.82; >> // only the right most outer point is rounded >> right(-12)
cclip("yellow", arc=239.0, fn=6, id=d, od=d+1.75); >> // with smaller inner
diameter all outer points are rounded >> right(0) cclip("green", arc=239.0,
fn=6, id=d-0.75, od=d+1.75); >> // slightly increased arc and only leftmost
outer point isn't rounded >> right(12) cclip("red", arc=239.001, fn=6,
id=d-0.75, od=d+1.75); >> // same points as before but not computed and right
most outer point is >> also not rounded >> red_p = [[-2.28771, -1.29435],
[-3.035, 0], [-1.5175, 2.62839], [1.5175, >> 2.62839], [3.035, 0], [2.28771,
-1.29435]]; >> right(24) cclip("blue", arc=0, fn=6, id=d-0.75, od=d+1.75,
p=red_p); >> [image: offset_stroke.png] >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/679684/200)
](https://lists.openscad.org/empathy/attachment/679684)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

