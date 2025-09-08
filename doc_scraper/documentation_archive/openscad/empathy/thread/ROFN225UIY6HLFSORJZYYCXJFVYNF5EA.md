---
url: https://lists.openscad.org/empathy/thread/ROFN225UIY6HLFSORJZYYCXJFVYNF5EA
scraped_at: 2025-09-08T16:28:30.756916
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

###  Modules as functions

![](https://www.gravatar.com/avatar/a11af2fdbb73a5b23029ce3c1a94cade?d=blank&s=100)

PK

Peter Kriens

Fri, Aug 22, 2025 2:41 PM

The OEP8
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is the source for the object() and the $this
saga. I thought this was extensively discussed looking at the discussions in
the PR but I guess the current discussions prove that wrong.

The same PR <https://github.com/openscad/openscad/pull/4478> also contained
`module references`. Something that sounded extremely useful to me since that
would make name scoping of libraries a lot simpler. It would theoretically
allow something like this `bosl2= use <BOSL2/std.scad>` in the future (not
planned).

So this is what is in OEP8.  
module literals / module references

new expression component module (<params>) { <body> } yields module reference.  
module reference is just a value, can put in variable, put in array, pass as
argument, return from function, et cetera.  
call as  
m(args)  
a[i](args)  
o.m(args)  
(expr)(args)  
or combinations, e.g. a[i].m(args) for an array of objects with a member that
is a module reference.  
It will allow code like this.

small = module() cube(10);  
big = module() cube(100);  
(s ? small : big)();  
v = [ small, big];  
v[1]();  
function foo(w) =  
w = "c" ? module() cube(5)  
: w = "s" ? module() sphere(5)  
: undef;

This will enable calling a module from a function which is a pretty big
change. Literal modules are now values and can be used anywhere an expression
can be used. I.e. they can actually render from a function. (I expect this
will give some issues before this works perfectly because ordering between
functions/modules is a bit odd in OpenSCAD.)

When a module is instantiated from an expression, its value will be undef.

Should I work on this?

    
    
    Peter
    

The OEP8
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is the source for the object() and the $this
saga. I thought this was extensively discussed looking at the discussions in
the PR but I guess the current discussions prove that wrong. The same PR
<https://github.com/openscad/openscad/pull/4478> also contained `module
references`. Something that sounded extremely useful to me since that would
make name scoping of libraries a lot simpler. It would theoretically allow
something like this `bosl2= use <BOSL2/std.scad>` in the future (not planned).
So this is what is in OEP8. module literals / module references new expression
component module (<params>) { <body> } yields module reference. module
reference is just a value, can put in variable, put in array, pass as
argument, return from function, et cetera. call as m(args) a[i](args)
o.m(args) (expr)(args) or combinations, e.g. a[i].m(args) for an array of
objects with a member that is a module reference. It will allow code like
this. small = module() cube(10); big = module() cube(100); (s ? small :
big)(); v = [ small, big]; v[1](); function foo(w) = w = "c" ? module()
cube(5) : w = "s" ? module() sphere(5) : undef; This will enable calling a
module from a function which is a pretty big change. Literal modules are now
values and can be used anywhere an expression can be used. I.e. they can
actually render from a function. (I expect this will give some issues before
this works perfectly because ordering between functions/modules is a bit odd
in OpenSCAD.) When a module is instantiated from an expression, its value will
be undef. Should I work on this? Peter

![](https://www.gravatar.com/avatar/095124c1792024c67a3336fc575ec4a6?d=blank&s=100)

NH

nop head

Fri, Aug 22, 2025 3:31 PM

I don't see how module references allows name scoping of libraries. A  
library isn't a module.

And I don't think modules should be called from functions. Reference can be  
returned from a function but modules can only be called by statements so I  
expect module reference can only be invoked in statements.

On Fri, 22 Aug 2025 at 15:42, Peter Kriens via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

The OEP8  
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is  
the source for the object() and the $this saga. I thought this was  
extensively discussed looking at the discussions in the PR but I guess the  
current discussions prove that wrong.

The same PR <https://github.com/openscad/openscad/pull/4478> also  
contained `module references`. Something that sounded extremely useful to  
me since that would make name scoping of libraries a lot simpler. It would  
theoretically allow something like this `bosl2= use <BOSL2/std.scad>` in  
the future (not planned).

So this is what is in OEP8.

    
    
    -
    
    module literals / module references
    - new expression component module (<params>) { <body> } yields module
       reference.
       - module reference is just a value, can put in variable, put in
       array, pass as argument, return from function, et cetera.
       - call as
          - m(args)
          - a[i](args)
          - o.m(args)
          - (expr)(args)
          - or combinations, e.g. a[i].m(args) for an array of objects
          with a member that is a module reference.
    

It will allow code like this.

small = module() cube(10);  
big = module() cube(100);  
(s ? small : big)();  
v = [ small, big];  
v[1]();  
function foo(w) =  
w = "c" ? module() cube(5)  
: w = "s" ? module() sphere(5)  
: undef;

This will enable calling a module from a function which is a pretty big  
change. Literal modules are now values and can be used anywhere an  
expression can be used. I.e. they can actually render from a function. (I  
expect this will give some issues before this works perfectly because  
ordering between functions/modules is a bit odd in OpenSCAD.)

When a module is instantiated from an expression, its value will be undef.

Should I work on this?

Peter

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I don't see how module references allows name scoping of libraries. A library
isn't a module. And I don't think modules should be called from functions.
Reference can be returned from a function but modules can only be called by
statements so I expect module reference can only be invoked in statements. On
Fri, 22 Aug 2025 at 15:42, Peter Kriens via Discuss <
discuss@lists.openscad.org> wrote: > The OEP8 >
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is > the source for the object() and the $this
saga. I thought this was > extensively discussed looking at the discussions in
the PR but I guess the > current discussions prove that wrong. > > The same PR
<https://github.com/openscad/openscad/pull/4478> also > contained `module
references`. Something that sounded extremely useful to > me since that would
make name scoping of libraries a lot simpler. It would > theoretically allow
something like this `bosl2= use <BOSL2/std.scad>` in > the future (not
planned). > > So this is what is in OEP8. > > > \- > > module literals /
module references > \- new expression component module (<params>) { <body> }
yields module > reference. > \- module reference is just a value, can put in
variable, put in > array, pass as argument, return from function, et cetera. >
\- call as > \- m(args) > \- a[i](args) > \- o.m(args) > \- (expr)(args) > \-
or combinations, e.g. a[i].m(args) for an array of objects > with a member
that is a module reference. > > It will allow code like this. > > small =
module() cube(10); > big = module() cube(100); > (s ? small : big)(); > v = [
small, big]; > v[1](); > function foo(w) = > w = "c" ? module() cube(5) > : w
= "s" ? module() sphere(5) > : undef; > > > This will enable calling a module
from a function which is a pretty big > change. Literal modules are now values
and can be used anywhere an > expression can be used. I.e. they can actually
render from a function. (I > expect this will give some issues before this
works perfectly because > ordering between functions/modules is a bit odd in
OpenSCAD.) > > When a module is instantiated from an expression, its value
will be undef. > > Should I work on this? > > Peter > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Fri, Aug 22, 2025 3:55 PM

Calling modules from functions sure would make debugging easier. I can’t  
think of any other use for it at the moment. And it does seem like it  
raises complications associated with execution order. The utility of  
module references in general is not obvious to me.

The feature that seems like a huge one to me is the one that lets us get  
geometry data in user space. Then libraries can actually do interesting  
stuff to things created using the native geometry capability.

On Fri, Aug 22, 2025 at 11:31 nop head via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I don't see how module references allows name scoping of libraries. A  
library isn't a module.

And I don't think modules should be called from functions. Reference can  
be returned from a function but modules can only be called by statements so  
I expect module reference can only be invoked in statements.

On Fri, 22 Aug 2025 at 15:42, Peter Kriens via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

The OEP8  
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is  
the source for the object() and the $this saga. I thought this was  
extensively discussed looking at the discussions in the PR but I guess the  
current discussions prove that wrong.

The same PR <https://github.com/openscad/openscad/pull/4478> also  
contained `module references`. Something that sounded extremely useful to  
me since that would make name scoping of libraries a lot simpler. It would  
theoretically allow something like this `bosl2= use <BOSL2/std.scad>` in  
the future (not planned).

So this is what is in OEP8.

    
    
    -
    
    module literals / module references
    - new expression component module (<params>) { <body> } yields module
       reference.
       - module reference is just a value, can put in variable, put in
       array, pass as argument, return from function, et cetera.
       - call as
          - m(args)
          - a[i](args)
          - o.m(args)
          - (expr)(args)
          - or combinations, e.g. a[i].m(args) for an array of objects
          with a member that is a module reference.
    

It will allow code like this.

small = module() cube(10);  
big = module() cube(100);  
(s ? small : big)();  
v = [ small, big];  
v[1]();  
function foo(w) =  
w = "c" ? module() cube(5)  
: w = "s" ? module() sphere(5)  
: undef;

This will enable calling a module from a function which is a pretty big  
change. Literal modules are now values and can be used anywhere an  
expression can be used. I.e. they can actually render from a function. (I  
expect this will give some issues before this works perfectly because  
ordering between functions/modules is a bit odd in OpenSCAD.)

When a module is instantiated from an expression, its value will be undef.

Should I work on this?

Peter

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Calling modules from functions sure would make debugging easier. I can’t think
of any other use for it at the moment. And it does seem like it raises
complications associated with execution order. The utility of module
references in general is not obvious to me. The feature that seems like a huge
one to me is the one that lets us get geometry data in user space. Then
libraries can actually do interesting stuff to things created using the native
geometry capability. On Fri, Aug 22, 2025 at 11:31 nop head via Discuss <
discuss@lists.openscad.org> wrote: > I don't see how module references allows
name scoping of libraries. A > library isn't a module. > > And I don't think
modules should be called from functions. Reference can > be returned from a
function but modules can only be called by statements so > I expect module
reference can only be invoked in statements. > > On Fri, 22 Aug 2025 at 15:42,
Peter Kriens via Discuss < > discuss@lists.openscad.org> wrote: > >> The OEP8
>>
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is >> the source for the object() and the
$this saga. I thought this was >> extensively discussed looking at the
discussions in the PR but I guess the >> current discussions prove that wrong.
>> >> The same PR <https://github.com/openscad/openscad/pull/4478> also >>
contained `module references`. Something that sounded extremely useful to >>
me since that would make name scoping of libraries a lot simpler. It would >>
theoretically allow something like this `bosl2= use <BOSL2/std.scad>` in >>
the future (not planned). >> >> So this is what is in OEP8. >> >> >> \- >> >>
module literals / module references >> \- new expression component module
(<params>) { <body> } yields module >> reference. >> \- module reference is
just a value, can put in variable, put in >> array, pass as argument, return
from function, et cetera. >> \- call as >> \- m(args) >> \- a[i](args) >> \-
o.m(args) >> \- (expr)(args) >> \- or combinations, e.g. a[i].m(args) for an
array of objects >> with a member that is a module reference. >> >> It will
allow code like this. >> >> small = module() cube(10); >> big = module()
cube(100); >> (s ? small : big)(); >> v = [ small, big]; >> v[1](); >>
function foo(w) = >> w = "c" ? module() cube(5) >> : w = "s" ? module()
sphere(5) >> : undef; >> >> >> This will enable calling a module from a
function which is a pretty big >> change. Literal modules are now values and
can be used anywhere an >> expression can be used. I.e. they can actually
render from a function. (I >> expect this will give some issues before this
works perfectly because >> ordering between functions/modules is a bit odd in
OpenSCAD.) >> >> When a module is instantiated from an expression, its value
will be undef. >> >> Should I work on this? >> >> Peter >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/095124c1792024c67a3336fc575ec4a6?d=blank&s=100)

NH

nop head

Fri, Aug 22, 2025 4:00 PM

Model references would be useful so an object can have member modules as  
well as functions.

On Fri, 22 Aug 2025, 16:55 Adrian Mariano via Discuss, <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

Calling modules from functions sure would make debugging easier. I can’t  
think of any other use for it at the moment. And it does seem like it  
raises complications associated with execution order. The utility of  
module references in general is not obvious to me.

The feature that seems like a huge one to me is the one that lets us get  
geometry data in user space. Then libraries can actually do interesting  
stuff to things created using the native geometry capability.

On Fri, Aug 22, 2025 at 11:31 nop head via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I don't see how module references allows name scoping of libraries. A  
library isn't a module.

And I don't think modules should be called from functions. Reference can  
be returned from a function but modules can only be called by statements so  
I expect module reference can only be invoked in statements.

On Fri, 22 Aug 2025 at 15:42, Peter Kriens via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

The OEP8  
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is  
the source for the object() and the $this saga. I thought this was  
extensively discussed looking at the discussions in the PR but I guess the  
current discussions prove that wrong.

The same PR <https://github.com/openscad/openscad/pull/4478> also  
contained `module references`. Something that sounded extremely useful to  
me since that would make name scoping of libraries a lot simpler. It would  
theoretically allow something like this `bosl2= use <BOSL2/std.scad>` in  
the future (not planned).

So this is what is in OEP8.

    
    
    -
    
    module literals / module references
    - new expression component module (<params>) { <body> } yields
       module reference.
       - module reference is just a value, can put in variable, put in
       array, pass as argument, return from function, et cetera.
       - call as
          - m(args)
          - a[i](args)
          - o.m(args)
          - (expr)(args)
          - or combinations, e.g. a[i].m(args) for an array of objects
          with a member that is a module reference.
    

It will allow code like this.

small = module() cube(10);  
big = module() cube(100);  
(s ? small : big)();  
v = [ small, big];  
v[1]();  
function foo(w) =  
w = "c" ? module() cube(5)  
: w = "s" ? module() sphere(5)  
: undef;

This will enable calling a module from a function which is a pretty big  
change. Literal modules are now values and can be used anywhere an  
expression can be used. I.e. they can actually render from a function. (I  
expect this will give some issues before this works perfectly because  
ordering between functions/modules is a bit odd in OpenSCAD.)

When a module is instantiated from an expression, its value will be  
undef.

Should I work on this?

Peter

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

Model references would be useful so an object can have member modules as well
as functions. On Fri, 22 Aug 2025, 16:55 Adrian Mariano via Discuss, <
discuss@lists.openscad.org> wrote: > Calling modules from functions sure would
make debugging easier. I can’t > think of any other use for it at the moment.
And it does seem like it > raises complications associated with execution
order. The utility of > module references in general is not obvious to me. > >
The feature that seems like a huge one to me is the one that lets us get >
geometry data in user space. Then libraries can actually do interesting >
stuff to things created using the native geometry capability. > > On Fri, Aug
22, 2025 at 11:31 nop head via Discuss < > discuss@lists.openscad.org> wrote:
> >> I don't see how module references allows name scoping of libraries. A >>
library isn't a module. >> >> And I don't think modules should be called from
functions. Reference can >> be returned from a function but modules can only
be called by statements so >> I expect module reference can only be invoked in
statements. >> >> On Fri, 22 Aug 2025 at 15:42, Peter Kriens via Discuss < >>
discuss@lists.openscad.org> wrote: >> >>> The OEP8 >>>
<https://github.com/openscad/openscad/wiki/OEP8:-Objects-(dictionaries?),-Geometry-
as-data,-and-Module-References> is >>> the source for the object() and the
$this saga. I thought this was >>> extensively discussed looking at the
discussions in the PR but I guess the >>> current discussions prove that
wrong. >>> >>> The same PR <https://github.com/openscad/openscad/pull/4478>
also >>> contained `module references`. Something that sounded extremely
useful to >>> me since that would make name scoping of libraries a lot
simpler. It would >>> theoretically allow something like this `bosl2= use
<BOSL2/std.scad>` in >>> the future (not planned). >>> >>> So this is what is
in OEP8. >>> >>> >>> \- >>> >>> module literals / module references >>> \- new
expression component module (<params>) { <body> } yields >>> module reference.
>>> \- module reference is just a value, can put in variable, put in >>>
array, pass as argument, return from function, et cetera. >>> \- call as >>>
\- m(args) >>> \- a[i](args) >>> \- o.m(args) >>> \- (expr)(args) >>> \- or
combinations, e.g. a[i].m(args) for an array of objects >>> with a member that
is a module reference. >>> >>> It will allow code like this. >>> >>> small =
module() cube(10); >>> big = module() cube(100); >>> (s ? small : big)(); >>>
v = [ small, big]; >>> v[1](); >>> function foo(w) = >>> w = "c" ? module()
cube(5) >>> : w = "s" ? module() sphere(5) >>> : undef; >>> >>> >>> This will
enable calling a module from a function which is a pretty big >>> change.
Literal modules are now values and can be used anywhere an >>> expression can
be used. I.e. they can actually render from a function. (I >>> expect this
will give some issues before this works perfectly because >>> ordering between
functions/modules is a bit odd in OpenSCAD.) >>> >>> When a module is
instantiated from an expression, its value will be >>> undef. >>> >>> Should I
work on this? >>> >>> Peter >>> >>>
_______________________________________________ >>> OpenSCAD mailing list >>>
To unsubscribe send an email to discuss-leave@lists.openscad.org >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Fri, Aug 22, 2025 5:42 PM

I monitor this list, but not any/all of the PRs, so Peter's observation  
does not surprise me. Whether this is a good thing or not, I am not  
sure. But Peter's getting there only to discover that there is another  
hill to climb is frustrating.

Do we have a clear list of objectives/requirements for this/these new  
feature(s)? Maybe a prioritized list? Not a proposed syntax but  
objectives. Maybe that will help us focus on what is important.

Jon

On 8/22/2025 10:41 AM, Peter Kriens via Discuss wrote:

____

I thought this was extensively discussed looking at the discussions in  
the PR but I guess the current discussions prove that wrong.

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

I monitor this list, but not any/all of the PRs, so Peter's observation does
not surprise me. Whether this is a good thing or not, I am not sure. But
Peter's getting there only to discover that there is another hill to climb is
frustrating. Do we have a clear list of objectives/requirements for this/these
new feature(s)? Maybe a prioritized list? Not a proposed syntax but
objectives. Maybe that will help us focus on what is important. Jon On
8/22/2025 10:41 AM, Peter Kriens via Discuss wrote: > I thought this was
extensively discussed looking at the discussions in > the PR but I guess the
current discussions prove that wrong. \-- This email has been checked for
viruses by AVG antivirus software. www.avg.com

![](https://www.gravatar.com/avatar/1d92d790c6fa6509bcc5cb2148967c53?d=blank&s=100)

V

vulcan_@mac.com

Fri, Aug 22, 2025 9:06 PM

expressions are evaluated before modules,

functions can (currently) only be “called” in an expression

Is intended that module variables, AKA module references, be able to, or even
required to, return a value?

so:

`function apply_module( dataitem, module_var ) =`  
` module_var( dataitem );`

`result = apply_module( 12, module_var=cube );`

My issues and questions are :

  1. the call to “module_var(dataitem)” in the function is itself an expression, yes? so that would mean that module reference will be invoked in the order of evaluation of expressions in the script, before any other module that draw shapes?

  2. module_var() has to return a value that will be passed back as the result of the function call

  3. the call to apply_module causes “cube” to be assigned to the module_var parameter .. or is that not part of OPE8’s intention?

  4. cube() does not return a value so the function call will return ? undef?

  5. can we guarantee that the value for the dataitem argument will already be defined when apply_module is called? in my example the argument is just a literal 12, but in general it could be a variable defined elsewhere, or the result of a method reference being invoked

Or have i missed one or more points in my reading of OPE8

expressions are evaluated before modules, functions can (currently) only be
“called” in an expression Is intended that module variables, AKA module
references, be able to, or even required to, return a value? so: `function
apply_module( dataitem, module_var ) =`\ ` module_var( dataitem );` `result =
apply_module( 12, module_var=cube );` My issues and questions are : 1\. the
call to “module_var(dataitem)” in the function is itself an expression, yes?
so that would mean that module reference will be invoked in the order of
evaluation of expressions in the script, before any other module that draw
shapes? 2\. module_var() has to return a value that will be passed back as the
result of the function call 3\. the call to apply_module causes “cube” to be
assigned to the module_var parameter .. or is that not part of OPE8’s
intention? 4\. cube() does not return a value so the function call will return
? undef? 5\. can we guarantee that the value for the dataitem argument will
already be defined when apply_module is called? in my example the argument is
just a literal 12, but in general it could be a variable defined elsewhere, or
the result of a method reference being invoked Or have i missed one or more
points in my reading of OPE8

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 22, 2025 9:57 PM

On August 22, 2025 5:06:55 PM EDT, vulcan_--- via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

expressions are evaluated before modules,

functions can (currently) only be “called” in an expression

Is intended that module variables, AKA module references, be able to, or even
required to, return a value?

No, that's "geometry as data" or "geom as data" if you want to find the
discussion.

  * Cory

____

so:

`function apply_module( dataitem, module_var ) =`  
` module_var( dataitem );`

`result = apply_module( 12, module_var=cube );`

My issues and questions are :

  1. the call to “module_var(dataitem)” in the function is itself an expression, yes? so that would mean that module reference will be invoked in the order of evaluation of expressions in the script, before any other module that draw shapes?

  2. module_var() has to return a value that will be passed back as the result of the function call

  3. the call to apply_module causes “cube” to be assigned to the module_var parameter .. or is that not part of OPE8’s intention?

  4. cube() does not return a value so the function call will return ? undef?

  5. can we guarantee that the value for the dataitem argument will already be defined when apply_module is called? in my example the argument is just a literal 12, but in general it could be a variable defined elsewhere, or the result of a method reference being invoked

Or have i missed one or more points in my reading of OPE8

On August 22, 2025 5:06:55 PM EDT, vulcan_--- via Discuss
<discuss@lists.openscad.org> wrote: >expressions are evaluated before modules,
> >functions can (currently) only be “called” in an expression > >Is intended
that module variables, AKA module references, be able to, or even required to,
return a value? No, that's "geometry as data" or "geom as data" if you want to
find the discussion. \- Cory > >so: > >`function apply_module( dataitem,
module_var ) =`\ >` module_var( dataitem );` > >`result = apply_module( 12,
module_var=cube );` > >My issues and questions are : > >1\. the call to
“module_var(dataitem)” in the function is itself an expression, yes? so that
would mean that module reference will be invoked in the order of evaluation of
expressions in the script, before any other module that draw shapes? > >2\.
module_var() has to return a value that will be passed back as the result of
the function call > >3\. the call to apply_module causes “cube” to be assigned
to the module_var parameter .. or is that not part of OPE8’s intention? > >4\.
cube() does not return a value so the function call will return ? undef? >
>5\. can we guarantee that the value for the dataitem argument will already be
defined when apply_module is called? in my example the argument is just a
literal 12, but in general it could be a variable defined elsewhere, or the
result of a method reference being invoked > >Or have i missed one or more
points in my reading of OPE8

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sat, Aug 23, 2025 10:57 PM

On 8/22/2025 4:41 PM, Peter Kriens via Discuss wrote:

____

This will enable calling a module from a function which is a pretty  
big change.

Assuming that you're working from my work... No, it does not. Module  
references are values, and can be manipulated and created by functions,  
but they cannot be invoked in expressions.

____

Literal modules are now values and can be used anywhere an expression  
can be used. I.e. they can actually render from a function.

Again, no, they cannot.

____

Should I work on this?

Module references? Sure. Invoking modules from expressions? I  
wouldn't go there.

(Note that PR#4478's geometry values do allow invoking modules from  
expressions; the result is a geometry value. But that's totally  
orthogonal to module references.)

On 8/22/2025 4:41 PM, Peter Kriens via Discuss wrote: > This will enable
calling a module from a function which is a pretty > big change. Assuming that
you're working from my work... No, it does not. Module references are values,
and can be manipulated and created by functions, but they cannot be invoked in
expressions. > Literal modules are now values and can be used anywhere an
expression > can be used. I.e. they can actually render from a function.
Again, no, they cannot. > Should I work on this? Module references? Sure.
Invoking modules from expressions? I wouldn't go there. (Note that PR#4478's
geometry values do allow invoking modules from expressions; the result is a
geometry value. But that's totally orthogonal to module references.)

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sat, Aug 23, 2025 11:07 PM

On 8/22/2025 5:31 PM, nop head via Discuss wrote:

____

I don't see how module references allows name scoping of libraries. A  
library isn't a module.

A library is a collection of functions, modules, and variables.

If you could wrap an entire library up in a single object, you could  
avoid having that library consume global namespace.

For instance, with module references you could do:

    
    
    myLib = object(
         someVar = 5,
         someFunc = function (arg) ... ,
         someMod = module (arg) { ... },
         ...
    );
    

and then you could use myLib.someVar, myLib.someFunc(), and  
myLib.someMod(), without needing to put someVar, someFunc, and someMod  
into the global namespace.

On 8/22/2025 5:31 PM, nop head via Discuss wrote: > I don't see how module
references allows name scoping of libraries. A > library isn't a module. A
library is a collection of functions, modules, and variables. If you could
wrap an entire library up in a single object, you could avoid having that
library consume global namespace. For instance, with module references you
could do: myLib = object( someVar = 5, someFunc = function (arg) ... , someMod
= module (arg) { ... }, ... ); and then you could use myLib.someVar,
myLib.someFunc(), and myLib.someMod(), without needing to put someVar,
someFunc, and someMod into the global namespace.

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sat, Aug 23, 2025 11:20 PM

On 8/22/2025 5:55 PM, Adrian Mariano via Discuss wrote:

____

Calling modules from functions sure would make debugging easier. I  
can’t think of any other use for it at the moment. And it does seem  
like it raises complications associated with execution order.

I've got to think that Peter misunderstood; I think that calling modules  
from functions would be a _lot_ more work than I'd done in PR#4478.

____

The utility of module references in general is not obvious to me.

Module references can be used to allow treating geometry as data, sort  
of. For instance, suppose we're trying to provide a library that lets  
you model a train. You'd like to be able to give the list of cars as an  
array, something like [ locomotive, boxcar, boxcar, coalcar, caboose ].  
Module references let you do that.

Geometry values, which you mention, fill a very similar niche, but are  
both more and less powerful. My model train demo (which uses PR#4478  
features) actually represents its cars as functions that return objects  
that include some metadata and a geometry value for the actual model of  
the car.

I don't think that you actually need module references if you have  
function references and geometry values, but they seem like a good piece  
of symmetry.

____

The feature that seems like a huge one to me is the one that lets us  
get geometry data in user space. Then libraries can actually do  
interesting stuff to things created using the native geometry capability.

Yes, in particular the render() function, which accepts a geometry value  
and returns a list of vertexes and faces (and other metadata) allows all  
sorts of interesting things.

But I already tried bringing in objects, module references, and geometry  
values all at the same time, and it stalled for lack of time for people  
to think about it. I am not optimistic about reviving that all-at-once  
approach, so would prefer to add the features one at a time.

(I did them all at once so that I could satisfy myself that the  
syntactic interactions were workable, and I found that they mostly were.)

On 8/22/2025 5:55 PM, Adrian Mariano via Discuss wrote: > Calling modules from
functions sure would make debugging easier. I > can’t think of any other use
for it at the moment. And it does seem > like it raises complications
associated with execution order. I've got to think that Peter misunderstood; I
think that calling modules from functions would be a *lot* more work than I'd
done in PR#4478. > The utility of module references in general is not obvious
to me. Module references can be used to allow treating geometry as data, sort
of. For instance, suppose we're trying to provide a library that lets you
model a train. You'd like to be able to give the list of cars as an array,
something like [ locomotive, boxcar, boxcar, coalcar, caboose ]. Module
references let you do that. Geometry values, which you mention, fill a very
similar niche, but are both more and less powerful. My model train demo (which
uses PR#4478 features) actually represents its cars as functions that return
objects that include some metadata and a geometry value for the actual model
of the car. I don't think that you actually need module references if you have
function references and geometry values, but they seem like a good piece of
symmetry. > The feature that seems like a huge one to me is the one that lets
us > get geometry data in user space. Then libraries can actually do >
interesting stuff to things created using the native geometry capability. Yes,
in particular the render() function, which accepts a geometry value and
returns a list of vertexes and faces (and other metadata) allows all sorts of
interesting things. But I already tried bringing in objects, module
references, and geometry values all at the same time, and it stalled for lack
of time for people to think about it. I am not optimistic about reviving that
all-at-once approach, so would prefer to add the features one at a time. (I
did them all at once so that I could satisfy myself that the syntactic
interactions were workable, and I found that they mostly were.)

[Next
page](https://lists.openscad.org/empathy/thread/ROFN225UIY6HLFSORJZYYCXJFVYNF5EA?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

