---
url: https://lists.openscad.org/empathy/thread/ZSY7FECJEKETZTWJCPKXCOPPQ4R4OOAF
scraped_at: 2025-09-08T16:28:32.706954
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

###  projection(cut=true) question

![](https://www.gravatar.com/avatar/73fc5538ea57395caa32e2b5c63acdc0?d=blank&s=100)

JD

John David

Mon, Aug 25, 2025 5:00 AM

Is there a clean way to set up a projection(cut=var) such that var can be  
set in the interface, and if it is not set, then extrude the part to some  
thickness without duplicating the call inside an if/then/else?

pseudo code:

    
    
    if (projection_cut) {
        projection(cut = true)
           part1(var1, ... );
    } else {
        linear_extrude(thickness2)
             part1(var1, ... );
    }
    

I've tried a number of things and get various complaints like:

    
    
        projection(cut = projection_cut)
        linear_extrude(thickness2)
           part1(var1, ... );
    

and

    
    
        linear_extrude(thickness2)
        projection(cut = projection_cut)
           part1(var1, ... );
    

And similar variants.

Anyway, I am hoping to clean up some code.

EBo --

Is there a clean way to set up a projection(cut=var) such that var can be set
in the interface, and if it is not set, then extrude the part to some
thickness without duplicating the call inside an if/then/else? pseudo code: if
(projection_cut) { projection(cut = true) part1(var1, ... ); } else {
linear_extrude(thickness2) part1(var1, ... ); } I've tried a number of things
and get various complaints like: projection(cut = projection_cut)
linear_extrude(thickness2) part1(var1, ... ); and linear_extrude(thickness2)
projection(cut = projection_cut) part1(var1, ... ); And similar variants.
Anyway, I am hoping to clean up some code. EBo --

![](https://www.gravatar.com/avatar/73fc5538ea57395caa32e2b5c63acdc0?d=blank&s=100)

JD

John David

Mon, Aug 25, 2025 5:56 AM

I need to modify my description above (I misunderstood what the  
projection(cut) was doing). Basically under normal conditions I want the  
part to 3D render, but if I set a cut variable, I wanted it projected into  
2D to process as a laser cut file. I was hoping there was a trick to keep  
from duplicating the calls.

EBo --

On Mon, Aug 25, 2025 at 1:00 AM John David
[ebo.2112@gmail.com](mailto:ebo.2112@gmail.com) wrote:

____

Is there a clean way to set up a projection(cut=var) such that var can be  
set in the interface, and if it is not set, then extrude the part to some  
thickness without duplicating the call inside an if/then/else?

pseudo code:

    
    
     if (projection_cut) {
         projection(cut = true)
            part1(var1, ... );
     } else {
         linear_extrude(thickness2)
              part1(var1, ... );
     }
    

I've tried a number of things and get various complaints like:

    
    
         projection(cut = projection_cut)
         linear_extrude(thickness2)
            part1(var1, ... );
    

and

    
    
         linear_extrude(thickness2)
         projection(cut = projection_cut)
            part1(var1, ... );
    

And similar variants.

Anyway, I am hoping to clean up some code.

EBo --

I need to modify my description above (I misunderstood what the
projection(cut) was doing). Basically under normal conditions I want the part
to 3D render, but if I set a cut variable, I wanted it projected into 2D to
process as a laser cut file. I was hoping there was a trick to keep from
duplicating the calls. EBo -- On Mon, Aug 25, 2025 at 1:00 AM John David
<ebo.2112@gmail.com> wrote: > Is there a clean way to set up a
projection(cut=var) such that var can be > set in the interface, and if it is
not set, then extrude the part to some > thickness without duplicating the
call inside an if/then/else? > > pseudo code: > > if (projection_cut) { >
projection(cut = true) > part1(var1, ... ); > } else { >
linear_extrude(thickness2) > part1(var1, ... ); > } > > I've tried a number of
things and get various complaints like: > > projection(cut = projection_cut) >
linear_extrude(thickness2) > part1(var1, ... ); > > and > >
linear_extrude(thickness2) > projection(cut = projection_cut) > part1(var1,
... ); > > And similar variants. > > Anyway, I am hoping to clean up some
code. > > EBo -- >

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Aug 25, 2025 7:40 AM

On 8/25/2025 7:56 AM, John David via Discuss wrote:

____

Basically under normal conditions I want the part to 3D render, but if  
I set a cut variable, I wanted it projected into 2D to process as a  
laser cut file. I was hoping there was a trick to keep from  
duplicating the calls.

shouldCut = false;

module maybeCut() {  
if (shouldCut) {  
projection(cut=true)  
children();  
} else {  
children();  
}  
}

maybeCut() sphere(r=20);

Similarly if you really meant project rather than cut.

On 8/25/2025 7:56 AM, John David via Discuss wrote: > Basically under normal
conditions I want the part to 3D render, but if > I set a cut variable, I
wanted it projected into 2D to process as a > laser cut file. I was hoping
there was a trick to keep from > duplicating the calls. shouldCut = false;
module maybeCut() { if (shouldCut) { projection(cut=true) children(); } else {
children(); } } maybeCut() sphere(r=20); Similarly if you really meant project
rather than cut.

![](https://www.gravatar.com/avatar/73fc5538ea57395caa32e2b5c63acdc0?d=blank&s=100)

JD

John David

Mon, Aug 25, 2025 11:12 AM

Thank you. That worked!

On Mon, Aug 25, 2025 at 3:40 AM Jordan Brown
[openscad@jordan.maileater.net](mailto:openscad@jordan.maileater.net)  
wrote:

____

On 8/25/2025 7:56 AM, John David via Discuss wrote:

Basically under normal conditions I want the part to 3D render, but if I  
set a cut variable, I wanted it projected into 2D to process as a laser cut  
file. I was hoping there was a trick to keep from duplicating the calls.

shouldCut = false;

module maybeCut() {  
if (shouldCut) {  
projection(cut=true)  
children();  
} else {  
children();  
}  
}

maybeCut() sphere(r=20);

Similarly if you really meant project rather than cut.

Thank you. That worked! On Mon, Aug 25, 2025 at 3:40 AM Jordan Brown
<openscad@jordan.maileater.net> wrote: > > On 8/25/2025 7:56 AM, John David
via Discuss wrote: > > Basically under normal conditions I want the part to 3D
render, but if I > set a cut variable, I wanted it projected into 2D to
process as a laser cut > file. I was hoping there was a trick to keep from
duplicating the calls. > > shouldCut = false; > > module maybeCut() { > if
(shouldCut) { > projection(cut=true) > children(); > } else { > children(); >
} > } > > maybeCut() sphere(r=20); > > > Similarly if you really meant project
rather than cut. > > >

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

