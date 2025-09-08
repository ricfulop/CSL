---
url: https://lists.openscad.org/empathy/thread/GD43WUASXZ2N3YGINL23NVMI4QXWNIED
scraped_at: 2025-09-08T16:28:20.781056
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

###  Namespace and `using` now available for evaluation from PR #6131

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 29, 2025 8:08 PM

Hello Everyone,

I believe I have the namespace keyword fully implemented and the using  
keyword working for functions and modules. Singular references (i.e.  
namespace_name::variable) and looking up variables are next. It also  
seems include works inside a namespace, which shouldn't be surprising as  
it just copy-pastes the file contents while parsing, but I haven't  
really thought about this.

I'm not sure if you can download the builds run by the checks, but all  
builds succeeded and the only failing tests are the two I've added for  
not-yet-complete functionality.

<https://github.com/openscad/openscad/pull/6131>

  * Cory Cross

using-demos.scad:

// Break circle  
module circle() {}

$fn=40;

namespace apple {  
function only_in_apple() = "red";  
function what_color() = only_in_apple();  
module worm(ring_d=2) {  
color(what_color())  
rotate_extrude(angle=270)  
translate([ring_d,0,0])  
circle(1);  
}  
}

namespace banana {  
include <b0rk.scad>  
using apple;  
my_color = "green";  
function what_color() = my_color;  
module tall() {  
my_color="black"; // As intended, not used.  
color(what_color()) cylinder(h=5,r=1);  
translate([0,0,2]) worm(2.5);  
if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0);  
}  
}

using banana;  
echo(my_color); // Assignment lookup TBD  
echo(what_color());  
tall(); // Center is green, worm is red.  
echo(only_in_apple()); // Expect unknown function and that's what happens!

b0rk.scad:

b0rk = true;

Hello Everyone, I believe I have the namespace keyword fully implemented and
the using keyword working for functions and modules. Singular references (i.e.
namespace_name::variable) and looking up variables are next. It also seems
include works inside a namespace, which shouldn't be surprising as it just
copy-pastes the file contents while parsing, but I haven't really thought
about this. I'm not sure if you can download the builds run by the checks, but
all builds succeeded and the only failing tests are the two I've added for
not-yet-complete functionality. https://github.com/openscad/openscad/pull/6131
\- Cory Cross using-demos.scad: // Break circle module circle() {} $fn=40;
namespace apple { function only_in_apple() = "red"; function what_color() =
only_in_apple(); module worm(ring_d=2) { color(what_color())
rotate_extrude(angle=270) translate([ring_d,0,0]) circle(1); } } namespace
banana { include <b0rk.scad> using apple; my_color = "green"; function
what_color() = my_color; module tall() { my_color="black"; // As intended, not
used. color(what_color()) cylinder(h=5,r=1); translate([0,0,2]) worm(2.5);
if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0); } } using banana;
echo(my_color); // Assignment lookup TBD echo(what_color()); tall(); // Center
is green, worm is red. echo(only_in_apple()); // Expect unknown function and
that's what happens! b0rk.scad: b0rk = true;

[ ![Attached image](https://lists.openscad.org/empathy/image/679033/200)
](https://lists.openscad.org/empathy/attachment/679033)

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 29, 2025 8:29 PM

I forgot some details about semantics; the long version is in Issue#522  
<https://github.com/openscad/openscad/issues/522>, the short version is:

  1. Namespaces can only be at top level (no nesting).
  2. They are evaluated before evaluating the source file. (So all files   
are read/included, namespaces are evaluated in the order first  
mentioned, then source file starts being evaluated)

     1. This means $special variables in the source file do not affect   
namespace assignments

     2. Builtins are in scope for namespace evaluations
     3. Namespace _assignments_ cannot use values, functions, or modules   
from namespaces first declared after their own; or transitively  
via functions. (This is existing semantics: function x() = x;  
y=x(); x=1; does not work)

     4. Namespace functions and modules can use values, functions, and   
modules from any namespace

     5. Namespace functions and modules are affected by $special   
variables when called and can set them for calling other  
functions and modules.

  3. Namespace names have their own environment and cannot be assigned to   
variables (this could be added later).

  4. namespace can be repeated; it's treated as if you concatenated the   
bodies of all namespace blocks into the first one.

  5. Existing OpenSCAD semantics should apply: repeated variable   
definitions act is if the last one was written at the location of  
the first definition, repeated function/module definition will  
replace the earlier ones.

  6. Namespaces are evaluated in order of their first mention. (namespace   
a{} namespace b{using a; y=x;} namespace a{x=1;} will assign 1 to y)

  7. Namespaces in use<>d files may or may not work. Haven't tried.

  * Cory

On 8/29/25 1:08 PM, Cory Cross via Discuss wrote:

____

Hello Everyone,

I believe I have the namespace keyword fully implemented and the using  
keyword working for functions and modules. Singular references (i.e.  
namespace_name::variable) and looking up variables are next. It also  
seems include works inside a namespace, which shouldn't be surprising  
as it just copy-pastes the file contents while parsing, but I haven't  
really thought about this.

I'm not sure if you can download the builds run by the checks, but all  
builds succeeded and the only failing tests are the two I've added for  
not-yet-complete functionality.

<https://github.com/openscad/openscad/pull/6131>

  * Cory Cross

using-demos.scad:

// Break circle  
module circle() {}

$fn=40;

namespace apple {  
function only_in_apple() = "red";  
function what_color() = only_in_apple();  
module worm(ring_d=2) {  
color(what_color())  
rotate_extrude(angle=270)  
translate([ring_d,0,0])  
circle(1);  
}  
}

namespace banana {  
include <b0rk.scad>  
using apple;  
my_color = "green";  
function what_color() = my_color;  
module tall() {  
my_color="black"; // As intended, not used.  
color(what_color()) cylinder(h=5,r=1);  
translate([0,0,2]) worm(2.5);  
if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0);  
}  
}

using banana;  
echo(my_color); // Assignment lookup TBD  
echo(what_color());  
tall(); // Center is green, worm is red.  
echo(only_in_apple()); // Expect unknown function and that's what happens!

b0rk.scad:

b0rk = true;

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

I forgot some details about semantics; the long version is in Issue#522
<https://github.com/openscad/openscad/issues/522>, the short version is: 1\.
Namespaces can only be at top level (no nesting). 2\. They are evaluated
before evaluating the source file. (So all files are read/included, namespaces
are evaluated in the order first mentioned, then source file starts being
evaluated) 1\. This means $special variables in the source file do not affect
namespace assignments 2\. Builtins are in scope for namespace evaluations 3\.
Namespace _assignments_ cannot use values, functions, or modules from
namespaces first declared after their own; or transitively via functions.
(This is existing semantics: function x() = x; y=x(); x=1; does not work) 4\.
Namespace functions and modules can use values, functions, and modules from
any namespace 5\. Namespace functions and modules are affected by $special
variables when called and can set them for calling other functions and
modules. 3\. Namespace names have their own environment and cannot be assigned
to variables (this could be added later). 4\. namespace can be repeated; it's
treated as if you concatenated the bodies of all namespace blocks into the
first one. 5\. Existing OpenSCAD semantics should apply: repeated variable
definitions act is if the last one was written at the location of the first
definition, repeated function/module definition will replace the earlier ones.
6\. Namespaces are evaluated in order of their first mention. (namespace a{}
namespace b{using a; y=x;} namespace a{x=1;} will assign 1 to y) 7\.
Namespaces in use<>d files may or may not work. Haven't tried. \- Cory On
8/29/25 1:08 PM, Cory Cross via Discuss wrote: > Hello Everyone, > > I believe
I have the namespace keyword fully implemented and the using > keyword working
for functions and modules. Singular references (i.e. >
namespace_name::variable) and looking up variables are next. It also > seems
include works inside a namespace, which shouldn't be surprising > as it just
copy-pastes the file contents while parsing, but I haven't > really thought
about this. > > I'm not sure if you can download the builds run by the checks,
but all > builds succeeded and the only failing tests are the two I've added
for > not-yet-complete functionality. > >
https://github.com/openscad/openscad/pull/6131 > > \- Cory Cross > > using-
demos.scad: > > // Break circle > module circle() {} > > $fn=40; > > namespace
apple { > function only_in_apple() = "red"; > function what_color() =
only_in_apple(); > module worm(ring_d=2) { > color(what_color()) >
rotate_extrude(angle=270) > translate([ring_d,0,0]) > circle(1); > } > } > >
namespace banana { > include <b0rk.scad> > using apple; > my_color = "green";
> function what_color() = my_color; > module tall() { > my_color="black"; //
As intended, not used. > color(what_color()) cylinder(h=5,r=1); >
translate([0,0,2]) worm(2.5); > if(b0rk) translate([0,0,5])
cylinder(h=2,r1=1,r2=0); > } > } > > using banana; > echo(my_color); //
Assignment lookup TBD > echo(what_color()); > tall(); // Center is green, worm
is red. > echo(only_in_apple()); // Expect unknown function and that's what
happens! > > b0rk.scad: > > b0rk = true; > > > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/679036/200)
](https://lists.openscad.org/empathy/attachment/679036)

![](https://www.gravatar.com/avatar/4ae585652404eee099c2b2e079e0c817?d=blank&s=100)

BC

Bob Carlson

Fri, Aug 29, 2025 11:15 PM

Am I missing something? The place I think of namespaces being useful is for
defining libraries. I don’t see how this syntax is practical for a library as
large as BOSL2 or NopHead’s.

-Bob

____

On Aug 29, 2025, at 13:29, Cory Cross via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

I forgot some details about semantics; the long version is in Issue#522
<https://github.com/openscad/openscad/issues/522>, the short version is:

Namespaces can only be at top level (no nesting).  
They are evaluated before evaluating the source file. (So all files are
read/included, namespaces are evaluated in the order first mentioned, then
source file starts being evaluated)  
This means $special variables in the source file do not affect namespace
assignments  
Builtins are in scope for namespace evaluations  
Namespace assignments cannot use values, functions, or modules from namespaces
first declared after their own; or transitively via functions. (This is
existing semantics: function x() = x; y=x(); x=1; does not work)  
Namespace functions and modules can use values, functions, and modules from
any namespace  
Namespace functions and modules are affected by $special variables when called
and can set them for calling other functions and modules.  
Namespace names have their own environment and cannot be assigned to variables
(this could be added later).  
namespace can be repeated; it's treated as if you concatenated the bodies of
all namespace blocks into the first one.  
Existing OpenSCAD semantics should apply: repeated variable definitions act is
if the last one was written at the location of the first definition, repeated
function/module definition will replace the earlier ones.  
Namespaces are evaluated in order of their first mention. (namespace a{}
namespace b{using a; y=x;} namespace a{x=1;} will assign 1 to y)  
Namespaces in use<>d files may or may not work. Haven't tried.

  * Cory

On 8/29/25 1:08 PM, Cory Cross via Discuss wrote:

____

Hello Everyone,

I believe I have the namespace keyword fully implemented and the using keyword
working for functions and modules. Singular references (i.e.
namespace_name::variable) and looking up variables are next. It also seems
include works inside a namespace, which shouldn't be surprising as it just
copy-pastes the file contents while parsing, but I haven't really thought
about this.

I'm not sure if you can download the builds run by the checks, but all builds
succeeded and the only failing tests are the two I've added for not-yet-
complete functionality.

<https://github.com/openscad/openscad/pull/6131>

  * Cory Cross

using-demos.scad:

// Break circle  
module circle() {}

$fn=40;

namespace apple {  
function only_in_apple() = "red";  
function what_color() = only_in_apple();  
module worm(ring_d=2) {  
color(what_color())  
rotate_extrude(angle=270)  
translate([ring_d,0,0])  
circle(1);  
}  
}

namespace banana {  
include <b0rk.scad>  
using apple;  
my_color = "green";  
function what_color() = my_color;  
module tall() {  
my_color="black"; // As intended, not used.  
color(what_color()) cylinder(h=5,r=1);  
translate([0,0,2]) worm(2.5);  
if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0);  
}  
}

using banana;  
echo(my_color); // Assignment lookup TBD  
echo(what_color());  
tall(); // Center is green, worm is red.  
echo(only_in_apple()); // Expect unknown function and that's what happens!

b0rk.scad:

b0rk = true;

<using-demos.png>

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
[mailto:discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Am I missing something? The place I think of namespaces being useful is for
defining libraries. I don’t see how this syntax is practical for a library as
large as BOSL2 or NopHead’s. -Bob > On Aug 29, 2025, at 13:29, Cory Cross via
Discuss <discuss@lists.openscad.org> wrote: > > I forgot some details about
semantics; the long version is in Issue#522
<https://github.com/openscad/openscad/issues/522>, the short version is: > >
Namespaces can only be at top level (no nesting). > They are evaluated before
evaluating the source file. (So all files are read/included, namespaces are
evaluated in the order first mentioned, then source file starts being
evaluated) > This means $special variables in the source file do not affect
namespace assignments > Builtins are in scope for namespace evaluations >
Namespace assignments cannot use values, functions, or modules from namespaces
first declared after their own; or transitively via functions. (This is
existing semantics: function x() = x; y=x(); x=1; does not work) > Namespace
functions and modules can use values, functions, and modules from any
namespace > Namespace functions and modules are affected by $special variables
when called and can set them for calling other functions and modules. >
Namespace names have their own environment and cannot be assigned to variables
(this could be added later). > namespace can be repeated; it's treated as if
you concatenated the bodies of all namespace blocks into the first one. >
Existing OpenSCAD semantics should apply: repeated variable definitions act is
if the last one was written at the location of the first definition, repeated
function/module definition will replace the earlier ones. > Namespaces are
evaluated in order of their first mention. (namespace a{} namespace b{using a;
y=x;} namespace a{x=1;} will assign 1 to y) > Namespaces in use<>d files may
or may not work. Haven't tried. > \- Cory > > On 8/29/25 1:08 PM, Cory Cross
via Discuss wrote: >> Hello Everyone, >> >> I believe I have the namespace
keyword fully implemented and the using keyword working for functions and
modules. Singular references (i.e. namespace_name::variable) and looking up
variables are next. It also seems include works inside a namespace, which
shouldn't be surprising as it just copy-pastes the file contents while
parsing, but I haven't really thought about this. >> >> I'm not sure if you
can download the builds run by the checks, but all builds succeeded and the
only failing tests are the two I've added for not-yet-complete functionality.
>> >> https://github.com/openscad/openscad/pull/6131 >> >> \- Cory Cross >> >>
using-demos.scad: >> >> // Break circle >> module circle() {} >> >> $fn=40; >>
>> namespace apple { >> function only_in_apple() = "red"; >> function
what_color() = only_in_apple(); >> module worm(ring_d=2) { >>
color(what_color()) >> rotate_extrude(angle=270) >> translate([ring_d,0,0]) >>
circle(1); >> } >> } >> >> namespace banana { >> include <b0rk.scad> >> using
apple; >> my_color = "green"; >> function what_color() = my_color; >> module
tall() { >> my_color="black"; // As intended, not used. >> color(what_color())
cylinder(h=5,r=1); >> translate([0,0,2]) worm(2.5); >> if(b0rk)
translate([0,0,5]) cylinder(h=2,r1=1,r2=0); >> } >> } >> >> using banana; >>
echo(my_color); // Assignment lookup TBD >> echo(what_color()); >> tall(); //
Center is green, worm is red. >> echo(only_in_apple()); // Expect unknown
function and that's what happens! >> >> b0rk.scad: >> >> b0rk = true; >> >>
<using-demos.png> >> >> >> >> _______________________________________________
>> OpenSCAD mailing list >> To unsubscribe send an email to discuss-
leave@lists.openscad.org <mailto:discuss-leave@lists.openscad.org> >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sat, Aug 30, 2025 1:25 AM

On 8/29/25 4:15 PM, Bob Carlson via Discuss wrote:

____

Am I missing something? The place I think of namespaces being useful  
is for defining libraries. I don’t see how this syntax is practical  
for a library as large as BOSL2 or NopHead’s.

I think you missed my email sent 27 August @ 14:53 Pacific.

With this syntax, most of bosl2 could be put in one namespace with 3 lines:

namespace bosl2 {  
include <BOSL2/std.scad>  
}

Now, as I wrote in the other message, I think per-file namespaces make  
more sense and I outline exactly why adding the namespace keyword is  
less work and a better result than abusing object().

  * Cory

____

-Bob

____

On Aug 29, 2025, at 13:29, Cory Cross via Discuss  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

I forgot some details about semantics; the long version is in  
Issue#522 <https://github.com/openscad/openscad/issues/522>, the  
short version is:

  1. Namespaces can only be at top level (no nesting).
  2. They are evaluated before evaluating the source file. (So all   
files are read/included, namespaces are evaluated in the order  
first mentioned, then source file starts being evaluated)

     1. This means $special variables in the source file do not   
affect namespace assignments

     2. Builtins are in scope for namespace evaluations
     3. Namespace _assignments_ cannot use values, functions, or   
modules from namespaces first declared after their own; or  
transitively via functions. (This is existing semantics:  
function x() = x; y=x(); x=1; does not work)

     4. Namespace functions and modules can use values, functions,   
and modules from any namespace

     5. Namespace functions and modules are affected by $special   
variables when called and can set them for calling other  
functions and modules.

  3. Namespace names have their own environment and cannot be assigned   
to variables (this could be added later).

  4. namespace can be repeated; it's treated as if you concatenated   
the bodies of all namespace blocks into the first one.

  5. Existing OpenSCAD semantics should apply: repeated variable   
definitions act is if the last one was written at the location of  
the first definition, repeated function/module definition will  
replace the earlier ones.

  6. Namespaces are evaluated in order of their first mention.   
(namespace a{} namespace b{using a; y=x;} namespace a{x=1;} will  
assign 1 to y)

  7. Namespaces in use<>d files may or may not work. Haven't tried.

  * Cory

On 8/29/25 1:08 PM, Cory Cross via Discuss wrote:

____

Hello Everyone,

I believe I have the namespace keyword fully implemented and the  
using keyword working for functions and modules. Singular references  
(i.e. namespace_name::variable) and looking up variables are next.  
It also seems include works inside a namespace, which shouldn't be  
surprising as it just copy-pastes the file contents while parsing,  
but I haven't really thought about this.

I'm not sure if you can download the builds run by the checks, but  
all builds succeeded and the only failing tests are the two I've  
added for not-yet-complete functionality.

<https://github.com/openscad/openscad/pull/6131>

  * Cory Cross

using-demos.scad:

// Break circle  
module circle() {}

$fn=40;

namespace apple {  
function only_in_apple() = "red";  
function what_color() = only_in_apple();  
module worm(ring_d=2) {  
color(what_color())  
rotate_extrude(angle=270)  
translate([ring_d,0,0])  
circle(1);  
}  
}

namespace banana {  
include <b0rk.scad>  
using apple;  
my_color = "green";  
function what_color() = my_color;  
module tall() {  
my_color="black"; // As intended, not used.  
color(what_color()) cylinder(h=5,r=1);  
translate([0,0,2]) worm(2.5);  
if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0);  
}  
}

using banana;  
echo(my_color); // Assignment lookup TBD  
echo(what_color());  
tall(); // Center is green, worm is red.  
echo(only_in_apple()); // Expect unknown function and that's what  
happens!

b0rk.scad:

b0rk = true;

<using-demos.png>

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

On 8/29/25 4:15 PM, Bob Carlson via Discuss wrote: > Am I missing something?
The place I think of namespaces being useful > is for defining libraries. I
don’t see how this syntax is practical > for a library as large as BOSL2 or
NopHead’s. I think you missed my email sent 27 August @ 14:53 Pacific. With
this syntax, most of bosl2 could be put in one namespace with 3 lines:
namespace bosl2 { include <BOSL2/std.scad> } Now, as I wrote in the other
message, I think per-file namespaces make more sense and I outline exactly why
adding the namespace keyword is less work and a better result than abusing
object(). \- Cory > > -Bob > >> On Aug 29, 2025, at 13:29, Cory Cross via
Discuss >> <discuss@lists.openscad.org> wrote: >> >> I forgot some details
about semantics; the long version is in >> Issue#522
<https://github.com/openscad/openscad/issues/522>, the >> short version is: >>
>> 1\. Namespaces can only be at top level (no nesting). >> 2\. They are
evaluated before evaluating the source file. (So all >> files are
read/included, namespaces are evaluated in the order >> first mentioned, then
source file starts being evaluated) >> 1\. This means $special variables in
the source file do not >> affect namespace assignments >> 2\. Builtins are in
scope for namespace evaluations >> 3\. Namespace _assignments_ cannot use
values, functions, or >> modules from namespaces first declared after their
own; or >> transitively via functions. (This is existing semantics: >>
function x() = x; y=x(); x=1; does not work) >> 4\. Namespace functions and
modules can use values, functions, >> and modules from any namespace >> 5\.
Namespace functions and modules are affected by $special >> variables when
called and can set them for calling other >> functions and modules. >> 3\.
Namespace names have their own environment and cannot be assigned >> to
variables (this could be added later). >> 4\. namespace can be repeated; it's
treated as if you concatenated >> the bodies of all namespace blocks into the
first one. >> 5\. Existing OpenSCAD semantics should apply: repeated variable
>> definitions act is if the last one was written at the location of >> the
first definition, repeated function/module definition will >> replace the
earlier ones. >> 6\. Namespaces are evaluated in order of their first mention.
>> (namespace a{} namespace b{using a; y=x;} namespace a{x=1;} will >> assign
1 to y) >> 7\. Namespaces in use<>d files may or may not work. Haven't tried.
>> >> \- Cory >> >> On 8/29/25 1:08 PM, Cory Cross via Discuss wrote: >>>
Hello Everyone, >>> >>> I believe I have the namespace keyword fully
implemented and the >>> using keyword working for functions and modules.
Singular references >>> (i.e. namespace_name::variable) and looking up
variables are next. >>> It also seems include works inside a namespace, which
shouldn't be >>> surprising as it just copy-pastes the file contents while
parsing, >>> but I haven't really thought about this. >>> >>> I'm not sure if
you can download the builds run by the checks, but >>> all builds succeeded
and the only failing tests are the two I've >>> added for not-yet-complete
functionality. >>> >>> https://github.com/openscad/openscad/pull/6131 >>> >>>
\- Cory Cross >>> >>> using-demos.scad: >>> >>> // Break circle >>> module
circle() {} >>> >>> $fn=40; >>> >>> namespace apple { >>> function
only_in_apple() = "red"; >>> function what_color() = only_in_apple(); >>>
module worm(ring_d=2) { >>> color(what_color()) >>> rotate_extrude(angle=270)
>>> translate([ring_d,0,0]) >>> circle(1); >>> } >>> } >>> >>> namespace
banana { >>> include <b0rk.scad> >>> using apple; >>> my_color = "green"; >>>
function what_color() = my_color; >>> module tall() { >>> my_color="black"; //
As intended, not used. >>> color(what_color()) cylinder(h=5,r=1); >>>
translate([0,0,2]) worm(2.5); >>> if(b0rk) translate([0,0,5])
cylinder(h=2,r1=1,r2=0); >>> } >>> } >>> >>> using banana; >>> echo(my_color);
// Assignment lookup TBD >>> echo(what_color()); >>> tall(); // Center is
green, worm is red. >>> echo(only_in_apple()); // Expect unknown function and
that's what >>> happens! >>> >>> b0rk.scad: >>> >>> b0rk = true; >>> >>>
<using-demos.png> >>> >>> >>> _______________________________________________
>>> OpenSCAD mailing list >>> To unsubscribe send an email todiscuss-
leave@lists.openscad.org >> >> _______________________________________________
>> OpenSCAD mailing list >> To unsubscribe send an email to discuss-
leave@lists.openscad.org > > > _______________________________________________
> OpenSCAD mailing list > To unsubscribe send an email todiscuss-
leave@lists.openscad.org

![](https://www.gravatar.com/avatar/798098a6fc43352d853354f54544ef33?d=blank&s=100)

LM

Leonard Martin Struttmann

Sat, Aug 30, 2025 1:49 AM

So, if I did that:

namespace bosl2 {  
include <BOSL2/std.scad>  
}

...could I then define my own cuboid() module which would then be  
distinct from bosl2's cuboid()?

How, then, would I call each one?

Len

On Fri, Aug 29, 2025 at 8:25 PM Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

On 8/29/25 4:15 PM, Bob Carlson via Discuss wrote:

Am I missing something? The place I think of namespaces being useful is  
for defining libraries. I don’t see how this syntax is practical for a  
library as large as BOSL2 or NopHead’s.

I think you missed my email sent 27 August @ 14:53 Pacific.

With this syntax, most of bosl2 could be put in one namespace with 3 lines:

namespace bosl2 {  
include <BOSL2/std.scad>  
}

Now, as I wrote in the other message, I think per-file namespaces make  
more sense and I outline exactly why adding the namespace keyword is less  
work and a better result than abusing object().

  * Cory

-Bob

On Aug 29, 2025, at 13:29, Cory Cross via Discuss  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

I forgot some details about semantics; the long version is in Issue#522  
<https://github.com/openscad/openscad/issues/522>, the short version is:

    
    
    1. Namespaces can only be at top level (no nesting).
    2. They are evaluated before evaluating the source file. (So all files
    are read/included, namespaces are evaluated in the order first mentioned,
    then source file starts being evaluated)
       1. This means $special variables in the source file do not affect
       namespace assignments
       2. Builtins are in scope for namespace evaluations
       3. Namespace *assignments* cannot use values, functions, or modules
       from namespaces first declared after their own; or transitively via
       functions. (This is existing semantics: function x() = x; y=x(); x=1; does
       not work)
       4. Namespace functions and modules can use values, functions, and
       modules from any namespace
       5. Namespace functions and modules are affected by $special
       variables when called and can set them for calling other functions and
       modules.
       3. Namespace names have their own environment and cannot be
    assigned to variables (this could be added later).
    4. namespace can be repeated; it's treated as if you concatenated the
    bodies of all namespace blocks into the first one.
    5. Existing OpenSCAD semantics should apply: repeated variable
    definitions act is if the last one was written at the location of the first
    definition, repeated function/module definition will replace the earlier
    ones.
    6. Namespaces are evaluated in order of their first mention.
    (namespace a{} namespace b{using a; y=x;} namespace a{x=1;} will assign 1
    to y)
    7. Namespaces in use<>d files may or may not work. Haven't tried.
    

  * Cory

On 8/29/25 1:08 PM, Cory Cross via Discuss wrote:

Hello Everyone,

I believe I have the namespace keyword fully implemented and the using  
keyword working for functions and modules. Singular references (i.e.  
namespace_name::variable) and looking up variables are next. It also  
seems include works inside a namespace, which shouldn't be surprising as  
it just copy-pastes the file contents while parsing, but I haven't really  
thought about this.

I'm not sure if you can download the builds run by the checks, but all  
builds succeeded and the only failing tests are the two I've added for  
not-yet-complete functionality.

<https://github.com/openscad/openscad/pull/6131>

  * Cory Cross

using-demos.scad:

// Break circle  
module circle() {}

$fn=40;

namespace apple {  
function only_in_apple() = "red";  
function what_color() = only_in_apple();  
module worm(ring_d=2) {  
color(what_color())  
rotate_extrude(angle=270)  
translate([ring_d,0,0])  
circle(1);  
}  
}

namespace banana {  
include <b0rk.scad>  
using apple;  
my_color = "green";  
function what_color() = my_color;  
module tall() {  
my_color="black"; // As intended, not used.  
color(what_color()) cylinder(h=5,r=1);  
translate([0,0,2]) worm(2.5);  
if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0);  
}  
}

using banana;  
echo(my_color); // Assignment lookup TBD  
echo(what_color());  
tall(); // Center is green, worm is red.  
echo(only_in_apple()); // Expect unknown function and that's what happens!

b0rk.scad:

b0rk = true;

<using-demos.png>

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

So, if I did that: namespace bosl2 { include <BOSL2/std.scad> } ...could I
then define my own cuboid() module which would then be distinct from bosl2's
cuboid()? How, then, would I call each one? Len On Fri, Aug 29, 2025 at 8:25
PM Cory Cross via Discuss < discuss@lists.openscad.org> wrote: > On 8/29/25
4:15 PM, Bob Carlson via Discuss wrote: > > Am I missing something? The place
I think of namespaces being useful is > for defining libraries. I don’t see
how this syntax is practical for a > library as large as BOSL2 or NopHead’s. >
> > I think you missed my email sent 27 August @ 14:53 Pacific. > > With this
syntax, most of bosl2 could be put in one namespace with 3 lines: > >
namespace bosl2 { > include <BOSL2/std.scad> > } > > Now, as I wrote in the
other message, I think per-file namespaces make > more sense and I outline
exactly why adding the namespace keyword is less > work and a better result
than abusing object(). > > \- Cory > > > -Bob > > On Aug 29, 2025, at 13:29,
Cory Cross via Discuss > <discuss@lists.openscad.org>
<discuss@lists.openscad.org> wrote: > > I forgot some details about semantics;
the long version is in Issue#522 >
<https://github.com/openscad/openscad/issues/522>, the short version is: > > >
1\. Namespaces can only be at top level (no nesting). > 2\. They are evaluated
before evaluating the source file. (So all files > are read/included,
namespaces are evaluated in the order first mentioned, > then source file
starts being evaluated) > 1\. This means $special variables in the source file
do not affect > namespace assignments > 2\. Builtins are in scope for
namespace evaluations > 3\. Namespace *assignments* cannot use values,
functions, or modules > from namespaces first declared after their own; or
transitively via > functions. (This is existing semantics: function x() = x;
y=x(); x=1; does > not work) > 4\. Namespace functions and modules can use
values, functions, and > modules from any namespace > 5\. Namespace functions
and modules are affected by $special > variables when called and can set them
for calling other functions and > modules. > 3\. Namespace names have their
own environment and cannot be > assigned to variables (this could be added
later). > 4\. namespace can be repeated; it's treated as if you concatenated
the > bodies of all namespace blocks into the first one. > 5\. Existing
OpenSCAD semantics should apply: repeated variable > definitions act is if the
last one was written at the location of the first > definition, repeated
function/module definition will replace the earlier > ones. > 6\. Namespaces
are evaluated in order of their first mention. > (namespace a{} namespace
b{using a; y=x;} namespace a{x=1;} will assign 1 > to y) > 7\. Namespaces in
use<>d files may or may not work. Haven't tried. > > \- Cory > > On 8/29/25
1:08 PM, Cory Cross via Discuss wrote: > > Hello Everyone, > > I believe I
have the namespace keyword fully implemented and the using > keyword working
for functions and modules. Singular references (i.e. >
namespace_name::variable) and looking up variables are next. It also > seems
include works inside a namespace, which shouldn't be surprising as > it just
copy-pastes the file contents while parsing, but I haven't really > thought
about this. > > I'm not sure if you can download the builds run by the checks,
but all > builds succeeded and the only failing tests are the two I've added
for > not-yet-complete functionality. > >
https://github.com/openscad/openscad/pull/6131 > > \- Cory Cross > > using-
demos.scad: > > // Break circle > module circle() {} > > $fn=40; > > namespace
apple { > function only_in_apple() = "red"; > function what_color() =
only_in_apple(); > module worm(ring_d=2) { > color(what_color()) >
rotate_extrude(angle=270) > translate([ring_d,0,0]) > circle(1); > } > } > >
namespace banana { > include <b0rk.scad> > using apple; > my_color = "green";
> function what_color() = my_color; > module tall() { > my_color="black"; //
As intended, not used. > color(what_color()) cylinder(h=5,r=1); >
translate([0,0,2]) worm(2.5); > if(b0rk) translate([0,0,5])
cylinder(h=2,r1=1,r2=0); > } > } > > using banana; > echo(my_color); //
Assignment lookup TBD > echo(what_color()); > tall(); // Center is green, worm
is red. > echo(only_in_apple()); // Expect unknown function and that's what
happens! > > b0rk.scad: > > b0rk = true; > > <using-demos.png> > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sat, Aug 30, 2025 2:39 AM

On 8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote:

____

So, if I did that:

namespace bosl2 {  
include <BOSL2/std.scad>  
}

...could I then define my own cuboid() module which would then be  
distinct from bosl2's cuboid()?

Yes.

____

How, then, would I call each one?

You _will_ be able to:

myfile.scad:  
namespace bosl2 {  
include <BOSL2/std.scad>  
}  
module cuboid(arg0, arg1, etc) { // This is yours  
cube(arg0); // Your implementation here  
}  
module compare_cuboids() {  
difference() {  
cuboid(1); // Your cuboid  
bosl2::cuboid(1); // Bosl2 cuboid  
}  
}

I say "will" because I will be implementing "bosl2::cuboid" syntax in  
the next few days.

  * Cory

____

Len

On Fri, Aug 29, 2025 at 8:25 PM Cory Cross via Discuss  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

    
    
     On 8/29/25 4:15 PM, Bob Carlson via Discuss wrote:
    

____

    
    
    Am I missing something? The place I think of namespaces being
     useful is for defining libraries. I don’t see how this syntax is
     practical for a library as large as BOSL2 or NopHead’s.
    
    
     I think you missed my email sent 27 August @ 14:53 Pacific.
    
     With this syntax, most of bosl2 could be put in one namespace with
     3 lines:
    
     namespace bosl2 {
       include <BOSL2/std.scad>
     }
    
     Now, as I wrote in the other message, I think per-file namespaces
     make more sense and I outline exactly why adding the namespace
     keyword is less work and a better result than abusing object().
    
     - Cory
    

____

    
    
    -Bob

____

    
    
    On Aug 29, 2025, at 13:29, Cory Cross via Discuss<discuss@lists.openscad.org> <mailto:discuss@lists.openscad.org>
     wrote:
    
     I forgot some details about semantics; the long version is in
     Issue#522 <https://github.com/openscad/openscad/issues/522>, the
     short version is:
    
      1. Namespaces can only be at top level (no nesting).
      2. They are evaluated before evaluating the source file. (So
         all files are read/included, namespaces are evaluated in the
         order first mentioned, then source file starts being evaluated)
          1. This means $special variables in the source file do not
             affect namespace assignments
          2. Builtins are in scope for namespace evaluations
          3. Namespace _assignments_ cannot use values, functions, or
             modules from namespaces first declared after their own;
             or transitively via functions. (This is existing
             semantics: function x() = x; y=x(); x=1; does not work)
          4. Namespace functions and modules can use values,
             functions, and modules from any namespace
          5. Namespace functions and modules are affected by $special
             variables when called and can set them for calling other
             functions and modules.
      3. Namespace names have their own environment and cannot be
         assigned to variables (this could be added later).
      4. namespace can be repeated; it's treated as if you
         concatenated the bodies of all namespace blocks into the
         first one.
      5. Existing OpenSCAD semantics should apply: repeated variable
         definitions act is if the last one was written at the
         location of the first definition, repeated function/module
         definition will replace the earlier ones.
      6. Namespaces are evaluated in order of their first mention.
         (namespace a{} namespace b{using a; y=x;} namespace a{x=1;}
         will assign 1 to y)
      7. Namespaces in use<>d files may or may not work. Haven't tried.
    
     - Cory
    
     On 8/29/25 1:08 PM, Cory Cross via Discuss wrote:
    

____

    
    
    Hello Everyone,
    
     I believe I have the namespace keyword fully implemented and
     the using keyword working for functions and modules. Singular
     references (i.e. namespace_name::variable) and looking up
     variables are next. It also seems include works inside a
     namespace, which shouldn't be surprising as it just copy-pastes
     the file contents while parsing, but I haven't really thought
     about this.
    
     I'm not sure if you can download the builds run by the checks,
     but all builds succeeded and the only failing tests are the two
     I've added for not-yet-complete functionality.
    
     https://github.com/openscad/openscad/pull/6131
    
     - Cory Cross
    
     using-demos.scad:
    
     // Break circle
     module circle() {}
    
     $fn=40;
    
     namespace apple {
       function only_in_apple() = "red";
       function what_color() = only_in_apple();
       module worm(ring_d=2) {
         color(what_color())
           rotate_extrude(angle=270)
             translate([ring_d,0,0])
                 circle(1);
       }
     }
    
     namespace banana {
       include<b0rk.scad>
       using apple;
       my_color = "green";
       function what_color() = my_color;
       module tall() {
         my_color="black"; // As intended, not used.
         color(what_color()) cylinder(h=5,r=1);
         translate([0,0,2]) worm(2.5);
         if(b0rk) translate([0,0,5]) cylinder(h=2,r1=1,r2=0);
       }
     }
    
     using banana;
     echo(my_color); // Assignment lookup TBD
     echo(what_color());
     tall(); // Center is green, worm is red.
     echo(only_in_apple()); // Expect unknown function and that's
     what happens!
    
     b0rk.scad:
    
     b0rk = true;
    
     <using-demos.png>
    
    
     _______________________________________________
     OpenSCAD mailing list
     To unsubscribe send an email todiscuss-leave@lists.openscad.org
    
    
    
     _______________________________________________
     OpenSCAD mailing list
     To unsubscribe send an email to discuss-leave@lists.openscad.org
    
    
    
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

On 8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote: > So, if I
did that: > > namespace bosl2 { > include <BOSL2/std.scad> > } > > ...could I
then define my own cuboid() module which would then be > distinct from bosl2's
cuboid()? Yes. > > How, then, would I call each one? You *will* be able to:
myfile.scad: namespace bosl2 { include <BOSL2/std.scad> } module cuboid(arg0,
arg1, etc) { // This is yours cube(arg0); // Your implementation here } module
compare_cuboids() { difference() { cuboid(1); // Your cuboid bosl2::cuboid(1);
// Bosl2 cuboid } } I say "will" because I will be implementing
"bosl2::cuboid" syntax in the next few days. \- Cory > > Len > > On Fri, Aug
29, 2025 at 8:25 PM Cory Cross via Discuss > <discuss@lists.openscad.org>
wrote: > > On 8/29/25 4:15 PM, Bob Carlson via Discuss wrote: >> Am I missing
something? The place I think of namespaces being >> useful is for defining
libraries. I don’t see how this syntax is >> practical for a library as large
as BOSL2 or NopHead’s. > > I think you missed my email sent 27 August @ 14:53
Pacific. > > With this syntax, most of bosl2 could be put in one namespace
with > 3 lines: > > namespace bosl2 { > include <BOSL2/std.scad> > } > > Now,
as I wrote in the other message, I think per-file namespaces > make more sense
and I outline exactly why adding the namespace > keyword is less work and a
better result than abusing object(). > > \- Cory > >> >> -Bob >> >>> On Aug
29, 2025, at 13:29, Cory Cross via Discuss >>> <discuss@lists.openscad.org>
<mailto:discuss@lists.openscad.org> >>> wrote: >>> >>> I forgot some details
about semantics; the long version is in >>> Issue#522
<https://github.com/openscad/openscad/issues/522>, the >>> short version is:
>>> >>> 1\. Namespaces can only be at top level (no nesting). >>> 2\. They are
evaluated before evaluating the source file. (So >>> all files are
read/included, namespaces are evaluated in the >>> order first mentioned, then
source file starts being evaluated) >>> 1\. This means $special variables in
the source file do not >>> affect namespace assignments >>> 2\. Builtins are
in scope for namespace evaluations >>> 3\. Namespace _assignments_ cannot use
values, functions, or >>> modules from namespaces first declared after their
own; >>> or transitively via functions. (This is existing >>> semantics:
function x() = x; y=x(); x=1; does not work) >>> 4\. Namespace functions and
modules can use values, >>> functions, and modules from any namespace >>> 5\.
Namespace functions and modules are affected by $special >>> variables when
called and can set them for calling other >>> functions and modules. >>> 3\.
Namespace names have their own environment and cannot be >>> assigned to
variables (this could be added later). >>> 4\. namespace can be repeated; it's
treated as if you >>> concatenated the bodies of all namespace blocks into the
>>> first one. >>> 5\. Existing OpenSCAD semantics should apply: repeated
variable >>> definitions act is if the last one was written at the >>>
location of the first definition, repeated function/module >>> definition will
replace the earlier ones. >>> 6\. Namespaces are evaluated in order of their
first mention. >>> (namespace a{} namespace b{using a; y=x;} namespace a{x=1;}
>>> will assign 1 to y) >>> 7\. Namespaces in use<>d files may or may not
work. Haven't tried. >>> >>> \- Cory >>> >>> On 8/29/25 1:08 PM, Cory Cross
via Discuss wrote: >>>> Hello Everyone, >>>> >>>> I believe I have the
namespace keyword fully implemented and >>>> the using keyword working for
functions and modules. Singular >>>> references (i.e.
namespace_name::variable) and looking up >>>> variables are next. It also
seems include works inside a >>>> namespace, which shouldn't be surprising as
it just copy-pastes >>>> the file contents while parsing, but I haven't really
thought >>>> about this. >>>> >>>> I'm not sure if you can download the builds
run by the checks, >>>> but all builds succeeded and the only failing tests
are the two >>>> I've added for not-yet-complete functionality. >>>> >>>>
https://github.com/openscad/openscad/pull/6131 >>>> >>>> \- Cory Cross >>>>
>>>> using-demos.scad: >>>> >>>> // Break circle >>>> module circle() {} >>>>
>>>> $fn=40; >>>> >>>> namespace apple { >>>> function only_in_apple() =
"red"; >>>> function what_color() = only_in_apple(); >>>> module
worm(ring_d=2) { >>>> color(what_color()) >>>> rotate_extrude(angle=270) >>>>
translate([ring_d,0,0]) >>>> circle(1); >>>> } >>>> } >>>> >>>> namespace
banana { >>>> include <b0rk.scad> >>>> using apple; >>>> my_color = "green";
>>>> function what_color() = my_color; >>>> module tall() { >>>>
my_color="black"; // As intended, not used. >>>> color(what_color())
cylinder(h=5,r=1); >>>> translate([0,0,2]) worm(2.5); >>>> if(b0rk)
translate([0,0,5]) cylinder(h=2,r1=1,r2=0); >>>> } >>>> } >>>> >>>> using
banana; >>>> echo(my_color); // Assignment lookup TBD >>>> echo(what_color());
>>>> tall(); // Center is green, worm is red. >>>> echo(only_in_apple()); //
Expect unknown function and that's >>>> what happens! >>>> >>>> b0rk.scad:
>>>> >>>> b0rk = true; >>>> >>>> <using-demos.png> >>>> >>>> >>>>
_______________________________________________ >>>> OpenSCAD mailing list
>>>> To unsubscribe send an email todiscuss-leave@lists.openscad.org >>> >>>
_______________________________________________ >>> OpenSCAD mailing list >>>
To unsubscribe send an email to discuss-leave@lists.openscad.org >> >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email todiscuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Sat, Aug 30, 2025 11:11 AM

Nice!

In my modification to your example, below, Cory, would I need to say  
"bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD would find  
it within BOSL2? That is, does use of the namespace feature then  
require use of the space name thereafter?

namespace bosl2 {  
include <BOSL2/std.scad>  
}  
module compare_cuboids() {  
difference() {  
cuboid(1); // maybe the BOSL2 cuboid?  
bosl2::cuboid(1); // certainly the Bosl2 cuboid  
}  
}

Thanks.

Jon

On 8/29/2025 10:39 PM, Cory Cross via Discuss wrote:

____

On 8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote:

____

So, if I did that:

namespace bosl2 {  
include <BOSL2/std.scad>  
}

...could I then define my own cuboid() module which would then be  
distinct from bosl2's cuboid()?

Yes.

____

How, then, would I call each one?

You _will_ be able to:

myfile.scad:  
namespace bosl2 {  
include <BOSL2/std.scad>  
}  
module cuboid(arg0, arg1, etc) { // This is yours  
cube(arg0); // Your implementation here  
}  
module compare_cuboids() {  
difference() {  
cuboid(1); // Your cuboid  
bosl2::cuboid(1); // Bosl2 cuboid  
}  
}

I say "will" because I will be implementing "bosl2::cuboid" syntax in  
the next few days.

  * Cory

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

Nice! In my modification to your example, below, Cory, would I need to say
"bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD would find it
within BOSL2? That is, does use of the namespace feature then require use of
the space name thereafter? namespace bosl2 { include <BOSL2/std.scad> } module
compare_cuboids() { difference() { cuboid(1); // maybe the BOSL2 cuboid?
bosl2::cuboid(1); // certainly the Bosl2 cuboid } } Thanks. Jon On 8/29/2025
10:39 PM, Cory Cross via Discuss wrote: > On 8/29/25 6:49 PM, Leonard Martin
Struttmann via Discuss wrote: >> So, if I did that: >> >> namespace bosl2 { >>
include <BOSL2/std.scad> >> } >> >> ...could I then define my own cuboid()
module which would then be >> distinct from bosl2's cuboid()? > Yes. >> >>
How, then, would I call each one? > You *will* be able to: > > myfile.scad: >
namespace bosl2 { > include <BOSL2/std.scad> > } > module cuboid(arg0, arg1,
etc) { // This is yours > cube(arg0); // Your implementation here > } > module
compare_cuboids() { > difference() { > cuboid(1); // Your cuboid >
bosl2::cuboid(1); // Bosl2 cuboid > } > } > > I say "will" because I will be
implementing "bosl2::cuboid" syntax in > the next few days. > > \- Cory > \--
This email has been checked for viruses by AVG antivirus software. www.avg.com

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sat, Aug 30, 2025 4:33 PM

If you add the line `using bosl2;` then if you don't define your own cuboid(),
it uses the one from bosl2.

The `using` statement can be inside a module definition, so it only takes
effect inside that single module, or it can be at the top level, so it takes
effect in all your own module definitions.

  * Cory

On August 30, 2025 7:11:15 AM EDT, Jon Bondy via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

Nice!

In my modification to your example, below, Cory, would I need to say
"bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD would find it
within BOSL2? That is, does use of the namespace feature then require use of
the space name thereafter?

namespace bosl2 {  
include <BOSL2/std.scad>  
}  
module compare_cuboids() {  
difference() {  
cuboid(1); // maybe the BOSL2 cuboid?  
bosl2::cuboid(1); // certainly the Bosl2 cuboid  
}  
}

Thanks.

Jon

On 8/29/2025 10:39 PM, Cory Cross via Discuss wrote:

____

On 8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote:

____

So, if I did that:

namespace bosl2 {  
include <BOSL2/std.scad>  
}

...could I then define my own cuboid() module which would then be distinct
from bosl2's cuboid()?

Yes.

____

How, then, would I call each one?

You _will_ be able to:

myfile.scad:  
namespace bosl2 {  
include <BOSL2/std.scad>  
}  
module cuboid(arg0, arg1, etc) { // This is yours  
cube(arg0); // Your implementation here  
}  
module compare_cuboids() {  
difference() {  
cuboid(1); // Your cuboid  
bosl2::cuboid(1); // Bosl2 cuboid  
}  
}

I say "will" because I will be implementing "bosl2::cuboid" syntax in the next
few days.

  * Cory

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

If you add the line `using bosl2;` then if you don't define your own cuboid(),
it uses the one from bosl2. The `using` statement can be inside a module
definition, so it only takes effect inside that single module, or it can be at
the top level, so it takes effect in all your own module definitions. \- Cory
On August 30, 2025 7:11:15 AM EDT, Jon Bondy via Discuss
<discuss@lists.openscad.org> wrote: >Nice! > >In my modification to your
example, below, Cory, would I need to say "bosl2::cuboid()" or could I just
say "cuboid()" and OpenSCAD would find it within BOSL2? That is, does use of
the namespace feature then require use of the space name thereafter? > >
>namespace bosl2 { > include <BOSL2/std.scad> >} >module compare_cuboids() { >
difference() { > cuboid(1); // maybe the BOSL2 cuboid? > bosl2::cuboid(1); //
certainly the Bosl2 cuboid > } >} > > >Thanks. > >Jon > >On 8/29/2025 10:39
PM, Cory Cross via Discuss wrote: >> On 8/29/25 6:49 PM, Leonard Martin
Struttmann via Discuss wrote: >>> So, if I did that: >>> >>> namespace bosl2 {
>>> include <BOSL2/std.scad> >>> } >>> >>> ...could I then define my own
cuboid() module which would then be distinct from bosl2's cuboid()? >> Yes.
>>> >>> How, then, would I call each one? >> You *will* be able to: >> >>
myfile.scad: >> namespace bosl2 { >> include <BOSL2/std.scad> >> } >> module
cuboid(arg0, arg1, etc) { // This is yours >> cube(arg0); // Your
implementation here >> } >> module compare_cuboids() { >> difference() { >>
cuboid(1); // Your cuboid >> bosl2::cuboid(1); // Bosl2 cuboid >> } >> } >> >>
I say "will" because I will be implementing "bosl2::cuboid" syntax in the next
few days. >> >> \- Cory >> > >\-- >This email has been checked for viruses by
AVG antivirus software. >www.avg.com

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Sat, Aug 30, 2025 7:17 PM

Thanks. But once you use the namespace construct, you are committed to  
using bosl2:: within that scope. Correct?

Jon

On 8/30/2025 12:33 PM, Cory Cross via Discuss wrote:

____

If you add the line`using bosl2;` then if you don't define your own  
cuboid(), it uses the one from bosl2.

The `using` statement can be inside a module definition, so it only  
takes effect inside that single module, or it can be at the top level,  
so it takes effect in all your own module definitions.

  * Cory

On August 30, 2025 7:11:15 AM EDT, Jon Bondy via Discuss  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

    
    
     Nice!
    
     In my modification to your example, below, Cory,  would I need to
     say "bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD
     would find it within BOSL2?  That is, does use of the namespace
     feature then require use of the space name thereafter?
    
    
     namespace bosl2 {
       include <BOSL2/std.scad>
     }
     module compare_cuboids() {
       difference() {
         cuboid(1); // maybe the BOSL2 cuboid?
         bosl2::cuboid(1); // certainly the Bosl2 cuboid
       }
     }
    
    
     Thanks.
    
     Jon
    
     On 8/29/2025 10:39 PM, Cory Cross via Discuss wrote:
    

____

    
    
    On 8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote:

____

    
    
    So, if I did that:
    
     namespace bosl2 {
       include<BOSL2/std.scad>
     }
    
     ...could I then define my own cuboid() module which would then
     be distinct from bosl2's cuboid()?
    
    
    
     Yes.
    

____

    
    
    How, then, would I call each one?
    
    
     You *will* be able to:
    
     myfile.scad:
     namespace bosl2 {
       include <BOSL2/std.scad>
     }
     module cuboid(arg0, arg1, etc) { // This is yours
       cube(arg0); // Your implementation here
     }
     module compare_cuboids() {
       difference() {
         cuboid(1); // Your cuboid
         bosl2::cuboid(1); // Bosl2 cuboid
       }
     }
    
     I say "will" because I will be implementing "bosl2::cuboid"
     syntax in the next few days.
    
     - Cory
    
    
    
     <http://www.avg.com/email-signature?utm_medium=email&utm_source=link&utm_campaign=sig-email&utm_content=emailclient>
     	Virus-free.www.avg.com
     <http://www.avg.com/email-signature?utm_medium=email&utm_source=link&utm_campaign=sig-email&utm_content=emailclient>
    
    
     <#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

Thanks. But once you use the namespace construct, you are committed to using
bosl2:: within that scope. Correct? Jon On 8/30/2025 12:33 PM, Cory Cross via
Discuss wrote: > If you add the line `using bosl2;` then if you don't define
your own > cuboid(), it uses the one from bosl2. > > The `using` statement can
be inside a module definition, so it only > takes effect inside that single
module, or it can be at the top level, > so it takes effect in all your own
module definitions. > > \- Cory > > > On August 30, 2025 7:11:15 AM EDT, Jon
Bondy via Discuss > <discuss@lists.openscad.org> wrote: > > Nice! > > In my
modification to your example, below, Cory, would I need to > say
"bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD > would find it
within BOSL2? That is, does use of the namespace > feature then require use of
the space name thereafter? > > > namespace bosl2 { > include <BOSL2/std.scad>
> } > module compare_cuboids() { > difference() { > cuboid(1); // maybe the
BOSL2 cuboid? > bosl2::cuboid(1); // certainly the Bosl2 cuboid > } > } > > >
Thanks. > > Jon > > On 8/29/2025 10:39 PM, Cory Cross via Discuss wrote: >> On
8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote: >>> So, if I did
that: >>> >>> namespace bosl2 { >>> include <BOSL2/std.scad> >>> } >>> >>>
...could I then define my own cuboid() module which would then >>> be distinct
from bosl2's cuboid()? >> Yes. >>> >>> How, then, would I call each one? >>
You *will* be able to: >> >> myfile.scad: >> namespace bosl2 { >> include
<BOSL2/std.scad> >> } >> module cuboid(arg0, arg1, etc) { // This is yours >>
cube(arg0); // Your implementation here >> } >> module compare_cuboids() { >>
difference() { >> cuboid(1); // Your cuboid >> bosl2::cuboid(1); // Bosl2
cuboid >> } >> } >> >> I say "will" because I will be implementing
"bosl2::cuboid" >> syntax in the next few days. >> >> \- Cory >> > >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > Virus-free.www.avg.com >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > > > <#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2> >
> > _______________________________________________ > OpenSCAD mailing list >
To unsubscribe send an email todiscuss-leave@lists.openscad.org \-- This email
has been checked for viruses by AVG antivirus software. www.avg.com

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sun, Aug 31, 2025 2:35 AM

Ah, no, the `using` statement eases that:

namespace bosl2 {...}

module cuboid(){}

module myshape() {  
using bosl2;  
cuboid(); // the bosl2 cuboid  
cyl(); // bosl2 cyl, etc  
}

cuboid(); // your cuboid

On August 30, 2025 12:17:46 PM PDT, Jon Bondy via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

Thanks. But once you use the namespace construct, you are committed to using
bosl2:: within that scope. Correct?

Jon

On 8/30/2025 12:33 PM, Cory Cross via Discuss wrote:

____

If you add the line`using bosl2;` then if you don't define your own cuboid(),
it uses the one from bosl2.

The `using` statement can be inside a module definition, so it only takes
effect inside that single module, or it can be at the top level, so it takes
effect in all your own module definitions.

  * Cory

On August 30, 2025 7:11:15 AM EDT, Jon Bondy via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

    
    
     Nice!
    
     In my modification to your example, below, Cory,  would I need to
     say "bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD
     would find it within BOSL2?  That is, does use of the namespace
     feature then require use of the space name thereafter?
    
    
     namespace bosl2 {
       include <BOSL2/std.scad>
     }
     module compare_cuboids() {
       difference() {
         cuboid(1); // maybe the BOSL2 cuboid?
         bosl2::cuboid(1); // certainly the Bosl2 cuboid
       }
     }
    
    
     Thanks.
    
     Jon
    
     On 8/29/2025 10:39 PM, Cory Cross via Discuss wrote:
    

____

    
    
    On 8/29/25 6:49 PM, Leonard Martin Struttmann via Discuss wrote:

____

    
    
    So, if I did that:
    
     namespace bosl2 {
       include<BOSL2/std.scad>
     }
    
     ...could I then define my own cuboid() module which would then
     be distinct from bosl2's cuboid()?
    
    
    
     Yes.
    

____

    
    
    How, then, would I call each one?
    
    
     You *will* be able to:
    
     myfile.scad:
     namespace bosl2 {
       include <BOSL2/std.scad>
     }
     module cuboid(arg0, arg1, etc) { // This is yours
       cube(arg0); // Your implementation here
     }
     module compare_cuboids() {
       difference() {
         cuboid(1); // Your cuboid
         bosl2::cuboid(1); // Bosl2 cuboid
       }
     }
    
     I say "will" because I will be implementing "bosl2::cuboid"
     syntax in the next few days.
    
     - Cory
    
    
    
     <http://www.avg.com/email-signature?utm_medium=email&utm_source=link&utm_campaign=sig-email&utm_content=emailclient>
     	Virus-free.www.avg.com
     <http://www.avg.com/email-signature?utm_medium=email&utm_source=link&utm_campaign=sig-email&utm_content=emailclient>
    
    
     <#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

Ah, no, the `using` statement eases that: namespace bosl2 {...} module
cuboid(){} module myshape() { using bosl2; cuboid(); // the bosl2 cuboid
cyl(); // bosl2 cyl, etc } cuboid(); // your cuboid On August 30, 2025
12:17:46 PM PDT, Jon Bondy via Discuss <discuss@lists.openscad.org> wrote:
>Thanks. But once you use the namespace construct, you are committed to using
bosl2:: within that scope. Correct? > >Jon > > >On 8/30/2025 12:33 PM, Cory
Cross via Discuss wrote: >> If you add the line `using bosl2;` then if you
don't define your own cuboid(), it uses the one from bosl2. >> >> The `using`
statement can be inside a module definition, so it only takes effect inside
that single module, or it can be at the top level, so it takes effect in all
your own module definitions. >> >> \- Cory >> >> >> On August 30, 2025 7:11:15
AM EDT, Jon Bondy via Discuss <discuss@lists.openscad.org> wrote: >> >> Nice!
>> >> In my modification to your example, below, Cory, would I need to >> say
"bosl2::cuboid()" or could I just say "cuboid()" and OpenSCAD >> would find it
within BOSL2? That is, does use of the namespace >> feature then require use
of the space name thereafter? >> >> >> namespace bosl2 { >> include
<BOSL2/std.scad> >> } >> module compare_cuboids() { >> difference() { >>
cuboid(1); // maybe the BOSL2 cuboid? >> bosl2::cuboid(1); // certainly the
Bosl2 cuboid >> } >> } >> >> >> Thanks. >> >> Jon >> >> On 8/29/2025 10:39 PM,
Cory Cross via Discuss wrote: >>> On 8/29/25 6:49 PM, Leonard Martin
Struttmann via Discuss wrote: >>>> So, if I did that: >>>> >>>> namespace
bosl2 { >>>> include <BOSL2/std.scad> >>>> } >>>> >>>> ...could I then define
my own cuboid() module which would then >>>> be distinct from bosl2's
cuboid()? >>> Yes. >>>> >>>> How, then, would I call each one? >>> You *will*
be able to: >>> >>> myfile.scad: >>> namespace bosl2 { >>> include
<BOSL2/std.scad> >>> } >>> module cuboid(arg0, arg1, etc) { // This is yours
>>> cube(arg0); // Your implementation here >>> } >>> module compare_cuboids()
{ >>> difference() { >>> cuboid(1); // Your cuboid >>> bosl2::cuboid(1); //
Bosl2 cuboid >>> } >>> } >>> >>> I say "will" because I will be implementing
"bosl2::cuboid" >>> syntax in the next few days. >>> >>> \- Cory >>> >> >>
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> >> Virus-free.www.avg.com >>
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> >> >> >>
<#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2> >> >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email todiscuss-leave@lists.openscad.org > >\-- >This
email has been checked for viruses by AVG antivirus software. >www.avg.com

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

