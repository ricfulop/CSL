---
url: https://lists.openscad.org/empathy/thread/BXPYVNOC7JVCZKW7D3M5ABK6JJQPFEMC
scraped_at: 2025-09-08T16:28:21.694675
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

###  We are not in a good place

![](https://www.gravatar.com/avatar/4ae585652404eee099c2b2e079e0c817?d=blank&s=100)

BC

Bob Carlson

Mon, Aug 25, 2025 9:02 PM

I am very happy that objects have finally been released. I’ve followed all the
discussions about OO with occasional insterest and sometimes horror.

The endless discussions of possible extensions has confused me mightily. The
concurrent modification of the documentation by Vulcan, though well
intentioned, is in my opinion a disaster.

Let me give a couple of examples. I would like to recode my small personal
library using objects. Using objects to create a local namespace seems like a
good idea but requires module references. With all the talk about them I have
lost track of whether the latest build has them or not. I can’t trust the
documentation to tell me. Apparently not supported yet.

I put together a module that would take a 2D path in 3D space and do a linear
extrude along the normal of the 2D polygon. I have always been a bit confused
about when a path becomes 2D geometry and can no longer be accessed as data.
For example I would like to be able to get circle() to produce a path. That
didn’t seem to work. I went to the wiki to try and understand. The muddling of
terms by Vulcan made the exercise impossible. I So my linear_extrude3d module
works using ideas and functions from BOSL2. I had to just muddle thru.

The discussions on object took a frustrating turn when it was suggested that
object implies inheritance so OpenSCAD should support full inheritance. Since
when has any thought that experience with any previous language should create
expectations of OpenSCAD? I have no idea how many languages I have written
code in by now, certainly dozens, a few I even created myself. OpenSCAD has
rules that I can’t remember a single other language with an equivalent. It’s
fine though! It works!

Adding multiple inheritance? Good grief no. Overloading? It would be wasteful
syntactic sugar. The peculiarities of OpenSCAD are bad enough without adding
stuff like this. I fully support the maintainers practice of keeping
enhancements as simple as possible. The discussion of "center" has been
refreshingly down to earth. I personally don’t care because I actually code in
OpenSCAD-BOSL2.

I wish the namespaces for libraries would get solved. Like objects, it seems
like it’s been juts over the horizon for years. That’s 100 times more useful
than overloading or inheritance.

-Bob

I am very happy that objects have finally been released. I’ve followed all the
discussions about OO with occasional insterest and sometimes horror. The
endless discussions of possible extensions has confused me mightily. The
concurrent modification of the documentation by Vulcan, though well
intentioned, is in my opinion a disaster. Let me give a couple of examples. I
would like to recode my small personal library using objects. Using objects to
create a local namespace seems like a good idea but requires module
references. With all the talk about them I have lost track of whether the
latest build has them or not. I can’t trust the documentation to tell me.
Apparently not supported yet. I put together a module that would take a 2D
path in 3D space and do a linear extrude along the normal of the 2D polygon. I
have always been a bit confused about when a path becomes 2D geometry and can
no longer be accessed as data. For example I would like to be able to get
circle() to produce a path. That didn’t seem to work. I went to the wiki to
try and understand. The muddling of terms by Vulcan made the exercise
impossible. I So my linear_extrude3d module works using ideas and functions
from BOSL2. I had to just muddle thru. The discussions on object took a
frustrating turn when it was suggested that object implies inheritance so
OpenSCAD should support full inheritance. Since when has any thought that
experience with any previous language should create expectations of OpenSCAD?
I have no idea how many languages I have written code in by now, certainly
dozens, a few I even created myself. OpenSCAD has rules that I can’t remember
a single other language with an equivalent. It’s fine though! It works! Adding
multiple inheritance? Good grief no. Overloading? It would be wasteful
syntactic sugar. The peculiarities of OpenSCAD are bad enough without adding
stuff like this. I fully support the maintainers practice of keeping
enhancements as simple as possible. The discussion of "center" has been
refreshingly down to earth. I personally don’t care because I actually code in
OpenSCAD-BOSL2. I wish the namespaces for libraries would get solved. Like
objects, it seems like it’s been juts over the horizon for years. That’s 100
times more useful than overloading or inheritance. -Bob

![](https://www.gravatar.com/avatar/095124c1792024c67a3336fc575ec4a6?d=blank&s=100)

NH

nop head

Mon, Aug 25, 2025 9:26 PM

I don't see the problem with centre because when I model it's about 50/50  
if I want something centred.

On Mon, 25 Aug 2025 at 22:02, Bob Carlson via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I am very happy that objects have finally been released. I’ve followed all  
the discussions about OO with occasional insterest and sometimes horror.

The endless discussions of possible extensions has confused me mightily.  
The concurrent modification of the documentation by Vulcan, though well  
intentioned, is in my opinion a disaster.

Let me give a couple of examples. I would like to recode my small personal  
library using objects. Using objects to create a local namespace seems like  
a good idea but requires module references. With all the talk about them I  
have lost track of whether the latest build has them or not. I can’t trust  
the documentation to tell me. Apparently not supported yet.

I put together a module that would take a 2D path in 3D space and do a  
linear extrude along the normal of the 2D polygon. I have always been a bit  
confused about when a path becomes 2D geometry and can no longer be  
accessed as data. For example I would like to be able to get circle() to  
produce a path. That didn’t seem to work. I went to the wiki to try and  
understand. The muddling of terms by Vulcan made the exercise impossible. I  
So my linear_extrude3d module works using ideas and functions from BOSL2. I  
had to just muddle thru.

The discussions on object took a frustrating turn when it was suggested  
that object implies inheritance so OpenSCAD should support full  
inheritance. Since when has any thought that experience with any previous  
language should create expectations of OpenSCAD? I have no idea how many  
languages I have written code in by now, certainly dozens, a few I even  
created myself. OpenSCAD has rules that I can’t remember a single other  
language with an equivalent. It’s fine though! It works!

Adding multiple inheritance? Good grief no. Overloading? It would be  
wasteful syntactic sugar. The peculiarities of OpenSCAD are bad enough  
without adding stuff like this. I fully support the maintainers practice of  
keeping enhancements as simple as possible. The discussion of "center" has  
been refreshingly down to earth. I personally don’t care because I actually  
code in OpenSCAD-BOSL2.

I wish the namespaces for libraries would get solved. Like objects, it  
seems like it’s been juts over the horizon for years. That’s 100 times more  
useful than overloading or inheritance.

-Bob

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I don't see the problem with centre because when I model it's about 50/50 if I
want something centred. On Mon, 25 Aug 2025 at 22:02, Bob Carlson via Discuss
< discuss@lists.openscad.org> wrote: > I am very happy that objects have
finally been released. I’ve followed all > the discussions about OO with
occasional insterest and sometimes horror. > > The endless discussions of
possible extensions has confused me mightily. > The concurrent modification of
the documentation by Vulcan, though well > intentioned, is in my opinion a
disaster. > > Let me give a couple of examples. I would like to recode my
small personal > library using objects. Using objects to create a local
namespace seems like > a good idea but requires module references. With all
the talk about them I > have lost track of whether the latest build has them
or not. I can’t trust > the documentation to tell me. Apparently not supported
yet. > > I put together a module that would take a 2D path in 3D space and do
a > linear extrude along the normal of the 2D polygon. I have always been a
bit > confused about when a path becomes 2D geometry and can no longer be >
accessed as data. For example I would like to be able to get circle() to >
produce a path. That didn’t seem to work. I went to the wiki to try and >
understand. The muddling of terms by Vulcan made the exercise impossible. I >
So my linear_extrude3d module works using ideas and functions from BOSL2. I >
had to just muddle thru. > > The discussions on object took a frustrating turn
when it was suggested > that object implies inheritance so OpenSCAD should
support full > inheritance. Since when has any thought that experience with
any previous > language should create expectations of OpenSCAD? I have no idea
how many > languages I have written code in by now, certainly dozens, a few I
even > created myself. OpenSCAD has rules that I can’t remember a single other
> language with an equivalent. It’s fine though! It works! > > Adding multiple
inheritance? Good grief no. Overloading? It would be > wasteful syntactic
sugar. The peculiarities of OpenSCAD are bad enough > without adding stuff
like this. I fully support the maintainers practice of > keeping enhancements
as simple as possible. The discussion of "center" has > been refreshingly down
to earth. I personally don’t care because I actually > code in OpenSCAD-BOSL2.
> > I wish the namespaces for libraries would get solved. Like objects, it >
seems like it’s been juts over the horizon for years. That’s 100 times more >
useful than overloading or inheritance. > > -Bob >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/a11af2fdbb73a5b23029ce3c1a94cade?d=blank&s=100)

PK

Peter Kriens

Wed, Aug 27, 2025 1:45 PM

You can find the working proposal for the $this here:
<https://github.com/openscad/openscad/pull/6022>

If you can't build it yourself and you're on a Mac, I'd be happy to send you
the App to play with. It actually works like a charm!

This PR has unfortunately NO module references. I started working on module
references but lost appetite after the train wreck here around objects.

A workaround to the limitation that lack of reference gives, is to only have
functions in the object and then have one global module `mylib_render(object)`
in the global namespace that figures out what to do based in info in the
object. Not perfect, but the enemy of good is better.

The following is the kind of code I was thinking of for a library. (This is
not a proposal or anything real, it is just a working sketch I made an hour.)

Type = object( MOVE="move", CUBE="cube", CYL="cyl" );  
Move = object( type=Type.MOVE, size=[0,0,0]);  
Shape = object(  
size = [1,1,1],  
wall = 0,  
inner = function()  
let (  
z = closed ? 2 _wall : wall,  
shape = object(  
$this,  
size = size-[2_wall,2*wall,z]  
),  
)  
Mylib.move( vector=[0,0,z], shape ), // inner  
);  
Cube = object(  
Shape,  
type = Type.CUBE  
);  
Cyl = object(  
Shape,  
type = Type.CYL,  
);

Mylib = object(  
cube = function( size, wall=0, closed=false ) object(  
Cube,  
size = size,  
wall = wall,  
closed = closed,  
),  
cyl = function( size, wall=0, closed=false ) object(  
Cyl,  
size = size,  
wall = wall,  
closed = closed,  
),  
move = function( vector, shape ) object(  
Move,  
size = vector,  
child = shape ),  
);

module mylib( shape ) {

    
    
    module basic( shape) {
        if ( shape.type == Type.MOVE ) {
            translate( shape.size ) 
        basic( shape.child );
        } else if ( shape.type == Type.CUBE ) {
            cube(shape.size, center=true);
        } else if ( shape.type == Type.CYL ) {
            translate([0,0,-shape.size.z/2]) 
            scale( shape.size ) cylinder(d=1,h=1);
        }
    }
    
    difference() {
        basic( shape ); // outer
        if ( shape.wall ) {
            basic( shape.inner() );				
        }
    }
    

}

// examples  
$fn=100;  
translate([-5,0,0]) {  
s = Mylib.cube( size=[5,10,5], wall=1 );  
mylib(s);  
}  
translate([5,0,0]) {  
s = Mylib.cyl( size=[5,10,5], wall=0.5 );  
mylib(s);  
}

This works in my PR and gives:  
￼

I find it a real pity that $this got derailed because I really would like to
get your kind of experiences to see what details can be improved. The library
use case is for me very important. (To my eternal regret I am a yack shaver.
(I could've been rich!) I'd liked to contribute to BOSL, but after 45 years of
writing OO (really!) my hands are incapable of writing array code ... so I
needed objects in OpenSCAD so I can shave my yacks in BOSL ... Sigh.)

    
    
    Peter
    

____

On 25 Aug 2025, at 23:02, Bob Carlson via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

I am very happy that objects have finally been released. I’ve followed all the
discussions about OO with occasional insterest and sometimes horror.

The endless discussions of possible extensions has confused me mightily. The
concurrent modification of the documentation by Vulcan, though well
intentioned, is in my opinion a disaster.

Let me give a couple of examples. I would like to recode my small personal
library using objects. Using objects to create a local namespace seems like a
good idea but requires module references. With all the talk about them I have
lost track of whether the latest build has them or not. I can’t trust the
documentation to tell me. Apparently not supported yet.

I put together a module that would take a 2D path in 3D space and do a linear
extrude along the normal of the 2D polygon. I have always been a bit confused
about when a path becomes 2D geometry and can no longer be accessed as data.
For example I would like to be able to get circle() to produce a path. That
didn’t seem to work. I went to the wiki to try and understand. The muddling of
terms by Vulcan made the exercise impossible. I So my linear_extrude3d module
works using ideas and functions from BOSL2. I had to just muddle thru.

The discussions on object took a frustrating turn when it was suggested that
object implies inheritance so OpenSCAD should support full inheritance. Since
when has any thought that experience with any previous language should create
expectations of OpenSCAD? I have no idea how many languages I have written
code in by now, certainly dozens, a few I even created myself. OpenSCAD has
rules that I can’t remember a single other language with an equivalent. It’s
fine though! It works!

Adding multiple inheritance? Good grief no. Overloading? It would be wasteful
syntactic sugar. The peculiarities of OpenSCAD are bad enough without adding
stuff like this. I fully support the maintainers practice of keeping
enhancements as simple as possible. The discussion of "center" has been
refreshingly down to earth. I personally don’t care because I actually code in
OpenSCAD-BOSL2.

I wish the namespaces for libraries would get solved. Like objects, it seems
like it’s been juts over the horizon for years. That’s 100 times more useful
than overloading or inheritance.

-Bob

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

You can find the working proposal for the $this here:
https://github.com/openscad/openscad/pull/6022 If you can't build it yourself
and you're on a Mac, I'd be happy to send you the App to play with. It
actually works like a charm! This PR has unfortunately NO module references. I
started working on module references but lost appetite after the train wreck
here around objects. A workaround to the limitation that lack of reference
gives, is to only have functions in the object and then have one global module
`mylib_render(object)` in the global namespace that figures out what to do
based in info in the object. Not perfect, but the enemy of good is better. The
following is the kind of code I was thinking of for a library. (This is not a
proposal or anything real, it is just a working sketch I made an hour.) Type =
object( MOVE="move", CUBE="cube", CYL="cyl" ); Move = object( type=Type.MOVE,
size=[0,0,0]); Shape = object( size = [1,1,1], wall = 0, inner = function()
let ( z = closed ? 2*wall : wall, shape = object( $this, size =
size-[2*wall,2*wall,z] ), ) Mylib.move( vector=[0,0,z], shape ), // inner );
Cube = object( Shape, type = Type.CUBE ); Cyl = object( Shape, type =
Type.CYL, ); Mylib = object( cube = function( size, wall=0, closed=false )
object( Cube, size = size, wall = wall, closed = closed, ), cyl = function(
size, wall=0, closed=false ) object( Cyl, size = size, wall = wall, closed =
closed, ), move = function( vector, shape ) object( Move, size = vector, child
= shape ), ); module mylib( shape ) { module basic( shape) { if ( shape.type
== Type.MOVE ) { translate( shape.size ) basic( shape.child ); } else if (
shape.type == Type.CUBE ) { cube(shape.size, center=true); } else if (
shape.type == Type.CYL ) { translate([0,0,-shape.size.z/2]) scale( shape.size
) cylinder(d=1,h=1); } } difference() { basic( shape ); // outer if (
shape.wall ) { basic( shape.inner() ); } } } // examples $fn=100;
translate([-5,0,0]) { s = Mylib.cube( size=[5,10,5], wall=1 ); mylib(s); }
translate([5,0,0]) { s = Mylib.cyl( size=[5,10,5], wall=0.5 ); mylib(s); }
This works in my PR and gives: ￼ I find it a real pity that $this got derailed
because I really would like to get your kind of experiences to see what
details can be improved. The library use case is for me very important. (To my
eternal regret I am a yack shaver. (I could've been rich!) I'd liked to
contribute to BOSL, but after 45 years of writing OO (really!) my hands are
incapable of writing array code ... so I needed objects in OpenSCAD so I can
shave my yacks in BOSL ... Sigh.) Peter > On 25 Aug 2025, at 23:02, Bob
Carlson via Discuss <discuss@lists.openscad.org> wrote: > > I am very happy
that objects have finally been released. I’ve followed all the discussions
about OO with occasional insterest and sometimes horror. > > The endless
discussions of possible extensions has confused me mightily. The concurrent
modification of the documentation by Vulcan, though well intentioned, is in my
opinion a disaster. > > Let me give a couple of examples. I would like to
recode my small personal library using objects. Using objects to create a
local namespace seems like a good idea but requires module references. With
all the talk about them I have lost track of whether the latest build has them
or not. I can’t trust the documentation to tell me. Apparently not supported
yet. > > I put together a module that would take a 2D path in 3D space and do
a linear extrude along the normal of the 2D polygon. I have always been a bit
confused about when a path becomes 2D geometry and can no longer be accessed
as data. For example I would like to be able to get circle() to produce a
path. That didn’t seem to work. I went to the wiki to try and understand. The
muddling of terms by Vulcan made the exercise impossible. I So my
linear_extrude3d module works using ideas and functions from BOSL2. I had to
just muddle thru. > > The discussions on object took a frustrating turn when
it was suggested that object implies inheritance so OpenSCAD should support
full inheritance. Since when has any thought that experience with any previous
language should create expectations of OpenSCAD? I have no idea how many
languages I have written code in by now, certainly dozens, a few I even
created myself. OpenSCAD has rules that I can’t remember a single other
language with an equivalent. It’s fine though! It works! > > Adding multiple
inheritance? Good grief no. Overloading? It would be wasteful syntactic sugar.
The peculiarities of OpenSCAD are bad enough without adding stuff like this. I
fully support the maintainers practice of keeping enhancements as simple as
possible. The discussion of "center" has been refreshingly down to earth. I
personally don’t care because I actually code in OpenSCAD-BOSL2. > > I wish
the namespaces for libraries would get solved. Like objects, it seems like
it’s been juts over the horizon for years. That’s 100 times more useful than
overloading or inheritance. > > -Bob >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/678788/200)
](https://lists.openscad.org/empathy/attachment/678788)

![](https://www.gravatar.com/avatar/4ae585652404eee099c2b2e079e0c817?d=blank&s=100)

BC

Bob Carlson

Thu, Aug 28, 2025 12:12 AM

I gave it a few minutes and I cannot understand what’s going on. If it’s not
intuitive and doesn’t follow easily from existing OpenSCAD, I don’t think it
helps. It’s just an academic exercise. (And I share your age AND preference
for OO.)

-Bob

____

On Aug 27, 2025, at 06:45, Peter
Kriens[peter.kriens@aqute.biz](mailto:peter.kriens@aqute.biz) wrote:

You can find the working proposal for the $this here:
<https://github.com/openscad/openscad/pull/6022>

If you can't build it yourself and you're on a Mac, I'd be happy to send you
the App to play with. It actually works like a charm!

This PR has unfortunately NO module references. I started working on module
references but lost appetite after the train wreck here around objects.

A workaround to the limitation that lack of reference gives, is to only have
functions in the object and then have one global module `mylib_render(object)`
in the global namespace that figures out what to do based in info in the
object. Not perfect, but the enemy of good is better.

The following is the kind of code I was thinking of for a library. (This is
not a proposal or anything real, it is just a working sketch I made an hour.)

Type = object( MOVE="move", CUBE="cube", CYL="cyl" );  
Move = object( type=Type.MOVE, size=[0,0,0]);  
Shape = object(  
size = [1,1,1],  
wall = 0,  
inner = function()  
let (  
z = closed ? 2 _wall : wall,  
shape = object(  
$this,  
size = size-[2_wall,2*wall,z]  
),  
)  
Mylib.move( vector=[0,0,z], shape ), // inner  
);  
Cube = object(  
Shape,  
type = Type.CUBE  
);  
Cyl = object(  
Shape,  
type = Type.CYL,  
);

Mylib = object(  
cube = function( size, wall=0, closed=false ) object(  
Cube,  
size = size,  
wall = wall,  
closed = closed,  
),  
cyl = function( size, wall=0, closed=false ) object(  
Cyl,  
size = size,  
wall = wall,  
closed = closed,  
),  
move = function( vector, shape ) object(  
Move,  
size = vector,  
child = shape ),  
);

module mylib( shape ) {

    
    
     module basic( shape) {
         if ( shape.type == Type.MOVE ) {
             translate( shape.size ) 
        basic( shape.child );
         } else if ( shape.type == Type.CUBE ) {
             cube(shape.size, center=true);
         } else if ( shape.type == Type.CYL ) {
             translate([0,0,-shape.size.z/2]) 
             scale( shape.size ) cylinder(d=1,h=1);
         }
     }
    
     difference() {
         basic( shape ); // outer
         if ( shape.wall ) {
             basic( shape.inner() );				
         }
     }
    

}

// examples  
$fn=100;  
translate([-5,0,0]) {  
s = Mylib.cube( size=[5,10,5], wall=1 );  
mylib(s);  
}  
translate([5,0,0]) {  
s = Mylib.cyl( size=[5,10,5], wall=0.5 );  
mylib(s);  
}

This works in my PR and gives:  
<PastedGraphic-3.png>

I find it a real pity that $this got derailed because I really would like to
get your kind of experiences to see what details can be improved. The library
use case is for me very important. (To my eternal regret I am a yack shaver.
(I could've been rich!) I'd liked to contribute to BOSL, but after 45 years of
writing OO (really!) my hands are incapable of writing array code ... so I
needed objects in OpenSCAD so I can shave my yacks in BOSL ... Sigh.)

    
    
    Peter
    

____

On 25 Aug 2025, at 23:02, Bob Carlson via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

I am very happy that objects have finally been released. I’ve followed all the
discussions about OO with occasional insterest and sometimes horror.

The endless discussions of possible extensions has confused me mightily. The
concurrent modification of the documentation by Vulcan, though well
intentioned, is in my opinion a disaster.

Let me give a couple of examples. I would like to recode my small personal
library using objects. Using objects to create a local namespace seems like a
good idea but requires module references. With all the talk about them I have
lost track of whether the latest build has them or not. I can’t trust the
documentation to tell me. Apparently not supported yet.

I put together a module that would take a 2D path in 3D space and do a linear
extrude along the normal of the 2D polygon. I have always been a bit confused
about when a path becomes 2D geometry and can no longer be accessed as data.
For example I would like to be able to get circle() to produce a path. That
didn’t seem to work. I went to the wiki to try and understand. The muddling of
terms by Vulcan made the exercise impossible. I So my linear_extrude3d module
works using ideas and functions from BOSL2. I had to just muddle thru.

The discussions on object took a frustrating turn when it was suggested that
object implies inheritance so OpenSCAD should support full inheritance. Since
when has any thought that experience with any previous language should create
expectations of OpenSCAD? I have no idea how many languages I have written
code in by now, certainly dozens, a few I even created myself. OpenSCAD has
rules that I can’t remember a single other language with an equivalent. It’s
fine though! It works!

Adding multiple inheritance? Good grief no. Overloading? It would be wasteful
syntactic sugar. The peculiarities of OpenSCAD are bad enough without adding
stuff like this. I fully support the maintainers practice of keeping
enhancements as simple as possible. The discussion of "center" has been
refreshingly down to earth. I personally don’t care because I actually code in
OpenSCAD-BOSL2.

I wish the namespaces for libraries would get solved. Like objects, it seems
like it’s been juts over the horizon for years. That’s 100 times more useful
than overloading or inheritance.

-Bob

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I gave it a few minutes and I cannot understand what’s going on. If it’s not
intuitive and doesn’t follow easily from existing OpenSCAD, I don’t think it
helps. It’s just an academic exercise. (And I share your age AND preference
for OO.) -Bob > On Aug 27, 2025, at 06:45, Peter Kriens
<peter.kriens@aqute.biz> wrote: > > You can find the working proposal for the
$this here: https://github.com/openscad/openscad/pull/6022 > > If you can't
build it yourself and you're on a Mac, I'd be happy to send you the App to
play with. It actually works like a charm! > > This PR has unfortunately NO
module references. I started working on module references but lost appetite
after the train wreck here around objects. > > A workaround to the limitation
that lack of reference gives, is to only have functions in the object and then
have one global module `mylib_render(object)` in the global namespace that
figures out what to do based in info in the object. Not perfect, but the enemy
of good is better. > > The following is the kind of code I was thinking of for
a library. (This is not a proposal or anything real, it is just a working
sketch I made an hour.) > > Type = object( MOVE="move", CUBE="cube", CYL="cyl"
); > Move = object( type=Type.MOVE, size=[0,0,0]); > Shape = object( > size =
[1,1,1], > wall = 0, > inner = function() > let ( > z = closed ? 2*wall :
wall, > shape = object( > $this, > size = size-[2*wall,2*wall,z] > ), > ) >
Mylib.move( vector=[0,0,z], shape ), // inner > ); > Cube = object( > Shape, >
type = Type.CUBE > ); > Cyl = object( > Shape, > type = Type.CYL, > ); > >
Mylib = object( > cube = function( size, wall=0, closed=false ) object( >
Cube, > size = size, > wall = wall, > closed = closed, > ), > cyl = function(
size, wall=0, closed=false ) object( > Cyl, > size = size, > wall = wall, >
closed = closed, > ), > move = function( vector, shape ) object( > Move, >
size = vector, > child = shape ), > ); > > module mylib( shape ) { > > module
basic( shape) { > if ( shape.type == Type.MOVE ) { > translate( shape.size ) >
basic( shape.child ); > } else if ( shape.type == Type.CUBE ) { >
cube(shape.size, center=true); > } else if ( shape.type == Type.CYL ) { >
translate([0,0,-shape.size.z/2]) > scale( shape.size ) cylinder(d=1,h=1); > }
> } > > difference() { > basic( shape ); // outer > if ( shape.wall ) { >
basic( shape.inner() ); > } > } > } > > > // examples > $fn=100; >
translate([-5,0,0]) { > s = Mylib.cube( size=[5,10,5], wall=1 ); > mylib(s); >
} > translate([5,0,0]) { > s = Mylib.cyl( size=[5,10,5], wall=0.5 ); >
mylib(s); > } > > This works in my PR and gives: > <PastedGraphic-3.png> > > I
find it a real pity that $this got derailed because I really would like to get
your kind of experiences to see what details can be improved. The library use
case is for me very important. (To my eternal regret I am a yack shaver. (I
could've been rich!) I'd liked to contribute to BOSL, but after 45 years of
writing OO (really!) my hands are incapable of writing array code ... so I
needed objects in OpenSCAD so I can shave my yacks in BOSL ... Sigh.) > >
Peter > >> On 25 Aug 2025, at 23:02, Bob Carlson via Discuss
<discuss@lists.openscad.org> wrote: >> >> I am very happy that objects have
finally been released. I’ve followed all the discussions about OO with
occasional insterest and sometimes horror. >> >> The endless discussions of
possible extensions has confused me mightily. The concurrent modification of
the documentation by Vulcan, though well intentioned, is in my opinion a
disaster. >> >> Let me give a couple of examples. I would like to recode my
small personal library using objects. Using objects to create a local
namespace seems like a good idea but requires module references. With all the
talk about them I have lost track of whether the latest build has them or not.
I can’t trust the documentation to tell me. Apparently not supported yet. >>
>> I put together a module that would take a 2D path in 3D space and do a
linear extrude along the normal of the 2D polygon. I have always been a bit
confused about when a path becomes 2D geometry and can no longer be accessed
as data. For example I would like to be able to get circle() to produce a
path. That didn’t seem to work. I went to the wiki to try and understand. The
muddling of terms by Vulcan made the exercise impossible. I So my
linear_extrude3d module works using ideas and functions from BOSL2. I had to
just muddle thru. >> >> The discussions on object took a frustrating turn when
it was suggested that object implies inheritance so OpenSCAD should support
full inheritance. Since when has any thought that experience with any previous
language should create expectations of OpenSCAD? I have no idea how many
languages I have written code in by now, certainly dozens, a few I even
created myself. OpenSCAD has rules that I can’t remember a single other
language with an equivalent. It’s fine though! It works! >> >> Adding multiple
inheritance? Good grief no. Overloading? It would be wasteful syntactic sugar.
The peculiarities of OpenSCAD are bad enough without adding stuff like this. I
fully support the maintainers practice of keeping enhancements as simple as
possible. The discussion of "center" has been refreshingly down to earth. I
personally don’t care because I actually code in OpenSCAD-BOSL2. >> >> I wish
the namespaces for libraries would get solved. Like objects, it seems like
it’s been juts over the horizon for years. That’s 100 times more useful than
overloading or inheritance. >> >> -Bob >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/798098a6fc43352d853354f54544ef33?d=blank&s=100)

LM

Leonard Martin Struttmann

Thu, Aug 28, 2025 1:39 AM

*I gave it a few minutes and I cannot understand what’s going on. *

Me, too! It seems like a LOT of code that could be implemented easier with  
plain ol' OpenSCAD modules.

*I gave it a few minutes and I cannot understand what’s going on. * Me, too! It seems like a LOT of code that could be implemented easier with plain ol' OpenSCAD modules. 

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Thu, Aug 28, 2025 5:36 AM

On 8/28/2025 3:39 AM, Leonard Martin Struttmann via Discuss wrote:

____

Me, too! It seems like a LOT of code that could be implemented easier  
with plain ol' OpenSCAD modules.

Without talking about any particular replacement style... the problem  
with plain ol' OpenSCAD modules is naming.

BOSL2, for instance, undoubtedly has numerous internal functions and  
modules. They exist to help it do its work; they are not for your use  
and so are not documented.

What happens if you happen to define a module with the same name as one  
of BOSL2's internal modules? Nothing good, I'm sure. Heck, BOSL2 has a  
_lot_ of documented modules; do you keep a full list in your head as  
names to avoid?

And if you _do_ avoid all of BOSL2's names... will tomorrow's version  
add a new name that conflicts with a name in your project?

And if you want to use BOSL2 in conjunction with some other library, do  
they have names that conflict?

The goal of this particular sub-effort (or you might see reference to a  
"namespace" effort with similar goals) is to allow a library to isolate  
its names, so that you only get the library's module when you  
specifically ask for it.

On 8/28/2025 3:39 AM, Leonard Martin Struttmann via Discuss wrote: > Me, too!
It seems like a LOT of code that could be implemented easier > with plain ol'
OpenSCAD modules. Without talking about any particular replacement style...
the problem with plain ol' OpenSCAD modules is naming. BOSL2, for instance,
undoubtedly has numerous internal functions and modules. They exist to help it
do its work; they are not for your use and so are not documented. What happens
if you happen to define a module with the same name as one of BOSL2's internal
modules? Nothing good, I'm sure. Heck, BOSL2 has a *lot* of documented
modules; do you keep a full list in your head as names to avoid? And if you
*do* avoid all of BOSL2's names... will tomorrow's version add a new name that
conflicts with a name in your project? And if you want to use BOSL2 in
conjunction with some other library, do they have names that conflict? The
goal of this particular sub-effort (or you might see reference to a
"namespace" effort with similar goals) is to allow a library to isolate its
names, so that you only get the library's module when you specifically ask for
it.

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Thu, Aug 28, 2025 5:54 AM

And if you don't use or write libraries, or the libraries that you use  
or write haven't chosen to adopt whatever name management scheme we come  
up with, then the effect on you is almost exactly zero. (There may be a  
few new names that you must avoid.)

And if you don't use or write libraries, or the libraries that you use or
write haven't chosen to adopt whatever name management scheme we come up with,
then the effect on you is almost exactly zero. (There may be a few new names
that you must avoid.)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

