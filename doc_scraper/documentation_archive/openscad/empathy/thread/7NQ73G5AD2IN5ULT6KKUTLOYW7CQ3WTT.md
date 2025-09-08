---
url: https://lists.openscad.org/empathy/thread/7NQ73G5AD2IN5ULT6KKUTLOYW7CQ3WTT
scraped_at: 2025-09-08T16:28:18.716233
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

###  Functions as Object Members: Recalculation slowing down compilation

![](https://www.gravatar.com/avatar/b748bb54f164c5fafb7e920f624d4cd0?d=blank&s=100)

NS

Nathan Sokalski

Sat, Aug 30, 2025 9:42 PM

I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function? Nathan
Sokalski njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Sat, Aug 30, 2025 9:48 PM

If the function is going to return the same value after objection creation  
shouldn't you be creating the object with that member as a variable and  
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I have been working on a new model using the 2025.07.11 prebuild  
containing the object() function. Many of my objects contain members that  
are functions, even functions that call other members that are also  
functions. My code seems to be getting very slow, and (correct me if I am  
wrong) I was wondering if this is because so many functions are being  
called so many times. Most of these function members will always return the  
same value once the object is created (they do not have any parameters, and  
the equation or operations in them only use constants). Is there a way to  
avoid recalculating a function a large number of times? For example, if a  
function does nothing other than return the sum of 2 other constant  
members, is there a way to assign a value to the member that is a  
"calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

If the function is going to return the same value after objection creation
shouldn't you be creating the object with that member as a variable and
compute its value at creation time? On Sat, Aug 30, 2025 at 5:43 PM Nathan
Sokalski via Discuss < discuss@lists.openscad.org> wrote: > I have been
working on a new model using the 2025.07.11 prebuild > containing the object()
function. Many of my objects contain members that > are functions, even
functions that call other members that are also > functions. My code seems to
be getting very slow, and (correct me if I am > wrong) I was wondering if this
is because so many functions are being > called so many times. Most of these
function members will always return the > same value once the object is
created (they do not have any parameters, and > the equation or operations in
them only use constants). Is there a way to > avoid recalculating a function a
large number of times? For example, if a > function does nothing other than
return the sum of 2 other constant > members, is there a way to assign a value
to the member that is a > "calculated constant" instead of a function? > >
Nathan Sokalski > njsokalski@hotmail.com >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/b748bb54f164c5fafb7e920f624d4cd0?d=blank&s=100)

NS

Nathan Sokalski

Sat, Aug 30, 2025 11:19 PM

How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the object is
created, but are unknown prior to calculation.

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Sent: Saturday, August 30, 2025 5:48 PM  
To: OpenSCAD general discussion Mailing-list
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

If the function is going to return the same value after objection creation
shouldn't you be creating the object with that member as a variable and
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

How would I do something like the following? righttriangle=object( SideA=3,
SideB=4,
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),
AngleC=90); In this object, SideC, AngleA & AngleB will remain the same once
the object is created, but are unknown prior to calculation. Nathan Sokalski
njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Adrian Mariano via Discuss
<discuss@lists.openscad.org> Sent: Saturday, August 30, 2025 5:48 PM To:
OpenSCAD general discussion Mailing-list <discuss@lists.openscad.org> Cc:
Adrian Mariano <avm4@cornell.edu> Subject: [OpenSCAD] Re: Functions as Object
Members: Recalculation slowing down compilation If the function is going to
return the same value after objection creation shouldn't you be creating the
object with that member as a variable and compute its value at creation time?
On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote: I have
been working on a new model using the 2025.07.11 prebuild containing the
object() function. Many of my objects contain members that are functions, even
functions that call other members that are also functions. My code seems to be
getting very slow, and (correct me if I am wrong) I was wondering if this is
because so many functions are being called so many times. Most of these
function members will always return the same value once the object is created
(they do not have any parameters, and the equation or operations in them only
use constants). Is there a way to avoid recalculating a function a large
number of times? For example, if a function does nothing other than return the
sum of 2 other constant members, is there a way to assign a value to the
member that is a "calculated constant" instead of a function? Nathan Sokalski
njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
_______________________________________________ OpenSCAD mailing list To
unsubscribe send an email to discuss-leave@lists.openscad.org<mailto:discuss-
leave@lists.openscad.org>

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Sat, Aug 30, 2025 11:44 PM

What's the larger context here? Are you proposing that you're actually  
going to make that object by using the above code as shown? Because I  
can't see how that's sensible. It's a lot of complicated stuff to type to  
create the object. If the object is actually made by a function, the  
function precomputes everything and fills in the fields. That seems  
straight forward. So I'm not sure why you can't do it that way.

Or if you really want to embed just that somewhere, you could do  
this...which really is more or less what the function I mentioned would  
look like:

righttriangle=  
let(SideA=3,  
SideB=4,  
SideC=sqrt(SideA^2+SideB^2),  
AngleA=asin(SideA/SideC),  
AngleB=asin(SideB/SideC)  
)  
object(  
SideA=SideA,  
SideB=SideB,  
SideC=SideC,  
AngleA=AngleA,  
AngleB=AngleB,  
AngleC=90);

Of course, really the sides and angles should be either arrays or objects  
too.

On Sat, Aug 30, 2025 at 7:20 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the  
object is created, but are unknown prior to calculation.

## Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

_From:_ Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
_Sent:_ Saturday, August 30, 2025 5:48 PM  
_To:_ OpenSCAD general discussion Mailing-list
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)

____

_Cc:_ Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
_Subject:_ [OpenSCAD] Re: Functions as Object Members: Recalculation  
slowing down compilation

If the function is going to return the same value after objection creation  
shouldn't you be creating the object with that member as a variable and  
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

I have been working on a new model using the 2025.07.11 prebuild  
containing the object() function. Many of my objects contain members that  
are functions, even functions that call other members that are also  
functions. My code seems to be getting very slow, and (correct me if I am  
wrong) I was wondering if this is because so many functions are being  
called so many times. Most of these function members will always return the  
same value once the object is created (they do not have any parameters, and  
the equation or operations in them only use constants). Is there a way to  
avoid recalculating a function a large number of times? For example, if a  
function does nothing other than return the sum of 2 other constant  
members, is there a way to assign a value to the member that is a  
"calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

What's the larger context here? Are you proposing that you're actually going
to make that object by using the above code as shown? Because I can't see how
that's sensible. It's a lot of complicated stuff to type to create the object.
If the object is actually made by a function, the function precomputes
everything and fills in the fields. That seems straight forward. So I'm not
sure why you can't do it that way. Or if you really want to embed just that
somewhere, you could do this...which really is more or less what the function
I mentioned would look like: righttriangle= let(SideA=3, SideB=4,
SideC=sqrt(SideA^2+SideB^2), AngleA=asin(SideA/SideC),
AngleB=asin(SideB/SideC) ) object( SideA=SideA, SideB=SideB, SideC=SideC,
AngleA=AngleA, AngleB=AngleB, AngleC=90); Of course, really the sides and
angles should be either arrays or objects too. On Sat, Aug 30, 2025 at 7:20 PM
Nathan Sokalski via Discuss < discuss@lists.openscad.org> wrote: > How would I
do something like the following? > righttriangle=object( > SideA=3, > SideB=4,
> SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))), >
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())), >
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())), >
AngleC=90); > In this object, SideC, AngleA & AngleB will remain the same once
the > object is created, but are unknown prior to calculation. > > Nathan
Sokalski > njsokalski@hotmail.com > \------------------------------ > *From:*
Adrian Mariano via Discuss <discuss@lists.openscad.org> > *Sent:* Saturday,
August 30, 2025 5:48 PM > *To:* OpenSCAD general discussion Mailing-list
<discuss@lists.openscad.org > > > *Cc:* Adrian Mariano <avm4@cornell.edu> >
*Subject:* [OpenSCAD] Re: Functions as Object Members: Recalculation > slowing
down compilation > > If the function is going to return the same value after
objection creation > shouldn't you be creating the object with that member as
a variable and > compute its value at creation time? > > On Sat, Aug 30, 2025
at 5:43 PM Nathan Sokalski via Discuss < > discuss@lists.openscad.org> wrote:
> > I have been working on a new model using the 2025.07.11 prebuild >
containing the object() function. Many of my objects contain members that >
are functions, even functions that call other members that are also >
functions. My code seems to be getting very slow, and (correct me if I am >
wrong) I was wondering if this is because so many functions are being > called
so many times. Most of these function members will always return the > same
value once the object is created (they do not have any parameters, and > the
equation or operations in them only use constants). Is there a way to > avoid
recalculating a function a large number of times? For example, if a > function
does nothing other than return the sum of 2 other constant > members, is there
a way to assign a value to the member that is a > "calculated constant"
instead of a function? > > Nathan Sokalski > njsokalski@hotmail.com >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/b748bb54f164c5fafb7e920f624d4cd0?d=blank&s=100)

NS

Nathan Sokalski

Sun, Aug 31, 2025 12:50 AM

I guess the way you show it does work, so I will probably end up doing it that
way, I guess it felt redundant to me to be assigning values in the let()
statement and then (what feels like) reassigning them in the result. But it
does seem to work and make sense, even if 2X as many lines of code. Thanks!

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Sent: Saturday, August 30, 2025 7:44 PM  
To: OpenSCAD general discussion Mailing-list
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

What's the larger context here? Are you proposing that you're actually going
to make that object by using the above code as shown? Because I can't see how
that's sensible. It's a lot of complicated stuff to type to create the object.
If the object is actually made by a function, the function precomputes
everything and fills in the fields. That seems straight forward. So I'm not
sure why you can't do it that way.

Or if you really want to embed just that somewhere, you could do this...which
really is more or less what the function I mentioned would look like:

righttriangle=  
let(SideA=3,  
SideB=4,  
SideC=sqrt(SideA^2+SideB^2),  
AngleA=asin(SideA/SideC),  
AngleB=asin(SideB/SideC)  
)  
object(  
SideA=SideA,  
SideB=SideB,  
SideC=SideC,  
AngleA=AngleA,  
AngleB=AngleB,  
AngleC=90);

Of course, really the sides and angles should be either arrays or objects too.

On Sat, Aug 30, 2025 at 7:20 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the object is
created, but are unknown prior to calculation.

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
Sent: Saturday, August 30, 2025 5:48 PM  
To: OpenSCAD general discussion Mailing-list
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
Cc: Adrian Mariano
<[avm4@cornell.edu](mailto:avm4@cornell.edu)[mailto:avm4@cornell.edu](mailto:avm4@cornell.edu)>  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

If the function is going to return the same value after objection creation
shouldn't you be creating the object with that member as a variable and
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I guess the way you show it does work, so I will probably end up doing it that
way, I guess it felt redundant to me to be assigning values in the let()
statement and then (what feels like) reassigning them in the result. But it
does seem to work and make sense, even if 2X as many lines of code. Thanks!
Nathan Sokalski njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Adrian Mariano via Discuss
<discuss@lists.openscad.org> Sent: Saturday, August 30, 2025 7:44 PM To:
OpenSCAD general discussion Mailing-list <discuss@lists.openscad.org> Cc:
Adrian Mariano <avm4@cornell.edu> Subject: [OpenSCAD] Re: Functions as Object
Members: Recalculation slowing down compilation What's the larger context
here? Are you proposing that you're actually going to make that object by
using the above code as shown? Because I can't see how that's sensible. It's a
lot of complicated stuff to type to create the object. If the object is
actually made by a function, the function precomputes everything and fills in
the fields. That seems straight forward. So I'm not sure why you can't do it
that way. Or if you really want to embed just that somewhere, you could do
this...which really is more or less what the function I mentioned would look
like: righttriangle= let(SideA=3, SideB=4, SideC=sqrt(SideA^2+SideB^2),
AngleA=asin(SideA/SideC), AngleB=asin(SideB/SideC) ) object( SideA=SideA,
SideB=SideB, SideC=SideC, AngleA=AngleA, AngleB=AngleB, AngleC=90); Of course,
really the sides and angles should be either arrays or objects too. On Sat,
Aug 30, 2025 at 7:20 PM Nathan Sokalski via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote: How
would I do something like the following? righttriangle=object( SideA=3,
SideB=4,
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),
AngleC=90); In this object, SideC, AngleA & AngleB will remain the same once
the object is created, but are unknown prior to calculation. Nathan Sokalski
njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Adrian Mariano via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> Sent:
Saturday, August 30, 2025 5:48 PM To: OpenSCAD general discussion Mailing-list
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> Cc: Adrian
Mariano <avm4@cornell.edu<mailto:avm4@cornell.edu>> Subject: [OpenSCAD] Re:
Functions as Object Members: Recalculation slowing down compilation If the
function is going to return the same value after objection creation shouldn't
you be creating the object with that member as a variable and compute its
value at creation time? On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via
Discuss <discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote:
I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function? Nathan
Sokalski njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
_______________________________________________ OpenSCAD mailing list To
unsubscribe send an email to discuss-leave@lists.openscad.org<mailto:discuss-
leave@lists.openscad.org> _______________________________________________
OpenSCAD mailing list To unsubscribe send an email to discuss-
leave@lists.openscad.org<mailto:discuss-leave@lists.openscad.org>

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Sun, Aug 31, 2025 1:45 AM

If this were a function that made the triangle object you could of course  
dispense with the let and just create the object, with sideA and sideB  
being function parameters. This is why I noted on the absence of larger  
context that might clarify what you actually need. The let is needed to  
create and hold the values of sideA and sideB, which have to come from  
somewhere. If they are already in scope you don't need a let to make them,  
but the code fragment you show doesn't really make sense to me as it  
stands, because I wouldn't hard code values for the sides into a structure  
like that.

On Sat, Aug 30, 2025 at 8:51 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I guess the way you show it does work, so I will probably end up doing it  
that way, I guess it felt redundant to me to be assigning values in the  
let() statement and then (what feels like) reassigning them in the result.  
But it does seem to work and make sense, even if 2X as many lines of code.  
Thanks!

## Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

_From:_ Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
_Sent:_ Saturday, August 30, 2025 7:44 PM  
_To:_ OpenSCAD general discussion Mailing-list
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)

____

_Cc:_ Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
_Subject:_ [OpenSCAD] Re: Functions as Object Members: Recalculation  
slowing down compilation

What's the larger context here? Are you proposing that you're actually  
going to make that object by using the above code as shown? Because I  
can't see how that's sensible. It's a lot of complicated stuff to type to  
create the object. If the object is actually made by a function, the  
function precomputes everything and fills in the fields. That seems  
straight forward. So I'm not sure why you can't do it that way.

Or if you really want to embed just that somewhere, you could do  
this...which really is more or less what the function I mentioned would  
look like:

righttriangle=  
let(SideA=3,  
SideB=4,  
SideC=sqrt(SideA^2+SideB^2),  
AngleA=asin(SideA/SideC),  
AngleB=asin(SideB/SideC)  
)  
object(  
SideA=SideA,  
SideB=SideB,  
SideC=SideC,  
AngleA=AngleA,  
AngleB=AngleB,  
AngleC=90);

Of course, really the sides and angles should be either arrays or objects  
too.

On Sat, Aug 30, 2025 at 7:20 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the  
object is created, but are unknown prior to calculation.

## Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

_From:_ Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
_Sent:_ Saturday, August 30, 2025 5:48 PM  
_To:_ OpenSCAD general discussion Mailing-list
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)

____

_Cc:_ Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
_Subject:_ [OpenSCAD] Re: Functions as Object Members: Recalculation  
slowing down compilation

If the function is going to return the same value after objection creation  
shouldn't you be creating the object with that member as a variable and  
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

I have been working on a new model using the 2025.07.11 prebuild  
containing the object() function. Many of my objects contain members that  
are functions, even functions that call other members that are also  
functions. My code seems to be getting very slow, and (correct me if I am  
wrong) I was wondering if this is because so many functions are being  
called so many times. Most of these function members will always return the  
same value once the object is created (they do not have any parameters, and  
the equation or operations in them only use constants). Is there a way to  
avoid recalculating a function a large number of times? For example, if a  
function does nothing other than return the sum of 2 other constant  
members, is there a way to assign a value to the member that is a  
"calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

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

If this were a function that made the triangle object you could of course
dispense with the let and just create the object, with sideA and sideB being
function parameters. This is why I noted on the absence of larger context that
might clarify what you actually need. The let is needed to create and hold the
values of sideA and sideB, which have to come from somewhere. If they are
already in scope you don't need a let to make them, but the code fragment you
show doesn't really make sense to me as it stands, because I wouldn't hard
code values for the sides into a structure like that. On Sat, Aug 30, 2025 at
8:51 PM Nathan Sokalski via Discuss < discuss@lists.openscad.org> wrote: > I
guess the way you show it does work, so I will probably end up doing it > that
way, I guess it felt redundant to me to be assigning values in the > let()
statement and then (what feels like) reassigning them in the result. > But it
does seem to work and make sense, even if 2X as many lines of code. > Thanks!
> > Nathan Sokalski > njsokalski@hotmail.com > \------------------------------
> *From:* Adrian Mariano via Discuss <discuss@lists.openscad.org> > *Sent:*
Saturday, August 30, 2025 7:44 PM > *To:* OpenSCAD general discussion Mailing-
list <discuss@lists.openscad.org > > > *Cc:* Adrian Mariano <avm4@cornell.edu>
> *Subject:* [OpenSCAD] Re: Functions as Object Members: Recalculation >
slowing down compilation > > What's the larger context here? Are you proposing
that you're actually > going to make that object by using the above code as
shown? Because I > can't see how that's sensible. It's a lot of complicated
stuff to type to > create the object. If the object is actually made by a
function, the > function precomputes everything and fills in the fields. That
seems > straight forward. So I'm not sure why you can't do it that way. > > Or
if you really want to embed just that somewhere, you could do > this...which
really is more or less what the function I mentioned would > look like: > >
righttriangle= > let(SideA=3, > SideB=4, > SideC=sqrt(SideA^2+SideB^2), >
AngleA=asin(SideA/SideC), > AngleB=asin(SideB/SideC) > ) > object( >
SideA=SideA, > SideB=SideB, > SideC=SideC, > AngleA=AngleA, > AngleB=AngleB, >
AngleC=90); > > Of course, really the sides and angles should be either arrays
or objects > too. > > On Sat, Aug 30, 2025 at 7:20 PM Nathan Sokalski via
Discuss < > discuss@lists.openscad.org> wrote: > > How would I do something
like the following? > righttriangle=object( > SideA=3, > SideB=4, >
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))), >
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())), >
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())), >
AngleC=90); > In this object, SideC, AngleA & AngleB will remain the same once
the > object is created, but are unknown prior to calculation. > > Nathan
Sokalski > njsokalski@hotmail.com > \------------------------------ > *From:*
Adrian Mariano via Discuss <discuss@lists.openscad.org> > *Sent:* Saturday,
August 30, 2025 5:48 PM > *To:* OpenSCAD general discussion Mailing-list
<discuss@lists.openscad.org > > > *Cc:* Adrian Mariano <avm4@cornell.edu> >
*Subject:* [OpenSCAD] Re: Functions as Object Members: Recalculation > slowing
down compilation > > If the function is going to return the same value after
objection creation > shouldn't you be creating the object with that member as
a variable and > compute its value at creation time? > > On Sat, Aug 30, 2025
at 5:43 PM Nathan Sokalski via Discuss < > discuss@lists.openscad.org> wrote:
> > I have been working on a new model using the 2025.07.11 prebuild >
containing the object() function. Many of my objects contain members that >
are functions, even functions that call other members that are also >
functions. My code seems to be getting very slow, and (correct me if I am >
wrong) I was wondering if this is because so many functions are being > called
so many times. Most of these function members will always return the > same
value once the object is created (they do not have any parameters, and > the
equation or operations in them only use constants). Is there a way to > avoid
recalculating a function a large number of times? For example, if a > function
does nothing other than return the sum of 2 other constant > members, is there
a way to assign a value to the member that is a > "calculated constant"
instead of a function? > > Nathan Sokalski > njsokalski@hotmail.com >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sun, Aug 31, 2025 2:15 AM

I'm assuming you're trying to do lazy evaluation? My idea:

First, use Python convention of always having "self" as the first argument of
all functions intended as methods.

Second, don't retrieve values directly. Use this function:

function zed(obj, member) =  
let ( thunk = obj[member] )  
is_function(thunk) ? thunk(obj) : thunk;

member is a string unfortunately.

On August 30, 2025 4:19:58 PM PDT, Nathan Sokalski via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the object is
created, but are unknown prior to calculation.

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Sent: Saturday, August 30, 2025 5:48 PM  
To: OpenSCAD general discussion Mailing-list
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

If the function is going to return the same value after objection creation
shouldn't you be creating the object with that member as a variable and
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I'm assuming you're trying to do lazy evaluation? My idea: First, use Python
convention of always having "self" as the first argument of all functions
intended as methods. Second, don't retrieve values directly. Use this
function: function zed(obj, member) = let ( thunk = obj[member] )
is_function(thunk) ? thunk(obj) : thunk; member is a string unfortunately. On
August 30, 2025 4:19:58 PM PDT, Nathan Sokalski via Discuss
<discuss@lists.openscad.org> wrote: >How would I do something like the
following? >righttriangle=object( > SideA=3, > SideB=4, >
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))), >
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())), >
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())), >
AngleC=90); >In this object, SideC, AngleA & AngleB will remain the same once
the object is created, but are unknown prior to calculation. > >Nathan
Sokalski >njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
>________________________________ >From: Adrian Mariano via Discuss
<discuss@lists.openscad.org> >Sent: Saturday, August 30, 2025 5:48 PM >To:
OpenSCAD general discussion Mailing-list <discuss@lists.openscad.org> >Cc:
Adrian Mariano <avm4@cornell.edu> >Subject: [OpenSCAD] Re: Functions as Object
Members: Recalculation slowing down compilation > >If the function is going to
return the same value after objection creation shouldn't you be creating the
object with that member as a variable and compute its value at creation time?
> >On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote: >I have
been working on a new model using the 2025.07.11 prebuild containing the
object() function. Many of my objects contain members that are functions, even
functions that call other members that are also functions. My code seems to be
getting very slow, and (correct me if I am wrong) I was wondering if this is
because so many functions are being called so many times. Most of these
function members will always return the same value once the object is created
(they do not have any parameters, and the equation or operations in them only
use constants). Is there a way to avoid recalculating a function a large
number of times? For example, if a function does nothing other than return the
sum of 2 other constant members, is there a way to assign a value to the
member that is a "calculated constant" instead of a function? > >Nathan
Sokalski >njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
>_______________________________________________ >OpenSCAD mailing list >To
unsubscribe send an email to discuss-leave@lists.openscad.org<mailto:discuss-
leave@lists.openscad.org>

![](https://www.gravatar.com/avatar/b748bb54f164c5fafb7e920f624d4cd0?d=blank&s=100)

NS

Nathan Sokalski

Sun, Aug 31, 2025 2:23 AM

The triangle might not have been a great example, it was just the first idea
that popped into my head because it has props calculated from other props,
they wee just hard coded here as an example, I think your let suggestion it
good

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Sent: Saturday, August 30, 2025 9:45 PM  
To: OpenSCAD general discussion Mailing-list
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

If this were a function that made the triangle object you could of course
dispense with the let and just create the object, with sideA and sideB being
function parameters. This is why I noted on the absence of larger context that
might clarify what you actually need. The let is needed to create and hold the
values of sideA and sideB, which have to come from somewhere. If they are
already in scope you don't need a let to make them, but the code fragment you
show doesn't really make sense to me as it stands, because I wouldn't hard
code values for the sides into a structure like that.

On Sat, Aug 30, 2025 at 8:51 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
I guess the way you show it does work, so I will probably end up doing it that
way, I guess it felt redundant to me to be assigning values in the let()
statement and then (what feels like) reassigning them in the result. But it
does seem to work and make sense, even if 2X as many lines of code. Thanks!

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
Sent: Saturday, August 30, 2025 7:44 PM  
To: OpenSCAD general discussion Mailing-list
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
Cc: Adrian Mariano
<[avm4@cornell.edu](mailto:avm4@cornell.edu)[mailto:avm4@cornell.edu](mailto:avm4@cornell.edu)>  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

What's the larger context here? Are you proposing that you're actually going
to make that object by using the above code as shown? Because I can't see how
that's sensible. It's a lot of complicated stuff to type to create the object.
If the object is actually made by a function, the function precomputes
everything and fills in the fields. That seems straight forward. So I'm not
sure why you can't do it that way.

Or if you really want to embed just that somewhere, you could do this...which
really is more or less what the function I mentioned would look like:

righttriangle=  
let(SideA=3,  
SideB=4,  
SideC=sqrt(SideA^2+SideB^2),  
AngleA=asin(SideA/SideC),  
AngleB=asin(SideB/SideC)  
)  
object(  
SideA=SideA,  
SideB=SideB,  
SideC=SideC,  
AngleA=AngleA,  
AngleB=AngleB,  
AngleC=90);

Of course, really the sides and angles should be either arrays or objects too.

On Sat, Aug 30, 2025 at 7:20 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the object is
created, but are unknown prior to calculation.

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Adrian Mariano via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
Sent: Saturday, August 30, 2025 5:48 PM  
To: OpenSCAD general discussion Mailing-list
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
Cc: Adrian Mariano
<[avm4@cornell.edu](mailto:avm4@cornell.edu)[mailto:avm4@cornell.edu](mailto:avm4@cornell.edu)>  
Subject: [OpenSCAD] Re: Functions as Object Members: Recalculation slowing
down compilation

If the function is going to return the same value after objection creation
shouldn't you be creating the object with that member as a variable and
compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
wrote:  
I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)[mailto:discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

The triangle might not have been a great example, it was just the first idea
that popped into my head because it has props calculated from other props,
they wee just hard coded here as an example, I think your let suggestion it
good Nathan Sokalski njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Adrian Mariano via Discuss
<discuss@lists.openscad.org> Sent: Saturday, August 30, 2025 9:45 PM To:
OpenSCAD general discussion Mailing-list <discuss@lists.openscad.org> Cc:
Adrian Mariano <avm4@cornell.edu> Subject: [OpenSCAD] Re: Functions as Object
Members: Recalculation slowing down compilation If this were a function that
made the triangle object you could of course dispense with the let and just
create the object, with sideA and sideB being function parameters. This is why
I noted on the absence of larger context that might clarify what you actually
need. The let is needed to create and hold the values of sideA and sideB,
which have to come from somewhere. If they are already in scope you don't need
a let to make them, but the code fragment you show doesn't really make sense
to me as it stands, because I wouldn't hard code values for the sides into a
structure like that. On Sat, Aug 30, 2025 at 8:51 PM Nathan Sokalski via
Discuss <discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote:
I guess the way you show it does work, so I will probably end up doing it that
way, I guess it felt redundant to me to be assigning values in the let()
statement and then (what feels like) reassigning them in the result. But it
does seem to work and make sense, even if 2X as many lines of code. Thanks!
Nathan Sokalski njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Adrian Mariano via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> Sent:
Saturday, August 30, 2025 7:44 PM To: OpenSCAD general discussion Mailing-list
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> Cc: Adrian
Mariano <avm4@cornell.edu<mailto:avm4@cornell.edu>> Subject: [OpenSCAD] Re:
Functions as Object Members: Recalculation slowing down compilation What's the
larger context here? Are you proposing that you're actually going to make that
object by using the above code as shown? Because I can't see how that's
sensible. It's a lot of complicated stuff to type to create the object. If the
object is actually made by a function, the function precomputes everything and
fills in the fields. That seems straight forward. So I'm not sure why you
can't do it that way. Or if you really want to embed just that somewhere, you
could do this...which really is more or less what the function I mentioned
would look like: righttriangle= let(SideA=3, SideB=4,
SideC=sqrt(SideA^2+SideB^2), AngleA=asin(SideA/SideC),
AngleB=asin(SideB/SideC) ) object( SideA=SideA, SideB=SideB, SideC=SideC,
AngleA=AngleA, AngleB=AngleB, AngleC=90); Of course, really the sides and
angles should be either arrays or objects too. On Sat, Aug 30, 2025 at 7:20 PM
Nathan Sokalski via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote: How
would I do something like the following? righttriangle=object( SideA=3,
SideB=4,
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),
AngleC=90); In this object, SideC, AngleA & AngleB will remain the same once
the object is created, but are unknown prior to calculation. Nathan Sokalski
njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Adrian Mariano via Discuss
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> Sent:
Saturday, August 30, 2025 5:48 PM To: OpenSCAD general discussion Mailing-list
<discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> Cc: Adrian
Mariano <avm4@cornell.edu<mailto:avm4@cornell.edu>> Subject: [OpenSCAD] Re:
Functions as Object Members: Recalculation slowing down compilation If the
function is going to return the same value after objection creation shouldn't
you be creating the object with that member as a variable and compute its
value at creation time? On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via
Discuss <discuss@lists.openscad.org<mailto:discuss@lists.openscad.org>> wrote:
I have been working on a new model using the 2025.07.11 prebuild containing
the object() function. Many of my objects contain members that are functions,
even functions that call other members that are also functions. My code seems
to be getting very slow, and (correct me if I am wrong) I was wondering if
this is because so many functions are being called so many times. Most of
these function members will always return the same value once the object is
created (they do not have any parameters, and the equation or operations in
them only use constants). Is there a way to avoid recalculating a function a
large number of times? For example, if a function does nothing other than
return the sum of 2 other constant members, is there a way to assign a value
to the member that is a "calculated constant" instead of a function? Nathan
Sokalski njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
_______________________________________________ OpenSCAD mailing list To
unsubscribe send an email to discuss-leave@lists.openscad.org<mailto:discuss-
leave@lists.openscad.org> _______________________________________________
OpenSCAD mailing list To unsubscribe send an email to discuss-
leave@lists.openscad.org<mailto:discuss-leave@lists.openscad.org>
_______________________________________________ OpenSCAD mailing list To
unsubscribe send an email to discuss-leave@lists.openscad.org<mailto:discuss-
leave@lists.openscad.org>

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Sun, Aug 31, 2025 12:23 PM

Actually Nathan doesn't care about lazy evaluation. He is complaining  
about poor run time. The proposal to use a user written function instead  
of the dot notation to access object members is both ugly and will also  
make runtime worse, since it adds a bunch of overhead to accessing object  
members. Nathan's whole concern was that he was calling too many  
functions, and this just triples the call count. I don't know if function  
calls are the reason for his observed performance issues---would be worth  
getting to the bottom of that---but his requested goal was the opposite of  
lazy evaluation: he wanted eager evaluation to avoid function calls at use  
time.

Also the basic behavior of using a function is already "lazy evaluation".  
That is, if you define a function member and access it as needed that's not  
calculated until you call it. You don't need a special member access  
function to do this. You just need to know if your member is a function or  
not. But since memoization is impossible in a user-space lazy evaluation  
scheme in OpenSCAD, it seems like applications for lazy evaluation are  
limited and generally manageable by simply passing a function literal to  
code that expects a function literal.

On Sat, Aug 30, 2025 at 10:15 PM Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I'm assuming you're trying to do lazy evaluation? My idea:

First, use Python convention of always having "self" as the first argument  
of all functions intended as methods.

Second, don't retrieve values directly. Use this function:

function zed(obj, member) =  
let ( thunk = obj[member] )  
is_function(thunk) ? thunk(obj) : thunk;

member is a string unfortunately.

On August 30, 2025 4:19:58 PM PDT, Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

How would I do something like the following?  
righttriangle=object(  
SideA=3,  
SideB=4,  
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
AngleC=90);  
In this object, SideC, AngleA & AngleB will remain the same once the  
object is created, but are unknown prior to calculation.

## Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

_From:_ Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
_Sent:_ Saturday, August 30, 2025 5:48 PM  
_To:_ OpenSCAD general discussion Mailing-list <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
_Cc:_ Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
_Subject:_ [OpenSCAD] Re: Functions as Object Members: Recalculation  
slowing down compilation

If the function is going to return the same value after objection  
creation shouldn't you be creating the object with that member as a  
variable and compute its value at creation time?

On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

I have been working on a new model using the 2025.07.11 prebuild  
containing the object() function. Many of my objects contain members that  
are functions, even functions that call other members that are also  
functions. My code seems to be getting very slow, and (correct me if I am  
wrong) I was wondering if this is because so many functions are being  
called so many times. Most of these function members will always return the  
same value once the object is created (they do not have any parameters, and  
the equation or operations in them only use constants). Is there a way to  
avoid recalculating a function a large number of times? For example, if a  
function does nothing other than return the sum of 2 other constant  
members, is there a way to assign a value to the member that is a  
"calculated constant" instead of a function?

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Actually Nathan doesn't care about lazy evaluation. He is complaining about
poor run time. The proposal to use a user written function instead of the dot
notation to access object members is both ugly and will also make runtime
worse, since it adds a bunch of overhead to accessing object members. Nathan's
whole concern was that he was calling too many functions, and this just
triples the call count. I don't know if function calls are the reason for his
observed performance issues---would be worth getting to the bottom of that---
but his requested goal was the opposite of lazy evaluation: he wanted eager
evaluation to avoid function calls at use time. Also the basic behavior of
using a function is already "lazy evaluation". That is, if you define a
function member and access it as needed that's not calculated until you call
it. You don't need a special member access function to do this. You just need
to know if your member is a function or not. But since memoization is
impossible in a user-space lazy evaluation scheme in OpenSCAD, it seems like
applications for lazy evaluation are limited and generally manageable by
simply passing a function literal to code that expects a function literal. On
Sat, Aug 30, 2025 at 10:15 PM Cory Cross via Discuss <
discuss@lists.openscad.org> wrote: > I'm assuming you're trying to do lazy
evaluation? My idea: > > First, use Python convention of always having "self"
as the first argument > of all functions intended as methods. > > Second,
don't retrieve values directly. Use this function: > > function zed(obj,
member) = > let ( thunk = obj[member] ) > is_function(thunk) ? thunk(obj) :
thunk; > > member is a string unfortunately. > > > > On August 30, 2025
4:19:58 PM PDT, Nathan Sokalski via Discuss < > discuss@lists.openscad.org>
wrote: > >> How would I do something like the following? >>
righttriangle=object( >> SideA=3, >> SideB=4, >>
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))), >>
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())), >>
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())), >>
AngleC=90); >> In this object, SideC, AngleA & AngleB will remain the same
once the >> object is created, but are unknown prior to calculation. >> >>
Nathan Sokalski >> njsokalski@hotmail.com >> \------------------------------
>> *From:* Adrian Mariano via Discuss <discuss@lists.openscad.org> >> *Sent:*
Saturday, August 30, 2025 5:48 PM >> *To:* OpenSCAD general discussion
Mailing-list < >> discuss@lists.openscad.org> >> *Cc:* Adrian Mariano
<avm4@cornell.edu> >> *Subject:* [OpenSCAD] Re: Functions as Object Members:
Recalculation >> slowing down compilation >> >> If the function is going to
return the same value after objection >> creation shouldn't you be creating
the object with that member as a >> variable and compute its value at creation
time? >> >> On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss < >>
discuss@lists.openscad.org> wrote: >> >> I have been working on a new model
using the 2025.07.11 prebuild >> containing the object() function. Many of my
objects contain members that >> are functions, even functions that call other
members that are also >> functions. My code seems to be getting very slow, and
(correct me if I am >> wrong) I was wondering if this is because so many
functions are being >> called so many times. Most of these function members
will always return the >> same value once the object is created (they do not
have any parameters, and >> the equation or operations in them only use
constants). Is there a way to >> avoid recalculating a function a large number
of times? For example, if a >> function does nothing other than return the sum
of 2 other constant >> members, is there a way to assign a value to the member
that is a >> "calculated constant" instead of a function? >> >> Nathan
Sokalski >> njsokalski@hotmail.com >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org >> >>
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sun, Aug 31, 2025 3:49 PM

I figured you would reply with the answer you did, so with the limited
information available, I thought I would cover the case where there are many
values to create, only a small subset will be used for any given instance, and
they are expensive to calculate.

If we're assuming this is the actual use, then side and angle should be arrays
:) and let or function args are the best.

On August 31, 2025 5:23:10 AM PDT, Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

Also the basic behavior of using a function is already "lazy evaluation".  
That is, if you define a function member and access it as needed that's not  
calculated until you call it.

Yes, but I figured you would be giving the answer to calculate all fields and
assign as values into the object. So I offered the alternative where the
calculation is expensive but often unnecessary (though I didn't say that).

And, of course, it's not _actually_ lazy evaluation.

So I'd prefer

function ra(sideA, sideB) =  
object(sides=[sideA,sideB,sqrt(sideA^2+sideB^2)], angles=[...]);

which form supports all polygons.

  * Cory

You don't need a special member access

____

function to do this. You just need to know if your member is a function or  
not. But since memoization is impossible in a user-space lazy evaluation  
scheme in OpenSCAD, it seems like applications for lazy evaluation are  
limited and generally manageable by simply passing a function literal to  
code that expects a function literal.

On Sat, Aug 30, 2025 at 10:15 PM Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

> I'm assuming you're trying to do lazy evaluation? My idea:
>
> First, use Python convention of always having "self" as the first argument  
> of all functions intended as methods.
>
> Second, don't retrieve values directly. Use this function:
>
> function zed(obj, member) =  
> let ( thunk = obj[member] )  
> is_function(thunk) ? thunk(obj) : thunk;
>
> member is a string unfortunately.
>
> On August 30, 2025 4:19:58 PM PDT, Nathan Sokalski via Discuss <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:
>

>> How would I do something like the following?  
> righttriangle=object(  
> SideA=3,  
> SideB=4,  
> SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))),  
> AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())),  
> AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())),  
> AngleC=90);  
> In this object, SideC, AngleA & AngleB will remain the same once the  
> object is created, but are unknown prior to calculation.
>>

>> ## Nathan Sokalski  
> [njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)
>>

>> _From:_ Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
> _Sent:_ Saturday, August 30, 2025 5:48 PM  
> _To:_ OpenSCAD general discussion Mailing-list <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>  
> _Cc:_ Adrian Mariano [avm4@cornell.edu](mailto:avm4@cornell.edu)  
> _Subject:_ [OpenSCAD] Re: Functions as Object Members: Recalculation  
> slowing down compilation
>>

>> If the function is going to return the same value after objection  
> creation shouldn't you be creating the object with that member as a  
> variable and compute its value at creation time?
>>

>> On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via Discuss <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:
>>

>> I have been working on a new model using the 2025.07.11 prebuild  
> containing the object() function. Many of my objects contain members that  
> are functions, even functions that call other members that are also  
> functions. My code seems to be getting very slow, and (correct me if I am  
> wrong) I was wondering if this is because so many functions are being  
> called so many times. Most of these function members will always return the  
> same value once the object is created (they do not have any parameters, and  
> the equation or operations in them only use constants). Is there a way to  
> avoid recalculating a function a large number of times? For example, if a  
> function does nothing other than return the sum of 2 other constant  
> members, is there a way to assign a value to the member that is a  
> "calculated constant" instead of a function?
>>

>> Nathan Sokalski  
> [njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)
>>

>> * * *

>>

>> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
>>

>> * * *

>
> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I figured you would reply with the answer you did, so with the limited
information available, I thought I would cover the case where there are many
values to create, only a small subset will be used for any given instance, and
they are expensive to calculate. If we're assuming this is the actual use,
then side and angle should be arrays :) and let or function args are the best.
On August 31, 2025 5:23:10 AM PDT, Adrian Mariano via Discuss
<discuss@lists.openscad.org> wrote: >Also the basic behavior of using a
function is already "lazy evaluation". >That is, if you define a function
member and access it as needed that's not >calculated until you call it. Yes,
but I figured you would be giving the answer to calculate all fields and
assign as values into the object. So I offered the alternative where the
calculation is expensive but often unnecessary (though I didn't say that).
And, of course, it's not *actually* lazy evaluation. So I'd prefer function
ra(sideA, sideB) = object(sides=[sideA,sideB,sqrt(sideA^2+sideB^2)],
angles=[...]); which form supports all polygons. \- Cory You don't need a
special member access >function to do this. You just need to know if your
member is a function or >not. But since memoization is impossible in a user-
space lazy evaluation >scheme in OpenSCAD, it seems like applications for lazy
evaluation are >limited and generally manageable by simply passing a function
literal to >code that expects a function literal. > >On Sat, Aug 30, 2025 at
10:15 PM Cory Cross via Discuss < >discuss@lists.openscad.org> wrote: > >> I'm
assuming you're trying to do lazy evaluation? My idea: >> >> First, use Python
convention of always having "self" as the first argument >> of all functions
intended as methods. >> >> Second, don't retrieve values directly. Use this
function: >> >> function zed(obj, member) = >> let ( thunk = obj[member] ) >>
is_function(thunk) ? thunk(obj) : thunk; >> >> member is a string
unfortunately. >> >> >> >> On August 30, 2025 4:19:58 PM PDT, Nathan Sokalski
via Discuss < >> discuss@lists.openscad.org> wrote: >> >>> How would I do
something like the following? >>> righttriangle=object( >>> SideA=3, >>>
SideB=4, >>>
SideC=function()(sqrt((righttriangle.SideA^2)+(righttriangle.SideB^2))), >>>
AngleA=function()(asin(righttriangle.SideA/righttriangle.SideC())), >>>
AngleB=function()(asin(righttriangle.SideB/righttriangle.SideC())), >>>
AngleC=90); >>> In this object, SideC, AngleA & AngleB will remain the same
once the >>> object is created, but are unknown prior to calculation. >>> >>>
Nathan Sokalski >>> njsokalski@hotmail.com >>> \------------------------------
>>> *From:* Adrian Mariano via Discuss <discuss@lists.openscad.org> >>>
*Sent:* Saturday, August 30, 2025 5:48 PM >>> *To:* OpenSCAD general
discussion Mailing-list < >>> discuss@lists.openscad.org> >>> *Cc:* Adrian
Mariano <avm4@cornell.edu> >>> *Subject:* [OpenSCAD] Re: Functions as Object
Members: Recalculation >>> slowing down compilation >>> >>> If the function is
going to return the same value after objection >>> creation shouldn't you be
creating the object with that member as a >>> variable and compute its value
at creation time? >>> >>> On Sat, Aug 30, 2025 at 5:43 PM Nathan Sokalski via
Discuss < >>> discuss@lists.openscad.org> wrote: >>> >>> I have been working
on a new model using the 2025.07.11 prebuild >>> containing the object()
function. Many of my objects contain members that >>> are functions, even
functions that call other members that are also >>> functions. My code seems
to be getting very slow, and (correct me if I am >>> wrong) I was wondering if
this is because so many functions are being >>> called so many times. Most of
these function members will always return the >>> same value once the object
is created (they do not have any parameters, and >>> the equation or
operations in them only use constants). Is there a way to >>> avoid
recalculating a function a large number of times? For example, if a >>>
function does nothing other than return the sum of 2 other constant >>>
members, is there a way to assign a value to the member that is a >>>
"calculated constant" instead of a function? >>> >>> Nathan Sokalski >>>
njsokalski@hotmail.com >>> _______________________________________________ >>>
OpenSCAD mailing list >>> To unsubscribe send an email to discuss-
leave@lists.openscad.org >>> >>>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org >>

[Next
page](https://lists.openscad.org/empathy/thread/7NQ73G5AD2IN5ULT6KKUTLOYW7CQ3WTT?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

